"""Held-out checks. No factor in the model is FITTED (no regression, curve fit or optimiser anywhere in the code; the
thin-disk exponent k is solved exactly from prior draws, not fitted to data). The only quantities estimated from the
Archive data in this repo are (a) f_superhab's best value 0.104 = P(size|HZ,R<2) x P(temp|HZ,R<2) (independence
assumed) and (b) the ESI similarity weights (bootstrap means). This script gives 50/50 split checks of those two.
Output: rigor/heldout.json"""
import json, os, sys, numpy as np, pandas as pd
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT); sys.path.insert(0, ROOT)
from esi import seff
df = pd.read_csv("data/pscomppars.csv", low_memory=False)
teff = df.st_teff; S = df.pl_insol.copy()
miss = S.isna() & df.st_lum.notna() & df.pl_orbsmax.notna(); S[miss] = 10**df.st_lum[miss] / df.pl_orbsmax[miss]**2
tc = teff.clip(lower=2600); ok = teff.between(2300, 7200) & S.notna()
hz = ok & (S <= seff("recent_venus", tc)) & (S >= seff("early_mars", tc))
T = 288.0 * S ** 0.25; base = hz & (df.pl_rade < 2)
size = df.pl_rade.between(1.0, 1.5)[base].to_numpy(); temp = T.between(282, 302)[base].to_numpy(); n = len(size)
rng = np.random.default_rng(20261019); NS = 5000
err = {"product (2 params, model's estimator)": [], "joint frequency (1 param)": [], "prior-bracket midpoint 0.114 (0 params)": [], "random null (2 params, U(0,1) x U(0,1))": []}
for _ in range(NS):
    idx = rng.permutation(n); A, B = idx[: n // 2], idx[n // 2:]
    obs = (size[B] & temp[B]).mean()
    err["product (2 params, model's estimator)"].append(abs(size[A].mean() * temp[A].mean() - obs))
    err["joint frequency (1 param)"].append(abs((size[A] & temp[A]).mean() - obs))
    err["prior-bracket midpoint 0.114 (0 params)"].append(abs(np.sqrt(0.03 * 0.43) - obs))
    err["random null (2 params, U(0,1) x U(0,1))"].append(abs(rng.random() * rng.random() - obs))
E = {k: np.array(v) for k, v in err.items()}; P = E["product (2 params, model's estimator)"]
ncomp = 3
cmp_ = {k: dict(mean_abs_err_product=float(P.mean()), mean_abs_err_other=float(v.mean()),
                frac_splits_product_better=float((P < v).mean()), frac_ties=float((P == v).mean()),
                one_sided_p_product_not_better=float((P >= v).mean()), bonferroni_p=min(1.0, float((P >= v).mean()) * ncomp))
        for k, v in E.items() if v is not P}
sup = dict(n_planets=int(n), n_size=int(size.sum()), n_temp=int(temp.sum()), n_joint=int((size & temp).sum()),
           product_full=float(size.mean() * temp.mean()), joint_full=float((size & temp).mean()), splits=NS,
           comparisons=cmp_, bonferroni_m=ncomp,
           note="Scored by |estimate(half A) - joint frequency(half B)|. Split p-values are a descriptive frequency over random splits, not independent tests; n is small.")
E_ = json.load(open("data/esi_hz.json"))["conservative"]
esi = {}
for nm, e in (("pooled", E_["esi4"]), ("M", E_["by_type"]["M"]["esi4"])):
    e = np.array(e); d = []
    for _ in range(NS):
        i = rng.permutation(len(e)); d.append(e[i[: len(e) // 2]].mean() - e[i[len(e) // 2:]].mean())
    d = np.array(d)
    esi[nm] = dict(n=len(e), mean=float(e.mean()), split_half_abs_diff_median=float(np.median(abs(d))), split_half_abs_diff_p95=float(np.percentile(abs(d), 95)),
                   log10_effect_on_N_p95=float(np.log10((e.mean() + np.percentile(abs(d), 95) / 2) / e.mean())))
out = dict(fitted_factors="none", superhab_independence_check=sup, esi_split_half=esi)
json.dump(out, open("rigor/heldout.json", "w"), indent=1); print(json.dumps(out, indent=1))
