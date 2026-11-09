# Results — time-aware extended Drake model (stone-age-or-greater)

**Headline scenario: `nathan_headline`** (user-approved). Literature baseline for comparison: `baseline`.

Model versions: **v2** (multi-spectral M/K/G/F host classes + multiphase civilisation stages) for `baseline`, `baseline_no_exomoons`, `nathan_headline`, `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`; all other scenarios are **v1** (two host classes G/K + M, single stone-age-or-greater phase). v1 numbers for the re-run scenarios are kept in results/v1/.

N = expected number of Milky Way worlds with stone-age-or-greater tool users alive at the same time (present day, other than Earth). Percentiles are over parameter uncertainty (posterior after the Earth-timing update where enabled).

| scenario | median (50/50) | mean | 10th pct | 90th pct | P(N<1) | P(no other, Poisson) | P(1<=N<=3) | time-avg N over history | median N_ever (by now) | ESS |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 0.00179 | 1.61e+03 | 3.72e-07 | 7.04 | 0.837 | 0.809 | 0.039 | median 3.47e-04 / mean 471 | 1.13 | 13586 |
| baseline_no_exomoons | 0.00143 | 1.36e+03 | 2.98e-07 | 5.88 | 0.844 | 0.817 | 0.039 | median 2.70e-04 / mean 382 | 0.874 | 13586 |
| snyder_beattie_priors | 5.51e-21 | 0.643 | 3.60e-30 | 1.04e-11 | 0.999 | 0.999 | 0.000 | median 1.17e-21 / mean 0.227 | 4.70e-18 | 3151 |
| user_inputs | 9.93e-05 | 34.4 | 3.94e-08 | 0.251 | 0.934 | 0.916 | 0.021 | median 2.57e-05 / mean 12.3 | 0.875 | 34101 |
| user_fast_intelligence | 571 | 6.01e+05 | 0.736 | 2.06e+05 | 0.110 | 0.097 | 0.042 | median 218 / mean 3.36e+05 | 967 | 200000 |
| similarity_weighted | 895 | 4.69e+05 | 2.68 | 2.08e+05 | 0.067 | 0.058 | 0.038 | median 356 / mean 1.78e+05 | 4.39e+04 | 200000 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 2.12e+08 | 1.75e+05 | 5.41e+08 | 0.000 | 0.000 | 0.000 | median 7.50e+06 / mean 8.11e+07 | 7.87e+08 | 200000 |
| earth_random_draw | 157 | 2.32e+05 | 0.225 | 5.9e+04 | 0.159 | 0.141 | 0.057 | median 50.4 / mean 7.91e+04 | 1.2e+04 | 200000 |
| nathan_headline | 2.63e+03 | 6.92e+05 | 13.2 | 4.12e+05 | 0.027 | 0.024 | 0.023 | median 1.01e+03 / mean 2.69e+05 | 5.58e+04 | 200000 |
| nathan_headline_no_superhab | 2.46e+03 | 6.48e+05 | 12.3 | 3.87e+05 | 0.028 | 0.025 | 0.024 | median 944 / mean 2.53e+05 | 5.28e+04 | 200000 |
| nathan_headline_no_tooluse | 678 | 3.06e+05 | 2.86 | 1.32e+05 | 0.062 | 0.054 | 0.039 | median 246 / mean 1.12e+05 | 5.21e+04 | 200000 |
| classic_static_SDO_style | 28.8 | 8.05e+06 | 3.14e-60 | 1.49e+06 | 0.465 | 0.463 | 0.007 | (static) | – | – |

## Worlds vs tool-using species (species_per_tool_world)

species_now = N_now x concurrent hominin-grade species per tool world (log-uniform 1-5, best 2.38, from Smithsonian date spans); species_ever = N_ever x cumulative species per tool world (uniform 8-16, best 15). The factor multiplies species, not worlds.

| scenario | median worlds now | median species now | species 10th-90th | mean species now | median worlds ever | median species ever | best-estimate species now |
|---|---|---|---|---|---|---|---|
| baseline | 0.00179 | 0.00392 | 8.52e-07 – 15.9 | 4.11e+03 | 1.13 | 13.2 | 8.28e+03 |
| baseline_no_exomoons | 0.00143 | 0.00308 | 6.54e-07 – 13.1 | 3.6e+03 | 0.874 | 10.4 | 8.12e+03 |
| snyder_beattie_priors | 5.51e-21 | 1.29e-20 | 6.98e-30 – 2.21e-11 | 0.954 | 4.70e-18 | 5.56e-17 | 7.87e+03 |
| user_inputs | 9.93e-05 | 2.20e-04 | 8.56e-08 – 0.6 | 85.2 | 0.875 | 10.2 | 206 |
| user_fast_intelligence | 571 | 1.28e+03 | 1.58 – 4.75e+05 | 1.50e+06 | 967 | 1.14e+04 | 1.29e+05 |
| similarity_weighted | 895 | 1.99e+03 | 5.91 – 4.81e+05 | 1.14e+06 | 4.39e+04 | 5.19e+05 | 6.68e+03 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 4.20e+07 | 3.79e+05 – 1.27e+09 | 5.29e+08 | 7.87e+08 | 9.26e+09 | 1.34e+07 |
| earth_random_draw | 157 | 352 | 0.492 – 1.35e+05 | 6.09e+05 | 1.2e+04 | 1.42e+05 | 7.87e+03 |
| nathan_headline | 2.63e+03 | 5.85e+03 | 28.6 – 9.45e+05 | 1.67e+06 | 5.58e+04 | 6.56e+05 | 3.72e+04 |
| nathan_headline_no_superhab | 2.46e+03 | 5.48e+03 | 26.8 – 8.87e+05 | 1.56e+06 | 5.28e+04 | 6.20e+05 | 3.51e+04 |
| nathan_headline_no_tooluse | 678 | 1.52e+03 | 6.25 – 3.06e+05 | 7.30e+05 | 5.21e+04 | 6.12e+05 | 7.39e+03 |
| classic_static_SDO_style | 28.8 | 61.8 | 6.93e-60 – 3.40e+06 | 2.00e+07 | – | – | – |

## Similarity-weight variants — similarity_weighted

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 895 | 4.69e+05 | 2.68 – 2.08e+05 | 0.067 | 0.038 | 4.39e+04 |
| conservative_k10 | 0.243 | 254 | 1.34e+05 | 0.76 – 5.91e+04 | 0.111 | 0.052 | 1.25e+04 |
| conservative_k2 | 0.726 | 763 | 4.00e+05 | 2.29 – 1.77e+05 | 0.071 | 0.039 | 3.75e+04 |
| conservative_k3 | 0.623 | 655 | 3.43e+05 | 1.96 – 1.52e+05 | 0.076 | 0.041 | 3.22e+04 |
| conservative_k5 | 0.466 | 489 | 2.57e+05 | 1.47 – 1.13e+05 | 0.086 | 0.044 | 2.4e+04 |
| optimistic_k1 | 0.865 | 911 | 4.77e+05 | 2.73 – 2.11e+05 | 0.066 | 0.037 | 4.47e+04 |
| optimistic_k10 | 0.281 | 295 | 1.56e+05 | 0.886 – 6.87e+04 | 0.105 | 0.050 | 1.45e+04 |
| optimistic_k2 | 0.751 | 791 | 4.15e+05 | 2.37 – 1.83e+05 | 0.070 | 0.039 | 3.89e+04 |
| optimistic_k3 | 0.655 | 690 | 3.62e+05 | 2.07 – 1.60e+05 | 0.075 | 0.040 | 3.39e+04 |
| optimistic_k5 | 0.505 | 531 | 2.79e+05 | 1.6 – 1.23e+05 | 0.083 | 0.043 | 2.61e+04 |

## Similarity-weight variants — similarity_weighted_no_rare_earth

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 1.90e+07 | 2.12e+08 | 1.75e+05 – 5.41e+08 | 0.000 | 0.000 | 7.87e+08 |
| conservative_k10 | 0.243 | 5.40e+06 | 6.06e+07 | 4.96e+04 – 1.55e+08 | 0.000 | 0.000 | 2.23e+08 |
| conservative_k2 | 0.726 | 1.62e+07 | 1.81e+08 | 1.49e+05 – 4.62e+08 | 0.000 | 0.000 | 6.72e+08 |
| conservative_k3 | 0.623 | 1.39e+07 | 1.55e+08 | 1.28e+05 – 3.97e+08 | 0.000 | 0.000 | 5.77e+08 |
| conservative_k5 | 0.466 | 1.04e+07 | 1.16e+08 | 9.56e+04 – 2.97e+08 | 0.000 | 0.000 | 4.30e+08 |
| optimistic_k1 | 0.865 | 1.93e+07 | 2.15e+08 | 1.78e+05 – 5.50e+08 | 0.000 | 0.000 | 8.01e+08 |
| optimistic_k10 | 0.281 | 6.26e+06 | 7.02e+07 | 5.76e+04 – 1.79e+08 | 0.000 | 0.000 | 2.60e+08 |
| optimistic_k2 | 0.751 | 1.68e+07 | 1.87e+08 | 1.55e+05 – 4.78e+08 | 0.000 | 0.000 | 6.96e+08 |
| optimistic_k3 | 0.655 | 1.46e+07 | 1.63e+08 | 1.35e+05 – 4.17e+08 | 0.000 | 0.000 | 6.07e+08 |
| optimistic_k5 | 0.505 | 1.13e+07 | 1.26e+08 | 1.04e+05 – 3.22e+08 | 0.000 | 0.000 | 4.68e+08 |

## Similarity-weight variants — nathan_headline

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.63e+03 | 6.92e+05 | 13.2 – 4.12e+05 | 0.027 | 0.023 | 5.58e+04 |
| conservative_k10 | 0.243 | 745 | 1.98e+05 | 3.72 – 1.17e+05 | 0.054 | 0.037 | 1.59e+04 |
| conservative_k2 | 0.726 | 2.25e+03 | 5.91e+05 | 11.2 – 3.52e+05 | 0.030 | 0.024 | 4.77e+04 |
| conservative_k3 | 0.623 | 1.93e+03 | 5.08e+05 | 9.64 – 3.01e+05 | 0.033 | 0.026 | 4.1e+04 |
| conservative_k5 | 0.466 | 1.44e+03 | 3.80e+05 | 7.2 – 2.25e+05 | 0.038 | 0.029 | 3.06e+04 |
| optimistic_k1 | 0.865 | 2.68e+03 | 7.05e+05 | 13.4 – 4.21e+05 | 0.027 | 0.023 | 5.68e+04 |
| optimistic_k10 | 0.281 | 867 | 2.30e+05 | 4.32 – 1.37e+05 | 0.051 | 0.034 | 1.84e+04 |
| optimistic_k2 | 0.751 | 2.32e+03 | 6.13e+05 | 11.6 – 3.65e+05 | 0.029 | 0.024 | 4.93e+04 |
| optimistic_k3 | 0.655 | 2.03e+03 | 5.35e+05 | 10.1 – 3.19e+05 | 0.032 | 0.026 | 4.31e+04 |
| optimistic_k5 | 0.505 | 1.56e+03 | 4.13e+05 | 7.8 – 2.46e+05 | 0.037 | 0.028 | 3.32e+04 |

## Similarity-weight variants — nathan_headline_no_superhab

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.46e+03 | 6.48e+05 | 12.3 – 3.87e+05 | 0.028 | 0.024 | 5.28e+04 |
| conservative_k10 | 0.243 | 699 | 1.86e+05 | 3.51 – 1.10e+05 | 0.056 | 0.037 | 1.5e+04 |
| conservative_k2 | 0.726 | 2.1e+03 | 5.54e+05 | 10.5 – 3.31e+05 | 0.031 | 0.025 | 4.51e+04 |
| conservative_k3 | 0.623 | 1.8e+03 | 4.75e+05 | 9.05 – 2.84e+05 | 0.034 | 0.027 | 3.87e+04 |
| conservative_k5 | 0.466 | 1.35e+03 | 3.56e+05 | 6.74 – 2.11e+05 | 0.040 | 0.030 | 2.89e+04 |
| optimistic_k1 | 0.865 | 2.51e+03 | 6.60e+05 | 12.6 – 3.94e+05 | 0.028 | 0.023 | 5.37e+04 |
| optimistic_k10 | 0.281 | 813 | 2.16e+05 | 4.07 – 1.28e+05 | 0.052 | 0.035 | 1.74e+04 |
| optimistic_k2 | 0.751 | 2.17e+03 | 5.74e+05 | 10.9 – 3.43e+05 | 0.030 | 0.025 | 4.66e+04 |
| optimistic_k3 | 0.655 | 1.9e+03 | 5.01e+05 | 9.5 – 2.99e+05 | 0.033 | 0.026 | 4.07e+04 |
| optimistic_k5 | 0.505 | 1.46e+03 | 3.86e+05 | 7.31 – 2.30e+05 | 0.038 | 0.029 | 3.14e+04 |

## Similarity-weight variants — nathan_headline_no_tooluse

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 678 | 3.06e+05 | 2.86 – 1.32e+05 | 0.062 | 0.039 | 5.21e+04 |
| conservative_k10 | 0.243 | 192 | 8.75e+04 | 0.816 – 3.74e+04 | 0.109 | 0.057 | 1.48e+04 |
| conservative_k2 | 0.726 | 579 | 2.61e+05 | 2.45 – 1.13e+05 | 0.067 | 0.042 | 4.45e+04 |
| conservative_k3 | 0.623 | 497 | 2.24e+05 | 2.1 – 9.66e+04 | 0.072 | 0.044 | 3.82e+04 |
| conservative_k5 | 0.466 | 370 | 1.68e+05 | 1.57 – 7.21e+04 | 0.082 | 0.048 | 2.86e+04 |
| optimistic_k1 | 0.865 | 690 | 3.12e+05 | 2.92 – 1.35e+05 | 0.062 | 0.039 | 5.3e+04 |
| optimistic_k10 | 0.281 | 223 | 1.02e+05 | 0.945 – 4.38e+04 | 0.102 | 0.055 | 1.72e+04 |
| optimistic_k2 | 0.751 | 599 | 2.71e+05 | 2.54 – 1.17e+05 | 0.066 | 0.041 | 4.61e+04 |
| optimistic_k3 | 0.655 | 522 | 2.36e+05 | 2.21 – 1.02e+05 | 0.070 | 0.043 | 4.02e+04 |
| optimistic_k5 | 0.505 | 402 | 1.82e+05 | 1.7 – 7.87e+04 | 0.079 | 0.046 | 3.1e+04 |

## nathan_headline: effect of each new factor (paired draws: per comparison (see table))

| comparison | median N_now of comparison | nathan_headline median / comparison median | per-sample log10(N_headline/N_comparison): median [10th, 90th] |
|---|---|---|---|
| without superhabitability (tool-use change only) | 2.46e+03 | ×1.07 | 0.015 [0.002, 0.073] |
| without cross-lineage tool use (superhab only) | 678 | ×3.88 | 0.598 [0.328, 0.789] |
| without both (= similarity_weighted, v1 model) | 895 | ×2.94 | n/a (independent draws; compare medians) |

## Multi-spectral breakdown (v2 model: M/K/G/F host classes)

Each host type has its own star fraction (RECONS / Kroupa IMF), eta-Earth, habitable window, exomoon-host giants, activity/UV/tidal penalties, similarity weight (own Archive ESI list if >= 3 HZ rocky planets, else pooled) and, for K only, the superhabitability boost. Share = that type's fraction of the posterior-mean N_now; median share = per-sample median.

| scenario | host type | median N_now | 10th–90th | mean | P(N<1) | share of mean N | median share [10th, 90th] | median N_ever | best-estimate N_now | similarity weight (median) |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | M | 2.34e-04 | 4.16e-08 – 1.12 | 621 | 0.898 | 38.6% | 15.2% [2.2, 58.1] | 0.123 | 465 | – |
| baseline | K | 0.00116 | 2.47e-07 – 4.48 | 894 | 0.854 | 55.5% | 74.9% [36.2, 93.8] | 0.705 | 2.77e+03 | – |
| baseline | G | 5.92e-05 | 1.16e-08 – 0.264 | 94.4 | 0.933 | 5.9% | 3.9% [0.5, 18.7] | 0.0958 | 247 | – |
| baseline | F | 6.28e-08 | 8.57e-12 – 4.11e-04 | 1.18 | 0.994 | 0.1% | 0.0% [0.0, 0.1] | 3.69e-04 | 0.908 | – |
| baseline | **all** | 0.00179 | 3.72e-07 – 7.04 | 1.61e+03 | 0.837 | 100% | – | 1.13 | 3.48e+03 | – |
| baseline_no_exomoons | M | 1.89e-04 | 3.48e-08 – 0.912 | 531 | 0.902 | 39.2% | 15.9% [2.3, 59.3] | 0.103 | 456 | – |
| baseline_no_exomoons | K | 8.99e-04 | 1.92e-07 – 3.63 | 745 | 0.862 | 55.0% | 74.0% [35.2, 93.6] | 0.55 | 2.71e+03 | – |
| baseline_no_exomoons | G | 4.63e-05 | 8.82e-09 – 0.216 | 78.1 | 0.937 | 5.8% | 3.8% [0.5, 19.5] | 0.0744 | 243 | – |
| baseline_no_exomoons | F | 4.25e-08 | 5.67e-12 – 2.96e-04 | 0.843 | 0.995 | 0.1% | 0.0% [0.0, 0.1] | 2.55e-04 | 0.862 | – |
| baseline_no_exomoons | **all** | 0.00143 | 2.98e-07 – 5.88 | 1.36e+03 | 0.844 | 100% | – | 0.874 | 3.41e+03 | – |
| nathan_headline | M | 280 | 1.06 – 6e+04 | 1.90e+05 | 0.098 | 27.4% | 12.4% [1.8, 51.7] | 5.12e+03 | 1.98e+03 | 0.849 |
| nathan_headline | K | 1.69e+03 | 8.36 – 2.66e+05 | 4.40e+05 | 0.035 | 63.5% | 71.8% [38.8, 89.7] | 3.22e+04 | 1.25e+04 | 0.841 |
| nathan_headline | G | 228 | 1.15 – 3.55e+04 | 6.21e+04 | 0.094 | 9.0% | 9.3% [2.7, 25.6] | 9.56e+03 | 1.14e+03 | 0.85 |
| nathan_headline | F | 1.67 | 0.00681 – 324 | 906 | 0.453 | 0.1% | 0.1% [0.0, 0.6] | 458 | 5.61 | 0.85 |
| nathan_headline | **all** | 2.63e+03 | 13.2 – 4.12e+05 | 6.92e+05 | 0.027 | 100% | – | 5.58e+04 | 1.56e+04 | – |
| nathan_headline_no_superhab | M | 280 | 1.06 – 6e+04 | 1.90e+05 | 0.098 | 29.3% | 13.3% [2.0, 53.7] | 5.12e+03 | 1.98e+03 | 0.849 |
| nathan_headline_no_superhab | K | 1.54e+03 | 7.69 – 2.41e+05 | 3.96e+05 | 0.037 | 61.0% | 69.9% [36.7, 88.7] | 2.93e+04 | 1.16e+04 | 0.841 |
| nathan_headline_no_superhab | G | 228 | 1.15 – 3.55e+04 | 6.21e+04 | 0.094 | 9.6% | 9.9% [2.9, 27.0] | 9.56e+03 | 1.14e+03 | 0.85 |
| nathan_headline_no_superhab | F | 1.67 | 0.00681 – 324 | 906 | 0.453 | 0.1% | 0.1% [0.0, 0.7] | 458 | 5.61 | 0.85 |
| nathan_headline_no_superhab | **all** | 2.46e+03 | 12.3 – 3.87e+05 | 6.48e+05 | 0.028 | 100% | – | 5.28e+04 | 1.48e+04 | – |
| nathan_headline_no_tooluse | M | 73.3 | 0.232 – 1.92e+04 | 8.43e+04 | 0.170 | 27.6% | 12.4% [1.8, 51.9] | 4.8e+03 | 395 | 0.849 |
| nathan_headline_no_tooluse | K | 436 | 1.83 – 8.51e+04 | 1.95e+05 | 0.077 | 63.8% | 72.2% [38.8, 90.0] | 3.03e+04 | 2.5e+03 | 0.841 |
| nathan_headline_no_tooluse | G | 56.5 | 0.242 – 1.1e+04 | 2.61e+04 | 0.173 | 8.5% | 8.9% [2.5, 25.1] | 8.79e+03 | 210 | 0.85 |
| nathan_headline_no_tooluse | F | 0.325 | 0.00114 – 78.7 | 327 | 0.601 | 0.1% | 0.1% [0.0, 0.5] | 324 | 0.771 | 0.85 |
| nathan_headline_no_tooluse | **all** | 678 | 2.86 – 1.32e+05 | 3.06e+05 | 0.062 | 100% | – | 5.21e+04 | 3.1e+03 | – |

Top Archive planets by ESI per host type (Kopparapu+2014 HZ, R < 1.8 R_earth; conservative / optimistic counts):

| type | n (cons / opt) | top planets, optimistic HZ (ESI) | best outside the HZ cut (R<1.8; ESI, insolation S) |
|---|---|---|---|
| M | 22 / 35 | Teegarden's Star b (0.979), TOI-700 d (0.942), Kepler-1649 c (0.940), GJ 3378 b (0.938), TOI-700 e (0.932) | – |
| K | 3 / 5 | Kepler-442 b (0.882), Kepler-1410 b (0.860), Kepler-1544 b (0.841), Kepler-62 e (0.824), Kepler-62 f (0.799) | Kepler-1512 b (0.883, S=1.60) |
| G | 1 / 1 | Kepler-452 b (0.879) | Kepler-1126 c (0.813, S=2.06), Kepler-69 c (0.733, S=2.69) |
| F | 0 / 0 | none | Kepler-132 e (0.677, S=6.10), Kepler-1620 b (0.598, S=7.92), Kepler-1633 b (0.456, S=26.26) |

## Multiphase breakdown (v2 model: civilisation stages)

Stage chain inside each tool-using episode: lithic -> agricultural -> industrial -> radio-capable -> spacefaring (orbital spaceflight). Advance times log-uniform Earth/10..Earth x10 (Earth: 3.29 Myr, 11.2 kyr, 135 yr, 62 yr); stage collapse hazards (agri 1e-7..1e-3/yr, industrial 1e-6..1e-2/yr ASSUMED; radio and spacefaring 1e-10..1e-2/yr = 1/L with SDO 2018's L 1e2..1e10 yr); a uniform(0,1) fraction of collapses regresses one stage and can recur, the rest end the lineage. N per stage = N_now x long-run share of tool-using time in that stage (stationary approximation).

| scenario | stage | median N_now | 10th–90th | mean | P(N<1) | median share of tool-using time [10th, 90th] | best-estimate N_now |
|---|---|---|---|---|---|---|---|
| baseline | lithic | 0.00115 | 3.00e-07 – 3.58 | 1.03e+03 | 0.859 | 0.969 [0.202, 0.999] | 2.46e+03 |
| baseline | agricultural | 2.05e-06 | 4.33e-10 – 0.0083 | 4.83 | 0.982 | 0.00115 [1.15e-04, 0.0127] | 7.44 |
| baseline | industrial | 2.54e-08 | 3.79e-12 – 1.15e-04 | 0.0676 | 0.998 | 1.33e-05 [9.80e-07, 1.89e-04] | 0.0901 |
| baseline | radio | 1.61e-08 | 2.41e-12 – 8.13e-05 | 0.0626 | 0.998 | 8.72e-06 [5.05e-07, 1.57e-04] | 0.0728 |
| baseline | spacefaring | 2.52e-05 | 1.28e-09 – 0.505 | 574 | 0.914 | 0.0208 [1.51e-04, 0.796] | 1.01e+03 |
| baseline | **radio-capable (radio + spacefaring)** | 2.65e-05 | 1.35e-09 – 0.512 | 574 | 0.914 | – | 1.01e+03 |
| baseline_no_exomoons | lithic | 9.12e-04 | 2.36e-07 – 2.93 | 840 | 0.866 | 0.969 [0.202, 0.999] | 2.41e+03 |
| baseline_no_exomoons | agricultural | 1.56e-06 | 3.15e-10 – 0.00691 | 2.93 | 0.983 | 0.00115 [1.15e-04, 0.0127] | 7.3 |
| baseline_no_exomoons | industrial | 2.02e-08 | 2.99e-12 – 9.33e-05 | 0.0351 | 0.998 | 1.33e-05 [9.80e-07, 1.89e-04] | 0.0884 |
| baseline_no_exomoons | radio | 1.30e-08 | 1.84e-12 – 6.55e-05 | 0.0476 | 0.998 | 8.72e-06 [5.05e-07, 1.57e-04] | 0.0714 |
| baseline_no_exomoons | spacefaring | 2.03e-05 | 9.39e-10 – 0.423 | 513 | 0.918 | 0.0208 [1.51e-04, 0.796] | 994 |
| baseline_no_exomoons | **radio-capable (radio + spacefaring)** | 2.10e-05 | 1.01e-09 – 0.428 | 513 | 0.918 | – | 994 |
| nathan_headline | lithic | 1.64e+03 | 9.94 – 2.31e+05 | 4.17e+05 | 0.030 | 0.969 [0.199, 0.999] | 1.1e+04 |
| nathan_headline | agricultural | 3.13 | 0.0129 – 590 | 1.77e+03 | 0.395 | 0.00115 [1.13e-04, 0.0128] | 33.4 |
| nathan_headline | industrial | 0.0355 | 1.26e-04 – 7.27 | 23.8 | 0.785 | 1.33e-05 [9.59e-07, 1.84e-04] | 0.405 |
| nathan_headline | radio | 0.0232 | 6.78e-05 – 5.79 | 47.5 | 0.805 | 8.51e-06 [4.97e-07, 1.55e-04] | 0.327 |
| nathan_headline | spacefaring | 41.3 | 0.0191 – 5.5e+04 | 2.74e+05 | 0.274 | 0.0206 [1.47e-04, 0.797] | 4.55e+03 |
| nathan_headline | **radio-capable (radio + spacefaring)** | 42.9 | 0.0216 – 5.51e+04 | 2.74e+05 | 0.270 | – | 4.55e+03 |
| nathan_headline_no_superhab | lithic | 1.54e+03 | 9.36 – 2.16e+05 | 3.91e+05 | 0.031 | 0.969 [0.199, 0.999] | 1.04e+04 |
| nathan_headline_no_superhab | agricultural | 2.94 | 0.0121 – 553 | 1.66e+03 | 0.401 | 0.00115 [1.13e-04, 0.0128] | 31.6 |
| nathan_headline_no_superhab | industrial | 0.0333 | 1.18e-04 – 6.8 | 22.2 | 0.789 | 1.33e-05 [9.59e-07, 1.84e-04] | 0.382 |
| nathan_headline_no_superhab | radio | 0.0218 | 6.36e-05 – 5.44 | 44.7 | 0.809 | 8.51e-06 [4.97e-07, 1.55e-04] | 0.309 |
| nathan_headline_no_superhab | spacefaring | 38.7 | 0.0179 – 5.14e+04 | 2.56e+05 | 0.278 | 0.0206 [1.47e-04, 0.797] | 4.3e+03 |
| nathan_headline_no_superhab | **radio-capable (radio + spacefaring)** | 40.2 | 0.0202 – 5.14e+04 | 2.56e+05 | 0.273 | – | 4.3e+03 |
| nathan_headline_no_tooluse | lithic | 427 | 2.28 – 7.12e+04 | 1.64e+05 | 0.068 | 0.969 [0.199, 0.999] | 2.19e+03 |
| nathan_headline_no_tooluse | agricultural | 0.829 | 0.00298 – 173 | 557 | 0.517 | 0.00115 [1.13e-04, 0.0128] | 6.64 |
| nathan_headline_no_tooluse | industrial | 0.00941 | 2.87e-05 – 2.14 | 7.44 | 0.863 | 1.33e-05 [9.59e-07, 1.84e-04] | 0.0804 |
| nathan_headline_no_tooluse | radio | 0.00612 | 1.55e-05 – 1.69 | 15 | 0.876 | 8.51e-06 [4.97e-07, 1.55e-04] | 0.0649 |
| nathan_headline_no_tooluse | spacefaring | 10.2 | 0.00425 – 1.87e+04 | 1.41e+05 | 0.358 | 0.0206 [1.47e-04, 0.797] | 904 |
| nathan_headline_no_tooluse | **radio-capable (radio + spacefaring)** | 10.6 | 0.00472 – 1.87e+04 | 1.41e+05 | 0.354 | – | 904 |

Radio-capable N vs classic SETI-style Drake: Sandberg, Drexler & Ord 2018's 'current knowledge' sketch gives median N = 0.32, mean 27 million, P(N<1) = 52% (communicating civilisations; their Table 1). This model's static SDO-style stone-age variant: median 28.8.

| scenario | median episode length (yr) [10th, 90th] | radio-capable: median NN distance (ly) | top drivers of radio-capable N (swing, dex) |
|---|---|---|---|
| baseline | 1.21e+06 [3.15e+04, 1.87e+07] | 8.08e+06 (N<1) | l_stone_yr 4.4; tau_stone_tool_intelligence 4.3; f_land_and_ocean 3.7; stage_h_space_per_yr 3.1; tau_abiogenesis 2.7 |
| baseline_no_exomoons | 1.21e+06 [3.15e+04, 1.87e+07] | 9.08e+06 (N<1) | tau_stone_tool_intelligence 4.4; l_stone_yr 4.4; f_land_and_ocean 3.7; stage_h_space_per_yr 3.1; tau_abiogenesis 2.7 |
| nathan_headline | 1.21e+06 [3.11e+04, 1.86e+07] | 6.35e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; f_land_and_ocean 3.4; f_plate_tectonics 1.8; m_recurrence 1.4 |
| nathan_headline_no_superhab | 1.21e+06 [3.11e+04, 1.86e+07] | 6.57e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; f_land_and_ocean 3.3; f_plate_tectonics 1.8; m_recurrence 1.5 |
| nathan_headline_no_tooluse | 1.21e+06 [3.11e+04, 1.86e+07] | 1.28e+04 | l_stone_yr 4.5; stage_h_space_per_yr 3.4; f_land_and_ocean 3.4; f_plate_tectonics 1.8; m_recurrence 1.6 |

## Spacing: equal-cube side and median nearest-neighbour distance (disk volume ~7.9e12 ly³, user-supplied)

Cube side = (V/N)^(1/3). Nearest-neighbour: random (Poisson) placement; 3D median r = (3 ln2/(4πn))^(1/3), or the thin-disk 2D form when r exceeds the 1,000-ly thickness (R = 50,000 ly). Values for N < 1 mean no neighbour is expected; they are shown only formally.

| scenario | median N | cube side at median (ly) | median NN distance at median (ly) | regime | NN at 90th-pct N (ly) | NN at 10th-pct N (ly) |
|---|---|---|---|---|---|---|
| baseline | 0.00179 | 1.64e+05 | 9.83e+05 (N<1: none expected) | 2D thin disk | 1.57e+04 | 6.83e+07 (N<1: none expected) |
| baseline_no_exomoons | 0.00143 | 1.77e+05 | 1.10e+06 (N<1: none expected) | 2D thin disk | 1.72e+04 | 7.63e+07 (N<1: none expected) |
| snyder_beattie_priors | 5.51e-21 | 1.13e+11 | 5.61e+14 (N<1: none expected) | 2D thin disk | 1.29e+10 (N<1: none expected) | 2.20e+19 (N<1: none expected) |
| user_inputs | 9.93e-05 | 4.30e+05 | 4.18e+06 (N<1: none expected) | 2D thin disk | 8.31e+04 (N<1: none expected) | 2.10e+08 (N<1: none expected) |
| user_fast_intelligence | 571 | 2.4e+03 | 1.74e+03 | 2D thin disk | 185 | 4.85e+04 (N<1: none expected) |
| similarity_weighted | 895 | 2.07e+03 | 1.39e+03 | 2D thin disk | 185 | 2.54e+04 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 74.6 | 41 | 3D | 13.4 | 195 |
| earth_random_draw | 157 | 3.69e+03 | 3.32e+03 | 2D thin disk | 281 | 8.77e+04 (N<1: none expected) |
| nathan_headline | 2.63e+03 | 1.44e+03 | 792 | 3D | 147 | 1.15e+04 |
| nathan_headline_no_superhab | 2.46e+03 | 1.48e+03 | 810 | 3D | 150 | 1.18e+04 |
| nathan_headline_no_tooluse | 678 | 2.27e+03 | 1.6e+03 | 2D thin disk | 215 | 2.46e+04 |
| classic_static_SDO_style | 28.8 | 6.49e+03 | 7.75e+03 | 2D thin disk | 95.7 | 2.35e+34 (N<1: none expected) |

## Comparison with the user's claims

| scenario | median N_now | P(1<=N_now<=3) ('1-3 at a time') | P(N_now>=1) | median N_ever by now | P(50<=N_ever<=100) | P(N_ever>=50) |
|---|---|---|---|---|---|---|
| baseline | 0.00179 | 0.039 | 0.163 | 1.13 | 0.038 | 0.243 |
| baseline_no_exomoons | 0.00143 | 0.039 | 0.156 | 0.874 | 0.036 | 0.232 |
| snyder_beattie_priors | 5.51e-21 | 0.000 | 0.001 | 4.70e-18 | 0.000 | 0.001 |
| user_inputs | 9.93e-05 | 0.021 | 0.066 | 0.875 | 0.039 | 0.233 |
| user_fast_intelligence | 571 | 0.042 | 0.890 | 967 | 0.047 | 0.723 |
| similarity_weighted | 895 | 0.038 | 0.933 | 4.39e+04 | 0.014 | 0.982 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 0.000 | 1.000 | 7.87e+08 | 0.000 | 1.000 |
| earth_random_draw | 157 | 0.057 | 0.841 | 1.2e+04 | 0.030 | 0.924 |
| nathan_headline | 2.63e+03 | 0.023 | 0.973 | 5.58e+04 | 0.012 | 0.986 |
| nathan_headline_no_superhab | 2.46e+03 | 0.024 | 0.972 | 5.28e+04 | 0.012 | 0.986 |
| nathan_headline_no_tooluse | 678 | 0.039 | 0.938 | 5.21e+04 | 0.012 | 0.985 |

## Exomoon effect (paired, same draws)
Median N_now with exomoons 0.00179 vs without 0.00143; per-sample log10(N_with/N_without): median 0.008 dex, 90th pct 0.316, 99th pct 1.075. Median share of habitable bodies that are moons: M 0.0111, K 0.0195, G 0.0177, F 0.0384.


## Deterministic best-estimate point calculations

All parameters at their `best` values; hard-step expected times set equal to Earth's observed intervals (a 'Copernican / Earth-is-typical' choice).

| scenario | N_now | time-avg N | N_ever by now | fraction from Sun-like hosts (v1: G/K; v2: F/G/K) |
|---|---|---|---|---|
| baseline | 3.48e+03 | 1.27e+03 | 8.14e+04 | 0.866 |
| baseline_no_exomoons | 3.41e+03 | 1.24e+03 | 7.99e+04 | 0.866 |
| snyder_beattie_priors | 3.31e+03 | 1.93e+03 | 8.26e+04 | 0.733 |
| user_inputs | 86.5 | 41.8 | 8.63e+04 | 0.82 |
| user_fast_intelligence | 5.44e+04 | 2.79e+04 | 9.17e+04 | 0.825 |
| similarity_weighted | 2.81e+03 | 1.64e+03 | 7.02e+04 | 0.733 |
| similarity_weighted_no_rare_earth | 5.63e+06 | 3.29e+06 | 1.41e+08 | 0.733 |
| earth_random_draw | 3.31e+03 | 1.93e+03 | 8.26e+04 | 0.733 |
| nathan_headline | 1.56e+04 | 6.05e+03 | 7.62e+04 | 0.873 |
| nathan_headline_no_superhab | 1.48e+04 | 5.74e+03 | 7.26e+04 | 0.866 |
| nathan_headline_no_tooluse | 3.1e+03 | 1.13e+03 | 7.21e+04 | 0.873 |

## Sensitivity — baseline

ESS = 13586 of 200000 samples. Median share of N_now from G/K hosts: 0.848. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.475 | -0.65 | -4.82 | 4.17 |
| f_land_and_ocean | +0.370 | -4.54 | -0.92 | 3.62 |
| l_stone_yr | +0.290 | -4.45 | -1.78 | 2.67 |
| tau_abiogenesis | -0.270 | -1.81 | -4.41 | 2.60 |
| tau_complex_multicellularity | -0.269 | -1.64 | -4.16 | 2.52 |
| tau_eukaryogenesis | -0.266 | -1.68 | -4.15 | 2.48 |
| tau_oxygenic_photosynthesis_GOE | -0.262 | -1.64 | -3.99 | 2.35 |
| f_plate_tectonics | +0.187 | -3.72 | -1.97 | 1.75 |
| r_ster0_per_gyr | -0.157 | -2.27 | -4.02 | 1.75 |
| f_large_moon | +0.133 | -3.55 | -2.08 | 1.46 |
| f_jupiter_shield | +0.100 | -3.23 | -2.27 | 0.96 |
| f_ghz | +0.106 | -3.15 | -2.28 | 0.87 |
| m_recurrence | -0.119 | -2.42 | -3.22 | 0.80 |
| ne_K | +0.037 | -3.05 | -2.52 | 0.53 |
| f_exomoon_host | +0.037 | -2.79 | -2.38 | 0.41 |

## Sensitivity — baseline_no_exomoons

ESS = 13586 of 200000 samples. Median share of N_now from G/K hosts: 0.841. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.473 | -0.73 | -4.90 | 4.17 |
| f_land_and_ocean | +0.369 | -4.65 | -1.02 | 3.63 |
| tau_abiogenesis | -0.269 | -1.86 | -4.50 | 2.64 |
| l_stone_yr | +0.288 | -4.56 | -1.92 | 2.64 |
| tau_complex_multicellularity | -0.269 | -1.71 | -4.22 | 2.51 |
| tau_eukaryogenesis | -0.266 | -1.80 | -4.29 | 2.49 |
| tau_oxygenic_photosynthesis_GOE | -0.261 | -1.70 | -4.03 | 2.33 |
| f_plate_tectonics | +0.187 | -3.81 | -2.04 | 1.77 |
| r_ster0_per_gyr | -0.156 | -2.33 | -4.09 | 1.76 |
| f_large_moon | +0.154 | -3.71 | -2.10 | 1.60 |
| f_jupiter_shield | +0.114 | -3.44 | -2.30 | 1.14 |
| f_ghz | +0.107 | -3.24 | -2.41 | 0.84 |
| m_recurrence | -0.118 | -2.52 | -3.29 | 0.77 |
| ne_K | +0.040 | -3.15 | -2.58 | 0.58 |
| f_m_habitable | +0.036 | -3.08 | -2.63 | 0.45 |

## Sensitivity — snyder_beattie_priors

ESS = 3151 of 200000 samples. Median share of N_now from G/K hosts: 0.746. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.58 -> posterior 0.06; posterior P(tau_intelligence<5 Gyr) = 0.11.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.406 | -14.18 | -24.63 | 10.45 |
| tau_abiogenesis | -0.357 | -16.00 | -25.68 | 9.68 |
| tau_complex_multicellularity | -0.349 | -14.87 | -24.00 | 9.13 |
| tau_oxygenic_photosynthesis_GOE | -0.333 | -16.05 | -24.78 | 8.73 |
| tau_eukaryogenesis | -0.376 | -15.94 | -24.63 | 8.68 |
| f_land_and_ocean | +0.145 | -21.63 | -18.40 | 3.23 |
| l_stone_yr | +0.131 | -21.59 | -18.82 | 2.77 |
| ne_gk | +0.032 | -20.58 | -19.01 | 1.57 |
| th_gk_gyr | +0.052 | -21.19 | -19.77 | 1.43 |
| ne_m | -0.022 | -19.01 | -20.27 | 1.27 |
| f_jupiter_shield | +0.048 | -20.63 | -19.47 | 1.16 |
| f_plate_tectonics | +0.069 | -21.40 | -20.30 | 1.10 |
| r_self_per_gyr | -0.023 | -20.88 | -19.86 | 1.02 |
| r_ster0_per_gyr | -0.029 | -20.12 | -21.07 | 0.95 |
| th_m_gyr | -0.023 | -19.74 | -20.64 | 0.89 |

## Sensitivity — user_inputs

ESS = 34101 of 500000 samples. Median share of N_now from G/K hosts: 0.7. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.507 | -1.73 | -6.03 | 4.30 |
| f_land_and_ocean | +0.381 | -5.67 | -2.39 | 3.29 |
| tau_eukaryogenesis | -0.292 | -2.85 | -5.45 | 2.60 |
| tau_abiogenesis | -0.295 | -2.99 | -5.54 | 2.55 |
| tau_oxygenic_photosynthesis_GOE | -0.272 | -2.78 | -5.30 | 2.52 |
| tau_complex_multicellularity | -0.281 | -2.92 | -5.32 | 2.40 |
| f_plate_tectonics | +0.201 | -4.84 | -3.19 | 1.65 |
| f_large_moon | +0.156 | -4.70 | -3.25 | 1.45 |
| r_ster0_per_gyr | -0.122 | -3.72 | -5.05 | 1.33 |
| f_jupiter_shield | +0.106 | -4.49 | -3.48 | 1.02 |
| f_ghz | +0.104 | -4.53 | -3.55 | 0.99 |
| m_recurrence | -0.129 | -3.38 | -4.31 | 0.92 |
| l_stone_yr | +0.058 | -4.31 | -3.75 | 0.56 |
| f_m_flares | +0.054 | -4.18 | -3.64 | 0.53 |
| ne_gk | +0.051 | -4.26 | -3.75 | 0.52 |

## Sensitivity — user_fast_intelligence

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.779. Median epoch of peak N(t): 0.15 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.50; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.510 | 1.13 | 4.49 | 3.36 |
| tau_eukaryogenesis | -0.309 | 3.32 | 1.09 | 2.22 |
| tau_abiogenesis | -0.309 | 3.31 | 1.10 | 2.21 |
| tau_complex_multicellularity | -0.311 | 3.31 | 1.11 | 2.19 |
| tau_oxygenic_photosynthesis_GOE | -0.311 | 3.30 | 1.11 | 2.19 |
| f_plate_tectonics | +0.268 | 1.87 | 3.67 | 1.80 |
| f_large_moon | +0.189 | 2.19 | 3.46 | 1.28 |
| r_ster0_per_gyr | -0.144 | 3.04 | 1.92 | 1.12 |
| f_jupiter_shield | +0.136 | 2.31 | 3.24 | 0.93 |
| f_ghz | +0.134 | 2.31 | 3.22 | 0.91 |
| f_exomoon_host | +0.062 | 2.63 | 3.12 | 0.49 |
| ne_gk | +0.071 | 2.55 | 2.99 | 0.45 |
| f_m_flares | +0.059 | 2.62 | 3.00 | 0.38 |
| f_m_habitable | +0.057 | 2.61 | 2.98 | 0.37 |
| m_disk_now | +0.029 | 2.61 | 2.86 | 0.25 |

## Sensitivity — similarity_weighted

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.823. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.568 | 1.34 | 4.64 | 3.31 |
| l_stone_yr | +0.558 | 0.99 | 4.13 | 3.14 |
| f_plate_tectonics | +0.299 | 2.07 | 3.84 | 1.77 |
| m_recurrence | -0.242 | 3.62 | 2.15 | 1.46 |
| f_large_moon | +0.208 | 2.31 | 3.60 | 1.28 |
| r_ster0_per_gyr | -0.160 | 3.25 | 2.17 | 1.08 |
| f_jupiter_shield | +0.151 | 2.50 | 3.42 | 0.92 |
| f_ghz | +0.149 | 2.49 | 3.41 | 0.92 |
| ne_gk | +0.085 | 2.71 | 3.21 | 0.50 |
| f_exomoon_host | +0.065 | 2.84 | 3.33 | 0.49 |
| th_gk_gyr | +0.079 | 2.65 | 3.09 | 0.43 |
| f_m_habitable | +0.063 | 2.81 | 3.19 | 0.38 |
| f_m_flares | +0.054 | 2.84 | 3.17 | 0.33 |
| stars_per_msun | +0.037 | 2.84 | 3.04 | 0.20 |
| m_disk_now | +0.032 | 2.84 | 3.04 | 0.20 |

## Sensitivity — similarity_weighted_no_rare_earth

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.808. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| l_stone_yr | +0.803 | 5.19 | 8.36 | 3.17 |
| m_recurrence | -0.341 | 7.97 | 6.50 | 1.47 |
| r_ster0_per_gyr | -0.230 | 7.58 | 6.51 | 1.07 |
| f_ghz | +0.214 | 6.84 | 7.74 | 0.90 |
| ne_gk | +0.144 | 7.00 | 7.60 | 0.59 |
| th_gk_gyr | +0.117 | 6.97 | 7.43 | 0.46 |
| f_m_flares | +0.086 | 7.13 | 7.52 | 0.38 |
| f_m_habitable | +0.094 | 7.14 | 7.51 | 0.37 |
| r_self_per_gyr | -0.049 | 7.34 | 7.11 | 0.23 |
| stars_per_msun | +0.053 | 7.17 | 7.38 | 0.21 |
| m_disk_now | +0.045 | 7.16 | 7.35 | 0.19 |
| f_gk | +0.035 | 7.22 | 7.34 | 0.12 |
| sfr_now | +0.016 | 7.22 | 7.32 | 0.10 |
| ne_m | +0.024 | 7.23 | 7.33 | 0.10 |
| f_early_disk_mass | -0.009 | 7.33 | 7.25 | 0.08 |

## Sensitivity — earth_random_draw

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.797. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.61 -> posterior 0.61; posterior P(tau_intelligence<5 Gyr) = 0.89.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.507 | 0.60 | 3.87 | 3.28 |
| l_stone_yr | +0.511 | 0.21 | 3.40 | 3.19 |
| tau_stone_tool_intelligence | -0.269 | 2.94 | 0.68 | 2.26 |
| f_plate_tectonics | +0.271 | 1.28 | 3.11 | 1.82 |
| m_recurrence | -0.207 | 2.90 | 1.48 | 1.42 |
| r_ster0_per_gyr | -0.162 | 2.52 | 1.27 | 1.25 |
| f_large_moon | +0.189 | 1.60 | 2.85 | 1.24 |
| tau_oxygenic_photosynthesis_GOE | -0.127 | 2.44 | 1.36 | 1.08 |
| tau_complex_multicellularity | -0.118 | 2.45 | 1.40 | 1.05 |
| f_ghz | +0.132 | 1.75 | 2.65 | 0.90 |
| f_jupiter_shield | +0.134 | 1.78 | 2.66 | 0.88 |
| tau_eukaryogenesis | -0.085 | 2.36 | 1.55 | 0.81 |
| tau_abiogenesis | -0.075 | 2.31 | 1.58 | 0.73 |
| th_gk_gyr | +0.094 | 1.80 | 2.40 | 0.60 |
| ne_gk | +0.075 | 1.97 | 2.44 | 0.46 |

## Sensitivity — nathan_headline

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.876. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.622 | 1.78 | 5.13 | 3.35 |
| l_stone_yr | +0.429 | 1.80 | 4.17 | 2.37 |
| f_plate_tectonics | +0.327 | 2.49 | 4.30 | 1.81 |
| m_recurrence | -0.257 | 4.05 | 2.64 | 1.41 |
| f_large_moon | +0.234 | 2.77 | 4.08 | 1.30 |
| r_ster0_per_gyr | -0.181 | 3.72 | 2.60 | 1.12 |
| f_jupiter_shield | +0.164 | 3.00 | 3.90 | 0.90 |
| f_ghz | +0.164 | 2.98 | 3.85 | 0.87 |
| f_exomoon_host | +0.061 | 3.34 | 3.72 | 0.38 |
| stage_tau_agri_yr | +0.058 | 3.26 | 3.55 | 0.29 |
| f_m_habitable | +0.045 | 3.34 | 3.62 | 0.28 |
| n_tool_origins | +0.047 | 3.28 | 3.55 | 0.27 |
| tau_stone_tool_intelligence | -0.047 | 3.55 | 3.28 | 0.27 |
| f_m_flares | +0.045 | 3.33 | 3.60 | 0.27 |
| stage_h_space_per_yr | -0.062 | 3.58 | 3.32 | 0.27 |

## Sensitivity — nathan_headline_no_superhab

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.867. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.622 | 1.75 | 5.10 | 3.35 |
| l_stone_yr | +0.429 | 1.77 | 4.14 | 2.37 |
| f_plate_tectonics | +0.327 | 2.47 | 4.27 | 1.81 |
| m_recurrence | -0.257 | 4.02 | 2.61 | 1.41 |
| f_large_moon | +0.232 | 2.75 | 4.05 | 1.29 |
| r_ster0_per_gyr | -0.181 | 3.69 | 2.57 | 1.12 |
| f_jupiter_shield | +0.163 | 2.97 | 3.87 | 0.90 |
| f_ghz | +0.164 | 2.95 | 3.82 | 0.87 |
| f_exomoon_host | +0.063 | 3.30 | 3.71 | 0.40 |
| stage_tau_agri_yr | +0.058 | 3.23 | 3.53 | 0.30 |
| f_m_habitable | +0.047 | 3.31 | 3.60 | 0.29 |
| f_m_flares | +0.048 | 3.30 | 3.58 | 0.28 |
| n_tool_origins | +0.047 | 3.25 | 3.52 | 0.27 |
| tau_stone_tool_intelligence | -0.047 | 3.52 | 3.25 | 0.27 |
| stage_h_space_per_yr | -0.062 | 3.56 | 3.29 | 0.26 |

## Sensitivity — nathan_headline_no_tooluse

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.876. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.597 | 1.18 | 4.53 | 3.35 |
| l_stone_yr | +0.466 | 1.10 | 3.73 | 2.64 |
| f_plate_tectonics | +0.314 | 1.90 | 3.72 | 1.81 |
| m_recurrence | -0.283 | 3.61 | 1.99 | 1.61 |
| f_large_moon | +0.225 | 2.19 | 3.49 | 1.30 |
| r_ster0_per_gyr | -0.180 | 3.14 | 1.97 | 1.17 |
| f_jupiter_shield | +0.158 | 2.41 | 3.31 | 0.89 |
| f_ghz | +0.158 | 2.38 | 3.26 | 0.88 |
| f_exomoon_host | +0.058 | 2.76 | 3.14 | 0.38 |
| stage_tau_agri_yr | +0.069 | 2.63 | 2.99 | 0.36 |
| stage_h_space_per_yr | -0.078 | 3.05 | 2.70 | 0.35 |
| f_m_habitable | +0.044 | 2.76 | 3.03 | 0.28 |
| f_m_flares | +0.044 | 2.75 | 3.00 | 0.26 |
| stars_per_msun | +0.040 | 2.72 | 2.95 | 0.23 |
| ne_K | +0.042 | 2.73 | 2.96 | 0.23 |
