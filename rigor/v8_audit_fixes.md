# Drake v8 audit fixes (2026-11-09)

Source FAIL: `/workspace/audit_scratch/drake_v8/REPORT.md`. Applied in the public repo as the new headline (2026-11-09). Audit re-check: PASS.

## Fixes applied

1. **f_not_flooded** (`params.yaml` v8 params): U(0.76,1) → **U(0.32,1.0)** [MODELED], anchored to Boley et al. 2025 ApJ (arXiv:2510.24854) §IV.3.2 full topography set (Mars-like 0%, Venus-like 24%, Earth-like 35%, Mercury-like 68% fully submerged → not-flooded 1.00…0.32).
2. **stage_q_regress / q_regress**: dropped the 0/9 Seshat binomial floor; feature removed from all headline/sensitivity/baseline `v8:` lists. Prior reverts to v5 **U(0,1)** [GUESS]. Hoyer+2025 kept as a qualitative note only under `v8.features.q_regress`.
3. **t_recovery_gyr**: retagged **[MODELED]** (Lyson 2019 local ecological recovery vs Kirchner & Weil 2000 global diversity lag — unlike quantities bridged).
4. **ne_M high**: 0.41 → **0.351** (Gillis 2026 §V.5 conservative HZ terrestrial 95% upper); low stays 0.05.
5. **Tyrrell sensitivity**: documented in RIGOR_SUMMARY §11 that 0.0145 (fraction of *all runs*) and 0.087 (fraction of *planets* succeeding ≥1/100) are different estimands; sensitivity-only, not headline. Also noted on `f_climate_persist` source line.

## Re-run results (n=1e5 paired vs v5; OAT n=5e4)

| | v5 | v8 (pre-fix) | **v8 (post-fix)** |
|---|---:|---:|---:|
| headline median radio-or-better | 32.2 | 224 | **73.5** |
| 10–90% | 0.016–5.09e4 | 0.193–1.03e5 | **0.073–4.08e4** |
| P(<1) | 0.288 | 0.169 | **0.222** |
| stone-age-or-greater median | 1.57e4 | 3.23e4 | **2.43e4** |
| literature baseline median | 7.75e-5 | 3.03e-4 | **1.03e-4** (ESS 6,945) |

Paired median shift vs v5: **+0.309 dex** (was +0.750).

### Sensitivity (on top of post-fix v8)
- env-paced: median **71.1** (−0.007 dex vs v8)
- Tyrrell replaces PT×moon: median **150** (+0.305 dex vs v8)
- Tyrrell replaces moon only: median **14.8** (−0.715 dex vs v8)

### One-at-a-time (changed / land)
- **land**: +0.394 dex (median 78.4) — was +0.524
- **ne_m**: −0.001 dex (median 31.2) — ~0, as before

### Checks
- `v8_none == v5`: **True** (bit-for-bit, n=5000)
- `v8_support_violations`: **[]**
- `check.py`: max rel err 5.4e-13 / 3.4e-12; support_violations []; samples_outside_bounds 0
- pairing (shared `p_sfr_now`): pass

Artifacts: `rigor/v8.json`, `rigor/v8_radio.png`, `rigor/RIGOR_SUMMARY.md` §11.
