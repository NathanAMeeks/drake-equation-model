"""v6: condition the v5 model on 'no alien probe found near Earth' (likelihood weighting, LOCAL analysis only).
For each saved v5 draw the model is re-evaluated (exactly reproduces saved outputs) to get its tool-using history Nt(t).
Spacefaring entries per Gyr:  e(t) = Nt(t) * s_sf * (alpha_raw + h_space)
  s_sf     = share of tool-using worlds in the spacefaring stage, incl. v5 ocean/O2 gates (from N_radio_capable, phi)
  alpha_raw + h_space = total exit rate of the spacefaring stage, so entries = occupancy x exit rate (renewal identity);
  dead civilisations are included because every entry over galactic history is counted.
Each probe-sending civ's exploration wave reaches the Sun T_cross after it starts (Hart 1975; Nicholson & Forgan 2013).
Only arrivals after the Earth-Moon system formed (last 4.5 Gyr) and before now count; optional probe lifetime tau_p [GUESS].
Expected detectable probes  lam = f_send [GUESS] * f_det * sum_t e(t) dt * window * exp(-(t_now - t_arr)/tau_p)
P(no probe found | draw) = exp(-lam); new weight = old weight * exp(-lam)."""
import sys, os, json, numpy as np, yaml
R0 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, R0); os.chdir(R0)
import drake_model as dm, analyze as an
cfg = yaml.safe_load(open("params.yaml"))
SC = ["nathan_headline_ocean_linked_v5", "baseline_ocean_linked_v5"]
TC = {"hart_0.1c": 6.5e5, "hart_settle": 2e6, "nf2013_srp_max": 1e7}      # yr
TAU = {"inf": np.inf, **{f"{v:.0e}": v for v in 10 ** np.arange(2, 10.01, 0.5)}}   # yr, probe lifetime grid (exact in-bin integral)
T_EM = 4.5                                                                  # Gyr, Earth-Moon system age
FSEND = [1e-4, 1e-3, 1e-2, 0.1, 1.0]
FDET = {"solar_system_1e-3": 1e-3, "mars_like_0.1": 0.1, "moon_EM_Lpts_0.5": 0.5}
cache = "results/v6_probe_Etau.npz"   # v6b: lifetime grid, exact exponential integral inside each time bin

def exposures(scen):
    m = dm.Model(cfg, scen); z = np.load(f"results/samples_{scen}.npz")
    n = len(z["r_N_now"]); t = m.t; dt = m.dt; tn = m.T
    keys = [k for k in z.files if k.startswith("p_")]
    E = {f"{a}|{b}": np.zeros(n) for a in TC for b in TAU}
    for i0 in range(0, n, 2000):
        ix = slice(i0, min(n, i0 + 2000)); P = {k[2:]: z[k][ix] for k in keys}
        o, Nt = m.evaluate(P)
        a_raw = 1e9 / P["l_stone_yr"] + (P["r_bigfive_per_gyr"] * P["p_bigfive_kills_toolusers"]
               + P["p_lethal_astro"] * (P["r_grb_per_gyr"] + P["r_sn_per_gyr"]) + P["r_self_per_gyr"])
        ex = a_raw + 1e9 * P["stage_h_space_per_yr"]
        Nn = o["N_now"]; ps, pr = o["phi_spacefaring"], o["phi_radio"]
        s_sf = np.where(Nn > 0, o["N_radio_capable"] / np.where(Nn > 0, Nn, 1), 0) * ps / np.maximum(ps + pr, 1e-300)
        rate = Nt * (s_sf * ex)[:, None]                                   # entries per Gyr
        for a, Tc in TC.items():
            Tg = Tc / 1e9; lo, hi = t - dt / 2, t + dt / 2
            frac = np.clip((np.minimum(hi, tn - Tg) - np.maximum(lo, tn - T_EM - Tg)) / dt, 0, 1)
            s_lo = np.clip(np.maximum(lo, tn - T_EM - Tg), None, tn - Tg); s_hi = np.clip(np.minimum(hi, tn - Tg), None, tn - Tg)
            ok = s_hi > s_lo
            for b, tau in TAU.items():
                if np.isfinite(tau):
                    tg = tau / 1e9   # Gyr; integral of exp(-(tn - Tg - s)/tau) over entry times s in [s_lo, s_hi]
                    k = np.where(ok, tg * (np.exp(-(tn - Tg - s_hi) / tg) - np.exp(-(tn - Tg - s_lo) / tg)), 0.0)
                else:
                    k = frac * dt
                E[f"{a}|{b}"][ix] = (rate * k[None, :]).sum(1)
        print(scen, i0, flush=True)
    return E

if not os.path.exists(cache):
    np.savez_compressed(cache, **{f"{s}#{k}": v for s in SC for k, v in exposures(s).items()})
EZ = np.load(cache)

def summ(z, w):
    rc, nn = z["r_N_radio_capable"], z["r_N_now"]; wn = w / w.sum()
    return dict(radio_median=an.wq(rc, w, .5), radio_p10=an.wq(rc, w, .1), radio_p90=an.wq(rc, w, .9),
                P_radio_lt1=float(wn[rc < 1].sum()), stone_median=an.wq(nn, w, .5), ess=an.ess(w))
SHOW = ["l_stone_yr", "stage_h_space_per_yr", "stage_tau_space_yr", "stage_h_radio_per_yr", "stage_h_ind_per_yr",
        "f_land_and_ocean", "f_plate_tectonics", "r_self_per_gyr", "tau_stone_tool_intelligence", "stage_q_regress"]
out = {"sources": {
  "Hart1975": "https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?1975QJRAS..16..128H&defaultprint=YES&filetype=.pdf",
  "NicholsonForgan2013": "https://arxiv.org/abs/1307.1648", "Bracewell1960": "https://doi.org/10.1038/186670a0",
  "FreitasValdes1980": "https://www.rfreitas.com/Astro/SearchIcarus1980.htm",
  "ValdesFreitas1983": "https://rfreitas.com/Astro/SearchIcarus1983.htm",
  "FreitasValdes1985": "https://ui.adsabs.harvard.edu/abs/1985AcAau..12.1027F/abstract",
  "HaqqMisraKopparapu2012": "https://arxiv.org/abs/1111.1212"},
  "settings": dict(T_cross_yr=TC, tau_probe_yr={k: str(v) for k, v in TAU.items()}, earth_moon_age_gyr=T_EM,
                   f_send=FSEND, f_det=FDET), "scenarios": {}}
for s in SC:
    z = np.load(f"results/samples_{s}.npz"); lw = z["r_logw"]
    w0 = np.exp(lw - np.max(lw[np.isfinite(lw)])); w0[~np.isfinite(w0)] = 0
    D = {"prior": summ(z, w0), "expected_spacefaring_arrivals_median": {k.split("#")[1]: an.wq(EZ[k], w0, .5) for k in EZ.files if k.startswith(s + "#")},
         "sweep": {}, "variants": {}, "pull_dex": {}}
    E = EZ[f"{s}#nf2013_srp_max|inf"]
    for fd_k, fd in FDET.items():
        for fs in FSEND:
            D["sweep"][f"{fd_k}|{fs:g}"] = summ(z, w0 * np.exp(-fs * fd * E))
    for k in EZ.files:
        if k.startswith(s + "#"):
            D["variants"][k.split("#")[1]] = {f"{fp:g}": summ(z, w0 * np.exp(-fp * EZ[k])) for fp in (1e-3, 1e-1)}  # fp = f_send*f_det
    for fp in (1e-3, 1e-1):
        w1 = w0 * np.exp(-fp * E)
        D["pull_dex"][f"{fp:g}"] = {p: float(np.log10(an.wq(z["p_" + p], w1, .5) / an.wq(z["p_" + p], w0, .5)))
                                    for p in SHOW if "p_" + p in z.files}
    out["scenarios"][s] = D

# ---------------- v6b: sourced per-location probe lifetimes (impact + dynamical removal), replacing the guessed lifetimes
def grun(m):   # Grun et al. 1985 cumulative meteoroid flux at 1 AU, impacts per m^2 per yr on a randomly oriented plate (ESA MADWEB form)
    return 3.15576e7 * ((2.2e3 * m ** 0.306 + 15) ** -4.38 + 1.3e-9 * (m + 1e11 * m ** 2 + 1e27 * m ** 4) ** -0.36 + 1.3e-16 * (m + 1e6 * m ** 2) ** -0.85)
M_KILL_G, A_M2 = 1.0, 1.0   # [GUESS] >=1 g (~1 cm stony) at ~20 km/s disables the probe; [MODELED] 1 m^2 cross-section (10 m^2 -> 10x shorter)
TAU_IMP_1AU = 1.0 / (4 * grun(M_KILL_G) * A_M2)    # isotropic flux on a convex body: hits = 4 x plate flux x cross-section
LOC = {   # name: (tau_dyn_yr, heliocentric distance AU for 1/r impact scaling [MODELED, Mann+2004 n ~ r^-1], note)
  "Earth-Moon L4/L5 (searched)": (1e2, 1.0, "Kordylewski-cloud sims: <0.1% of stable paths remain after 100 yr (Celest Mech Dyn Astr 2024)"),
  "Lunar distant retrograde orbit": (7.5e2, 1.0, "stable DROs ~1e4 lunar periods (MNRAS 494, 2727, 2020) = ~750 yr"),
  "Moon surface": (np.inf, 1.0, "no dynamical removal; burial by regolith gardening (Speyerer+2016) not modelled"),
  "Sun-Earth L4/L5, transient (like 2010 TK7)": (2.5e5, 1.0, "2010 TK7 total 1:1 lifetime <0.25 Myr (Dvorak+2012)"),
  "Sun-Earth L4/L5, most stable region": (1e9, 1.0, "MEGASIM: stretched-exponential decay, none left by 2.33 Gyr (ApJ 2022); 1e9 yr used as order of magnitude"),
  "Mars Trojans": (4.5e9, 1.52, "dynamical half-lives ~ age of Solar System (Scholl+2005)"),
  "Main belt (1 m body)": (3.0e10, None, "Yarkovsky removal ~0.03%/Myr; collisional lifetime 14 Myr used for impacts (Bottke+2005)"),
  "Jupiter Trojans": (4.5e9 / 0.26, 5.2, "~23-25% escape over Solar System age (MNRAS 2020, Jovian Trojan stability) -> e-folding ~17 Gyr"),
}
lg = np.log10(np.array([v for v in TAU.values() if np.isfinite(v)])); lk = [k for k, v in TAU.items() if np.isfinite(v)]
def E_at(s, tau, tc="nf2013_srp_max"):   # log-log interpolation on the lifetime grid
    Y = np.log10(np.stack([np.maximum(EZ[f"{s}#{tc}|{k}"], 1e-300) for k in lk]))
    x = np.clip(np.log10(tau), lg[0], lg[-1]); j = min(np.searchsorted(lg, x), len(lg) - 1); i = max(j - 1, 0)
    f = 0 if i == j else (x - lg[i]) / (lg[j] - lg[i]); return 10 ** (Y[i] * (1 - f) + Y[j] * f)
out["v6b_lifetimes"] = {"impact": dict(source="Grun et al. 1985 (ESA MADWEB form); cross-check Brown et al. 2002 N(>D)=37 D^-2.7 per yr on Earth",
                        kill_mass_g=M_KILL_G, cross_section_m2=A_M2, grun_flux_ge_kill_per_m2_yr=grun(M_KILL_G), tau_impact_1AU_yr=TAU_IMP_1AU,
                        tau_impact_1AU_10m2_yr=TAU_IMP_1AU / 10, tau_impact_0p1g_yr=1 / (4 * grun(0.1)), tau_impact_10g_yr=1 / (4 * grun(10.0))), "locations": {}}
PROD = [1e-4, 1e-3, 1e-2, 0.1, 1.0]
for nm, (td, r, note) in LOC.items():
    ti = 1.4e7 if r is None else TAU_IMP_1AU * r
    tl = 1 / (1 / ti + 1 / td)
    out["v6b_lifetimes"]["locations"][nm] = dict(tau_dyn_yr=td, tau_impact_yr=ti, tau_combined_yr=tl, note=note)
    for s in SC:
        z = np.load(f"results/samples_{s}.npz"); lw = z["r_logw"]
        w0 = np.exp(lw - np.max(lw[np.isfinite(lw)])); w0[~np.isfinite(w0)] = 0; E = E_at(s, tl)
        out["scenarios"][s].setdefault("v6b_location_sweep", {})[nm] = dict(arrivals_alive_median=an.wq(E, w0, .5),
            sweep={f"{fp:g}": summ(z, w0 * np.exp(-fp * E)) for fp in PROD})
json.dump(out, open("rigor/v6_probe.json", "w"), indent=1, default=float)

import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
for a, s in zip(ax, SC):
    z = np.load(f"results/samples_{s}.npz"); lw = z["r_logw"]
    w0 = np.exp(lw - np.max(lw[np.isfinite(lw)])); w0[~np.isfinite(w0)] = 0
    x = np.log10(np.clip(z["r_N_radio_capable"], 1e-12, None)); b = np.linspace(-12, 8, 81)
    cur = [("before (v5)", None, "k"), ("persist forever", np.inf, "C3")] + [(nm, out["v6b_lifetimes"]["locations"][nm]["tau_combined_yr"], c)
           for nm, c in (("Earth-Moon L4/L5 (searched)", "C2"), ("Sun-Earth L4/L5, transient (like 2010 TK7)", "C1"), ("Jupiter Trojans", "C0"))]
    for lab, tau, c in cur:
        wt = w0 if tau is None else w0 * np.exp(-1.0 * (EZ[f"{s}#nf2013_srp_max|inf"] if not np.isfinite(tau) else E_at(s, tau)))
        a.hist(x, b, weights=wt, density=True, histtype="step", color=c, lw=1.5, label=lab if tau is None else f"{lab} ({tau:.1e} yr)")
    a.axvline(0, color="gray", ls=":"); a.set_title(s); a.set_xlabel("log10 radio-or-better civilizations now"); a.legend(fontsize=7)
fig.suptitle("v6b: no-probe conditioning with sourced probe lifetimes, f_send x f_det = 1 (T_cross 1e7 yr)")
fig.tight_layout(); fig.savefig("rigor/v6b_probe.png", dpi=120)
print("done")
