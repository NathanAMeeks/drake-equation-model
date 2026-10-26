"""First-order Sobol indices S1 = Var(E[log10 N | X_i]) / Var(log10 N) from the existing MC samples (given-data
estimator, 50 equal-weight quantile bins; importance weights used for Bayes-updated scenarios). A permutation null
(X_i shuffled) gives the estimator's noise floor. Output: rigor/sobol.json, rigor/sobol_ranking.png"""
import json, os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SC = ["nathan_headline", "nathan_headline_ocean", "baseline", "baseline_ocean"]; NB = 50
def w_of(z):
    lw = z["r_logw"]; w = np.exp(lw - np.max(lw[np.isfinite(lw)])); w[~np.isfinite(w)] = 0; return w / w.sum()
def s1(x, y, w):
    o = np.argsort(x, kind="stable"); cw = np.cumsum(w[o]); b = np.minimum((cw * NB).astype(int), NB - 1)
    mu = (w * y).sum(); v = (w * (y - mu) ** 2).sum()
    W = np.bincount(b, w[o], NB); M = np.bincount(b, w[o] * y[o], NB) / np.where(W > 0, W, 1)
    return float((W * (M - mu) ** 2).sum() / v)
out = {}; rng = np.random.default_rng(1)
fig, axs = plt.subplots(2, 2, figsize=(15, 11))
for ax, sc in zip(axs.ravel(), SC):
    z = np.load(os.path.join(ROOT, f"results/samples_{sc}.npz")); w = w_of(z)
    ess = 1 / (w ** 2).sum()
    y = np.log10(np.clip(z["r_N_now"], 1e-300, None))
    keys = [k for k in z.files if k.startswith("p_") and not k.startswith("p_aux_") and np.ptp(z[k]) > 0]
    keys = [k for k in keys if not (k.startswith("p_w_similarity_") and np.allclose(z[k], z["p_w_similarity"]))]
    res = {k[2:]: s1(z[k], y, w) for k in keys}
    null = [s1(rng.permutation(z[keys[0]]), y, w) for _ in range(20)]
    floor = float(np.percentile(null, 95))
    r = sorted(res.items(), key=lambda kv: -kv[1])
    out[sc] = dict(S1=dict(r), sum_S1=float(sum(res.values())), null_95pct=floor, ess=float(ess), var_log10N=float(np.cov(y, aweights=w)))
    top = r[:15][::-1]
    ax.barh([k for k, _ in top], [v for _, v in top], color="#2f5f98"); ax.axvline(floor, color="crimson", ls="--", lw=1, label=f"permutation null 95% ({floor:.1e})")
    ax.set_title(f"{sc}: first-order Sobol S1 of log10 N_now\n(sum S1 = {out[sc]['sum_S1']:.2f}; rest = interactions; ESS {ess:,.0f})", fontsize=10)
    ax.tick_params(axis="y", labelsize=8); ax.legend(fontsize=8); ax.set_xlabel("share of Var(log10 N_now)")
fig.tight_layout(); fig.savefig(os.path.join(ROOT, "rigor/sobol_ranking.png"), dpi=110)
json.dump(out, open(os.path.join(ROOT, "rigor/sobol.json"), "w"), indent=1)
for sc in SC:
    print(sc, "sumS1 %.2f ess %.0f floor %.1e" % (out[sc]["sum_S1"], out[sc]["ess"], out[sc]["null_95pct"]), [(k, round(v, 3)) for k, v in list(out[sc]["S1"].items())[:8]])
