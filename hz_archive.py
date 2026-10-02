"""Count rocky habitable-zone planets in the NASA Exoplanet Archive composite table (pscomppars).
HZ limits: Kopparapu et al. 2014 ApJL 787, L29 (1 Earth-mass coefficients), Seff = S0 + aT + bT^2 + cT^3 + dT^4, T = Teff-5780 K.
Conservative: runaway greenhouse -> maximum greenhouse; optimistic: recent Venus -> early Mars.
"""
import pandas as pd, numpy as np, json, sys
C = {  # S0, a, b, c, d
 "recent_venus": (1.776, 2.136e-4, 2.533e-8, -1.332e-11, -3.097e-15),
 "runaway_gh":   (1.107, 1.332e-4, 1.58e-8, -8.308e-12, -1.931e-15),
 "max_gh":       (0.356, 6.171e-5, 1.698e-9, -3.198e-12, -5.575e-16),
 "early_mars":   (0.32, 5.547e-5, 1.526e-9, -2.874e-12, -5.011e-16)}
def seff(k, teff):
    S0, a, b, c, d = C[k]; T = teff - 5780.0
    return S0 + a*T + b*T**2 + c*T**3 + d*T**4
df = pd.read_csv("data/pscomppars.csv", low_memory=False)
out = {"total_confirmed_rows": int(len(df)), "unique_pl_name": int(df.pl_name.nunique())}
teff = df.st_teff; S = df.pl_insol.copy()
# fill missing insolation from L and a:  S = L/a^2 (L in Lsun from log10)
miss = S.isna() & df.st_lum.notna() & df.pl_orbsmax.notna()
S[miss] = 10**df.st_lum[miss] / df.pl_orbsmax[miss]**2
out["insolation_filled_from_L_a"] = int(miss.sum())
ok = teff.between(2600, 7200) & S.notna()
out["planets_with_Teff_2600_7200_and_insolation"] = int(ok.sum())
rocky = df.pl_rade < 1.8
cons = ok & (S <= seff("runaway_gh", teff)) & (S >= seff("max_gh", teff))
opt = ok & (S <= seff("recent_venus", teff)) & (S >= seff("early_mars", teff))
simple = S.between(0.36, 1.1)   # user's simple flat bounds
out["conservative_HZ_any_size"] = int(cons.sum())
out["conservative_HZ_R_lt_1.8"] = int((cons & rocky).sum())
out["optimistic_HZ_any_size"] = int(opt.sum())
out["optimistic_HZ_R_lt_1.8"] = int((opt & rocky).sum())
out["simple_0.36-1.1_S_R_lt_1.8"] = int((simple & rocky).sum())
out["R_lt_1.8_total"] = int(rocky.sum())
out["missing_radius"] = int(df.pl_rade.isna().sum())
def sptype(t):
    return np.select([t >= 6000, t >= 5200, t >= 3900, t >= 2300], ["F", "G", "K", "M"], "other")
df["sp"] = sptype(teff.fillna(0))
for lab, m in [("conservative", cons & rocky), ("optimistic", opt & rocky)]:
    out[f"{lab}_rocky_by_spectral_type"] = df[m].sp.value_counts().to_dict()
    out[f"{lab}_rocky_names"] = sorted(df[m].pl_name.tolist())
out["transiting_planets_total"] = int((df.tran_flag == 1).sum())
out["discovery_method_counts"] = df.discoverymethod.value_counts().to_dict()
json.dump(out, open("data/hz_counts.json", "w"), indent=1)
for k, v in out.items():
    if not k.endswith("names"): print(k, v)
print("conservative rocky:", out["conservative_rocky_names"])
# sensitivity: hosts cooler than 2600 K (e.g. TRAPPIST-1) evaluated with Teff clamped to 2600 K
tc = teff.clip(lower=2600)
ok2 = teff.between(2300, 7200) & S.notna()
cons2 = ok2 & (S <= seff("runaway_gh", tc)) & (S >= seff("max_gh", tc)) & rocky
opt2 = ok2 & (S <= seff("recent_venus", tc)) & (S >= seff("early_mars", tc)) & rocky
out["conservative_rocky_incl_cool_hosts_clamped"] = int(cons2.sum())
out["optimistic_rocky_incl_cool_hosts_clamped"] = int(opt2.sum())
out["added_by_clamp_conservative"] = sorted(set(df[cons2].pl_name) - set(df[cons & rocky].pl_name))
out["added_by_clamp_optimistic"] = sorted(set(df[opt2].pl_name) - set(df[opt & rocky].pl_name))
out["rocky_radius_from_calculation_count"] = int(df[(opt2)].pl_rade_reflink.astype(str).str.contains("Calculated", case=False).sum()) if "pl_rade_reflink" in df else None
json.dump(out, open("data/hz_counts.json", "w"), indent=1)
print({k: out[k] for k in ["conservative_rocky_incl_cool_hosts_clamped","optimistic_rocky_incl_cool_hosts_clamped","added_by_clamp_conservative","added_by_clamp_optimistic","rocky_radius_from_calculation_count"]})
# HZ giant planets (exomoon hosts): mass > 0.3 M_jup or radius > 6 R_earth
giant = (df.pl_bmassj > 0.3) | (df.pl_rade > 6)
out["conservative_HZ_giants"] = int((cons & giant).sum())
out["optimistic_HZ_giants"] = int((opt & giant).sum())
out["optimistic_HZ_giants_by_type"] = df[opt & giant].sp.value_counts().to_dict()
json.dump(out, open("data/hz_counts.json", "w"), indent=1)
print({k: out[k] for k in ["conservative_HZ_giants","optimistic_HZ_giants","optimistic_HZ_giants_by_type"]})
