"""Rigorous interval bound engine (python-flint/Arb). bound(m, box) -> (lower, upper) on N_now for parameter box
{name: (lo, hi)}. v2 (2026-10-19): exact hypoexponential CDF at the monotone corner, occupancy kernel K(a) floor
instead of pi_on alone, coarse window search. All steps rigorous for the continuous-time model equations."""
import json, math, os, sys, numpy as np
from flint import arb, ctx
ctx.prec = 160
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ROOT)
import drake_model as dm
E = json.load(open(os.path.join(ROOT, "data/esi_hz.json")))
NSIG = 6.0
lo = lambda x: float(x.lower()); hi = lambda x: float(x.upper())

def supp(s):
    s = dm._num(s); d = s["dist"]
    if d == "fixed": return float(s["value"]), float(s["value"])
    if d in ("uniform", "loguniform"): return float(s["low"]), float(s["high"])
    if d == "one_plus_loguniform": return 1 + float(s["low"]), 1 + float(s["high"])
    if d == "normal": return max(float(s.get("min", -np.inf)), s["mean"] - NSIG * s["sd"]), min(float(s.get("max", np.inf)), s["mean"] + NSIG * s["sd"])
    raise ValueError(d)

def median(s):
    s = dm._num(s); d = s["dist"]
    if d == "fixed": return float(s["value"])
    if d == "uniform": return 0.5 * (s["low"] + s["high"])
    if d == "loguniform": return math.sqrt(s["low"] * s["high"])
    if d == "one_plus_loguniform": return 1 + math.sqrt(s["low"] * s["high"])
    if d == "normal": return float(s["mean"])
    raise ValueError(d)

def full_box(m):
    box = {k: supp(v) for k, v in m.param_specs().items()}
    sim = m.scn.get("similarity")
    for c in m.classes:   # similarity weight per class: bootstrap mean of ESI^k lies in [min, max] of the list used
        if sim:
            kx = float(sim["headline_exponent"]); e = E[sim["population"]]["by_type"].get(c, {}).get("esi4", [])
            if len(e) < int(sim.get("min_n_by_type", 3)): e = E[sim["population"]]["esi4"]
            box[f"w_similarity_{c}"] = (min(e) ** kx, max(e) ** kx)
        else: box[f"w_similarity_{c}"] = (1.0, 1.0)
    if "n_tool_origins" in box:
        a, b = box["n_tool_origins"]; nm = "tau_" + m.steps[-1]["name"]
        box[nm] = (m.earth_dt[-1] / b, m.earth_dt[-1] / a)
    return box

def hypo_cdf(a, rates):
    """P(sum of independent Exp(rate_j) <= a); exact (distinct rates) or Erlang (all equal)."""
    r = [arb(x) for x in rates]
    if max(rates) - min(rates) <= 1e-12 * max(rates):
        lam = r[0]; s = arb(0); term = arb(1)
        for k in range(len(r)):
            s += term; term = term * lam * a / (k + 1)
        return 1 - (-lam * a).exp() * s
    if len(set(rates)) < len(rates): return None
    tot = arb(0)
    for j, lj in enumerate(r):
        c = arb(1)
        for k, lk in enumerate(r):
            if k != j: c *= lk / (lk - lj)
        tot += c * (-lj * a).exp()
    return 1 - tot

def cdf_lo(a, taus_hi):
    v = hypo_cdf(a, [1 / t for t in taus_hi])
    if v is None: v = hypo_cdf(a, [1 / max(taus_hi)] * len(taus_hi))   # all at the largest tau: stochastically larger sum
    return arb(max(lo(v), 0.0))

def cdf_up(a, taus_lo):
    v = hypo_cdf(a, [1 / t for t in taus_lo])
    if v is None: v = hypo_cdf(a, [1 / min(taus_lo)] * len(taus_lo))
    return arb(min(hi(v), 1.0))

def bound(m, box, cfg, nwin=(10, 6)):
    L_ = lambda k: arb(box[k][0]); H_ = lambda k: arb(box[k][1]); T = arb(m.T)
    taus = [box["tau_" + s["name"]] for s in m.steps]
    rk_hi = H_("r_bigfive_per_gyr") * H_("p_bigfive_kills_toolusers") + H_("p_lethal_astro") * (H_("r_grb_per_gyr") + H_("r_sn_per_gyr")) + H_("r_self_per_gyr")
    # mean episode length >= expected time in stage 1 (lithic has no extra hazard; it is left only by advancing at rate
    # 1/tau_agri or by the baseline end rate) => effective end rate <= alpha_base + min(max_s h_s, 1/tau_agri_min)
    a1 = 1e9 / box[cfg["multiphase"]["advance_params"][0]][0]
    a_hi = 1 / (L_("l_stone_yr") / 1e9) + rk_hi + min(max(box[k][1] for k in cfg["multiphase"]["hazard_params"]) * 1e9, a1)
    b_lo = 1 / (H_("m_recurrence") * arb(taus[-1][1])); b_hi = 1 / (L_("m_recurrence") * arb(taus[-1][0]))
    pi_lo = b_lo / (a_hi + b_lo)
    Mf_hi = H_("m_disk_now") / (1 - H_("return_fraction")); Mf_lo = L_("m_disk_now") / (1 - L_("return_fraction"))
    surv_lo = (-(H_("r_ster0_per_gyr") * Mf_hi / (L_("sfr_now") * 1e9))).exp()
    common_hi = Mf_hi * H_("stars_per_msun") * H_("fp") * H_("f_ghz"); common_lo = L_("stars_per_msun") * L_("fp") * L_("f_ghz")
    target_lo = (1 - H_("f_early_disk_mass")) * Mf_lo / (H_("sfr_now") * 1e9)
    D_hi = T - L_("thick_end_gyr"); D_lo = T - H_("thick_end_gyr")
    f = lambda k, D: D if abs(k) < 1e-12 else ((k * D).exp() - 1) / k
    ka, kb = -20.0, 20.0
    for _ in range(100):
        mid = 0.5 * (ka + kb)
        if hi(f(arb(mid), D_hi)) <= lo(target_lo): ka = mid
        else: kb = mid
    act = m.active_multipliers(); ocean = bool(m.scn.get("ocean_path", False))
    land_only = m.scn.get("ocean_replaces", ["f_land_and_ocean", "f_m_water"]) if ocean else []
    Nup, Nlo = arb(0), arb(0)
    for c in m.classes:
        ml, mh, mml, mmh, Ll, Lh = (arb(1),) * 6
        for nm, s in act.items():
            if c not in m._targets(s): continue
            if nm in land_only: Ll *= L_(nm); Lh *= H_(nm); continue
            ml *= L_(nm); mh *= H_(nm)
            if s.get("applies_to_exomoons", True): mml *= L_(nm); mmh *= H_(nm)
        if ocean:
            ow = "f_ocean_world_m" if c == "M" else "f_ocean_world_gk"
            Ol = max(min(box[ow][0], 1 - hi(Lh)), 0.0) * box["f_ocean_fecundity"][0]
            LOl = Ll + arb(Ol); LOh = Lh + H_(ow) * H_("f_ocean_fecundity")
            if hi(LOh) > 1: LOh = arb(1)
        else: LOl, LOh = Ll, Lh
        w = box[f"w_similarity_{c}"]
        ml *= LOl * w[0]; mh *= LOh * w[1]; mml *= LOl * w[0]; mmh *= LOh * w[1]
        if "f_superhab" in box and c in cfg["star_classes"].get("superhab_classes", ["K"]): mh = mh * H_("superhab_boost")
        moon_l = L_("f_exomoon_host") * L_("f_exomoon_habitable"); moon_h = H_("f_exomoon_host") * H_("f_exomoon_habitable")
        pen_l, pen_h = arb(1), arb(1)
        for pp in cfg["star_classes"]["classes"][c].get("penalty_params", []): pen_l *= L_(pp); pen_h *= H_(pp)
        fs, ne, ng, th = f"f_star_{c}", f"ne_{c}", f"n_giant_hz_{c}", f"th_{c}_gyr"
        per_l = L_(fs) * pen_l * (L_(ne) * ml + L_(ng) * moon_l * mml)
        per_h = H_(fs) * pen_h * (H_(ne) * mh + H_(ng) * moon_h * mmh)
        Nup += common_hi * per_h * cdf_up(arb(min(box[th][1], m.T)), [t[0] for t in taus])
        amax = min(box[th][0], lo(D_lo)); best = 0.0
        for alo in np.linspace(0.05, amax * 0.95, nwin[0]):
            for ahi in np.linspace(alo + 0.05, amax, nwin[1]):
                A, B = arb(float(alo)), arb(float(ahi))
                mw = L_("sfr_now") * 1e9 * (f(arb(ka), B) - f(arb(ka), A))
                fz = 1 / (1 + (-(T - B - H_("t_metal_gyr")) / 0.5).exp())
                Ea = (-A * (a_hi + b_hi)).exp()                     # K(a) >= Ea + pi_lo (1 - Ea), K decreasing in age
                q = cdf_lo(A, [t[1] for t in taus]) * (Ea + pi_lo * (1 - Ea))
                v = lo(common_lo * mw * fz * q * surv_lo * per_l)
                best = max(best, v)
        Nlo += arb(best)
    return lo(Nlo), hi(Nup)
