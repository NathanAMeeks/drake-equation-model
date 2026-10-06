"""Markdown for the v2 (multi-spectral M/K/G/F + multiphase stages) breakdowns. Shared by update_readme.py and build_readme.py."""
import json, os

def fmt(x):
    if x is None: return "–"
    try:
        if x != x: return "n/a"
    except Exception: pass
    if x == 0: return "0"
    if 1e-3 <= abs(x) < 1e5: return f"{x:.3g}"
    return f"{x:.2e}"

def rng_(s):
    d = s["dist"]
    if d == "fixed": return f"fixed {s['value']}"
    if d in ("uniform", "loguniform", "one_plus_loguniform"): return f"{d} [{s['low']}, {s['high']}]"
    if d == "normal": return f"normal {s['mean']} ± {s['sd']}"
    return d

def cell(x): return str(x).replace("|", "/").replace("\n", " ")

def variable_rows(cfg):
    """Variables-table rows for the v2 parameters."""
    rows = []
    for c, d in cfg["star_classes"]["classes"].items():
        for fld, nm in (("f_star", f"f_star_{c}"), ("ne", f"ne_{c}"), ("th_gyr", f"th_{c}_gyr"), ("n_giant_hz", f"n_giant_hz_{c}")):
            s = d[fld]
            rows.append(f"| `{nm}` | {rng_(s)} | {s.get('best', {'loguniform': 'geometric mean', 'uniform': 'midpoint'}.get(s['dist'], 'default'))} | {cell(s.get('unit', ''))} (v2 multi-spectral) | {cell(s.get('source', ''))} — {cell(s.get('url', ''))} |")
    for k, s in cfg["multiphase"]["params"].items():
        rows.append(f"| `{k}` | {rng_(s)} | {s.get('best', {'loguniform': 'geometric mean', 'uniform': 'midpoint'}.get(s['dist'], 'default'))} | {cell(s.get('unit', ''))} (v2 multiphase) | {cell(s.get('source', ''))} — {cell(s.get('url', ''))} |")
    return rows

def section(S, cfg, E, head, lit, v1=None, level="##", img_prefix="results/"):
    v2 = [k for k, s in S.items() if isinstance(s, dict) and s.get("model_version") == "v2"]
    scens = [x for x in (head, lit) if x in S and "by_type" in S[x]]
    if not scens: return ""
    L = [f"{level} Multi-spectral and multiphase breakdowns (v2 model)\n"]
    L.append("Suggested by a friend of Nathan's (Oct 2026). Re-run with the v2 model (2e5 samples each): " + ", ".join(f"`{k}`" for k in v2) +
             ". Every other scenario is still the v1 model (two host classes, G/K and M, and one stone-age-or-greater phase).\n")
    if v1:
        ch = []
        for k in scens:
            if k in v1 and "N_now" in v1[k]:
                ch.append(f"`{k}` {fmt(v1[k]['N_now']['median'])} (v1) → {fmt(S[k]['N_now']['median'])} (v2)")
        if ch: L.append("Change in the median N_now from v1 to v2: " + "; ".join(ch) + ". The v2 total adds F stars, splits G from K (K now has its own, higher η⊕ and longer habitable window), "
                        "adds K-activity and F-UV penalties and per-type ESI weights, and adds stage-specific collapse hazards after the lithic stage.\n")
    L.append(f"![Multi-spectral breakdown]({img_prefix}spectral_breakdown.png)\n")
    L.append(f"{level}# By host star type\n")
    L.append("Each type has its own star fraction (RECONS and Gaia-EDR3 10-pc censuses vs Kroupa IMF), η⊕, habitable window, HZ giants for exomoons, activity/UV/tidal penalties, and similarity weight "
             "(its own Archive ESI list if it has ≥ 3 HZ rocky planets, otherwise the pooled list). The superhabitability boost applies only to K hosts. "
             "*Share* = that type's fraction of the posterior-mean N; *median share* = per-sample median of the type's fraction.\n")
    L.append("| scenario | host type | median N now | 10th–90th pct | P(N<1) | share of mean N | median share [10th, 90th] | median N ever |")
    L.append("|---|---|---|---|---|---|---|---|")
    for k in scens:
        for c, d in S[k]["by_type"].items():
            a = d["N_now"]
            L.append(f"| {k} | {c} | **{fmt(a['median'])}** | {fmt(a['p10'])} – {fmt(a['p90'])} | {a['P_lambda_lt1']:.3f} | {100*d['share_of_mean']:.1f}% | {100*d['share_median']:.1f}% [{100*d['share_p10']:.1f}, {100*d['share_p90']:.1f}] | {fmt(d['N_ever']['median'])} |")
        a = S[k]["N_now"]
        L.append(f"| {k} | **all** | **{fmt(a['median'])}** | {fmt(a['p10'])} – {fmt(a['p90'])} | {a['P_lambda_lt1']:.3f} | 100% | – | {fmt(S[k]['N_ever']['median'])} |")
    L.append("\n**Top Archive planets by ESI, per host type** (Kopparapu+2014 HZ, R < 1.8 R⊕; Schulze-Makuch+2011 4-property ESI):\n")
    L.append("| type | HZ rocky planets (conservative / optimistic) | top planets, optimistic HZ (ESI) | best R < 1.8 planets outside the HZ cut (ESI, insolation S⊕) |")
    L.append("|---|---|---|---|")
    for c in ("M", "K", "G", "F"):
        bo, bc = E["optimistic"]["by_type"][c], E["conservative"]["by_type"][c]
        tops = ", ".join(f"{t['pl_name']} ({t['ESI4']:.3f})" for t in bo["top"]) or "none"
        anyt = ", ".join(f"{t['pl_name']} ({t['ESI4']:.3f}, S={t['S']:.2f})" for t in E["top_any_orbit_R_lt_1p8_by_type"][c] if t["pl_name"] not in bo["names"])
        anyt = ", ".join(anyt.split(", ")[:6]) if anyt else "–"
        L.append(f"| {c} | {bc['n']} / {bo['n']} | {tops} | {anyt} |")
    L.append("\n" + f"![Multiphase breakdown]({img_prefix}stage_breakdown.png)\n")
    L.append(f"{level}# By civilisation stage\n")
    mp = cfg["multiphase"]
    L.append("Inside each tool-using episode a world moves through **lithic → agricultural → industrial → radio-capable → spacefaring** (orbital spaceflight). "
             "Each advance is an exponential waiting time. From stage 2 on, a stage-specific collapse hazard applies: a fraction q regresses one stage (and can recur later), and the rest ends the lineage. "
             "The baseline end-of-lineage hazards (intrinsic lifetime, Big-Five extinctions, GRB/SN, self-inflicted) apply in every stage. "
             "N in a stage = N_now × the long-run share of tool-using time spent in that stage.\n")
    L.append("| stage parameter | prior | Earth anchor / best | source |")
    L.append("|---|---|---|---|")
    for k, s in mp["params"].items():
        dflt = {"loguniform": "geometric mean", "uniform": "midpoint"}.get(s["dist"], "default")
        L.append(f"| `{k}` | {rng_(s)} | {s.get('best', dflt)} | {cell(s['source'])} |")
    L.append("")
    L.append("| scenario | stage | median N now | 10th–90th pct | mean | P(N<1) | median share of tool-using time [10th, 90th] |")
    L.append("|---|---|---|---|---|---|---|")
    for k in scens:
        if "stages" not in S[k]: continue
        for st, d in S[k]["stages"].items():
            a = d["N_now"]
            L.append(f"| {k} | {st} | **{fmt(a['median'])}** | {fmt(a['p10'])} – {fmt(a['p90'])} | {fmt(a['mean'])} | {a['P_lambda_lt1']:.3f} | {fmt(d['phi_median'])} [{fmt(d['phi_p10'])}, {fmt(d['phi_p90'])}] |")
        r = S[k]["radio_capable"]; a = r["N_now"]
        L.append(f"| {k} | **radio-capable (radio + spacefaring)** | **{fmt(a['median'])}** | {fmt(a['p10'])} – {fmt(a['p90'])} | {fmt(a['mean'])} | {a['P_lambda_lt1']:.3f} | – |")
    cs = S.get("classic_static_SDO_style", {}).get("N_now", {})
    L.append("\n**Radio-capable N vs classic SETI-style Drake estimates.** ")
    parts = []
    for k in scens:
        if "radio_capable" not in S[k]: continue
        r = S[k]["radio_capable"]; sp = r.get("spacing", {}).get("median", {})
        nn = f"; median nearest-neighbour distance at the median ≈ {fmt(sp.get('nn_median_ly'))} ly" if sp.get("nn_median_ly") and sp.get("N", 0) >= 1 else ("; below 1, so no radio neighbour is expected at the median" if sp else "")
        parts.append(f"`{k}`: median **{fmt(r['N_now']['median'])}** radio-capable worlds now (10th–90th {fmt(r['N_now']['p10'])} – {fmt(r['N_now']['p90'])}, P(N<1) = {r['N_now']['P_lambda_lt1']:.2f}{nn}); "
                     f"top drivers: " + ", ".join(f"{o['param']} ({o['swing']:.1f} dex)" for o in r["sens"][:4]))
    L.append("* " + "\n* ".join(parts))
    L.append(f"* Sandberg, Drexler & Ord 2018 (arXiv:1806.02404), 'current knowledge' sketch for communicating civilisations: median N = 0.32, mean 27 million, P(N<1) = 52%. This repo's static SDO-style stone-age variant: median {fmt(cs.get('median'))}.")
    L.append("* Radio-only (radio but not yet spacefaring) is a very short stage here, because Earth went from radio to orbital spaceflight in 62 years. Almost all radio-capable worlds are therefore in the spacefaring stage.\n")
    return "\n".join(L) + "\n"

def caveats():
    return """* **Multi-spectral (v2).** The K-activity and F-UV penalties, the F-star HZ-giant rate, and the mass bins behind the Kroupa fractions are ASSUMED. The F-star η⊕ low end is scaled from the Kepler F/G small-planet occurrence ratio (Kunimoto & Matthews 2020), not measured in the HZ; K and F habitable windows are continuously-habitable-zone durations from Cuntz & Guinan 2016. Per-type ESI lists are tiny (M 22, K 3, G 1, F 0 conservative HZ planets), so G and F use the pooled list. The K share comes mainly from K stars being ~1.4–4.5× more common than G stars with a higher η⊕ range, and from the M-dwarf penalties; the K-only superhabitability boost moves the K share by only ~2–3 percentage points.
* **Multiphase (v2).** Stage advance times are Earth/10 to Earth×10 around one Earth history; the agricultural and industrial collapse hazards and the regress fraction are ASSUMED; the radio and spacefaring hazards reuse Sandberg, Drexler & Ord 2018's 1e2–1e10 yr lifetime prior. Stage shares use the long-run (stationary) occupancy of the stage chain, which ignores worlds that started their tool-using phase within the last few Myr. The stage-specific hazards are added on top of the v1 self-inflicted hazard `r_self_per_gyr`, so some self-inflicted risk may be counted twice (conservative for N).
"""
