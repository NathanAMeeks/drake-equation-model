# Changelog

## 2026-10-06 — Literature refresh of weakly sourced inputs, source-provenance table, first SETI scan log
Each change below is old → new, with its source. Ranges for every other input are unchanged.
- **`r_sn_per_gyr`** (core-collapse supernovae per Gyr within the lethal distance): fixed 1.5 (Gehrels et al. 2003, 8 pc) → log-uniform 0.11–3.6, best 2.5. Quintana, Wright & Martínez García 2025, MNRAS 538, 1367 (Gaia-based census of OB stars within 1 kpc) give a 20-pc rate of 2.0 (+0.9/−0.3) per Gyr with an upper progenitor-mass limit and 2.5 (+1.1/−0.3) without one (https://arxiv.org/abs/2503.08286). Thomas & Yelland 2023, ApJ 950, 41 put the lethal distance near 20 pc (https://iopscience.iop.org/article/10.3847/1538-4357/accf8a). The low end, 0.11, is the 20-pc rate scaled to 8 pc by volume.
- **`p_bigfive_kills_toolusers`**: log-uniform 0.1–1 (ASSUMED) → 0.16–1. The low end is the smallest Big-Five marine species loss (Frasnian, 16–20%; Stanley 2016, PNAS 113, E6325, https://www.pnas.org/doi/10.1073/pnas.1613094113). Genus losses of 22–57% (Bambach et al. 2004, tabulated in McGhee et al. 2013, https://people.ucsc.edu/~mclapham/papers/McGheeEtAl2013.pdf) fall inside the range. The upper end stays at 1 because large terrestrial lineages fared worse; all non-avian dinosaurs were lost.
- **K-dwarf habitable window `star_classes.K.th_gyr`**: log-uniform 8–30, best 15 (ASSUMED) → 16.0–41.4, best 21.9. These are continuously-habitable-zone durations for K0–K5 from Cuntz & Guinan 2016, ApJ 827, 79, Table 2 (https://iopscience.iop.org/article/10.3847/0004-637X/827/1/79).
- **F-star habitable window `star_classes.F.th_gyr`**: log-uniform 1.5–5.0, best 2.7 (ASSUMED) → 1.4–5.0, best 2.8, from the same table (F0–F8). It is consistent with main-sequence lifetimes of 2.6–4.3 Gyr for 1.2–1.5 M☉ (Sato et al. 2014, https://arxiv.org/abs/1312.7431).
- **F-star η⊕ low end `star_classes.F.ne`**: 0.03 (ASSUMED) → 0.039. This is the G-class low end (0.10) × the Kepler F/G small-planet occurrence ratio 0.26/0.67 from Kunimoto & Matthews 2020, AJ 159, 248 (https://arxiv.org/abs/2004.05296).
- **Star fractions from the Gaia-EDR3 10-pc census** (Reylé et al. 2021, A&A 650, A201, https://arxiv.org/abs/2104.14972):
  - `star_classes.M.f_star` low end 0.749 → 0.737;
  - `star_classes.G.f_star` high end 0.050 → 0.056;
  - v1 `f_m` low end 0.75 → 0.737.
  The K, F and `f_gk` ranges already contain the Gaia values; only the source was added.
- **Sources added, values unchanged:**
  - Xiang & Rix 2022 (Nature) for `disk_start_gyr` and `t_metal_gyr`;
  - Günther et al. 2020 (AJ 159, 60; TESS flare rates) for `f_m_flares` and `f_k_activity`;
  - Falótico et al. 2019 (capuchin stone tools ≥3,000 yr) and Hu et al. 2023 (Science; the ~930–813 ka bottleneck) for `l_stone_yr` and `n_tool_origins`;
  - Kemp 2019 and Scheffer et al. 2023 (PNAS; collapse of regional polities) for `stage_h_agri_per_yr`;
  - Breakthrough Listen prevalence limits (Price et al. 2020; Wlodarczyk-Sroka et al. 2020) for `stage_h_radio_per_yr`. These limits sit far above the model's radio-capable fraction, so they do not constrain it.
- **Still ASSUMED** (no usable quantitative data found; the reasons are in `params.yaml`):
  - star and planet inputs: `f_m_habitable`, `t_metal_gyr`, `f_exomoon_habitable`, F-star `n_giant_hz`;
  - hazards and recurrence: `r_ster0_per_gyr`, `r_self_per_gyr`, `p_lethal_astro`, `m_recurrence`;
  - stellar-activity penalties: `f_m_flares`, `f_k_activity`, `f_f_uv`;
  - civilisation stages: `stage_h_agri_per_yr`, `stage_h_ind_per_yr`, `stage_q_regress`;
  - headline and static-model extras: `f_superhab`, `superhab_boost`, `f_stone`.
  The following are partly ASSUMED:
  - `f_exomoon_host` and the M-dwarf HZ-giant low end;
  - the stage advance-time ranges;
  - the mapping in `n_tool_origins`.
- **New README section "Source provenance"** (`tools/provenance.py`), which classifies every sourced variable as literature-sourced (54), literature + ASSUMED element (10), user-supplied (4) or ASSUMED (17).
- **Re-ran all 11 scenarios** from the same seed (2e5 samples each; `user_inputs` 5e5). Old → new medians:
  - **headline `nathan_headline` 2.63e+03 → 2.79e+03**; literature **`baseline` 0.00179 → 0.00204**;
  - radio-capable worlds: headline 42.9 → 45.5, baseline 2.65e-05 → 3.01e-05;
  - `nathan_headline_no_superhab` 2.46e+03 → 2.61e+03; `nathan_headline_no_tooluse` 678 → 719; `baseline_no_exomoons` 0.00143 → 0.00161;
  - v1 scenarios moved by less than 1%: `snyder_beattie_priors` 5.51e-21 → 5.45e-21, `user_inputs` 9.93e-05 → 9.90e-05, `user_fast_intelligence` 571 → 569, `similarity_weighted` 895 → 888, `similarity_weighted_no_rare_earth` 1.90e+07 → 1.89e+07, `earth_random_draw` 157 → 156.
  - The K-dwarf share of the headline mean rose from 63% to 65%, mainly because of the longer K habitable window. Charts and `results/results_summary.md` were regenerated.
- **SETI scan log (new, `seti/`).** This is a feasibility pass on Breakthrough Listen public data: the 3I/ATLAS Green Bank cadence (L band, scans 0013–0018, compute node blc23, one ~2.9-MHz coarse channel at 1618.65–1621.58 MHz pulled from each of the six files by HTTP range requests, ≈0.9 GB).
  - turboSETI (max drift ±4 Hz/s) found 438 hits at S/N > 10 and 828 at S/N > 5.
  - turboSETI ON-OFF filtering left one filter-3 event at each threshold. Both have drift rates that disagree between the ON scans, and similar features appear in the OFF scans, so they are almost certainly RFI.
  - A synthetic drifting tone injected into the ON scans was recovered as a filter-3 event.
  - **No detection is claimed.** Details are in `seti/scan_log.md`. `seti/scan.py` and `seti/queue.json` give a reusable queue for weekly runs, with 3 jobs pending.
  - The Voyager-1 test file could not be used. The Berkeley server that hosts it was unreachable from the run machine, and the mirrored copy has only 2 time integrations.
- README rebuilt with `tools/build_readme.py`. Model by Nathan A. Meeks.

## 2026-10-05 — Data refresh: NASA Exoplanet Archive re-pulled, no change
- Re-ran `tools/fetch_data.py` on 5 Oct 2026 (`pscomppars` and the 22 Schulze-Makuch+2020 KOI rows from `cumulative`). Both files are byte-identical to the 1 Oct 2026 pull; the Archive's most recent weekly update is still 1 Oct 2026.
- Re-ran `hz_archive.py`, `esi.py` and `superhab.py`; all derived files in `data/` are unchanged. 6,375 confirmed planets; HZ rocky planets (R < 1.8 R⊕) 23 conservative / 37 optimistic (26 / 41 with Teff clamped to 2600 K); mean ESI 0.849 conservative / 0.865 optimistic; 7 K-hosted HZ planets with R < 2 R⊕, none meeting all superhabitability criteria.
- No model inputs changed, so the scenarios were not re-run and the results are unchanged: headline (`nathan_headline`) median 2.63e+03, literature `baseline` median 0.00179. A 2e5-sample reproducibility re-run of both from the same seed matched the published numbers.
- README rebuilt with `tools/build_readme.py`; the Archive inputs line now records the re-pull date. Model by Nathan A. Meeks.

## 2026-10-02 — Multi-spectral and multiphase breakdowns, suggested by a friend of Nathan's
- **Multi-spectral (v2 model):** N is broken down by host star type **M, K, G, F**. Each type has its own star fraction (RECONS 10-pc census vs Kroupa IMF), η⊕, habitable window, HZ giants for exomoons (Hill et al. 2018), activity/UV/tidal penalties (new `f_k_activity` and `f_f_uv` multipliers; M-dwarf penalties kept), and similarity weight (per-type Archive ESI lists). The superhabitability boost now applies to K hosts only (`f_superhab` rescaled to a fraction of K planets). Config: `star_classes:` in `params.yaml`; a scenario opts in with `multispectral: true`.
- **Multiphase (v2 model):** civilisations move through stages (lithic → agricultural → industrial → radio-capable → spacefaring). Each stage has an advance time anchored on Earth's history, plus a collapse hazard (radio and spacefaring use Sandberg, Drexler & Ord 2018's L prior). A share of collapses regresses one stage and can recur. Config: `multiphase:`; opt in with `multiphase: true`.
- Re-ran `nathan_headline`, `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`, `baseline` and `baseline_no_exomoons` with v2 (2e5 samples each). Headline median now 2.63e+03 (v1: 3.18e+03); literature baseline 0.00179 (v1: 0.00238). Radio-capable N (radio + spacefaring): headline median 42.9, baseline 2.65e-05. All other scenarios are unchanged v1 runs. The v1 results are kept in `results/v1_results.json`.
- New charts: `results/spectral_breakdown.png` and `results/stage_breakdown.png`. `esi.py` now writes per-host-type ESI lists and top planets. README rebuilt with `tools/build_readme.py`, using the new `tools/v2_sections.py`.

## 2026-10-02 — first public release
- Time-aware extended Drake model (`drake_model.py`): disk star-formation history, G/K vs M hosts, Rare-Earth multipliers, habitable exomoons, five evolutionary hard steps, extinction/sterilisation hazards, recurrence of tool use, N(t) over 13.8 Gyr.
- Scenarios: literature `baseline` (Snyder-Beattie-style Earth-timing update), `baseline_no_exomoons`, `snyder_beattie_priors`, `user_inputs`, `user_fast_intelligence`, `similarity_weighted` (+ `_no_rare_earth`), `earth_random_draw`, classic static Sandberg-Drexler-Ord comparison.
- **Headline: `nathan_headline`** = similarity-weighted (ESI^1, conservative HZ, Earth timeline typical) + superhabitability boost (Schulze-Makuch, Heller & Guinan 2020 criteria; 1-3x ASSUMED) + cross-lineage tool use (animals->tools step fast/repeatable, 3-7 independent origins). Sensitivity runs `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`.
- NASA Exoplanet Archive analysis (pscomppars, 1 Oct 2026): HZ rocky counts (`hz_archive.py`), Earth Similarity Index (`esi.py`), superhabitability screen (`superhab.py`).
- Species-per-tool-world factor from Smithsonian Human Origins date spans; spacing (equal-cube side, nearest-neighbour distance) for a ~7.9e12 ly^3 disk.
- Charts: per-scenario histograms and tornado plots, all-scenario comparison, ESI distribution.
