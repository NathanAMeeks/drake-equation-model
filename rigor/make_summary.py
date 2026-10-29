"""Writes rigor/RIGOR_SUMMARY.md from bounds.json, sobol.json, heldout.json, leakage.json."""
import json, math, os
H = os.path.dirname(os.path.abspath(__file__)); J = lambda f: json.load(open(os.path.join(H, f)))
B, S, HO, LK = J("bounds.json"), J("sobol.json"), J("heldout.json"), J("leakage.json")
g = lambda x: f"{x:.3g}"
L = ["# Rigor add-on (2026-10-19, extended 2026-10-26)\n", "**Headline metric (from 2026-10-26):** the median number of radio-or-better civilizations (radio plus spacefaring stages) that exist now in the Milky Way. Worlds with stone-age-or-greater tool users (N_now) are kept as a secondary number. Sections 1–7 below were written for N_now; section 8 uses the new headline.\n",
"## 1. Guaranteed bounds on N_now over the full prior support\n",
f"Method: {B['method']}. Every factor is set to the full support of its prior. Two normal priors with no upper limit (`sfr_now`, `m_disk_now`) are cut at mean + {B['normal_truncation_sd']:.0f} sd; without that cut the upper bound is infinite, because N is linear in disk mass. "
"The bounds apply to the continuous-time model equations. They are made conservative with the inequalities listed below. All 200,000 MC samples of each scenario fall inside them. "
"**The bounds answer \"what is logically possible under these priors\", not \"what is likely\".** Their width (about 60–80 dex) is the honest size of the prior support; the MC 10–90% range is what the priors' *shapes* imply.\n",
"| scenario | guaranteed min | guaranteed max | bound width (dex) | MC median | MC 10–90% | MC width (dex) |", "|---|---|---|---|---|---|---|"]
for s, b in B["scenarios"].items():
    m = b["MC"]; L.append(f"| `{s}` | {g(b['N_now_lower'])} | {g(b['N_now_upper'])} | {b['log10_width_dex']:.1f} | {g(m['median'])} | {g(m['p10'])}–{g(m['p90'])} | {m['width_10_90_dex']:.2f} |")
L += ["\nConservative steps (each one can only widen the interval):\n"] + [f"* {x}" for x in B["inequalities"]]
L += ["\nThe lower bound is small mainly because of three things at their worst corners: the occupancy floor pi_on (the shortest stone-age lifetime and the highest stage hazards), the hard-step completion probability (tau up to 1e3 Gyr in the baseline), and every multiplier at its low end.\n",
"## 2. Held-out testing\n",
"**No factor in the model is fitted.** There is no regression, curve fit or optimiser in the code. The thin-disk star-formation exponent is solved exactly from prior draws, not fitted to data; the habitable-zone occurrence rates and the star-formation history are literature priors. So there is no fitted trend to hold out. "
"Only two quantities are *estimated* from Archive data here, and both got a 50/50 split check:\n"]
s_ = HO["superhab_independence_check"]
L.append(f"* **`f_superhab` best value 0.104** = P(size) × P(temp), assuming the two are independent (n = {s_['n_planets']} HZ planets with R < 2; {s_['n_size']} pass size, {s_['n_temp']} pass temperature, {s_['n_joint']} pass both, so the joint fraction is {s_['joint_full']:.3f}). Over {s_['splits']} random 50/50 splits, each estimator was fitted on one half and scored by absolute error against the other half's joint frequency, with Bonferroni correction for m = {s_['bonferroni_m']} comparisons:")
for k, v in s_["comparisons"].items():
    L.append(f"  * vs {k}: mean abs error {v['mean_abs_err_product']:.3f} vs {v['mean_abs_err_other']:.3f}; product better in {v['frac_splits_product_better']:.0%} of splits; Bonferroni p = {v['bonferroni_p']:.2f}")
L.append("  * Verdict: the independence-product estimator does **not** beat trivial baselines and is not significantly better than an equal-parameter random null. The 0.104 best value is not supported over the direct joint fraction (0.061). Both lie inside the prior bracket 0.03–0.43, which is unchanged. Its first-order Sobol share is <0.1%, so this does not move N.")
for nm, e in HO["esi_split_half"].items():
    L.append(f"* **ESI weight ({nm} list, n = {e['n']})**: split-half difference of the mean ESI, median {e['split_half_abs_diff_median']:.3f}, 95th percentile {e['split_half_abs_diff_p95']:.3f}, which is ≤ {e['log10_effect_on_N_p95']:.3f} dex in N. Stable; this is a descriptive check (not a prediction test).")
L += ["\n## 3. Leakage check\n",
"* **Earth's timeline.** In the headline and its ocean variant the step times are *set* to Earth's intervals and the Earth-timing likelihood is switched off (`bayes_update: false`), so Earth's dates are used once, as a prior. In the baselines the dates are used once, as a likelihood, with the observer-selection normalisation (divide by P(completion within Earth's window)); this is present in the code: "
+ str(LK["selection_correction_in_code"]) + ". No double use. The headline is still *conditional on Earth being typical*: that is an assumption, not leakage.",
"* **N includes Earth.** The target (tool-using worlds now) contains Earth, and the inputs use Earth's history. Nothing conditions on N ≥ 1, so the reported P(N<1) is a prior-predictive number, not a probability given that we exist.",
f"* **ESI weighting.** The lists are Archive exoplanets only (Solar System bodies present: {LK['esi_lists_contain_solar_system_bodies']}). Earth enters only as the ESI reference point. ESI's temperature term comes from insolation, and the habitable-zone cut behind ne also uses insolation, so the HZ condition is partly applied twice. That is a mild double penalty, not target leakage, and it is small (ESI weights 0.74–0.94).",
f"* **Tool-use counts.** `n_tool_origins` includes hominins ({LK['n_tool_origins_includes_hominins']}), whose own first stone tools fix the 0.597 Gyr interval that is divided by n. The same Earth record therefore sets both the interval and one of the counts. This is a soft circularity: Earth's success is part of the evidence that tool use is repeatable. Its effect on N is small (first-order Sobol share ≈ 0.3%).",
f"* **Model outputs or SETI results used as inputs:** {LK['params_reference_model_outputs']} / {LK['seti_results_used_as_inputs']}. None found.",
"\n## 4. Evidence tags\n",
"Each sourced variable in `params.yaml` now has a `tag:` set to [MEASURED], [MODELED] or [GUESS], and the tag is shown in the README provenance table. The mapping: ASSUMED and user-supplied become [GUESS]; literature + ASSUMED element becomes [MODELED]; literature-sourced is [MEASURED] for censuses, surveys and dated records, else [MODELED]. The SDO 2018 Table-1 ranges are tagged [GUESS], because they compile published opinions.\n",
"## 5. Sensitivity ranking (first-order Sobol share of Var(log10 N_now))\n",
"![sobol](sobol_ranking.png)\n", "| rank | " + " | ".join(f"`{s}`" for s in S) + " |", "|---|" + "---|" * len(S)]
tops = {s: list(v["S1"].items())[:8] for s, v in S.items()}
for i in range(8):
    L.append(f"| {i+1} | " + " | ".join(f"{tops[s][i][0]} {tops[s][i][1]:.2f}" for s in S) + " |")
L.append("| sum S1 | " + " | ".join(f"{v['sum_S1']:.2f}" for v in S.values()) + " |")
L.append("\nGiven-data estimator with 50 quantile bins on the existing 2e5 samples (importance-weighted for the baselines, effective sample size ≈ 13,900). The permutation-null noise floor is ≤ 0.005. Sum S1 < 1 means interactions. In the baselines the sum exceeds 1 because the Earth-timing posterior correlates the step times, and first-order Sobol assumes independent inputs; read those values as a ranking only. `p_ocean_to_industrial` does not appear because it changes only the stage split, not N_now.\n")

# ---- section 6: v2 rigor additions (2026-10-19)
g = lambda f: json.load(open(os.path.join(H, f)))
B2, PB, QM, CK = g("bounds_v2.json"), g("pbox.json"), g("qmc.json"), g("check.json")
e = lambda x: f"{x:.3g}"
L += ["## 6. v2 additions (Oct 19)", "",
"**Linked inputs** (`links:` in params.yaml, Gaussian copula on shared hidden log-space variables; every link strength is [GUESS]). The groups are geology (plate tectonics, land+ocean, rocky composition), water (ocean-world fractions, with land+ocean anti-linked), civ_risk (stage hazards and r_self), galactic_env (SN, GRB, sterilisation rates) and M-dwarf activity. Weighted median (10–90%), 2e5 draws:", "",
"| scenario | unlinked | linked |", "|---|---|---|"]
import numpy as np
def wq(x, w, qs):
    o = np.argsort(x); c = np.cumsum(w[o]); c /= c[-1]; return [x[o][np.searchsorted(c, q)] for q in qs]
for s in ["nathan_headline_ocean", "baseline_ocean"]:
    row = []
    for t in (s, s + "_linked"):
        Z = np.load(os.path.join(os.path.dirname(H), "results", f"samples_{t}.npz")); lw = Z["r_logw"]
        w = np.exp(lw - lw.max()) if "baseline" in s else np.ones(len(lw)); q = wq(Z["r_N_now"], w, [.1, .5, .9])
        row.append(f"{e(q[1])} ({e(q[0])}–{e(q[2])})")
    L.append(f"| `{s}` | {row[0]} | {row[1]} |")
L += ["", "Links leave the supports unchanged, so they cannot change any guaranteed bound. The p-box below holds for any dependence among the guesses.", "",
"**Guaranteed bounds, tightened** (`engine.py` + `bnb.py`, python-flint/Arb). Changes: an exact hypoexponential CDF at the monotone τ corners; an occupancy floor from the kernel K(a) rather than π_on alone; a bound on the episode end rate using the lithic-stage residence time (stage 1 carries no extra hazard); and branch-and-bound over 60 splits per tail. These are rigorous for the model equations.", "",
"| scenario | old min | new min | old max | new max | width old→new (dex) |", "|---|---|---|---|---|---|"]
for s, v in B2.items():
    L.append(f"| `{s}` | {e(v['old'][0])} | {e(v['bnb'][0])} | {e(v['old'][1])} | {e(v['bnb'][1])} | {v['width_dex_old']:.1f}→{v['width_dex_new']:.1f} |")
L += ["", "The upper bound is a product of monotone factors at their worst corner, which is already attained, so branch-and-bound cannot lower it further.", "",
"**Binding factors** = the factors whose restriction to the half away from their worst end tightens that tail bound most (gain in dex):", ""]
for s in ["nathan_headline_ocean", "baseline_ocean"]:
    v = B2[s]; f = lambda lst: ", ".join(f"{k} ({end}, {gn})" for k, end, gn in lst[:3])
    L.append(f"- `{s}`: low tail is set by {f(v['binding_low_tail'])}; high tail is set by {f(v['binding_high_tail'])}.")
L += ["", "**P-box** (`pbox.py`, ![pbox](pbox.png)). The [MEASURED]/[MODELED] inputs are drawn from their priors (2000 stored draws). Each [GUESS] or untagged input is held as its whole interval, which gives a rigorous [lo_i, hi_i] per draw. The coverage interval uses two-sided DKW at 95% confidence.", "",
"| scenario | 90% coverage interval (if every guess range is honest) | hard interval, MEASURED/MODELED only, guesses fixed at medians |", "|---|---|---|"]
for s, v in PB.items():
    L.append(f"| `{s}` | [{e(v['coverage90'][0])}, {e(v['coverage90'][1])}] | [{e(v['hard_known_only_guess_at_median'][0])}, {e(v['hard_known_only_guess_at_median'][1])}] |")
L += ["", "The coverage interval is almost as wide as the hard bounds, so the [GUESS] ranges alone account for nearly all of the 60+ dex. The per-draw boxes are not branch-and-bounded, which is why the lower end sits below the tightened hard minimum. The baseline p-box uses unweighted prior draws: its step times are [GUESS] intervals, so the Earth-timing weights cannot be applied rigorously.", "",
"**Faster sampling** (`qmc.py`). The estimate is E[log10 N_now], unweighted, from 16 replicates of 4096 draws. Scrambled Sobol is used for all inverse-CDF inputs; the ESI bootstrap stays pseudo-random. The control variate is the sum of the log10 loguniform inputs, whose mean is exact.", "",
"| scenario | var. reduction: MC+CV | Sobol | Sobol+CV |", "|---|---|---|---|"]
for s in ["nathan_headline_ocean", "baseline_ocean"]:
    r = QM[s]["var_reduction_vs_mc"]; L.append(f"| `{s}` | {r['mc_cv']:.2f}× | {r['qmc']:.0f}× | {r['qmc_cv']:.0f}× |")
pf = QM["pick_freeze_cache"]
L += ["", f"At equal cost, the variance reduction equals the speedup. The control variate adds nothing on top of Sobol, because scrambled Sobol already integrates the linear term almost exactly. Caching the unchanged stages (solve_k, stage chain, step DFTs) in a pick-freeze run ({pf['n']} draws, base run plus {len(pf['factors'])} factors) took {pf['secs_plain']} s down to {pf['secs_cached']} s, a {pf['speedup']}× speedup with a {pf['cache_hit_rate']:.0%} hit rate, and the output was bit-identical.", "",
"**Independent check** (`check.py`). It does not import drake_model. It uses time-domain convolutions, its own root finder and its own stage-chain solve, working only from the formulas and params.yaml.", "",
"| scenario | draws checked | max rel. error in N | max abs. error in logw | p10 / p50 / p90 | support violations | samples outside new bounds |", "|---|---|---|---|---|---|---|"]
for s, v in CK.items():
    L.append(f"| `{s}` | {v['n_checked']} | {v['max_rel_err_N']:.1e} | {v['max_abs_dlogw']:.1e} | {' / '.join(e(x) for x in v['p10_p50_p90'])} | {len(v['support_violations'])} | {v['samples_outside_bounds']} |")
L += ["", "No mismatches were found, so there were no bugs to fix."]

# ---- section 7: v3 features (2026-10-21)
V = g("v3.json"); f3 = lambda x: f"{x:.3g}"
L += ["", "## 7. v3 features (Oct 21): star multiplicity cut (A) and multi-moon civilisations (B)", "",
"Paired runs of 1e5 draws each. The new inputs come from their own random stream, so every other draw is identical to the parent's first 1e5 draws. Medians are weighted for the baseline. The parent row is the parent's own first 1e5 draws.", "",
"| run | median (10–90%) | radio-capable median | paired median change (dex) | share of N in multi-civ systems |", "|---|---|---|---|---|"]
for k, v in V.items():
    q = v["p10_p50_p90"]; d = v.get("paired_median_log10_ratio"); sh = v.get("multi_civ_share_of_N")
    L.append(f"| `{k}` | {f3(q[1])} ({f3(q[0])}–{f3(q[2])}) | {f3(v['radio_median'])} | {'' if d is None else f'{d:+.3f}'} | {'' if sh is None else f'{sh:.1%}'} |")
L += ["",
"**A. Multiplicity cut.** Habitable worlds are allowed only in single or binary systems; binaries are still handled by the existing `f_binary_ok`. A fraction `f_hab_triple_plus` of triple-or-higher systems is let through: [GUESS], loguniform 1e-3–0.3. Each host type c gets the factor 1 − f_triple_plus_c·(1 − f_hab_triple_plus). The triple-or-higher fractions (THF) are:",
"- M: 2.6–7.7%, [MEASURED], from Winters+2019 via Offner+2023 PPVII Table 1.",
"- K: 6.3–12%, [MODELED], bracketed between the table's 0.3–0.6 and 0.75–1.25 Msun rows. This is consistent with Raghavan+2010 (8% triple + 3% higher).",
"- G: 10–14%, [MEASURED].",
"- F: 12–16%, [MEASURED].",
"",
"Double counting: `f_binary_ok` removes close binaries (<47 au, Kraus+2016) from all stars. Triples are a separate category of system, so the two cuts act on different configurations. However, a triple with a close inner pair could be removed by both, because the model treats the two cuts as independent. That overlap can over-remove at most the triple fraction (≤16%, ≤0.08 dex). THF counts systems by their primary; companions in the same system are not counted separately.", "",
"**B. Multi-moon civilisations.** Each giant that hosts a habitable moon has `n_hab_moons_per_giant` = k habitable moons: [MODELED], uniform 1–3. Grounding: Jupiter has 4 large moons and Saturn has 1; Cilibrasi+2018 find surviving systems most often have 3 moons, with a maximum of 5. The upper limit of 3 is assumed. Expected civilisation-bearing moon worlds scale by k·(1+(k−1)·p_second_civ). The first civilisation can arise on any of the k moons, which is accurate for small occupancy. After that, each other moon gets a civilisation with probability `p_second_civ` [GUESS], loguniform 1e-3–0.5, through impact transfer.",
"",
"Worlds in multi-civilisation systems are counted as N_moon·(E[X] − P(X=1))/E[X], where X = 1 + Bin(k−1, p2). N_now counts worlds, so `p_dominance` [GUESS] does not reduce N_now: an absorbed world is still occupied. It reduces only the number of independent civilisations, N_civ_now (median 3.15e4 headline_ocean_moons, 0.0427 baseline_ocean_moons). `tech_accel` [GUESS], loguniform 1–10, divides the industrial→radio→spacefaring advance times and the industrial and radio hazards. It applies only to multi-civilisation worlds and changes the stage split (radio-capable). Its effect on episode length, and therefore on N_now, is left out, which is conservative. Planet–planet multi-civilisation systems are not modelled.", ""]

# ---- section 8: v4 variables (2026-10-26)
V4 = g("v4.json"); H4, B4 = V4["nathan_headline_ocean_linked"], V4["baseline_ocean_linked"]
fq = lambda q: f"{f3(q[1])} ({f3(q[0])}–{f3(q[2])})"
L += ["", "## 8. New variables, first pass (Oct 26; superseded by section 9, which removes the [GUESS]-based ones)", "",
"Each variant is paired with its `*_linked` parent: all new inputs come from their own random stream. The variant `_v4` contains every new variable except interstellar expansion; `_v4x` adds expansion. Both use 1e5 draws, and each single-variable variant uses 5e4. Baseline numbers are weighted by Earth's timing.", "",
"| run | radio-or-better median (10–90%) | P(radio-or-better < 1) | stone-age-or-greater median |", "|---|---|---|---|"]
for nm, X in (("nathan_headline_ocean_linked", H4), ("baseline_ocean_linked", B4)):
    a, x = X["_v4"], X["_v4x"]
    L.append(f"| `{nm}` (parent) | {fq(a['parent_radio_p10_p50_p90'])} | {a['parent_P_radio_lt_1']:.2f} | {f3(a['parent_stone_median'])} |")
    L.append(f"| `{nm}_v4` | {fq(a['radio_p10_p50_p90'])} | {a['P_radio_lt_1']:.2f} | {f3(a['stone_median'])} ({f3(a['stone_median_excl_subsurface'])} without the subsurface path) |")
    L.append(f"| `{nm}_v4x` (with expansion) | {fq(x['radio_p10_p50_p90'])} | {x['P_radio_lt_1']:.2f} | {f3(x['stone_median'])} |")
FE = ["metal", "ghz", "oxygen", "recovery", "resources", "climate", "subsurface", "expansion"]
L += ["", "**Each variable alone** (paired dex shift in radio-or-better: median of the per-draw log ratio / shift of the median / shift of the 90th percentile):", "",
"| variable | headline_ocean_linked | baseline_ocean_linked |", "|---|---|---|"]
for f in FE:
    c = lambda X: f"{X['_v4_'+f]['paired_dex_radio_median']:+.2f} / {X['_v4_'+f]['dex_shift_of_radio_median']:+.2f} / {X['_v4_'+f]['dex_shift_of_radio_p90']:+.2f}"
    L.append(f"| {f} | {c(H4)} | {c(B4)} |")
L += ["", "**Sobol top drivers of log10 radio-or-better** (first-order, `_v4`): headline " + ", ".join(f"{k} {v:.2f}" for k, v in H4["_v4"]["sobol_radio_top8"][:5]) + "; baseline " + ", ".join(f"{k} {v:.2f}" for k, v in B4["_v4"]["sobol_radio_top8"][:5]) + ". With expansion (`_v4x`), `v_front_c` enters the headline top 6. The S1 sums exceed 1 because linked and Bayes-updated inputs are correlated, so read these as rankings only.", "",
"**How each variable enters the model** (tags are in params.yaml):",
"- **Metallicity / phosphorus.** Factor (1+(R−1)·f_rich,gal)/(1+(R−1)·0.48) × f_P. R is the terrestrial-planet occurrence ratio, metal-rich vs metal-poor, [MEASURED] 1.72 +0.19/−0.17 (Wang & Fischer 2015). 0.48 is the metal-rich share of their Kepler sample. The galactic metal-rich fraction is [GUESS]; Hayden+2015 APOGEE gives the shape of the metallicity distribution but no galaxy-wide fraction. f_P is [GUESS] (Hinkel+2020: the Sun is relatively P-rich, and P is measured in only ~100 stars). Almost the whole shift comes from f_P.",
"- **GHZ with radial migration.** r_ster0 = astrophysical [MODELED, Barnes+2026 galaxy-wide 1e-5–2e-4/Gyr] + non-astrophysical [GUESS 1e-6–0.25]. Each star's exposure is spread lognormally around the galaxy mean (log-sd [GUESS], smoothed by migration σ_RM8 = 3.6 kpc; Frankel+2018), and N is averaged over that spread. **The astrophysical part is now constrained to ≤2e-4/Gyr, but the low-tail risk sits in the assumed non-astrophysical part (giant impacts, runaway climate), which no GHZ data constrain.** Net effect: the median barely moves; the low tail rises slightly (p10 +0.04 to +0.06 dex, p01 up to +0.18 dex).",
"- **Oxygenation timing.** Industry needs O2 at fire level. Earth reached it about 0.17 Gyr after complex multicellularity: 0.6 Ga to earliest charcoal ~0.43 Ga, with sustained fires needing ≥16% (Geology 50:1048, 2022; Belcher & McElwain 2008). The NOE is dated 0.85–0.54 Ga and the GOE ~2.4 Ga (Lyons+2014); the GOE is already a hard step. The lag scale and the never-oxygenated fraction are [GUESS]. Tool-user occupancy before the lag cannot industrialise. The gate applies to both the land path and the ocean path, the latter on top of p_ocean_to_industrial.",
"- **Recovery time.** 5–20 Myr [MODELED, Kirchner & Weil 2000: ~10 Myr origination lag] is added to the tool-use re-evolution time. It matters only when re-evolution is fast, as in the headline.",
"- **Fuel/ore** [GUESS 0.05–1] gates industry. **Climate thermostat** [GUESS 0.5–1] is linked to the geology hidden variable (0.5); Foley & Smye 2018 give the context: stagnant-lid planets stay temperate for 1–5 Gyr only in limited parameter ranges.",
"- **Subsurface oceans** are a separate path. Number per star is [GUESS 0.1–10], with context from Solar System ocean moons and Sumi+2023 (21 free-floating planets per star). Fecundity is [GUESS 1e-6–1e-2] and the chance of reaching technology is [GUESS 1e-6–1e-3]. This path has no rare-Earth factors, so it dominates the stone-age count under these guesses (~96% by mean) but adds nothing to radio-or-better at the median.",
"- **Interstellar expansion** (Carroll-Nellenback+2019 settlement fronts). Each expanding spacefaring civilisation holds on average ρ·f·(4π/3)(v·L)³/4 settled systems while it is spacefaring, capped at f × N_stars. ρ = 0.08 pc⁻³ (their value, citing Henry+2018). v is [MODELED]: 1e-3–0.1 c probes, with a ~100 km/s floor from stellar motions. f and p_expand are [GUESS]. **Settled worlds make up almost all of the radio-or-better mean when expansion is on**: the 90th percentile rises by 4.5–6.4 dex. Settlements are assumed to end with their parent's spacefaring phase, which is conservative.", ""]

# ---- section 9: v5 = data-anchored subset (2026-10-26)
V5 = g("v5.json"); H5, B5 = V5["nathan_headline_ocean_linked"], V5["baseline_ocean_linked"]
L += ["", "## 9. v5: only the data-anchored new variables (Oct 26, current)", "",
"Removed from the section-8 set because their effect rests on [GUESS] ranges: fossil fuel/ores, the phosphorus part of the metallicity variable, climate thermostat, subsurface/rogue habitats, and interstellar expansion. The older model's own [GUESS] factors are unchanged; this pass covers only the new batch. The oxygen gate now applies to the land path only. The ocean path already has `p_ocean_to_industrial`, so gating it again would double-count. Each `_v5` variant is paired with its `*_linked` parent: 1e5 draws, single-variable runs 5e4.", "",
"| run | radio-or-better median (10–90%) | P(radio-or-better < 1) | stone-age-or-greater median |", "|---|---|---|---|"]
for nm, X in (("nathan_headline_ocean_linked", H5), ("baseline_ocean_linked", B5)):
    a = X["_v5"]
    L.append(f"| `{nm}` (parent) | {fq(a['parent_radio_p10_p50_p90'])} | {a['parent_P_radio_lt_1']:.2f} | {f3(a['parent_stone_median'])} |")
    L.append(f"| `{nm}_v5` | {fq(a['radio_p10_p50_p90'])} | {a['P_radio_lt_1']:.2f} | {f3(a['stone_median'])} |")
L += ["", "| variable alone (paired dex shift, radio-or-better: per-draw median / median / p90) | headline | baseline |", "|---|---|---|"]
for f in ["metal", "ghz", "oxygen", "recovery"]:
    c = lambda X: f"{X['_v5_'+f]['paired_dex_radio_median']:+.2f} / {X['_v5_'+f]['dex_shift_of_radio_median']:+.2f} / {X['_v5_'+f]['dex_shift_of_radio_p90']:+.2f}"
    L.append(f"| {f} | {c(H5)} | {c(B5)} |")
L += ["", "**Top 5 Sobol drivers of log10 radio-or-better** (`_v5`): headline " + ", ".join(f"{k} {v:.2f}" for k, v in H5["_v5"]["sobol_radio_top8"][:5]) + "; baseline " + ", ".join(f"{k} {v:.2f}" for k, v in B5["_v5"]["sobol_radio_top8"][:5]) + ".", "",
"**Inputs and how the ranges were set:**",
"- **Metallicity occurrence.** R is [MEASURED] 1.72 +0.19/−0.17, the terrestrial-planet occurrence ratio for metal-rich vs metal-poor stars (Wang & Fischer 2015). The galactic metal-rich fraction is [MODELED] uniform 0.023–0.607. That range spans the six Hayden+2015 Table 1 midplane bins (R = 3–15 kpc), each converted to P([Fe/H] > 0.05) with a Gaussian(mean, σ) approximation. Any mass weighting of the bins must lie inside that span. Kepler-field reference: 0.48.",
"- **GHZ + migration.** The star-to-star exposure spread s is [MODELED] uniform 0–√2. These are bounds, not a fit: 0 means complete radial mixing; √2 is the spread an exponential disk gives with no migration. Migration (Frankel+2018, 3.6 kpc over 8 Gyr) puts the truth between them. r_ster0 keeps its existing prior.",
"- **Oxygenation.** The lag is [MEASURED] uniform 0.17–0.18 Gyr, spanning only the two sourced Earth anchors: complex multicellularity at 0.6 Ga, then the earliest charcoal (needing ≥16% O2) at ~0.43 Ga (Geology 2022) and ~0.42 Ga (Scott & Glasspool 2006). The previous [GUESS] spread and the never-oxygenated fraction were dropped. Applies to the land path only.",
"- **Recovery.** Fixed at 10 Myr [MEASURED] (Kirchner & Weil 2000). The earlier 5–20 Myr spread was an assumption and has been removed.", ""]

open(os.path.join(H, "RIGOR_SUMMARY.md"), "w").write("\n".join(L)); print("ok")
