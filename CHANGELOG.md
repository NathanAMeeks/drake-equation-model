# Changelog

## 2026-10-02 — first public release
- Time-aware extended Drake model (`drake_model.py`): disk star-formation history, G/K vs M hosts, Rare-Earth multipliers, habitable exomoons, five evolutionary hard steps, extinction/sterilisation hazards, recurrence of tool use, N(t) over 13.8 Gyr.
- Scenarios: literature `baseline` (Snyder-Beattie-style Earth-timing update), `baseline_no_exomoons`, `snyder_beattie_priors`, `user_inputs`, `user_fast_intelligence`, `similarity_weighted` (+ `_no_rare_earth`), `earth_random_draw`, classic static Sandberg-Drexler-Ord comparison.
- **Headline: `nathan_headline`** = similarity-weighted (ESI^1, conservative HZ, Earth timeline typical) + superhabitability boost (Schulze-Makuch, Heller & Guinan 2020 criteria; 1-3x ASSUMED) + cross-lineage tool use (animals->tools step fast/repeatable, 3-7 independent origins). Sensitivity runs `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`.
- NASA Exoplanet Archive analysis (pscomppars, 1 Oct 2026): HZ rocky counts (`hz_archive.py`), Earth Similarity Index (`esi.py`), superhabitability screen (`superhab.py`).
- Species-per-tool-world factor from Smithsonian Human Origins date spans; spacing (equal-cube side, nearest-neighbour distance) for a ~7.9e12 ly^3 disk.
- Charts: per-scenario histograms and tornado plots, all-scenario comparison, ESI distribution.
