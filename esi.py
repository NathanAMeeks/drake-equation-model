"""Earth Similarity Index (ESI) for NASA Exoplanet Archive HZ rocky planets.
Primary: Schulze-Makuch et al. 2011 (Astrobiology 11, 1041) 4-property ESI
    ESI = prod_i (1 - |x_i - x_i0| / (x_i + x_i0)) ** (w_i / n),   n = 4
    radius w=0.57, bulk density w=1.07, escape velocity w=0.70, surface temperature w=5.58 (ref 288 K)
    (reference values / weights: PHL table, https://phl.upr.edu/projects/earth-similarity-index-esi)
  inputs: R = pl_rade; M = pl_bmasse (Archive; may be M-R-relation or Msini, flagged); density = M/R^3,
          v_esc = sqrt(M/R) (Earth units); T_surf = 288 K * S^0.25 (ASSUMPTION: Earth-like albedo+greenhouse,
          i.e. temperature similarity is driven by insolation only; no exoplanet surface temperatures are measured).
          Missing mass or mass given only as an upper limit (pl_bmasselim=1) -> Chen & Kipping 2017 Terran relation M = R^(1/0.279).
Cross-check: PHL Habitable Worlds Catalog flux-radius form ESI_S = 1 - sqrt(0.5*[((S-1)/(S+1))^2 + ((R-1)/(R+1))^2]).
HZ definitions identical to hz_archive.py (Kopparapu+2014; Teff clamped to >=2600 K for cooler hosts such as TRAPPIST-1).
"""
import json, numpy as np, pandas as pd
C = {"recent_venus": (1.776, 2.136e-4, 2.533e-8, -1.332e-11, -3.097e-15),
     "runaway_gh": (1.107, 1.332e-4, 1.58e-8, -8.308e-12, -1.931e-15),
     "max_gh": (0.356, 6.171e-5, 1.698e-9, -3.198e-12, -5.575e-16),
     "early_mars": (0.32, 5.547e-5, 1.526e-9, -2.874e-12, -5.011e-16)}
def seff(k, teff):
    S0, a, b, c, d = C[k]; T = teff - 5780.0
    return S0 + a*T + b*T**2 + c*T**3 + d*T**4
W = {"R": 0.57, "rho": 1.07, "vesc": 0.70, "T": 5.58}
def sim(x, x0): return 1 - np.abs(x - x0) / (x + x0)
def esi4(R, M, S):
    rho = M / R**3; v = np.sqrt(M / R); T = 288.0 * S**0.25
    return (sim(R, 1)**(W["R"]/4) * sim(rho, 1)**(W["rho"]/4) * sim(v, 1)**(W["vesc"]/4) * sim(T, 288.0)**(W["T"]/4))
def esi_phl(R, S): return 1 - np.sqrt(0.5 * (((S-1)/(S+1))**2 + ((R-1)/(R+1))**2))

if __name__ == "__main__":
    df = pd.read_csv("data/pscomppars.csv", low_memory=False)
    teff = df.st_teff; S = df.pl_insol.copy()
    miss = S.isna() & df.st_lum.notna() & df.pl_orbsmax.notna()
    S[miss] = 10**df.st_lum[miss] / df.pl_orbsmax[miss]**2
    tc = teff.clip(lower=2600); ok = teff.between(2300, 7200) & S.notna()
    rocky = df.pl_rade < 1.8
    cons = ok & (S <= seff("runaway_gh", tc)) & (S >= seff("max_gh", tc)) & rocky
    opt = ok & (S <= seff("recent_venus", tc)) & (S >= seff("early_mars", tc)) & rocky
    M = df.pl_bmasse.copy(); mprov = df.pl_bmassprov.fillna("none").copy()
    nm = (M.isna() | (df.pl_bmasselim == 1)) & df.pl_rade.notna()   # missing mass OR mass is only an upper limit
    M[nm] = df.pl_rade[nm] ** (1 / 0.279); mprov[nm] = "Chen&Kipping2017 (this script)"
    df = df.copy(); df["S"] = S; df["M_used"] = M; df["mass_source"] = mprov
    df["ESI4"] = esi4(df.pl_rade, M, S); df["ESI_PHL_SR"] = esi_phl(df.pl_rade, S)
    df["T_surf_assumed_K"] = 288.0 * S**0.25
    out = {}
    cols = ["pl_name", "hostname", "st_teff", "sy_dist", "pl_rade", "M_used", "mass_source", "S", "T_surf_assumed_K", "ESI4", "ESI_PHL_SR", "discoverymethod"]
    for lab, m in [("conservative", cons), ("optimistic", opt)]:
        d = df[m].sort_values("ESI4", ascending=False)
        e = d.ESI4.values
        out[lab] = dict(n=int(len(d)), esi4=[float(x) for x in e], esi_phl=[float(x) for x in d.ESI_PHL_SR.values],
                        names=d.pl_name.tolist(),
                        mean=float(e.mean()), median=float(np.median(e)), min=float(e.min()), max=float(e.max()),
                        frac_ge_0p8=float((e >= 0.8).mean()),
                        mean_pow={str(k): float((e**k).mean()) for k in [1, 2, 3, 5, 10]},
                        mass_source_counts=d.mass_source.value_counts().to_dict())
        d[cols].to_csv(f"data/esi_hz_rocky_{lab}.csv", index=False)
    json.dump(out, open("data/esi_hz.json", "w"), indent=1)
    for lab in out:
        o = out[lab]; print(lab, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in o.items() if k not in ("esi4", "esi_phl", "names")})
    d = df[opt].sort_values("ESI4", ascending=False)
    pd.set_option("display.width", 250)
    print(d[cols].head(15).round(3).to_string(index=False))
    print("Earth check ESI4(1,1,1) =", esi4(np.array(1.0), np.array(1.0), np.array(1.0)), " Mars(R .532, M .107, S .431) =", esi4(np.array(.532), np.array(.107), np.array(.431)))
