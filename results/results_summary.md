# Results — time-aware extended Drake model (stone-age-or-greater)

**Headline scenario: `nathan_headline`** (user-approved). Literature baseline for comparison: `baseline`.

Model versions: **v2** (multi-spectral M/K/G/F host classes + multiphase civilisation stages) for `baseline`, `baseline_no_exomoons`, `nathan_headline`, `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`; all other scenarios are **v1** (two host classes G/K + M, single stone-age-or-greater phase). v1 numbers for the re-run scenarios are kept in results/v1/.

N = expected number of Milky Way worlds with stone-age-or-greater tool users alive at the same time (present day, other than Earth). Percentiles are over parameter uncertainty (posterior after the Earth-timing update where enabled).

| scenario | median (50/50) | mean | 10th pct | 90th pct | P(N<1) | P(no other, Poisson) | P(1<=N<=3) | time-avg N over history | median N_ever (by now) | ESS |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 0.00204 | 1.73e+03 | 4.33e-07 | 7.99 | 0.832 | 0.804 | 0.041 | median 3.64e-04 / mean 484 | 1.18 | 13586 |
| baseline_no_exomoons | 0.00161 | 1.46e+03 | 3.34e-07 | 6.54 | 0.840 | 0.812 | 0.040 | median 2.84e-04 / mean 392 | 0.92 | 13586 |
| snyder_beattie_priors | 5.45e-21 | 0.64 | 3.53e-30 | 1.04e-11 | 0.999 | 0.999 | 0.000 | median 1.16e-21 / mean 0.227 | 4.71e-18 | 3151 |
| user_inputs | 9.90e-05 | 34.2 | 3.92e-08 | 0.25 | 0.934 | 0.916 | 0.021 | median 2.57e-05 / mean 12.3 | 0.873 | 34101 |
| user_fast_intelligence | 569 | 5.99e+05 | 0.735 | 2.06e+05 | 0.110 | 0.098 | 0.042 | median 218 / mean 3.35e+05 | 965 | 200000 |
| similarity_weighted | 888 | 4.63e+05 | 2.67 | 2.05e+05 | 0.067 | 0.058 | 0.038 | median 354 / mean 1.76e+05 | 4.39e+04 | 200000 |
| similarity_weighted_no_rare_earth | 1.89e+07 | 2.09e+08 | 1.75e+05 | 5.34e+08 | 0.000 | 0.000 | 0.000 | median 7.45e+06 / mean 8.02e+07 | 7.86e+08 | 200000 |
| earth_random_draw | 156 | 2.29e+05 | 0.224 | 5.83e+04 | 0.159 | 0.141 | 0.058 | median 49.9 / mean 7.82e+04 | 1.2e+04 | 200000 |
| nathan_headline | 2.79e+03 | 7.27e+05 | 13.8 | 4.36e+05 | 0.027 | 0.023 | 0.022 | median 1.03e+03 / mean 2.74e+05 | 5.66e+04 | 200000 |
| nathan_headline_no_superhab | 2.61e+03 | 6.80e+05 | 13 | 4.09e+05 | 0.028 | 0.024 | 0.023 | median 968 / mean 2.58e+05 | 5.37e+04 | 200000 |
| nathan_headline_no_tooluse | 719 | 3.21e+05 | 3.04 | 1.40e+05 | 0.061 | 0.052 | 0.039 | median 252 / mean 1.14e+05 | 5.29e+04 | 200000 |
| classic_static_SDO_style | 28.8 | 8.05e+06 | 3.14e-60 | 1.49e+06 | 0.465 | 0.463 | 0.007 | (static) | – | – |

## Worlds vs tool-using species (species_per_tool_world)

species_now = N_now x concurrent hominin-grade species per tool world (log-uniform 1-5, best 2.38, from Smithsonian date spans); species_ever = N_ever x cumulative species per tool world (uniform 8-16, best 15). The factor multiplies species, not worlds.

| scenario | median worlds now | median species now | species 10th-90th | mean species now | median worlds ever | median species ever | best-estimate species now |
|---|---|---|---|---|---|---|---|
| baseline | 0.00204 | 0.00446 | 9.53e-07 – 17.7 | 4.51e+03 | 1.18 | 14 | 8.29e+03 |
| baseline_no_exomoons | 0.00161 | 0.0035 | 7.60e-07 – 14.5 | 3.95e+03 | 0.92 | 10.9 | 8.14e+03 |
| snyder_beattie_priors | 5.45e-21 | 1.28e-20 | 6.90e-30 – 2.20e-11 | 0.95 | 4.71e-18 | 5.52e-17 | 7.8e+03 |
| user_inputs | 9.90e-05 | 2.20e-04 | 8.52e-08 – 0.599 | 84.9 | 0.873 | 10.2 | 205 |
| user_fast_intelligence | 569 | 1.28e+03 | 1.58 – 4.74e+05 | 1.49e+06 | 965 | 1.14e+04 | 1.29e+05 |
| similarity_weighted | 888 | 1.98e+03 | 5.89 – 4.75e+05 | 1.13e+06 | 4.39e+04 | 5.18e+05 | 6.62e+03 |
| similarity_weighted_no_rare_earth | 1.89e+07 | 4.17e+07 | 3.78e+05 – 1.26e+09 | 5.23e+08 | 7.86e+08 | 9.25e+09 | 1.33e+07 |
| earth_random_draw | 156 | 348 | 0.49 – 1.34e+05 | 6.02e+05 | 1.2e+04 | 1.42e+05 | 7.8e+03 |
| nathan_headline | 2.79e+03 | 6.2e+03 | 30.1 – 1.00e+06 | 1.76e+06 | 5.66e+04 | 6.66e+05 | 3.73e+04 |
| nathan_headline_no_superhab | 2.61e+03 | 5.82e+03 | 28.2 – 9.43e+05 | 1.64e+06 | 5.37e+04 | 6.29e+05 | 3.52e+04 |
| nathan_headline_no_tooluse | 719 | 1.61e+03 | 6.61 – 3.24e+05 | 7.66e+05 | 5.29e+04 | 6.21e+05 | 7.4e+03 |
| classic_static_SDO_style | 28.8 | 61.8 | 6.93e-60 – 3.40e+06 | 2.00e+07 | – | – | – |

## Similarity-weight variants — similarity_weighted

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 888 | 4.63e+05 | 2.67 – 2.05e+05 | 0.067 | 0.038 | 4.39e+04 |
| conservative_k10 | 0.243 | 253 | 1.32e+05 | 0.759 – 5.85e+04 | 0.111 | 0.052 | 1.24e+04 |
| conservative_k2 | 0.726 | 758 | 3.95e+05 | 2.28 – 1.75e+05 | 0.071 | 0.039 | 3.74e+04 |
| conservative_k3 | 0.623 | 650 | 3.39e+05 | 1.96 – 1.50e+05 | 0.076 | 0.041 | 3.21e+04 |
| conservative_k5 | 0.466 | 486 | 2.54e+05 | 1.46 – 1.12e+05 | 0.086 | 0.044 | 2.4e+04 |
| optimistic_k1 | 0.865 | 903 | 4.72e+05 | 2.72 – 2.09e+05 | 0.066 | 0.037 | 4.47e+04 |
| optimistic_k10 | 0.281 | 293 | 1.54e+05 | 0.884 – 6.79e+04 | 0.105 | 0.050 | 1.45e+04 |
| optimistic_k2 | 0.751 | 785 | 4.10e+05 | 2.36 – 1.82e+05 | 0.070 | 0.039 | 3.88e+04 |
| optimistic_k3 | 0.655 | 685 | 3.58e+05 | 2.06 – 1.58e+05 | 0.075 | 0.040 | 3.39e+04 |
| optimistic_k5 | 0.505 | 528 | 2.76e+05 | 1.59 – 1.22e+05 | 0.083 | 0.043 | 2.61e+04 |

## Similarity-weight variants — similarity_weighted_no_rare_earth

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 1.89e+07 | 2.09e+08 | 1.75e+05 – 5.34e+08 | 0.000 | 0.000 | 7.86e+08 |
| conservative_k10 | 0.243 | 5.37e+06 | 5.98e+07 | 4.94e+04 – 1.53e+08 | 0.000 | 0.000 | 2.23e+08 |
| conservative_k2 | 0.726 | 1.61e+07 | 1.79e+08 | 1.49e+05 – 4.56e+08 | 0.000 | 0.000 | 6.71e+08 |
| conservative_k3 | 0.623 | 1.38e+07 | 1.53e+08 | 1.28e+05 – 3.91e+08 | 0.000 | 0.000 | 5.76e+08 |
| conservative_k5 | 0.466 | 1.03e+07 | 1.15e+08 | 9.53e+04 – 2.93e+08 | 0.000 | 0.000 | 4.30e+08 |
| optimistic_k1 | 0.865 | 1.92e+07 | 2.13e+08 | 1.78e+05 – 5.43e+08 | 0.000 | 0.000 | 8.00e+08 |
| optimistic_k10 | 0.281 | 6.22e+06 | 6.94e+07 | 5.75e+04 – 1.77e+08 | 0.000 | 0.000 | 2.59e+08 |
| optimistic_k2 | 0.751 | 1.67e+07 | 1.85e+08 | 1.55e+05 – 4.72e+08 | 0.000 | 0.000 | 6.95e+08 |
| optimistic_k3 | 0.655 | 1.45e+07 | 1.61e+08 | 1.34e+05 – 4.11e+08 | 0.000 | 0.000 | 6.06e+08 |
| optimistic_k5 | 0.505 | 1.12e+07 | 1.24e+08 | 1.03e+05 – 3.18e+08 | 0.000 | 0.000 | 4.67e+08 |

## Similarity-weight variants — nathan_headline

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.79e+03 | 7.27e+05 | 13.8 – 4.36e+05 | 0.027 | 0.022 | 5.66e+04 |
| conservative_k10 | 0.243 | 792 | 2.08e+05 | 3.92 – 1.24e+05 | 0.053 | 0.036 | 1.61e+04 |
| conservative_k2 | 0.726 | 2.38e+03 | 6.21e+05 | 11.8 – 3.72e+05 | 0.029 | 0.024 | 4.84e+04 |
| conservative_k3 | 0.623 | 2.05e+03 | 5.33e+05 | 10.1 – 3.19e+05 | 0.032 | 0.025 | 4.16e+04 |
| conservative_k5 | 0.466 | 1.53e+03 | 3.99e+05 | 7.57 – 2.39e+05 | 0.037 | 0.028 | 3.11e+04 |
| optimistic_k1 | 0.865 | 2.85e+03 | 7.41e+05 | 14.1 – 4.44e+05 | 0.026 | 0.022 | 5.76e+04 |
| optimistic_k10 | 0.281 | 920 | 2.42e+05 | 4.56 – 1.44e+05 | 0.049 | 0.034 | 1.87e+04 |
| optimistic_k2 | 0.751 | 2.47e+03 | 6.44e+05 | 12.2 – 3.86e+05 | 0.028 | 0.023 | 5.01e+04 |
| optimistic_k3 | 0.655 | 2.16e+03 | 5.62e+05 | 10.7 – 3.37e+05 | 0.031 | 0.025 | 4.37e+04 |
| optimistic_k5 | 0.505 | 1.66e+03 | 4.34e+05 | 8.23 – 2.59e+05 | 0.035 | 0.028 | 3.37e+04 |

## Similarity-weight variants — nathan_headline_no_superhab

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.61e+03 | 6.80e+05 | 13 – 4.09e+05 | 0.028 | 0.023 | 5.37e+04 |
| conservative_k10 | 0.243 | 740 | 1.95e+05 | 3.69 – 1.16e+05 | 0.055 | 0.036 | 1.52e+04 |
| conservative_k2 | 0.726 | 2.23e+03 | 5.81e+05 | 11.1 – 3.49e+05 | 0.030 | 0.024 | 4.58e+04 |
| conservative_k3 | 0.623 | 1.91e+03 | 4.99e+05 | 9.53 – 2.99e+05 | 0.033 | 0.026 | 3.93e+04 |
| conservative_k5 | 0.466 | 1.43e+03 | 3.73e+05 | 7.11 – 2.23e+05 | 0.039 | 0.029 | 2.94e+04 |
| optimistic_k1 | 0.865 | 2.66e+03 | 6.92e+05 | 13.3 – 4.15e+05 | 0.027 | 0.023 | 5.45e+04 |
| optimistic_k10 | 0.281 | 861 | 2.26e+05 | 4.29 – 1.35e+05 | 0.051 | 0.035 | 1.77e+04 |
| optimistic_k2 | 0.751 | 2.31e+03 | 6.02e+05 | 11.5 – 3.61e+05 | 0.029 | 0.024 | 4.74e+04 |
| optimistic_k3 | 0.655 | 2.01e+03 | 5.25e+05 | 10 – 3.15e+05 | 0.032 | 0.025 | 4.13e+04 |
| optimistic_k5 | 0.505 | 1.55e+03 | 4.05e+05 | 7.72 – 2.43e+05 | 0.037 | 0.028 | 3.19e+04 |

## Similarity-weight variants — nathan_headline_no_tooluse

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 719 | 3.21e+05 | 3.04 – 1.40e+05 | 0.061 | 0.039 | 5.29e+04 |
| conservative_k10 | 0.243 | 204 | 9.17e+04 | 0.866 – 3.97e+04 | 0.106 | 0.057 | 1.5e+04 |
| conservative_k2 | 0.726 | 614 | 2.74e+05 | 2.6 – 1.20e+05 | 0.065 | 0.041 | 4.52e+04 |
| conservative_k3 | 0.623 | 528 | 2.35e+05 | 2.23 – 1.03e+05 | 0.070 | 0.043 | 3.88e+04 |
| conservative_k5 | 0.466 | 394 | 1.76e+05 | 1.67 – 7.65e+04 | 0.080 | 0.047 | 2.9e+04 |
| optimistic_k1 | 0.865 | 731 | 3.26e+05 | 3.1 – 1.43e+05 | 0.060 | 0.039 | 5.38e+04 |
| optimistic_k10 | 0.281 | 238 | 1.07e+05 | 1 – 4.64e+04 | 0.100 | 0.054 | 1.75e+04 |
| optimistic_k2 | 0.751 | 635 | 2.84e+05 | 2.69 – 1.24e+05 | 0.064 | 0.040 | 4.67e+04 |
| optimistic_k3 | 0.655 | 554 | 2.48e+05 | 2.34 – 1.08e+05 | 0.069 | 0.042 | 4.08e+04 |
| optimistic_k5 | 0.505 | 427 | 1.91e+05 | 1.81 – 8.34e+04 | 0.077 | 0.046 | 3.15e+04 |

## nathan_headline: effect of each new factor (paired draws: per comparison (see table))

| comparison | median N_now of comparison | nathan_headline median / comparison median | per-sample log10(N_headline/N_comparison): median [10th, 90th] |
|---|---|---|---|
| without superhabitability (tool-use change only) | 2.61e+03 | ×1.07 | 0.016 [0.002, 0.074] |
| without cross-lineage tool use (superhab only) | 719 | ×3.89 | 0.598 [0.328, 0.788] |
| without both (= similarity_weighted, v1 model) | 888 | ×3.15 | n/a (independent draws; compare medians) |

## Multi-spectral breakdown (v2 model: M/K/G/F host classes)

Each host type has its own star fraction (RECONS / Kroupa IMF), eta-Earth, habitable window, exomoon-host giants, activity/UV/tidal penalties, similarity weight (own Archive ESI list if >= 3 HZ rocky planets, else pooled) and, for K only, the superhabitability boost. Share = that type's fraction of the posterior-mean N_now; median share = per-sample median.

| scenario | host type | median N_now | 10th–90th | mean | P(N<1) | share of mean N | median share [10th, 90th] | median N_ever | best-estimate N_now | similarity weight (median) |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | M | 2.31e-04 | 4.13e-08 – 1.1 | 616 | 0.898 | 35.6% | 13.0% [1.9, 52.2] | 0.122 | 460 | – |
| baseline | K | 0.00141 | 2.91e-07 – 5.47 | 1.01e+03 | 0.847 | 58.5% | 77.8% [41.8, 94.3] | 0.745 | 2.76e+03 | – |
| baseline | G | 6.29e-05 | 1.23e-08 – 0.28 | 101 | 0.932 | 5.8% | 3.7% [0.5, 18.1] | 0.102 | 266 | – |
| baseline | F | 5.82e-08 | 7.88e-12 – 4.02e-04 | 1.14 | 0.994 | 0.1% | 0.0% [0.0, 0.1] | 3.50e-04 | 1.05 | – |
| baseline | **all** | 0.00204 | 4.33e-07 – 7.99 | 1.73e+03 | 0.832 | 100% | – | 1.18 | 3.49e+03 | – |
| baseline_no_exomoons | M | 1.87e-04 | 3.42e-08 – 0.901 | 527 | 0.903 | 36.1% | 13.6% [2.1, 53.3] | 0.102 | 451 | – |
| baseline_no_exomoons | K | 0.00108 | 2.30e-07 – 4.29 | 849 | 0.855 | 58.2% | 76.9% [40.6, 94.2] | 0.605 | 2.71e+03 | – |
| baseline_no_exomoons | G | 4.94e-05 | 9.35e-09 – 0.229 | 83.4 | 0.936 | 5.7% | 3.6% [0.4, 18.8] | 0.0806 | 261 | – |
| baseline_no_exomoons | F | 4.14e-08 | 5.15e-12 – 2.88e-04 | 0.816 | 0.995 | 0.1% | 0.0% [0.0, 0.1] | 2.53e-04 | 0.995 | – |
| baseline_no_exomoons | **all** | 0.00161 | 3.34e-07 – 6.54 | 1.46e+03 | 0.840 | 100% | – | 0.92 | 3.42e+03 | – |
| nathan_headline | M | 277 | 1.05 – 5.94e+04 | 1.88e+05 | 0.098 | 25.8% | 11.5% [1.7, 49.3] | 5.08e+03 | 1.96e+03 | 0.849 |
| nathan_headline | K | 1.82e+03 | 9 – 2.87e+05 | 4.72e+05 | 0.034 | 64.9% | 72.7% [40.6, 90.0] | 3.23e+04 | 1.25e+04 | 0.841 |
| nathan_headline | G | 244 | 1.23 – 3.81e+04 | 6.69e+04 | 0.091 | 9.2% | 9.4% [2.7, 25.9] | 1.02e+04 | 1.22e+03 | 0.85 |
| nathan_headline | F | 1.62 | 0.0065 – 319 | 915 | 0.456 | 0.1% | 0.1% [0.0, 0.6] | 472 | 6.38 | 0.85 |
| nathan_headline | **all** | 2.79e+03 | 13.8 – 4.36e+05 | 7.27e+05 | 0.027 | 100% | – | 5.66e+04 | 1.57e+04 | – |
| nathan_headline_no_superhab | M | 277 | 1.05 – 5.94e+04 | 1.88e+05 | 0.098 | 27.6% | 12.3% [1.8, 51.3] | 5.08e+03 | 1.96e+03 | 0.849 |
| nathan_headline_no_superhab | K | 1.66e+03 | 8.24 – 2.61e+05 | 4.24e+05 | 0.036 | 62.4% | 70.8% [38.4, 89.1] | 2.93e+04 | 1.16e+04 | 0.841 |
| nathan_headline_no_superhab | G | 244 | 1.23 – 3.81e+04 | 6.69e+04 | 0.091 | 9.8% | 10.0% [2.9, 27.4] | 1.02e+04 | 1.22e+03 | 0.85 |
| nathan_headline_no_superhab | F | 1.62 | 0.0065 – 319 | 915 | 0.456 | 0.1% | 0.1% [0.0, 0.6] | 472 | 6.38 | 0.85 |
| nathan_headline_no_superhab | **all** | 2.61e+03 | 13 – 4.09e+05 | 6.80e+05 | 0.028 | 100% | – | 5.37e+04 | 1.48e+04 | – |
| nathan_headline_no_tooluse | M | 72.6 | 0.23 – 1.9e+04 | 8.32e+04 | 0.170 | 26.0% | 11.5% [1.7, 49.4] | 4.76e+03 | 391 | 0.849 |
| nathan_headline_no_tooluse | K | 471 | 1.98 – 9.25e+04 | 2.09e+05 | 0.074 | 65.2% | 73.1% [40.8, 90.4] | 3.03e+04 | 2.49e+03 | 0.841 |
| nathan_headline_no_tooluse | G | 60.5 | 0.258 – 1.18e+04 | 2.8e+04 | 0.169 | 8.7% | 9.0% [2.5, 25.5] | 9.44e+03 | 226 | 0.85 |
| nathan_headline_no_tooluse | F | 0.312 | 0.00107 – 76.8 | 328 | 0.604 | 0.1% | 0.0% [0.0, 0.5] | 329 | 0.89 | 0.85 |
| nathan_headline_no_tooluse | **all** | 719 | 3.04 – 1.40e+05 | 3.21e+05 | 0.061 | 100% | – | 5.29e+04 | 3.11e+03 | – |

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
| baseline | lithic | 0.00128 | 3.34e-07 – 4.05 | 1.11e+03 | 0.853 | 0.969 [0.203, 0.999] | 2.46e+03 |
| baseline | agricultural | 2.30e-06 | 4.94e-10 – 0.00948 | 5 | 0.981 | 0.00115 [1.15e-04, 0.0127] | 7.45 |
| baseline | industrial | 2.91e-08 | 4.28e-12 – 1.23e-04 | 0.0697 | 0.998 | 1.33e-05 [9.86e-07, 1.90e-04] | 0.0903 |
| baseline | radio | 1.82e-08 | 2.70e-12 – 9.16e-05 | 0.0643 | 0.998 | 8.73e-06 [5.07e-07, 1.57e-04] | 0.0729 |
| baseline | spacefaring | 2.86e-05 | 1.47e-09 – 0.584 | 612 | 0.911 | 0.0208 [1.51e-04, 0.794] | 1.01e+03 |
| baseline | **radio-capable (radio + spacefaring)** | 3.01e-05 | 1.56e-09 – 0.595 | 612 | 0.911 | – | 1.01e+03 |
| baseline_no_exomoons | lithic | 0.00102 | 2.63e-07 – 3.27 | 909 | 0.861 | 0.969 [0.203, 0.999] | 2.42e+03 |
| baseline_no_exomoons | agricultural | 1.81e-06 | 3.68e-10 – 0.00758 | 3.08 | 0.982 | 0.00115 [1.15e-04, 0.0127] | 7.31 |
| baseline_no_exomoons | industrial | 2.30e-08 | 3.35e-12 – 1.05e-04 | 0.0368 | 0.998 | 1.33e-05 [9.86e-07, 1.90e-04] | 0.0886 |
| baseline_no_exomoons | radio | 1.46e-08 | 2.13e-12 – 7.44e-05 | 0.0491 | 0.998 | 8.73e-06 [5.07e-07, 1.57e-04] | 0.0715 |
| baseline_no_exomoons | spacefaring | 2.31e-05 | 1.11e-09 – 0.466 | 548 | 0.915 | 0.0208 [1.51e-04, 0.794] | 994 |
| baseline_no_exomoons | **radio-capable (radio + spacefaring)** | 2.43e-05 | 1.19e-09 – 0.476 | 548 | 0.915 | – | 994 |
| nathan_headline | lithic | 1.75e+03 | 10.6 – 2.46e+05 | 4.40e+05 | 0.029 | 0.969 [0.201, 0.999] | 1.11e+04 |
| nathan_headline | agricultural | 3.33 | 0.0138 – 627 | 1.85e+03 | 0.390 | 0.00116 [1.14e-04, 0.0128] | 33.5 |
| nathan_headline | industrial | 0.0376 | 1.33e-04 – 7.74 | 25.1 | 0.780 | 1.33e-05 [9.64e-07, 1.84e-04] | 0.406 |
| nathan_headline | radio | 0.0247 | 7.22e-05 – 6.15 | 50.9 | 0.801 | 8.52e-06 [5.00e-07, 1.55e-04] | 0.328 |
| nathan_headline | spacefaring | 43.8 | 0.0203 – 5.79e+04 | 2.86e+05 | 0.271 | 0.0206 [1.47e-04, 0.796] | 4.56e+03 |
| nathan_headline | **radio-capable (radio + spacefaring)** | 45.5 | 0.0228 – 5.8e+04 | 2.86e+05 | 0.266 | – | 4.56e+03 |
| nathan_headline_no_superhab | lithic | 1.64e+03 | 9.9 – 2.31e+05 | 4.11e+05 | 0.030 | 0.969 [0.201, 0.999] | 1.05e+04 |
| nathan_headline_no_superhab | agricultural | 3.12 | 0.0129 – 588 | 1.73e+03 | 0.396 | 0.00116 [1.14e-04, 0.0128] | 31.7 |
| nathan_headline_no_superhab | industrial | 0.0353 | 1.25e-04 – 7.26 | 23.4 | 0.785 | 1.33e-05 [9.64e-07, 1.84e-04] | 0.383 |
| nathan_headline_no_superhab | radio | 0.0231 | 6.77e-05 – 5.76 | 47.8 | 0.805 | 8.52e-06 [5.00e-07, 1.55e-04] | 0.31 |
| nathan_headline_no_superhab | spacefaring | 41 | 0.019 – 5.43e+04 | 2.67e+05 | 0.275 | 0.0206 [1.47e-04, 0.796] | 4.31e+03 |
| nathan_headline_no_superhab | **radio-capable (radio + spacefaring)** | 42.6 | 0.0214 – 5.44e+04 | 2.67e+05 | 0.270 | – | 4.31e+03 |
| nathan_headline_no_tooluse | lithic | 454 | 2.43 – 7.57e+04 | 1.73e+05 | 0.066 | 0.969 [0.201, 0.999] | 2.2e+03 |
| nathan_headline_no_tooluse | agricultural | 0.881 | 0.00316 – 186 | 584 | 0.512 | 0.00116 [1.14e-04, 0.0128] | 6.65 |
| nathan_headline_no_tooluse | industrial | 0.01 | 3.05e-05 – 2.28 | 7.87 | 0.859 | 1.33e-05 [9.64e-07, 1.84e-04] | 0.0805 |
| nathan_headline_no_tooluse | radio | 0.0065 | 1.65e-05 – 1.81 | 16.4 | 0.873 | 8.52e-06 [5.00e-07, 1.55e-04] | 0.065 |
| nathan_headline_no_tooluse | spacefaring | 10.8 | 0.00449 – 1.98e+04 | 1.47e+05 | 0.354 | 0.0206 [1.47e-04, 0.796] | 904 |
| nathan_headline_no_tooluse | **radio-capable (radio + spacefaring)** | 11.2 | 0.00499 – 1.98e+04 | 1.47e+05 | 0.350 | – | 904 |

Radio-capable N vs classic SETI-style Drake: Sandberg, Drexler & Ord 2018's 'current knowledge' sketch gives median N = 0.32, mean 27 million, P(N<1) = 52% (communicating civilisations; their Table 1). This model's static SDO-style stone-age variant: median 28.8.

| scenario | median episode length (yr) [10th, 90th] | radio-capable: median NN distance (ly) | top drivers of radio-capable N (swing, dex) |
|---|---|---|---|
| baseline | 1.20e+06 [3.15e+04, 1.85e+07] | 7.59e+06 (N<1) | l_stone_yr 4.4; tau_stone_tool_intelligence 4.3; f_land_and_ocean 3.7; stage_h_space_per_yr 3.1; tau_abiogenesis 2.7 |
| baseline_no_exomoons | 1.20e+06 [3.15e+04, 1.85e+07] | 8.44e+06 (N<1) | l_stone_yr 4.4; tau_stone_tool_intelligence 4.3; f_land_and_ocean 3.7; stage_h_space_per_yr 3.1; tau_abiogenesis 2.7 |
| nathan_headline | 1.21e+06 [3.11e+04, 1.84e+07] | 6.17e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; f_land_and_ocean 3.3; f_plate_tectonics 1.8; m_recurrence 1.4 |
| nathan_headline_no_superhab | 1.21e+06 [3.11e+04, 1.84e+07] | 6.38e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; f_land_and_ocean 3.4; f_plate_tectonics 1.8; m_recurrence 1.4 |
| nathan_headline_no_tooluse | 1.21e+06 [3.11e+04, 1.84e+07] | 1.24e+04 | l_stone_yr 4.5; stage_h_space_per_yr 3.4; f_land_and_ocean 3.4; f_plate_tectonics 1.8; m_recurrence 1.6 |

## Spacing: equal-cube side and median nearest-neighbour distance (disk volume ~7.9e12 ly³, user-supplied)

Cube side = (V/N)^(1/3). Nearest-neighbour: random (Poisson) placement; 3D median r = (3 ln2/(4πn))^(1/3), or the thin-disk 2D form when r exceeds the 1,000-ly thickness (R = 50,000 ly). Values for N < 1 mean no neighbour is expected; they are shown only formally.

| scenario | median N | cube side at median (ly) | median NN distance at median (ly) | regime | NN at 90th-pct N (ly) | NN at 10th-pct N (ly) |
|---|---|---|---|---|---|---|
| baseline | 0.00204 | 1.57e+05 | 9.22e+05 (N<1: none expected) | 2D thin disk | 1.47e+04 | 6.32e+07 (N<1: none expected) |
| baseline_no_exomoons | 0.00161 | 1.70e+05 | 1.04e+06 (N<1: none expected) | 2D thin disk | 1.63e+04 | 7.20e+07 (N<1: none expected) |
| snyder_beattie_priors | 5.45e-21 | 1.13e+11 | 5.64e+14 (N<1: none expected) | 2D thin disk | 1.29e+10 (N<1: none expected) | 2.21e+19 (N<1: none expected) |
| user_inputs | 9.90e-05 | 4.30e+05 | 4.18e+06 (N<1: none expected) | 2D thin disk | 8.33e+04 (N<1: none expected) | 2.10e+08 (N<1: none expected) |
| user_fast_intelligence | 569 | 2.4e+03 | 1.74e+03 | 2D thin disk | 185 | 4.86e+04 (N<1: none expected) |
| similarity_weighted | 888 | 2.07e+03 | 1.4e+03 | 2D thin disk | 185 | 2.55e+04 |
| similarity_weighted_no_rare_earth | 1.89e+07 | 74.8 | 41.1 | 3D | 13.5 | 196 |
| earth_random_draw | 156 | 3.7e+03 | 3.34e+03 | 2D thin disk | 282 | 8.8e+04 (N<1: none expected) |
| nathan_headline | 2.79e+03 | 1.41e+03 | 776 | 3D | 144 | 1.12e+04 |
| nathan_headline_no_superhab | 2.61e+03 | 1.45e+03 | 794 | 3D | 147 | 1.15e+04 |
| nathan_headline_no_tooluse | 719 | 2.22e+03 | 1.55e+03 | 2D thin disk | 210 | 2.39e+04 |
| classic_static_SDO_style | 28.8 | 6.49e+03 | 7.75e+03 | 2D thin disk | 95.7 | 2.35e+34 (N<1: none expected) |

## Comparison with the user's claims

| scenario | median N_now | P(1<=N_now<=3) ('1-3 at a time') | P(N_now>=1) | median N_ever by now | P(50<=N_ever<=100) | P(N_ever>=50) |
|---|---|---|---|---|---|---|
| baseline | 0.00204 | 0.041 | 0.168 | 1.18 | 0.038 | 0.245 |
| baseline_no_exomoons | 0.00161 | 0.040 | 0.160 | 0.92 | 0.036 | 0.234 |
| snyder_beattie_priors | 5.45e-21 | 0.000 | 0.001 | 4.71e-18 | 0.000 | 0.001 |
| user_inputs | 9.90e-05 | 0.021 | 0.066 | 0.873 | 0.039 | 0.233 |
| user_fast_intelligence | 569 | 0.042 | 0.890 | 965 | 0.047 | 0.723 |
| similarity_weighted | 888 | 0.038 | 0.933 | 4.39e+04 | 0.014 | 0.982 |
| similarity_weighted_no_rare_earth | 1.89e+07 | 0.000 | 1.000 | 7.86e+08 | 0.000 | 1.000 |
| earth_random_draw | 156 | 0.058 | 0.841 | 1.2e+04 | 0.030 | 0.924 |
| nathan_headline | 2.79e+03 | 0.022 | 0.973 | 5.66e+04 | 0.011 | 0.987 |
| nathan_headline_no_superhab | 2.61e+03 | 0.023 | 0.972 | 5.37e+04 | 0.012 | 0.986 |
| nathan_headline_no_tooluse | 719 | 0.039 | 0.939 | 5.29e+04 | 0.012 | 0.985 |

## Exomoon effect (paired, same draws)
Median N_now with exomoons 0.00204 vs without 0.00161; per-sample log10(N_with/N_without): median 0.008 dex, 90th pct 0.317, 99th pct 1.083. Median share of habitable bodies that are moons: M 0.0111, K 0.0195, G 0.0177, F 0.0341.


## Deterministic best-estimate point calculations

All parameters at their `best` values; hard-step expected times set equal to Earth's observed intervals (a 'Copernican / Earth-is-typical' choice).

| scenario | N_now | time-avg N | N_ever by now | fraction from Sun-like hosts (v1: G/K; v2: F/G/K) |
|---|---|---|---|---|
| baseline | 3.49e+03 | 1.28e+03 | 8.27e+04 | 0.868 |
| baseline_no_exomoons | 3.42e+03 | 1.25e+03 | 8.12e+04 | 0.868 |
| snyder_beattie_priors | 3.28e+03 | 1.92e+03 | 8.25e+04 | 0.734 |
| user_inputs | 86.3 | 41.7 | 8.63e+04 | 0.821 |
| user_fast_intelligence | 5.43e+04 | 2.79e+04 | 9.17e+04 | 0.826 |
| similarity_weighted | 2.78e+03 | 1.63e+03 | 7.01e+04 | 0.734 |
| similarity_weighted_no_rare_earth | 5.58e+06 | 3.27e+06 | 1.41e+08 | 0.734 |
| earth_random_draw | 3.28e+03 | 1.92e+03 | 8.25e+04 | 0.734 |
| nathan_headline | 1.57e+04 | 6.1e+03 | 7.74e+04 | 0.875 |
| nathan_headline_no_superhab | 1.48e+04 | 5.79e+03 | 7.38e+04 | 0.868 |
| nathan_headline_no_tooluse | 3.11e+03 | 1.14e+03 | 7.32e+04 | 0.874 |

## Sensitivity — baseline

ESS = 13586 of 200000 samples. Median share of N_now from G/K hosts: 0.87. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.476 | -0.61 | -4.76 | 4.15 |
| f_land_and_ocean | +0.370 | -4.50 | -0.86 | 3.64 |
| l_stone_yr | +0.289 | -4.39 | -1.76 | 2.63 |
| tau_abiogenesis | -0.269 | -1.76 | -4.37 | 2.61 |
| tau_complex_multicellularity | -0.269 | -1.56 | -4.12 | 2.56 |
| tau_eukaryogenesis | -0.267 | -1.67 | -4.10 | 2.43 |
| tau_oxygenic_photosynthesis_GOE | -0.262 | -1.58 | -3.90 | 2.32 |
| r_ster0_per_gyr | -0.163 | -2.18 | -4.00 | 1.82 |
| f_plate_tectonics | +0.188 | -3.68 | -1.92 | 1.77 |
| f_large_moon | +0.134 | -3.42 | -2.02 | 1.40 |
| f_jupiter_shield | +0.099 | -3.15 | -2.22 | 0.93 |
| f_ghz | +0.106 | -3.08 | -2.24 | 0.84 |
| m_recurrence | -0.119 | -2.36 | -3.15 | 0.79 |
| ne_K | +0.038 | -2.99 | -2.42 | 0.57 |
| f_exomoon_host | +0.038 | -2.76 | -2.31 | 0.46 |

## Sensitivity — baseline_no_exomoons

ESS = 13586 of 200000 samples. Median share of N_now from G/K hosts: 0.864. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.474 | -0.69 | -4.84 | 4.15 |
| f_land_and_ocean | +0.369 | -4.59 | -1.00 | 3.60 |
| l_stone_yr | +0.288 | -4.52 | -1.88 | 2.64 |
| tau_abiogenesis | -0.268 | -1.83 | -4.46 | 2.63 |
| tau_complex_multicellularity | -0.269 | -1.66 | -4.19 | 2.52 |
| tau_eukaryogenesis | -0.267 | -1.77 | -4.22 | 2.45 |
| tau_oxygenic_photosynthesis_GOE | -0.261 | -1.65 | -4.00 | 2.34 |
| r_ster0_per_gyr | -0.161 | -2.29 | -4.08 | 1.80 |
| f_plate_tectonics | +0.187 | -3.74 | -2.00 | 1.74 |
| f_large_moon | +0.154 | -3.68 | -2.05 | 1.63 |
| f_jupiter_shield | +0.113 | -3.39 | -2.24 | 1.15 |
| f_ghz | +0.106 | -3.17 | -2.33 | 0.85 |
| m_recurrence | -0.119 | -2.42 | -3.26 | 0.84 |
| ne_K | +0.042 | -3.11 | -2.49 | 0.62 |
| r_sn_per_gyr | -0.027 | -2.62 | -3.01 | 0.40 |

## Sensitivity — snyder_beattie_priors

ESS = 3151 of 200000 samples. Median share of N_now from G/K hosts: 0.748. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.58 -> posterior 0.06; posterior P(tau_intelligence<5 Gyr) = 0.11.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.406 | -14.18 | -24.62 | 10.44 |
| tau_abiogenesis | -0.357 | -16.00 | -25.68 | 9.68 |
| tau_complex_multicellularity | -0.349 | -14.87 | -24.01 | 9.13 |
| tau_oxygenic_photosynthesis_GOE | -0.333 | -16.06 | -24.80 | 8.74 |
| tau_eukaryogenesis | -0.376 | -15.99 | -24.67 | 8.68 |
| f_land_and_ocean | +0.145 | -21.64 | -18.41 | 3.23 |
| l_stone_yr | +0.131 | -21.59 | -18.83 | 2.76 |
| ne_gk | +0.032 | -20.58 | -19.01 | 1.58 |
| th_gk_gyr | +0.052 | -21.19 | -19.79 | 1.40 |
| ne_m | -0.022 | -19.01 | -20.27 | 1.27 |
| f_jupiter_shield | +0.048 | -20.63 | -19.48 | 1.15 |
| f_plate_tectonics | +0.069 | -21.40 | -20.30 | 1.10 |
| r_self_per_gyr | -0.022 | -20.87 | -19.86 | 1.02 |
| r_ster0_per_gyr | -0.028 | -20.11 | -21.10 | 0.98 |
| th_m_gyr | -0.023 | -19.74 | -20.64 | 0.89 |

## Sensitivity — user_inputs

ESS = 34101 of 500000 samples. Median share of N_now from G/K hosts: 0.702. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.507 | -1.73 | -6.03 | 4.30 |
| f_land_and_ocean | +0.381 | -5.68 | -2.39 | 3.29 |
| tau_eukaryogenesis | -0.292 | -2.85 | -5.45 | 2.60 |
| tau_abiogenesis | -0.295 | -2.99 | -5.55 | 2.55 |
| tau_oxygenic_photosynthesis_GOE | -0.272 | -2.79 | -5.31 | 2.52 |
| tau_complex_multicellularity | -0.281 | -2.92 | -5.32 | 2.40 |
| f_plate_tectonics | +0.201 | -4.84 | -3.19 | 1.65 |
| f_large_moon | +0.156 | -4.70 | -3.26 | 1.45 |
| r_ster0_per_gyr | -0.122 | -3.72 | -5.05 | 1.33 |
| f_jupiter_shield | +0.106 | -4.49 | -3.48 | 1.02 |
| f_ghz | +0.104 | -4.54 | -3.55 | 0.98 |
| m_recurrence | -0.129 | -3.38 | -4.31 | 0.92 |
| l_stone_yr | +0.058 | -4.31 | -3.75 | 0.56 |
| f_m_flares | +0.054 | -4.18 | -3.65 | 0.53 |
| ne_gk | +0.051 | -4.26 | -3.75 | 0.51 |

## Sensitivity — user_fast_intelligence

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.78. Median epoch of peak N(t): 0.15 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.50; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.510 | 1.13 | 4.49 | 3.36 |
| tau_eukaryogenesis | -0.309 | 3.31 | 1.09 | 2.22 |
| tau_abiogenesis | -0.309 | 3.31 | 1.10 | 2.21 |
| tau_oxygenic_photosynthesis_GOE | -0.311 | 3.30 | 1.10 | 2.19 |
| tau_complex_multicellularity | -0.311 | 3.30 | 1.11 | 2.19 |
| f_plate_tectonics | +0.268 | 1.87 | 3.67 | 1.80 |
| f_large_moon | +0.189 | 2.19 | 3.46 | 1.28 |
| r_ster0_per_gyr | -0.144 | 3.04 | 1.92 | 1.12 |
| f_jupiter_shield | +0.136 | 2.31 | 3.24 | 0.93 |
| f_ghz | +0.134 | 2.31 | 3.22 | 0.91 |
| f_exomoon_host | +0.062 | 2.63 | 3.12 | 0.49 |
| ne_gk | +0.071 | 2.55 | 2.99 | 0.45 |
| f_m_flares | +0.059 | 2.62 | 3.00 | 0.38 |
| f_m_habitable | +0.056 | 2.61 | 2.98 | 0.37 |
| m_disk_now | +0.029 | 2.61 | 2.86 | 0.25 |

## Sensitivity — similarity_weighted

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.824. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.569 | 1.33 | 4.64 | 3.31 |
| l_stone_yr | +0.557 | 0.99 | 4.12 | 3.13 |
| f_plate_tectonics | +0.299 | 2.06 | 3.84 | 1.77 |
| m_recurrence | -0.242 | 3.62 | 2.15 | 1.47 |
| f_large_moon | +0.208 | 2.31 | 3.59 | 1.28 |
| r_ster0_per_gyr | -0.161 | 3.25 | 2.17 | 1.08 |
| f_ghz | +0.149 | 2.49 | 3.41 | 0.92 |
| f_jupiter_shield | +0.151 | 2.50 | 3.42 | 0.92 |
| ne_gk | +0.086 | 2.70 | 3.21 | 0.51 |
| f_exomoon_host | +0.065 | 2.84 | 3.33 | 0.49 |
| th_gk_gyr | +0.079 | 2.65 | 3.08 | 0.43 |
| f_m_habitable | +0.063 | 2.80 | 3.19 | 0.38 |
| f_m_flares | +0.054 | 2.84 | 3.17 | 0.33 |
| stars_per_msun | +0.037 | 2.83 | 3.04 | 0.20 |
| m_disk_now | +0.032 | 2.84 | 3.04 | 0.20 |

## Sensitivity — similarity_weighted_no_rare_earth

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.809. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| l_stone_yr | +0.802 | 5.19 | 8.36 | 3.16 |
| m_recurrence | -0.342 | 7.97 | 6.49 | 1.47 |
| r_ster0_per_gyr | -0.230 | 7.58 | 6.51 | 1.07 |
| f_ghz | +0.215 | 6.84 | 7.74 | 0.90 |
| ne_gk | +0.144 | 7.00 | 7.59 | 0.59 |
| th_gk_gyr | +0.117 | 6.97 | 7.42 | 0.46 |
| f_m_flares | +0.086 | 7.13 | 7.51 | 0.38 |
| f_m_habitable | +0.093 | 7.14 | 7.51 | 0.37 |
| r_self_per_gyr | -0.048 | 7.34 | 7.11 | 0.23 |
| stars_per_msun | +0.053 | 7.16 | 7.37 | 0.21 |
| m_disk_now | +0.045 | 7.16 | 7.35 | 0.19 |
| f_gk | +0.035 | 7.21 | 7.33 | 0.12 |
| sfr_now | +0.016 | 7.22 | 7.32 | 0.11 |
| ne_m | +0.024 | 7.23 | 7.33 | 0.10 |
| f_early_disk_mass | -0.009 | 7.32 | 7.24 | 0.08 |

## Sensitivity — earth_random_draw

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.799. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.61 -> posterior 0.61; posterior P(tau_intelligence<5 Gyr) = 0.89.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.507 | 0.59 | 3.87 | 3.28 |
| l_stone_yr | +0.510 | 0.21 | 3.39 | 3.18 |
| tau_stone_tool_intelligence | -0.269 | 2.94 | 0.68 | 2.26 |
| f_plate_tectonics | +0.271 | 1.28 | 3.10 | 1.82 |
| m_recurrence | -0.207 | 2.90 | 1.47 | 1.42 |
| r_ster0_per_gyr | -0.162 | 2.52 | 1.27 | 1.25 |
| f_large_moon | +0.189 | 1.60 | 2.84 | 1.24 |
| tau_oxygenic_photosynthesis_GOE | -0.128 | 2.43 | 1.36 | 1.08 |
| tau_complex_multicellularity | -0.118 | 2.45 | 1.40 | 1.05 |
| f_ghz | +0.132 | 1.75 | 2.65 | 0.90 |
| f_jupiter_shield | +0.134 | 1.77 | 2.66 | 0.88 |
| tau_eukaryogenesis | -0.085 | 2.36 | 1.55 | 0.81 |
| tau_abiogenesis | -0.075 | 2.31 | 1.57 | 0.73 |
| th_gk_gyr | +0.094 | 1.79 | 2.39 | 0.60 |
| ne_gk | +0.075 | 1.97 | 2.43 | 0.47 |

## Sensitivity — nathan_headline

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.885. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.621 | 1.80 | 5.15 | 3.35 |
| l_stone_yr | +0.429 | 1.82 | 4.20 | 2.38 |
| f_plate_tectonics | +0.327 | 2.51 | 4.33 | 1.81 |
| m_recurrence | -0.257 | 4.07 | 2.66 | 1.41 |
| f_large_moon | +0.234 | 2.80 | 4.11 | 1.31 |
| r_ster0_per_gyr | -0.187 | 3.76 | 2.60 | 1.16 |
| f_jupiter_shield | +0.164 | 3.02 | 3.93 | 0.91 |
| f_ghz | +0.164 | 3.00 | 3.88 | 0.87 |
| f_exomoon_host | +0.061 | 3.37 | 3.75 | 0.38 |
| stage_tau_agri_yr | +0.058 | 3.28 | 3.58 | 0.30 |
| stage_h_space_per_yr | -0.062 | 3.61 | 3.34 | 0.27 |
| n_tool_origins | +0.047 | 3.31 | 3.57 | 0.27 |
| tau_stone_tool_intelligence | -0.047 | 3.57 | 3.31 | 0.27 |
| f_m_habitable | +0.042 | 3.37 | 3.63 | 0.26 |
| f_m_flares | +0.043 | 3.36 | 3.61 | 0.26 |

## Sensitivity — nathan_headline_no_superhab

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.877. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.621 | 1.78 | 5.12 | 3.35 |
| l_stone_yr | +0.429 | 1.79 | 4.17 | 2.38 |
| f_plate_tectonics | +0.327 | 2.49 | 4.30 | 1.81 |
| m_recurrence | -0.258 | 4.05 | 2.63 | 1.41 |
| f_large_moon | +0.232 | 2.78 | 4.08 | 1.30 |
| r_ster0_per_gyr | -0.186 | 3.73 | 2.58 | 1.15 |
| f_jupiter_shield | +0.163 | 3.00 | 3.90 | 0.90 |
| f_ghz | +0.163 | 2.97 | 3.85 | 0.88 |
| f_exomoon_host | +0.063 | 3.33 | 3.73 | 0.40 |
| stage_tau_agri_yr | +0.058 | 3.25 | 3.55 | 0.30 |
| f_m_habitable | +0.044 | 3.34 | 3.61 | 0.27 |
| stage_h_space_per_yr | -0.062 | 3.58 | 3.31 | 0.27 |
| n_tool_origins | +0.047 | 3.28 | 3.55 | 0.27 |
| tau_stone_tool_intelligence | -0.047 | 3.55 | 3.28 | 0.27 |
| f_m_flares | +0.045 | 3.33 | 3.59 | 0.26 |

## Sensitivity — nathan_headline_no_tooluse

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.885. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.597 | 1.20 | 4.56 | 3.35 |
| l_stone_yr | +0.465 | 1.13 | 3.76 | 2.63 |
| f_plate_tectonics | +0.314 | 1.93 | 3.74 | 1.82 |
| m_recurrence | -0.283 | 3.63 | 2.01 | 1.62 |
| f_large_moon | +0.225 | 2.21 | 3.52 | 1.31 |
| r_ster0_per_gyr | -0.186 | 3.18 | 1.98 | 1.21 |
| f_jupiter_shield | +0.158 | 2.44 | 3.34 | 0.90 |
| f_ghz | +0.157 | 2.41 | 3.29 | 0.88 |
| f_exomoon_host | +0.058 | 2.79 | 3.17 | 0.38 |
| stage_tau_agri_yr | +0.069 | 2.66 | 3.02 | 0.36 |
| stage_h_space_per_yr | -0.077 | 3.08 | 2.73 | 0.35 |
| f_m_habitable | +0.041 | 2.79 | 3.05 | 0.26 |
| stars_per_msun | +0.040 | 2.74 | 2.98 | 0.24 |
| f_m_flares | +0.041 | 2.78 | 3.02 | 0.24 |
| ne_K | +0.042 | 2.75 | 2.99 | 0.24 |
