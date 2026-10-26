"""P-box: [MEASURED]/[MODELED] inputs sampled (stored draws, their priors), every [GUESS]/untagged input kept as its whole
interval -> per-draw rigorous [lo_i, hi_i] (engine.bound). Valid for ANY dependence among guesses (incl. links).
Coverage interval via two-sided DKW (95% confidence). Also hard interval for MEASURED/MODELED box with guesses at medians."""
import json, math, os, sys, numpy as np, yaml
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); R = os.path.dirname(H); sys.path.insert(0, R)
import engine as E, drake_model as dm
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
cfg = yaml.safe_load(open(os.path.join(R, "params.yaml"))); NS = int(os.environ.get("NS", 2000))
def tag_of(m, specs, k):
    if k.startswith("w_similarity"): return "MEASURED"           # bootstrap of Archive ESI list
    if k == "tau_" + m.steps[-1]["name"] and "n_tool_origins" in specs: k = "n_tool_origins"
    return (specs.get(k) or {}).get("tag", "UNTAGGED")
out = {}; fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
for j, s in enumerate(["nathan_headline_ocean", "baseline_ocean"]):
    m = dm.Model(cfg, s); specs = m.param_specs(); box = E.full_box(m)
    known = [k for k in box if tag_of(m, specs, k) in ("MEASURED", "MODELED") and box[k][1] > box[k][0]]
    guess = [k for k in box if k not in known and box[k][1] > box[k][0]]
    Z = np.load(os.path.join(R, "results", f"samples_{s}.npz")); idx = np.random.default_rng(3).choice(len(Z["r_N_now"]), NS, replace=False)
    LH = np.array([E.bound(m, {**box, **{k: (float(Z["p_" + k][i]),) * 2 for k in known}}, cfg) for i in idx])
    lo, hi = np.sort(LH[:, 0]), np.sort(LH[:, 1]); eps = math.sqrt(math.log(2 / 0.05) / (2 * NS))
    a = float(lo[max(int(math.floor((0.05 - eps) * NS)) - 1, 0)]) if 0.05 > eps else float(lo[0])
    b = float(hi[min(int(math.ceil((0.95 + eps) * NS)), NS - 1)])
    med = {**{k: (v, v) for k, v in ((k, E.median(specs[k])) for k in guess if k in specs)}}
    for k in guess:
        if k not in med: med[k] = (math.sqrt(box[k][0] * box[k][1]),) * 2 if box[k][0] > 0 else ((box[k][0] + box[k][1]) / 2,) * 2
    hk = E.bound(m, {**box, **med}, cfg)
    out[s] = dict(n_draws=NS, dkw_eps=eps, n_known=len(known), n_guess=len(guess), known=known,
                  coverage90=[a, b], coverage_note="[a,b] contains N with >=90% prob. (95% confidence, DKW) if every guess range is honest; unweighted prior draws" + (" (pre-Earth-timing weights: baseline taus are GUESS intervals)" if "baseline" in s else ""),
                  pbox_quantiles={q: [float(np.quantile(lo, q)), float(np.quantile(hi, q))] for q in (0.1, 0.5, 0.9)},
                  hard_known_only_guess_at_median=list(hk))
    print(s, out[s]["coverage90"], out[s]["pbox_quantiles"], hk, flush=True)
    y = np.arange(1, NS + 1) / NS
    ax[j].step(np.log10(hi), y, label="F lower (from hi_i)"); ax[j].step(np.log10(lo), y, label="F upper (from lo_i)")
    MC = np.sort(Z["r_N_now"]); ax[j].plot(np.log10(np.maximum(MC, 1e-300)), np.arange(1, len(MC) + 1) / len(MC), "k--", lw=1, label="MC (unweighted)")
    ax[j].axvspan(math.log10(a), math.log10(b), color="grey", alpha=.15, label="90% coverage interval")
    ax[j].set_title(s); ax[j].set_xlabel("log10 N_now"); ax[j].set_xlim(math.log10(a) - 2, math.log10(b) + 1)
ax[0].set_ylabel("CDF"); ax[0].legend(fontsize=7); plt.tight_layout(); plt.savefig(os.path.join(H, "pbox.png"), dpi=110)
json.dump(out, open(os.path.join(H, "pbox.json"), "w"), indent=1)
