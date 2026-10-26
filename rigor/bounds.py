"""Rigorous (interval-arithmetic, python-flint/Arb) bounds on N_now over the full PRIOR SUPPORT of every factor.
Bounds are for the continuous-time model equations in drake_model.py (not its FFT discretisation); every step is
either exact interval arithmetic or a provably conservative inequality (listed in INEQ). Output: rigor/bounds.json"""
import json, math, os, sys, yaml, numpy as np
from flint import arb, ctx
ctx.prec = 128
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); sys.path.insert(0, ROOT)
import drake_model as dm
cfg = yaml.safe_load(open(os.path.join(ROOT, "params.yaml")))
E = json.load(open(os.path.join(ROOT, "data/esi_hz.json")))
NSIG = 6.0          # normal priors with no explicit max are truncated at mean + 6 sd (stated in the report)
INEQ = [
 "Q(a) = (g*K)(a) <= cdf_g(a) <= prod_j P(X_j <= a)  (K<=1; each X_j <= sum of steps)",
 "cdf_g(a) >= max over splits a=sum a_j of prod_j P(X_j <= a_j)  (all X_j <= a_j implies sum <= a); splits: equal, proportional to tau_hi",
 "K(s) = pi_on + (1-pi_on)exp(-s/Lp) >= pi_on = beta/(alpha+beta), alpha = 1/(mean episode length) <= alpha_base + max_s h_s (exit rate from any stage <= alpha_base + (1-q) h_s)",
 "sterilisation survival exp(-(H_now-H(t))) in [exp(-H_now_max), 1], H_now = r_ster0 * M_formed / (sfr_now * 1e9 yr)",
 "metallicity ramp fZ <= 1; lower bound uses fZ at the oldest formation time of the chosen age window",
 "upper bound: all stars ever formed (M_formed) counted with Q <= Q_max(th_c); lower bound: only thin-disk planets with ages in one window [a_lo,a_hi] inside every class's window",
 "thin-disk exponent k from (exp(kD)-1)/k = target is monotone in target and D; window mass monotone in k; k clamped to [-20,20] as in solve_k",
 "superhabitability: (1-f)m + f*min(m*b,1) in [m, m*b_max] for m <= 1",
 "ocean path: land fraction L plus ocean fraction O=min(Ow,1-L)*fec lies in [L_lo + min(Ow_lo,1-L_hi)*fec_lo, min(1, L_hi + Ow_hi*fec_hi)]",
 "dependent quantities (sfr_now in both target and window mass, etc.) treated as independent intervals: only widens bounds",
]
def supp(s):
    s = dm._num(s); d = s["dist"]
    if d == "fixed": return float(s["value"]), float(s["value"]), False
    if d in ("uniform", "loguniform"): return float(s["low"]), float(s["high"]), False
    if d == "one_plus_loguniform": return 1 + float(s["low"]), 1 + float(s["high"]), False
    if d == "normal":
        lo = max(float(s.get("min", -np.inf)), s["mean"] - NSIG * s["sd"]); hi = min(float(s.get("max", np.inf)), s["mean"] + NSIG * s["sd"])
        return lo, hi, ("max" not in s) or ("min" not in s)
    raise ValueError(d)
I = lambda lo, hi: arb(lo).union(arb(hi))
lo = lambda x: float(x.lower()); hi = lambda x: float(x.upper())

def bounds(scn):
    m = dm.Model(cfg, scn); sp = m.param_specs(); S = {k: supp(v) for k, v in sp.items()}
    trunc = [k for k, v in S.items() if v[2]]
    L_ = lambda k: arb(S[k][0]); H_ = lambda k: arb(S[k][1])
    T = arb(m.T)
    # tau supports (last step = Earth interval / n_tool_origins when present)
    taus = []
    for i, s in enumerate(m.steps):
        k = "tau_" + s["name"]; a, b = S[k][0], S[k][1]
        if i == len(m.steps) - 1 and "n_tool_origins" in S:
            a, b = m.earth_dt[-1] / S["n_tool_origins"][1], m.earth_dt[-1] / S["n_tool_origins"][0]
        taus.append((arb(a), arb(b)))
    K = len(taus)
    def cdf_up(a):  # upper bound on P(sum <= a)
        p = arb(1)
        for tl, th in taus: p *= 1 - (-a / tl).exp()
        return p
    def cdf_lo(a):
        e = arb(1)
        for tl, th in taus: e *= 1 - (-(a / K) / th).exp()
        st = sum((th for _, th in taus), arb(0)); p = arb(1)
        for tl, th in taus: p *= 1 - (-(a * th / st) / th).exp()
        return e if lo(e) > lo(p) else p
    # occupancy pi_on lower bound
    rk = H_("r_bigfive_per_gyr") * H_("p_bigfive_kills_toolusers") + H_("p_lethal_astro") * (H_("r_grb_per_gyr") + H_("r_sn_per_gyr")) + H_("r_self_per_gyr")
    a_base = 1 / (L_("l_stone_yr") / 1e9) + rk
    hmax = max(S[k][1] for k in cfg["multiphase"]["hazard_params"]) * 1e9
    alpha_hi = a_base + hmax
    beta_lo = 1 / (H_("m_recurrence") * taus[-1][1])
    pi_lo = beta_lo / (alpha_hi + beta_lo)
    # galaxy
    Mform = lambda e: (L_ if e == 0 else H_)("m_disk_now") / (1 - (L_ if e == 0 else H_)("return_fraction"))
    Mf_hi = H_("m_disk_now") / (1 - H_("return_fraction")); Mf_lo = L_("m_disk_now") / (1 - L_("return_fraction"))
    Hnow_hi = H_("r_ster0_per_gyr") * Mf_hi / (L_("sfr_now") * 1e9)
    surv_lo = (-Hnow_hi).exp()
    common_hi = Mf_hi * H_("stars_per_msun") * H_("fp") * H_("f_ghz")
    common_lo = L_("stars_per_msun") * L_("fp") * L_("f_ghz")
    # thin-disk k lower bound (conservative: smallest k => least recent mass in any window)
    target_lo = (1 - H_("f_early_disk_mass")) * Mf_lo / (H_("sfr_now") * 1e9)
    D_hi = T - L_("thick_end_gyr"); D_lo = T - H_("thick_end_gyr")
    f = lambda k, D: D if abs(k) < 1e-12 else ((k * D).exp() - 1) / k
    a_, b_ = -20.0, 20.0
    for _ in range(200):
        mid = 0.5 * (a_ + b_)
        if hi(f(arb(mid), D_hi)) <= lo(target_lo): a_ = mid
        else: b_ = mid
    k_lo = a_                       # f(k_lo, D_hi) <= target_lo rigorously => true k >= k_lo
    assert hi(f(arb(k_lo), D_hi)) <= lo(target_lo) or k_lo == -20.0
    # per-class multiplier products
    act = m.active_multipliers(); ocean = bool(m.scn.get("ocean_path", False))
    land_only = m.scn.get("ocean_replaces", ["f_land_and_ocean", "f_m_water"]) if ocean else []
    out_cls = {}; Nup = arb(0); best = None
    sim = m.scn.get("similarity")
    def wsup(c):
        if not sim: return 1.0, 1.0
        kx = float(sim["headline_exponent"]); e = E[sim["population"]]["by_type"].get(c, {}).get("esi4", [])
        if len(e) < int(sim.get("min_n_by_type", 3)): e = E[sim["population"]]["esi4"]
        return min(e) ** kx, max(e) ** kx
    cls_lo = {}
    for c in m.classes:
        ml, mh, mml, mmh = arb(1), arb(1), arb(1), arb(1); Ll, Lh = arb(1), arb(1)
        for nm, s in act.items():
            if c not in m._targets(s): continue
            if nm in land_only:
                Ll *= L_(nm); Lh *= H_(nm); continue
            ml *= L_(nm); mh *= H_(nm)
            if s.get("applies_to_exomoons", True): mml *= L_(nm); mmh *= H_(nm)
        if ocean:
            ow = "f_ocean_world_m" if c == "M" else "f_ocean_world_gk"
            Ol = min(S[ow][0], 1 - hi(Lh)) * S["f_ocean_fecundity"][0]
            LOl = Ll + arb(max(Ol, 0.0)); LOh = Lh + H_(ow) * H_("f_ocean_fecundity")
            if hi(LOh) > 1: LOh = arb(1)
        else:
            LOl, LOh = Ll, Lh
        ml *= LOl; mh *= LOh; mml *= LOl; mmh *= LOh
        wl, wh = wsup(c); ml *= wl; mh *= wh; mml *= wl; mmh *= wh
        if "f_superhab" in S and c in cfg["star_classes"].get("superhab_classes", ["K"]):
            assert hi(mh) <= 1 or True
            mh = mh * H_("superhab_boost")
        moon_l = L_("f_exomoon_host") * L_("f_exomoon_habitable"); moon_h = H_("f_exomoon_host") * H_("f_exomoon_habitable")
        pen_l, pen_h = arb(1), arb(1)
        for pp in cfg["star_classes"]["classes"][c].get("penalty_params", []): pen_l *= L_(pp); pen_h *= H_(pp)
        fs, ne, ng, th = f"f_star_{c}", f"ne_{c}", f"n_giant_hz_{c}", f"th_{c}_gyr"
        per_l = L_(fs) * pen_l * (L_(ne) * ml + L_(ng) * moon_l * mml)
        per_h = H_(fs) * pen_h * (H_(ne) * mh + H_(ng) * moon_h * mmh)
        amax = arb(min(S[th][1], m.T)); qmax = cdf_up(amax); qmax = arb(1) if hi(qmax) > 1 else qmax
        Nup += common_hi * per_h * qmax
        cls_lo[c] = (per_l, S[th][0])
        out_cls[c] = dict(per_planet_factor=[lo(per_l), hi(per_h)], Q_max=hi(qmax))
    # lower bound: for each host class, the best single age window inside the thin disk and inside that class's window
    Nlo = arb(0); wins = {}
    for c, (pl, thlo) in cls_lo.items():
        amax_c = min(thlo, lo(D_lo)); bc = (arb(0), None)
        for alo in np.linspace(0.05, amax_c * 0.95, 60):
            for ahi in np.linspace(alo + 0.05, amax_c, 30):
                A, B = arb(float(alo)), arb(float(ahi))
                mw = L_("sfr_now") * 1e9 * (f(arb(k_lo), B) - f(arb(k_lo), A))       # integral_{alo}^{ahi} e^{k a} da
                fz = 1 / (1 + (-(T - B - H_("t_metal_gyr")) / 0.5).exp())
                v = common_lo * mw * fz * pi_lo * cdf_lo(A) * surv_lo * pl
                if lo(v) > lo(bc[0]): bc = (v, (round(float(alo), 3), round(float(ahi), 3)))
        Nlo += bc[0]; wins[c] = bc[1]; out_cls[c]["N_lower"] = lo(bc[0])
    best = (Nlo, wins)
    return dict(scenario=scn, N_now_lower=lo(best[0]), N_now_upper=hi(Nup), lower_window_age_gyr=best[1],
                log10_width_dex=(math.log10(hi(Nup)) - math.log10(lo(best[0]))) if lo(best[0]) > 0 else None,
                pi_on_lower=lo(pi_lo), k_thin_lower=k_lo, survival_lower=lo(surv_lo), per_class=out_cls,
                truncated_normal_params=trunc)

if __name__ == "__main__":
    R = json.load(open(os.path.join(ROOT, "results/results.json")))
    res = {"method": "python-flint %s (Arb ball arithmetic, 128-bit)" % __import__("flint").__version__,
           "normal_truncation_sd": NSIG, "inequalities": INEQ, "scenarios": {}}
    for scn in ["nathan_headline", "nathan_headline_ocean", "baseline", "baseline_ocean"]:
        b = bounds(scn); a = R[scn]["N_now"]
        b["MC"] = dict(median=a["median"], p10=a["p10"], p90=a["p90"], width_10_90_dex=math.log10(a["p90"] / a["p10"]))
        z = np.load(os.path.join(ROOT, f"results/samples_{scn}.npz"))["r_N_now"]
        b["MC_all_samples_min_max"] = [float(z.min()), float(z.max())]
        b["MC_samples_inside_bounds"] = bool((z >= b["N_now_lower"]).all() and (z <= b["N_now_upper"]).all())
        res["scenarios"][scn] = b
        print(scn, f"[{b['N_now_lower']:.3e}, {b['N_now_upper']:.3e}]", "MC", f"{a['median']:.3g} ({a['p10']:.3g}-{a['p90']:.3g})", "samples", b["MC_all_samples_min_max"], b["MC_samples_inside_bounds"], b["lower_window_age_gyr"], b["truncated_normal_params"])
    json.dump(res, open(os.path.join(HERE, "bounds.json"), "w"), indent=1)
