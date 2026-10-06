# Time-aware extended Drake equation: simultaneous stone-age-or-greater civilizations in the Milky Way

*Model by Nathan A. Meeks.* A Monte Carlo, time-resolved Drake model that counts how many worlds in the Milky Way have stone-tool-using (or more advanced) life **at the same time as us**.

## Headline

| | Nathan's headline (`nathan_headline`) | Literature baseline (`baseline`) |
|---|---|---|
| **Median (50/50) worlds now, other than Earth** | **2.79e+03** | **0.00204** |
| 10th–90th percentile | 13.8 – 4.36e+05 | 4.33e-07 – 7.99 |
| Mean | 7.27e+05 | 1.73e+03 |
| P(N < 1) | 0.027 | 0.832 |
| Median tool-using species now | 6.2e+03 | 0.00446 |
| Median worlds that ever had tool users (by now) | 5.66e+04 | 1.18 |
| Median radio-capable worlds now (radio + spacefaring stages) | 45.5 | 3.01e-05 |
| Largest host-type share of N (share of mean) | K dwarfs 65% | K dwarfs 58% |
| Median nearest-neighbour distance at the median N | 776 ly | 9.22e+05 ly (N<1: no neighbour expected) |
| Equal-cube side at the median N (disk ≈ 7.9e12 ly³) | 1.41e+03 ly | 1.57e+05 ly |

![All scenarios compared](results/comparison_scenarios.png)

Headline histogram: [`results/hist_log10N.png`](results/hist_log10N.png) · sensitivity tornado: [`results/tornado.png`](results/tornado.png) · literature baseline: [`hist`](results/hist_log10N_baseline.png), [`tornado`](results/tornado_baseline.png)

## Multi-spectral and multiphase breakdowns (v2 model)

Suggested by a friend of Nathan's (Oct 2026). Re-run with the v2 model (2e5 samples each): `baseline`, `baseline_no_exomoons`, `nathan_headline`, `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`. Every other scenario is still the v1 model (two host classes, G/K and M, and one stone-age-or-greater phase).

Change in the median N_now from v1 to v2: `nathan_headline` 3.18e+03 (v1) → 2.79e+03 (v2); `baseline` 0.00238 (v1) → 0.00204 (v2). The v2 total adds F stars, splits G from K (K now has its own, higher η⊕ and longer habitable window), adds K-activity and F-UV penalties and per-type ESI weights, and adds stage-specific collapse hazards after the lithic stage.

![Multi-spectral breakdown](results/spectral_breakdown.png)

### By host star type

Each type has its own star fraction (RECONS and Gaia-EDR3 10-pc censuses vs Kroupa IMF), η⊕, habitable window, HZ giants for exomoons, activity/UV/tidal penalties, and similarity weight (its own Archive ESI list if it has ≥ 3 HZ rocky planets, otherwise the pooled list). The superhabitability boost applies only to K hosts. *Share* = that type's fraction of the posterior-mean N; *median share* = per-sample median of the type's fraction.

| scenario | host type | median N now | 10th–90th pct | P(N<1) | share of mean N | median share [10th, 90th] | median N ever |
|---|---|---|---|---|---|---|---|
| nathan_headline | M | **277** | 1.05 – 5.94e+04 | 0.098 | 25.8% | 11.5% [1.7, 49.3] | 5.08e+03 |
| nathan_headline | K | **1.82e+03** | 9 – 2.87e+05 | 0.034 | 64.9% | 72.7% [40.6, 90.0] | 3.23e+04 |
| nathan_headline | G | **244** | 1.23 – 3.81e+04 | 0.091 | 9.2% | 9.4% [2.7, 25.9] | 1.02e+04 |
| nathan_headline | F | **1.62** | 0.0065 – 319 | 0.456 | 0.1% | 0.1% [0.0, 0.6] | 472 |
| nathan_headline | **all** | **2.79e+03** | 13.8 – 4.36e+05 | 0.027 | 100% | – | 5.66e+04 |
| baseline | M | **2.31e-04** | 4.13e-08 – 1.1 | 0.898 | 35.6% | 13.0% [1.9, 52.2] | 0.122 |
| baseline | K | **0.00141** | 2.91e-07 – 5.47 | 0.847 | 58.5% | 77.8% [41.8, 94.3] | 0.745 |
| baseline | G | **6.29e-05** | 1.23e-08 – 0.28 | 0.932 | 5.8% | 3.7% [0.5, 18.1] | 0.102 |
| baseline | F | **5.82e-08** | 7.88e-12 – 4.02e-04 | 0.994 | 0.1% | 0.0% [0.0, 0.1] | 3.50e-04 |
| baseline | **all** | **0.00204** | 4.33e-07 – 7.99 | 0.832 | 100% | – | 1.18 |

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
| `stage_h_agri_per_yr` | loguniform [1e-07, 0.001] | geometric mean | ASSUMED. Earth: farming has persisted ~11.5 kyr world-wide despite many regional collapses (Tainter 1988, The Collapse of Complex Societies); one world gives no galactic rate. Regional data do not map onto a world-wide rate: Kemp 2019 (87 civilisations 3000 BCE-600 CE: mean lifespan 336 yr, median ~250 yr) and Scheffer et al. 2023 PNAS 120, e2218834120 (hundreds of premodern states, Seshat and MOROS data: termination risk rises over the first ~200 yr, then plateaus) measure the end of polities, after which farming continued; the regional rate (~3e-3/yr) is only a loose upper context. URLs: https://www.bbc.com/future/article/20190218-the-lifespans-of-ancient-civilisations-compared ; https://www.pnas.org/doi/10.1073/pnas.2218834120 |
| `stage_h_ind_per_yr` | loguniform [1e-06, 0.01] | geometric mean | ASSUMED (Earth: ~265 yr industrial so far). Natural extinction alone is < 6.9e-5/yr (Snyder-Beattie, Ord & Bonsall 2019 Sci.Rep. 9, 11054), so most of this range is anthropogenic risk, which that bound does not cover |
| `stage_h_radio_per_yr` | loguniform [1e-10, 0.01] | geometric mean | 1/L with L log-uniform 1e2 .. 1e10 yr = Sandberg, Drexler & Ord 2018 Table 1 (lifetime of a detectable civilisation). SETI gives no duration: Breakthrough Listen non-detections limit prevalence only (<0.066% of stellar systems within 50 pc host continuous transmitters with EIRP >~1e13 W, Wlodarczyk-Sroka, Garrett & Siemion 2020 MNRAS 498, 5720; <0.45% / <0.37% of GBT L/S-band targets above 2.1e12 W, Price+2020 AJ 159, 86), orders of magnitude above the model's radio-capable fraction, so no constraint. URLs: https://arxiv.org/abs/2006.09756 ; https://iopscience.iop.org/article/10.3847/1538-3881/ab65f1 |
| `stage_h_space_per_yr` | loguniform [1e-10, 0.01] | geometric mean | Same as radio stage (SDO 2018 L 1e2 .. 1e10 yr); ASSUMED that orbital capability does not by itself lower the hazard |
| `stage_q_regress` | uniform [0.0, 1.0] | midpoint | ASSUMED (no quantitative literature). Earth's regional collapses mostly regressed rather than ended lineages (Tainter 1988) |

| scenario | stage | median N now | 10th–90th pct | mean | P(N<1) | median share of tool-using time [10th, 90th] |
|---|---|---|---|---|---|---|
| nathan_headline | lithic | **1.75e+03** | 10.6 – 2.46e+05 | 4.40e+05 | 0.029 | 0.969 [0.201, 0.999] |
| nathan_headline | agricultural | **3.33** | 0.0138 – 627 | 1.85e+03 | 0.390 | 0.00116 [1.14e-04, 0.0128] |
| nathan_headline | industrial | **0.0376** | 1.33e-04 – 7.74 | 25.1 | 0.780 | 1.33e-05 [9.64e-07, 1.84e-04] |
| nathan_headline | radio | **0.0247** | 7.22e-05 – 6.15 | 50.9 | 0.801 | 8.52e-06 [5.00e-07, 1.55e-04] |
| nathan_headline | spacefaring | **43.8** | 0.0203 – 5.79e+04 | 2.86e+05 | 0.271 | 0.0206 [1.47e-04, 0.796] |
| nathan_headline | **radio-capable (radio + spacefaring)** | **45.5** | 0.0228 – 5.8e+04 | 2.86e+05 | 0.266 | – |
| baseline | lithic | **0.00128** | 3.34e-07 – 4.05 | 1.11e+03 | 0.853 | 0.969 [0.203, 0.999] |
| baseline | agricultural | **2.30e-06** | 4.94e-10 – 0.00948 | 5 | 0.981 | 0.00115 [1.15e-04, 0.0127] |
| baseline | industrial | **2.91e-08** | 4.28e-12 – 1.23e-04 | 0.0697 | 0.998 | 1.33e-05 [9.86e-07, 1.90e-04] |
| baseline | radio | **1.82e-08** | 2.70e-12 – 9.16e-05 | 0.0643 | 0.998 | 8.73e-06 [5.07e-07, 1.57e-04] |
| baseline | spacefaring | **2.86e-05** | 1.47e-09 – 0.584 | 612 | 0.911 | 0.0208 [1.51e-04, 0.794] |
| baseline | **radio-capable (radio + spacefaring)** | **3.01e-05** | 1.56e-09 – 0.595 | 612 | 0.911 | – |

**Radio-capable N vs classic SETI-style Drake estimates.** 
* `nathan_headline`: median **45.5** radio-capable worlds now (10th–90th 0.0228 – 5.8e+04, P(N<1) = 0.27; median nearest-neighbour distance at the median ≈ 6.17e+03 ly); top drivers: l_stone_yr (4.2 dex), stage_h_space_per_yr (3.4 dex), f_land_and_ocean (3.3 dex), f_plate_tectonics (1.8 dex)
* `baseline`: median **3.01e-05** radio-capable worlds now (10th–90th 1.56e-09 – 0.595, P(N<1) = 0.91; below 1, so no radio neighbour is expected at the median); top drivers: l_stone_yr (4.4 dex), tau_stone_tool_intelligence (4.3 dex), f_land_and_ocean (3.7 dex), stage_h_space_per_yr (3.1 dex)
* Sandberg, Drexler & Ord 2018 (arXiv:1806.02404), 'current knowledge' sketch for communicating civilisations: median N = 0.32, mean 27 million, P(N<1) = 52%. This repo's static SDO-style stone-age variant: median 28.8.
* Radio-only (radio but not yet spacefaring) is a very short stage here, because Earth went from radio to orbital spaceflight in 62 years. Almost all radio-capable worlds are therefore in the spacefaring stage.


## Method

**Target.** Worlds hosting a lineage that habitually makes stone tools (Lomekwi/Oldowan level) or anything more advanced, alive *now*. Radio detectability does not enter: it changes what we can detect, not N.

1. **Star formation history of the disk.** A thick-disk phase 13.0–8.5 Gyr ago (≈ half the disk mass), then an exponential thin disk normalised to today's SFR and disk mass. This replaces a constant R\*.
2. **Habitable bodies per star**, split by host type (v2: M, K, G, F; v1 scenarios: G/K and M):
   * η⊕ from Kepler/Archive studies.
   * Rare-Earth multipliers: plate tectonics, land + ocean, large moon, Jupiter shield, binary stability, M-dwarf flares and tidal/water loss; v2 adds a K-dwarf activity/tidal penalty and an F-star UV penalty.
   * Galactic habitable zone and a metallicity ramp in time.
   * Habitable exomoons around HZ giants.
3. **Biology as hard steps:** abiogenesis → oxygenic photosynthesis → eukaryotes → complex multicellularity → stone-tool intelligence. Each step is an exponential waiting time, and their convolution competes with the host's habitable window.
4. **Duration and recurrence.** A tool-using phase ends through intrinsic lifetime, Big-Five-class extinctions, GRBs/supernovae and self-inflicted risk. It can re-evolve afterwards (an alternating renewal process). Whole-biosphere sterilisation scales with past star formation.
5. **Civilisation stages (v2).** Inside each tool-using episode: lithic → agricultural → industrial → radio-capable → spacefaring, with advance times, collapse hazards, and regression/recurrence (see the breakdown section above).
6. **Output.** N(t) on a 20-Myr grid over 13.8 Gyr. Reported: N now (total, per host type, per stage), time-averaged N, N_ever, and species = worlds × hominin-like species per tool world.

**Nathan's headline (`nathan_headline`).**
* **Similarity weighting.** Known Earth-like planets are treated as sharing Earth's evolutionary timeline as the *typical* case (each step's expected time equals Earth's observed interval), weighted by the Earth Similarity Index (Schulze-Makuch et al. 2011, ESI¹) of the NASA Exoplanet Archive's HZ rocky planets.
* **Superhabitability boost.** A boost of 1–3× (ASSUMED) applies to the fraction of K-dwarf planets (v2; G/K in v1) meeting the Schulze-Makuch, Heller & Guinan 2020 criteria.
* **Cross-lineage tool use.** Tool use evolved independently many times on Earth (primates, corvids, octopus, sea otters, dolphins, elephants). The animals → tools step is therefore modelled as fast and repeatable: Earth's 0.597-Gyr interval is divided by 3–7 independent origins.

**Literature baseline (`baseline`).** Hard-step expected times are log-uniform over 1e-3–1e3 Gyr, then updated on Earth's dated fossil record with the observer-selection correction of Snyder-Beattie et al. 2021, which favours slow, rare steps. **The choice between these two framings explains most of the ~6-orders-of-magnitude gap between the two headline numbers.**

**Archive inputs** (pscomppars, Archive update of 1 Oct 2026, re-pulled 5 Oct 2026 with no change: 6,375 confirmed planets):
* HZ rocky planets (R < 1.8 R⊕): 23 conservative and 37 optimistic, or 26 and 41 including TRAPPIST-1 with Teff clamped to 2600 K.
* Mean ESI: 0.849 (conservative) and 0.865 (optimistic).
* Top ESI: Teegarden's Star b 0.979, TOI-700 d 0.942, Kepler-1649 c 0.940, GJ 3378 b 0.938, TOI-700 e 0.932, GJ 1002 b 0.926.
* No confirmed Archive planet meets the superhabitable criteria (K host, 1.0–1.5 R⊕, 282–302 K assumed surface temperature). The closest is Kepler-62 f (K host, 1.41 R⊕, 7 Gyr; too cold under the assumed temperature).

## Variables and sources

Every variable lives in [`params.yaml`](params.yaml). `best` is the value used in the deterministic point estimate; the default is the geometric mean for log-uniform and the midpoint for uniform.

| variable | distribution / range | best | meaning | source |
|---|---|---|---|---|
| `sfr_now` | normal 1.65 ± 0.19 | default | Msun/yr | Licquia & Newman 2015, ApJ 806, 96 — https://arxiv.org/abs/1407.1078 |
| `m_disk_now` | normal 5.17e10 ± 1.11e10 | default | Msun (disk stellar mass today) | Licquia & Newman 2015 — https://arxiv.org/abs/1407.1078 |
| `return_fraction` | uniform [0.27, 0.41] | default | - | Madau & Dickinson 2014 ARA&A (R=0.27 Salpeter, 0.41 Chabrier) — https://ned.ipac.caltech.edu/level5/March14/Madau/paper.pdf |
| `f_early_disk_mass` | uniform [0.4, 0.6] | default | fraction of disk mass formed 13.0-8.5 Gyr ago (thick-disk phase) | Snaith et al. 2015 A&A 578, A87 ('roughly half the stellar mass in first 4-5 Gyr') — https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `disk_start_gyr` | fixed 0.8 | default | Gyr after Big Bang (13.0 Gyr ago) | Snaith et al. 2015 (thick disk 9-13 Gyr ago); CONFIRMED by Xiang & Rix 2022 Nature 603, 599 (Gaia EDR3 + LAMOST ages of ~250,000 subgiants: old disk began forming ~13 Gyr ago, 0.8 Gyr after the Big Bang) — https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html ; https://www.nature.com/articles/s41586-022-04496-5 |
| `thick_end_gyr` | fixed 5.3 | default | Gyr after Big Bang (8.5 Gyr ago) | Snaith et al. 2015 (sharp SFR drop ~8-9 Gyr ago) — https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `stars_per_msun` | uniform [1.6, 2.8] | 1.64 | stars per Msun formed | Kroupa 2001 IMF: 1.64 H-burning stars/Msun (integrated here); 2.8 = 1/0.36 incl. brown dwarfs — https://adsabs.harvard.edu/pdf/2001mnras.322..231k |
| `f_gk` | uniform [0.1, 0.17] | default | fraction of stars that are G/K | RECONS 10-pc census (G 5.0% + K 11.6%); Kroupa IMF 0.6-1.1 Msun = 10%; Gaia-EDR3 10-pc census (Reyle+2021 A&A 650, A201: G 18 + Sun, K 38 of 338 stars incl. white dwarfs = 16.9%; 15.2% if the 36 unresolved probable-M companions are added) lies inside the range — http://www.recons.org/census.posted.htm ; https://arxiv.org/abs/2104.14972 |
| `f_m` | uniform [0.737, 0.81] | default | fraction of stars that are M dwarfs | Gaia-EDR3 10-pc census (Reyle+2021 A&A 650, A201: 249 M of 338 stars incl. white dwarfs and the Sun = 0.737; 0.762 with the 36 unresolved probable-M companions); RECONS 10-pc census (75%); Kroupa IMF 0.08-0.6 Msun = 81%. (2026-10-06: low 0.75 -> 0.737) — https://arxiv.org/abs/2104.14972 ; http://www.recons.org/census.posted.htm |
| `fp` | fixed 1.0 | default | - | Cassan et al. 2012 Nature 481, 167 (>=1 bound planet per star) — https://www.nature.com/articles/nature10684 |
| `ne_gk` | loguniform [0.1, 0.88] | 0.35 | rocky HZ planets per G/K star (fp folded in) | Bryson+2021 AJ 161, 36 (G-mid-K: 0.37-0.60 conservative, 0.58-0.88 optimistic); 2026 Astronomy & Computing reanalysis of 4,510 Archive transit planets: K ~0.27, F/G ~0.10 (schematic). best = K-weighted (K:G ~2:1 by number, RECONS) — https://arxiv.org/abs/2010.14812 ; https://astrobiology.com/2026/08/06/quantifying-detection-bias-and-recovering-habitable-zone-occurrence-rates-in-the-nasa-exoplanet-archive/ |
| `ne_m` | loguniform [0.16, 0.41] | 0.24 | Earth-size HZ planets per M dwarf (before the M-dwarf habitability penalties) | Dressing & Charbonneau 2015 ApJ 807, 45 (0.16 conservative, 0.24 broad HZ); 2026 Astronomy & Computing Archive reanalysis (M ~0.41, completeness-corrected; raw 4.03%) — https://arxiv.org/abs/1501.01623 ; https://astrobiology.com/2026/08/06/quantifying-detection-bias-and-recovering-habitable-zone-occurrence-rates-in-the-nasa-exoplanet-archive/ |
| `f_m_habitable` | loguniform [0.03, 1.0] | default | M-dwarf penalty for tidal locking + pre-main-sequence water loss (flares are separate, see multipliers.f_m_flares) | ASSUMED bracket informed by Shields+2016 Phys.Rep.; Luger & Barnes 2015; Lingam & Loeb 2018 JCAP; Haqq-Misra+2018 IJA; Snyder-Beattie+2021 prediction — https://arxiv.org/abs/1610.05765 |
| `th_gk_gyr` | loguniform [5.0, 20.0] | 7.0 | Gyr habitable window for complex life (G/K) | Rushby et al. 2013 Astrobiology (Earth HZ lifetime 6.29-7.79 Gyr; K dwarfs longer); Earth biosphere ends 0.8-1.5 Ga from now (Caldeira & Kasting 1992 via Snyder-Beattie+2021) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `th_m_gyr` | loguniform [10.0, 50.0] | 20.0 | Gyr habitable window (M dwarfs) | Rushby et al. 2013 (HZ lifetimes up to 54.7 Gyr) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `f_ghz` | loguniform [0.1, 1.0] | default | spatial fraction of disk stars in Galactic Habitable Zone | Lineweaver, Fenner & Gibson 2004 Science (<10% incl. time/metallicity cuts); Prantzos 2008 SSRv (whole disk by now); Gowanlock+2011 (1.2% incl. more factors) — https://arxiv.org/abs/astro-ph/0401024 |
| `t_metal_gyr` | uniform [1.0, 3.0] | default | Gyr after Big Bang when Earth-forming metallicity is reached (logistic midpoint, width 0.5 Gyr) | ASSUMED (no direct measurement of when Earth-forming metallicity was reached); informed by Lineweaver 2001 Icarus (metallicity selection; Earths avg 1.8+/-0.9 Gyr older than Earth) and Zackrisson+2016 ApJ 833, 214. Consistent with Xiang & Rix 2022 Nature (Gaia: thick-disk [Fe/H] rose from about -1 to +0.5 during the 5-6 Gyr after disk formation began 13 Gyr ago); the data do not pin down the logistic midpoint, so the bracket is kept — https://ui.adsabs.harvard.edu/abs/2001Icar..151..307L/abstract ; https://www.nature.com/articles/s41586-022-04496-5 |
| `n_giant_hz_gk` | uniform [0.065, 0.115] | default | giant planets (3-25 R_earth) in optimistic HZ per G/K star | Hill et al. 2018 ApJ 860, 6 (G 6.5+/-1.9%, K 11.5+/-3.1%) — https://arxiv.org/abs/1805.03370 |
| `n_giant_hz_m` | loguniform [0.01, 0.12] | 0.06 | giant planets in optimistic HZ per M dwarf | Hill et al. 2018 (M 6+/-6%); lower bound 0.01 ASSUMED — https://arxiv.org/abs/1805.03370 |
| `f_exomoon_host` | loguniform [0.0001, 1.0] | default | fraction of HZ giants hosting a >~0.1-0.3 M_earth (atmosphere-retaining) moon | WIDE ASSUMED prior. Low end: Canup & Ward 2006 Nature (satellite systems ~1e-4 of planet mass -> in-situ moons Moon-to-Mars size); capture routes Williams 2013 Astrobiology, Porter & Grundy 2011 ApJL (~half of captured orbits circularise); Kepler-1625b-i (Teachey & Kipping 2018) and Kepler-1708b-i (Kipping+2022) candidates contested (Heller+2023, arXiv:2312.03786). High end: Hill+2018 'one large moon per giant' case — https://www.nature.com/articles/nature04860 |
| `f_exomoon_habitable` | loguniform [0.1, 1.0] | default | fraction of such moons outside the tidal/illumination 'habitable edge' | ASSUMED range; Heller & Barnes 2013 Astrobiology 13, 18 (habitable edge; tidal heating can sterilise); Williams, Kasting & Wade 1997 Nature 385, 234 (habitable moons concept) — https://arxiv.org/abs/1209.5323 |
| `r_ster0_per_gyr` | loguniform [0.001, 0.25] | default | per Gyr, whole-biosphere sterilisation rate today (scaled by SFR(t)/SFR_now in the past) | ASSUMED; upper bound: Earth's biosphere unsterilised for ~4 Gyr; SFR scaling motivated by Piran & Jimenez 2014 PRL (GRB hazard higher in early Universe) — https://arxiv.org/abs/1409.2506 |
| `r_bigfive_per_gyr` | uniform [9.3, 10.6] | default | per Gyr, Big-Five-class mass extinctions (Earth analog) | Big Five at ~444, 372, 252, 201, 66 Ma (US NPS / geologic time scale): intervals 72,120,51,135 Myr (mean 94.5 Myr => 10.6/Gyr); 5 events in 539 Myr Phanerozoic => 9.3/Gyr; Raup & Sepkoski 1982 — https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm |
| `p_bigfive_kills_toolusers` | loguniform [0.16, 1.0] | default | probability a Big-Five-class event ends a widespread tool-using lineage | LITERATURE-INFORMED (2026-10-06; was ASSUMED loguniform 0.1-1). Low 0.16 = smallest Big-Five marine SPECIES loss (Frasnian 16-20%; Stanley 2016 PNAS 113, E6325: end-Permian ~81%, end-Cretaceous ~56%, end-Ordovician ~50%); marine GENUS losses 22-57% (Bambach et al. 2004 Paleobiology 30, 522, tabulated in McGhee et al. 2013) fall inside. High 1.0 kept because large-bodied terrestrial lineages fared worse than the marine average (all non-avian dinosaurs were lost at the K-Pg). Mapping 'a tool-using lineage is lost with the per-species/genus extinction fraction' is ASSUMED — https://www.pnas.org/doi/10.1073/pnas.1613094113 ; https://people.ucsc.edu/~mclapham/papers/McGheeEtAl2013.pdf |
| `r_self_per_gyr` | loguniform [0.1, 100.0] | 3.0 | per Gyr, self-inflicted / technological end-of-lineage hazard (mean 10 Myr to 10 Gyr), averaged over the whole stone-age-or-later phase | ASSUMED, no galactic data. Earth-only context (NOT used as galactic L): Urban 2024 Science (climate threatens 7.6% of species avg; 1.6% at ~1.3 C; ~1/3 at highest emissions); Ceballos & Ehrlich 2023 PNAS (73 tetrapod genera lost since 1500, ~35x background) vs PLOS Biol 2025 (102 genera, rare & decelerating) — https://www.science.org/doi/10.1126/science.adp4461 |
| `r_grb_per_gyr` | uniform [0.46, 1.4] | default | per Gyr today at solar radius, ozone-destroying (complex-life-lethal) long GRBs | Piran & Jimenez 2014 PRL (>90% in 5 Gyr => >=0.46/Gyr; 50% in 500 Myr => 1.4/Gyr) — https://arxiv.org/abs/1409.2506 |
| `r_sn_per_gyr` | loguniform [0.11, 3.6] | 2.5 | per Gyr, core-collapse SNe within the lethal distance (8-20 pc) | LITERATURE (2026-10-06; was fixed 1.5 = Gehrels+2003 ApJ 585, 1169, 8 pc). Rate within 20 pc from the Gaia-based census of OB stars within 1 kpc: 2.0 (+0.9/-0.3)/Gyr with an upper progenitor-mass limit, 2.5 (+1.1/-0.3)/Gyr without (Quintana, Wright & Martinez Garcia 2025 MNRAS 538, 1367). Lethal distance ~20 pc as working value (Thomas & Yelland 2023 ApJ 950, 41: ~62% global ozone loss at 20 pc), vs the older 8-10 pc (Gehrels+2003). High 3.6 = 2.5+1.1 at 20 pc; low 0.11 = (2.0-0.3) x (8/20)^3 (volume scaling, valid since 8-20 pc << the 76 pc OB scale height); best 2.5 = central 20-pc rate. Context: 60Fe in deep-sea archives records SNe at <=100 pc 1.5-3.2 and 6.5-8.7 Myr ago (Wallner+2016 Nature 532, 69) — https://arxiv.org/abs/2503.08286 ; https://iopscience.iop.org/article/10.3847/1538-4357/accf8a ; https://arxiv.org/abs/astro-ph/0211361 ; https://www.nature.com/articles/nature17196 |
| `p_lethal_astro` | loguniform [0.1, 1.0] | default | probability a GRB/SN event actually ends a tool-using lineage | ASSUMED (Gehrels+2003 note SN pathway 'may be less important than previously thought') — https://arxiv.org/abs/astro-ph/0211361 |
| `l_stone_yr` | loguniform [1.0e4, 1.0e9] | 6.6e6 | yr, intrinsic (background, non-catastrophic, non-self-inflicted) duration of the stone-age-or-later phase | Earth: >=3.3 Myr so far (Harmand+2015 Nature); Gott 1993 Copernican estimate (best = 2x elapsed); chimp stone age >=4.3 kyr (Mercader+2007 PNAS); capuchin stone tool use >=3,000 yr (oldest phase 2,993-2,422 cal BP; Falotico+2019 Nat.Ecol.Evol. 3, 1034); SDO 2018 L upper ~1e9-1e10. Range kept: genetics show lithic-stage lineages can come close to ending (Hu+2023 Science 381, 979: ~1,280 breeding individuals for ~117 kyr, ~930-813 ka) but give no rate — https://www.nature.com/articles/nature14464 ; https://www.nature.com/articles/s41559-019-0904-4 ; https://www.science.org/doi/10.1126/science.abq7487 |
| `m_recurrence` | loguniform [0.01, 1.0] | default | expected re-evolution time of tool use after loss, as a multiple of the intelligence step's tau | ASSUMED (no quantitative literature); multiple independent stone-tool lineages on Earth (Mercader+2007) suggest re-evolution can be easier than the first time — https://www.pnas.org/doi/10.1073/pnas.0607909104 |
| `f_plate_tectonics` | loguniform [0.01, 1.0] | 0.17 |  | Stern & Gerya 2024 Sci.Rep. (f_pt < 0.17); Valencia+2007 ApJL ('inevitable' on super-Earths) vs O'Neill & Lenardic 2007 GRL (stagnant lid); Stern 2016 GSF — https://www.nature.com/articles/s41598-024-54700-x |
| `f_land_and_ocean` | loguniform [0.0002, 1.0] | default |  | Stern & Gerya 2024 (f_oc 0.0002-0.01); Simpson 2017 MNRAS (most HZ worlds >90% ocean); stone tools need dry land — https://arxiv.org/abs/1607.03095 |
| `f_large_moon` | loguniform [0.022, 1.0] | default |  | Elser+2011 Icarus (massive moon for ~1/12 of terrestrial planets, range 1/45-1/4); Laskar+1993 vs Lissauer, Barnes & Chambers 2012 Icarus (moonless obliquity mostly modest -> moon may not be needed) — https://arxiv.org/abs/1105.4616 |
| `f_jupiter_shield` | loguniform [0.067, 1.0] | default |  | Wittenmyer+2020 MNRAS (cool Jupiters around 6.73% of stars); Horner & Jones 2008 IJA (shield role ambiguous -> may not be needed) — https://arxiv.org/abs/1912.01821 |
| `f_binary_ok` | uniform [0.8, 1.0] | default |  | Kraus+2016 AJ 152, 8 (close binaries <47 AU suppress planets; ~1/5 of solar-type stars disallowed); Raghavan+2010 ApJS (54% single). Upper bound 1 because Kepler eta-Earth may already include binaries — https://arxiv.org/abs/1604.05744 |
| `f_m_flares` | loguniform [0.03, 1.0] | default |  | ASSUMED bracket (flare statistics exist but no published mapping to a habitable fraction). Data: TESS flares on >40% of mid-to-late M dwarfs vs ~5% of K dwarfs (Gunther+2020 AJ 159, 60); HZ X-ray and Ly-alpha irradiance tabulated by spectral type in Cuntz & Guinan 2016 ApJ 827, 79 Table 3. Flare/XUV/proton-event ozone & atmosphere erosion reviewed in Shields+2016 Phys.Rep.; Tilley+2019 (arXiv:1711.08484); Lingam & Loeb 2018. URLs: arXiv:1901.00443 — https://arxiv.org/abs/1610.05765 |
| `f_k_activity` | loguniform [0.5, 1.0] | default |  | ASSUMED mild K-dwarf penalty (late-K flares/XUV and possible HZ tidal locking); no published survival fraction. Data: ~5% of K dwarfs show TESS flares vs >40% of mid/late M (Gunther+2020 AJ 159, 60, arXiv:1901.00443); HZ X-ray/Ly-alpha irradiance by spectral type in Cuntz & Guinan 2016 Table 3; HZ planets of stars cooler than ~K3 (4800 K) tidally lock within ~4.5 Gyr (Cuntz & Guinan 2016). Cuntz & Guinan 2016 ApJ 827, 79 (K dwarfs: favourable hosts, far lower activity than M dwarfs); Barnes 2017 Celest.Mech.Dyn.Astr. 129, 509 (HZ planets of low-mass stars can tidally lock within ~1 Gyr) — https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79 ; https://link.springer.com/article/10.1007/s10569-017-9783-7 |
| `f_f_uv` | loguniform [0.14, 1.0] | default |  | ASSUMED mapping of Sato et al. 2014 Int.J.Astrobiol. 13, 244 (F0-F8 V, 1.2-1.5 Msun: DNA damage at Earth-equivalent orbits 2.5-7.1x solar without atmospheric attenuation, much less with it): survival fraction 1/7.1 .. 1 — https://arxiv.org/abs/1312.7431 |
| `extra_worlds_per_system` | one_plus_loguniform [0.001, 0.1] | default |  (user scenarios only) | USER-PROPOSED (speculative past intelligence on Venus/Mars): low-weight bonus for >1 tool-using world per system; not literature — user research export |
| `tau_abiogenesis` | per scenario (baseline log-uniform 1e-3–1e3 Gyr; headline = Earth's interval) | Earth interval | expected waiting time; completed on Earth 3.9 Ga | Snyder-Beattie+2021 Table 1 (3.5->4.1 Gya range) — https://pmc.ncbi.nlm.nih.gov/articles/PMC7997718/ |
| `tau_oxygenic_photosynthesis_GOE` | per scenario (baseline log-uniform 1e-3–1e3 Gyr; headline = Earth's interval) | Earth interval | expected waiting time; completed on Earth 2.4 Ga | Lyons, Reinhard & Planavsky 2014 Nature (GOE ~2.4-2.3 Ga) — https://www.nature.com/articles/nature13068 |
| `tau_eukaryogenesis` | per scenario (baseline log-uniform 1e-3–1e3 Gyr; headline = Earth's interval) | Earth interval | expected waiting time; completed on Earth 1.84 Ga | Betts+2018 via Snyder-Beattie+2021 Table 1 (<1.84 Ga) — https://pmc.ncbi.nlm.nih.gov/articles/PMC7997718/ |
| `tau_complex_multicellularity` | per scenario (baseline log-uniform 1e-3–1e3 Gyr; headline = Earth's interval) | Earth interval | expected waiting time; completed on Earth 0.6 Ga | Knoll 2011 Annu.Rev.EPS (animal complex multicellularity, Ediacaran) — https://www.annualreviews.org/content/journals/10.1146/annurev.earth.031208.100209 |
| `tau_stone_tool_intelligence` | per scenario (baseline log-uniform 1e-3–1e3 Gyr; headline = Earth's interval) | Earth interval | expected waiting time; completed on Earth 0.0033 Ga | Harmand+2015 Nature (Lomekwi 3, 3.3 Ma) — https://www.nature.com/articles/nature14464 |
| `f_star_M` | uniform [0.737, 0.811] | midpoint | fraction of stars formed that are M dwarfs (v2 multi-spectral) | Gaia-EDR3 10-pc census 249/338 = 0.737 (Reyle+2021 A&A 650, A201 Table 3; denominator = A 4 + F 8 + G 18 + Sun + K 38 + M 249 + white dwarfs 20; 0.762 if the 36 unresolved probable-M companions are counted); RECONS 10-pc census 283/378 = 0.749; Kroupa 2001 IMF number fraction 0.08-0.6 Msun = 0.811 (integrated here). (2026-10-06: low 0.749 -> 0.737) — https://arxiv.org/abs/2104.14972 ; http://www.recons.org/census.posted.htm |
| `ne_M` | loguniform [0.16, 0.41] | 0.24 | Earth-size HZ planets per M dwarf (v2 multi-spectral) | Dressing & Charbonneau 2015 ApJ 807, 45 (0.16 conservative, 0.24 broad HZ); 2026 Astronomy & Computing Archive reanalysis (M ~0.41) — https://arxiv.org/abs/1501.01623 |
| `th_M_gyr` | loguniform [10.0, 50.0] | 20.0 | Gyr habitable window (v2 multi-spectral) | Rushby et al. 2013 Astrobiology 13, 833 (HZ lifetimes up to 54.7 Gyr) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `n_giant_hz_M` | loguniform [0.01, 0.12] | 0.06 | HZ giants per star (exomoon hosts) (v2 multi-spectral) | Hill et al. 2018 ApJ 860, 67 Table: M 6.0+/-6.0%; lower bound 0.01 ASSUMED — https://arxiv.org/abs/1805.03370 |
| `f_star_K` | uniform [0.077, 0.116] | midpoint | fraction of stars formed that are K dwarfs (v2 multi-spectral) | Kroupa 2001 IMF 0.6-0.9 Msun = 0.077 (integrated here); RECONS 44/378 = 0.116; Gaia-EDR3 10-pc census 38/338 = 0.112 (Reyle+2021) lies inside — http://www.recons.org/census.posted.htm ; https://arxiv.org/abs/2104.14972 |
| `ne_K` | loguniform [0.27, 0.88] | 0.49 | rocky HZ planets per K dwarf (v2 multi-spectral) | 2026 Astronomy & Computing Archive reanalysis K ~0.27 (low); Bryson+2021 AJ 161, 36 G-mid-K 0.37-0.60 conservative / 0.58-0.88 optimistic (high) — https://arxiv.org/abs/2010.14812 ; https://astrobiology.com/2026/08/06/quantifying-detection-bias-and-recovering-habitable-zone-occurrence-rates-in-the-nasa-exoplanet-archive/ |
| `th_K_gyr` | loguniform [16.0, 41.4] | 21.9 | Gyr habitable window (v2 multi-spectral) | LITERATURE (2026-10-06; was ASSUMED loguniform 8-30, best 15). Continuously-habitable-zone durations t_ev from Cuntz & Guinan 2016 ApJ 827, 79 Table 2: K0 16.0 (conservative HZ) / 24.8 (general HZ), K2 21.9 / 32.0, K5 30.4 / 41.4, K8 >50 Gyr. Low = K0 conservative, high = K5 general (K8 >50 not used, conservative), best = K2 conservative. Same mapping as the G class, whose 5-10 Gyr range matches the G2 values 4.8 / 9.9 Gyr in the same table — https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79 |
| `n_giant_hz_K` | uniform [0.084, 0.146] | midpoint | HZ giants per star (v2 multi-spectral) | Hill et al. 2018: K 11.5+/-3.1% (+/-1 sigma) — https://arxiv.org/abs/1805.03370 |
| `f_star_G` | uniform [0.026, 0.056] | midpoint | fraction of stars formed that are G dwarfs (v2 multi-spectral) | Kroupa 2001 IMF 0.9-1.1 Msun = 0.026 (integrated here); RECONS 19/378 = 0.050; Gaia-EDR3 10-pc census (18 + Sun)/338 = 0.056 (Reyle+2021 A&A 650, A201). (2026-10-06: high 0.050 -> 0.056) — http://www.recons.org/census.posted.htm ; https://arxiv.org/abs/2104.14972 |
| `ne_G` | loguniform [0.1, 0.88] | 0.3 | rocky HZ planets per G dwarf (v2 multi-spectral) | 2026 Astronomy & Computing Archive reanalysis F/G ~0.10 (low); Bryson+2021 G-mid-K up to 0.88 optimistic (high) — https://arxiv.org/abs/2010.14812 |
| `th_G_gyr` | loguniform [5.0, 10.0] | 6.5 | Gyr habitable window (v2 multi-spectral) | Rushby+2013 (Earth HZ lifetime 6.29-7.79 Gyr); Earth biosphere ends 0.8-1.5 Ga from now (Caldeira & Kasting 1992 via Snyder-Beattie+2021) — https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `n_giant_hz_G` | uniform [0.046, 0.084] | midpoint | HZ giants per star (v2 multi-spectral) | Hill et al. 2018: G 6.5+/-1.9% (+/-1 sigma) — https://arxiv.org/abs/1805.03370 |
| `f_star_F` | uniform [0.0185, 0.0285] | midpoint | fraction of stars formed that are F dwarfs (v2 multi-spectral) | RECONS 7/378 = 0.0185 (present day; some F stars have already died); Kroupa 2001 IMF 1.1-1.5 Msun = 0.0285 (integrated here); Gaia-EDR3 10-pc census 8/338 = 0.024 (Reyle+2021) lies inside — http://www.recons.org/census.posted.htm ; https://arxiv.org/abs/2104.14972 |
| `ne_F` | loguniform [0.039, 0.6] | 0.1 | rocky HZ planets per F dwarf (v2 multi-spectral) | 2026 Archive reanalysis F/G ~0.10 (best); Bryson+2021 sample extends only to 6300 K (upper 0.60 = its conservative upper bound). Low (2026-10-06: 0.03 ASSUMED -> 0.039 DERIVED) = G-class low 0.10 x the Kepler F/G small-planet occurrence ratio 0.26/0.67 = 0.39 (1-2.83 R_earth, P<200 d; Kunimoto & Matthews 2020 AJ 159, 248; F-star HZ rates themselves are unmeasured) — https://arxiv.org/abs/2010.14812 ; https://arxiv.org/abs/2004.05296 |
| `th_F_gyr` | loguniform [1.4, 5.0] | 2.8 | Gyr habitable window (v2 multi-spectral) | LITERATURE (2026-10-06; was ASSUMED loguniform 1.5-5.0, best 2.7). Continuously-habitable-zone durations t_ev from Cuntz & Guinan 2016 ApJ 827, 79 Table 2: F0 1.4 (conservative HZ) / 2.1 (general HZ), F2 1.8 / 2.4, F5 2.3 / 3.1, F8 2.8 / 5.0 Gyr. Low = F0 conservative, high = F8 general, best = F8 conservative (late F most numerous under the IMF). Consistent with main-sequence lifetimes 2.6-4.3 Gyr for 1.2-1.5 Msun (Sato et al. 2014 Int.J.Astrobiol. 13, 244) — https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79 ; https://arxiv.org/abs/1312.7431 |
| `n_giant_hz_F` | uniform [0.046, 0.084] | midpoint | HZ giants per star (v2 multi-spectral) | ASSUMED = G value (Hill et al. 2018 report no F-star rate) — https://arxiv.org/abs/1805.03370 |
| `stage_tau_agri_yr` | loguniform [3.3e5, 3.3e7] | 3.29e6 | yr, expected time lithic -> agricultural (v2 multiphase) | Earth anchor 3.3 Ma (Harmand+2015 Lomekwi 3) -> ~11.5 ka (Zeder 2011 Curr.Anthropol. 52, S221) = 3.29 Myr; range = Earth/10 .. Earth x10 ASSUMED — https://www.nature.com/articles/nature14464 ; https://doi.org/10.1086/659307 |
| `stage_tau_ind_yr` | loguniform [1.1e3, 1.1e5] | 1.1e4 | yr, expected time agricultural -> industrial (v2 multiphase) | Earth anchor ~11.5 ka -> ~1760 CE (~11.2 kyr); range Earth/10 .. x10 ASSUMED — https://doi.org/10.1086/659307 ; https://www.britannica.com/event/Industrial-Revolution |
| `stage_tau_radio_yr` | loguniform [14.0, 1400.0] | 135.0 | yr, expected time industrial -> radio-capable (v2 multiphase) | Earth anchor ~1760 -> 1895 (Marconi's first radio transmissions) = ~135 yr (user: ~150 yr); range Earth/10 .. x10 ASSUMED — https://www.britannica.com/biography/Guglielmo-Marconi |
| `stage_tau_space_yr` | loguniform [6.2, 620.0] | 62.0 | yr, expected time radio -> spacefaring (orbital spaceflight) (v2 multiphase) | Earth anchor 1895 -> 1957 (Sputnik 1) = 62 yr; range Earth/10 .. x10 ASSUMED — https://www.nasa.gov/history/sputnik/ |
| `stage_h_agri_per_yr` | loguniform [1e-07, 0.001] | geometric mean | per yr, world-wide collapse hazard of the agricultural stage (v2 multiphase) | ASSUMED. Earth: farming has persisted ~11.5 kyr world-wide despite many regional collapses (Tainter 1988, The Collapse of Complex Societies); one world gives no galactic rate. Regional data do not map onto a world-wide rate: Kemp 2019 (87 civilisations 3000 BCE-600 CE: mean lifespan 336 yr, median ~250 yr) and Scheffer et al. 2023 PNAS 120, e2218834120 (hundreds of premodern states, Seshat and MOROS data: termination risk rises over the first ~200 yr, then plateaus) measure the end of polities, after which farming continued; the regional rate (~3e-3/yr) is only a loose upper context. URLs: https://www.bbc.com/future/article/20190218-the-lifespans-of-ancient-civilisations-compared ; https://www.pnas.org/doi/10.1073/pnas.2218834120 — https://doi.org/10.1086/659307 |
| `stage_h_ind_per_yr` | loguniform [1e-06, 0.01] | geometric mean | per yr, world-wide collapse hazard of the industrial stage (v2 multiphase) | ASSUMED (Earth: ~265 yr industrial so far). Natural extinction alone is < 6.9e-5/yr (Snyder-Beattie, Ord & Bonsall 2019 Sci.Rep. 9, 11054), so most of this range is anthropogenic risk, which that bound does not cover — https://www.nature.com/articles/s41598-019-47540-7 |
| `stage_h_radio_per_yr` | loguniform [1e-10, 0.01] | geometric mean | per yr, collapse hazard of the radio-capable stage (v2 multiphase) | 1/L with L log-uniform 1e2 .. 1e10 yr = Sandberg, Drexler & Ord 2018 Table 1 (lifetime of a detectable civilisation). SETI gives no duration: Breakthrough Listen non-detections limit prevalence only (<0.066% of stellar systems within 50 pc host continuous transmitters with EIRP >~1e13 W, Wlodarczyk-Sroka, Garrett & Siemion 2020 MNRAS 498, 5720; <0.45% / <0.37% of GBT L/S-band targets above 2.1e12 W, Price+2020 AJ 159, 86), orders of magnitude above the model's radio-capable fraction, so no constraint. URLs: https://arxiv.org/abs/2006.09756 ; https://iopscience.iop.org/article/10.3847/1538-3881/ab65f1 — https://arxiv.org/abs/1806.02404 |
| `stage_h_space_per_yr` | loguniform [1e-10, 0.01] | geometric mean | per yr, collapse hazard of the spacefaring stage (v2 multiphase) | Same as radio stage (SDO 2018 L 1e2 .. 1e10 yr); ASSUMED that orbital capability does not by itself lower the hazard — https://arxiv.org/abs/1806.02404 |
| `stage_q_regress` | uniform [0.0, 1.0] | midpoint | fraction of stage collapses that regress one stage (and can recur) instead of ending the tool-using lineage (v2 multiphase) | ASSUMED (no quantitative literature). Earth's regional collapses mostly regressed rather than ended lineages (Tainter 1988) — https://www.cambridge.org/core/books/collapse-of-complex-societies/ |
| `f_superhab` | loguniform [0.03, 0.43] | 0.104 | fraction of K-dwarf habitable planets meeting the superhabitable criteria (~1.0-1.5 R_earth, ~5 K warmer); age 5-8 Gyr is handled by the time model; applied to K hosts only (headline only) | ASSUMED bracket around an Archive-derived 0.104 = P(1.0<=R<=1.5 given HZ, R<2) 25/49 x P(T_surf 282-302 K given HZ, R<2) 10/49 (superhab.py; independence assumed). (v1 used 0.073 = 0.104 x K share 0.70 of G/K.) Criteria: Schulze-Makuch, Heller & Guinan 2020 Astrobiology 20, 1394 Table 2 — https://pmc.ncbi.nlm.nih.gov/articles/PMC7757576/ |
| `superhab_boost` | loguniform [1.0, 3.0] | 1.73 | multiplier (>1) on the per-planet step-success probability for superhabitable planets (capped so probability <= 1) (headline only) | ASSUMED (user-suggested 1-3x). Schulze-Makuch+2020 and Heller & Armstrong 2014 (Astrobiology 14, 50) argue qualitatively for higher habitability/biomass but give no numeric factor — https://doi.org/10.1089/ast.2013.1088 |
| `n_tool_origins` | loguniform [3.0, 7.0] | 6.0 | effective number of independent origins of tool use among complex animals on Earth; tau_stone_tool_intelligence = 0.5967 Gyr (Earth's multicellularity->stone-tools interval) / n (headline only) | Low 3 = independent lithic-flake-producing primate lineages (hominins, Harmand+2015; bearded capuchins, Proffitt+2016 Nature 539, 85; long-tailed macaques, Proffitt+2023 Sci.Adv. 9, eade8159). Dated non-hominin stone-tool archaeology: capuchins >=3,000 yr (Falotico+2019 Nat.Ecol.Evol. 3, 1034), chimpanzees >=4.3 kyr (Mercader+2007 PNAS); behaviour rarely fossilises, so origin dates (and the count) stay uncertain. Best 6 = the user's list, each verified: primates (Goodall 1964 Nature 201, 1264), corvids (Hunt 1996 Nature 379, 249), octopus (Finn, Tregenza & Norman 2009 Curr.Biol. 19, R1069), sea otters (Hall & Schaller 1964 J.Mammal. 45, 287), dolphins (Kruetzen+2005 PNAS 102, 8939), elephants (Hart+2001 Anim.Behav. 62, 839). High 7 = classes with documented tool use (Bentley-Condit & Smith 2010 Behaviour 147, 185: three phyla, seven classes). Mapping origins -> Poisson rate (n events in ~0.6 Gyr => expected first-origin time 0.6/n Gyr) is ASSUMED — https://doi.org/10.1038/nature20112 ; https://www.science.org/doi/10.1126/sciadv.ade8159 ; https://brill.com/view/journals/beh/147/2/article-p185_3.xml |
| `w_similarity` | bootstrap mean of ESI^k over Archive HZ rocky planets | 0.849 | similarity weight (similarity/headline scenarios) | Schulze-Makuch+2011 Astrobiology 11, 1041 — https://phl.upr.edu/projects/earth-similarity-index-esi |
| `species_concurrent_per_tool_world` | loguniform [1.0, 5.0] | 2.38 | time-averaged number of coexisting hominin(-grade) species on a world during its stone-age-or-later phase | Derived from Smithsonian Human Origins 'When Lived' spans (21 species; 15 have fossils <=3.3 Ma): over 3.3 Ma-present the mean number of coexisting hominin species = 2.38 (best), max 5 (e.g. ~236 ka: H. erectus, heidelbergensis, naledi, neanderthalensis, sapiens), min 1 (today); Homo-only mean 1.75 over 2.4 Ma-present. Wood & Boyle 2016 AJPA: taxic diversity (>1 species) in every interval from 4 Ma to c.40 ka. Fossil spans are minima (Signor-Lipps) and taxonomy may be over-split. — https://humanorigins.si.edu/evidence/human-fossils/species ; https://doi.org/10.1002/ajpa.22902 |
| `species_cumulative_per_tool_world` | uniform [8.0, 16.0] | 15.0 | hominin species ever produced per tool-using world (~3.3 Myr of Earth's record) | Smithsonian list: 8 Homo species, 15 hominin species with fossils in the stone-tool era (best); Wikipedia 'List of Homo species' names 16 Homo species incl. contested ones; USER figure 9-16 'humanoid species' (consistent). Earth-only, ~3.3 Myr; worlds with longer phases could have more. — https://humanorigins.si.edu/evidence/human-fossils/species ; https://en.wikipedia.org/wiki/List_of_Homo_species |

Ranges marked **ASSUMED** have no quantitative literature value. **USER** marks Nathan's own inputs, which are kept separate from literature values.

## Source provenance

Every sourced variable in [`params.yaml`](params.yaml), classified from its `source` field: **literature-sourced** (value or range taken or derived from cited published data), **literature + ASSUMED element** (cited data, but the mapping onto the model variable or part of the range is a judgement), **user-supplied** (Nathan's own inputs) and **ASSUMED** (no usable quantitative literature value; the reason is in the source text). Counts: literature-sourced 54, literature + ASSUMED element 10, user-supplied 4, ASSUMED 17.

<details><summary>Full provenance table (click to expand)</summary>

| variable | provenance | first source / note | URL |
|---|---|---|---|
| `sfr_now` | literature-sourced | Licquia & Newman 2015, ApJ 806, 96 | https://arxiv.org/abs/1407.1078 |
| `m_disk_now` | literature-sourced | Licquia & Newman 2015 | https://arxiv.org/abs/1407.1078 |
| `return_fraction` | literature-sourced | Madau & Dickinson 2014 ARA&A (R=0.27 Salpeter, 0.41 Chabrier) | https://ned.ipac.caltech.edu/level5/March14/Madau/paper.pdf |
| `f_early_disk_mass` | literature-sourced | Snaith et al. 2015 A&A 578, A87 ('roughly half the stellar mass in first 4-5 Gyr') | https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `disk_start_gyr` | literature-sourced | Snaith et al. 2015 (thick disk 9-13 Gyr ago); CONFIRMED by Xiang & Rix 2022 Nature 603, 599 (Gaia EDR3 + LAMOST ages of ~250,000 subgiants: old disk began … | https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `thick_end_gyr` | literature-sourced | Snaith et al. 2015 (sharp SFR drop ~8-9 Gyr ago) | https://www.aanda.org/articles/aa/full_html/2015/06/aa24281-14/aa24281-14.html |
| `stars_per_msun` | literature-sourced | Kroupa 2001 IMF: 1.64 H-burning stars/Msun (integrated here); 2.8 = 1/0.36 incl. brown dwarfs | https://adsabs.harvard.edu/pdf/2001mnras.322..231k |
| `f_gk` | literature-sourced | RECONS 10-pc census (G 5.0% + K 11.6%); Kroupa IMF 0.6-1.1 Msun = 10%; Gaia-EDR3 10-pc census (Reyle+2021 A&A 650, A201: G 18 + Sun, K 38 of 338 stars incl. … | http://www.recons.org/census.posted.htm |
| `f_m` | literature-sourced | Gaia-EDR3 10-pc census (Reyle+2021 A&A 650, A201: 249 M of 338 stars incl. white dwarfs and the Sun = 0.737; 0.762 with the 36 unresolved probable-M … | https://arxiv.org/abs/2104.14972 |
| `fp` | literature-sourced | Cassan et al. 2012 Nature 481, 167 (>=1 bound planet per star) | https://www.nature.com/articles/nature10684 |
| `ne_gk` | literature-sourced | Bryson+2021 AJ 161, 36 (G-mid-K: 0.37-0.60 conservative, 0.58-0.88 optimistic); 2026 Astronomy & Computing reanalysis of 4,510 Archive transit planets: K … | https://arxiv.org/abs/2010.14812 |
| `ne_m` | literature-sourced | Dressing & Charbonneau 2015 ApJ 807, 45 (0.16 conservative, 0.24 broad HZ); 2026 Astronomy & Computing Archive reanalysis (M ~0.41, completeness-corrected; … | https://arxiv.org/abs/1501.01623 |
| `th_gk_gyr` | literature-sourced | Rushby et al. 2013 Astrobiology (Earth HZ lifetime 6.29-7.79 Gyr; K dwarfs longer); Earth biosphere ends 0.8-1.5 Ga from now (Caldeira & Kasting 1992 via … | https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `th_m_gyr` | literature-sourced | Rushby et al. 2013 (HZ lifetimes up to 54.7 Gyr) | https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `f_ghz` | literature-sourced | Lineweaver, Fenner & Gibson 2004 Science (<10% incl. time/metallicity cuts); Prantzos 2008 SSRv (whole disk by now); Gowanlock+2011 (1.2% incl. more factors) | https://arxiv.org/abs/astro-ph/0401024 |
| `n_giant_hz_gk` | literature-sourced | Hill et al. 2018 ApJ 860, 6 (G 6.5+/-1.9%, K 11.5+/-3.1%) | https://arxiv.org/abs/1805.03370 |
| `r_bigfive_per_gyr` | literature-sourced | Big Five at ~444, 372, 252, 201, 66 Ma (US NPS / geologic time scale): intervals 72,120,51,135 Myr (mean 94.5 Myr => 10.6/Gyr); 5 events in 539 Myr … | https://www.nps.gov/subjects/fossils/mass-extinctions-through-geologic-time.htm |
| `r_grb_per_gyr` | literature-sourced | Piran & Jimenez 2014 PRL (>90% in 5 Gyr => >=0.46/Gyr; 50% in 500 Myr => 1.4/Gyr) | https://arxiv.org/abs/1409.2506 |
| `r_sn_per_gyr` | literature-sourced | LITERATURE (2026-10-06; was fixed 1.5 = Gehrels+2003 ApJ 585, 1169, 8 pc). Rate within 20 pc from the Gaia-based census of OB stars within 1 kpc: 2.0 … | https://arxiv.org/abs/2503.08286 |
| `l_stone_yr` | literature-sourced | Earth: >=3.3 Myr so far (Harmand+2015 Nature); Gott 1993 Copernican estimate (best = 2x elapsed); chimp stone age >=4.3 kyr (Mercader+2007 PNAS); capuchin … | https://www.nature.com/articles/nature14464 |
| `multipliers.f_plate_tectonics` | literature-sourced | Stern & Gerya 2024 Sci.Rep. (f_pt < 0.17); Valencia+2007 ApJL ('inevitable' on super-Earths) vs O'Neill & Lenardic 2007 GRL (stagnant lid); Stern 2016 GSF | https://www.nature.com/articles/s41598-024-54700-x |
| `multipliers.f_land_and_ocean` | literature-sourced | Stern & Gerya 2024 (f_oc 0.0002-0.01); Simpson 2017 MNRAS (most HZ worlds >90% ocean); stone tools need dry land | https://arxiv.org/abs/1607.03095 |
| `multipliers.f_large_moon` | literature-sourced | Elser+2011 Icarus (massive moon for ~1/12 of terrestrial planets, range 1/45-1/4); Laskar+1993 vs Lissauer, Barnes & Chambers 2012 Icarus (moonless … | https://arxiv.org/abs/1105.4616 |
| `multipliers.f_jupiter_shield` | literature-sourced | Wittenmyer+2020 MNRAS (cool Jupiters around 6.73% of stars); Horner & Jones 2008 IJA (shield role ambiguous -> may not be needed) | https://arxiv.org/abs/1912.01821 |
| `multipliers.f_binary_ok` | literature-sourced | Kraus+2016 AJ 152, 8 (close binaries <47 AU suppress planets; ~1/5 of solar-type stars disallowed); Raghavan+2010 ApJS (54% single). Upper bound 1 because … | https://arxiv.org/abs/1604.05744 |
| `star_classes.M.f_star` | literature-sourced | Gaia-EDR3 10-pc census 249/338 = 0.737 (Reyle+2021 A&A 650, A201 Table 3; denominator = A 4 + F 8 + G 18 + Sun + K 38 + M 249 + white dwarfs 20; 0.762 if … | https://arxiv.org/abs/2104.14972 |
| `star_classes.M.ne` | literature-sourced | Dressing & Charbonneau 2015 ApJ 807, 45 (0.16 conservative, 0.24 broad HZ); 2026 Astronomy & Computing Archive reanalysis (M ~0.41) | https://arxiv.org/abs/1501.01623 |
| `star_classes.M.th_gyr` | literature-sourced | Rushby et al. 2013 Astrobiology 13, 833 (HZ lifetimes up to 54.7 Gyr) | https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `star_classes.K.f_star` | literature-sourced | Kroupa 2001 IMF 0.6-0.9 Msun = 0.077 (integrated here); RECONS 44/378 = 0.116; Gaia-EDR3 10-pc census 38/338 = 0.112 (Reyle+2021) lies inside | http://www.recons.org/census.posted.htm |
| `star_classes.K.ne` | literature-sourced | 2026 Astronomy & Computing Archive reanalysis K ~0.27 (low); Bryson+2021 AJ 161, 36 G-mid-K 0.37-0.60 conservative / 0.58-0.88 optimistic (high) | https://arxiv.org/abs/2010.14812 |
| `star_classes.K.th_gyr` | literature-sourced | LITERATURE (2026-10-06; was ASSUMED loguniform 8-30, best 15). Continuously-habitable-zone durations t_ev from Cuntz & Guinan 2016 ApJ 827, 79 Table 2: K0 … | https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79 |
| `star_classes.K.n_giant_hz` | literature-sourced | Hill et al. 2018: K 11.5+/-3.1% (+/-1 sigma) | https://arxiv.org/abs/1805.03370 |
| `star_classes.G.f_star` | literature-sourced | Kroupa 2001 IMF 0.9-1.1 Msun = 0.026 (integrated here); RECONS 19/378 = 0.050; Gaia-EDR3 10-pc census (18 + Sun)/338 = 0.056 (Reyle+2021 A&A 650, A201). … | http://www.recons.org/census.posted.htm |
| `star_classes.G.ne` | literature-sourced | 2026 Astronomy & Computing Archive reanalysis F/G ~0.10 (low); Bryson+2021 G-mid-K up to 0.88 optimistic (high) | https://arxiv.org/abs/2010.14812 |
| `star_classes.G.th_gyr` | literature-sourced | Rushby+2013 (Earth HZ lifetime 6.29-7.79 Gyr); Earth biosphere ends 0.8-1.5 Ga from now (Caldeira & Kasting 1992 via Snyder-Beattie+2021) | https://research-repository.st-andrews.ac.uk/handle/10023/5071 |
| `star_classes.G.n_giant_hz` | literature-sourced | Hill et al. 2018: G 6.5+/-1.9% (+/-1 sigma) | https://arxiv.org/abs/1805.03370 |
| `star_classes.F.f_star` | literature-sourced | RECONS 7/378 = 0.0185 (present day; some F stars have already died); Kroupa 2001 IMF 1.1-1.5 Msun = 0.0285 (integrated here); Gaia-EDR3 10-pc census 8/338 = … | http://www.recons.org/census.posted.htm |
| `star_classes.F.ne` | literature-sourced | 2026 Archive reanalysis F/G ~0.10 (best); Bryson+2021 sample extends only to 6300 K (upper 0.60 = its conservative upper bound). Low (2026-10-06: 0.03 … | https://arxiv.org/abs/2010.14812 |
| `star_classes.F.th_gyr` | literature-sourced | LITERATURE (2026-10-06; was ASSUMED loguniform 1.5-5.0, best 2.7). Continuously-habitable-zone durations t_ev from Cuntz & Guinan 2016 ApJ 827, 79 Table 2: … | https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79 |
| `multiphase.stage_h_radio_per_yr` | literature-sourced | 1/L with L log-uniform 1e2 .. 1e10 yr = Sandberg, Drexler & Ord 2018 Table 1 (lifetime of a detectable civilisation). SETI gives no duration: Breakthrough … | https://arxiv.org/abs/1806.02404 |
| `hard_steps.abiogenesis` | literature-sourced | Snyder-Beattie+2021 Table 1 (3.5->4.1 Gya range) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7997718/ |
| `hard_steps.oxygenic_photosynthesis_GOE` | literature-sourced | Lyons, Reinhard & Planavsky 2014 Nature (GOE ~2.4-2.3 Ga) | https://www.nature.com/articles/nature13068 |
| `hard_steps.eukaryogenesis` | literature-sourced | Betts+2018 via Snyder-Beattie+2021 Table 1 (<1.84 Ga) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7997718/ |
| `hard_steps.complex_multicellularity` | literature-sourced | Knoll 2011 Annu.Rev.EPS (animal complex multicellularity, Ediacaran) | https://www.annualreviews.org/content/journals/10.1146/annurev.earth.031208.100209 |
| `hard_steps.stone_tool_intelligence` | literature-sourced | Harmand+2015 Nature (Lomekwi 3, 3.3 Ma) | https://www.nature.com/articles/nature14464 |
| `species.species_concurrent_per_tool_world` | literature-sourced | Derived from Smithsonian Human Origins 'When Lived' spans (21 species; 15 have fossils <=3.3 Ma): over 3.3 Ma-present the mean number of coexisting hominin … | https://humanorigins.si.edu/evidence/human-fossils/species |
| `species.species_cumulative_per_tool_world` | literature-sourced | Smithsonian list: 8 Homo species, 15 hominin species with fossils in the stone-tool era (best); Wikipedia 'List of Homo species' names 16 Homo species incl. … | https://humanorigins.si.edu/evidence/human-fossils/species |
| `species.context_total_named_species` | literature-sourced | VERIFIED: Catalogue of Life estimates ~2.3M extant species recognised by taxonomists; COL Base Release 2026-07-14 lists 2,258,977 accepted species (incl. … | https://www.checklistbank.org/dataset/278910 |
| `classic_static.R_star` | literature-sourced | SDO 2018 Table 1 | https://arxiv.org/abs/1806.02404 |
| `classic_static.fp` | literature-sourced | SDO 2018 Table 1 | https://arxiv.org/abs/1806.02404 |
| `classic_static.ne` | literature-sourced | SDO 2018 Table 1 | https://arxiv.org/abs/1806.02404 |
| `classic_static.log10_lambdaVt` | literature-sourced | SDO 2018: fl = 1-exp(-lambda V t), log-normal, sigma = 50 decades, median 1 | https://arxiv.org/abs/1806.02404 |
| `classic_static.fi` | literature-sourced | SDO 2018 Table 1 | https://arxiv.org/abs/1806.02404 |
| `classic_static.L_stone` | literature-sourced | same as l_stone_yr above | https://www.nature.com/articles/nature14464 |
| `n_giant_hz_m` | literature + ASSUMED element | Hill et al. 2018 (M 6+/-6%); lower bound 0.01 ASSUMED | https://arxiv.org/abs/1805.03370 |
| `f_exomoon_host` | literature + ASSUMED element | WIDE ASSUMED prior. Low end: Canup & Ward 2006 Nature (satellite systems ~1e-4 of planet mass -> in-situ moons Moon-to-Mars size); capture routes Williams … | https://www.nature.com/articles/nature04860 |
| `p_bigfive_kills_toolusers` | literature + ASSUMED element | LITERATURE-INFORMED (2026-10-06; was ASSUMED loguniform 0.1-1). Low 0.16 = smallest Big-Five marine SPECIES loss (Frasnian 16-20%; Stanley 2016 PNAS 113, … | https://www.pnas.org/doi/10.1073/pnas.1613094113 |
| `star_classes.M.n_giant_hz` | literature + ASSUMED element | Hill et al. 2018 ApJ 860, 67 Table: M 6.0+/-6.0%; lower bound 0.01 ASSUMED | https://arxiv.org/abs/1805.03370 |
| `multiphase.stage_tau_agri_yr` | literature + ASSUMED element | Earth anchor 3.3 Ma (Harmand+2015 Lomekwi 3) -> ~11.5 ka (Zeder 2011 Curr.Anthropol. 52, S221) = 3.29 Myr; range = Earth/10 .. Earth x10 ASSUMED | https://www.nature.com/articles/nature14464 |
| `multiphase.stage_tau_ind_yr` | literature + ASSUMED element | Earth anchor ~11.5 ka -> ~1760 CE (~11.2 kyr); range Earth/10 .. x10 ASSUMED | https://doi.org/10.1086/659307 |
| `multiphase.stage_tau_radio_yr` | literature + ASSUMED element | Earth anchor ~1760 -> 1895 (Marconi's first radio transmissions) = ~135 yr (user: ~150 yr); range Earth/10 .. x10 ASSUMED | https://www.britannica.com/biography/Guglielmo-Marconi |
| `multiphase.stage_tau_space_yr` | literature + ASSUMED element | Earth anchor 1895 -> 1957 (Sputnik 1) = 62 yr; range Earth/10 .. x10 ASSUMED | https://www.nasa.gov/history/sputnik/ |
| `multiphase.stage_h_space_per_yr` | literature + ASSUMED element | Same as radio stage (SDO 2018 L 1e2 .. 1e10 yr); ASSUMED that orbital capability does not by itself lower the hazard | https://arxiv.org/abs/1806.02404 |
| `scenarios.nathan_headline.n_tool_origins` | literature + ASSUMED element | Low 3 = independent lithic-flake-producing primate lineages (hominins, Harmand+2015; bearded capuchins, Proffitt+2016 Nature 539, 85; long-tailed macaques, … | https://doi.org/10.1038/nature20112 |
| `multipliers.extra_worlds_per_system` | user-supplied | USER-PROPOSED (speculative past intelligence on Venus/Mars): low-weight bonus for >1 tool-using world per system; not literature | user research export |
| `scenarios.user_inputs.l_stone_yr` | user-supplied | USER-PROPOSED 50-200 kyr extinction window (CONFLICTS with Big-Five spacing of ~50-135 Myr; kept as the user's scenario) |  |
| `scenarios.user_inputs.th_gk_gyr` | user-supplied | USER: Sun ~4 Gyr remaining (+~4.4 Gyr elapsed) |  |
| `geometry.disk_volume_ly3` | user-supplied | USER-SUPPLIED ~7.9e+12 ly^3 (cylinder r = 50000 ly, thickness 1000 ly); used only for spacing |  |
| `f_m_habitable` | ASSUMED | ASSUMED bracket informed by Shields+2016 Phys.Rep.; Luger & Barnes 2015; Lingam & Loeb 2018 JCAP; Haqq-Misra+2018 IJA; Snyder-Beattie+2021 prediction | https://arxiv.org/abs/1610.05765 |
| `t_metal_gyr` | ASSUMED | ASSUMED (no direct measurement of when Earth-forming metallicity was reached); informed by Lineweaver 2001 Icarus (metallicity selection; Earths avg … | https://ui.adsabs.harvard.edu/abs/2001Icar..151..307L/abstract |
| `f_exomoon_habitable` | ASSUMED | ASSUMED range; Heller & Barnes 2013 Astrobiology 13, 18 (habitable edge; tidal heating can sterilise); Williams, Kasting & Wade 1997 Nature 385, 234 … | https://arxiv.org/abs/1209.5323 |
| `r_ster0_per_gyr` | ASSUMED | ASSUMED; upper bound: Earth's biosphere unsterilised for ~4 Gyr; SFR scaling motivated by Piran & Jimenez 2014 PRL (GRB hazard higher in early Universe) | https://arxiv.org/abs/1409.2506 |
| `r_self_per_gyr` | ASSUMED | ASSUMED, no galactic data. Earth-only context (NOT used as galactic L): Urban 2024 Science (climate threatens 7.6% of species avg; 1.6% at ~1.3 C; ~1/3 at … | https://www.science.org/doi/10.1126/science.adp4461 |
| `p_lethal_astro` | ASSUMED | ASSUMED (Gehrels+2003 note SN pathway 'may be less important than previously thought') | https://arxiv.org/abs/astro-ph/0211361 |
| `m_recurrence` | ASSUMED | ASSUMED (no quantitative literature); multiple independent stone-tool lineages on Earth (Mercader+2007) suggest re-evolution can be easier than the first time | https://www.pnas.org/doi/10.1073/pnas.0607909104 |
| `multipliers.f_m_flares` | ASSUMED | ASSUMED bracket (flare statistics exist but no published mapping to a habitable fraction). Data: TESS flares on >40% of mid-to-late M dwarfs vs ~5% of K … | https://arxiv.org/abs/1610.05765 |
| `multipliers.f_k_activity` | ASSUMED | ASSUMED mild K-dwarf penalty (late-K flares/XUV and possible HZ tidal locking); no published survival fraction. Data: ~5% of K dwarfs show TESS flares vs … | https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79 |
| `multipliers.f_f_uv` | ASSUMED | ASSUMED mapping of Sato et al. 2014 Int.J.Astrobiol. 13, 244 (F0-F8 V, 1.2-1.5 Msun: DNA damage at Earth-equivalent orbits 2.5-7.1x solar without … | https://arxiv.org/abs/1312.7431 |
| `star_classes.F.n_giant_hz` | ASSUMED | ASSUMED = G value (Hill et al. 2018 report no F-star rate) | https://arxiv.org/abs/1805.03370 |
| `multiphase.stage_h_agri_per_yr` | ASSUMED | ASSUMED. Earth: farming has persisted ~11.5 kyr world-wide despite many regional collapses (Tainter 1988, The Collapse of Complex Societies); one world … | https://doi.org/10.1086/659307 |
| `multiphase.stage_h_ind_per_yr` | ASSUMED | ASSUMED (Earth: ~265 yr industrial so far). Natural extinction alone is < 6.9e-5/yr (Snyder-Beattie, Ord & Bonsall 2019 Sci.Rep. 9, 11054), so most of this … | https://www.nature.com/articles/s41598-019-47540-7 |
| `multiphase.stage_q_regress` | ASSUMED | ASSUMED (no quantitative literature). Earth's regional collapses mostly regressed rather than ended lineages (Tainter 1988) | https://www.cambridge.org/core/books/collapse-of-complex-societies/ |
| `scenarios.nathan_headline.f_superhab` | ASSUMED | ASSUMED bracket around an Archive-derived 0.104 = P(1.0<=R<=1.5 given HZ, R<2) 25/49 x P(T_surf 282-302 K given HZ, R<2) 10/49 (superhab.py; independence … | https://pmc.ncbi.nlm.nih.gov/articles/PMC7757576/ |
| `scenarios.nathan_headline.superhab_boost` | ASSUMED | ASSUMED (user-suggested 1-3x). Schulze-Makuch+2020 and Heller & Armstrong 2014 (Astrobiology 14, 50) argue qualitatively for higher habitability/biomass but … | https://doi.org/10.1089/ast.2013.1088 |
| `classic_static.f_stone` | ASSUMED | ASSUMED (replaces fc): fraction of intelligent lineages reaching habitual stone-tool use | https://www.pnas.org/doi/10.1073/pnas.0607909104 |

</details>


## Results: all scenarios

| scenario | samples | median worlds now | 10th–90th pct | mean | P(N<1) | median species now | median worlds ever | median NN distance (ly) |
|---|---|---|---|---|---|---|---|---|
| baseline (literature) [v2] | 200000 | 0.00204 | 4.33e-07 – 7.99 | 1.73e+03 | 0.832 | 0.00446 | 1.18 | 9.22e+05 (N<1) |
| baseline_no_exomoons [v2] | 200000 | 0.00161 | 3.34e-07 – 6.54 | 1.46e+03 | 0.840 | 0.0035 | 0.92 | 1.04e+06 (N<1) |
| snyder_beattie_priors | 200000 | 5.45e-21 | 3.53e-30 – 1.04e-11 | 0.64 | 0.999 | 1.28e-20 | 4.71e-18 | 5.64e+14 (N<1) |
| user_inputs | 500000 | 9.90e-05 | 3.92e-08 – 0.25 | 34.2 | 0.934 | 2.20e-04 | 0.873 | 4.18e+06 (N<1) |
| user_fast_intelligence | 200000 | 569 | 0.735 – 2.06e+05 | 5.99e+05 | 0.110 | 1.28e+03 | 965 | 1.74e+03 |
| similarity_weighted | 200000 | 888 | 2.67 – 2.05e+05 | 4.63e+05 | 0.067 | 1.98e+03 | 4.39e+04 | 1.4e+03 |
| similarity_weighted_no_rare_earth | 200000 | 1.89e+07 | 1.75e+05 – 5.34e+08 | 2.09e+08 | 0.000 | 4.17e+07 | 7.86e+08 | 41.1 |
| earth_random_draw | 200000 | 156 | 0.224 – 5.83e+04 | 2.29e+05 | 0.159 | 348 | 1.2e+04 | 3.34e+03 |
| **nathan_headline** (headline) [v2] | 200000 | 2.79e+03 | 13.8 – 4.36e+05 | 7.27e+05 | 0.027 | 6.2e+03 | 5.66e+04 | 776 |
| nathan_headline_no_superhab [v2] | 200000 | 2.61e+03 | 13 – 4.09e+05 | 6.80e+05 | 0.028 | 5.82e+03 | 5.37e+04 | 794 |
| nathan_headline_no_tooluse [v2] | 200000 | 719 | 3.04 – 1.40e+05 | 3.21e+05 | 0.061 | 1.61e+03 | 5.29e+04 | 1.55e+03 |
| classic_static_SDO_style | 1000000 | 28.8 | 3.14e-60 – 1.49e+06 | 8.05e+06 | 0.465 | 61.8 | – | 7.75e+03 |

Effect of the headline's new factors (paired draws): without superhabitability the median is 2.61e+03 (headline ×1.07); without cross-lineage tool use it is 719 (×3.89).

[v2] = re-run with the multi-spectral (M/K/G/F) + multiphase model; unmarked scenarios are the v1 model (G/K + M hosts, one phase).

Scenario definitions are in `params.yaml` under `scenarios:`. Full statistics, sensitivity tables and ESI-exponent variants are in [`results/results_summary.md`](results/results_summary.md).

## What it means (plain language)

* **If Earth's history is typical** (Nathan's headline), the Milky Way has about **2.79e+03** worlds with stone-age-or-better tool users right now, and the typical distance to the nearest one is about **776 light-years**. The range is very wide (13.8 to 4.36e+05), but under these assumptions it is unlikely we are alone (P(N<1) ≈ 3%).
* **If Earth's history is treated as a lucky draw** that we see only because we exist (the literature baseline), the median falls to **0.00204**, and we are probably the only such world right now (P(N<1) ≈ 83%).
* **The data cannot yet decide between those two views.** The biggest swings come from how often planets have both land and ocean, how long a stone-age-or-later phase lasts, plate tectonics, and the hard-step timescales. Star counts and η⊕ matter much less (η⊕ for K stars swings the headline by less than one order of magnitude (it is not among the top 15 drivers)).
* **What Nathan's two new factors do.** Superhabitable worlds change the answer only slightly (×1.07). Treating tool use as fast and repeatable matters more (×3.9). This is probably mostly through faster re-emergence after a collapse, because the first arrival moves by only ~0.5 of ~4.4 Gyr.
* **Stone-age worlds are effectively invisible** at interstellar distances, so a large N is consistent with the silence we observe.
* **Most of these worlds would still be in the stone age.** In the stage breakdown, most tool-using time is spent in the lithic stage, because Earth took 3.3 Myr to get from stone tools to farming. Radio-capable worlds number about **45.5** in the headline (P(N<1) ≈ 27%) and **3.01e-05** in the literature baseline.
* **K dwarfs dominate.** Orange K stars supply most of N in both framings (65% headline, 58% baseline). They are ~1.4–4.5× more common than G stars, have a higher η⊕ range and long habitable windows. M dwarfs are ~6–10× more numerous than K dwarfs but carry the flare and tidal-locking/water-loss penalties. The superhabitability boost (K only) adds just a few percentage points. F stars contribute ~0.1%: they are rare (~2–3% of stars), their continuously-habitable-zone windows (1.4–5 Gyr, Cuntz & Guinan 2016) are mostly shorter than the ~4-Gyr Earth-like path to tool use, and they carry a UV penalty.

## Caveats

* **Prior-dominated.** Defensible priors move the median by more than 20 orders of magnitude (`snyder_beattie_priors` 5.5e-21 vs the headline). Read medians as summaries of the stated uncertainty, not measurements.
* **The headline assumes Earth's timeline is typical** and skips the observer-selection correction. ESI measures only bulk size, density, escape velocity and temperature; the temperature is assumed from insolation (Earth-like albedo and greenhouse). It says nothing about biology.
* **Superhabitability inputs.**
  * The 1–3× boost and the qualifying fraction are ASSUMED; neither source paper gives a number.
  * Schulze-Makuch et al. 2020 list 24 candidates, of which only 23 names were legible in the available figure. Most are unconfirmed KOIs.
* **Tool-use inputs.** Mapping "number of independent tool-use origins" onto a rate is ASSUMED. Non-hominin origins cannot be dated (behaviour rarely fossilises), and only hominins reached intentional stone flaking (capuchin and macaque flakes are unintentional by-products).
* **Several brackets are ASSUMED:** M-dwarf penalties, sterilisation rate, recurrence, self-inflicted risk, metallicity ramp, moon-host fraction. The Rare-Earth multipliers are treated as independent.
* **Species counts** assume Earth's hominin radiation is typical: on average 2.38 coexisting species, 15 over ~3.3 Myr (Smithsonian Human Origins). They depend on how finely taxonomists split species.
* **Spacing assumptions.** Nearest-neighbour distances assume random placement in a 50,000-ly-radius, 1,000-ly-thick disk (≈7.9e12 ly³, a user-supplied figure). Below 1 expected world they are formal only.
* **Multi-spectral (v2).** The K-activity and F-UV penalties, the F-star HZ-giant rate, and the mass bins behind the Kroupa fractions are ASSUMED. The F-star η⊕ low end is scaled from the Kepler F/G small-planet occurrence ratio (Kunimoto & Matthews 2020), not measured in the HZ; K and F habitable windows are continuously-habitable-zone durations from Cuntz & Guinan 2016. Per-type ESI lists are tiny (M 22, K 3, G 1, F 0 conservative HZ planets), so G and F use the pooled list. The K share comes mainly from K stars being ~1.4–4.5× more common than G stars with a higher η⊕ range, and from the M-dwarf penalties; the K-only superhabitability boost moves the K share by only ~2–3 percentage points.
* **Multiphase (v2).** Stage advance times are Earth/10 to Earth×10 around one Earth history; the agricultural and industrial collapse hazards and the regress fraction are ASSUMED; the radio and spacefaring hazards reuse Sandberg, Drexler & Ord 2018's 1e2–1e10 yr lifetime prior. Stage shares use the long-run (stationary) occupancy of the stage chain, which ignores worlds that started their tool-using phase within the last few Myr. The stage-specific hazards are added on top of the v1 self-inflicted hazard `r_self_per_gyr`, so some self-inflicted risk may be counted twice (conservative for N).
* **Sample sizes.** 2e5–1e6 per scenario. Importance-weighted scenarios have smaller effective sample sizes (see `results_summary.md`).

## SETI scan log

Feasibility pass on Breakthrough Listen public data with turboSETI (`seti/scan.py`, queue in `seti/queue.json`). Full details in [`seti/scan_log.md`](seti/scan_log.md).

* **3I/ATLAS GBT L-band (1618.65-1621.58 MHz, Iridium/GNSS region): blc23 scans 0013-0018, coarse channel 23** — hits at S/N>10: 438; ON-OFF filter-3 events: 1; at S/N>5: 828; ON-OFF filter-3 events: 1. Top plotted: 1618.785314 MHz, -2.121 Hz/s, S/N 23.38 ([plot](seti/out/blc23_guppi_61027_17226_DIAG_3I_ATLAS_00_cc23_a6a8c0a9/top_hit.png)). Injection check: a synthetic drifting tone added to the ON scans was recovered as a filter-3 event.

Every hit is almost certainly RFI or noise; **no detection is claimed**, and anything interesting would need re-observation. 3 job(s) pending for the weekly run.

## Reproduce

```bash
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
python tools/fetch_data.py          # NASA Exoplanet Archive pscomppars (~80 MB) + KOI rows
python hz_archive.py && python esi.py && python superhab.py      # derived data in data/
python drake_model.py               # all scenarios in params.yaml (n_samples each; slow at 1e6)
python drake_model.py --scenario nathan_headline --n 200000      # one scenario (run several in parallel)
python drake_model.py --analyze-only                              # stats, charts, results_summary.md
python tools/build_readme.py        # refresh this README from results (uses tools/v2_sections.py)
```
Raw samples (`results/*.npz`, several hundred MB) and `data/pscomppars.csv` are not committed. They regenerate from the commands above, and the random seed is fixed in `params.yaml`.

## Add or change a variable
* **New habitability factor:** add an entry under `multipliers:` in `params.yaml` with `dist`, `low`/`high` (or `value`), `applies_to: [gk, m]`, `source` and `url`. It is sampled automatically, applied, and included in the sensitivity tornado.
* **New evolutionary step:** add an entry under `hard_steps:` with `earth_gya` (when it happened on Earth).
* **Scenario-specific change:** add `overrides:` (replace an existing variable) or `extra_params:` (new scenario-only variable) under the scenario. Then list the scenario in `run.scenarios_to_run`.
* **New host type or stage:** host classes live under `star_classes.classes` (per-class `f_star`, `ne`, `th_gyr`, `n_giant_hz`, `penalty_params`); stages under `multiphase` (`advance_params`, `hazard_params`). A scenario uses them with `multispectral: true` / `multiphase: true`. Multipliers can target single classes with `applies_to: [K]` etc.
* **Headline:** set `run.headline_scenario`. `run.literature_baseline` is always reported alongside it.
* Supported distributions: `fixed`, `uniform`, `loguniform`, `normal` (with optional min/max), `lognormal10`, `one_plus_loguniform`.

## License and credit
Model by Nathan A. Meeks. MIT License (see `LICENSE`). Literature values belong to their cited authors. Exoplanet data: NASA Exoplanet Archive (https://exoplanetarchive.ipac.caltech.edu), operated by Caltech/IPAC under contract with NASA.
