"""Superhabitability screen of NASA Exoplanet Archive planets (pscomppars) after Schulze-Makuch, Heller & Guinan 2020
(Astrobiology 20, 1394; Table 2 'Most Valuable Planets'): K-dwarf host; ~5-8 Gyr old; up to ~1.5 M_earth and ~10% larger than Earth;
mean surface temperature ~5 C above Earth's (their candidate screen: within 10 deg of an optimal 19 C); plus criteria not observable
(O2 25-30%, shallow-water archipelagos, large moon, plate tectonics, magnetic field).
Operational criteria used here (labelled):
  host_K      : 3900 <= Teff < 5200 K (same split as hz_archive.py)
  size_user   : 1.0 <= R <= 1.5 R_earth (user's '~1.0-1.5'); size_strict: 1.0 <= R <= 1.2 and M <= 1.5 M_earth (paper: ~10% larger, <=1.5 M_earth)
  temp        : T_surf = 288 K * S^0.25 (ASSUMED Earth albedo+greenhouse, as in esi.py) within 282-302 K (19 C +/- 10 K)
  age         : 5 <= st_age <= 8 Gyr (Archive stellar age; often missing / very uncertain)
  hz          : Kopparapu+2014 optimistic HZ, Teff clamped >= 2600 K
Also cross-matches the KOIs legible in the paper's Fig. 2 against the Archive KOI cumulative table (data/smh2020_kois.csv).
"""
import json, numpy as np, pandas as pd
from esi import seff, esi4
df = pd.read_csv("data/pscomppars.csv", low_memory=False)
teff = df.st_teff; S = df.pl_insol.copy()
miss = S.isna() & df.st_lum.notna() & df.pl_orbsmax.notna(); S[miss] = 10**df.st_lum[miss] / df.pl_orbsmax[miss]**2
tc = teff.clip(lower=2600); ok = teff.between(2300, 7200) & S.notna()
hz = ok & (S <= seff("recent_venus", tc)) & (S >= seff("early_mars", tc))
M = df.pl_bmasse.where(df.pl_bmasselim != 1)
M = M.fillna(df.pl_rade ** (1 / 0.279))
T = 288.0 * S ** 0.25
crit = pd.DataFrame({
    "hz": hz, "host_K": teff.between(3900, 5199.9), "size_user": df.pl_rade.between(1.0, 1.5),
    "size_strict": df.pl_rade.between(1.0, 1.2) & (M <= 1.5), "temp": T.between(282, 302),
    "age_5_8": df.st_age.between(5, 8), "age_known": df.st_age.notna()})
out = {"n_hz_R_lt_2": int((hz & (df.pl_rade < 2)).sum())}
base = crit.hz & (df.pl_rade < 2)
for k in ["host_K", "size_user", "size_strict", "temp", "age_5_8", "age_known"]:
    out[f"hz_R<2 & {k}"] = int((base & crit[k]).sum())
combos = {
    "K + size_user": base & crit.host_K & crit.size_user,
    "K + size_user + temp": base & crit.host_K & crit.size_user & crit.temp,
    "K + size_user + age": base & crit.host_K & crit.size_user & crit.age_5_8,
    "K + temp + age (paper's three broad criteria)": base & crit.host_K & crit.temp & crit.age_5_8,
    "K + size_user + temp + age": base & crit.host_K & crit.size_user & crit.temp & crit.age_5_8,
    "K + size_strict + temp + age": base & crit.host_K & crit.size_strict & crit.temp & crit.age_5_8}
cols = ["pl_name", "st_teff", "st_age", "sy_dist", "pl_rade", "S"]
d = df.assign(S=S, T_surf=T, M_used=M, ESI4=esi4(df.pl_rade, M, S))
out["combos"] = {k: int(v.sum()) for k, v in combos.items()}
out["lists"] = {k: d[v][cols + ["T_surf", "M_used", "ESI4"]].round(3).to_dict("records") for k, v in combos.items() if v.sum() <= 40}
# partial-criteria table for all K-hosted HZ planets with R<2
kk = base & crit.host_K
tab = d[kk][cols + ["T_surf", "ESI4"]].copy()
for k in ["size_user", "size_strict", "temp", "age_5_8"]: tab[k] = crit[k][kk].values
tab["n_criteria_met(K,size_user,temp,age)"] = 1 + tab[["size_user", "temp", "age_5_8"]].sum(1)
tab = tab.sort_values(["n_criteria_met(K,size_user,temp,age)", "ESI4"], ascending=False)
tab.to_csv("data/superhab_K_hz_planets.csv", index=False)
out["K_hosted_HZ_R_lt_2"] = tab.round(3).to_dict("records")
# fraction of HZ rocky (R<1.8, optimistic) G/K-hosted planets that pass K + size_user (+temp)
gk = base & (df.pl_rade < 1.8) & teff.between(3900, 6000)
out["GK_HZ_rocky_n"] = int(gk.sum())
out["GK_HZ_rocky_frac_K_size_user"] = float((gk & crit.host_K & crit.size_user).sum() / max(gk.sum(), 1))
out["GK_HZ_rocky_frac_K_size_user_temp"] = float((gk & crit.host_K & crit.size_user & crit.temp).sum() / max(gk.sum(), 1))
# paper's Fig.2 KOIs vs Archive KOI cumulative table
k = pd.read_csv("data/smh2020_kois.csv")
out["paper_fig2_kois_legible"] = 23
out["paper_fig2_kois_in_cumulative"] = int(len(k))
out["paper_fig2_kois_confirmed"] = k[k.koi_disposition == "CONFIRMED"][["kepoi_name", "kepler_name", "koi_prad", "koi_insol", "koi_steff"]].to_dict("records")
out["paper_fig2_kois_disposition_counts"] = k.koi_disposition.value_counts().to_dict()
kk2 = k.copy(); kk2["T_surf"] = 288 * kk2.koi_insol ** 0.25
kk2["K_host"] = kk2.koi_steff.between(3900, 5199.9); kk2["size_user"] = kk2.koi_prad.between(1.0, 1.5); kk2["temp"] = kk2.T_surf.between(282, 302)
out["paper_kois_K_host_now"] = int(kk2.K_host.sum()); out["paper_kois_size_user"] = int(kk2.size_user.sum()); out["paper_kois_temp"] = int(kk2.temp.sum())
out["paper_kois_K_and_size"] = kk2[kk2.K_host & kk2.size_user].kepoi_name.tolist()
kk2.round(3).to_csv("data/smh2020_kois_screened.csv", index=False)
json.dump(out, open("data/superhab.json", "w"), indent=1, default=str)
for k_, v in out.items():
    if k_ not in ("lists", "K_hosted_HZ_R_lt_2"): print(k_, v)
pd.set_option("display.width", 250); print(tab.round(3).head(25).to_string(index=False))
