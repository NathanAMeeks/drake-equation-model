"""v5 (2026-10-26, guessed v4 variables removed): headline = radio-or-better civilisations now (radio + spacefaring stages). Paired comparison of the new
variables vs the *_linked parents, P(radio<1), Sobol S1 of log10 N_radio. Output rigor/v5.json, rigor/v5_radio.png"""
import json, os, sys, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB = 50
def s1(x, y, w):   # same given-data estimator as rigor/sobol.py (not imported: that module runs on import)
    o = np.argsort(x, kind="stable"); cw = np.cumsum(w[o]); b = np.minimum((cw * NB).astype(int), NB - 1)
    mu = (w * y).sum(); v = (w * (y - mu) ** 2).sum()
    W = np.bincount(b, w[o], NB); M = np.bincount(b, w[o] * y[o], NB) / np.where(W > 0, W, 1)
    return float((W * (M - mu) ** 2).sum() / v)
L = lambda f: np.load(os.path.join(R, "results", f"samples_{f}.npz"))
def wq(x, w, qs):
    o = np.argsort(x); c = np.cumsum(w[o]); c /= c[-1]; return [float(x[o][np.searchsorted(c, q)]) for q in qs]
def rad(z, n):
    return (z["r_N_radio_capable"] if "r_N_radio_capable" in z.files else z["r_N_now_stage_radio"] + z["r_N_now_stage_spacefaring"])[:n]
lg = lambda x: np.log10(np.clip(x, 1e-300, None))
FE = ["metal", "ghz", "oxygen", "recovery"]
out = {}; fig, axs = plt.subplots(1, 3, figsize=(17, 4.8))
for j, p in enumerate(["nathan_headline_ocean_linked", "baseline_ocean_linked"]):
    Z0 = L(p); bay = p.startswith("baseline"); res = {}
    for v, n in [("_v5", 100000)] + [(f"_v5_{f}", 50000) for f in FE]:
        Z = L(p + v); n = min(n, len(Z["r_N_now"])); assert np.array_equal(Z["p_sfr_now"], Z0["p_sfr_now"][:n])
        lw = Z0["r_logw"][:n]; w = np.exp(lw - lw.max()) if bay else np.ones(n)
        r0, r1 = rad(Z0, n), rad(Z, n); s0, s1_ = Z0["r_N_now"][:n], Z["r_N_now"][:n]
        d = dict(n=n, radio_p10_p50_p90=wq(r1, w, [.1, .5, .9]), parent_radio_p10_p50_p90=wq(r0, w, [.1, .5, .9]),
                 stone_median=wq(s1_, w, [.5])[0], parent_stone_median=wq(s0, w, [.5])[0],
                 P_radio_lt_1=float((w * (r1 < 1)).sum() / w.sum()), parent_P_radio_lt_1=float((w * (r0 < 1)).sum() / w.sum()),
                 paired_dex_radio_median=wq(lg(r1) - lg(r0), w, [.5])[0], dex_shift_of_radio_median=float(np.log10(wq(r1, w, [.5])[0] / wq(r0, w, [.5])[0])),
                 dex_shift_of_radio_p90=float(np.log10(wq(r1, w, [.9])[0] / wq(r0, w, [.9])[0])), dex_shift_of_stone_median=float(np.log10(wq(s1_, w, [.5])[0] / wq(s0, w, [.5])[0])))
        if "r_N_now_subsurface" in Z.files: d["subsurface_share_of_stone"] = float((w * Z["r_N_now_subsurface"][:n]).sum() / (w * s1_).sum())
        if "r_N_settled" in Z.files: d["settled_share_of_radio"] = float((w * Z["r_N_settled"][:n]).sum() / (w * r1).sum())
        if v == "_v5":
            ww = w / w.sum(); y = lg(r1); keys = [k for k in Z.files if k.startswith("p_") and not k.startswith("p_aux_") and np.ptp(Z[k][:n]) > 0]
            keys = [k for k in keys if not (k.startswith("p_w_similarity_") and np.allclose(Z[k][:n], Z["p_w_similarity"][:n]))]
            S = sorted(((k[2:], s1(Z[k][:n], y, ww)) for k in keys), key=lambda kv: -kv[1]); d["sobol_radio_top8"] = S[:8]; d["sobol_sum"] = float(sum(v_ for _, v_ in S))
        res[v] = d
        if v == "_v5":
            o = np.argsort(r1); c = np.cumsum(w[o]); axs[j].plot(lg(r1[o]), c / c[-1], label=f"{v[1:]}: median {d['radio_p10_p50_p90'][1]:.3g}")
    o = np.argsort(r0); c = np.cumsum(w[o]); axs[j].plot(lg(r0[o]), c / c[-1], "k--", label=f"parent: median {res['_v5']['parent_radio_p10_p50_p90'][1]:.3g}")
    axs[j].axvline(0, color="grey", lw=.8); axs[j].set_xlim(-8, 10); axs[j].set_xlabel("log10 radio-or-better civilisations now"); axs[j].set_title(p); axs[j].legend(fontsize=8)
    axs[2].barh([f"{f} ({'H' if j == 0 else 'B'})" for f in FE], [res[f"_v5_{f}"]["paired_dex_radio_median"] for f in FE], color="#2f5f98" if j == 0 else "#c87137", alpha=.8)
    out[p] = res; print(p, {k: (round(v["paired_dex_radio_median"], 3), "%.3g" % v["radio_p10_p50_p90"][1]) for k, v in res.items()})
axs[0].set_ylabel("CDF"); axs[2].axvline(0, color="k", lw=.8); axs[2].set_xlabel("paired median shift, log10 radio-or-better (dex)"); axs[2].set_title("each new variable alone (H = headline, B = baseline)")
fig.tight_layout(); fig.savefig(os.path.join(R, "rigor/v5_radio.png"), dpi=110); json.dump(out, open(os.path.join(R, "rigor/v5.json"), "w"), indent=1)
