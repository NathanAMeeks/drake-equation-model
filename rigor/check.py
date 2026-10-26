"""Independent check (does NOT import drake_model): recompute N_now per draw from the written formulas + params.yaml,
using direct time-domain convolutions (model uses FFTs), own root finder and own stage-chain solve. Output rigor/check.json"""
import json, math, os, sys, numpy as np, yaml
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); cfg = yaml.safe_load(open(os.path.join(R, "params.yaml")))
assert "drake_model" not in sys.modules
run = cfg["run"]; dt, T = run["dt_gyr"], run["t_now_gyr"]; I = int(round(T / dt)); t = (np.arange(I) + .5) * dt; age = t.copy()
steps = cfg["hard_steps"]; dates = [run["earth_habitable_start_gya"]] + [s["earth_gya"] for s in steps]
edt = np.array([dates[i] - dates[i + 1] for i in range(len(steps))]); iE = int(round(dates[0] / dt))
def geo(tau): q = math.exp(-dt / tau); return (1 - q) * q ** np.arange(I)
def k_of(target, D):   # Newton on log form, independent of model bisection; clamp [-20,20] as documented
    f = lambda k: (D if abs(k) < 1e-12 else math.expm1(k * D) / k) - target
    a, b = -20.0, 20.0
    if f(a) > 0: return a
    if f(b) < 0: return b
    for _ in range(200):
        m = .5 * (a + b); (a, b) = (m, b) if f(m) < 0 else (a, m)
    return .5 * (a + b)
def targets(spec, classes):
    out = []
    for tg in spec.get("applies_to", ["gk", "m"]): out += {"gk": ["K", "G", "F"], "m": ["M"]}.get(tg, [tg])
    return [c for c in out if c in classes]
def one(p, scen):
    sc = cfg["scenarios"][scen]; classes = list(cfg["star_classes"]["classes"]); mpc = cfg["multiphase"]
    Mf = p["m_disk_now"] / (1 - p["return_fraction"]); ts, tq = p["disk_start_gyr"], p["thick_end_gyr"]
    k = k_of((1 - p["f_early_disk_mass"]) * Mf / (p["sfr_now"] * 1e9), T - tq)
    sfr = np.where(t < ts, 0, np.where(t < tq, p["f_early_disk_mass"] * Mf / ((tq - ts) * 1e9), p["sfr_now"] * np.exp(k * (T - t))))
    fZ = 1 / (1 + np.exp(-(t - p["t_metal_gyr"]) / .5))
    act = {n: s for n, s in cfg["multipliers"].items() if "scenarios" not in s or scen.replace("_linked", "") in s["scenarios"] or scen in s["scenarios"]}
    mult = {c: 1.0 for c in classes}; multm = dict(mult)
    for n, s in act.items():
        for c in targets(s, classes):
            mult[c] *= p[n]; multm[c] *= p[n] if s.get("applies_to_exomoons", True) else 1
    for c in classes:
        w = p.get(f"w_similarity_{c}", p.get("w_similarity", 1.0)); mult[c] *= w; multm[c] *= w
    mo, mmo = {}, {}
    for c in classes:
        L = 1.0
        for n in sc.get("ocean_replaces", ["f_land_and_ocean", "f_m_water"]):
            if n in act and c in targets(act[n], classes): L *= p[n]
        Ow = p["f_ocean_world_m"] if c == "M" else p["f_ocean_world_gk"]; r = min(Ow, 1 - L) * p["f_ocean_fecundity"] / L
        mo[c], mmo[c] = mult[c] * r, multm[c] * r
    if "f_superhab" in p:
        f, b = p["f_superhab"], p["superhab_boost"]
        for c in cfg["star_classes"].get("superhab_classes", ["K"]):
            mult[c] = (1 - f) * mult[c] + f * min(mult[c] * b, 1); mo[c] = (1 - f) * mo[c] + f * min(mo[c] * b, 1)
    moon = p.get("f_exomoon_host", 0) * p.get("f_exomoon_habitable", 1)
    base = sfr * 1e9 * dt * p["stars_per_msun"] * p["fp"] * p["f_ghz"] * fZ
    taus = [p["tau_" + s["name"]] for s in steps]; g = np.zeros(I); g[0] = 1
    for tau in taus: g = np.convolve(g, geo(tau))[:I]
    logw = sum(-math.log(x) - e / x for x, e in zip(taus, edt)) - math.log(g[:iE].sum())
    Lg = p["l_stone_yr"] / 1e9
    al = 1 / Lg + p["r_bigfive_per_gyr"] * p["p_bigfive_kills_toolusers"] + p["p_lethal_astro"] * (p["r_grb_per_gyr"] + p["r_sn_per_gyr"]) + p["r_self_per_gyr"]
    S = len(mpc["stages"]); a = [1e9 / p[x] for x in mpc["advance_params"]]; h = [0] + [1e9 * p[x] for x in mpc["hazard_params"]]
    q = p[mpc["regress_fraction_param"]]; A = np.zeros((S, S))
    for s in range(S):     # -Q generator: time-in-state vector solves T (-Q) = e1
        A[s, s] = al + h[s] + (a[s] if s < S - 1 else 0)
        if s < S - 1: A[s, s + 1] = -a[s]
        if s > 0: A[s, s - 1] = -q * h[s]
    Tst = np.linalg.lstsq(A.T, np.eye(S)[0], rcond=None)[0]; al = 1 / Tst.sum()
    be = 1 / (p["m_recurrence"] * taus[-1]); pi = be / (al + be); Lp = 1 / (al + be); c_ = Lp / dt * (1 - math.exp(-dt / Lp))
    K = pi + (1 - pi) * c_ * np.exp(-np.arange(I) * dt / Lp)
    Q = np.convolve(g, K)[:I]
    H = np.cumsum(p["r_ster0_per_gyr"] * sfr / p["sfr_now"] * dt); N = 0.0
    for c in classes:
        d = cfg["star_classes"]["classes"][c]; pen = np.prod([p[x] for x in d.get("penalty_params", [])])
        fs, ne, ng = p[f"f_star_{c}"], p[f"ne_{c}"], p[f"n_giant_hz_{c}"]
        W = Q * (age < p[f"th_{c}_gyr"])
        for m1, m2 in ([(mult[c], multm[c])] + ([(mo[c], mmo[c])] if sc.get("ocean_path") else [])):
            pl = base * fs * (ne * m1 + ng * moon * m2) * pen
            N += (pl * np.exp(H - H[-1]) * W[::-1]).sum()
    return N, logw
def wq(x, w, qs):
    o = np.argsort(x); c = np.cumsum(w[o]); c /= c[-1]; return [float(x[o][np.searchsorted(c, q)]) for q in qs]
def table_support(spec):
    d = spec.get("dist")
    if d in ("uniform", "loguniform"): return float(spec["low"]), float(spec["high"])
    if d == "fixed": return float(spec["value"]), float(spec["value"])
    return None
if __name__ == "__main__":
    out = {}; nsub = int(os.environ.get("NSUB", 1000)); rng = np.random.default_rng(1)
    for scen in sys.argv[1:] or ["nathan_headline_ocean", "baseline_ocean"]:
        Z = np.load(os.path.join(R, "results", f"samples_{scen}.npz")); n = len(Z["r_N_now"])
        idx = rng.choice(n, nsub, replace=False); P = {k[2:]: Z[k] for k in Z.files if k.startswith("p_")}
        rec = np.array([one({k: float(v[i]) for k, v in P.items()}, scen) for i in idx])
        Nm = Z["r_N_now"][idx]; rel = np.abs(rec[:, 0] - Nm) / np.maximum(np.abs(Nm), 1e-300)
        bayes = cfg["scenarios"][scen].get("bayes_update", True) and run.get("bayes_update_on_earth_timing", True)
        lw = Z["r_logw"]; w = np.exp(lw - lw.max()) if bayes else np.ones(n)
        dlw = float(np.max(np.abs(rec[:, 1] - lw[idx]))) if bayes else 0.0
        # supports from table (uniform / loguniform only) -- independent of the model's sampler
        viol = []
        for k, v in P.items():
            sp = cfg["params"].get(k) or cfg["multipliers"].get(k) or cfg["multiphase"]["params"].get(k)
            s = table_support({kk: (float(vv) if isinstance(vv, (int, float, str)) and kk in ("low", "high", "value") else vv) for kk, vv in sp.items()}) if sp else None
            if s and (v.min() < s[0] * (1 - 1e-9) or v.max() > s[1] * (1 + 1e-9)): viol.append(k)
        b = json.load(open(os.path.join(R, "rigor", "bounds_v2.json"))).get(scen, {}).get("bnb")
        own_q = wq(Z["r_N_now"], w, [.1, .5, .9])
        out[scen] = dict(n_checked=nsub, max_rel_err_N=float(rel.max()), median_rel_err_N=float(np.median(rel)),
                         n_rel_err_gt_1em6=int((rel > 1e-6).sum()), max_abs_dlogw=dlw, p10_p50_p90=own_q,
                         support_violations=viol, samples_outside_bounds=(int(((Z["r_N_now"] < b[0]) | (Z["r_N_now"] > b[1])).sum()) if b else None))
        print(scen, out[scen], flush=True)
    json.dump(out, open(os.path.join(R, "rigor", "check.json"), "w"), indent=1)
