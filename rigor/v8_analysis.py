"""v8 (2026-11-09, local): combined data-backed candidates vs v5, paired draw by draw. One-at-a-time variants (v5 + one feature),
sensitivity variants on top of v8 (env-paced hard steps, Tyrrell climate persistence), baseline v8, Sobol S1 of log10 radio-or-better.
Output rigor/v8.json, rigor/v8_radio.png"""
import json, os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); NB = 50
H = "nathan_headline_ocean_linked"; B = "baseline_ocean_linked"
FEAT = ["land", "ne_m", "m_flares", "thick", "pt_best", "recovery", "eta_earth", "glacial", "impacts"]  # q_regress dropped (audit fix)
def s1(x, y, w):
    o = np.argsort(x, kind="stable"); cw = np.cumsum(w[o]); b = np.minimum((cw * NB).astype(int), NB - 1)
    mu = (w * y).sum(); v = (w * (y - mu) ** 2).sum()
    W = np.bincount(b, w[o], NB); M = np.bincount(b, w[o] * y[o], NB) / np.where(W > 0, W, 1)
    return float((W * (M - mu) ** 2).sum() / v)
L = lambda f: np.load(os.path.join(R, "results", f"samples_{f}.npz"))
def wq(x, w, qs):
    o = np.argsort(x); c = np.cumsum(w[o]); c /= c[-1]; return [float(x[o][np.searchsorted(c, q)]) for q in qs]
lg = lambda x: np.log10(np.clip(x, 1e-300, None))
def wts(Z, n, bay):
    if not bay: return np.ones(n)
    lw = Z["r_logw"][:n]; w = np.exp(lw - lw[np.isfinite(lw)].max()); w[~np.isfinite(w)] = 0; return w
def summ(Z, Z0, n, bay, sobol=False):
    w = wts(Z, n, bay); r1, r0 = Z["r_N_radio_capable"][:n], Z0["r_N_radio_capable"][:n]
    assert np.array_equal(Z["p_sfr_now"][:n], Z0["p_sfr_now"][:n]), "pairing broken"
    d = dict(n=n, ess=float(w.sum() ** 2 / (w ** 2).sum()), radio_p10_p50_p90=wq(r1, w, [.1, .5, .9]), v5_radio_p10_p50_p90=wq(r0, w, [.1, .5, .9]),
             P_radio_lt_1=float((w * (r1 < 1)).sum() / w.sum()), v5_P_radio_lt_1=float((w * (r0 < 1)).sum() / w.sum()),
             stone_median=wq(Z["r_N_now"][:n], w, [.5])[0], v5_stone_median=wq(Z0["r_N_now"][:n], w, [.5])[0],
             paired_dex_radio_median=wq(lg(r1) - lg(r0), w, [.5])[0], dex_shift_of_radio_median=float(np.log10(wq(r1, w, [.5])[0] / wq(r0, w, [.5])[0])))
    if sobol:
        ww = w / w.sum(); y = lg(r1); keys = [k for k in Z.files if k.startswith("p_") and not k.startswith("p_aux_") and np.ptp(Z[k][:n]) > 0]
        keys = [k for k in keys if not (k.startswith("p_w_similarity_") and np.allclose(Z[k][:n], Z["p_w_similarity"][:n]))]
        S = sorted(((k[2:], s1(Z[k][:n], y, ww)) for k in keys), key=lambda kv: -kv[1]); d["sobol_radio_top10"] = S[:10]; d["sobol_sum"] = float(sum(v for _, v in S))
        rng = np.random.default_rng(1); d["sobol_null95"] = float(np.percentile([s1(rng.permutation(Z[keys[0]][:n]), y, ww) for _ in range(20)], 95))
    return d
out = {}; V5 = L(H + "_v5"); BV5 = L(B + "_v5")
N0 = L(H + "_v8_none"); n0 = len(N0["r_N_now"])
out["regression_v8_none_equals_v5"] = bool(np.array_equal(N0["r_N_radio_capable"], V5["r_N_radio_capable"][:n0]) and np.array_equal(N0["r_N_now"], V5["r_N_now"][:n0]))
out["v8"] = summ(L(H + "_v8"), V5, 100000, False, sobol=True)
out["v5_sobol"] = summ(V5, V5, 100000, False, sobol=True)["sobol_radio_top10"]
for s in ["envpaced", "tyrrell", "tyrrell_moon"]: out[f"v8_{s}"] = summ(L(H + f"_v8_{s}"), V5, 100000, False)
for s in ["envpaced", "tyrrell", "tyrrell_moon"]:   # also relative to v8 itself
    Z = L(H + f"_v8_{s}"); Z8 = L(H + "_v8"); out[f"v8_{s}"]["paired_dex_vs_v8"] = wq(lg(Z["r_N_radio_capable"]) - lg(Z8["r_N_radio_capable"]), np.ones(100000), [.5])[0]
out["baseline_v8"] = summ(L(B + "_v8"), BV5, 100000, True)
out["one_at_a_time"] = {f: summ(L(H + f"_v8_only_{f}"), V5, 50000, False) for f in FEAT}
import yaml; cfg = yaml.safe_load(open(os.path.join(R, "params.yaml"))); Z8 = L(H + "_v8"); viol = []
for k, sp in cfg["v8"]["params"].items():
    x = Z8["p_" + k]; lo_, hi_ = float(sp["low"]), float(sp["high"])
    if x.min() < lo_ * (1 - 1e-9) or x.max() > hi_ * (1 + 1e-9): viol.append(k)
for k, lo_, hi_ in [("ne_K", .16, 1.5), ("ne_G", .10, 1.5), ("ne_M", .05, .351), ("f_m_flares", .03, .39), ("stage_q_regress", .0, 1), ("t_recovery_gyr", 1e-4, 1e-2)]:  # ne_M high Gillis 0.351; q_regress back to v5 U(0,1)
    x = Z8["p_" + k]
    if x.min() < lo_ * (1 - 1e-9) or x.max() > hi_ * (1 + 1e-9): viol.append(k)
out["v8_support_violations"] = viol
json.dump(out, open(os.path.join(R, "rigor/v8.json"), "w"), indent=1)
fig, ax = plt.subplots(1, 2, figsize=(14, 4.8))
for nm, Z, st in [("v5", V5, "k--"), ("v8", L(H + "_v8"), "C0-"), ("v8 + env-paced", L(H + "_v8_envpaced"), "C2-"), ("v8 + Tyrrell (repl. PT x moon)", L(H + "_v8_tyrrell"), "C3-"), ("v8 + Tyrrell (repl. moon)", L(H + "_v8_tyrrell_moon"), "C1-")]:
    r = np.sort(Z["r_N_radio_capable"]); ax[0].plot(lg(r), np.arange(1, len(r) + 1) / len(r), st, label=f"{nm}: median {np.median(r):.3g}")
ax[0].axvline(0, color="grey", lw=.8); ax[0].set_xlim(-8, 10); ax[0].legend(fontsize=8); ax[0].set_xlabel("log10 radio-or-better civilisations now"); ax[0].set_ylabel("CDF"); ax[0].set_title("headline (v8 local build)")
oa = out["one_at_a_time"]; ax[1].barh(FEAT, [oa[f]["paired_dex_radio_median"] for f in FEAT]); ax[1].axvline(0, color="k", lw=.8)
ax[1].set_xlabel("paired median shift vs v5 (dex), one feature at a time"); fig.tight_layout(); fig.savefig(os.path.join(R, "rigor/v8_radio.png"), dpi=110)
print(json.dumps({k: (v if not isinstance(v, dict) else {kk: vv for kk, vv in v.items() if kk in ("radio_p10_p50_p90", "P_radio_lt_1", "stone_median", "paired_dex_radio_median", "ess", "paired_dex_vs_v8")}) for k, v in out.items() if k != "one_at_a_time"}, indent=0))
print({f: (round(v["paired_dex_radio_median"], 3), round(v["dex_shift_of_radio_median"], 3), "%.3g" % v["radio_p10_p50_p90"][1]) for f, v in oa.items()})
print("v8 sobol", [(k, round(v, 3)) for k, v in out["v8"]["sobol_radio_top10"]], "null95", out["v8"]["sobol_null95"])
print("v5 sobol", [(k, round(v, 3)) for k, v in out["v5_sobol"]])
