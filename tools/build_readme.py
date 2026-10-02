#!/usr/bin/env python3
"""Regenerate README.md from params.yaml, results/results.json and data/*.json (run after analyze)."""
import json, os, yaml
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
cfg = yaml.safe_load(open("params.yaml")); S = json.load(open("results/results.json"))
E = json.load(open("data/esi_hz.json")); SH = json.load(open("data/superhab.json")); HZ = json.load(open("data/hz_counts.json"))
head = cfg["run"]["headline_scenario"]; lit = cfg["run"].get("literature_baseline", "baseline")
def fmt(x):
    if x is None: return "–"
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
H, B = S[head], S[lit]; h, b = H["N_now"], B["N_now"]
L = []
L.append("# Time-aware extended Drake equation: simultaneous stone-age-or-greater civilizations in the Milky Way\n")
L.append("*Model by Nathan A. Meeks.* A Monte Carlo, time-resolved Drake model that counts how many worlds in the Milky Way "
         "have stone-tool-using (or more advanced) life **at the same time as us**.\n")
L.append("## Headline\n")
L.append("| | Nathan's headline (`%s`) | Literature baseline (`%s`) |" % (head, lit))
L.append("|---|---|---|")
L.append(f"| **Median (50/50) worlds now, other than Earth** | **{fmt(h['median'])}** | **{fmt(b['median'])}** |")
L.append(f"| 10th–90th percentile | {fmt(h['p10'])} – {fmt(h['p90'])} | {fmt(b['p10'])} – {fmt(b['p90'])} |")
L.append(f"| Mean | {fmt(h['mean'])} | {fmt(b['mean'])} |")
L.append(f"| P(N < 1) | {h['P_lambda_lt1']:.3f} | {b['P_lambda_lt1']:.3f} |")
L.append(f"| Median tool-using species now | {fmt(H['species_now']['median'])} | {fmt(B['species_now']['median'])} |")
L.append(f"| Median worlds that ever had tool users (by now) | {fmt(H['N_ever']['median'])} | {fmt(B['N_ever']['median'])} |")
hs, bs = H["spacing"]["median"], B["spacing"]["median"]
L.append(f"| Median nearest-neighbour distance at the median N | {fmt(hs['nn_median_ly'])} ly | {fmt(bs['nn_median_ly'])} ly (N<1: no neighbour expected) |")
L.append(f"| Equal-cube side at the median N (disk ≈ 7.9e12 ly³) | {fmt(hs['cube_side_ly'])} ly | {fmt(bs['cube_side_ly'])} ly |")
L.append("\n![All scenarios compared](results/comparison_scenarios.png)\n")
L.append(f"Headline histogram: [`results/hist_log10N.png`](results/hist_log10N.png) · sensitivity tornado: [`results/tornado.png`](results/tornado.png) · "
         f"literature baseline: [`hist`](results/hist_log10N_baseline.png), [`tornado`](results/tornado_baseline.png)\n")
L.append("## Method\n")
L.append("""**Target.** Worlds hosting a lineage that habitually makes stone tools (Lomekwi/Oldowan level) or anything more advanced, alive *now*. Radio detectability does not enter: it changes what we can detect, not N.

1. **Star formation history of the disk.** A thick-disk phase 13.0–8.5 Gyr ago (≈ half the disk mass), then an exponential thin disk normalised to today's SFR and disk mass. This replaces a constant R\\*.
2. **Habitable bodies per star**, split into G/K and M hosts:
   * η⊕ from Kepler/Archive studies.
   * Rare-Earth multipliers: plate tectonics, land + ocean, large moon, Jupiter shield, binary stability, M-dwarf flares and tidal/water loss.
   * Galactic habitable zone and a metallicity ramp in time.
   * Habitable exomoons around HZ giants.
3. **Biology as hard steps:** abiogenesis → oxygenic photosynthesis → eukaryotes → complex multicellularity → stone-tool intelligence. Each step is an exponential waiting time, and their convolution competes with the host's habitable window.
4. **Duration and recurrence.** A tool-using phase ends through intrinsic lifetime, Big-Five-class extinctions, GRBs/supernovae and self-inflicted risk. It can re-evolve afterwards (an alternating renewal process). Whole-biosphere sterilisation scales with past star formation.
5. **Output.** N(t) on a 20-Myr grid over 13.8 Gyr. Reported: N now, time-averaged N, N_ever, and species = worlds × hominin-like species per tool world.

**Nathan's headline (`nathan_headline`).**
* **Similarity weighting.** Known Earth-like planets are treated as sharing Earth's evolutionary timeline as the *typical* case (each step's expected time equals Earth's observed interval), weighted by the Earth Similarity Index (Schulze-Makuch et al. 2011, ESI¹) of the NASA Exoplanet Archive's HZ rocky planets.
* **Superhabitability boost.** A boost of 1–3× (ASSUMED) applies to the fraction of G/K planets meeting the Schulze-Makuch, Heller & Guinan 2020 criteria.
* **Cross-lineage tool use.** Tool use evolved independently many times on Earth (primates, corvids, octopus, sea otters, dolphins, elephants). The animals → tools step is therefore modelled as fast and repeatable: Earth's 0.597-Gyr interval is divided by 3–7 independent origins.

**Literature baseline (`baseline`).** Hard-step expected times are log-uniform over 1e-3–1e3 Gyr, then updated on Earth's dated fossil record with the observer-selection correction of Snyder-Beattie et al. 2021, which favours slow, rare steps. **The choice between these two framings explains most of the ~6-orders-of-magnitude gap between the two headline numbers.**
""")
c, o = E["conservative"], E["optimistic"]
L.append(f"""**Archive inputs** (pscomppars, pulled 1 Oct 2026: {HZ['total_confirmed_rows']:,} confirmed planets):
* HZ rocky planets (R < 1.8 R⊕): {HZ['conservative_HZ_R_lt_1.8']} conservative and {HZ['optimistic_HZ_R_lt_1.8']} optimistic, or {HZ['conservative_rocky_incl_cool_hosts_clamped']} and {HZ['optimistic_rocky_incl_cool_hosts_clamped']} including TRAPPIST-1 with Teff clamped to 2600 K.
* Mean ESI: {c['mean']:.3f} (conservative) and {o['mean']:.3f} (optimistic).
* Top ESI: {', '.join(f"{n} {e:.3f}" for n, e in list(zip(o['names'], o['esi4']))[:6])}.
* No confirmed Archive planet meets the superhabitable criteria (K host, 1.0–1.5 R⊕, 282–302 K assumed surface temperature). The closest is Kepler-62 f (K host, 1.41 R⊕, 7 Gyr; too cold under the assumed temperature).
""")
L.append("## Variables and sources\n")
L.append("Every variable lives in [`params.yaml`](params.yaml). `best` is the value used in the deterministic point estimate; the default is the geometric mean for log-uniform and the midpoint for uniform.\n")
L.append("| variable | distribution / range | best | meaning | source |")
L.append("|---|---|---|---|---|")
for sec in ("params", "multipliers"):
    for k, s in cfg[sec].items():
        scope = " (user scenarios only)" if "scenarios" in s else ""
        L.append(f"| `{k}` | {rng_(s)} | {s.get('best', 'default')} | {cell(s.get('unit', ''))}{scope} | {cell(s.get('source', ''))} — {cell(s.get('url', ''))} |")
for st in cfg["hard_steps"]:
    L.append(f"| `tau_{st['name']}` | per scenario (baseline log-uniform 1e-3–1e3 Gyr; headline = Earth's interval) | Earth interval | expected waiting time; completed on Earth {st['earth_gya']} Ga | {cell(st['source'])} — {st['url']} |")
for k, s in cfg["scenarios"]["nathan_headline"]["extra_params"].items():
    L.append(f"| `{k}` | {rng_(s)} | {s.get('best')} | {cell(s['unit'])} (headline only) | {cell(s['source'])} — {cell(s['url'])} |")
L.append(f"| `w_similarity` | bootstrap mean of ESI^k over Archive HZ rocky planets | {c['mean_pow']['1']:.3f} | similarity weight (similarity/headline scenarios) | Schulze-Makuch+2011 Astrobiology 11, 1041 — https://phl.upr.edu/projects/earth-similarity-index-esi |")
for k in ("species_concurrent_per_tool_world", "species_cumulative_per_tool_world"):
    s = cfg["species"][k]
    L.append(f"| `{k}` | {rng_(s)} | {s['best']} | {cell(s['unit'])} | {cell(s['source'])} — {cell(s['url'])} |")
L.append("\nRanges marked **ASSUMED** have no quantitative literature value. **USER** marks Nathan's own inputs, which are kept separate from literature values.\n")
L.append("## Results: all scenarios\n")
L.append("| scenario | samples | median worlds now | 10th–90th pct | mean | P(N<1) | median species now | median worlds ever | median NN distance (ly) |")
L.append("|---|---|---|---|---|---|---|---|---|")
for k, s in S.items():
    if "N_now" not in s: continue
    a = s["N_now"]; sp = s.get("species_now"); ev = s.get("N_ever"); d = s.get("spacing", {}).get("median", {})
    nn = (fmt(d.get("nn_median_ly")) + (" (N<1)" if d.get("N", 1) < 1 else "")) if d.get("nn_median_ly") else "–"
    lab = f"**{k}** (headline)" if k == head else (f"{k} (literature)" if k == lit else k)
    L.append(f"| {lab} | {s.get('n', 1000000)} | {fmt(a['median'])} | {fmt(a['p10'])} – {fmt(a['p90'])} | {fmt(a['mean'])} | {a['P_lambda_lt1']:.3f} | {fmt(sp['median']) if sp else '–'} | {fmt(ev['median']) if ev else '–'} | {nn} |")
pf = S.get("nathan_factor_effects", {})
if pf:
    L.append(f"\nEffect of the headline's new factors (paired draws): without superhabitability the median is {fmt(pf['nathan_headline_no_superhab']['median_N'])} (headline ×{pf['nathan_headline_no_superhab']['ratio_of_medians']:.2f}); "
             f"without cross-lineage tool use it is {fmt(pf['nathan_headline_no_tooluse']['median_N'])} (×{pf['nathan_headline_no_tooluse']['ratio_of_medians']:.2f}).")
L.append("\nScenario definitions are in `params.yaml` under `scenarios:`. Full statistics, sensitivity tables and ESI-exponent variants are in [`results/results_summary.md`](results/results_summary.md).\n")
L.append("## What it means (plain language)\n")
L.append(f"""* **If Earth's history is typical** (Nathan's headline), the Milky Way has about **{fmt(h['median'])}** worlds with stone-age-or-better tool users right now, and the typical distance to the nearest one is about **{fmt(hs['nn_median_ly'])} light-years**. The range is very wide ({fmt(h['p10'])} to {fmt(h['p90'])}), but under these assumptions it is unlikely we are alone (P(N<1) ≈ {h['P_lambda_lt1']:.0%}).
* **If Earth's history is treated as a lucky draw** that we see only because we exist (the literature baseline), the median falls to **{fmt(b['median'])}**, and we are probably the only such world right now (P(N<1) ≈ {b['P_lambda_lt1']:.0%}).
* **The data cannot yet decide between those two views.** The biggest swings come from how often planets have both land and ocean, how long a stone-age-or-later phase lasts, plate tectonics, and the hard-step timescales. Star counts and η⊕ matter much less (η⊕ for G/K stars swings the headline by only ~0.6 orders of magnitude).
* **What Nathan's two new factors do.** Superhabitable worlds change the answer only slightly (×{pf.get('nathan_headline_no_superhab', {}).get('ratio_of_medians', float('nan')):.2f}). Treating tool use as fast and repeatable matters more (×{pf.get('nathan_headline_no_tooluse', {}).get('ratio_of_medians', float('nan')):.1f}). This is probably mostly through faster re-emergence after a collapse, because the first arrival moves by only ~0.5 of ~4.4 Gyr.
* **Stone-age worlds are effectively invisible** at interstellar distances, so a large N is consistent with the silence we observe.
""")
L.append("## Caveats\n")
L.append("""* **Prior-dominated.** Defensible priors move the median by more than 20 orders of magnitude (`snyder_beattie_priors` 5.5e-21 vs the headline). Read medians as summaries of the stated uncertainty, not measurements.
* **The headline assumes Earth's timeline is typical** and skips the observer-selection correction. ESI measures only bulk size, density, escape velocity and temperature; the temperature is assumed from insolation (Earth-like albedo and greenhouse). It says nothing about biology.
* **Superhabitability inputs.**
  * The 1–3× boost and the qualifying fraction are ASSUMED; neither source paper gives a number.
  * Schulze-Makuch et al. 2020 list 24 candidates, of which only 23 names were legible in the available figure. Most are unconfirmed KOIs.
* **Tool-use inputs.** Mapping "number of independent tool-use origins" onto a rate is ASSUMED. Non-hominin origins cannot be dated (behaviour rarely fossilises), and only hominins reached intentional stone flaking (capuchin and macaque flakes are unintentional by-products).
* **Several brackets are ASSUMED:** M-dwarf penalties, sterilisation rate, recurrence, self-inflicted risk, metallicity ramp, moon-host fraction. The Rare-Earth multipliers are treated as independent.
* **Species counts** assume Earth's hominin radiation is typical: on average 2.38 coexisting species, 15 over ~3.3 Myr (Smithsonian Human Origins). They depend on how finely taxonomists split species.
* **Spacing assumptions.** Nearest-neighbour distances assume random placement in a 50,000-ly-radius, 1,000-ly-thick disk (≈7.9e12 ly³, a user-supplied figure). Below 1 expected world they are formal only.
* **Sample sizes.** 2e5–1e6 per scenario. Importance-weighted scenarios have smaller effective sample sizes (see `results_summary.md`).
""")
L.append("## Reproduce\n")
L.append("""```bash
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
python tools/fetch_data.py          # NASA Exoplanet Archive pscomppars (~80 MB) + KOI rows
python hz_archive.py && python esi.py && python superhab.py      # derived data in data/
python drake_model.py               # all scenarios in params.yaml (n_samples each; slow at 1e6)
python drake_model.py --scenario nathan_headline --n 200000      # one scenario (run several in parallel)
python drake_model.py --analyze-only                              # stats, charts, results_summary.md
python tools/build_readme.py        # refresh this README from results
```
Raw samples (`results/*.npz`, several hundred MB) and `data/pscomppars.csv` are not committed. They regenerate from the commands above, and the random seed is fixed in `params.yaml`.

## Add or change a variable
* **New habitability factor:** add an entry under `multipliers:` in `params.yaml` with `dist`, `low`/`high` (or `value`), `applies_to: [gk, m]`, `source` and `url`. It is sampled automatically, applied, and included in the sensitivity tornado.
* **New evolutionary step:** add an entry under `hard_steps:` with `earth_gya` (when it happened on Earth).
* **Scenario-specific change:** add `overrides:` (replace an existing variable) or `extra_params:` (new scenario-only variable) under the scenario. Then list the scenario in `run.scenarios_to_run`.
* **Headline:** set `run.headline_scenario`. `run.literature_baseline` is always reported alongside it.
* Supported distributions: `fixed`, `uniform`, `loguniform`, `normal` (with optional min/max), `lognormal10`, `one_plus_loguniform`.

## License and credit
Model by Nathan A. Meeks. MIT License (see `LICENSE`). Literature values belong to their cited authors. Exoplanet data: NASA Exoplanet Archive (https://exoplanetarchive.ipac.caltech.edu), operated by Caltech/IPAC under contract with NASA.
""")
open("README.md", "w").write("\n".join(L))
print("README.md written", len(L))
