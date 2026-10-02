"""Reporting: statistics, sensitivity, plots, markdown summary."""
import os, json, math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def wq(x, w, q):
    o = np.argsort(x); x, w = x[o], w[o]
    c = np.cumsum(w); c = c / c[-1]
    return float(np.interp(q, c, x))

def stats(N, w):
    m = np.isfinite(N); N, w = N[m], w[m]
    w = w / w.sum()
    L = np.log10(np.maximum(N, 1e-300))
    p0 = float((w * np.exp(-np.minimum(N, 700))).sum())
    rng = np.random.default_rng(0)
    pois = np.where(N < 1e8, rng.poisson(np.minimum(N, 1e8)), N)
    return dict(median=10 ** wq(L, w, 0.5), mean=float((w * N).sum()),
                p10=10 ** wq(L, w, 0.10), p90=10 ** wq(L, w, 0.90),
                p05=10 ** wq(L, w, 0.05), p95=10 ** wq(L, w, 0.95),
                P_lambda_lt1=float(w[N < 1].sum()), P_zero_other_poisson=p0,
                median_poisson_count=wq(pois.astype(float), w, 0.5),
                P_between_1_and_3=float(w[(N >= 1) & (N <= 3)].sum()),
                P_lambda_ge_1=float(w[N >= 1].sum()))

def wspearman(x, y, w):
    rx = np.argsort(np.argsort(x)).astype(float); ry = np.argsort(np.argsort(y)).astype(float)
    w = w / w.sum()
    mx, my = (w * rx).sum(), (w * ry).sum()
    cov = (w * (rx - mx) * (ry - my)).sum()
    return float(cov / math.sqrt((w * (rx - mx) ** 2).sum() * (w * (ry - my) ** 2).sum()))

def sensitivity(P, N, w):
    L = np.log10(np.maximum(N, 1e-300)); out = []
    for k, v in P.items():
        if k.startswith("aux_") or np.ptp(v) == 0: continue
        x = np.log10(v) if np.all(v > 0) else v
        lo, hi = wq(x, w, 0.1), wq(x, w, 0.9)
        ml, mh = x <= lo, x >= hi
        if ml.sum() < 50 or mh.sum() < 50 or w[ml].sum() == 0 or w[mh].sum() == 0: continue
        out.append(dict(param=k, spearman=wspearman(x, L, w),
                        med_low=wq(L[ml], w[ml], 0.5), med_high=wq(L[mh], w[mh], 0.5)))
    for o in out: o["swing"] = abs(o["med_high"] - o["med_low"])
    return sorted(out, key=lambda o: -o["swing"])

def ess(w): return float(w.sum() ** 2 / (w ** 2).sum())

def spacing(N, geo):
    """Equal-cube side (V/N)^(1/3) and median nearest-neighbour distance for N worlds placed at random (Poisson) in the disk.
    3D Poisson median NN distance r = (3 ln2 / (4 pi n))^(1/3); if that exceeds the disk thickness the 2D (thin-disk) form
    r = sqrt(ln2 / (pi n_A)) with n_A = N / (pi R^2) is used instead."""
    V, R, H = float(geo["disk_volume_ly3"]), float(geo["disk_radius_ly"]), float(geo["disk_thickness_ly"])
    if not (N > 0): return dict(N=N, cube_side_ly=None, nn_median_ly=None, regime=None)
    cube = (V / N) ** (1 / 3)
    r3 = (3 * math.log(2) / (4 * math.pi * (N / V))) ** (1 / 3)
    if r3 <= H: r, reg = r3, "3D"
    else: r, reg = math.sqrt(math.log(2) / (math.pi * N / (math.pi * R ** 2))), "2D thin disk"
    return dict(N=N, cube_side_ly=cube, nn_median_ly=r, regime=reg, exceeds_galaxy=bool(r > 2 * R or N < 1))

def fmt(x):
    if x is None or not np.isfinite(x): return "n/a"
    if x == 0: return "0"
    if 1e-3 <= abs(x) < 1e5: return f"{x:.3g}"
    return f"{x:.2e}"

def report(cfg, allres, Ncl, outdir):
    summary = {}
    head = cfg["run"]["headline_scenario"]
    for scen, A in allres.items():
        R, P = A["R"], A["P"]
        lw = R["logw"]; w = np.exp(lw - np.max(lw[np.isfinite(lw)])); w[~np.isfinite(w)] = 0
        S = dict(N_now=stats(R["N_now"], w), N_timeavg=stats(R["N_timeavg"], w), N_ever=stats(R["N_ever"], w),
                 ess=ess(w), n=len(w), best=A["best"],
                 frac_gk_median=wq(np.nan_to_num(R["frac_gk"], nan=0.0), w, 0.5),
                 t_peak_median_gyr_ago=cfg["run"]["t_now_gyr"] - wq(R["t_peak"], w, 0.5),
                 mean_planet_age_median=wq(R["mean_planet_age"], w, 0.5),
                 sens=sensitivity(P, R["N_now"], w)[:15])
        Ne = R["N_ever"]; wn = w / w.sum()
        S["P_N_ever_50_100"] = float(wn[(Ne >= 50) & (Ne <= 100)].sum())
        S["P_N_ever_ge_50"] = float(wn[Ne >= 50].sum())
        S["P_N_now_ge_1"] = float(wn[R["N_now"] >= 1].sum())
        if "exomoon_share_gk" in R:
            S["exomoon_share_gk_median"] = wq(np.nan_to_num(R["exomoon_share_gk"]), w, 0.5)
            S["exomoon_share_gk_p90"] = wq(np.nan_to_num(R["exomoon_share_gk"]), w, 0.9)
        # posterior check vs Kipping 2020: P(abiogenesis tau < 1 Gyr)
        ta = P.get("tau_abiogenesis")
        if ta is not None:
            S["post_P_tau_abio_lt_1Gyr"] = float(w[ta < 1].sum() / w.sum())
            S["prior_P_tau_abio_lt_1Gyr"] = float((ta < 1).mean())
            ti = P["tau_stone_tool_intelligence"]
            S["post_P_tau_intel_lt_earthwindow"] = float(w[ti < 5.0].sum() / w.sum())
        # ---------- species per tool-using world (post hoc, independent draws)
        sp = cfg.get("species")
        if sp:
            import drake_model as dm
            rs = np.random.default_rng(sp["seed"])
            sc_ = dm.sample(sp["species_concurrent_per_tool_world"], len(w), rs)
            su_ = dm.sample(sp["species_cumulative_per_tool_world"], len(w), rs)
            S["species_now"] = stats(R["N_now"] * sc_, w)
            S["species_ever"] = stats(R["N_ever"] * su_, w)
            b = A["best"]
            S["best"]["species_now"] = b["N_now"] * dm.best(sp["species_concurrent_per_tool_world"])
            S["best"]["species_ever"] = b["N_ever"] * dm.best(sp["species_cumulative_per_tool_world"])
        # ---------- similarity-weight variants (exact rescaling: N is linear in w)
        if "w_similarity" in P:
            S["similarity_variants"] = {}
            for key in sorted(k for k in P if k.startswith("aux_w_")):
                Nk = R["N_now"] * P[key] / P["w_similarity"]
                S["similarity_variants"][key[6:]] = dict(N_now=stats(Nk, w), N_ever_median=wq(np.log10(np.maximum(R["N_ever"] * P[key] / P["w_similarity"], 1e-300)), w, 0.5),
                                                         w_median=wq(P[key], w, 0.5))
                S["similarity_variants"][key[6:]]["N_ever_median"] = 10 ** S["similarity_variants"][key[6:]]["N_ever_median"]
        if cfg.get("geometry"):
            S["spacing"] = {q: spacing(S["N_now"][q], cfg["geometry"]) for q in ("median", "p10", "p90")}
        # ---------- v2: multi-spectral breakdown (per host class)
        cls_ = [c for c in ("M", "K", "G", "F") if f"N_now_{c}" in R]
        if cls_:
            S["model_version"] = "v2"
            wn_ = w / w.sum(); meanN = float((wn_ * R["N_now"]).sum())
            S["by_type"] = {}
            for c in cls_:
                Nc = R[f"N_now_{c}"]; sh = np.where(R["N_now"] > 0, Nc / np.where(R["N_now"] > 0, R["N_now"], 1), 0.0)
                S["by_type"][c] = dict(N_now=stats(Nc, w), N_ever=stats(R[f"N_ever_{c}"], w),
                                       share_median=wq(sh, w, 0.5), share_p10=wq(sh, w, 0.1), share_p90=wq(sh, w, 0.9),
                                       share_of_mean=float((wn_ * Nc).sum()) / meanN if meanN > 0 else float("nan"),
                                       exomoon_share_median=wq(R[f"exomoon_share_{c}"], w, 0.5),
                                       best_N_now=A["best"].get(f"N_now_{c}"),
                                       w_similarity_median=(wq(P[f"w_similarity_{c}"], w, 0.5) if f"w_similarity_{c}" in P else None))
        # ---------- v2: multiphase breakdown (civilisation stages)
        stg = [k[4:] for k in R if k.startswith("phi_")]
        if stg:
            S["stages"] = {}
            for st in stg:
                ph = R[f"phi_{st}"]
                S["stages"][st] = dict(N_now=stats(R[f"N_now_stage_{st}"], w), phi_median=wq(ph, w, 0.5), phi_p10=wq(ph, w, 0.1), phi_p90=wq(ph, w, 0.9),
                                       best_N_now=A["best"].get(f"N_now_stage_{st}"), best_phi=A["best"].get(f"phi_{st}"))
            rc = sum(R[f"N_now_stage_{st}"] for st in stg if st in ("radio", "spacefaring"))
            S["radio_capable"] = dict(N_now=stats(rc, w), best_N_now=sum(A["best"].get(f"N_now_stage_{st}", 0) for st in ("radio", "spacefaring")),
                                      sens=sensitivity(P, rc, w)[:12])
            if cfg.get("geometry"):
                S["radio_capable"]["spacing"] = {q: spacing(S["radio_capable"]["N_now"][q], cfg["geometry"]) for q in ("median", "p10", "p90")}
            S["L_episode_yr"] = dict(median=wq(R["L_episode_yr"], w, 0.5), p10=wq(R["L_episode_yr"], w, 0.1), p90=wq(R["L_episode_yr"], w, 0.9))
        summary[scen] = S
        # ---------- histogram
        L = np.log10(np.maximum(R["N_now"], 1e-300)); m = L > -300
        lo = max(-40, np.floor(wq(L, w, 0.02))); hi = np.ceil(wq(L, w, 0.995)) + 1
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.hist(np.clip(L[m], lo, hi), bins=120, range=(lo, hi), weights=w[m], density=True, color="#4a7ab5", alpha=0.85)
        med = math.log10(S["N_now"]["median"])
        ax.axvline(med, color="crimson", lw=2, label=f"median (50/50) N = {fmt(S['N_now']['median'])}")
        ax.axvline(math.log10(S["N_now"]["p10"]), color="gray", ls="--", label="10th / 90th pct")
        ax.axvline(math.log10(S["N_now"]["p90"]), color="gray", ls="--")
        ax.axvline(0, color="k", ls=":", label="N = 1")
        if True:
            ax.axvspan(0, math.log10(3), color="orange", alpha=0.25, label="user claim: 1-3 at a time")
        ax.set_xlabel("log10 N  (worlds with stone-age-or-greater tool users alive now, Milky Way)\n(tails beyond the axis range are piled into the edge bins)")
        ax.set_ylabel("posterior density"); ax.set_title(f"Time-aware extended Drake model — scenario: {scen}")
        ax.legend(fontsize=8); fig.tight_layout()
        fig.savefig(os.path.join(outdir, f"hist_log10N_{scen}.png"), dpi=130); plt.close(fig)
        # ---------- tornado
        sens = S["sens"][:12][::-1]
        fig, ax = plt.subplots(figsize=(9, 6))
        base = med
        for i, o in enumerate(sens):
            a, b = o["med_low"] - base, o["med_high"] - base
            ax.barh(i, a, left=base, color="#c0504d"); ax.barh(i, b, left=base, color="#4f81bd")
        ax.set_yticks(range(len(sens))); ax.set_yticklabels([o["param"] for o in sens], fontsize=8)
        ax.axvline(base, color="k", lw=1)
        ax.set_xlabel("median log10 N when parameter in its lowest 10% (red) vs highest 10% (blue)")
        ax.set_title(f"Sensitivity tornado — {scen}"); fig.tight_layout()
        fig.savefig(os.path.join(outdir, f"tornado_{scen}.png"), dpi=130); plt.close(fig)
    # copy headline charts to canonical names
    import shutil
    shutil.copy(os.path.join(outdir, f"hist_log10N_{head}.png"), os.path.join(outdir, "hist_log10N.png"))
    shutil.copy(os.path.join(outdir, f"tornado_{head}.png"), os.path.join(outdir, "tornado.png"))
    if "baseline" in allres and "baseline_no_exomoons" in allres:
        a, b = allres["baseline"]["R"], allres["baseline_no_exomoons"]["R"]
        if len(a["N_now"]) == len(b["N_now"]):
            lw = a["logw"]; w = np.exp(lw - np.max(lw[np.isfinite(lw)])); w[~np.isfinite(w)] = 0
            r = np.log10(np.maximum(a["N_now"], 1e-300) / np.maximum(b["N_now"], 1e-300))
            summary["exomoon_effect"] = dict(median_log10_ratio=wq(r, w, 0.5), p90_log10_ratio=wq(r, w, 0.9),
                                             p99_log10_ratio=wq(r, w, 0.99),
                                             median_with=summary["baseline"]["N_now"]["median"],
                                             median_without=summary["baseline_no_exomoons"]["N_now"]["median"])
    # paired with/without table for nathan_headline's new factors
    trio = ["nathan_headline", "nathan_headline_no_superhab", "nathan_headline_no_tooluse", "similarity_weighted"]
    if all(t in allres for t in trio):
        ref = allres["nathan_headline"]["R"]["N_now"]
        pf = {"paired_draws": "per comparison (see table)"}
        for t in trio[1:]:
            o = allres[t]["R"]["N_now"]
            paired_t = (len(o) == len(ref) and np.allclose(allres[t]["P"]["sfr_now"], allres["nathan_headline"]["P"]["sfr_now"])
                        and np.allclose(allres[t]["P"]["tau_abiogenesis"], allres["nathan_headline"]["P"]["tau_abiogenesis"])
                        and summary[t].get("model_version") == summary["nathan_headline"].get("model_version"))
            if not paired_t:
                pf[t] = dict(median_N=summary[t]["N_now"]["median"], ratio_of_medians=summary["nathan_headline"]["N_now"]["median"] / summary[t]["N_now"]["median"],
                             persample_log10_ratio_median=float("nan"), p10=float("nan"), p90=float("nan"), paired=False)
                continue
            if len(o) == len(ref):
                r = np.log10(np.maximum(ref, 1e-300) / np.maximum(o, 1e-300))
                pf[t] = dict(median_N=summary[t]["N_now"]["median"], ratio_of_medians=summary["nathan_headline"]["N_now"]["median"] / summary[t]["N_now"]["median"],
                             persample_log10_ratio_median=float(np.median(r)), p10=float(np.quantile(r, 0.1)), p90=float(np.quantile(r, 0.9)), paired=True)
        summary["nathan_factor_effects"] = pf
    # classic static
    summary["classic_static_SDO_style"] = dict(N_now=stats(Ncl, np.ones_like(Ncl)))
    if cfg.get("geometry"):
        summary["classic_static_SDO_style"]["spacing"] = {q: spacing(summary["classic_static_SDO_style"]["N_now"][q], cfg["geometry"]) for q in ("median", "p10", "p90")}
    if cfg.get("species"):
        import drake_model as dm
        rs = np.random.default_rng(cfg["species"]["seed"] + 7)
        summary["classic_static_SDO_style"]["species_now"] = stats(Ncl * dm.sample(cfg["species"]["species_concurrent_per_tool_world"], len(Ncl), rs), np.ones_like(Ncl))
    comparison_chart(summary, outdir, head)
    esi_chart(outdir)
    lit = cfg["run"].get("literature_baseline", "baseline")
    spectral_chart(summary, outdir, [head, lit])
    stage_chart(summary, outdir, [head, lit])
    json.dump(summary, open(os.path.join(outdir, "results.json"), "w"), indent=1, default=float)
    write_md(cfg, summary, outdir)
    return summary

def comparison_chart(S, outdir, head=None):
    rows = []
    for k, s in S.items():
        if "N_now" not in s: continue
        lab = (f"★ {k} (HEADLINE)" if k == head else (f"{k} (literature baseline)" if k == "baseline" else k))
        if s.get("model_version") == "v2": lab += " [v2]"
        rows.append((lab, s["N_now"], s.get("species_now")))
        for v in ("optimistic_k1", "conservative_k3", "conservative_k10"):
            if k not in ("similarity_weighted", "nathan_headline"): break
            d = s.get("similarity_variants", {}).get(v)
            if d: rows.append((f"   {k} [{v.replace('_k', ', ESI^')}]", d["N_now"], None))
    rows = rows[::-1]
    fig, ax = plt.subplots(figsize=(11, 0.45 * len(rows) + 1.8))
    for i, (k, a, sp) in enumerate(rows):
        lg = lambda x: math.log10(max(x, 1e-60))
        ax.plot([lg(a["p05"]), lg(a["p95"])], [i, i], color="#9bb7d4", lw=2, zorder=1)
        ax.plot([lg(a["p10"]), lg(a["p90"])], [i, i], color="#2f5f98", lw=6, zorder=2)
        ax.plot(lg(a["median"]), i, "o", color="crimson", zorder=3)
        ax.text(min(lg(a["p95"]), 14) + 0.3, i, f"median {fmt(a['median'])}", va="center", fontsize=7)
        if sp: ax.plot(lg(sp["median"]), i, "D", color="darkorange", ms=5, zorder=3)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=8)
    ax.axvline(0, color="k", ls=":"); ax.axvspan(0, math.log10(3), color="orange", alpha=0.2)
    ax.set_xlim(-42, 18)
    ax.set_xlabel("log10 N now (Milky Way worlds with stone-age-or-greater tool users, other than Earth)\n"
                  "red dot = median worlds; thick bar = 10-90%; thin = 5-95% (clipped at 1e-42);\norange diamond = median tool-using SPECIES; shaded band = user's '1-3 at a time'", fontsize=9)
    ax.set_title("All scenarios compared ([v2] = multi-spectral M/K/G/F + multiphase model)"); fig.tight_layout()
    fig.savefig(os.path.join(outdir, "comparison_scenarios.png"), dpi=130); plt.close(fig)

TYPE_COL = {"M": "#c0504d", "K": "#f79646", "G": "#e6c619", "F": "#4f81bd"}
def spectral_chart(S, outdir, scens):
    scens = [x for x in scens if x in S and "by_type" in S[x]]
    if not scens: return
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2), gridspec_kw=dict(width_ratios=[1.6, 1]))
    lg = lambda x: math.log10(max(x, 1e-60))
    types = ["M", "K", "G", "F"]
    for j, sc in enumerate(scens):
        bt = S[sc]["by_type"]
        for i, c in enumerate(types):
            if c not in bt: continue
            a = bt[c]["N_now"]; y = i + (0.18 if j == 0 else -0.18)
            ax[0].plot([lg(a["p10"]), lg(a["p90"])], [y, y], color=TYPE_COL[c], lw=7 if j == 0 else 3, alpha=0.9 if j == 0 else 0.6, solid_capstyle="butt")
            ax[0].plot(lg(a["median"]), y, "o" if j == 0 else "s", color="k", ms=6 if j == 0 else 4)
            ax[0].text(lg(a["p90"]) + 0.2, y, f"{sc}: median {fmt(a['median'])}", va="center", fontsize=7)
        tot = S[sc]["N_now"]; y = len(types) + (0.18 if j == 0 else -0.18)
        ax[0].plot([lg(tot["p10"]), lg(tot["p90"])], [y, y], color="gray", lw=7 if j == 0 else 3)
        ax[0].plot(lg(tot["median"]), y, "o" if j == 0 else "s", color="k", ms=6 if j == 0 else 4)
        ax[0].text(lg(tot["p90"]) + 0.2, y, f"{sc}: median {fmt(tot['median'])}", va="center", fontsize=7)
        # shares
        bottom = 0
        for c in types:
            if c not in bt: continue
            v = bt[c]["share_of_mean"] * 100
            ax[1].bar(j, v, bottom=bottom, color=TYPE_COL[c], label=c if j == 0 else None, edgecolor="k", lw=0.5)
            if v > 8: ax[1].text(j, bottom + v / 2, f"{c} {v:.0f}%\n(median share {100*bt[c]['share_median']:.0f}%)", ha="center", va="center", fontsize=7)
            bottom += v
    ax[0].set_yticks(range(len(types) + 1)); ax[0].set_yticklabels([f"{c} dwarfs" for c in types] + ["TOTAL"])
    ax[0].axvline(0, color="k", ls=":")
    ax[0].set_xlabel("log10 N now by host type (median dot, 10-90%% bar)\nthick/circle = %s ; thin/square = %s" % tuple((scens + [""])[:2]), fontsize=8)
    ax[0].set_title("Multi-spectral breakdown: worlds with stone-age-or-greater tool users")
    ax[1].set_xticks(range(len(scens))); ax[1].set_xticklabels(scens, fontsize=8); ax[1].set_ylabel("% of posterior-mean N_now")
    ax[1].set_title("Share by host type"); ax[1].legend(fontsize=8, loc="upper right"); ax[1].set_ylim(0, 100)
    fig.tight_layout(); fig.savefig(os.path.join(outdir, "spectral_breakdown.png"), dpi=130); plt.close(fig)

def stage_chart(S, outdir, scens):
    scens = [x for x in scens if x in S and "stages" in S[x]]
    if not scens: return
    st = list(S[scens[0]]["stages"].keys())
    fig, ax = plt.subplots(figsize=(12, 5.5))
    lg = lambda x: math.log10(max(x, 1e-60))
    rows = [("all stages (stone-age-or-greater)", lambda s: s["N_now"])] + [(k, (lambda k: lambda s: s["stages"][k]["N_now"])(k)) for k in st] + \
           [("radio-capable (radio + spacefaring)", lambda s: s["radio_capable"]["N_now"])]
    cols = ["#7f7f7f", "#8c564b", "#2ca02c", "#9467bd", "#1f77b4", "#17becf", "#d62728"]
    for j, sc in enumerate(scens):
        for i, (lab, f) in enumerate(rows):
            a = f(S[sc]); y = len(rows) - 1 - i + (0.18 if j == 0 else -0.18)
            ax.plot([lg(a["p10"]), lg(a["p90"])], [y, y], color=cols[i % len(cols)], lw=7 if j == 0 else 3, alpha=0.9 if j == 0 else 0.6, solid_capstyle="butt")
            ax.plot(lg(a["median"]), y, "o" if j == 0 else "s", color="k", ms=6 if j == 0 else 4)
            ax.text(min(lg(a["p90"]), 12) + 0.2, y, f"{sc}: median {fmt(a['median'])}", va="center", fontsize=7)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows][::-1])
    lo_ = min(lg(f(S[sc])["p10"]) for sc in scens for _, f in rows); hi_ = max(lg(f(S[sc])["p90"]) for sc in scens for _, f in rows)
    ax.axvline(0, color="k", ls=":"); ax.set_xlim(max(-40, math.floor(lo_) - 1), hi_ + 5)
    ax.set_xlabel("log10 N now in each stage (median dot, 10-90%% bar)\nthick/circle = %s ; thin/square = %s" % tuple((scens + [""])[:2]), fontsize=8)
    ax.set_title("Multiphase breakdown: Milky Way worlds by civilisation stage right now")
    fig.tight_layout(); fig.savefig(os.path.join(outdir, "stage_breakdown.png"), dpi=130); plt.close(fig)

def esi_chart(outdir):
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "esi_hz.json")
    if not os.path.exists(p): return
    E = json.load(open(p))
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for lab, c in (("optimistic", "#9bb7d4"), ("conservative", "#2f5f98")):
        ax[0].hist(E[lab]["esi4"], bins=np.linspace(0.4, 1.0, 25), color=c, alpha=0.8, label=f"{lab} HZ, R<1.8 (n={E[lab]['n']}), mean {E[lab]['mean']:.2f}")
    ax[0].axvline(0.8, color="k", ls=":", label="ESI 0.8 ('Earth-like', PHL)")
    ax[0].set_xlabel("ESI (Schulze-Makuch+2011, 4-property; T_surf from insolation)"); ax[0].set_ylabel("planets"); ax[0].legend(fontsize=8)
    ax[0].set_title("NASA Exoplanet Archive HZ rocky planets")
    ks = [1, 2, 3, 5, 10]
    for lab, c in (("conservative", "#2f5f98"), ("optimistic", "#9bb7d4")):
        ax[1].plot(ks, [E[lab]["mean_pow"][str(k)] for k in ks], "o-", color=c, label=lab)
    ax[1].set_xlabel("exponent k in p = ESI^k"); ax[1].set_ylabel("population mean similarity weight <ESI^k>")
    ax[1].set_title("Similarity -> probability weight"); ax[1].legend(); ax[1].set_ylim(0, 1)
    top = E["optimistic"]
    txt = "\n".join(f"{n}: {e:.3f}" for n, e in list(zip(top["names"], top["esi4"]))[:10])
    ax[0].text(0.41, ax[0].get_ylim()[1] * 0.95, "Top 10 (optimistic HZ):\n" + txt, va="top", fontsize=7, family="monospace")
    fig.tight_layout(); fig.savefig(os.path.join(outdir, "esi_distribution.png"), dpi=130); plt.close(fig)

def write_md(cfg, S, outdir):
    L = []
    L.append("# Results — time-aware extended Drake model (stone-age-or-greater)\n")
    L.append(f"**Headline scenario: `{cfg['run']['headline_scenario']}`** (user-approved). Literature baseline for comparison: `{cfg['run'].get('literature_baseline', 'baseline')}`.\n")
    v2l = [k for k, s in S.items() if s.get("model_version") == "v2"]
    if v2l:
        L.append("Model versions: **v2** (multi-spectral M/K/G/F host classes + multiphase civilisation stages) for " + ", ".join(f"`{k}`" for k in v2l) +
                 "; all other scenarios are **v1** (two host classes G/K + M, single stone-age-or-greater phase). v1 numbers for the re-run scenarios are kept in results/v1/.\n")
    L.append("N = expected number of Milky Way worlds with stone-age-or-greater tool users alive at the same time (present day, other than Earth). "
             "Percentiles are over parameter uncertainty (posterior after the Earth-timing update where enabled).\n")
    L.append("| scenario | median (50/50) | mean | 10th pct | 90th pct | P(N<1) | P(no other, Poisson) | P(1<=N<=3) | time-avg N over history | median N_ever (by now) | ESS |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for k, s in S.items():
        if "N_now" not in s: continue
        a = s["N_now"]
        if "N_timeavg" in s:
            L.append(f"| {k} | {fmt(a['median'])} | {fmt(a['mean'])} | {fmt(a['p10'])} | {fmt(a['p90'])} | {a['P_lambda_lt1']:.3f} | {a['P_zero_other_poisson']:.3f} | {a['P_between_1_and_3']:.3f} | median {fmt(s['N_timeavg']['median'])} / mean {fmt(s['N_timeavg']['mean'])} | {fmt(s['N_ever']['median'])} | {s['ess']:.0f} |")
        else:
            L.append(f"| {k} | {fmt(a['median'])} | {fmt(a['mean'])} | {fmt(a['p10'])} | {fmt(a['p90'])} | {a['P_lambda_lt1']:.3f} | {a['P_zero_other_poisson']:.3f} | {a['P_between_1_and_3']:.3f} | (static) | – | – |")
    L.append("\n## Worlds vs tool-using species (species_per_tool_world)\n")
    L.append("species_now = N_now x concurrent hominin-grade species per tool world (log-uniform 1-5, best 2.38, from Smithsonian date spans); "
             "species_ever = N_ever x cumulative species per tool world (uniform 8-16, best 15). The factor multiplies species, not worlds.\n")
    L.append("| scenario | median worlds now | median species now | species 10th-90th | mean species now | median worlds ever | median species ever | best-estimate species now |")
    L.append("|---|---|---|---|---|---|---|---|")
    for k, s in S.items():
        if "species_now" not in s: continue
        a, b = s["N_now"], s["species_now"]
        e = s.get("species_ever"); ne = s.get("N_ever")
        L.append(f"| {k} | {fmt(a['median'])} | {fmt(b['median'])} | {fmt(b['p10'])} – {fmt(b['p90'])} | {fmt(b['mean'])} | {fmt(ne['median']) if ne else '–'} | {fmt(e['median']) if e else '–'} | {fmt(s['best']['species_now']) if 'best' in s and 'species_now' in s['best'] else '–'} |")
    for k, s in S.items():
        if "similarity_variants" not in s: continue
        L.append(f"\n## Similarity-weight variants — {k}\n")
        L.append("p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). " +
                 ("Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).\n" if s.get("model_version") == "v2" else "Exact rescaling of the same draws (N is linear in the weight).\n"))
        L.append("| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |")
        L.append("|---|---|---|---|---|---|---|---|")
        for v, d in s["similarity_variants"].items():
            a = d["N_now"]
            L.append(f"| {v} | {d['w_median']:.3f} | {fmt(a['median'])} | {fmt(a['mean'])} | {fmt(a['p10'])} – {fmt(a['p90'])} | {a['P_lambda_lt1']:.3f} | {a['P_between_1_and_3']:.3f} | {fmt(d['N_ever_median'])} |")
    if "nathan_factor_effects" in S:
        pf = S["nathan_factor_effects"]
        L.append("\n## nathan_headline: effect of each new factor (paired draws: %s)\n" % pf["paired_draws"])
        L.append("| comparison | median N_now of comparison | nathan_headline median / comparison median | per-sample log10(N_headline/N_comparison): median [10th, 90th] |")
        L.append("|---|---|---|---|")
        lab = {"nathan_headline_no_superhab": "without superhabitability (tool-use change only)", "nathan_headline_no_tooluse": "without cross-lineage tool use (superhab only)", "similarity_weighted": "without both (= similarity_weighted, v1 model)"}
        for t, d in pf.items():
            if t == "paired_draws": continue
            L.append(f"| {lab[t]} | {fmt(d['median_N'])} | ×{d['ratio_of_medians']:.2f} | " + (f"{d['persample_log10_ratio_median']:.3f} [{d['p10']:.3f}, {d['p90']:.3f}] |" if d.get("paired") else "n/a (independent draws; compare medians) |"))
    v2 = [k for k, s in S.items() if "by_type" in s]
    if v2:
        L.append("\n## Multi-spectral breakdown (v2 model: M/K/G/F host classes)\n")
        L.append("Each host type has its own star fraction (RECONS / Kroupa IMF), eta-Earth, habitable window, exomoon-host giants, activity/UV/tidal penalties, "
                 "similarity weight (own Archive ESI list if >= 3 HZ rocky planets, else pooled) and, for K only, the superhabitability boost. "
                 "Share = that type's fraction of the posterior-mean N_now; median share = per-sample median.\n")
        L.append("| scenario | host type | median N_now | 10th–90th | mean | P(N<1) | share of mean N | median share [10th, 90th] | median N_ever | best-estimate N_now | similarity weight (median) |")
        L.append("|---|---|---|---|---|---|---|---|---|---|---|")
        for k in v2:
            for c, d in S[k]["by_type"].items():
                a = d["N_now"]
                L.append(f"| {k} | {c} | {fmt(a['median'])} | {fmt(a['p10'])} – {fmt(a['p90'])} | {fmt(a['mean'])} | {a['P_lambda_lt1']:.3f} | {100*d['share_of_mean']:.1f}% | {100*d['share_median']:.1f}% [{100*d['share_p10']:.1f}, {100*d['share_p90']:.1f}] | {fmt(d['N_ever']['median'])} | {fmt(d['best_N_now'])} | {fmt(d['w_similarity_median']) if d['w_similarity_median'] is not None else '–'} |")
            a = S[k]["N_now"]
            L.append(f"| {k} | **all** | {fmt(a['median'])} | {fmt(a['p10'])} – {fmt(a['p90'])} | {fmt(a['mean'])} | {a['P_lambda_lt1']:.3f} | 100% | – | {fmt(S[k]['N_ever']['median'])} | {fmt(S[k]['best']['N_now'])} | – |")
        try:
            E = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "esi_hz.json")))
            L.append("\nTop Archive planets by ESI per host type (Kopparapu+2014 HZ, R < 1.8 R_earth; conservative / optimistic counts):\n")
            L.append("| type | n (cons / opt) | top planets, optimistic HZ (ESI) | best outside the HZ cut (R<1.8; ESI, insolation S) |")
            L.append("|---|---|---|---|")
            for c in ("M", "K", "G", "F"):
                bo, bc = E["optimistic"]["by_type"][c], E["conservative"]["by_type"][c]
                tops = ", ".join(f"{t['pl_name']} ({t['ESI4']:.3f})" for t in bo["top"]) or "none"
                anyt = ", ".join(f"{t['pl_name']} ({t['ESI4']:.3f}, S={t['S']:.2f})" for t in E["top_any_orbit_R_lt_1p8_by_type"][c][:3] if t["pl_name"] not in bo["names"]) or "–"
                L.append(f"| {c} | {bc['n']} / {bo['n']} | {tops} | {anyt} |")
        except Exception as ex:
            L.append(f"(ESI per-type table unavailable: {ex})")
    v2s = [k for k, s in S.items() if "stages" in s]
    if v2s:
        L.append("\n## Multiphase breakdown (v2 model: civilisation stages)\n")
        L.append("Stage chain inside each tool-using episode: lithic -> agricultural -> industrial -> radio-capable -> spacefaring (orbital spaceflight). "
                 "Advance times log-uniform Earth/10..Earth x10 (Earth: 3.29 Myr, 11.2 kyr, 135 yr, 62 yr); stage collapse hazards (agri 1e-7..1e-3/yr, industrial 1e-6..1e-2/yr ASSUMED; "
                 "radio and spacefaring 1e-10..1e-2/yr = 1/L with SDO 2018's L 1e2..1e10 yr); a uniform(0,1) fraction of collapses regresses one stage and can recur, the rest end the lineage. "
                 "N per stage = N_now x long-run share of tool-using time in that stage (stationary approximation).\n")
        L.append("| scenario | stage | median N_now | 10th–90th | mean | P(N<1) | median share of tool-using time [10th, 90th] | best-estimate N_now |")
        L.append("|---|---|---|---|---|---|---|---|")
        for k in v2s:
            for st, d in S[k]["stages"].items():
                a = d["N_now"]
                L.append(f"| {k} | {st} | {fmt(a['median'])} | {fmt(a['p10'])} – {fmt(a['p90'])} | {fmt(a['mean'])} | {a['P_lambda_lt1']:.3f} | {fmt(d['phi_median'])} [{fmt(d['phi_p10'])}, {fmt(d['phi_p90'])}] | {fmt(d['best_N_now'])} |")
            r = S[k]["radio_capable"]; a = r["N_now"]
            L.append(f"| {k} | **radio-capable (radio + spacefaring)** | {fmt(a['median'])} | {fmt(a['p10'])} – {fmt(a['p90'])} | {fmt(a['mean'])} | {a['P_lambda_lt1']:.3f} | – | {fmt(r['best_N_now'])} |")
        L.append("\nRadio-capable N vs classic SETI-style Drake: Sandberg, Drexler & Ord 2018's 'current knowledge' sketch gives median N = 0.32, mean 27 million, P(N<1) = 52% (communicating civilisations; their Table 1). "
                 f"This model's static SDO-style stone-age variant: median {fmt(S['classic_static_SDO_style']['N_now']['median'])}.\n")
        L.append("| scenario | median episode length (yr) [10th, 90th] | radio-capable: median NN distance (ly) | top drivers of radio-capable N (swing, dex) |")
        L.append("|---|---|---|---|")
        for k in v2s:
            e = S[k]["L_episode_yr"]; r = S[k]["radio_capable"]
            sp_ = r.get("spacing", {}).get("median", {})
            nn = (fmt(sp_.get("nn_median_ly")) + (" (N<1)" if sp_.get("N", 0) < 1 else "")) if sp_ else "–"
            L.append(f"| {k} | {fmt(e['median'])} [{fmt(e['p10'])}, {fmt(e['p90'])}] | {nn} | " + "; ".join(f"{o['param']} {o['swing']:.1f}" for o in r["sens"][:5]) + " |")
    L.append("\n## Spacing: equal-cube side and median nearest-neighbour distance (disk volume ~7.9e12 ly³, user-supplied)\n")
    L.append("Cube side = (V/N)^(1/3). Nearest-neighbour: random (Poisson) placement; 3D median r = (3 ln2/(4πn))^(1/3), or the thin-disk 2D form when r exceeds the 1,000-ly thickness (R = 50,000 ly). Values for N < 1 mean no neighbour is expected; they are shown only formally.\n")
    L.append("| scenario | median N | cube side at median (ly) | median NN distance at median (ly) | regime | NN at 90th-pct N (ly) | NN at 10th-pct N (ly) |")
    L.append("|---|---|---|---|---|---|---|")
    for k, s in S.items():
        if "spacing" not in s: continue
        m_, hi_, lo_ = s["spacing"]["median"], s["spacing"]["p90"], s["spacing"]["p10"]
        flag = lambda d: (fmt(d["nn_median_ly"]) + (" (N<1: none expected)" if d["N"] < 1 else "")) if d["nn_median_ly"] else "–"
        L.append(f"| {k} | {fmt(m_['N'])} | {fmt(m_['cube_side_ly'])} | {flag(m_)} | {m_['regime']} | {flag(hi_)} | {flag(lo_)} |")
    L.append("\n## Comparison with the user's claims\n")
    L.append("| scenario | median N_now | P(1<=N_now<=3) ('1-3 at a time') | P(N_now>=1) | median N_ever by now | P(50<=N_ever<=100) | P(N_ever>=50) |")
    L.append("|---|---|---|---|---|---|---|")
    for k, s in S.items():
        if "P_N_ever_50_100" in s:
            L.append(f"| {k} | {fmt(s['N_now']['median'])} | {s['N_now']['P_between_1_and_3']:.3f} | {s['P_N_now_ge_1']:.3f} | {fmt(s['N_ever']['median'])} | {s['P_N_ever_50_100']:.3f} | {s['P_N_ever_ge_50']:.3f} |")
    if "exomoon_effect" in S:
        e = S["exomoon_effect"]
        L.append(f"\n## Exomoon effect (paired, same draws)\nMedian N_now with exomoons {fmt(e['median_with'])} vs without {fmt(e['median_without'])}; "
                 f"per-sample log10(N_with/N_without): median {e['median_log10_ratio']:.3f} dex, 90th pct {e['p90_log10_ratio']:.3f}, 99th pct {e['p99_log10_ratio']:.3f}. "
                 + (f"Median share of habitable bodies that are moons: " + (", ".join(f"{c} {fmt(d['exomoon_share_median'])}" for c, d in S['baseline']['by_type'].items()) if 'by_type' in S['baseline'] else f"G/K {fmt(S['baseline'].get('exomoon_share_gk_median'))} (90th pct {fmt(S['baseline'].get('exomoon_share_gk_p90'))})") + ".\n"))
    L.append("\n## Deterministic best-estimate point calculations\n")
    L.append("All parameters at their `best` values; hard-step expected times set equal to Earth's observed intervals (a 'Copernican / Earth-is-typical' choice).\n")
    L.append("| scenario | N_now | time-avg N | N_ever by now | fraction from Sun-like hosts (v1: G/K; v2: F/G/K) |")
    L.append("|---|---|---|---|---|")
    for k, s in S.items():
        if "best" in s:
            b = s["best"]
            L.append(f"| {k} | {fmt(b['N_now'])} | {fmt(b['N_timeavg'])} | {fmt(b['N_ever'])} | {fmt(b['frac_gk'])} |")
    for k, s in S.items():
        if "sens" not in s: continue
        L.append(f"\n## Sensitivity — {k}\n")
        L.append(f"ESS = {s['ess']:.0f} of {s['n']} samples. Median share of N_now from G/K hosts: {fmt(s['frac_gk_median'])}. "
                 f"Median epoch of peak N(t): {fmt(s['t_peak_median_gyr_ago'])} Gyr ago. Median mean-age of habitable planets: {fmt(s['mean_planet_age_median'])} Gyr.")
        if "post_P_tau_abio_lt_1Gyr" in s:
            L.append(f"P(tau_abiogenesis<1 Gyr): prior {s['prior_P_tau_abio_lt_1Gyr']:.2f} -> posterior {s['post_P_tau_abio_lt_1Gyr']:.2f}; "
                     f"posterior P(tau_intelligence<5 Gyr) = {s['post_P_tau_intel_lt_earthwindow']:.2f}.\n")
        L.append("| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |")
        L.append("|---|---|---|---|---|")
        for o in s["sens"]:
            L.append(f"| {o['param']} | {o['spearman']:+.3f} | {o['med_low']:.2f} | {o['med_high']:.2f} | {o['swing']:.2f} |")
    open(os.path.join(outdir, "results_summary.md"), "w").write("\n".join(L) + "\n")
