# Extended, time-aware Drake model: how many "stone-age-or-greater" worlds exist at once in the Milky Way?

Built for Nathan Meeks (Oct 2026). **Headline scenario: `nathan_headline`** (user-approved; `run.headline_scenario` in params.yaml). Literature `baseline` kept for comparison. Everything is driven by **`params.yaml`**. Add or change a variable there and rerun. No code edits are needed.

```
cd /workspace/drake
.venv/bin/python drake_model.py                      # all scenarios, n from params.yaml (1e6)
.venv/bin/python drake_model.py --n 20000            # quick run
.venv/bin/python drake_model.py --scenario baseline  # one scenario (for parallel runs)
.venv/bin/python drake_model.py --analyze-only       # rebuild report/plots from saved samples
.venv/bin/python hz_archive.py                       # NASA Exoplanet Archive HZ counts -> data/hz_counts.json
.venv/bin/python esi.py                              # Earth Similarity Index of HZ rocky planets -> data/esi_hz.json (+ CSVs)
.venv/bin/python tools/update_readme.py              # refresh README numbers from results/results.json
```

## Files
| path | what |
|---|---|
| `params.yaml` | the single config file: every variable, its distribution, best value, source, and the scenarios |
| `drake_model.py` | Monte Carlo model (vectorised, analytic-DFT convolutions) |
| `analyze.py` | statistics, sensitivity, plots, `results/results_summary.md` |
| `hz_archive.py` | counts rocky/giant HZ planets in the NASA Exoplanet Archive (Kopparapu+2014 HZ) |
| `esi.py` | Schulze-Makuch+2011 Earth Similarity Index for Archive HZ rocky planets (feeds `similarity_weighted`) |
| `data/esi_hz.json`, `data/esi_hz_rocky_{conservative,optimistic}.csv` | ESI values, population means of ESI^k, per-planet table |
| `data/si_species.html`, `data/si/*.html`, `data/si_when_lived.json` | Smithsonian Human Origins species list and 'When Lived' spans (species factor) |
| `superhab.py` | superhabitability screen (Schulze-Makuch+2020 criteria) of Archive planets and of the paper's KOIs → `data/superhab.json`, `data/superhab_K_hz_planets.csv`, `data/smh2020_kois_screened.csv` |
| `data/pscomppars.csv` | NASA Exoplanet Archive composite table (TAP pull, 1 Oct 2026) |
| `data/hz_counts.json` | archive-derived HZ counts |
| `results/results_summary.md`, `results/results.json` | numbers |
| `results/hist_log10N.png`, `results/tornado.png` | headline (baseline) histogram and tornado; `*_<scenario>.png` for each scenario |
| `results/spectral_breakdown.png` | v2: N by host type M/K/G/F (median, 10–90%) and share of N, headline vs literature baseline |
| `results/stage_breakdown.png` | v2: N by civilisation stage (lithic … spacefaring) and radio-capable N, headline vs literature baseline |
| `tools/v2_sections.py` | builds the v2 breakdown sections of the READMEs |
| `results/v1/` | v1 samples/results of the five re-run scenarios (before multi-spectral/multiphase) |
| `results/comparison_scenarios.png` | all scenarios on one axis (median, 10–90%, 5–95%, species median) |
| `results/esi_distribution.png` | ESI histogram of HZ rocky planets + population weight vs exponent |
| `results/samples_<scenario>.npz` | all samples, weights and outputs |
| `xpost/` | the image from the X post |

## What the target is
The usual Drake equation counts *radio-communicating* civilizations. This model counts **worlds that have a lineage of habitually stone-tool-making intelligence (Lomekwi/Oldowan level) or anything more advanced**, alive at the same time. On this definition `fc` and `L` become **"reaching stone-tool use"** and **`L_stone`, the length of the stone-age-or-later phase**. Radio detectability (the user's ~100-yr radio bubble, probes pinging habitable zones) changes what we can *detect*. It does not change N, so it is not a factor here.

## Model structure (time-aware)
1. **Star formation history of the disk.** Thick-disk phase 13.0 to 8.5 Gyr ago with ~half of the disk mass (Snaith+2015), then an exponential thin-disk phase normalised to today's SFR (1.65 Msun/yr) and disk mass (Licquia & Newman 2015). This replaces a constant R*. The bulge and halo are excluded, the bulge as hostile and the halo as metal-poor.
2. **Habitable bodies per star**, split into G/K and M hosts: `ne` (Kepler/Archive η⊕, with fp folded in) × Rare-Earth multipliers (plate tectonics, land and ocean, large moon, Jupiter shield, binary-star stability, M-dwarf flares, tidal locking and water loss) × galactic habitable zone × a metallicity ramp in time. **Plus habitable exomoons**: HZ giants × fraction hosting a ≥0.1–0.3 M⊕ moon × moon habitability.
3. **Biology as hard steps** (Carter 1983; Hanson 1998; Watson 2008; Snyder-Beattie+2021): abiogenesis → oxygenic photosynthesis/GOE → eukaryogenesis → complex multicellularity → stone-tool intelligence. Each step is a Poisson waiting time with expected time τ_k, and the convolution gives the time-to-tool-users distribution, which competes with each host's habitable window. With `bayes_update_on_earth_timing`, every sample is **weighted by the likelihood of Earth's dated transitions, conditioned on Earth having finished them all by now**. This is the Snyder-Beattie+2021 observer-selection update, and it removes rates that are too fast for Earth's record.
4. **Duration and recurrence.** A tool-using phase lasts Exp(L_eff) with 1/L_eff = 1/L_stone + r_BigFive·p_kill + p_lethal·(r_GRB + r_SN) + r_self. After it ends, the planet can re-evolve tool users at rate 1/(m_rec·τ_intelligence), modelled as an alternating renewal process. This is the "recurrence on the same planet" term.
5. **Hazards in time.** A whole-biosphere sterilisation hazard scales with SFR(t), so it is higher in the early, GRB-rich galaxy (Piran & Jimenez 2014). Planets older than their host's habitable window drop out.
6. **Outputs.** N(t) on a 20-Myr grid over 13.8 Gyr. The headline is **N_now** (simultaneous now). Also reported: the time-average of N(t) (expected overlap at a random moment of galactic history), N_ever (worlds that ever produced tool users by now, the Frank & Sullivan 2016 "archaeological" form), and P(no other world, Poisson).

Note on resets: with memoryless hard steps, a mass extinction that only resets the *current* step costs nothing extra. Resets therefore act here by **ending existing tool-using lineages** (L_eff) and through **whole-biosphere sterilisation**. Recovery and re-evolution happen through the recurrence term.

## Scenarios
* **v2 model** (`multispectral: true`, `multiphase: true` in params.yaml): nathan_headline, its two sensitivity variants, baseline and baseline_no_exomoons were re-run with M/K/G/F host classes and civilisation stages; see the v2 breakdown section. All other scenarios are v1.
* **nathan_headline** (HEADLINE, user-approved): similarity_weighted + superhabitability boost + cross-lineage (fast, repeatable) tool use. Sensitivity runs: **nathan_headline_no_superhab**, **nathan_headline_no_tooluse** (same random draws).
* **baseline** (literature baseline, kept for comparison): literature values. Hard-step τ is log-uniform from 1e-3 to 1e3 Gyr (6 decades centred on Earth's ~Gyr transition timescales), then updated on Earth's timing.
* **baseline_no_exomoons**: identical random draws with the exomoon term off. It isolates the exomoon effect.
* **snyder_beattie_priors**: SB2021's own prior bounds (1e-14 to 1e10 Gyr). This is the "intelligence is very rare" literature view.
* **user_inputs**: Nathan's assumptions: a 50–200 kyr stone-age-or-better lifetime/extinction window, the Sun with ~4 Gyr remaining, and a low-weight Venus/Mars-style extra-world bonus. Literature values fill every factor the user did not give.
* **user_fast_intelligence**: the same, plus the user's "tens of thousands of years" time-to-intelligence for the last step. Earth's ~0.6 Gyr gap from animals to tools rules this out, so the Earth-timing update is off for this one only.
* **similarity_weighted** (USER-PROPOSED argument): every habitable body gets Earth's observed step timeline as its *typical* case (each hard step's expected time = Earth's interval; no observer-selection reweighting), and its probability is scaled by w = ESI^k averaged over the Archive HZ-rocky ESI population. Rare-Earth multipliers kept. Exponent k = 1 (linear) headline; k = 2, 3, 5, 10 and the optimistic-HZ population reported as exact rescalings.
* **similarity_weighted_no_rare_earth**: the same, but similar planets are also assumed to share Earth's plate tectonics, land/ocean balance, large moon, Jupiter and binary outcome (those multipliers = 1). Upper-end reading.
* **earth_random_draw**: Earth's step timings are one random draw from each step's waiting-time distribution, with an uninformative prior on whether Earth was fast or slow (Earth's interval at a uniform-random quantile ⇒ τ_k = x_k/E_k, E_k ~ Exp(1)). No observer-selection correction.
* **classic_static_SDO_style**: the static Sandberg-Drexler-Ord 2018 Monte Carlo with fc→f_stone and L→L_stone, for comparison.

## The X post (Step 1)
https://x.com/NathanAMeeks/status/2105869738303963480 (posted 1 Oct 2026, 8:57 PM Arizona time). The text is only **"Well... 💩..."**. It quote-posts @ArcyloOfficial (2105628796489732396): *"Good morning, humans. 👽 I'm reading your finest journalism while handling intergalactic business..."*. That post's image (saved to `xpost/arcylo_photo1.jpg`) is an AI-generated picture of a green alien on a toilet in a grimy bathroom, reading a newspaper headlined "ELON BUYS MARS TOILET PAPER" / "TWITTER REBRANDED TO TOILET", with an Elon-in-a-spacesuit-on-a-toilet-roll-horse cartoon. **The post contains no Drake variables or values.** The user's Drake variables came from the research export summarised below.

## Headline results (from results/results_summary.md)

N = expected number of Milky Way worlds with stone-age-or-greater tool users alive **now**, other than Earth. Species = tool-using species (worlds × species_per_tool_world).

| scenario | n (ESS) | median worlds (50/50) | mean | 10th–90th pct | P(N<1) | P(no other world, Poisson) | median species now | median worlds ever | median species ever | P(50≤N_ever≤100) |
|---|---|---|---|---|---|---|---|---|---|---|
| **nathan_headline** (HEADLINE) | 200000 (200000) | **2.63e+03** | 6.92e+05 | 13.2 – 4.12e+05 | 0.027 | 0.024 | 5.85e+03 | 5.58e+04 | 6.56e+05 | 0.012 |
| baseline (literature baseline) | 200000 (13586) | **0.00179** | 1.61e+03 | 3.72e-07 – 7.04 | 0.837 | 0.809 | 0.00392 | 1.13 | 13.2 | 0.038 |
| nathan_headline_no_superhab | 200000 (200000) | **2.46e+03** | 6.48e+05 | 12.3 – 3.87e+05 | 0.028 | 0.025 | 5.48e+03 | 5.28e+04 | 6.20e+05 | 0.012 |
| nathan_headline_no_tooluse | 200000 (200000) | **678** | 3.06e+05 | 2.86 – 1.32e+05 | 0.062 | 0.054 | 1.52e+03 | 5.21e+04 | 6.12e+05 | 0.012 |
| similarity_weighted | 200000 (200000) | **895** | 4.69e+05 | 2.68 – 2.08e+05 | 0.067 | 0.058 | 1.99e+03 | 4.39e+04 | 5.19e+05 | 0.014 |
| similarity_weighted_no_rare_earth | 200000 (200000) | **1.90e+07** | 2.12e+08 | 1.75e+05 – 5.41e+08 | 0.000 | 0.000 | 4.20e+07 | 7.87e+08 | 9.26e+09 | 0.000 |
| earth_random_draw | 200000 (200000) | **157** | 2.32e+05 | 0.225 – 5.9e+04 | 0.159 | 0.141 | 352 | 1.2e+04 | 1.42e+05 | 0.030 |
| baseline_no_exomoons | 200000 (13586) | **0.00143** | 1.36e+03 | 2.98e-07 – 5.88 | 0.844 | 0.817 | 0.00308 | 0.874 | 10.4 | 0.036 |
| snyder_beattie_priors | 200000 (3151) | **5.51e-21** | 0.643 | 3.60e-30 – 1.04e-11 | 0.999 | 0.999 | 1.29e-20 | 4.70e-18 | 5.56e-17 | 0.000 |
| user_inputs | 500000 (34101) | **9.93e-05** | 34.4 | 3.94e-08 – 0.251 | 0.934 | 0.916 | 2.20e-04 | 0.875 | 10.2 | 0.039 |
| user_fast_intelligence | 200000 (200000) | **571** | 6.01e+05 | 0.736 – 2.06e+05 | 0.110 | 0.097 | 1.28e+03 | 967 | 1.14e+04 | 0.047 |
| classic_static_SDO_style | 1000000 | **28.8** | 8.05e+06 | 3.14e-60 – 1.49e+06 | 0.465 | 0.463 | 61.8 | – | – | – |

Exomoons (paired draws): median 0.00143 without → 0.00179 with (×1.25); per-sample effect median 0.008 dex, 90th pct 0.32 dex, 99th pct 1.07 dex.

Deterministic best estimates (all `best` values; hard-step τ = Earth's own intervals): nathan_headline N_now ≈ 1.56e+04 (species ≈ 3.72e+04); baseline N_now ≈ 3.48e+03 (species ≈ 8.28e+03); user_inputs N_now ≈ 86.5 (species ≈ 206); similarity_weighted N_now ≈ 2.81e+03 (species ≈ 6.68e+03); similarity_weighted_no_rare_earth N_now ≈ 5.63e+06 (species ≈ 1.34e+07).

Charts: `results/comparison_scenarios.png` (all scenarios), `results/hist_log10N.png` and `results/tornado.png` (headline = nathan_headline; literature baseline: `results/hist_log10N_baseline.png`, `results/tornado_baseline.png`), `results/hist_log10N_<scenario>.png`, `results/tornado_<scenario>.png`, `results/esi_distribution.png`.


## Multi-spectral and multiphase breakdowns (v2 model)

Suggested by a friend of Nathan's (Oct 2026). Re-run with the v2 model (2e5 samples each): `baseline`, `baseline_no_exomoons`, `nathan_headline`, `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`. Every other scenario is still the v1 model (two host classes, G/K and M, and one stone-age-or-greater phase).

Change in the median N_now from v1 to v2: `nathan_headline` 3.18e+03 (v1) → 2.63e+03 (v2); `baseline` 0.00238 (v1) → 0.00179 (v2). The v2 total adds F stars, splits G from K (K now has its own, higher η⊕ and longer habitable window), adds K-activity and F-UV penalties and per-type ESI weights, and adds stage-specific collapse hazards after the lithic stage.

![Multi-spectral breakdown](results/spectral_breakdown.png)

### By host star type

Each type has its own star fraction (RECONS 10-pc census vs Kroupa IMF), η⊕, habitable window, HZ giants for exomoons, activity/UV/tidal penalties, and similarity weight (its own Archive ESI list if it has ≥ 3 HZ rocky planets, otherwise the pooled list). The superhabitability boost applies only to K hosts. *Share* = that type's fraction of the posterior-mean N; *median share* = per-sample median of the type's fraction.

| scenario | host type | median N now | 10th–90th pct | P(N<1) | share of mean N | median share [10th, 90th] | median N ever |
|---|---|---|---|---|---|---|---|
| nathan_headline | M | **280** | 1.06 – 6e+04 | 0.098 | 27.4% | 12.4% [1.8, 51.7] | 5.12e+03 |
| nathan_headline | K | **1.69e+03** | 8.36 – 2.66e+05 | 0.035 | 63.5% | 71.8% [38.8, 89.7] | 3.22e+04 |
| nathan_headline | G | **228** | 1.15 – 3.55e+04 | 0.094 | 9.0% | 9.3% [2.7, 25.6] | 9.56e+03 |
| nathan_headline | F | **1.67** | 0.00681 – 324 | 0.453 | 0.1% | 0.1% [0.0, 0.6] | 458 |
| nathan_headline | **all** | **2.63e+03** | 13.2 – 4.12e+05 | 0.027 | 100% | – | 5.58e+04 |
| baseline | M | **2.34e-04** | 4.16e-08 – 1.12 | 0.898 | 38.6% | 15.2% [2.2, 58.1] | 0.123 |
| baseline | K | **0.00116** | 2.47e-07 – 4.48 | 0.854 | 55.5% | 74.9% [36.2, 93.8] | 0.705 |
| baseline | G | **5.92e-05** | 1.16e-08 – 0.264 | 0.933 | 5.9% | 3.9% [0.5, 18.7] | 0.0958 |
| baseline | F | **6.28e-08** | 8.57e-12 – 4.11e-04 | 0.994 | 0.1% | 0.0% [0.0, 0.1] | 3.69e-04 |
| baseline | **all** | **0.00179** | 3.72e-07 – 7.04 | 0.837 | 100% | – | 1.13 |

**Top Archive planets by ESI, per host type** (Kopparapu+2014 HZ, R < 1.8 R⊕; Schulze-Makuch+2011 4-property ESI):

| type | HZ rocky planets (conservative / optimistic) | top planets, optimistic HZ (ESI) | best R < 1.8 planets outside the HZ cut (ESI, insolation S⊕) |
|---|---|---|---|
| M | 22 / 35 | Teegarden's Star b (0.979), TOI-700 d (0.942), Kepler-1649 c (0.940), GJ 3378 b (0.938), TOI-700 e (0.932) | – |
| K | 3 / 5 | Kepler-442 b (0.882), Kepler-1410 b (0.860), Kepler-1544 b (0.841), Kepler-62 e (0.824), Kepler-62 f (0.799) | Kepler-1512 b (0.883, S=1.60), Kepler-395 c (0.832, S=2.11) |
| G | 1 / 1 | Kepler-452 b (0.879) | Kepler-1126 c (0.813, S=2.06), Kepler-69 c (0.733, S=2.69), Kepler-409 b (0.669, S=6.15) |
| F | 0 / 0 | none | Kepler-132 e (0.677, S=6.10), Kepler-1620 b (0.598, S=7.92), Kepler-1633 b (0.456, S=26.26) |

![Multiphase breakdown](results/stage_breakdown.png)

### By civilisation stage

Inside each tool-using episode a world moves through **lithic → agricultural → industrial → radio-capable → spacefaring** (orbital spaceflight). Each advance is an exponential waiting time. From stage 2 on, a stage-specific collapse hazard applies: a fraction q regresses one stage (and can recur later), and the rest ends the lineage. The baseline end-of-lineage hazards (intrinsic lifetime, Big-Five extinctions, GRB/SN, self-inflicted) apply in every stage. N in a stage = N_now × the long-run share of tool-using time spent in that stage.

| stage parameter | prior | Earth anchor / best | source |
|---|---|---|---|
| `stage_tau_agri_yr` | loguniform [3.3e5, 3.3e7] | 3.29e6 | Earth anchor 3.3 Ma (Harmand+2015 Lomekwi 3) -> ~11.5 ka (Zeder 2011 Curr.Anthropol. 52, S221) = 3.29 Myr; range = Earth/10 .. Earth x10 ASSUMED |
| `stage_tau_ind_yr` | loguniform [1.1e3, 1.1e5] | 1.1e4 | Earth anchor ~11.5 ka -> ~1760 CE (~11.2 kyr); range Earth/10 .. x10 ASSUMED |
| `stage_tau_radio_yr` | loguniform [14.0, 1400.0] | 135.0 | Earth anchor ~1760 -> 1895 (Marconi's first radio transmissions) = ~135 yr (user: ~150 yr); range Earth/10 .. x10 ASSUMED |
| `stage_tau_space_yr` | loguniform [6.2, 620.0] | 62.0 | Earth anchor 1895 -> 1957 (Sputnik 1) = 62 yr; range Earth/10 .. x10 ASSUMED |
| `stage_h_agri_per_yr` | loguniform [1e-07, 0.001] | geometric mean | ASSUMED. Earth: farming has persisted ~11.5 kyr world-wide despite many regional collapses (Tainter 1988, The Collapse of Complex Societies); one world gives no galactic rate |
| `stage_h_ind_per_yr` | loguniform [1e-06, 0.01] | geometric mean | ASSUMED (Earth: ~265 yr industrial so far). Natural extinction alone is < 6.9e-5/yr (Snyder-Beattie, Ord & Bonsall 2019 Sci.Rep. 9, 11054), so most of this range is anthropogenic risk, which that bound does not cover |
| `stage_h_radio_per_yr` | loguniform [1e-10, 0.01] | geometric mean | 1/L with L log-uniform 1e2 .. 1e10 yr = Sandberg, Drexler & Ord 2018 Table 1 (lifetime of a detectable civilisation) |
| `stage_h_space_per_yr` | loguniform [1e-10, 0.01] | geometric mean | Same as radio stage (SDO 2018 L 1e2 .. 1e10 yr); ASSUMED that orbital capability does not by itself lower the hazard |
| `stage_q_regress` | uniform [0.0, 1.0] | midpoint | ASSUMED (no quantitative literature). Earth's regional collapses mostly regressed rather than ended lineages (Tainter 1988) |

| scenario | stage | median N now | 10th–90th pct | mean | P(N<1) | median share of tool-using time [10th, 90th] |
|---|---|---|---|---|---|---|
| nathan_headline | lithic | **1.64e+03** | 9.94 – 2.31e+05 | 4.17e+05 | 0.030 | 0.969 [0.199, 0.999] |
| nathan_headline | agricultural | **3.13** | 0.0129 – 590 | 1.77e+03 | 0.395 | 0.00115 [1.13e-04, 0.0128] |
| nathan_headline | industrial | **0.0355** | 1.26e-04 – 7.27 | 23.8 | 0.785 | 1.33e-05 [9.59e-07, 1.84e-04] |
| nathan_headline | radio | **0.0232** | 6.78e-05 – 5.79 | 47.5 | 0.805 | 8.51e-06 [4.97e-07, 1.55e-04] |
| nathan_headline | spacefaring | **41.3** | 0.0191 – 5.5e+04 | 2.74e+05 | 0.274 | 0.0206 [1.47e-04, 0.797] |
| nathan_headline | **radio-capable (radio + spacefaring)** | **42.9** | 0.0216 – 5.51e+04 | 2.74e+05 | 0.270 | – |
| baseline | lithic | **0.00115** | 3.00e-07 – 3.58 | 1.03e+03 | 0.859 | 0.969 [0.202, 0.999] |
| baseline | agricultural | **2.05e-06** | 4.33e-10 – 0.0083 | 4.83 | 0.982 | 0.00115 [1.15e-04, 0.0127] |
| baseline | industrial | **2.54e-08** | 3.79e-12 – 1.15e-04 | 0.0676 | 0.998 | 1.33e-05 [9.80e-07, 1.89e-04] |
| baseline | radio | **1.61e-08** | 2.41e-12 – 8.13e-05 | 0.0626 | 0.998 | 8.72e-06 [5.05e-07, 1.57e-04] |
| baseline | spacefaring | **2.52e-05** | 1.28e-09 – 0.505 | 574 | 0.914 | 0.0208 [1.51e-04, 0.796] |
| baseline | **radio-capable (radio + spacefaring)** | **2.65e-05** | 1.35e-09 – 0.512 | 574 | 0.914 | – |

**Radio-capable N vs classic SETI-style Drake estimates.** 
* `nathan_headline`: median **42.9** radio-capable worlds now (10th–90th 0.0216 – 5.51e+04, P(N<1) = 0.27; median nearest-neighbour distance at the median ≈ 6.35e+03 ly); top drivers: l_stone_yr (4.2 dex), stage_h_space_per_yr (3.4 dex), f_land_and_ocean (3.4 dex), f_plate_tectonics (1.8 dex)
* `baseline`: median **2.65e-05** radio-capable worlds now (10th–90th 1.35e-09 – 0.512, P(N<1) = 0.91; below 1, so no radio neighbour is expected at the median); top drivers: l_stone_yr (4.4 dex), tau_stone_tool_intelligence (4.3 dex), f_land_and_ocean (3.7 dex), stage_h_space_per_yr (3.1 dex)
* Sandberg, Drexler & Ord 2018 (arXiv:1806.02404), 'current knowledge' sketch for communicating civilisations: median N = 0.32, mean 27 million, P(N<1) = 52%. This repo's static SDO-style stone-age variant: median 28.8.
* Radio-only (radio but not yet spacefaring) is a very short stage here, because Earth went from radio to orbital spaceflight in 62 years. Almost all radio-capable worlds are therefore in the spacefaring stage.


**Spacing at the median N** (disk ~7.9e12 ly³, user-supplied; nearest-neighbour distance assumes random placement):

| scenario | median N | equal-cube side (ly) | median nearest-neighbour distance (ly) | regime |
|---|---|---|---|---|
| nathan_headline | 2.63e+03 | 1.44e+03 | 792 | 3D |
| baseline | 0.00179 | 1.64e+05 | 9.83e+05 (N<1: none expected) | 2D thin disk |
| nathan_headline_no_superhab | 2.46e+03 | 1.48e+03 | 810 | 3D |
| nathan_headline_no_tooluse | 678 | 2.27e+03 | 1.6e+03 | 2D thin disk |
| similarity_weighted | 895 | 2.07e+03 | 1.39e+03 | 2D thin disk |
| similarity_weighted_no_rare_earth | 1.90e+07 | 74.6 | 41 | 3D |
| earth_random_draw | 157 | 3.69e+03 | 3.32e+03 | 2D thin disk |
| baseline_no_exomoons | 0.00143 | 1.77e+05 | 1.10e+06 (N<1: none expected) | 2D thin disk |
| snyder_beattie_priors | 5.51e-21 | 1.13e+11 | 5.61e+14 (N<1: none expected) | 2D thin disk |
| user_inputs | 9.93e-05 | 4.30e+05 | 4.18e+06 (N<1: none expected) | 2D thin disk |
| user_fast_intelligence | 571 | 2.4e+03 | 1.74e+03 | 2D thin disk |
| classic_static_SDO_style | 28.8 | 6.49e+03 | 7.75e+03 | 2D thin disk |

## Nathan's headline (`nathan_headline`)
**Approved by Nathan as the headline (Oct 2026).** The literature `baseline` is kept for comparison. Definition:
* Start from `similarity_weighted`: ESI¹ with the conservative HZ, each hard step's expected time equal to Earth's interval, and no observer-selection reweighting. Abiogenesis through multicellularity are unchanged.
* Add **(a) a superhabitability boost** for the qualifying fraction of K-dwarf planets (v2; G/K in v1).
* Add **(b) cross-lineage tool use**: the complex-animals → stone-tools step becomes fast and repeatable.

**Result.**
* Median (50/50) **2.63e+03** worlds now; mean 6.92e+05; 10th–90th percentile 13.2 – 4.12e+05.
* P(N<1) = 0.027; P(no other world, Poisson) = 0.024.
* Species now: median 5.85e+03 (10th–90th 28.6 – 9.45e+05).
* Worlds ever: median 5.58e+04; species ever: median 6.56e+05.
* Deterministic best estimate: 1.56e+04 worlds now.
* At the median N, the equal-cube side is **1.44e+03 ly** for a ~7.9e12 ly³ disk (user-supplied volume; equal to a 50,000-ly-radius, 1,000-ly-thick cylinder). The **median nearest-neighbour distance is 792 ly** (3D; random placement).
* Range of the nearest-neighbour distance: 147 ly at the 90th-percentile N to 1.15e+04 ly at the 10th.
* For comparison, the literature baseline median is 0.00179 (P(N<1) = 0.84).

**Effect of each new factor** (the two nathan_headline variants reuse the headline's random draws; similarity_weighted is an earlier, independently drawn run):

| comparison | its median N_now | headline median ÷ its median | per-sample log10 ratio: median [10th, 90th] |
|---|---|---|---|
| without superhabitability (tool-use change only) | 2.46e+03 | ×1.07 | 0.015 [0.002, 0.073] |
| without cross-lineage tool use (superhab only) | 678 | ×3.88 | 0.598 [0.328, 0.789] |
| without both (= similarity_weighted, v1 model: not directly comparable) | 895 | ×2.94 | n/a (independent draws; similarity_weighted was a finished run, not re-run) |

### (a) Superhabitability: Schulze-Makuch, Heller & Guinan 2020 (Astrobiology 20, 1394, https://pmc.ncbi.nlm.nih.gov/articles/PMC7757576/) and Heller & Armstrong 2014 (Astrobiology 14, 50, https://doi.org/10.1089/ast.2013.1088)
* **Criteria (paper, Table 2).**
  * K-dwarf host; about 5–8 Gyr old.
  * "Up to 1.5 more massive than Earth and about 10% larger"; mean surface temperature about 5 °C higher than Earth's.
  * Moist atmosphere with 25–30% O₂; scattered land and water with many shallow seas and archipelagos.
  * A large moon (1–10% of the planet's mass); plate tectonics and a strong magnetic field.
  * Only host type, age, size and (roughly) temperature are testable with Archive data.
* **The paper's 24 candidates.** The text says 24 planets and planet candidates smaller than 2 R⊕ (Fig. 2). Of these, 9 orbit K stars, 16 are about 5–8 Gyr old, and 5 are within 10° of the 19 °C optimum. Only KOI 5715.01 meets all three of those broad criteria, and it may be colder than Earth unless its greenhouse effect is stronger than Earth's. None meets all the criteria.
  * Verified from the PMC full text. I could read **23 name tags** in the PMC copy of Fig. 2; Table 3 is an image and its table page is behind a captcha, so the 24th name was not confirmed.
  * Today in the Archive KOI table: 22 of the 23 are listed, 2 CONFIRMED (Kepler-69 c, Kepler-1126 b) and 20 still CANDIDATE. KOI-456.04 is not in the cumulative table.
  * With current Archive values, 3 have K hosts (Teff < 5200 K) and 6 have 1.0–1.5 R⊕, but none has both.
  * Kepler-1126 b's Archive insolation is now 4.64 S⊕, well outside the HZ.
* **Archive confirmed planets** (`superhab.py`, optimistic HZ, R < 2 R⊕, K host 3900–5200 K): 7 planets. **None meets K + 1.0–1.5 R⊕ + 282–302 K (assumed T_surf).**
  * The closest is **Kepler-62 f** (K host, 1.41 R⊕, 7 Gyr), which fails only temperature (242 K assumed; its real temperature depends on its greenhouse).
  * The paper's three broad criteria (K + temperature + age) are met by 0 confirmed planets.

| planet | host Teff (K) | age (Gyr) | dist (pc) | R (R⊕) | S (S⊕) | T_surf assumed (K) | ESI | criteria met (K host, 1.0–1.5 R⊕, 282–302 K, 5–8 Gyr) |
|---|---|---|---|---|---|---|---|---|
| Kepler-62 f | 4925 | 7.0 | 301 | 1.41 | 0.50 | 242 | 0.799 | 3/4 (K, size, age) |
| Kepler-442 b | 4402 | 2.9 | 366 | 1.34 | 0.66 | 260 | 0.882 | 2/4 (K, size) |
| Kepler-1410 b | 4092 | 4.07 | 367 | 1.78 | 1.06 | 292 | 0.860 | 2/4 (K, temp) |
| Kepler-283 c | 4351 | 3.09 | 468 | 1.82 | 0.95 | 284 | 0.855 | 2/4 (K, temp) |
| Kepler-440 b | 4134 | 1.3 | 301 | 1.86 | 1.20 | 301 | 0.829 | 2/4 (K, temp) |
| Kepler-62 e | 4925 | 7.0 | 301 | 1.61 | 1.35 | 311 | 0.824 | 2/4 (K, age) |
| Kepler-1544 b | 4886 | 2.34 | 335 | 1.78 | 0.83 | 275 | 0.841 | 1/4 (K) |

* **Model.** For a fraction f_superhab of K-dwarf planets (v2), the per-planet step-success probability is multiplied by `superhab_boost`, capped so it cannot exceed 1. The boost is not applied to moons or to M, G or F hosts.
  * f_superhab is log-uniform 0.03–0.43, ASSUMED. The best value, 0.104, is derived from the Archive: 25/49 of HZ R < 2 planets at 1.0–1.5 R⊕ × 10/49 in the temperature window, assuming independence. (v1 applied 0.073 = 0.104 × the 0.70 K share to all G/K planets.)
  * superhab_boost is log-uniform **1–3×, ASSUMED** (the user's suggestion). Neither paper gives a number.
  * The 5–8 Gyr age criterion is not boosted separately, because the time-aware model already counts older planets as having had more time.

### (b) Cross-lineage tool use: why the animals → tools step is treated as not-hard
Tool use evolved independently in distantly related lineages (all citations verified):

| lineage | behaviour | citation |
|---|---|---|
| primates: chimpanzees | termite fishing, aimed throwing; stone-hammer nut cracking ≥4.3 kyr old | Goodall 1964 Nature 201, 1264 (https://doi.org/10.1038/2011264a0); Mercader+2007 PNAS (https://www.pnas.org/doi/10.1073/pnas.0607909104) |
| primates: hominins | stone tools from 3.3 Ma (Lomekwi 3) | Harmand+2015 Nature 521, 310 (https://www.nature.com/articles/nature14464) |
| primates: bearded capuchins | stone-on-stone percussion **unintentionally makes sharp flakes and cores like hominin tools**; ≥3,000 yr archaeological record | Proffitt+2016 Nature 539, 85 (https://doi.org/10.1038/nature20112); Falótico+2019 Nat. Ecol. Evol. (https://www.nature.com/articles/s41559-019-0904-4) |
| primates: long-tailed macaques | nut cracking unintentionally makes flakes resembling Oldowan/Lomekwian ones | Proffitt+2023 Sci. Adv. 9, eade8159 (https://www.science.org/doi/10.1126/sciadv.ade8159) |
| corvids (New Caledonian crow) | manufactures hooked twig and stepped pandanus-leaf tools | Hunt 1996 Nature 379, 249 (https://www.nature.com/articles/379249a0) |
| cephalopods (veined octopus) | carries coconut-shell halves for later use as a shelter | Finn, Tregenza & Norman 2009 Curr. Biol. 19, R1069 (https://doi.org/10.1016/j.cub.2009.10.052) |
| sea otters | pound shellfish on stone anvils/hammers | Hall & Schaller 1964 J. Mammal. 45, 287 |
| bottlenose dolphins (Shark Bay) | sponging, culturally transmitted | Krützen+2005 PNAS 102, 8939 (https://www.pnas.org/doi/10.1073/pnas.0500232102) |
| Asian elephants | modify branches to switch flies | Hart+2001 Anim. Behav. 62, 839 |
| overall | tool use across **three phyla and seven classes**; ~85% of entries use tools in only one category | Bentley-Condit & Smith 2010 Behaviour 147, 185 (https://brill.com/view/journals/beh/147/2/article-p185_3.xml) |

* **Number of independent origins.**
  * At least 6 independent lineages from the user's list are verified: primates, corvids, octopus, sea otters, dolphins and elephants.
  * Tool use is documented in ≥7 animal classes (Bentley-Condit & Smith 2010).
  * Lithic flake production specifically is known in 3 primate lineages: hominins (intentional), and capuchins and macaques (unintentional by-products).
* **Timing.** Complex animals appeared ~0.6 Ga (Knoll 2011). Behaviour rarely fossilises, so every documented origin is in a living lineage, with archaeological records going back only to 3.3 Ma (hominins) or a few kyr (chimpanzees, capuchins). **The record shows that tool use arose several times within ≤0.6 Gyr of complex animals. It cannot date any non-hominin origin more precisely.**
* **Model.**
  * `n_tool_origins` is log-uniform 3–7 (best 6), and τ_stone_tools = 0.597 Gyr / n: n origins in ~0.6 Gyr read as a Poisson rate gives an expected first-origin time of 0.6/n Gyr. This mapping is ASSUMED.
  * Re-evolution after a lineage ends scales with this shorter time, so tool use is also repeatable.
  * Caveat: most origins are recent and cluster in large-brained vertebrates, which suggests a long lead time followed by rapid repeats rather than a uniform rate. Only hominins reached habitual intentional flaking.

## Similarity-weighted scenario (Earth Similarity Index)
**The user's argument.** Earth is not the only data point. Known Earth-like planets should inherit Earth's "average data" (its evolutionary timeline and step success), scaled by how similar they are, the way all electrons are assumed to behave alike. This is implemented literally, and it is labelled USER-PROPOSED.

**ESI** (`esi.py`): Schulze-Makuch et al. 2011, Astrobiology 11, 1041 (https://doi.org/10.1089/ast.2010.0592). ESI = Π(1 − |x−x₀|/(x+x₀))^(wᵢ/n) over radius (w = 0.57), bulk density (1.07), escape velocity (0.70) and surface temperature (5.58, reference 288 K), with n = 4. Weights and reference values come from the PHL table (https://phl.upr.edu/projects/earth-similarity-index-esi).
* Inputs: Archive `pl_rade` and `pl_bmasse`. Mass upper limits and missing masses are replaced by the Chen & Kipping 2017 Terran M–R relation (https://arxiv.org/abs/1603.08614).
* Density = M/R³ and v_esc = √(M/R).
* No exoplanet surface temperature is measured, so **T_surf = 288 K × S^¼** is ASSUMED (Earth-like albedo and greenhouse). The PHL flux–radius form is given as a cross-check.
* Sanity check: Earth = 1.000; Mars (R 0.532, M 0.107, S 0.431) = 0.712, compared with the 0.70 reported for Mars after the 2011 paper (https://en.wikipedia.org/wiki/Earth_Similarity_Index).
* Caveat: for radial-velocity planets the Archive radius is itself an M–R estimate from M sin i.

**ESI distribution of Archive HZ rocky planets** (R < 1.8 R⊕, Kopparapu+2014 HZ, Teff clamped to ≥2600 K):

| HZ | n | mean ESI | median | min–max | fraction ≥ 0.8 | ⟨ESI²⟩ | ⟨ESI³⟩ | ⟨ESI⁵⟩ | ⟨ESI¹⁰⟩ |
|---|---|---|---|---|---|---|---|---|---|
| conservative | 26 | 0.849 | 0.848 | 0.741–0.942 | 0.73 | 0.725 | 0.623 | 0.466 | 0.243 |
| optimistic | 41 | 0.865 | 0.867 | 0.741–0.979 | 0.83 | 0.751 | 0.655 | 0.505 | 0.282 |

Top planets by ESI (optimistic HZ). All of the top 17 orbit M dwarfs; the best non-M hosts are Kepler-442 b (K, rank 18) and Kepler-452 b (G, rank 19).

| rank | planet | dist (pc) | R (R⊕) | M used (M⊕) | mass source | S (S⊕) | ESI (4-property) | ESI (PHL flux–radius) | in conservative HZ? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Teegarden's Star b | 3.8 | 1.05 | 1.16 | Msini | 1.08 | 0.979 | 0.968 | no |
| 2 | TOI-700 d | 31.1 | 1.15 | 1.58 | M-R relationship | 0.85 | 0.942 | 0.925 | yes |
| 3 | Kepler-1649 c | 92.2 | 1.06 | 1.20 | M-R relationship | 0.75 | 0.940 | 0.897 | yes |
| 4 | GJ 3378 b | 7.7 | 1.32 | 2.30 | Msini | 0.91 | 0.938 | 0.897 | yes |
| 5 | TOI-700 e | 31.1 | 0.92 | 0.72 | M-R relationship | 1.27 | 0.932 | 0.911 | no |
| 6 | GJ 1002 b | 4.8 | 1.03 | 1.08 | Msini | 0.67 | 0.926 | 0.860 | yes |
| 7 | Ross 128 b | 3.4 | 1.11 | 1.40 | Msini | 1.38 | 0.924 | 0.881 | no |
| 8 | K2-72 e | 66.4 | 1.29 | 2.21 | M-R relationship | 1.20 | 0.923 | 0.890 | no |
| 9 | Proxima Cen b | 1.3 | 1.02 | 1.05 | Msini | 0.64 | 0.920 | 0.845 | yes |
| 10 | Kepler-438 b | 195.9 | 1.12 | 1.46 | M-R relationship | 1.40 | 0.918 | 0.876 | no |
| 11 | Wolf 1069 b | 9.6 | 1.08 | 1.26 | Msini | 0.65 | 0.915 | 0.849 | yes |
| 12 | GJ 273 b | 5.9 | 1.51 | 2.89 | Msini | 1.06 | 0.907 | 0.855 | no |

**How it enters the model.**
* Each habitable body (planet or moon, G/K or M host) gets hard-step expected times equal to Earth's observed intervals. Earth's timeline is the typical case: waiting times are still exponential, but with Earth's means.
* There is **no** Snyder-Beattie reweighting toward slow or rare steps.
* Its probability is multiplied by w = ESI^k. The galaxy-wide η⊕ is weighted by the population mean ⟨ESI^k⟩, bootstrapped per sample from the HZ-rocky list.
* Other exponents and the optimistic population are exact rescalings of the same draws, because N is linear in w.

| population, p = ESI^k | median weight | median N_now | 10th–90th | P(N<1) | median N_now, no-Rare-Earth variant |
|---|---|---|---|---|---|
| conservative, k=1 | 0.850 | 895 | 2.68 – 2.08e+05 | 0.067 | 1.90e+07 |
| conservative, k=2 | 0.726 | 763 | 2.29 – 1.77e+05 | 0.071 | 1.62e+07 |
| conservative, k=3 | 0.623 | 655 | 1.96 – 1.52e+05 | 0.076 | 1.39e+07 |
| conservative, k=5 | 0.466 | 489 | 1.47 – 1.13e+05 | 0.086 | 1.04e+07 |
| conservative, k=10 | 0.243 | 254 | 0.76 – 5.91e+04 | 0.111 | 5.40e+06 |
| optimistic, k=1 | 0.865 | 911 | 2.73 – 2.11e+05 | 0.066 | 1.93e+07 |
| optimistic, k=2 | 0.751 | 791 | 2.37 – 1.83e+05 | 0.070 | 1.68e+07 |
| optimistic, k=3 | 0.655 | 690 | 2.07 – 1.60e+05 | 0.075 | 1.46e+07 |
| optimistic, k=5 | 0.505 | 531 | 1.6 – 1.23e+05 | 0.083 | 1.13e+07 |
| optimistic, k=10 | 0.281 | 295 | 0.886 – 6.87e+04 | 0.105 | 6.26e+06 |

**Interpretation.**
* The similarity weight itself is a modest correction: ×0.85 (linear) down to ×0.24 (k = 10), because the known HZ rocky planets are fairly Earth-like on the ESI's four bulk properties.
* What moves the answer from the baseline's ~10⁻³ to ~10³ is **treating Earth's timeline as typical, with no observer-selection correction**. ESI cannot test that assumption, because it measures size, density, escape velocity and insolation, not biology.
* Electrons are interchangeable because they are measured to be identical. Planets with ESI ≈ 0.9 are not known to share Earth's chemistry, tectonics, land fraction or history.
* Earth's own timing is subject to the selection effect Snyder-Beattie+2021 describe: we necessarily live on a planet that finished in time.
* Dropping the Rare-Earth multipliers as well (`similarity_weighted_no_rare_earth`) gives ~10⁷.

## Earth as one random draw (`earth_random_draw`)
* Each of Earth's step intervals x_k is treated as a draw at a uniform-random quantile of an Exp(τ_k) waiting time. This is an uninformative prior on whether Earth was fast or slow, so τ_k = x_k/E_k with E_k ~ Exp(1) (median τ_k = 1.44 x_k).
* It is mathematically the posterior from a single observation under a scale-invariant 1/τ prior, **without** the observer-selection (completed-by-now) correction.
* Result: median **157**, 10th–90th 0.225 – 5.9e+04, P(N<1) = 0.159, P(τ_abiogenesis < 1 Gyr) = 0.61.
* The baseline differs mainly in applying that observer-selection correction (on a broad log-uniform τ prior); it gives ~10⁻³ instead of ~10². Whether to apply the correction is the main open choice in this exercise (this exact scenario with the correction added was not run).

## Species per tool-using world (`species:` in params.yaml)
* The factor multiplies **tool-using species, not worlds**: species_now = N_now × species_concurrent and species_ever = N_ever × species_cumulative. It is drawn independently and post hoc in `analyze.py`, so the finished runs were not re-run.
* **species_concurrent_per_tool_world**: log-uniform 1–5, best 2.38. Derived from the Smithsonian Human Origins "When Lived" spans (https://humanorigins.si.edu/evidence/human-fossils/species): the page lists 21 species, and 15 of them have fossils in the stone-tool era (≤3.3 Ma).
  * The mean number of coexisting hominin species from 3.3 Ma to today is **2.38**. The maximum is **5** (~236 ka: H. erectus, heidelbergensis, naledi, neanderthalensis, sapiens) and the minimum is 1 (today).
  * Homo only: mean 1.75 over 2.4 Ma to today.
  * Wood & Boyle 2016 AJPA 159:S37 (https://doi.org/10.1002/ajpa.22902) find well-supported taxic diversity in every interval from 4 Ma to c. 40 ka. They give no single total, and they warn that some taxa may be over-split.
* **species_cumulative_per_tool_world**: uniform 8–16, best 15.
  * The Smithsonian list has 8 Homo species and 15 hominins in the tool era.
  * Wikipedia's "List of Homo species" (https://en.wikipedia.org/wiki/List_of_Homo_species) names 16 Homo species, including contested ones.
  * Nathan's figure of **9–16 humanoid species** is consistent with this; it is the user's figure, now verified as plausible.
* **Context: ~2.3M named species. VERIFIED.** The Catalogue of Life estimates 2.3M extant species recognised by taxonomists (https://www.checklistbank.org/dataset/278910). The COL Base Release of 2026-07-14 lists 2,258,977 accepted species, and the Extended Release 2,496,219 (https://www.catalogueoflife.org/data/download). This is context only; it is not used in N.

## Variables (all in params.yaml)

| variable | distribution / range | best | meaning | source (URL) |
|---|---|---|---|---|
| `sfr_now` | normal 1.65 ± 0.19 | (default) | Msun/yr | Licquia & Newman 2015, ApJ 806, 96 — https://arxiv.org/abs/1407.1078 |
| `m_disk_now` | normal 5.17e10 ± 1.11e10 | (default) | Msun (disk stellar mass today) | Licquia & Newman 2015 — https://arxiv.org/abs/1407.1078 |
| `return_fraction` | uniform [0.27, 0.41] | (default) | - | Madau & Dickinson 2014 ARA&A (R=0.27 Salpeter, 0.41 Chabrier) — https://ned.ipac.caltech.edu/level5/March14/Madau/paper.pdf |
| `f_early_disk_mass` | uniform [0.4, 0.6] | (default) | fraction of disk mass formed 13.0-8.5 Gyr ago (thick-disk phase) | Snaith et al. 2015 A&A 578, A87 ('roughly half the stellar mass in first 4-5 Gyr') — https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `disk_start_gyr` | fixed 0.8 | (default) | Gyr after Big Bang (13.0 Gyr ago) | Snaith et al. 2015 (thick disk 9-13 Gyr ago) — https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `thick_end_gyr` | fixed 5.3 | (default) | Gyr after Big Bang (8.5 Gyr ago) | Snaith et al. 2015 (sharp SFR drop ~8-9 Gyr ago) — https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `stars_per_msun` | uniform [1.6, 2.8] | 1.64 | stars per Msun formed | Kroupa 2001 IMF: 1.64 H-burning stars/Msun (integrated here); 2.8 = 1/0.36 incl. brown dwarfs — https://adsabs.harvard.edu/pdf/2001mnras.322..231k |
| `f_gk` | uniform [0.1, 0.17] | (default) | fraction of stars that are G/K | RECONS 10-pc census (G 5.0% + K 11.6%); Kroupa IMF 0.6-1.1 Msun = 10% — http://www.recons.org/census.posted.htm |
| `f_m` | uniform [0.75, 0.81] | (default) | fraction of stars that are M dwarfs | RECONS 10-pc census (75%); Kroupa IMF 0.08-0.6 Msun = 81% — http://www.recons.org/census.posted.htm |
| `fp` | fixed 1.0 | (default) | - | Cassan et al. 2012 Nature 481, 167 (>=1 bound planet per star) — https://www.nature.com/articles/nature10684 |
| `ne_gk` | loguniform [0.1, 0.88] | 0.35 | rocky HZ planets per G/K star (fp folded in) | Bryson+2021 AJ 161, 36 (G-mid-K: 0.37-0.60 conservative, 0.58-0.88 optimistic); 2026 Astronomy & Computing reanalysis of 4,510 Archive transit planets: K ~0.27, F/G ~0.10 (schematic). best = K-weighted (K:G ~2:1 by number, RECONS) — https://arxiv.org/abs/2010.14812 ; https://astrobiology.com/2026/08/06/quantifying-detection-bias-and-recovering-habitable-zone-occurrence-rates-in-the-nasa-exoplanet-archive/ |
| `ne_m` | loguniform [0.16, 0.41] | 0.24 | Earth-size HZ planets per M dwarf (before the M-dwarf habitability penalties) | Dressing & Charbonneau 2015 ApJ 807, 45 (0.16 conservative, 0.24 broad HZ); 2026 Astronomy & Computing Archive reanalysis (M ~0.41, completeness-corrected; raw 4.03%) — https://arxiv.org/abs/1501.01623 ; https://astrobiology.com/2026/08/06/quantifying-detection-bias-and-recovering-habitable-zone-occurrence-rates-in-the-nasa-exoplanet-archive/ |
| `f_m_habitable` | loguniform [0.03, 1.0] | (default) | M-dwarf penalty for tidal locking + pre-main-sequence water loss (flares are separate, see multipliers.f_m_flares) | ASSUMED bracket informed by Shields+2016 Phys.Rep.; Luger & Barnes 2015; Lingam & Loeb 2018 JCAP; Haqq-Misra+2018 IJA; Snyder-Beattie+2021 prediction — https://arxiv.org/abs/1610.05765 |
| `th_gk_gyr` | loguniform [5.0, 20.0] | 7.0 | Gyr habitable window for complex life (G/K) | Rushby et al. 2013 Astrobiology (Earth HZ lifetime 6.29-7.79 Gyr; K dwarfs longer); Earth biosphere ends 0.8-1.5 Ga from now (Caldeira & Kasting 1992 via Snyder-Beattie+2021) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `th_m_gyr` | loguniform [10.0, 50.0] | 20.0 | Gyr habitable window (M dwarfs) | Rushby et al. 2013 (HZ lifetimes up to 54.7 Gyr) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `f_ghz` | loguniform [0.1, 1.0] | (default) | spatial fraction of disk stars in Galactic Habitable Zone | Lineweaver, Fenner & Gibson 2004 Science (<10% incl. time/metallicity cuts); Prantzos 2008 SSRv (whole disk by now); Gowanlock+2011 (1.2% incl. more factors) — https://arxiv.org/abs/astro-ph/0401024 |
| `t_metal_gyr` | uniform [1.0, 3.0] | (default) | Gyr after Big Bang when Earth-forming metallicity is reached (logistic midpoint, width 0.5 Gyr) | ASSUMED; informed by Lineweaver 2001 Icarus (metallicity selection; Earths avg 1.8+/-0.9 Gyr older than Earth) and Zackrisson+2016 ApJ 833, 214 — https://ui.adsabs.harvard.edu/abs/2001Icar..151..307L/abstract |
| `n_giant_hz_gk` | uniform [0.065, 0.115] | (default) | giant planets (3-25 R_earth) in optimistic HZ per G/K star | Hill et al. 2018 ApJ 860, 6 (G 6.5+/-1.9%, K 11.5+/-3.1%) — https://arxiv.org/abs/1805.03370 |
| `n_giant_hz_m` | loguniform [0.01, 0.12] | 0.06 | giant planets in optimistic HZ per M dwarf | Hill et al. 2018 (M 6+/-6%); lower bound 0.01 ASSUMED — https://arxiv.org/abs/1805.03370 |
| `f_exomoon_host` | loguniform [0.0001, 1.0] | (default) | fraction of HZ giants hosting a >~0.1-0.3 M_earth (atmosphere-retaining) moon | WIDE ASSUMED prior. Low end: Canup & Ward 2006 Nature (satellite systems ~1e-4 of planet mass -> in-situ moons Moon-to-Mars size); capture routes Williams 2013 Astrobiology, Porter & Grundy 2011 ApJL (~half of captured orbits circularise); Kepler-1625b-i (Teachey & Kipping 2018) and Kepler-1708b-i (Kipping+2022) candidates contested (Heller+2023, arXiv:2312.03786). High end: Hill+2018 'one large moon per giant' case — https://www.nature.com/articles/nature04860 |
| `f_exomoon_habitable` | loguniform [0.1, 1.0] | (default) | fraction of such moons outside the tidal/illumination 'habitable edge' | ASSUMED range; Heller & Barnes 2013 Astrobiology 13, 18 (habitable edge; tidal heating can sterilise); Williams, Kasting & Wade 1997 Nature 385, 234 (habitable moons concept) — https://arxiv.org/abs/1209.5323 |
| `r_ster0_per_gyr` | loguniform [0.001, 0.25] | (default) | per Gyr, whole-biosphere sterilisation rate today (scaled by SFR(t)/SFR_now in the past) | ASSUMED; upper bound: Earth's biosphere unsterilised for ~4 Gyr; SFR scaling motivated by Piran & Jimenez 2014 PRL (GRB hazard higher in early Universe) — https://arxiv.org/abs/1409.2506 |
| `r_bigfive_per_gyr` | uniform [9.3, 10.6] | (default) | per Gyr, Big-Five-class mass extinctions (Earth analog) | Big Five at ~444, 372, 252, 201, 66 Ma (US NPS / geologic time scale): intervals 72,120,51,135 Myr (mean 94.5 Myr => 10.6/Gyr); 5 events in 539 Myr Phanerozoic => 9.3/Gyr; Raup & Sepkoski 1982 — https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm |
| `p_bigfive_kills_toolusers` | loguniform [0.1, 1.0] | (default) | probability a Big-Five-class event ends a widespread tool-using lineage | ASSUMED (mammals, birds and many large clades survived each Big Five event) — https://www.science.org/doi/10.1126/science.215.4539.1501 |
| `r_self_per_gyr` | loguniform [0.1, 100.0] | 3.0 | per Gyr, self-inflicted / technological end-of-lineage hazard (mean 10 Myr to 10 Gyr), averaged over the whole stone-age-or-later phase | ASSUMED, no galactic data. Earth-only context (NOT used as galactic L): Urban 2024 Science (climate threatens 7.6% of species avg; 1.6% at ~1.3 C; ~1/3 at highest emissions); Ceballos & Ehrlich 2023 PNAS (73 tetrapod genera lost since 1500, ~35x background) vs PLOS Biol 2025 (102 genera, rare & decelerating) — https://www.science.org/doi/10.1126/science.adp4461 |
| `r_grb_per_gyr` | uniform [0.46, 1.4] | (default) | per Gyr today at solar radius, ozone-destroying (complex-life-lethal) long GRBs | Piran & Jimenez 2014 PRL (>90% in 5 Gyr => >=0.46/Gyr; 50% in 500 Myr => 1.4/Gyr) — https://arxiv.org/abs/1409.2506 |
| `r_sn_per_gyr` | fixed 1.5 | (default) | per Gyr, core-collapse SNe within 8 pc | Gehrels et al. 2003 ApJ 585, 1169 (1.5/Gyr; ~doubles biologically active UV) — https://arxiv.org/abs/astro-ph/0211361 |
| `p_lethal_astro` | loguniform [0.1, 1.0] | (default) | probability a GRB/SN event actually ends a tool-using lineage | ASSUMED (Gehrels+2003 note SN pathway 'may be less important than previously thought') — https://arxiv.org/abs/astro-ph/0211361 |
| `l_stone_yr` | loguniform [1.0e4, 1.0e9] | 6.6e6 | yr, intrinsic (background, non-catastrophic, non-self-inflicted) duration of the stone-age-or-later phase | Earth: >=3.3 Myr so far (Harmand+2015 Nature); Gott 1993 Copernican estimate (best = 2x elapsed); chimp stone age >=4.3 kyr (Mercader+2007 PNAS); SDO 2018 L upper ~1e9-1e10 — https://www.nature.com/articles/nature14464 |
| `m_recurrence` | loguniform [0.01, 1.0] | (default) | expected re-evolution time of tool use after loss, as a multiple of the intelligence step's tau | ASSUMED (no quantitative literature); multiple independent stone-tool lineages on Earth (Mercader+2007) suggest re-evolution can be easier than the first time — https://www.pnas.org/doi/10.1073/pnas.0607909104 |
| `f_plate_tectonics` | loguniform [0.01, 1.0] | 0.17 |  | Stern & Gerya 2024 Sci.Rep. (f_pt < 0.17); Valencia+2007 ApJL ('inevitable' on super-Earths) vs O'Neill & Lenardic 2007 GRL (stagnant lid); Stern 2016 GSF — https://www.nature.com/articles/s41598-024-54700-x |
| `f_land_and_ocean` | loguniform [0.0002, 1.0] | (default) |  | Stern & Gerya 2024 (f_oc 0.0002-0.01); Simpson 2017 MNRAS (most HZ worlds >90% ocean); stone tools need dry land — https://arxiv.org/abs/1607.03095 |
| `f_large_moon` | loguniform [0.022, 1.0] | (default) |  (not applied to exomoons) | Elser+2011 Icarus (massive moon for ~1/12 of terrestrial planets, range 1/45-1/4); Laskar+1993 vs Lissauer, Barnes & Chambers 2012 Icarus (moonless obliquity mostly modest -> moon may not be needed) — https://arxiv.org/abs/1105.4616 |
| `f_jupiter_shield` | loguniform [0.067, 1.0] | (default) |  (not applied to exomoons) | Wittenmyer+2020 MNRAS (cool Jupiters around 6.73% of stars); Horner & Jones 2008 IJA (shield role ambiguous -> may not be needed) — https://arxiv.org/abs/1912.01821 |
| `f_binary_ok` | uniform [0.8, 1.0] | (default) |  | Kraus+2016 AJ 152, 8 (close binaries <47 AU suppress planets; ~1/5 of solar-type stars disallowed); Raghavan+2010 ApJS (54% single). Upper bound 1 because Kepler eta-Earth may already include binaries — https://arxiv.org/abs/1604.05744 |
| `f_m_flares` | loguniform [0.03, 1.0] | (default) |  | ASSUMED bracket; flare/XUV/proton-event ozone & atmosphere erosion reviewed in Shields+2016 Phys.Rep.; Tilley+2019 (arXiv:1711.08484); Lingam & Loeb 2018 — https://arxiv.org/abs/1610.05765 |
| `f_k_activity` | loguniform [0.5, 1.0] | (default) |  | ASSUMED mild K-dwarf penalty (late-K flares/XUV and possible HZ tidal locking). Cuntz & Guinan 2016 ApJ 827, 79 (K dwarfs: favourable hosts, far lower activity than M dwarfs); Barnes 2017 Celest.Mech.Dyn.Astr. 129, 509 (HZ planets of low-mass stars can tidally lock within ~1 Gyr) — https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79 ; https://link.springer.com/article/10.1007/s10569-017-9783-7 |
| `f_f_uv` | loguniform [0.14, 1.0] | (default) |  | ASSUMED mapping of Sato et al. 2014 Int.J.Astrobiol. 13, 244 (F0-F8 V, 1.2-1.5 Msun: DNA damage at Earth-equivalent orbits 2.5-7.1x solar without atmospheric attenuation, much less with it): survival fraction 1/7.1 .. 1 — https://arxiv.org/abs/1312.7431 |
| `extra_worlds_per_system` | one_plus_loguniform [0.001, 0.1] | (default) |  — user scenarios only | USER-PROPOSED (speculative past intelligence on Venus/Mars): low-weight bonus for >1 tool-using world per system; not literature — user research export |
| `tau_abiogenesis` | per scenario: baseline loguniform [1e-3, 1e3] Gyr; SB2021 [1e-14, 1e10] Gyr; similarity_weighted = Earth's interval; earth_random_draw = x/Exp(1) | Earth interval | expected waiting time of this hard step; on Earth it completed 3.9 Ga | Snyder-Beattie+2021 Table 1 (3.5->4.1 Gya range) — https://pmc.ncbi.nlm.nih.gov/articles/PMC7997718/ |
| `tau_oxygenic_photosynthesis_GOE` | per scenario: baseline loguniform [1e-3, 1e3] Gyr; SB2021 [1e-14, 1e10] Gyr; similarity_weighted = Earth's interval; earth_random_draw = x/Exp(1) | Earth interval | expected waiting time of this hard step; on Earth it completed 2.4 Ga | Lyons, Reinhard & Planavsky 2014 Nature (GOE ~2.4-2.3 Ga) — https://www.nature.com/articles/nature13068 |
| `tau_eukaryogenesis` | per scenario: baseline loguniform [1e-3, 1e3] Gyr; SB2021 [1e-14, 1e10] Gyr; similarity_weighted = Earth's interval; earth_random_draw = x/Exp(1) | Earth interval | expected waiting time of this hard step; on Earth it completed 1.84 Ga | Betts+2018 via Snyder-Beattie+2021 Table 1 (<1.84 Ga) — https://pmc.ncbi.nlm.nih.gov/articles/PMC7997718/ |
| `tau_complex_multicellularity` | per scenario: baseline loguniform [1e-3, 1e3] Gyr; SB2021 [1e-14, 1e10] Gyr; similarity_weighted = Earth's interval; earth_random_draw = x/Exp(1) | Earth interval | expected waiting time of this hard step; on Earth it completed 0.6 Ga | Knoll 2011 Annu.Rev.EPS (animal complex multicellularity, Ediacaran) — https://www.annualreviews.org/content/journals/10.1146/annurev.earth.031208.100209 |
| `tau_stone_tool_intelligence` | per scenario: baseline loguniform [1e-3, 1e3] Gyr; SB2021 [1e-14, 1e10] Gyr; similarity_weighted = Earth's interval; earth_random_draw = x/Exp(1) | Earth interval | expected waiting time of this hard step; on Earth it completed 0.0033 Ga | Harmand+2015 Nature (Lomekwi 3, 3.3 Ma) — https://www.nature.com/articles/nature14464 |
| `f_star_M` | uniform [0.749, 0.811] | midpoint | fraction of stars formed that are M dwarfs (v2 multi-spectral) | RECONS 10-pc census 283/378 = 0.749; Kroupa 2001 IMF number fraction 0.08-0.6 Msun = 0.811 (integrated here) — http://www.recons.org/census.posted.htm |
| `ne_M` | loguniform [0.16, 0.41] | 0.24 | Earth-size HZ planets per M dwarf (v2 multi-spectral) | Dressing & Charbonneau 2015 ApJ 807, 45 (0.16 conservative, 0.24 broad HZ); 2026 Astronomy & Computing Archive reanalysis (M ~0.41) — https://arxiv.org/abs/1501.01623 |
| `th_M_gyr` | loguniform [10.0, 50.0] | 20.0 | Gyr habitable window (v2 multi-spectral) | Rushby et al. 2013 Astrobiology 13, 833 (HZ lifetimes up to 54.7 Gyr) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `n_giant_hz_M` | loguniform [0.01, 0.12] | 0.06 | HZ giants per star (exomoon hosts) (v2 multi-spectral) | Hill et al. 2018 ApJ 860, 67 Table: M 6.0+/-6.0%; lower bound 0.01 ASSUMED — https://arxiv.org/abs/1805.03370 |
| `f_star_K` | uniform [0.077, 0.116] | midpoint | fraction of stars formed that are K dwarfs (v2 multi-spectral) | Kroupa 2001 IMF 0.6-0.9 Msun = 0.077 (integrated here); RECONS 44/378 = 0.116 — http://www.recons.org/census.posted.htm |
| `ne_K` | loguniform [0.27, 0.88] | 0.49 | rocky HZ planets per K dwarf (v2 multi-spectral) | 2026 Astronomy & Computing Archive reanalysis K ~0.27 (low); Bryson+2021 AJ 161, 36 G-mid-K 0.37-0.60 conservative / 0.58-0.88 optimistic (high) — https://arxiv.org/abs/2010.14812 ; https://astrobiology.com/2026/08/06/quantifying-detection-bias-and-recovering-habitable-zone-occurrence-rates-in-the-nasa-exoplanet-archive/ |
| `th_K_gyr` | loguniform [8.0, 30.0] | 15.0 | Gyr habitable window (v2 multi-spectral) | ASSUMED bracket informed by Rushby+2013 (Earth 6.29-7.79 Gyr; K/M hosts longer because of slower HZ migration; Kepler candidates up to 18.8 Gyr) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `n_giant_hz_K` | uniform [0.084, 0.146] | midpoint | HZ giants per star (v2 multi-spectral) | Hill et al. 2018: K 11.5+/-3.1% (+/-1 sigma) — https://arxiv.org/abs/1805.03370 |
| `f_star_G` | uniform [0.026, 0.05] | midpoint | fraction of stars formed that are G dwarfs (v2 multi-spectral) | Kroupa 2001 IMF 0.9-1.1 Msun = 0.026 (integrated here); RECONS 19/378 = 0.050 — http://www.recons.org/census.posted.htm |
| `ne_G` | loguniform [0.1, 0.88] | 0.3 | rocky HZ planets per G dwarf (v2 multi-spectral) | 2026 Astronomy & Computing Archive reanalysis F/G ~0.10 (low); Bryson+2021 G-mid-K up to 0.88 optimistic (high) — https://arxiv.org/abs/2010.14812 |
| `th_G_gyr` | loguniform [5.0, 10.0] | 6.5 | Gyr habitable window (v2 multi-spectral) | Rushby+2013 (Earth HZ lifetime 6.29-7.79 Gyr); Earth biosphere ends 0.8-1.5 Ga from now (Caldeira & Kasting 1992 via Snyder-Beattie+2021) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `n_giant_hz_G` | uniform [0.046, 0.084] | midpoint | HZ giants per star (v2 multi-spectral) | Hill et al. 2018: G 6.5+/-1.9% (+/-1 sigma) — https://arxiv.org/abs/1805.03370 |
| `f_star_F` | uniform [0.0185, 0.0285] | midpoint | fraction of stars formed that are F dwarfs (v2 multi-spectral) | RECONS 7/378 = 0.0185 (present day; some F stars have already died); Kroupa 2001 IMF 1.1-1.5 Msun = 0.0285 (integrated here) — http://www.recons.org/census.posted.htm |
| `ne_F` | loguniform [0.03, 0.6] | 0.1 | rocky HZ planets per F dwarf (v2 multi-spectral) | 2026 Archive reanalysis F/G ~0.10 (best); Bryson+2021 sample extends only to 6300 K (upper 0.60 = its conservative upper bound); low 0.03 ASSUMED (poor Kepler completeness for F hosts) — https://arxiv.org/abs/2010.14812 |
| `th_F_gyr` | loguniform [1.5, 5.0] | 2.7 | Gyr habitable window (v2 multi-spectral) | ASSUMED; F stars (1.2-1.5 Msun) have short main-sequence lifetimes that constrain habitability (Sato et al. 2014 Int.J.Astrobiol. 13, 244); Rushby+2013 only modelled 0.2-1.2 Msun — https://arxiv.org/abs/1312.7431 |
| `n_giant_hz_F` | uniform [0.046, 0.084] | midpoint | HZ giants per star (v2 multi-spectral) | ASSUMED = G value (Hill et al. 2018 report no F-star rate) — https://arxiv.org/abs/1805.03370 |
| `stage_tau_agri_yr` | loguniform [3.3e5, 3.3e7] | 3.29e6 | yr, expected time lithic -> agricultural (v2 multiphase) | Earth anchor 3.3 Ma (Harmand+2015 Lomekwi 3) -> ~11.5 ka (Zeder 2011 Curr.Anthropol. 52, S221) = 3.29 Myr; range = Earth/10 .. Earth x10 ASSUMED — https://www.nature.com/articles/nature14464 ; https://doi.org/10.1086/659307 |
| `stage_tau_ind_yr` | loguniform [1.1e3, 1.1e5] | 1.1e4 | yr, expected time agricultural -> industrial (v2 multiphase) | Earth anchor ~11.5 ka -> ~1760 CE (~11.2 kyr); range Earth/10 .. x10 ASSUMED — https://doi.org/10.1086/659307 ; https://www.britannica.com/event/Industrial-Revolution |
| `stage_tau_radio_yr` | loguniform [14.0, 1400.0] | 135.0 | yr, expected time industrial -> radio-capable (v2 multiphase) | Earth anchor ~1760 -> 1895 (Marconi's first radio transmissions) = ~135 yr (user: ~150 yr); range Earth/10 .. x10 ASSUMED — https://www.britannica.com/biography/Guglielmo-Marconi |
| `stage_tau_space_yr` | loguniform [6.2, 620.0] | 62.0 | yr, expected time radio -> spacefaring (orbital spaceflight) (v2 multiphase) | Earth anchor 1895 -> 1957 (Sputnik 1) = 62 yr; range Earth/10 .. x10 ASSUMED — https://www.nasa.gov/history/sputnik/ |
| `stage_h_agri_per_yr` | loguniform [1e-07, 0.001] | geometric mean | per yr, world-wide collapse hazard of the agricultural stage (v2 multiphase) | ASSUMED. Earth: farming has persisted ~11.5 kyr world-wide despite many regional collapses (Tainter 1988, The Collapse of Complex Societies); one world gives no galactic rate — https://doi.org/10.1086/659307 |
| `stage_h_ind_per_yr` | loguniform [1e-06, 0.01] | geometric mean | per yr, world-wide collapse hazard of the industrial stage (v2 multiphase) | ASSUMED (Earth: ~265 yr industrial so far). Natural extinction alone is < 6.9e-5/yr (Snyder-Beattie, Ord & Bonsall 2019 Sci.Rep. 9, 11054), so most of this range is anthropogenic risk, which that bound does not cover — https://www.nature.com/articles/s41598-019-47540-7 |
| `stage_h_radio_per_yr` | loguniform [1e-10, 0.01] | geometric mean | per yr, collapse hazard of the radio-capable stage (v2 multiphase) | 1/L with L log-uniform 1e2 .. 1e10 yr = Sandberg, Drexler & Ord 2018 Table 1 (lifetime of a detectable civilisation) — https://arxiv.org/abs/1806.02404 |
| `stage_h_space_per_yr` | loguniform [1e-10, 0.01] | geometric mean | per yr, collapse hazard of the spacefaring stage (v2 multiphase) | Same as radio stage (SDO 2018 L 1e2 .. 1e10 yr); ASSUMED that orbital capability does not by itself lower the hazard — https://arxiv.org/abs/1806.02404 |
| `stage_q_regress` | uniform [0.0, 1.0] | midpoint | fraction of stage collapses that regress one stage (and can recur) instead of ending the tool-using lineage (v2 multiphase) | ASSUMED (no quantitative literature). Earth's regional collapses mostly regressed rather than ended lineages (Tainter 1988) — https://www.cambridge.org/core/books/collapse-of-complex-societies/ |
| `f_superhab` | loguniform [0.03, 0.43] | 0.104 | fraction of K-dwarf habitable planets meeting the superhabitable criteria (~1.0-1.5 R_earth, ~5 K warmer); age 5-8 Gyr is handled by the time model; applied to K hosts only (nathan_headline only) | ASSUMED bracket around an Archive-derived 0.104 = P(1.0<=R<=1.5 given HZ, R<2) 25/49 x P(T_surf 282-302 K given HZ, R<2) 10/49 (superhab.py; independence assumed). (v1 used 0.073 = 0.104 x K share 0.70 of G/K.) Criteria: Schulze-Makuch, Heller & Guinan 2020 Astrobiology 20, 1394 Table 2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC7757576/ |
| `superhab_boost` | loguniform [1.0, 3.0] | 1.73 | multiplier (>1) on the per-planet step-success probability for superhabitable planets (capped so probability <= 1) (nathan_headline only) | ASSUMED (user-suggested 1-3x). Schulze-Makuch+2020 and Heller & Armstrong 2014 (Astrobiology 14, 50) argue qualitatively for higher habitability/biomass but give no numeric factor — https://doi.org/10.1089/ast.2013.1088 |
| `n_tool_origins` | loguniform [3.0, 7.0] | 6.0 | effective number of independent origins of tool use among complex animals on Earth; tau_stone_tool_intelligence = 0.5967 Gyr (Earth's multicellularity->stone-tools interval) / n (nathan_headline only) | Low 3 = independent lithic-flake-producing primate lineages (hominins, Harmand+2015; bearded capuchins, Proffitt+2016 Nature 539, 85; long-tailed macaques, Proffitt+2023 Sci.Adv. 9, eade8159). Best 6 = the user's list, each verified: primates (Goodall 1964 Nature 201, 1264), corvids (Hunt 1996 Nature 379, 249), octopus (Finn, Tregenza & Norman 2009 Curr.Biol. 19, R1069), sea otters (Hall & Schaller 1964 J.Mammal. 45, 287), dolphins (Kruetzen+2005 PNAS 102, 8939), elephants (Hart+2001 Anim.Behav. 62, 839). High 7 = classes with documented tool use (Bentley-Condit & Smith 2010 Behaviour 147, 185: three phyla, seven classes). Mapping origins -> Poisson rate (n events in ~0.6 Gyr => expected first-origin time 0.6/n Gyr) is ASSUMED — https://doi.org/10.1038/nature20112 ; https://www.science.org/doi/10.1126/sciadv.ade8159 ; https://brill.com/view/journals/beh/147/2/article-p185_3.xml |
| `w_similarity` | bootstrap mean of ESI^k over Archive HZ-rocky planets (similarity scenarios only) | ⟨ESI⟩ = 0.849 (conservative, k=1) | similarity weight applied to every habitable body | Schulze-Makuch+2011; PHL — https://phl.upr.edu/projects/earth-similarity-index-esi |
| `species_concurrent_per_tool_world` | loguniform [1.0, 5.0] | 2.38 | time-averaged number of coexisting hominin(-grade) species on a world during its stone-age-or-later phase (post hoc, multiplies species not worlds) | Derived from Smithsonian Human Origins 'When Lived' spans (21 species; 15 have fossils <=3.3 Ma): over 3.3 Ma-present the mean number of coexisting hominin species = 2.38 (best), max 5 (e.g. ~236 ka: H. erectus, heidelbergensis, naledi, neanderthalensis, sapiens), min 1 (today); Homo-only mean 1.75 over 2.4 Ma-present. Wood & Boyle 2016 AJPA: taxic diversity (>1 species) in every interval from 4 Ma to c.40 ka. Fossil spans are minima (Signor-Lipps) and taxonomy may be over-split. — https://humanorigins.si.edu/evidence/human-fossils/species ; https://doi.org/10.1002/ajpa.22902 |
| `species_cumulative_per_tool_world` | uniform [8.0, 16.0] | 15.0 | hominin species ever produced per tool-using world (~3.3 Myr of Earth's record) (post hoc, multiplies species not worlds) | Smithsonian list: 8 Homo species, 15 hominin species with fossils in the stone-tool era (best); Wikipedia 'List of Homo species' names 16 Homo species incl. contested ones; USER figure 9-16 'humanoid species' (consistent). Earth-only, ~3.3 Myr; worlds with longer phases could have more. — https://humanorigins.si.edu/evidence/human-fossils/species ; https://en.wikipedia.org/wiki/List_of_Homo_species |

Default `best`: geometric mean for log-uniform, midpoint for uniform, mean for normal.
User-scenario overrides: `l_stone_yr` log-uniform [5e4, 2e5] yr (USER); `th_gk_gyr` uniform [7.5, 9.5] Gyr (USER: Sun ~4 Gyr left); in `user_fast_intelligence`, `tau_stone_tool_intelligence` log-uniform [1e-5, 1e-4] Gyr (USER, 'tens of kyr'); `similarity_weighted_no_rare_earth` fixes f_plate, f_land, f_large_moon, f_jupiter, f_binary = 1.


## Data sources: what each factor can and cannot get from data
| factor | best available source used here | what it CANNOT give |
|---|---|---|
| R* / SFR(t) | Licquia & Newman 2015 (SFR, disk mass); Snaith+2015 (SFH shape); Kroupa 2001 IMF; NASA/RECONS stellar catalogs for class fractions | A single galactic star-formation rate. NASA stellar catalogs are local samples, and SFR(t) is a model reconstruction |
| fp | NASA Exoplanet Archive (6,375 confirmed in `pscomppars` on 1 Oct 2026); Cassan+2012 microlensing | A rate. Raw archive fractions are detection-biased and need a completeness model |
| ne | Archive + Kopparapu+2014 HZ limits (counts below); Bryson+2021; Dressing & Charbonneau 2015; 2026 Astronomy & Computing reanalysis (K ~0.27, M ~0.41) | Proof of water, atmosphere, magnetic field or volcanism (the user's "ne package"). HZ means only "the right insolation" |
| exomoons | Archive HZ giants (counts below); Hill+2018 occurrence | Any confirmed exomoon. Both candidates (Kepler-1625b-i, Kepler-1708b-i) are contested |
| fl | **Nothing outside Earth.** NCBI (user-cited: ~3.56M genomes, ~46.5k reference), DOE JGI IMG and NIH All of Us describe Earth life only | A probability. They are an Earth-only prior and say nothing about how often life starts elsewhere. No fl was derived from them |
| fi / f_stone | No governmental dataset. Earth timing (fossil record) via the Snyder-Beattie+2021 hard-step update; ITIS, USDA PLANTS, NOAA Fisheries, FWS ECOS and GBIF species baselines are Earth context only | A frequency of intelligence elsewhere |
| fc | No federal SETI archive. Irrelevant to stone-age N | – |
| Earth similarity | NASA Exoplanet Archive radii/masses/insolation → Schulze-Makuch+2011 ESI (`esi.py`) | Biology. ESI compares bulk size, density, escape velocity and (here assumed) temperature only; RV radii are M–R estimates |
| superhabitability | Schulze-Makuch+2020 criteria applied to Archive host Teff, radius, insolation, stellar age (`superhab.py`) | O₂ level, land/sea pattern, moon, tectonics, magnetic field (not observable); any numeric habitability boost |
| cross-lineage tool use | Primary behavioural literature (table in the nathan_headline section); Bentley-Condit & Smith 2010 catalog | Dates of non-hominin origins (behaviour rarely fossilises); any rate for other worlds |
| species per tool world | Smithsonian Human Origins species list and date spans; Wood & Boyle 2016; Wikipedia list of Homo species; Catalogue of Life (2.3M named species, context) | Any non-Earth rate; fossil spans are minima and taxonomy is debated |
| L / extinction | Big Five dates (US NPS / geologic time scale), Raup & Sepkoski 1982; Piran & Jimenez 2014 (GRB); Gehrels+2003 (SN); Earth context: Urban 2024 Science, Ceballos & Ehrlich 2023 PNAS, PLOS Biol 2025 (102 genera) | A galactic L. USGS, NOAA and FWS data are Earth analogs only |

### NASA Exoplanet Archive HZ counts (data/hz_counts.json; Kopparapu+2014 1-M⊕ coefficients, Teff 2600–7200 K)
* Confirmed planets in `pscomppars` on 1 Oct 2026: **6,375**. The user's figure is 6,366 as of 11 Sep 2026, consistent with steady growth. 4,741 are flagged as transiting.
* Rocky (R < 1.8 R⊕) in the **conservative** HZ (runaway → maximum greenhouse): **23**, or **26** when hosts cooler than 2600 K are clamped to 2600 K, which adds TRAPPIST-1 e, f, g. By host type (unclamped): 19 M, 3 K, 1 G.
* Rocky in the **optimistic** HZ (recent Venus → early Mars): **37**, or **41** with clamping (adds TRAPPIST-1 d–g). By host type: 31 M, 5 K, 1 G.
* The user's flat 0.36–1.1 S⊕ cut with R < 1.8 R⊕ gives **25**.
* For comparison, Bohl et al. 2026 (MNRAS, Cornell; Archive + Gaia DR3; rocky = <2 R⊕ or <5 M⊕) find **45** in their empirical HZ and **24** in a narrower 3D-model HZ. Verified: https://news.cornell.edu/stories/2026/03/where-find-other-earths-new-list-narrows-down-targets
* **HZ giants** (M > 0.3 MJ or R > 6 R⊕, possible exomoon hosts): **118** conservative, **159** optimistic (93 G, 36 K, 24 F, 6 M).
* These are raw detections. Transit geometry and long periods bias them heavily, so they are **not** used directly as ne. The 2026 reanalysis (verified via astrobiology.com, Astronomy & Computing) reports raw HZ fractions of 0.33% F/G, 0.72% K and 4.03% M, against completeness-corrected rates of ~0.27 (K) and ~0.41 (M). The correction is roughly 10–40×.

## The user's own claims and inputs (kept separate from the literature; compared in results)
From Nathan's research export (Grok and X). These are **user-proposed, not sourced literature**:
* 9 Jun 2025: "likely 1–3 intelligent civilizations at a time in this galaxy"; detection would need our species to last millions of years because of light-travel delay.
* 18 Feb 2026: "a handful at the same time in our galaxy, or none in the Universe".
* 2 Oct 2026 thread: "best case 50–100 intelligent races over a star's life in a galaxy, already dead; absolute best case 1–2 stone-age-or-better at the same time". @grok called "about 1" the 50/50 under the stated inputs. The thread also mentioned a **50–200 kyr stone-age-or-better extinction window**, the binary-star fraction, supernova/pulsar/flare rates, and a ~100-yr radio bubble.
* 30 Jul 2026: ne = water + volcanism + atmosphere + magnetic field + time; a "habitability window of several million years"; time-to-intelligence of "tens of thousands of years"; the Sun has ~4 Gyr left.
* Speculative past intelligence on Venus or Mars, used as a low-weight extra-worlds-per-system bonus in the user scenarios only.
* The simulation-theory 20–80% prior was used by the user only as a comparison and is **not** a Drake factor here.
* The user gave no numeric R*, fp, ne, fl, fi or fc.

How they are used: the 50–200 kyr window and ~4 Gyr remaining go into `user_inputs`, and "tens of kyr to intelligence" goes into `user_fast_intelligence`. Conflicts:
* The Big Five are spaced ~51–135 Myr apart (mean ~95 Myr). The geological record does **not** support a guaranteed 50–200 kyr wipeout clock, and Homo-lineage stone-tool use has already lasted ≥3.3 Myr (Harmand+2015).
* A habitable window of "several Myr" is far shorter than the Gyr-scale HZ lifetimes (Rushby+2013), so it is not used.
* "Tens of kyr to intelligence" is ruled out for Earth's animal-to-tools step, which took ~0.6 Gyr.

## Classic static comparison (Sandberg, Drexler & Ord 2018, stone-age variant)
| variable | distribution | source |
|---|---|---|
| `R_star` | loguniform [1, 100] | SDO 2018 Table 1 |
| `fp` | loguniform [0.1, 1] | SDO 2018 Table 1 |
| `ne` | loguniform [0.1, 1] | SDO 2018 Table 1 |
| `log10_lambdaVt` | log10 ~ normal(0, 50) | SDO 2018: fl = 1-exp(-lambda V t), log-normal, sigma = 50 decades, median 1 |
| `fi` | loguniform [0.001, 1] | SDO 2018 Table 1 |
| `f_stone` | loguniform [0.1, 1] | ASSUMED (replaces fc): fraction of intelligent lineages reaching habitual stone-tool use |
| `L_stone` | loguniform [1.0e4, 1.0e9] | same as l_stone_yr above |
## Other references used
* Sandberg, Drexler & Ord 2018, Dissolving the Fermi Paradox: https://arxiv.org/abs/1806.02404. Log-uniform uncertainty approach; their median N = 0.32 and P(N<1) = 52% for radio civilizations.
* Westby & Conselice 2020 ApJ 896, 58: https://iopscience.iop.org/article/10.3847/1538-4357/ab8225. Strong Astrobiological Copernican limit: ≥36 (+175/−32) communicating civilizations for L = 100 yr, mostly around M dwarfs.
* Frank & Sullivan 2016 Astrobiology 16, 359: https://arxiv.org/abs/1510.08837. "Archaeological" form. Humanity is unique in cosmic history only if f_bt < ~10⁻²²–10⁻²⁴.
* Kipping 2020 PNAS 117, 11995: https://www.pnas.org/doi/abs/10.1073/pnas.1921655117. Odds >3:1 that abiogenesis is fast and 3:2 that intelligence is rare.
* Snyder-Beattie, Sandberg, Drexler & Bonsall 2021 Astrobiology 21, 265: https://pmc.ncbi.nlm.nih.gov/articles/PMC7997718/
* Carter 1983 Phil Trans R Soc A 310, 347: https://ui.adsabs.harvard.edu/abs/1983RSPTA.310..347C/abstract
* Hanson 1998, The Great Filter: https://mason.gmu.edu/~rhanson/greatfilter.html
* Watson 2008 Astrobiology 8, 175: https://pubmed.ncbi.nlm.nih.gov/18237258/
* Lineweaver 2001 Icarus: https://ui.adsabs.harvard.edu/abs/2001Icar..151..307L/abstract. Used as a sanity check on planet ages.
* Lingam & Loeb 2018 JCAP, Is life most likely around Sun-like stars?: https://arxiv.org/abs/1710.11134
* Kopparapu et al. 2014 ApJL 787, L29 (HZ coefficients): https://arxiv.org/abs/1404.5292
* Gott 1993 Nature (Copernican duration argument): https://gwern.net/doc/existential-risk/1993-gott.pdf
* Teachey & Kipping 2018 Sci. Adv. (Kepler-1625b-i): https://www.science.org/doi/10.1126/sciadv.aav1784. Kipping+2022 Nat. Astron. (Kepler-1708b-i): https://www.nature.com/articles/s41550-021-01539-1. Heller+2023 rebuttal: https://arxiv.org/abs/2312.03786
* Williams, Kasting & Wade 1997 Nature 385, 234 (habitable moons; they need enough mass to retain an atmosphere and a magnetic field): https://www.nature.com/articles/385234a0

## Caveats
* **The answer is prior-dominated.** The hard-step τ priors and the Rare-Earth multipliers span many decades, and the median moves by orders of magnitude between defensible priors (baseline vs. Snyder-Beattie bounds). Read the "median" as a summary of stated uncertainty, not a measurement.
* Several brackets are labelled **ASSUMED** in `params.yaml`, where no quantitative literature exists: the M-dwarf penalties, sterilisation rate, recurrence multiplier, self-inflicted hazard, metallicity ramp, the moon-host fraction, and the lower bounds of some multipliers.
* The Rare-Earth multipliers are treated as independent. They are probably correlated (for example, plate tectonics with land fraction), and the Stern & Gerya 2024 ranges are themselves pessimistic.
* The Earth-timing update uses a single Earth history. Transition dates are uncertain by hundreds of Myr, and the binned convolution (20-Myr bins) biases completion times by ≲50 Myr.
* η⊕ values are survey-dependent. Kepler η⊕ may already include binaries, so the binary factor's upper bound is 1.
* Counting is per **world**, not per species. Earth today arguably has several "stone-age" lineages (humans; chimpanzee stone age per Mercader+2007), but it counts once.
* No conditioning on the Fermi observation. Stone-age worlds are undetectable at interstellar range anyway.
* **Similarity weighting** (user-proposed) is not a measurement of biology. ESI uses four bulk properties, with the temperature assumed from insolation. The large jump in N for `similarity_weighted` and `earth_random_draw` comes from treating Earth's timeline as typical, i.e. dropping the observer-selection correction, not from the ESI values.
* The ESI population is dominated by M-dwarf planets (most HZ rocky detections). It is applied as a weight for G/K and M hosts alike.
* Species counts assume Earth's hominin radiation (2.38 coexisting, 15 total over ~3.3 Myr) is typical for every tool world. Both counts depend on taxonomic splitting.
* The new scenarios use 2e5 samples. They have no importance weights (ESS = n).
* **nathan_headline caveat:** this is the user's chosen framing. It inherits similarity_weighted's key assumption that Earth's timeline is typical, with no observer-selection correction. That assumption, not the two new factors, accounts for most of the gap from the literature baseline. The superhab boost and the origins→rate mapping are ASSUMED. No confirmed Archive planet meets the superhabitable criteria (Kepler-62 f is the closest), and only 23 of the paper's 24 candidate names could be read.
* **Multi-spectral (v2).** The F-star η⊕ low end and habitable window, the K-activity and F-UV penalties, the F-star HZ-giant rate, and the mass bins behind the Kroupa fractions are ASSUMED. Per-type ESI lists are tiny (M 22, K 3, G 1, F 0 conservative HZ planets), so G and F use the pooled list. The K share is driven mainly by K's higher η⊕ range, its longer habitable window and the superhabitability boost (K only).
* **Multiphase (v2).** Stage advance times are Earth/10 to Earth×10 around one Earth history; the agricultural and industrial collapse hazards and the regress fraction are ASSUMED; the radio and spacefaring hazards reuse Sandberg, Drexler & Ord 2018's 1e2–1e10 yr lifetime prior. Stage shares use the long-run (stationary) occupancy of the stage chain, which ignores worlds that started their tool-using phase within the last few Myr. The stage-specific hazards are added on top of the v1 self-inflicted hazard `r_self_per_gyr`, so some self-inflicted risk may be counted twice (conservative for N).
