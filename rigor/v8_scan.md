# v8 data scan: all disciplines (research only, 2026-11-09)

Scope: new data (mostly 2023-2026) that could tighten an existing parameter in params.yaml or justify a new one.
Headline = median radio-or-better civilizations alive now (v5: 32.2; baseline 7.75e-5). No params.yaml / model edits made.
Every link below was opened or confirmed by search this session. Items already in v7_candidates.md are skipped unless new data materially changes them (marked UPDATE).
Context: headline first-order Sobol shares (RIGOR_SUMMARY sec. 5): f_land_and_ocean 0.39, l_stone_yr 0.22, f_plate_tectonics 0.11, m_recurrence 0.07, f_large_moon 0.06. Data on those moves the headline most.

## Ranked shortlist

### 1. Land/ocean balance is not a knife-edge (geology/planetary science), RAISES
- Finding: Höning & Spohn 2023 (Astrobiology 23, doi:10.1089/ast.2022.0070, arXiv:2211.09473): the coupled mantle-water/continent cycle gives three stable outcomes: land planet, ocean planet, balanced Earth-like planet (Earth-like is the least likely). But land and ocean planets still have biospheres with biomass/bioproductivity reduced to 1/3-1/2 of Earth's (abstract). 2025 ApJ study of 689 rocky planets with APOGEE/GALAH host compositions ("From Underground Oceans to Continents", doi:10.3847/1538-4357/ae182b, arXiv:2510.24854): with Earth's water budget, full submergence depends on topography: Mars-like topography none fully flooded (median 98% water cover), Earth-like ~70% cover, Venus-like 24% fully submerged; higher mantle FeO stores more water in the mantle (less surface flooding).
- Parameter: f_land_and_ocean (now loguniform 2e-4..1, [MODELED], Stern & Gerya 2024 f_oc 0.0002-0.01).
- Direction: raises the low end. A land requirement for stone tools is met on land-dominated worlds too, and full flooding at fixed water is a minority outcome (0-24%).
- Proposed: split into P(not fully flooded) 0.76-1.0 [MODELED, ApJ 2025, at Earth-like water mass] x productivity factor for unbalanced worlds 0.33-0.5 [MODELED, Höning & Spohn]. Must still be combined with the spread in water mass (Simpson 2017: most HZ worlds >90% ocean), which these studies hold fixed, so the 2e-4 floor should rise but not to ~0.3 outright.
- Rough effect: largest lever in the scan. The current factor's log-median is ~0.014. Raising it toward 0.1 would raise the headline by roughly 5-10x (it scales about linearly while N>1). Needs a careful build because it conflicts with Stern & Gerya.

### 2. "Hard steps" may not be hard (geobiology), RAISES
- Finding: Mills, Macalady, Frank & Wright 2025, Science Advances 11, eads5698 (doi:10.1126/sciadv.ads5698; arXiv:2408.10293): the timing of key transitions (eukaryotes, animals, humans) can be explained by global environmental "windows of habitability" (O2, nutrients, temperature, salinity) opening in sequence, not by intrinsic improbability. The authors say they have not falsified the hard-steps model, but they give a testable alternative.
- Parameter: hard_step_tau (earth_interval) and the Bayesian Earth-timing update. Proposed scenario: "environment-paced": step waits are tied to the planet's environmental clock (the model already has o2_lag_gyr), with intrinsic taus short.
- Range: none published. This is a structural alternative, not a number [MODELED]. Run as a sensitivity scenario, not as a headline change.
- Rough effect: large in the baseline (tau params dominate Sobol there). Smaller in the headline, which already uses Earth intervals. Not estimable without a run.

### 3. Mid-to-late M-dwarf HZ planet counts, first TESS measurement (astronomy), LOWERS low end / NARROWS
- Finding: Gillis, Cloutier & Pass 2026 (AJ, arXiv:2602.23364), 8,134 mid-to-late M dwarfs (0.1-0.4 Msun), TESS sectors 1-86: optimistic HZ (0.2-2 S_earth) terrestrial (0.8-1.5 R_earth) planets 0.142 (+0.093/-0.092) per star; conservative HZ terrestrial <0.351 (95%). Super-Earths outnumber sub-Neptunes 5.5:1 (the radius valley disappears), consistent with water-rich sub-Neptunes.
- Parameter: star_classes.M.ne / ne_m (now loguniform 0.16-0.41, best 0.24).
- Proposed: low 0.16 -> 0.05 (1-sigma floor), high 0.41 kept (consistent with <0.351 conservative and 0.235 1-sigma optimistic). [MEASURED]
- Rough effect: small. M dwarfs are a minority of the headline (K-dominated), so expect a few percent down.

### 4. UPDATE to v7 #2: more JWST rocky M-dwarf planets with no thick atmosphere (astronomy), LOWERS
- New data since params.yaml was set (0 of 4 -> 95% upper 0.53): TOI-1468 b bare rock, >1 bar CO2/H2O ruled out >3 sigma (Hot Rocks II, A&A 2025, https://www.aanda.org/articles/aa/full_html/2025/06/aa53449-24/aa53449-24.html); LTT 3780 b bare rock, CO2 atmospheres ruled out to 0.01 bar (Hot Rocks IV, AJ 2025, doi:10.3847/1538-3881/adfc51). TRAPPIST-1 b/c phase curves are now in Nature Astronomy 2026 (doi:10.1038/s41550-026-02806-9). Ambiguous: LHS 1478 b tentative CO2 atmosphere, but the two visits disagree (arXiv:2410.11048); GJ 3473 b ambiguous (Hot Rocks V).
- Parameter: multipliers.f_m_flares (high 0.53).
- Proposed: 0 of 6 thick atmospheres, so binomial 95% upper = 1-0.05^(1/6) = 0.39 [MEASURED analogue; mapping to HZ planets ASSUMED as before]. If LHS 1478 b is later confirmed, 1 of 7 gives a Clopper-Pearson 95% upper of ~0.58, so the bound would not tighten.
- Rough effect: a few percent down (M share small).

### 5. Counterweight: HZ M-dwarf planets are not shown to be airless (astronomy), RAISES / keeps door open
- TRAPPIST-1 e: primary H2 atmosphere ruled out >3 sigma; CO2-rich Venus/Mars-like disfavoured at 2 sigma; N2-rich with trace CO2/CH4 allowed; bare rock also fits (ApJL 2025, doi:10.3847/2041-8213/adf62e; arXiv:2509.05414). LHS 1140 b: tentative N2-dominated atmosphere (~2.3 sigma), H2-rich ruled out; water-world interpretation (ApJL 2024, doi:10.3847/2041-8213/ad5afa; ApJL ad5204). TRAPPIST-1 d: no Earth-like atmosphere (ApJ 2025, doi:10.3847/1538-4357/adf207).
- Parameter: f_m_habitable / f_m_flares lower bounds. Direction: do not let the airless trend for hot planets (#4) push the HZ M-class factor toward zero; no range change justified yet. [MEASURED, qualitative]

### 6. Thick-disk (old) stars host fewer small planets than metallicity predicts (astronomy/galactic), LOWERS
- Finding: Zink et al. 2023 AJ 165, 262 (doi:10.3847/1538-3881/acd24c), Kepler+K2 with Gaia DR3 kinematics: super-Earth occurrence drops 50+/-8% (sub-Neptunes 56+/-7%) over the first kpc of vertical oscillation amplitude, vs only 14+/-3% (19+/-2%) expected from metallicity alone; >4 sigma excess. Counterpoint (model, not data): Boettner & Dayal 2024 A&A (aa49557-24) population synthesis predicts Earth-mass planets ~1.5x MORE common around thick-disk stars.
- Parameter: new f_thick_disk_planets (multiplies ne for stars born in the thick-disk phase, disk_start..thick_end), or folded into t_metal_gyr/f_metal_rich_galaxy.
- Proposed: non-metallicity factor = 0.50/0.86 = 0.58, 1-sigma 0.49-0.67 [MEASURED, for P<40 d super-Earths; HZ extrapolation ASSUMED]. Model alternative up to 1.5 [MODELED]. Metallicity part (14%) already in metal_rocky_ratio, so it is not double counted.
- Rough effect: f_early_disk_mass is 0.4-0.6, but old stars weigh toward long-lived/early civilizations. Expect the headline x ~0.75-0.9.

### 7. Phosphorus: the Sun is typical, not unusually P-rich, relative to rock-forming elements (astrochemistry), RAISES / NARROWS
- Finding: Esposito et al. 2026 A&A (arXiv:2608.30484), 233 Hypatia FGK stars: solar P/Mg and P/Si molar ratios are representative of the local population; only solar P/O is mildly high. [P/Si] is flat with [Fe/H] in the thin disk (slope -0.01, 95% CI -0.11..0.08). Thick-disk stars are 0.2-0.5 dex poorer in many bio-essential and rock-forming elements.
- Parameter: f_phosphorus_ok (used in the v5 metallicity/phosphorus factor; now loguniform 0.3-1 [GUESS], rationale Hinkel+2020 "Sun P-rich").
- Direction: weakens the rationale for the 0.3 floor (bulk P relative to silicate barely varies across disk metallicities). The thick-disk deficit backs #6. No new numeric bound is justified; surface P depends on core partitioning (the authors say so). Recommend: keep the range, re-cite, or lift the floor only with a planet-interior model.
- Rough effect: <1.3x up if the floor is lifted.

### 8. Plate-tectonics-favourable mantle compositions in 29% of Hypatia-based Earth-size planets (geology), RAISES best
- Finding: Skemer et al. 2025, JGR Planets (doi:10.1029/2025JE009106; WashU summary https://eeps.washu.edu/news/potential-plate-tectonics-earth-exoplanets): mantles modelled from Hypatia stellar compositions; 29% have no mineral above 50% by volume, the most favourable case for fast ductile shear-zone formation (Earth-like plate boundaries). Mobile-lid likelihood depends mainly on composition and lithospheric strength, not planet mass.
- Parameter: f_plate_tectonics (loguniform 0.01-1, best 0.17, Stern & Gerya f_pt<0.17).
- Proposed: best 0.17 -> 0.29 [MODELED]; keep 0.01-1 (the other 71% are less favourable, not excluded).
- Rough effect: f_plate_tectonics Sobol 0.11. A best-value shift alone is ~1.3-1.7x up where the best value is used; little change to the loguniform draws.

### 9. Climate persistence over 3 Gyr is partly luck (climate/Earth-system), LOWERS
- Finding: Tyrrell 2020, Commun. Earth Environ. (doi:10.1038/s43247-020-00057-8): 100,000 planets with random climate feedbacks, each run 100 times over 3 Gyr. About 8.7% (8,710) stayed habitable at least once; only 1 succeeded in all 100 runs; most successful planets did so in fewer than 10 of 100 runs. Robust across 37 sensitivity variants (overall rates vary by variant).
- Parameter: f_climate_stable (U(0.5,1) [GUESS], v4 scenarios, not in the v5 headline) or a new f_climate_persist.
- Proposed: <=0.09 [MODELED] for random-feedback planets. Caveat: overlaps with f_plate_tectonics/geology links (a carbonate-silicate thermostat is a feedback), and the model's priors are not tied to real planets. Use only as a replacement for f_climate_stable, never multiplied on top.
- Rough effect: if adopted in place of U(0.5,1), up to ~x0.1-0.2 (large); needs de-duplication first.

### 10. Most societal crises do not end in collapse; collapses regress rather than end lineages (history/sociology), RAISES q
- Finding: Hoyer et al. 2025, Social Science History 50(2) 314-346 (doi:10.1017/ssh.2025.10113), Seshat Crisis DB: 168 analysed crises from the Bronze Age to the early 1900s; median duration 22 yr (<1 to >200 yr); ~5% end in collapse; crisis severity has not declined over time. Data on GitHub: https://github.com/datasets/seshat/blob/main/CrisisConsequencesData_NavigatingPolycrisis_2023.03.csv
- Parameter: stage_q_regress (U(0,1) [GUESS]); also gives a per-crisis collapse probability for the agricultural stage hazard.
- Proposed: P(collapse | crisis) 0.05 [MEASURED, Earth regional polities]; none of the recorded collapses ended the human tool-using lineage, which supports the high end of q. A numeric q floor would still be a mapping assumption.
- Rough effect: q affects regression vs termination. Moving it toward 1 raises the stone-age+ count more than the radio count. Modest.

### 11. Expert-elicited present-day catastrophe and extinction hazard (risk studies): CONTEXT ONLY
- Finding: Karger et al. 2023, Existential Risk Persuasion Tournament (https://forecastingresearch.org/research/existential-risk-persuasion-tournament): superforecaster medians P(catastrophe, >=10% of humanity dying within 5 yr, by 2100) = 9%; P(extinction) = 1%. That is ~1.2e-3/yr catastrophe and ~1.3e-4/yr extinction over 2023-2100 (computed here).
- Parameter: stage_h_ind_per_yr (1e-6..1e-2) and stage_h_radio_per_yr (1e-10..1e-2). Both values sit inside the current ranges.
- Tag: [GUESS] (elicitation, not measurement). Per Nathan's no-new-guess rule, record it only as a cross-check; do not adopt. If used, it would cut the radio-stage lifetime (L ~ 8e3 yr), lowering the headline strongly.

### 12. Nearby-supernova rate and extinction link confirmed (astronomy/paleontology), NARROWS (confirms)
- Finding: arXiv:2503.08286 (MNRAS 2025, "A census of OB stars within 1 kpc and the star formation and core collapse supernova rates of the Milky Way"): about 2.5 core-collapse SNe within lethal range per Gyr, consistent with one or both of the Late Devonian and end-Ordovician extinctions. RAS summary: https://ras.ac.uk/news-and-press/research-highlights/violent-supernovae-triggered-least-two-earth-extinctions
- Parameter: r_sn_per_gyr (best 2.5, already matches) and p_lethal_astro (0.1-1 [GUESS]). These events caused mass extinctions, not sterilisation, so Earth's record contains SN-scale events that the biosphere survived. That argues against p_lethal near 1 for lineages with large populations, but gives no numeric bound.

### 13. Prebiotic inventory is widespread; possible second biosphere in the Solar System (origin of life / planetary): watch items, RAISES (qualitative)
- Bennu samples: 14 of 20 protein amino acids, all 5 nucleobases, abundant ammonia (Glavin et al. 2025 Nat. Astron., doi:10.1038/s41550-024-02472-9); sodium phosphates and evaporite brine minerals (McCoy et al. 2025 Nature, doi:10.1038/s41586-024-08495-6).
- Mars "Cheyava Falls / Sapphire Canyon": redox reaction fronts with vivianite and greigite next to organic carbon, a potential biosignature; abiotic origins not excluded (Hurowitz et al. 2025 Nature, doi:10.1038/s41586-025-09413-0).
- Parameters: tau_abiogenesis (fast end), lithopanspermia (v7 raising #7), extra_worlds_per_system. No range yet. If Mars is confirmed, it would be the first data point for a second abiogenesis or transfer.

## Checked and set aside
- Miao et al. 2024 Sci. Adv. (1.635 Ga multicellular eukaryotes, doi:10.1126/sciadv.adk3208): simple multicellularity. The model's step is complex (animal) multicellularity at 0.6 Ga, so there is no change.
- G/K eta-Earth: no new published value after Bryson+2021 (a 2025 Kepler reprocessing is in progress, BAAS 57(2)). The 2026 Archive reanalysis is already in params.
- Large-moon frequency: no new population rate. Nakajima+2022 (fractionally large moons unlikely above ~1.6 R_earth) is a possible size cut for super-Earths, but it is old.
- Superflares, impacts, super-eruptions, pandemics, LUCA, agriculture origins, bottlenecks: already in v7. No materially new data found.

## Top GUESS parameters still unconstrained after this scan
1. stage_h_radio_per_yr / r_self_per_gyr: technological lifetime. Only Earth (no collapse in about 100 yr of radio) and elicitation (#11). SETI does not constrain duration.
2. m_recurrence: re-evolution of tool use after loss (headline Sobol 0.07). Only qualitative evidence (multiple primate stone-tool lineages); no rate data.
3. p_ocean_to_industrial and f_ocean_fecundity: whether ocean-world lineages reach industry. Theory only (Balbi & Frank 2024 O2/fire threshold); no data.
(Close behind: f_m_habitable (tidal locking; JWST only constrains hot planets), the links-group copula strengths (all [GUESS]), and t_metal_gyr, which #6 informs but whose logistic midpoint stays unpinned.)
