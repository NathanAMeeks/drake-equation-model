"""Ocean-intelligence path comparison chart: paired parent vs *_ocean scenarios (reads results/samples_*.npz)."""
import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
L = lambda s: np.load(os.path.join(R, f"samples_{s}.npz"))
pairs = [("nathan_headline", "nathan_headline_ocean"), ("baseline", "baseline_ocean")]
def W(d):
    lw = d["r_logw"]; w = np.exp(lw - np.max(lw[np.isfinite(lw)])); w[~np.isfinite(w)] = 0; return w / w.sum()
def wq(x, w, q):
    o = np.argsort(x); c = np.cumsum(w[o]); return x[o][min(np.searchsorted(c, q), len(x) - 1)]
stages = ["lithic", "agricultural", "industrial", "radio", "spacefaring"]
fig, ax = plt.subplots(2, 3, figsize=(17, 9))
for r, (a, b) in enumerate(pairs):
    A, B = L(a), L(b); wA, wB = W(A), W(B)
    lo = np.log10(np.clip(np.concatenate([A["r_N_now"], B["r_N_now"]]), 1e-30, None))
    bins = np.linspace(np.percentile(lo, 0.5), np.percentile(lo, 99.5), 70)
    for d, ww, nm, c in ((A, wA, a, "#2f5f98"), (B, wB, b, "#d2691e")):
        x = np.log10(np.clip(d["r_N_now"], 1e-30, None))
        ax[r, 0].hist(x, bins, weights=ww, histtype="step", lw=2, color=c, density=True, label=f"{nm}: median {wq(d['r_N_now'], ww, .5):.3g}")
        ax[r, 0].axvline(np.log10(wq(d["r_N_now"], ww, .5)), color=c, ls="--")
    ax[r, 0].set_xlabel("log10 N_now (tool-using worlds, Milky Way)"); ax[r, 0].legend(fontsize=8); ax[r, 0].set_title(f"{a}: land only vs land + ocean")
    w = np.arange(len(stages) + 1); lab = stages + ["radio-capable"]
    for k, (d, ww, c, off) in enumerate(((A, wA, "#2f5f98", -0.2), (B, wB, "#d2691e", 0.2))):
        v = [d[f"r_N_now_stage_{s}"] for s in stages] + [d["r_N_now_stage_radio"] + d["r_N_now_stage_spacefaring"]]
        med = [wq(x, ww, .5) for x in v]; p10 = [wq(x, ww, .1) for x in v]; p90 = [wq(x, ww, .9) for x in v]
        lm = np.log10(np.clip(med, 1e-30, None))
        ax[r, 1].bar(w + off, lm - np.floor(min(lm)) + 1, 0.4, bottom=np.floor(min(lm)) - 1, color=c, label=(a, b)[k])
        ax[r, 1].errorbar(w + off, lm, yerr=[lm - np.log10(np.clip(p10, 1e-30, None)), np.log10(np.clip(p90, 1e-30, None)) - lm], fmt="none", ecolor="k", lw=1)
    ax[r, 1].set_xticks(w); ax[r, 1].set_xticklabels(lab, rotation=25, fontsize=8); ax[r, 1].set_ylabel("log10 median N_now (bars: 10-90%)")
    ax[r, 1].legend(fontsize=8); ax[r, 1].set_title("stage breakdown")
    cl = ["M", "K", "G", "F"]
    for k, (d, ww, c, off) in enumerate(((A, wA, "#2f5f98", -0.2), (B, wB, "#d2691e", 0.2))):
        sh = [wq(d[f"r_N_now_{x}"] / np.where(d["r_N_now"] > 0, d["r_N_now"], 1), ww, .5) for x in cl]
        ax[r, 2].bar(np.arange(4) + off, sh, 0.4, color=c, label=(a, b)[k])
        for i, s_ in enumerate(sh): ax[r, 2].text(i + off, s_, f"{s_:.3f}", ha="center", va="bottom", fontsize=7)
    ax[r, 2].set_xticks(range(4)); ax[r, 2].set_xticklabels(cl); ax[r, 2].set_ylabel("median share of N_now"); ax[r, 2].legend(fontsize=8)
    ax[r, 2].set_title("host star-type share")
fig.suptitle("Ocean-intelligence path (paired samples, n = %d each)" % len(A["r_N_now"]))
fig.tight_layout(); out = os.path.join(R, "ocean_comparison.png"); fig.savefig(out, dpi=110); print("wrote", out)
