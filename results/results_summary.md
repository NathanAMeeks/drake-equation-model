# Results — time-aware extended Drake model (stone-age-or-greater)

**Headline scenario: `nathan_headline_ocean_linked_v8`** (user-approved). Literature baseline for comparison: `baseline_ocean_linked_v8`.

Model versions: **v2** (multi-spectral M/K/G/F host classes + multiphase civilisation stages) for `baseline`, `baseline_no_exomoons`, `nathan_headline`, `nathan_headline_no_superhab`, `nathan_headline_no_tooluse`, `nathan_headline_ocean`, `baseline_ocean`, `nathan_headline_ocean_linked`, `baseline_ocean_linked`, `nathan_headline_ocean_linked_v5`, `baseline_ocean_linked_v5`, `nathan_headline_ocean_linked_v8`, `baseline_ocean_linked_v8`; all other scenarios are **v1** (two host classes G/K + M, single stone-age-or-greater phase). v1 numbers for the re-run scenarios are kept in results/v1/.

N = expected number of Milky Way worlds with stone-age-or-greater tool users alive at the same time (present day, other than Earth). Percentiles are over parameter uncertainty (posterior after the Earth-timing update where enabled).

| scenario | median (50/50) | mean | 10th pct | 90th pct | P(N<1) | P(no other, Poisson) | P(1<=N<=3) | time-avg N over history | median N_ever (by now) | ESS |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 0.00357 | 1.7e+03 | 8.58e-07 | 11.1 | 0.813 | 0.782 | 0.044 | median 6.70e-04 / mean 542 | 2.2 | 13890 |
| baseline_no_exomoons | 0.00295 | 1.55e+03 | 6.94e-07 | 8.94 | 0.822 | 0.792 | 0.043 | median 5.40e-04 / mean 503 | 1.77 | 13890 |
| snyder_beattie_priors | 1.60e-20 | 0.198 | 8.48e-30 | 2.56e-11 | 0.998 | 0.998 | 0.001 | median 4.31e-21 / mean 0.0464 | 1.89e-17 | 3184 |
| user_inputs | 1.08e-04 | 25.3 | 4.80e-08 | 0.266 | 0.932 | 0.914 | 0.022 | median 3.93e-05 / mean 11.4 | 1.43 | 13819 |
| user_fast_intelligence | 395 | 4.03e+05 | 0.503 | 1.40e+05 | 0.124 | 0.110 | 0.047 | median 184 / mean 2.62e+05 | 875 | 200000 |
| similarity_weighted | 656 | 3.25e+05 | 1.99 | 1.54e+05 | 0.076 | 0.066 | 0.041 | median 309 / mean 1.36e+05 | 3.91e+04 | 200000 |
| similarity_weighted_no_rare_earth | 1.70e+07 | 1.85e+08 | 1.57e+05 | 4.74e+08 | 0.000 | 0.000 | 0.000 | median 8.06e+06 / mean 7.75e+07 | 8.37e+08 | 200000 |
| earth_random_draw | 120 | 1.59e+05 | 0.183 | 4.4e+04 | 0.172 | 0.152 | 0.060 | median 47.1 / mean 5.98e+04 | 1.15e+04 | 200000 |
| nathan_headline | 2.39e+03 | 5.72e+05 | 12.8 | 3.55e+05 | 0.028 | 0.024 | 0.023 | median 924 / mean 2.24e+05 | 5.16e+04 | 200000 |
| nathan_headline_no_superhab | 2.21e+03 | 5.22e+05 | 11.8 | 3.26e+05 | 0.029 | 0.025 | 0.024 | median 859 / mean 2.06e+05 | 4.82e+04 | 200000 |
| nathan_headline_no_tooluse | 622 | 2.54e+05 | 2.81 | 1.15e+05 | 0.063 | 0.054 | 0.040 | median 229 / mean 9.36e+04 | 4.86e+04 | 200000 |
| nathan_headline_ocean | 2.82e+04 | 1.37e+06 | 294 | 1.62e+06 | 0.002 | 0.002 | 0.003 | median 1.09e+04 / mean 5.32e+05 | 5.87e+05 | 200000 |
| baseline_ocean | 0.0413 | 5.68e+03 | 1.45e-05 | 83.9 | 0.703 | 0.665 | 0.062 | median 0.00771 / mean 1.56e+03 | 27.1 | 13890 |
| nathan_headline_ocean_linked | 2.9e+04 | 1.64e+06 | 272 | 1.85e+06 | 0.002 | 0.002 | 0.003 | median 1.12e+04 / mean 6.40e+05 | 5.93e+05 | 200000 |
| baseline_ocean_linked | 0.043 | 4.77e+03 | 1.56e-05 | 95.9 | 0.701 | 0.664 | 0.059 | median 0.00783 / mean 1.3e+03 | 26.6 | 13890 |
| nathan_headline_ocean_linked_v5 | 1.57e+04 | 9.67e+05 | 165 | 1.02e+06 | 0.003 | 0.002 | 0.004 | median 5.58e+03 / mean 3.63e+05 | 5.35e+05 | 100000 |
| baseline_ocean_linked_v5 | 0.0403 | 2.34e+03 | 1.64e-05 | 80 | 0.702 | 0.666 | 0.061 | median 0.00638 / mean 613 | 22.9 | 6945 |
| nathan_headline_ocean_linked_v8 | 2.43e+04 | 8.93e+05 | 299 | 1.15e+06 | 0.001 | 0.001 | 0.003 | median 7.99e+03 / mean 3.07e+05 | 5.25e+05 | 100000 |
| baseline_ocean_linked_v8 | 0.0337 | 2.28e+03 | 1.44e-05 | 58.5 | 0.718 | 0.680 | 0.054 | median 0.00518 / mean 616 | 18.7 | 6945 |
| classic_static_SDO_style | 28.8 | 8.05e+06 | 3.14e-60 | 1.49e+06 | 0.465 | 0.463 | 0.007 | (static) | – | – |

## Worlds vs tool-using species (species_per_tool_world)

species_now = N_now x concurrent hominin-grade species per tool world (log-uniform 1-5, best 2.38, from Smithsonian date spans); species_ever = N_ever x cumulative species per tool world (uniform 8-16, best 15). The factor multiplies species, not worlds.

| scenario | median worlds now | median species now | species 10th-90th | mean species now | median worlds ever | median species ever | best-estimate species now |
|---|---|---|---|---|---|---|---|
| baseline | 0.00357 | 0.00794 | 1.79e-06 – 26.8 | 4.89e+03 | 2.2 | 26 | 7.88e+03 |
| baseline_no_exomoons | 0.00295 | 0.00621 | 1.42e-06 – 21.7 | 4.46e+03 | 1.77 | 21.4 | 7.73e+03 |
| snyder_beattie_priors | 1.60e-20 | 3.38e-20 | 2.03e-29 – 5.22e-11 | 0.462 | 1.89e-17 | 2.14e-16 | 5.4e+03 |
| user_inputs | 1.08e-04 | 2.52e-04 | 1.12e-07 – 0.63 | 55.9 | 1.43 | 16.8 | 166 |
| user_fast_intelligence | 395 | 887 | 1.1 – 3.18e+05 | 1.02e+06 | 875 | 1.03e+04 | 1.04e+05 |
| similarity_weighted | 656 | 1.47e+03 | 4.3 – 3.53e+05 | 8.04e+05 | 3.91e+04 | 4.60e+05 | 4.59e+03 |
| similarity_weighted_no_rare_earth | 1.70e+07 | 3.76e+07 | 3.40e+05 – 1.13e+09 | 4.60e+08 | 8.37e+08 | 9.85e+09 | 1.15e+07 |
| earth_random_draw | 120 | 267 | 0.394 – 1.02e+05 | 3.99e+05 | 1.15e+04 | 1.36e+05 | 5.4e+03 |
| nathan_headline | 2.39e+03 | 5.37e+03 | 27.6 – 8.20e+05 | 1.41e+06 | 5.16e+04 | 6.05e+05 | 3.54e+04 |
| nathan_headline_no_superhab | 2.21e+03 | 4.94e+03 | 25.5 – 7.56e+05 | 1.29e+06 | 4.82e+04 | 5.67e+05 | 3.32e+04 |
| nathan_headline_no_tooluse | 622 | 1.41e+03 | 6.08 – 2.65e+05 | 6.24e+05 | 4.86e+04 | 5.72e+05 | 7.08e+03 |
| nathan_headline_ocean | 2.82e+04 | 6.34e+04 | 633 – 3.76e+06 | 3.38e+06 | 5.87e+05 | 6.91e+06 | 2.35e+05 |
| baseline_ocean | 0.0413 | 0.0926 | 3.15e-05 – 187 | 1.86e+04 | 27.1 | 320 | 5.25e+04 |
| nathan_headline_ocean_linked | 2.9e+04 | 6.49e+04 | 583 – 4.30e+06 | 4.05e+06 | 5.93e+05 | 6.95e+06 | 2.35e+05 |
| baseline_ocean_linked | 0.043 | 0.0939 | 3.26e-05 – 212 | 1.43e+04 | 26.6 | 317 | 5.25e+04 |
| nathan_headline_ocean_linked_v5 | 1.57e+04 | 3.49e+04 | 353 – 2.37e+06 | 2.39e+06 | 5.35e+05 | 6.29e+06 | 1.22e+05 |
| baseline_ocean_linked_v5 | 0.0403 | 0.0899 | 3.43e-05 – 179 | 5.7e+03 | 22.9 | 261 | 4.13e+04 |
| nathan_headline_ocean_linked_v8 | 2.43e+04 | 5.36e+04 | 649 – 2.67e+06 | 2.20e+06 | 5.25e+05 | 6.16e+06 | 4.74e+05 |
| baseline_ocean_linked_v8 | 0.0337 | 0.0743 | 3.07e-05 – 141 | 5.47e+03 | 18.7 | 219 | 1.13e+05 |
| classic_static_SDO_style | 28.8 | 61.8 | 6.93e-60 – 3.40e+06 | 2.00e+07 | – | – | – |

## Similarity-weight variants — similarity_weighted

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 656 | 3.25e+05 | 1.99 – 1.54e+05 | 0.076 | 0.041 | 3.91e+04 |
| conservative_k10 | 0.243 | 186 | 9.3e+04 | 0.563 – 4.39e+04 | 0.124 | 0.056 | 1.11e+04 |
| conservative_k2 | 0.725 | 560 | 2.77e+05 | 1.7 – 1.32e+05 | 0.081 | 0.043 | 3.34e+04 |
| conservative_k3 | 0.623 | 481 | 2.38e+05 | 1.46 – 1.13e+05 | 0.086 | 0.045 | 2.86e+04 |
| conservative_k5 | 0.466 | 359 | 1.78e+05 | 1.09 – 8.46e+04 | 0.097 | 0.049 | 2.14e+04 |
| optimistic_k1 | 0.865 | 668 | 3.30e+05 | 2.03 – 1.57e+05 | 0.075 | 0.041 | 3.98e+04 |
| optimistic_k10 | 0.281 | 217 | 1.08e+05 | 0.657 – 5.13e+04 | 0.118 | 0.054 | 1.29e+04 |
| optimistic_k2 | 0.751 | 580 | 2.87e+05 | 1.76 – 1.37e+05 | 0.080 | 0.043 | 3.45e+04 |
| optimistic_k3 | 0.655 | 506 | 2.51e+05 | 1.53 – 1.19e+05 | 0.084 | 0.045 | 3.01e+04 |
| optimistic_k5 | 0.505 | 390 | 1.93e+05 | 1.18 – 9.21e+04 | 0.094 | 0.048 | 2.32e+04 |

## Similarity-weight variants — similarity_weighted_no_rare_earth

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 1.70e+07 | 1.85e+08 | 1.57e+05 – 4.74e+08 | 0.000 | 0.000 | 8.37e+08 |
| conservative_k10 | 0.243 | 4.83e+06 | 5.31e+07 | 4.45e+04 – 1.35e+08 | 0.000 | 0.000 | 2.37e+08 |
| conservative_k2 | 0.725 | 1.46e+07 | 1.58e+08 | 1.34e+05 – 4.04e+08 | 0.000 | 0.000 | 7.14e+08 |
| conservative_k3 | 0.623 | 1.25e+07 | 1.36e+08 | 1.15e+05 – 3.47e+08 | 0.000 | 0.000 | 6.13e+08 |
| conservative_k5 | 0.466 | 9.33e+06 | 1.02e+08 | 8.59e+04 – 2.60e+08 | 0.000 | 0.000 | 4.57e+08 |
| optimistic_k1 | 0.865 | 1.74e+07 | 1.88e+08 | 1.60e+05 – 4.82e+08 | 0.000 | 0.000 | 8.53e+08 |
| optimistic_k10 | 0.281 | 5.63e+06 | 6.14e+07 | 5.16e+04 – 1.57e+08 | 0.000 | 0.000 | 2.76e+08 |
| optimistic_k2 | 0.751 | 1.51e+07 | 1.64e+08 | 1.39e+05 – 4.19e+08 | 0.000 | 0.000 | 7.41e+08 |
| optimistic_k3 | 0.655 | 1.32e+07 | 1.43e+08 | 1.21e+05 – 3.66e+08 | 0.000 | 0.000 | 6.46e+08 |
| optimistic_k5 | 0.505 | 1.01e+07 | 1.10e+08 | 9.32e+04 – 2.82e+08 | 0.000 | 0.000 | 4.98e+08 |

## Similarity-weight variants — nathan_headline

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.39e+03 | 5.72e+05 | 12.8 – 3.55e+05 | 0.028 | 0.023 | 5.16e+04 |
| conservative_k10 | 0.243 | 679 | 1.65e+05 | 3.65 – 1.01e+05 | 0.055 | 0.037 | 1.47e+04 |
| conservative_k2 | 0.725 | 2.04e+03 | 4.89e+05 | 10.9 – 3.03e+05 | 0.031 | 0.025 | 4.4e+04 |
| conservative_k3 | 0.623 | 1.75e+03 | 4.20e+05 | 9.4 – 2.59e+05 | 0.033 | 0.027 | 3.78e+04 |
| conservative_k5 | 0.466 | 1.31e+03 | 3.15e+05 | 7.03 – 1.94e+05 | 0.039 | 0.030 | 2.82e+04 |
| optimistic_k1 | 0.865 | 2.43e+03 | 5.82e+05 | 13.1 – 3.61e+05 | 0.028 | 0.023 | 5.25e+04 |
| optimistic_k10 | 0.281 | 789 | 1.89e+05 | 4.24 – 1.17e+05 | 0.051 | 0.035 | 1.7e+04 |
| optimistic_k2 | 0.751 | 2.11e+03 | 5.05e+05 | 11.3 – 3.13e+05 | 0.030 | 0.024 | 4.56e+04 |
| optimistic_k3 | 0.655 | 1.84e+03 | 4.41e+05 | 9.9 – 2.73e+05 | 0.032 | 0.026 | 3.98e+04 |
| optimistic_k5 | 0.505 | 1.42e+03 | 3.40e+05 | 7.62 – 2.10e+05 | 0.037 | 0.028 | 3.07e+04 |

## Similarity-weight variants — nathan_headline_no_superhab

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.21e+03 | 5.22e+05 | 11.8 – 3.26e+05 | 0.029 | 0.024 | 4.82e+04 |
| conservative_k10 | 0.243 | 626 | 1.51e+05 | 3.37 – 9.29e+04 | 0.058 | 0.038 | 1.37e+04 |
| conservative_k2 | 0.725 | 1.88e+03 | 4.46e+05 | 10.1 – 2.79e+05 | 0.032 | 0.026 | 4.11e+04 |
| conservative_k3 | 0.623 | 1.62e+03 | 3.83e+05 | 8.67 – 2.39e+05 | 0.035 | 0.027 | 3.52e+04 |
| conservative_k5 | 0.466 | 1.21e+03 | 2.87e+05 | 6.47 – 1.78e+05 | 0.041 | 0.030 | 2.63e+04 |
| optimistic_k1 | 0.865 | 2.24e+03 | 5.31e+05 | 12.1 – 3.31e+05 | 0.029 | 0.024 | 4.9e+04 |
| optimistic_k10 | 0.281 | 726 | 1.73e+05 | 3.9 – 1.08e+05 | 0.054 | 0.036 | 1.59e+04 |
| optimistic_k2 | 0.751 | 1.95e+03 | 4.61e+05 | 10.5 – 2.88e+05 | 0.031 | 0.025 | 4.26e+04 |
| optimistic_k3 | 0.655 | 1.7e+03 | 4.03e+05 | 9.13 – 2.51e+05 | 0.034 | 0.027 | 3.72e+04 |
| optimistic_k5 | 0.505 | 1.31e+03 | 3.10e+05 | 7.03 – 1.94e+05 | 0.039 | 0.029 | 2.86e+04 |

## Similarity-weight variants — nathan_headline_no_tooluse

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 622 | 2.54e+05 | 2.81 – 1.15e+05 | 0.063 | 0.040 | 4.86e+04 |
| conservative_k10 | 0.243 | 177 | 7.35e+04 | 0.801 – 3.27e+04 | 0.110 | 0.058 | 1.38e+04 |
| conservative_k2 | 0.725 | 531 | 2.17e+05 | 2.4 – 9.81e+04 | 0.068 | 0.042 | 4.15e+04 |
| conservative_k3 | 0.623 | 456 | 1.87e+05 | 2.06 – 8.42e+04 | 0.073 | 0.044 | 3.56e+04 |
| conservative_k5 | 0.466 | 340 | 1.40e+05 | 1.54 – 6.3e+04 | 0.083 | 0.048 | 2.66e+04 |
| optimistic_k1 | 0.865 | 633 | 2.58e+05 | 2.87 – 1.17e+05 | 0.063 | 0.039 | 4.95e+04 |
| optimistic_k10 | 0.281 | 205 | 8.4e+04 | 0.926 – 3.81e+04 | 0.103 | 0.056 | 1.6e+04 |
| optimistic_k2 | 0.751 | 550 | 2.24e+05 | 2.48 – 1.02e+05 | 0.067 | 0.041 | 4.3e+04 |
| optimistic_k3 | 0.655 | 479 | 1.96e+05 | 2.17 – 8.9e+04 | 0.071 | 0.043 | 3.75e+04 |
| optimistic_k5 | 0.505 | 369 | 1.51e+05 | 1.67 – 6.86e+04 | 0.080 | 0.047 | 2.89e+04 |

## Similarity-weight variants — nathan_headline_ocean

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.82e+04 | 1.37e+06 | 294 – 1.62e+06 | 0.002 | 0.003 | 5.87e+05 |
| conservative_k10 | 0.243 | 8.02e+03 | 3.93e+05 | 83.7 – 4.61e+05 | 0.005 | 0.008 | 1.67e+05 |
| conservative_k2 | 0.725 | 2.41e+04 | 1.17e+06 | 250 – 1.38e+06 | 0.002 | 0.003 | 5.01e+05 |
| conservative_k3 | 0.623 | 2.07e+04 | 1.00e+06 | 215 – 1.19e+06 | 0.002 | 0.004 | 4.30e+05 |
| conservative_k5 | 0.466 | 1.54e+04 | 7.50e+05 | 161 – 8.87e+05 | 0.003 | 0.005 | 3.21e+05 |
| optimistic_k1 | 0.865 | 2.88e+04 | 1.39e+06 | 299 – 1.65e+06 | 0.002 | 0.003 | 5.98e+05 |
| optimistic_k10 | 0.281 | 9.35e+03 | 4.53e+05 | 96.7 – 5.36e+05 | 0.005 | 0.007 | 1.94e+05 |
| optimistic_k2 | 0.751 | 2.5e+04 | 1.21e+06 | 260 – 1.43e+06 | 0.002 | 0.003 | 5.19e+05 |
| optimistic_k3 | 0.655 | 2.18e+04 | 1.05e+06 | 227 – 1.25e+06 | 0.002 | 0.004 | 4.52e+05 |
| optimistic_k5 | 0.505 | 1.68e+04 | 8.13e+05 | 175 – 9.64e+05 | 0.003 | 0.004 | 3.49e+05 |

## Similarity-weight variants — nathan_headline_ocean_linked

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 2.9e+04 | 1.64e+06 | 272 – 1.85e+06 | 0.002 | 0.003 | 5.93e+05 |
| conservative_k10 | 0.243 | 8.27e+03 | 4.72e+05 | 77.2 – 5.28e+05 | 0.006 | 0.008 | 1.68e+05 |
| conservative_k2 | 0.725 | 2.48e+04 | 1.40e+06 | 232 – 1.58e+06 | 0.002 | 0.004 | 5.06e+05 |
| conservative_k3 | 0.623 | 2.13e+04 | 1.20e+06 | 199 – 1.36e+06 | 0.003 | 0.004 | 4.34e+05 |
| conservative_k5 | 0.466 | 1.59e+04 | 9.02e+05 | 149 – 1.02e+06 | 0.003 | 0.005 | 3.24e+05 |
| optimistic_k1 | 0.865 | 2.96e+04 | 1.67e+06 | 276 – 1.89e+06 | 0.002 | 0.003 | 6.03e+05 |
| optimistic_k10 | 0.281 | 9.61e+03 | 5.43e+05 | 89.3 – 6.11e+05 | 0.005 | 0.007 | 1.95e+05 |
| optimistic_k2 | 0.751 | 2.57e+04 | 1.45e+06 | 240 – 1.64e+06 | 0.002 | 0.004 | 5.24e+05 |
| optimistic_k3 | 0.655 | 2.24e+04 | 1.27e+06 | 210 – 1.43e+06 | 0.003 | 0.004 | 4.57e+05 |
| optimistic_k5 | 0.505 | 1.73e+04 | 9.76e+05 | 161 – 1.10e+06 | 0.003 | 0.005 | 3.52e+05 |

## Similarity-weight variants — nathan_headline_ocean_linked_v5

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.849 | 1.57e+04 | 9.67e+05 | 165 – 1.02e+06 | 0.003 | 0.004 | 5.35e+05 |
| conservative_k10 | 0.243 | 4.47e+03 | 2.78e+05 | 46.3 – 2.92e+05 | 0.008 | 0.011 | 1.52e+05 |
| conservative_k2 | 0.725 | 1.34e+04 | 8.26e+05 | 141 – 8.74e+05 | 0.003 | 0.005 | 4.56e+05 |
| conservative_k3 | 0.623 | 1.15e+04 | 7.09e+05 | 121 – 7.49e+05 | 0.003 | 0.005 | 3.92e+05 |
| conservative_k5 | 0.465 | 8.59e+03 | 5.31e+05 | 89.9 – 5.61e+05 | 0.004 | 0.007 | 2.92e+05 |
| optimistic_k1 | 0.865 | 1.59e+04 | 9.84e+05 | 167 – 1.04e+06 | 0.003 | 0.004 | 5.45e+05 |
| optimistic_k10 | 0.281 | 5.19e+03 | 3.20e+05 | 54.1 – 3.39e+05 | 0.007 | 0.010 | 1.77e+05 |
| optimistic_k2 | 0.751 | 1.39e+04 | 8.54e+05 | 145 – 9.05e+05 | 0.003 | 0.005 | 4.73e+05 |
| optimistic_k3 | 0.655 | 1.21e+04 | 7.45e+05 | 127 – 7.90e+05 | 0.003 | 0.005 | 4.13e+05 |
| optimistic_k5 | 0.505 | 9.32e+03 | 5.74e+05 | 97.4 – 6.11e+05 | 0.004 | 0.006 | 3.19e+05 |

## Similarity-weight variants — nathan_headline_ocean_linked_v8

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Approximate rescaling of the same draws by the pooled-weight ratio (v2 uses per-type weights for M and K, whose means are within 0.01 of the pooled mean).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.849 | 2.43e+04 | 8.93e+05 | 299 – 1.15e+06 | 0.001 | 0.003 | 5.25e+05 |
| conservative_k10 | 0.243 | 6.91e+03 | 2.57e+05 | 84.4 – 3.27e+05 | 0.004 | 0.006 | 1.49e+05 |
| conservative_k2 | 0.725 | 2.07e+04 | 7.63e+05 | 254 – 9.80e+05 | 0.001 | 0.003 | 4.48e+05 |
| conservative_k3 | 0.623 | 1.78e+04 | 6.55e+05 | 218 – 8.40e+05 | 0.002 | 0.003 | 3.84e+05 |
| conservative_k5 | 0.465 | 1.33e+04 | 4.90e+05 | 163 – 6.28e+05 | 0.002 | 0.004 | 2.86e+05 |
| optimistic_k1 | 0.865 | 2.47e+04 | 9.09e+05 | 304 – 1.17e+06 | 0.001 | 0.002 | 5.33e+05 |
| optimistic_k10 | 0.281 | 8e+03 | 2.95e+05 | 98.2 – 3.78e+05 | 0.004 | 0.006 | 1.73e+05 |
| optimistic_k2 | 0.751 | 2.15e+04 | 7.89e+05 | 264 – 1.01e+06 | 0.001 | 0.003 | 4.63e+05 |
| optimistic_k3 | 0.655 | 1.87e+04 | 6.88e+05 | 230 – 8.83e+05 | 0.001 | 0.003 | 4.04e+05 |
| optimistic_k5 | 0.505 | 1.44e+04 | 5.30e+05 | 177 – 6.82e+05 | 0.002 | 0.004 | 3.11e+05 |

## nathan_headline: effect of each new factor (paired draws: per comparison (see table))

| comparison | median N_now of comparison | nathan_headline median / comparison median | per-sample log10(N_headline/N_comparison): median [10th, 90th] |
|---|---|---|---|
| without superhabitability (tool-use change only) | 2.21e+03 | ×1.08 | 0.020 [0.003, 0.091] |
| without cross-lineage tool use (superhab only) | 622 | ×3.84 | 0.594 [0.325, 0.786] |
| without both (= similarity_weighted, v1 model) | 656 | ×3.64 | n/a (independent draws; compare medians) |

## Multi-spectral breakdown (v2 model: M/K/G/F host classes)

Each host type has its own star fraction (RECONS / Kroupa IMF), eta-Earth, habitable window, exomoon-host giants, activity/UV/tidal penalties, similarity weight (own Archive ESI list if >= 3 HZ rocky planets, else pooled) and, for K only, the superhabitability boost. Share = that type's fraction of the posterior-mean N_now; median share = per-sample median.

| scenario | host type | median N_now | 10th–90th | mean | P(N<1) | share of mean N | median share [10th, 90th] | median N_ever | best-estimate N_now | similarity weight (median) |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | M | 1.62e-05 | 2.83e-09 – 0.0616 | 8.13 | 0.957 | 0.5% | 0.4% [0.1, 3.2] | 0.00853 | 14.6 | – |
| baseline | K | 0.00327 | 7.66e-07 – 10.4 | 1.45e+03 | 0.817 | 85.3% | 94.6% [79.2, 98.9] | 1.82 | 3.05e+03 | – |
| baseline | G | 1.30e-04 | 2.33e-08 – 0.48 | 238 | 0.919 | 14.0% | 4.0% [0.6, 18.7] | 0.247 | 245 | – |
| baseline | F | 1.17e-07 | 1.71e-11 – 7.23e-04 | 2.79 | 0.992 | 0.2% | 0.0% [0.0, 0.1] | 9.08e-04 | 1.01 | – |
| baseline | **all** | 0.00357 | 8.58e-07 – 11.1 | 1.7e+03 | 0.813 | 100% | – | 2.2 | 3.31e+03 | – |
| baseline_no_exomoons | M | 1.38e-05 | 2.31e-09 – 0.0495 | 7.57 | 0.959 | 0.5% | 0.5% [0.1, 3.4] | 0.0071 | 14.4 | – |
| baseline_no_exomoons | K | 0.00265 | 6.23e-07 – 8.22 | 1.31e+03 | 0.826 | 84.6% | 94.6% [78.2, 98.9] | 1.46 | 2.99e+03 | – |
| baseline_no_exomoons | G | 9.72e-05 | 1.86e-08 – 0.401 | 229 | 0.923 | 14.8% | 3.9% [0.6, 19.7] | 0.191 | 241 | – |
| baseline_no_exomoons | F | 8.15e-08 | 1.13e-11 – 5.28e-04 | 2.75 | 0.993 | 0.2% | 0.0% [0.0, 0.1] | 6.29e-04 | 0.961 | – |
| baseline_no_exomoons | **all** | 0.00295 | 6.94e-07 – 8.94 | 1.55e+03 | 0.822 | 100% | – | 1.77 | 3.25e+03 | – |
| nathan_headline | M | 8.97 | 0.0348 – 1.85e+03 | 5.78e+03 | 0.306 | 1.0% | 0.4% [0.1, 2.8] | 165 | 61.9 | 0.849 |
| nathan_headline | K | 2.02e+03 | 10.6 – 3.03e+05 | 5.00e+05 | 0.031 | 87.3% | 88.2% [70.3, 96.0] | 3.64e+04 | 1.37e+04 | 0.841 |
| nathan_headline | G | 230 | 1.21 – 3.59e+04 | 6.58e+04 | 0.093 | 11.5% | 10.4% [3.2, 28.0] | 1.14e+04 | 1.12e+03 | 0.85 |
| nathan_headline | F | 1.53 | 0.00644 – 297 | 804 | 0.461 | 0.1% | 0.1% [0.0, 0.6] | 559 | 6.04 | 0.85 |
| nathan_headline | **all** | 2.39e+03 | 12.8 – 3.55e+05 | 5.72e+05 | 0.028 | 100% | – | 5.16e+04 | 1.49e+04 | – |
| nathan_headline_no_superhab | M | 8.97 | 0.0348 – 1.85e+03 | 5.78e+03 | 0.306 | 1.1% | 0.4% [0.1, 3.1] | 165 | 61.9 | 0.849 |
| nathan_headline_no_superhab | K | 1.84e+03 | 9.71 – 2.75e+05 | 4.50e+05 | 0.033 | 86.1% | 87.2% [68.4, 95.6] | 3.31e+04 | 1.27e+04 | 0.841 |
| nathan_headline_no_superhab | G | 230 | 1.21 – 3.59e+04 | 6.58e+04 | 0.093 | 12.6% | 11.2% [3.5, 29.8] | 1.14e+04 | 1.12e+03 | 0.85 |
| nathan_headline_no_superhab | F | 1.53 | 0.00644 – 297 | 804 | 0.461 | 0.2% | 0.1% [0.0, 0.6] | 559 | 6.04 | 0.85 |
| nathan_headline_no_superhab | **all** | 2.21e+03 | 11.8 – 3.26e+05 | 5.22e+05 | 0.029 | 100% | – | 4.82e+04 | 1.39e+04 | – |
| nathan_headline_no_tooluse | M | 2.36 | 0.00778 – 607 | 2.56e+03 | 0.424 | 1.0% | 0.4% [0.1, 2.9] | 157 | 12.4 | 0.849 |
| nathan_headline_no_tooluse | K | 530 | 2.33 – 9.96e+04 | 2.23e+05 | 0.069 | 87.9% | 88.6% [70.8, 96.3] | 3.45e+04 | 2.75e+03 | 0.841 |
| nathan_headline_no_tooluse | G | 57.8 | 0.256 – 1.1e+04 | 2.79e+04 | 0.170 | 11.0% | 9.9% [2.9, 27.5] | 1.06e+04 | 208 | 0.85 |
| nathan_headline_no_tooluse | F | 0.301 | 0.00108 – 72.6 | 299 | 0.608 | 0.1% | 0.1% [0.0, 0.5] | 401 | 0.86 | 0.85 |
| nathan_headline_no_tooluse | **all** | 622 | 2.81 – 1.15e+05 | 2.54e+05 | 0.063 | 100% | – | 4.86e+04 | 2.98e+03 | – |
| nathan_headline_ocean | M | 913 | 7.12 – 7.4e+04 | 1.14e+05 | 0.036 | 8.4% | 3.6% [0.4, 22.4] | 1.61e+04 | 5.39e+03 | 0.849 |
| nathan_headline_ocean | K | 2.2e+04 | 224 – 1.28e+06 | 1.11e+06 | 0.002 | 80.8% | 82.6% [59.6, 93.9] | 3.85e+05 | 8.63e+04 | 0.841 |
| nathan_headline_ocean | G | 2.52e+03 | 25.9 – 1.53e+05 | 1.46e+05 | 0.014 | 10.7% | 9.5% [2.9, 26.1] | 1.21e+05 | 7.05e+03 | 0.85 |
| nathan_headline_ocean | F | 16.4 | 0.134 – 1.32e+03 | 1.8e+03 | 0.226 | 0.1% | 0.1% [0.0, 0.5] | 5.86e+03 | 38.1 | 0.85 |
| nathan_headline_ocean | **all** | 2.82e+04 | 294 – 1.62e+06 | 1.37e+06 | 0.002 | 100% | – | 5.87e+05 | 9.88e+04 | – |
| baseline_ocean | M | 0.0015 | 4.65e-07 – 3.73 | 853 | 0.857 | 15.0% | 4.1% [0.5, 25.0] | 0.911 | 1.28e+03 | – |
| baseline_ocean | K | 0.0342 | 1.19e-05 – 68.2 | 4.41e+03 | 0.714 | 77.6% | 88.5% [64.7, 97.3] | 20.6 | 1.92e+04 | – |
| baseline_ocean | G | 0.00126 | 3.89e-07 – 3.36 | 413 | 0.862 | 7.3% | 3.6% [0.5, 17.2] | 2.67 | 1.54e+03 | – |
| baseline_ocean | F | 1.17e-06 | 2.51e-10 – 0.00458 | 3.95 | 0.984 | 0.1% | 0.0% [0.0, 0.1] | 0.00982 | 6.38 | – |
| baseline_ocean | **all** | 0.0413 | 1.45e-05 – 83.9 | 5.68e+03 | 0.703 | 100% | – | 27.1 | 2.2e+04 | – |
| nathan_headline_ocean_linked | M | 930 | 6.7 – 8.22e+04 | 1.36e+05 | 0.038 | 8.3% | 3.6% [0.4, 25.3] | 1.63e+04 | 5.39e+03 | 0.849 |
| nathan_headline_ocean_linked | K | 2.23e+04 | 204 – 1.47e+06 | 1.33e+06 | 0.003 | 80.9% | 82.3% [58.0, 94.0] | 3.86e+05 | 8.63e+04 | 0.841 |
| nathan_headline_ocean_linked | G | 2.57e+03 | 23.2 – 1.74e+05 | 1.76e+05 | 0.015 | 10.7% | 9.4% [2.9, 26.0] | 1.20e+05 | 7.05e+03 | 0.85 |
| nathan_headline_ocean_linked | F | 16.8 | 0.123 – 1.51e+03 | 2.14e+03 | 0.230 | 0.1% | 0.1% [0.0, 0.5] | 5.89e+03 | 38.1 | 0.85 |
| nathan_headline_ocean_linked | **all** | 2.9e+04 | 272 – 1.85e+06 | 1.64e+06 | 0.002 | 100% | – | 5.93e+05 | 9.88e+04 | – |
| baseline_ocean_linked | M | 0.00154 | 4.76e-07 – 4.01 | 497 | 0.853 | 10.4% | 4.2% [0.4, 28.2] | 0.906 | 1.28e+03 | – |
| baseline_ocean_linked | K | 0.0341 | 1.23e-05 – 78.8 | 3.94e+03 | 0.713 | 82.5% | 88.2% [62.4, 97.4] | 20.1 | 1.92e+04 | – |
| baseline_ocean_linked | G | 0.00125 | 4.06e-07 – 3.57 | 333 | 0.857 | 7.0% | 3.6% [0.5, 17.1] | 2.55 | 1.54e+03 | – |
| baseline_ocean_linked | F | 1.18e-06 | 2.25e-10 – 0.00542 | 2.73 | 0.983 | 0.1% | 0.0% [0.0, 0.1] | 0.00924 | 6.38 | – |
| baseline_ocean_linked | **all** | 0.043 | 1.56e-05 – 95.9 | 4.77e+03 | 0.701 | 100% | – | 26.6 | 2.2e+04 | – |
| nathan_headline_ocean_linked_v5 | M | 506 | 4.13 – 4.56e+04 | 7.83e+04 | 0.047 | 8.1% | 3.6% [0.4, 25.5] | 1.47e+04 | 2.79e+03 | 0.849 |
| nathan_headline_ocean_linked_v5 | K | 1.22e+04 | 124 – 8.12e+05 | 7.84e+05 | 0.003 | 81.1% | 82.9% [58.8, 94.1] | 3.48e+05 | 4.46e+04 | 0.841 |
| nathan_headline_ocean_linked_v5 | G | 1.33e+03 | 13.2 – 9.45e+04 | 1.04e+05 | 0.022 | 10.7% | 9.0% [2.8, 24.6] | 1.09e+05 | 3.65e+03 | 0.849 |
| nathan_headline_ocean_linked_v5 | F | 8.57 | 0.0653 – 787 | 1.18e+03 | 0.287 | 0.1% | 0.1% [0.0, 0.5] | 5.34e+03 | 19.9 | 0.849 |
| nathan_headline_ocean_linked_v5 | **all** | 1.57e+04 | 165 – 1.02e+06 | 9.67e+05 | 0.003 | 100% | – | 5.35e+05 | 5.11e+04 | – |
| baseline_ocean_linked_v5 | M | 0.00153 | 4.87e-07 – 3.88 | 181 | 0.855 | 7.7% | 4.2% [0.4, 28.3] | 0.757 | 1e+03 | – |
| baseline_ocean_linked_v5 | K | 0.0329 | 1.35e-05 – 66.9 | 1.98e+03 | 0.713 | 84.4% | 88.9% [64.0, 97.5] | 17.3 | 1.51e+04 | – |
| baseline_ocean_linked_v5 | G | 0.00104 | 3.83e-07 – 2.95 | 185 | 0.864 | 7.9% | 3.2% [0.5, 14.7] | 2.19 | 1.22e+03 | – |
| baseline_ocean_linked_v5 | F | 9.78e-07 | 2.12e-10 – 0.00452 | 1.18 | 0.986 | 0.1% | 0.0% [0.0, 0.1] | 0.00768 | 5.07 | – |
| baseline_ocean_linked_v5 | **all** | 0.0403 | 1.64e-05 – 80 | 2.34e+03 | 0.702 | 100% | – | 22.9 | 1.73e+04 | – |
| nathan_headline_ocean_linked_v8 | M | 396 | 3.47 – 2.99e+04 | 4.34e+04 | 0.053 | 4.9% | 1.8% [0.2, 13.8] | 7.29e+03 | 7.02e+03 | 0.849 |
| nathan_headline_ocean_linked_v8 | K | 1.81e+04 | 217 – 8.78e+05 | 7.08e+05 | 0.002 | 79.3% | 81.1% [52.7, 94.3] | 3.22e+05 | 1.74e+05 | 0.841 |
| nathan_headline_ocean_linked_v8 | G | 2.98e+03 | 34.9 – 1.53e+05 | 1.41e+05 | 0.010 | 15.7% | 13.4% [3.6, 39.5] | 1.27e+05 | 1.79e+04 | 0.849 |
| nathan_headline_ocean_linked_v8 | F | 15.2 | 0.143 – 1.02e+03 | 1.17e+03 | 0.228 | 0.1% | 0.1% [0.0, 0.6] | 5e+03 | 96.9 | 0.849 |
| nathan_headline_ocean_linked_v8 | **all** | 2.43e+04 | 299 – 1.15e+06 | 8.93e+05 | 0.001 | 100% | – | 5.25e+05 | 1.99e+05 | – |
| baseline_ocean_linked_v8 | M | 6.49e-04 | 2.16e-07 – 1.63 | 84.4 | 0.882 | 3.7% | 2.1% [0.2, 16.7] | 0.33 | 1.78e+03 | – |
| baseline_ocean_linked_v8 | K | 0.0277 | 1.19e-05 – 49.3 | 1.89e+03 | 0.730 | 82.7% | 88.7% [61.9, 97.7] | 13.5 | 4.16e+04 | – |
| baseline_ocean_linked_v8 | G | 0.00151 | 5.90e-07 – 3.51 | 309 | 0.853 | 13.5% | 5.6% [0.8, 26.8] | 2.48 | 4.25e+03 | – |
| baseline_ocean_linked_v8 | F | 1.19e-06 | 2.91e-10 – 0.00437 | 0.834 | 0.985 | 0.0% | 0.0% [0.0, 0.1] | 0.00771 | 17.6 | – |
| baseline_ocean_linked_v8 | **all** | 0.0337 | 1.44e-05 – 58.5 | 2.28e+03 | 0.718 | 100% | – | 18.7 | 4.77e+04 | – |

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
| baseline | lithic | 0.0023 | 6.05e-07 – 5.88 | 1.29e+03 | 0.835 | 0.969 [0.182, 0.999] | 2.34e+03 |
| baseline | agricultural | 4.17e-06 | 9.46e-10 – 0.0134 | 3.35 | 0.977 | 0.00117 [1.10e-04, 0.013] | 7.08 |
| baseline | industrial | 4.67e-08 | 9.60e-12 – 1.73e-04 | 0.055 | 0.998 | 1.35e-05 [9.51e-07, 1.80e-04] | 0.0857 |
| baseline | radio | 3.29e-08 | 5.90e-12 – 1.33e-04 | 0.226 | 0.998 | 8.42e-06 [5.11e-07, 1.61e-04] | 0.0692 |
| baseline | spacefaring | 5.09e-05 | 2.78e-09 – 0.856 | 404 | 0.904 | 0.0208 [1.57e-04, 0.817] | 962 |
| baseline | **radio-capable (radio + spacefaring)** | 5.34e-05 | 3.09e-09 – 0.863 | 404 | 0.904 | – | 963 |
| baseline_no_exomoons | lithic | 0.00187 | 4.84e-07 – 4.72 | 1.22e+03 | 0.843 | 0.969 [0.182, 0.999] | 2.3e+03 |
| baseline_no_exomoons | agricultural | 3.32e-06 | 7.44e-10 – 0.0111 | 3.22 | 0.979 | 0.00117 [1.10e-04, 0.013] | 6.94 |
| baseline_no_exomoons | industrial | 3.80e-08 | 7.11e-12 – 1.45e-04 | 0.0518 | 0.998 | 1.35e-05 [9.51e-07, 1.80e-04] | 0.0841 |
| baseline_no_exomoons | radio | 2.66e-08 | 4.63e-12 – 1.05e-04 | 0.221 | 0.998 | 8.42e-06 [5.11e-07, 1.61e-04] | 0.0679 |
| baseline_no_exomoons | spacefaring | 4.11e-05 | 2.08e-09 – 0.701 | 322 | 0.908 | 0.0208 [1.57e-04, 0.817] | 944 |
| baseline_no_exomoons | **radio-capable (radio + spacefaring)** | 4.31e-05 | 2.33e-09 – 0.708 | 322 | 0.908 | – | 944 |
| nathan_headline | lithic | 1.5e+03 | 9.65 – 2.00e+05 | 3.30e+05 | 0.031 | 0.97 [0.2, 0.999] | 1.05e+04 |
| nathan_headline | agricultural | 2.82 | 0.0123 – 507 | 1.49e+03 | 0.403 | 0.00116 [1.14e-04, 0.0129] | 31.8 |
| nathan_headline | industrial | 0.032 | 1.17e-04 – 6.21 | 19.2 | 0.794 | 1.33e-05 [9.62e-07, 1.82e-04] | 0.386 |
| nathan_headline | radio | 0.0213 | 6.59e-05 – 5 | 33.9 | 0.814 | 8.51e-06 [5.05e-07, 1.57e-04] | 0.311 |
| nathan_headline | spacefaring | 37.3 | 0.0177 – 4.8e+04 | 2.41e+05 | 0.279 | 0.0202 [1.42e-04, 0.797] | 4.33e+03 |
| nathan_headline | **radio-capable (radio + spacefaring)** | 38.8 | 0.0197 – 4.81e+04 | 2.41e+05 | 0.275 | – | 4.33e+03 |
| nathan_headline_no_superhab | lithic | 1.38e+03 | 8.95 – 1.84e+05 | 3.00e+05 | 0.032 | 0.97 [0.2, 0.999] | 9.85e+03 |
| nathan_headline_no_superhab | agricultural | 2.6 | 0.0114 – 465 | 1.36e+03 | 0.411 | 0.00116 [1.14e-04, 0.0129] | 29.8 |
| nathan_headline_no_superhab | industrial | 0.0294 | 1.09e-04 – 5.7 | 17.5 | 0.800 | 1.33e-05 [9.62e-07, 1.82e-04] | 0.361 |
| nathan_headline_no_superhab | radio | 0.0197 | 6.10e-05 – 4.59 | 31.1 | 0.819 | 8.51e-06 [5.05e-07, 1.57e-04] | 0.291 |
| nathan_headline_no_superhab | spacefaring | 34.4 | 0.0163 – 4.42e+04 | 2.20e+05 | 0.284 | 0.0202 [1.42e-04, 0.797] | 4.05e+03 |
| nathan_headline_no_superhab | **radio-capable (radio + spacefaring)** | 35.8 | 0.0182 – 4.43e+04 | 2.20e+05 | 0.279 | – | 4.05e+03 |
| nathan_headline_no_tooluse | lithic | 394 | 2.24 – 6.09e+04 | 1.29e+05 | 0.069 | 0.97 [0.2, 0.999] | 2.1e+03 |
| nathan_headline_no_tooluse | agricultural | 0.751 | 0.00287 – 150 | 484 | 0.527 | 0.00116 [1.14e-04, 0.0129] | 6.36 |
| nathan_headline_no_tooluse | industrial | 0.00857 | 2.73e-05 – 1.84 | 6.16 | 0.871 | 1.33e-05 [9.62e-07, 1.82e-04] | 0.0771 |
| nathan_headline_no_tooluse | radio | 0.00567 | 1.53e-05 – 1.49 | 10.2 | 0.882 | 8.51e-06 [5.05e-07, 1.57e-04] | 0.0622 |
| nathan_headline_no_tooluse | spacefaring | 9.18 | 0.00392 – 1.65e+04 | 1.25e+05 | 0.362 | 0.0202 [1.42e-04, 0.797] | 865 |
| nathan_headline_no_tooluse | **radio-capable (radio + spacefaring)** | 9.59 | 0.00438 – 1.66e+04 | 1.25e+05 | 0.358 | – | 865 |
| nathan_headline_ocean | lithic | 1.75e+04 | 235 – 8.99e+05 | 8.02e+05 | 0.002 | 0.97 [0.2, 0.999] | 6.99e+04 |
| nathan_headline_ocean | agricultural | 494 | 1.09 – 1.56e+05 | 3.13e+05 | 0.097 | 0.00116 [1.14e-04, 0.0129] | 2.45e+04 |
| nathan_headline_ocean | industrial | 0.0521 | 2.26e-04 – 7.57 | 20.3 | 0.772 | 1.33e-05 [9.62e-07, 1.82e-04] | 0.397 |
| nathan_headline_ocean | radio | 0.034 | 1.26e-04 – 6.16 | 37.5 | 0.794 | 8.51e-06 [5.05e-07, 1.57e-04] | 0.321 |
| nathan_headline_ocean | spacefaring | 58.9 | 0.0316 – 6.34e+04 | 2.53e+05 | 0.250 | 0.0202 [1.42e-04, 0.797] | 4.46e+03 |
| nathan_headline_ocean | **radio-capable (radio + spacefaring)** | 61.1 | 0.0361 – 6.35e+04 | 2.53e+05 | 0.245 | – | 4.46e+03 |
| baseline_ocean | lithic | 0.0256 | 1.09e-05 – 44.2 | 4.52e+03 | 0.731 | 0.969 [0.182, 0.999] | 1.56e+04 |
| baseline_ocean | agricultural | 7.19e-04 | 1.00e-07 – 4.27 | 735 | 0.853 | 0.00117 [1.10e-04, 0.013] | 5.47e+03 |
| baseline_ocean | industrial | 7.36e-08 | 1.76e-11 – 2.40e-04 | 0.0559 | 0.998 | 1.35e-05 [9.51e-07, 1.80e-04] | 0.0884 |
| baseline_ocean | radio | 5.20e-08 | 1.07e-11 – 1.90e-04 | 0.227 | 0.998 | 8.42e-06 [5.11e-07, 1.61e-04] | 0.0713 |
| baseline_ocean | spacefaring | 8.40e-05 | 4.90e-09 – 1.23 | 418 | 0.895 | 0.0208 [1.57e-04, 0.817] | 992 |
| baseline_ocean | **radio-capable (radio + spacefaring)** | 8.81e-05 | 5.34e-09 – 1.25 | 418 | 0.895 | – | 992 |
| nathan_headline_ocean_linked | lithic | 1.74e+04 | 213 – 1.01e+06 | 9.25e+05 | 0.002 | 0.969 [0.179, 0.999] | 6.99e+04 |
| nathan_headline_ocean_linked | agricultural | 527 | 1.06 – 1.74e+05 | 3.55e+05 | 0.098 | 0.00113 [1.08e-04, 0.013] | 2.45e+04 |
| nathan_headline_ocean_linked | industrial | 0.0508 | 1.82e-04 – 9.66 | 28.2 | 0.762 | 1.31e-05 [9.25e-07, 1.78e-04] | 0.397 |
| nathan_headline_ocean_linked | radio | 0.033 | 1.02e-04 – 7.59 | 42.9 | 0.785 | 8.29e-06 [4.90e-07, 1.49e-04] | 0.321 |
| nathan_headline_ocean_linked | spacefaring | 59.2 | 0.0256 – 8.11e+04 | 3.64e+05 | 0.257 | 0.0207 [1.25e-04, 0.819] | 4.46e+03 |
| nathan_headline_ocean_linked | **radio-capable (radio + spacefaring)** | 61.5 | 0.0291 – 8.13e+04 | 3.64e+05 | 0.252 | – | 4.46e+03 |
| baseline_ocean_linked | lithic | 0.0261 | 1.12e-05 – 47.4 | 3.3e+03 | 0.732 | 0.968 [0.169, 0.999] | 1.56e+04 |
| baseline_ocean_linked | agricultural | 7.68e-04 | 1.02e-07 – 5.08 | 868 | 0.851 | 0.00113 [1.06e-04, 0.0131] | 5.47e+03 |
| baseline_ocean_linked | industrial | 7.21e-08 | 1.60e-11 – 2.80e-04 | 0.19 | 0.997 | 1.30e-05 [9.03e-07, 1.81e-04] | 0.0884 |
| baseline_ocean_linked | radio | 4.84e-08 | 1.03e-11 – 2.09e-04 | 0.162 | 0.998 | 8.22e-06 [4.78e-07, 1.53e-04] | 0.0713 |
| baseline_ocean_linked | spacefaring | 8.43e-05 | 4.04e-09 – 1.48 | 600 | 0.891 | 0.022 [1.29e-04, 0.829] | 992 |
| baseline_ocean_linked | **radio-capable (radio + spacefaring)** | 8.74e-05 | 4.45e-09 – 1.49 | 601 | 0.891 | – | 992 |
| nathan_headline_ocean_linked_v5 | lithic | 9.59e+03 | 133 – 5.22e+05 | 4.77e+05 | 0.003 | 0.969 [0.179, 0.999] | 3.61e+04 |
| nathan_headline_ocean_linked_v5 | agricultural | 280 | 0.611 – 1.06e+05 | 2.43e+05 | 0.121 | 0.00112 [1.08e-04, 0.0131] | 1.27e+04 |
| nathan_headline_ocean_linked_v5 | industrial | 0.0281 | 1.12e-04 – 5.04 | 11.1 | 0.807 | 1.31e-05 [9.18e-07, 1.78e-04] | 0.206 |
| nathan_headline_ocean_linked_v5 | radio | 0.0187 | 6.02e-05 – 3.91 | 17.1 | 0.826 | 8.29e-06 [4.87e-07, 1.48e-04] | 0.166 |
| nathan_headline_ocean_linked_v5 | spacefaring | 31.4 | 0.0142 – 5.14e+04 | 2.47e+05 | 0.292 | 0.021 [1.25e-04, 0.819] | 2.31e+03 |
| nathan_headline_ocean_linked_v5 | **radio-capable (radio + spacefaring)** | 32.2 | 0.016 – 5.09e+04 | 2.45e+05 | 0.288 | – | 2.31e+03 |
| baseline_ocean_linked_v5 | lithic | 0.0253 | 1.26e-05 – 41.4 | 1.19e+03 | 0.735 | 0.968 [0.166, 0.999] | 1.23e+04 |
| baseline_ocean_linked_v5 | agricultural | 7.24e-04 | 1.03e-07 – 4.16 | 801 | 0.853 | 0.00112 [1.08e-04, 0.0123] | 4.3e+03 |
| baseline_ocean_linked_v5 | industrial | 6.90e-08 | 1.71e-11 – 2.46e-04 | 0.02 | 0.998 | 1.29e-05 [9.32e-07, 1.77e-04] | 0.0695 |
| baseline_ocean_linked_v5 | radio | 4.32e-08 | 9.30e-12 – 1.81e-04 | 0.0498 | 0.998 | 8.19e-06 [4.74e-07, 1.49e-04] | 0.0561 |
| baseline_ocean_linked_v5 | spacefaring | 7.84e-05 | 4.20e-09 – 1.12 | 354 | 0.897 | 0.0215 [1.22e-04, 0.833] | 781 |
| baseline_ocean_linked_v5 | **radio-capable (radio + spacefaring)** | 7.75e-05 | 4.54e-09 – 1.1 | 351 | 0.898 | – | 781 |
| nathan_headline_ocean_linked_v8 | lithic | 1.82e+04 | 267 – 8.23e+05 | 6.64e+05 | 0.001 | 0.982 [0.45, 0.999] | 1.59e+05 |
| nathan_headline_ocean_linked_v8 | agricultural | 242 | 0.688 – 6.86e+04 | 1.55e+05 | 0.116 | 9.13e-04 [1.22e-04, 0.00757] | 2.13e+04 |
| nathan_headline_ocean_linked_v8 | industrial | 0.0861 | 6.12e-04 – 6.22 | 7.9 | 0.762 | 1.07e-05 [8.05e-07, 1.34e-04] | 1.83 |
| nathan_headline_ocean_linked_v8 | radio | 0.0627 | 3.47e-04 – 5.87 | 14.8 | 0.776 | 7.58e-06 [4.89e-07, 1.18e-04] | 1.5 |
| nathan_headline_ocean_linked_v8 | spacefaring | 72.1 | 0.0656 – 4.13e+04 | 7.48e+04 | 0.227 | 0.0127 [8.19e-05, 0.547] | 1.86e+04 |
| nathan_headline_ocean_linked_v8 | **radio-capable (radio + spacefaring)** | 73.5 | 0.0734 – 4.08e+04 | 7.4e+04 | 0.222 | – | 1.86e+04 |
| baseline_ocean_linked_v8 | lithic | 0.0252 | 1.18e-05 – 42.3 | 1.76e+03 | 0.735 | 0.982 [0.441, 0.999] | 3.82e+04 |
| baseline_ocean_linked_v8 | agricultural | 3.69e-04 | 5.68e-08 – 1.77 | 355 | 0.883 | 9.23e-04 [1.23e-04, 0.00722] | 5.1e+03 |
| baseline_ocean_linked_v8 | industrial | 1.22e-07 | 3.66e-11 – 2.51e-04 | 0.00961 | 0.998 | 1.05e-05 [8.30e-07, 1.37e-04] | 0.437 |
| baseline_ocean_linked_v8 | radio | 8.29e-08 | 2.22e-11 – 2.20e-04 | 0.0225 | 0.998 | 7.59e-06 [4.73e-07, 1.19e-04] | 0.358 |
| baseline_ocean_linked_v8 | spacefaring | 1.02e-04 | 7.74e-09 – 0.862 | 161 | 0.904 | 0.0128 [8.19e-05, 0.555] | 4.44e+03 |
| baseline_ocean_linked_v8 | **radio-capable (radio + spacefaring)** | 1.03e-04 | 8.17e-09 – 0.864 | 159 | 0.905 | – | 4.44e+03 |

Radio-capable N vs classic SETI-style Drake: Sandberg, Drexler & Ord 2018's 'current knowledge' sketch gives median N = 0.32, mean 27 million, P(N<1) = 52% (communicating civilisations; their Table 1). This model's static SDO-style stone-age variant: median 28.8.

| scenario | median episode length (yr) [10th, 90th] | radio-capable: median NN distance (ly) | top drivers of radio-capable N (swing, dex) |
|---|---|---|---|
| baseline | 1.18e+06 [3.18e+04, 1.87e+07] | 5.70e+06 (N<1) | l_stone_yr 4.5; tau_stone_tool_intelligence 4.2; stage_h_space_per_yr 3.3; f_land_and_ocean 3.1; tau_abiogenesis 2.6 |
| baseline_no_exomoons | 1.18e+06 [3.18e+04, 1.87e+07] | 6.34e+06 (N<1) | l_stone_yr 4.6; tau_stone_tool_intelligence 4.2; stage_h_space_per_yr 3.3; f_land_and_ocean 3.1; tau_abiogenesis 2.7 |
| nathan_headline | 1.21e+06 [3.09e+04, 1.83e+07] | 6.68e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; f_land_and_ocean 3.3; f_plate_tectonics 1.8; m_recurrence 1.4 |
| nathan_headline_no_superhab | 1.21e+06 [3.09e+04, 1.83e+07] | 6.96e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; f_land_and_ocean 3.3; f_plate_tectonics 1.8; m_recurrence 1.4 |
| nathan_headline_no_tooluse | 1.21e+06 [3.09e+04, 1.83e+07] | 1.34e+04 | l_stone_yr 4.4; stage_h_space_per_yr 3.5; f_land_and_ocean 3.3; f_plate_tectonics 1.8; m_recurrence 1.6 |
| nathan_headline_ocean | 1.21e+06 [3.09e+04, 1.83e+07] | 5.33e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; f_land_and_ocean 2.6; f_plate_tectonics 1.7; m_recurrence 1.5 |
| baseline_ocean | 1.18e+06 [3.18e+04, 1.87e+07] | 4.43e+06 (N<1) | l_stone_yr 4.5; tau_stone_tool_intelligence 4.2; stage_h_space_per_yr 3.4; tau_abiogenesis 2.6; f_land_and_ocean 2.5 |
| nathan_headline_ocean_linked | 1.21e+06 [3.09e+04, 2.02e+07] | 5.31e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.6; f_land_and_ocean 3.1; f_plate_tectonics 2.6; stage_h_ind_per_yr 1.8 |
| baseline_ocean_linked | 1.19e+06 [3.18e+04, 2.08e+07] | 4.45e+06 (N<1) | l_stone_yr 4.5; tau_stone_tool_intelligence 4.4; stage_h_space_per_yr 3.6; f_land_and_ocean 2.9; tau_eukaryogenesis 2.6 |
| nathan_headline_ocean_linked_v5 | 1.21e+06 [3.07e+04, 2.01e+07] | 7.33e+03 | l_stone_yr 4.4; stage_h_space_per_yr 3.7; f_land_and_ocean 3.1; f_plate_tectonics 2.6; stage_h_ind_per_yr 1.9 |
| baseline_ocean_linked_v5 | 1.18e+06 [3.33e+04, 2.06e+07] | 4.73e+06 (N<1) | l_stone_yr 4.5; tau_stone_tool_intelligence 4.2; stage_h_space_per_yr 3.9; f_plate_tectonics 2.8; f_land_and_ocean 2.7 |
| nathan_headline_ocean_linked_v8 | 1.39e+06 [3.07e+04, 1.56e+07] | 4.86e+03 | l_stone_yr 4.2; stage_h_space_per_yr 3.4; stage_h_ind_per_yr 1.9; f_plate_tectonics 1.8; stage_h_radio_per_yr 1.8 |
| baseline_ocean_linked_v8 | 1.38e+06 [3.33e+04, 1.56e+07] | 4.11e+06 (N<1) | l_stone_yr 4.4; tau_stone_tool_intelligence 4.3; stage_h_space_per_yr 3.5; tau_eukaryogenesis 2.7; tau_abiogenesis 2.6 |

## Spacing: equal-cube side and median nearest-neighbour distance (disk volume ~7.9e12 ly³, user-supplied)

Cube side = (V/N)^(1/3). Nearest-neighbour: random (Poisson) placement; 3D median r = (3 ln2/(4πn))^(1/3), or the thin-disk 2D form when r exceeds the 1,000-ly thickness (R = 50,000 ly). Values for N < 1 mean no neighbour is expected; they are shown only formally.

| scenario | median N | cube side at median (ly) | median NN distance at median (ly) | regime | NN at 90th-pct N (ly) | NN at 10th-pct N (ly) |
|---|---|---|---|---|---|---|
| baseline | 0.00357 | 1.30e+05 | 6.96e+05 (N<1: none expected) | 2D thin disk | 1.25e+04 | 4.49e+07 (N<1: none expected) |
| baseline_no_exomoons | 0.00295 | 1.39e+05 | 7.67e+05 (N<1: none expected) | 2D thin disk | 1.39e+04 | 5.00e+07 (N<1: none expected) |
| snyder_beattie_priors | 1.60e-20 | 7.91e+10 | 3.30e+14 (N<1: none expected) | 2D thin disk | 8.23e+09 (N<1: none expected) | 1.43e+19 (N<1: none expected) |
| user_inputs | 1.08e-04 | 4.18e+05 | 4.00e+06 (N<1: none expected) | 2D thin disk | 8.07e+04 (N<1: none expected) | 1.90e+08 (N<1: none expected) |
| user_fast_intelligence | 395 | 2.71e+03 | 2.09e+03 | 2D thin disk | 211 | 5.87e+04 (N<1: none expected) |
| similarity_weighted | 656 | 2.29e+03 | 1.63e+03 | 2D thin disk | 204 | 2.95e+04 |
| similarity_weighted_no_rare_earth | 1.70e+07 | 77.4 | 42.5 | 3D | 14 | 203 |
| earth_random_draw | 120 | 4.04e+03 | 3.81e+03 | 2D thin disk | 310 | 9.74e+04 (N<1: none expected) |
| nathan_headline | 2.39e+03 | 1.49e+03 | 818 | 3D | 154 | 1.16e+04 |
| nathan_headline_no_superhab | 2.21e+03 | 1.53e+03 | 840 | 3D | 159 | 1.21e+04 |
| nathan_headline_no_tooluse | 622 | 2.33e+03 | 1.67e+03 | 2D thin disk | 225 | 2.48e+04 |
| nathan_headline_ocean | 2.82e+04 | 654 | 359 | 3D | 93.1 | 2.43e+03 |
| baseline_ocean | 0.0413 | 5.76e+04 | 2.05e+05 (N<1: none expected) | 2D thin disk | 4.54e+03 | 1.09e+07 (N<1: none expected) |
| nathan_headline_ocean_linked | 2.9e+04 | 648 | 356 | 3D | 89 | 2.53e+03 |
| baseline_ocean_linked | 0.043 | 5.69e+04 | 2.01e+05 (N<1: none expected) | 2D thin disk | 4.25e+03 | 1.05e+07 (N<1: none expected) |
| nathan_headline_ocean_linked_v5 | 1.57e+04 | 796 | 437 | 3D | 108 | 3.25e+03 |
| baseline_ocean_linked_v5 | 0.0403 | 5.81e+04 | 2.07e+05 (N<1: none expected) | 2D thin disk | 4.65e+03 | 1.03e+07 (N<1: none expected) |
| nathan_headline_ocean_linked_v8 | 2.43e+04 | 688 | 378 | 3D | 104 | 2.41e+03 |
| baseline_ocean_linked_v8 | 0.0337 | 6.17e+04 | 2.27e+05 (N<1: none expected) | 2D thin disk | 5.44e+03 | 1.10e+07 (N<1: none expected) |
| classic_static_SDO_style | 28.8 | 6.49e+03 | 7.75e+03 | 2D thin disk | 95.7 | 2.35e+34 (N<1: none expected) |

## Comparison with the user's claims

| scenario | median N_now | P(1<=N_now<=3) ('1-3 at a time') | P(N_now>=1) | median N_ever by now | P(50<=N_ever<=100) | P(N_ever>=50) |
|---|---|---|---|---|---|---|
| baseline | 0.00357 | 0.044 | 0.187 | 2.2 | 0.044 | 0.282 |
| baseline_no_exomoons | 0.00295 | 0.043 | 0.178 | 1.77 | 0.042 | 0.268 |
| snyder_beattie_priors | 1.60e-20 | 0.001 | 0.002 | 1.89e-17 | 0.000 | 0.002 |
| user_inputs | 1.08e-04 | 0.022 | 0.068 | 1.43 | 0.041 | 0.255 |
| user_fast_intelligence | 395 | 0.047 | 0.876 | 875 | 0.047 | 0.717 |
| similarity_weighted | 656 | 0.041 | 0.924 | 3.91e+04 | 0.015 | 0.981 |
| similarity_weighted_no_rare_earth | 1.70e+07 | 0.000 | 1.000 | 8.37e+08 | 0.000 | 1.000 |
| earth_random_draw | 120 | 0.060 | 0.828 | 1.15e+04 | 0.029 | 0.928 |
| nathan_headline | 2.39e+03 | 0.023 | 0.972 | 5.16e+04 | 0.011 | 0.986 |
| nathan_headline_no_superhab | 2.21e+03 | 0.024 | 0.971 | 4.82e+04 | 0.012 | 0.985 |
| nathan_headline_no_tooluse | 622 | 0.040 | 0.937 | 4.86e+04 | 0.012 | 0.985 |
| nathan_headline_ocean | 2.82e+04 | 0.003 | 0.998 | 5.87e+05 | 0.000 | 1.000 |
| baseline_ocean | 0.0413 | 0.062 | 0.297 | 27.1 | 0.057 | 0.450 |
| nathan_headline_ocean_linked | 2.9e+04 | 0.003 | 0.998 | 5.93e+05 | 0.000 | 1.000 |
| baseline_ocean_linked | 0.043 | 0.059 | 0.299 | 26.6 | 0.056 | 0.450 |
| nathan_headline_ocean_linked_v5 | 1.57e+04 | 0.004 | 0.997 | 5.35e+05 | 0.000 | 1.000 |
| baseline_ocean_linked_v5 | 0.0403 | 0.061 | 0.298 | 22.9 | 0.053 | 0.437 |
| nathan_headline_ocean_linked_v8 | 2.43e+04 | 0.003 | 0.999 | 5.25e+05 | 0.000 | 1.000 |
| baseline_ocean_linked_v8 | 0.0337 | 0.054 | 0.282 | 18.7 | 0.056 | 0.422 |

## Exomoon effect (paired, same draws)
Median N_now with exomoons 0.00357 vs without 0.00295; per-sample log10(N_with/N_without): median 0.008 dex, 90th pct 0.326, 99th pct 1.077. Median share of habitable bodies that are moons: M 0.0111, K 0.0196, G 0.0178, F 0.0339.


## Deterministic best-estimate point calculations

All parameters at their `best` values; hard-step expected times set equal to Earth's observed intervals (a 'Copernican / Earth-is-typical' choice).

| scenario | N_now | time-avg N | N_ever by now | fraction from Sun-like hosts (v1: G/K; v2: F/G/K) |
|---|---|---|---|---|
| baseline | 3.31e+03 | 1.24e+03 | 8.15e+04 | 0.996 |
| baseline_no_exomoons | 3.25e+03 | 1.22e+03 | 8e+04 | 0.996 |
| snyder_beattie_priors | 2.27e+03 | 1.72e+03 | 8.07e+04 | 0.988 |
| user_inputs | 69.6 | 39.4 | 8.52e+04 | 0.993 |
| user_fast_intelligence | 4.37e+04 | 2.61e+04 | 8.98e+04 | 0.993 |
| similarity_weighted | 1.93e+03 | 1.46e+03 | 6.86e+04 | 0.988 |
| similarity_weighted_no_rare_earth | 4.82e+06 | 3.65e+06 | 1.72e+08 | 0.99 |
| earth_random_draw | 2.27e+03 | 1.72e+03 | 8.07e+04 | 0.988 |
| nathan_headline | 1.49e+04 | 5.89e+03 | 7.61e+04 | 0.996 |
| nathan_headline_no_superhab | 1.39e+04 | 5.55e+03 | 7.22e+04 | 0.996 |
| nathan_headline_no_tooluse | 2.98e+03 | 1.11e+03 | 7.25e+04 | 0.996 |
| nathan_headline_ocean | 9.88e+04 | 3.89e+04 | 5.01e+05 | 0.945 |
| baseline_ocean | 2.2e+04 | 8.22e+03 | 5.37e+05 | 0.942 |
| nathan_headline_ocean_linked | 9.88e+04 | 3.89e+04 | 5.01e+05 | 0.945 |
| baseline_ocean_linked | 2.2e+04 | 8.22e+03 | 5.37e+05 | 0.942 |
| nathan_headline_ocean_linked_v5 | 5.11e+04 | 2.01e+04 | 4.56e+05 | 0.945 |
| baseline_ocean_linked_v5 | 1.73e+04 | 6.47e+03 | 4.89e+05 | 0.942 |
| nathan_headline_ocean_linked_v8 | 1.99e+05 | 7.1e+04 | 9.80e+05 | 0.965 |
| baseline_ocean_linked_v8 | 4.77e+04 | 1.61e+04 | 1.04e+06 | 0.963 |

## Sensitivity — baseline

ESS = 13890 of 200000 samples. Median share of N_now from G/K hosts: 0.996. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.42; posterior P(tau_intelligence<5 Gyr) = 0.37.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.488 | -0.24 | -4.45 | 4.22 |
| f_land_and_ocean | +0.370 | -4.16 | -0.84 | 3.32 |
| l_stone_yr | +0.297 | -4.14 | -1.51 | 2.63 |
| tau_abiogenesis | -0.263 | -1.59 | -4.19 | 2.61 |
| tau_complex_multicellularity | -0.267 | -1.21 | -3.78 | 2.57 |
| tau_oxygenic_photosynthesis_GOE | -0.273 | -1.30 | -3.77 | 2.47 |
| tau_eukaryogenesis | -0.273 | -1.39 | -3.86 | 2.47 |
| f_plate_tectonics | +0.198 | -3.32 | -1.62 | 1.70 |
| r_ster0_per_gyr | -0.107 | -2.09 | -3.59 | 1.50 |
| f_large_moon | +0.148 | -2.98 | -1.66 | 1.32 |
| m_recurrence | -0.114 | -1.81 | -2.83 | 1.02 |
| f_jupiter_shield | +0.102 | -2.96 | -2.01 | 0.95 |
| f_ghz | +0.085 | -2.82 | -1.95 | 0.87 |
| ne_K | +0.052 | -2.75 | -2.25 | 0.50 |
| stage_tau_agri_yr | +0.046 | -2.72 | -2.24 | 0.48 |

## Sensitivity — baseline_no_exomoons

ESS = 13890 of 200000 samples. Median share of N_now from G/K hosts: 0.995. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.42; posterior P(tau_intelligence<5 Gyr) = 0.37.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.486 | -0.37 | -4.55 | 4.17 |
| f_land_and_ocean | +0.367 | -4.30 | -0.97 | 3.33 |
| tau_abiogenesis | -0.263 | -1.65 | -4.32 | 2.67 |
| l_stone_yr | +0.295 | -4.26 | -1.61 | 2.65 |
| tau_complex_multicellularity | -0.266 | -1.29 | -3.89 | 2.60 |
| tau_eukaryogenesis | -0.272 | -1.46 | -3.98 | 2.52 |
| tau_oxygenic_photosynthesis_GOE | -0.272 | -1.43 | -3.83 | 2.40 |
| f_plate_tectonics | +0.197 | -3.37 | -1.65 | 1.72 |
| r_ster0_per_gyr | -0.106 | -2.15 | -3.69 | 1.55 |
| f_large_moon | +0.170 | -3.21 | -1.69 | 1.52 |
| m_recurrence | -0.114 | -1.90 | -2.98 | 1.08 |
| f_jupiter_shield | +0.118 | -3.09 | -2.06 | 1.04 |
| f_ghz | +0.084 | -2.92 | -2.06 | 0.86 |
| ne_K | +0.058 | -2.88 | -2.31 | 0.57 |
| stage_tau_agri_yr | +0.047 | -2.84 | -2.36 | 0.48 |

## Sensitivity — snyder_beattie_priors

ESS = 3184 of 200000 samples. Median share of N_now from G/K hosts: 0.987. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.42 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.58 -> posterior 0.17; posterior P(tau_intelligence<5 Gyr) = 0.12.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.407 | -13.81 | -24.70 | 10.89 |
| tau_abiogenesis | -0.392 | -15.43 | -25.72 | 10.29 |
| tau_eukaryogenesis | -0.360 | -14.98 | -24.86 | 9.88 |
| tau_oxygenic_photosynthesis_GOE | -0.342 | -15.51 | -24.58 | 9.07 |
| tau_complex_multicellularity | -0.351 | -15.51 | -24.49 | 8.98 |
| l_stone_yr | +0.140 | -22.84 | -17.64 | 5.20 |
| f_land_and_ocean | +0.103 | -21.41 | -18.30 | 3.11 |
| r_sn_per_gyr | -0.037 | -19.05 | -21.17 | 2.11 |
| th_gk_gyr | +0.092 | -21.43 | -19.47 | 1.96 |
| r_ster0_per_gyr | -0.033 | -19.59 | -21.43 | 1.84 |
| f_m_flares | +0.005 | -20.44 | -19.14 | 1.30 |
| f_co_ratio | +0.018 | -20.97 | -19.69 | 1.28 |
| n_giant_hz_gk | -0.011 | -18.97 | -20.14 | 1.17 |
| f_jupiter_shield | +0.058 | -20.36 | -19.24 | 1.12 |
| f_plate_tectonics | +0.065 | -20.62 | -19.51 | 1.10 |

## Sensitivity — user_inputs

ESS = 13819 of 200000 samples. Median share of N_now from G/K hosts: 0.986. Median epoch of peak N(t): 1.03 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.41; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.507 | -1.67 | -5.93 | 4.26 |
| f_land_and_ocean | +0.392 | -5.68 | -2.34 | 3.35 |
| tau_abiogenesis | -0.281 | -3.06 | -5.83 | 2.78 |
| tau_eukaryogenesis | -0.299 | -2.76 | -5.30 | 2.55 |
| tau_complex_multicellularity | -0.288 | -2.65 | -5.14 | 2.49 |
| tau_oxygenic_photosynthesis_GOE | -0.293 | -2.68 | -5.03 | 2.35 |
| f_plate_tectonics | +0.212 | -4.77 | -3.14 | 1.63 |
| f_large_moon | +0.150 | -4.51 | -3.26 | 1.25 |
| r_ster0_per_gyr | -0.094 | -3.67 | -4.82 | 1.16 |
| m_recurrence | -0.135 | -3.42 | -4.44 | 1.01 |
| f_ghz | +0.108 | -4.53 | -3.61 | 0.92 |
| f_jupiter_shield | +0.100 | -4.38 | -3.53 | 0.85 |
| f_exomoon_host | +0.030 | -4.06 | -3.49 | 0.57 |
| l_stone_yr | +0.060 | -4.13 | -3.68 | 0.45 |
| ne_gk | +0.067 | -4.14 | -3.70 | 0.44 |

## Sensitivity — user_fast_intelligence

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.991. Median epoch of peak N(t): 1.93 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.50; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.512 | 0.96 | 4.33 | 3.37 |
| tau_eukaryogenesis | -0.314 | 3.16 | 0.91 | 2.25 |
| tau_abiogenesis | -0.312 | 3.15 | 0.91 | 2.24 |
| tau_oxygenic_photosynthesis_GOE | -0.316 | 3.15 | 0.92 | 2.23 |
| tau_complex_multicellularity | -0.312 | 3.11 | 0.93 | 2.18 |
| f_plate_tectonics | +0.267 | 1.72 | 3.52 | 1.80 |
| f_large_moon | +0.191 | 1.98 | 3.25 | 1.27 |
| r_ster0_per_gyr | -0.092 | 2.75 | 1.86 | 0.89 |
| f_jupiter_shield | +0.134 | 2.16 | 3.05 | 0.89 |
| f_ghz | +0.132 | 2.19 | 3.04 | 0.84 |
| ne_gk | +0.103 | 2.30 | 2.98 | 0.68 |
| f_exomoon_host | +0.068 | 2.47 | 3.02 | 0.55 |
| m_disk_now | +0.041 | 2.40 | 2.72 | 0.32 |
| th_gk_gyr | +0.042 | 2.42 | 2.74 | 0.31 |
| stars_per_msun | +0.035 | 2.47 | 2.70 | 0.23 |

## Sensitivity — similarity_weighted

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.993. Median epoch of peak N(t): 0.61 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.570 | 1.19 | 4.54 | 3.35 |
| l_stone_yr | +0.560 | 0.85 | 3.98 | 3.13 |
| f_plate_tectonics | +0.298 | 1.94 | 3.71 | 1.76 |
| m_recurrence | -0.238 | 3.47 | 2.05 | 1.42 |
| f_large_moon | +0.209 | 2.21 | 3.44 | 1.23 |
| f_ghz | +0.150 | 2.35 | 3.27 | 0.92 |
| f_jupiter_shield | +0.146 | 2.38 | 3.27 | 0.89 |
| r_ster0_per_gyr | -0.106 | 2.97 | 2.10 | 0.87 |
| th_gk_gyr | +0.135 | 2.28 | 3.09 | 0.80 |
| ne_gk | +0.117 | 2.46 | 3.18 | 0.71 |
| f_exomoon_host | +0.071 | 2.70 | 3.21 | 0.51 |
| m_disk_now | +0.041 | 2.67 | 2.95 | 0.28 |
| f_rocky_composition | +0.031 | 2.70 | 2.92 | 0.21 |
| r_self_per_gyr | -0.027 | 2.84 | 2.65 | 0.19 |
| f_gk | +0.031 | 2.73 | 2.90 | 0.18 |

## Sensitivity — similarity_weighted_no_rare_earth

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.994. Median epoch of peak N(t): 0.61 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| l_stone_yr | +0.805 | 5.15 | 8.31 | 3.16 |
| m_recurrence | -0.342 | 7.90 | 6.44 | 1.46 |
| f_ghz | +0.216 | 6.80 | 7.70 | 0.90 |
| r_ster0_per_gyr | -0.151 | 7.36 | 6.53 | 0.84 |
| ne_gk | +0.197 | 6.83 | 7.65 | 0.83 |
| th_gk_gyr | +0.193 | 6.70 | 7.49 | 0.78 |
| m_disk_now | +0.057 | 7.09 | 7.34 | 0.26 |
| r_self_per_gyr | -0.046 | 7.30 | 7.05 | 0.25 |
| stars_per_msun | +0.047 | 7.13 | 7.33 | 0.20 |
| f_gk | +0.045 | 7.14 | 7.33 | 0.20 |
| p_bigfive_kills_toolusers | -0.013 | 7.26 | 7.20 | 0.06 |
| f_m_water | +0.007 | 7.21 | 7.27 | 0.06 |
| return_fraction | +0.018 | 7.21 | 7.26 | 0.06 |
| t_metal_gyr | -0.012 | 7.27 | 7.22 | 0.06 |
| f_m_habitable | +0.006 | 7.21 | 7.26 | 0.05 |

## Sensitivity — earth_random_draw

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.992. Median epoch of peak N(t): 0.07 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.82 -> posterior 0.82; posterior P(tau_intelligence<5 Gyr) = 0.89.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.506 | 0.47 | 3.75 | 3.28 |
| l_stone_yr | +0.511 | 0.12 | 3.28 | 3.16 |
| tau_stone_tool_intelligence | -0.263 | 2.80 | 0.61 | 2.19 |
| f_plate_tectonics | +0.268 | 1.19 | 2.97 | 1.78 |
| m_recurrence | -0.207 | 2.76 | 1.36 | 1.41 |
| f_large_moon | +0.186 | 1.51 | 2.74 | 1.23 |
| tau_oxygenic_photosynthesis_GOE | -0.135 | 2.37 | 1.20 | 1.18 |
| tau_complex_multicellularity | -0.121 | 2.33 | 1.28 | 1.05 |
| th_gk_gyr | +0.158 | 1.38 | 2.38 | 1.01 |
| r_ster0_per_gyr | -0.107 | 2.24 | 1.30 | 0.95 |
| f_ghz | +0.136 | 1.61 | 2.53 | 0.91 |
| f_jupiter_shield | +0.133 | 1.64 | 2.51 | 0.88 |
| tau_eukaryogenesis | -0.084 | 2.22 | 1.45 | 0.77 |
| ne_gk | +0.103 | 1.72 | 2.43 | 0.71 |
| f_exomoon_host | +0.067 | 1.95 | 2.44 | 0.49 |

## Sensitivity — nathan_headline

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.996. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.624 | 1.76 | 5.06 | 3.30 |
| l_stone_yr | +0.431 | 1.77 | 4.11 | 2.34 |
| f_plate_tectonics | +0.326 | 2.49 | 4.26 | 1.77 |
| m_recurrence | -0.256 | 4.02 | 2.64 | 1.38 |
| f_large_moon | +0.235 | 2.78 | 4.05 | 1.28 |
| r_ster0_per_gyr | -0.129 | 3.55 | 2.57 | 0.98 |
| f_jupiter_shield | +0.166 | 2.92 | 3.86 | 0.94 |
| f_ghz | +0.164 | 2.91 | 3.84 | 0.93 |
| f_exomoon_host | +0.059 | 3.30 | 3.69 | 0.39 |
| ne_K | +0.060 | 3.21 | 3.55 | 0.34 |
| stage_tau_agri_yr | +0.058 | 3.16 | 3.48 | 0.33 |
| stage_h_space_per_yr | -0.060 | 3.51 | 3.21 | 0.30 |
| m_disk_now | +0.044 | 3.20 | 3.47 | 0.28 |
| f_k_activity | +0.044 | 3.25 | 3.51 | 0.26 |
| tau_stone_tool_intelligence | -0.046 | 3.50 | 3.25 | 0.25 |

## Sensitivity — nathan_headline_no_superhab

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.996. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.625 | 1.73 | 5.03 | 3.30 |
| l_stone_yr | +0.431 | 1.74 | 4.08 | 2.33 |
| f_plate_tectonics | +0.326 | 2.45 | 4.22 | 1.77 |
| m_recurrence | -0.257 | 3.98 | 2.60 | 1.38 |
| f_large_moon | +0.234 | 2.74 | 4.01 | 1.27 |
| r_ster0_per_gyr | -0.129 | 3.51 | 2.53 | 0.98 |
| f_jupiter_shield | +0.165 | 2.88 | 3.82 | 0.94 |
| f_ghz | +0.164 | 2.87 | 3.80 | 0.93 |
| f_exomoon_host | +0.063 | 3.26 | 3.67 | 0.41 |
| ne_K | +0.058 | 3.18 | 3.51 | 0.33 |
| stage_tau_agri_yr | +0.058 | 3.12 | 3.45 | 0.33 |
| stage_h_space_per_yr | -0.060 | 3.47 | 3.17 | 0.30 |
| m_disk_now | +0.044 | 3.16 | 3.44 | 0.27 |
| f_k_activity | +0.044 | 3.22 | 3.48 | 0.25 |
| tau_stone_tool_intelligence | -0.046 | 3.46 | 3.21 | 0.25 |

## Sensitivity — nathan_headline_no_tooluse

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.996. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.599 | 1.17 | 4.47 | 3.30 |
| l_stone_yr | +0.468 | 1.09 | 3.67 | 2.58 |
| f_plate_tectonics | +0.314 | 1.91 | 3.67 | 1.76 |
| m_recurrence | -0.284 | 3.57 | 1.98 | 1.59 |
| f_large_moon | +0.226 | 2.19 | 3.47 | 1.28 |
| r_ster0_per_gyr | -0.129 | 2.98 | 1.96 | 1.02 |
| f_ghz | +0.158 | 2.33 | 3.26 | 0.93 |
| f_jupiter_shield | +0.160 | 2.34 | 3.26 | 0.92 |
| stage_tau_agri_yr | +0.068 | 2.54 | 2.94 | 0.40 |
| stage_h_space_per_yr | -0.076 | 2.98 | 2.59 | 0.39 |
| f_exomoon_host | +0.057 | 2.72 | 3.10 | 0.39 |
| ne_K | +0.058 | 2.63 | 2.97 | 0.34 |
| m_disk_now | +0.042 | 2.62 | 2.89 | 0.27 |
| f_k_activity | +0.043 | 2.67 | 2.93 | 0.26 |
| f_rocky_composition | +0.035 | 2.67 | 2.89 | 0.22 |

## Sensitivity — nathan_headline_ocean

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.964. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| l_stone_yr | +0.519 | 2.83 | 5.18 | 2.35 |
| f_plate_tectonics | +0.395 | 3.58 | 5.37 | 1.79 |
| m_recurrence | -0.309 | 5.10 | 3.69 | 1.41 |
| f_large_moon | +0.282 | 3.84 | 5.12 | 1.29 |
| f_ocean_fecundity | +0.270 | 3.86 | 5.11 | 1.25 |
| r_ster0_per_gyr | -0.155 | 4.62 | 3.64 | 0.98 |
| f_land_and_ocean | +0.191 | 4.18 | 5.11 | 0.94 |
| f_jupiter_shield | +0.200 | 3.99 | 4.92 | 0.93 |
| f_ghz | +0.195 | 4.00 | 4.91 | 0.91 |
| f_exomoon_host | +0.068 | 4.38 | 4.75 | 0.37 |
| stage_tau_agri_yr | +0.071 | 4.24 | 4.57 | 0.34 |
| ne_K | +0.066 | 4.30 | 4.61 | 0.31 |
| stage_h_space_per_yr | -0.073 | 4.60 | 4.30 | 0.31 |
| m_disk_now | +0.053 | 4.30 | 4.56 | 0.26 |
| f_k_activity | +0.050 | 4.34 | 4.59 | 0.25 |

## Sensitivity — baseline_ocean

ESS = 13890 of 200000 samples. Median share of N_now from G/K hosts: 0.959. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.42; posterior P(tau_intelligence<5 Gyr) = 0.37.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.517 | 0.80 | -3.39 | 4.19 |
| l_stone_yr | +0.316 | -3.14 | -0.45 | 2.69 |
| tau_abiogenesis | -0.278 | -0.51 | -3.06 | 2.55 |
| tau_oxygenic_photosynthesis_GOE | -0.284 | -0.25 | -2.74 | 2.49 |
| tau_eukaryogenesis | -0.289 | -0.38 | -2.82 | 2.44 |
| tau_complex_multicellularity | -0.282 | -0.22 | -2.62 | 2.40 |
| f_plate_tectonics | +0.209 | -2.38 | -0.55 | 1.83 |
| f_large_moon | +0.162 | -1.99 | -0.64 | 1.36 |
| r_ster0_per_gyr | -0.109 | -1.22 | -2.54 | 1.32 |
| f_ocean_fecundity | +0.144 | -1.90 | -0.73 | 1.17 |
| f_land_and_ocean | +0.103 | -1.72 | -0.78 | 0.94 |
| f_jupiter_shield | +0.109 | -1.91 | -1.00 | 0.91 |
| m_recurrence | -0.127 | -0.92 | -1.80 | 0.88 |
| f_ghz | +0.085 | -1.72 | -0.93 | 0.79 |
| stage_h_space_per_yr | -0.070 | -1.05 | -1.54 | 0.50 |

## Sensitivity — nathan_headline_ocean_linked

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.964. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| l_stone_yr | +0.509 | 2.85 | 5.20 | 2.36 |
| f_plate_tectonics | +0.439 | 3.44 | 5.54 | 2.10 |
| f_land_and_ocean | +0.276 | 3.97 | 5.38 | 1.41 |
| m_recurrence | -0.299 | 5.10 | 3.70 | 1.40 |
| f_large_moon | +0.276 | 3.83 | 5.14 | 1.30 |
| f_ocean_fecundity | +0.264 | 3.85 | 5.12 | 1.27 |
| r_ster0_per_gyr | -0.153 | 4.63 | 3.65 | 0.99 |
| f_jupiter_shield | +0.196 | 3.99 | 4.94 | 0.95 |
| f_ghz | +0.190 | 4.02 | 4.92 | 0.90 |
| f_rocky_composition | +0.128 | 4.13 | 4.80 | 0.67 |
| f_exomoon_host | +0.068 | 4.39 | 4.77 | 0.38 |
| stage_h_space_per_yr | -0.078 | 4.64 | 4.31 | 0.33 |
| stage_tau_agri_yr | +0.067 | 4.25 | 4.58 | 0.32 |
| ne_K | +0.063 | 4.31 | 4.62 | 0.31 |
| m_disk_now | +0.052 | 4.30 | 4.57 | 0.27 |

## Sensitivity — baseline_ocean_linked

ESS = 13890 of 200000 samples. Median share of N_now from G/K hosts: 0.958. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.42; posterior P(tau_intelligence<5 Gyr) = 0.37.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.512 | 0.78 | -3.39 | 4.17 |
| l_stone_yr | +0.317 | -3.12 | -0.34 | 2.78 |
| tau_abiogenesis | -0.277 | -0.48 | -3.14 | 2.66 |
| tau_complex_multicellularity | -0.277 | -0.19 | -2.67 | 2.48 |
| tau_eukaryogenesis | -0.288 | -0.34 | -2.74 | 2.40 |
| tau_oxygenic_photosynthesis_GOE | -0.284 | -0.29 | -2.57 | 2.28 |
| f_plate_tectonics | +0.240 | -2.39 | -0.39 | 2.00 |
| f_land_and_ocean | +0.150 | -1.89 | -0.59 | 1.30 |
| r_ster0_per_gyr | -0.109 | -1.29 | -2.53 | 1.23 |
| f_large_moon | +0.159 | -1.94 | -0.71 | 1.23 |
| f_ocean_fecundity | +0.143 | -1.91 | -0.74 | 1.16 |
| f_jupiter_shield | +0.107 | -1.90 | -1.05 | 0.85 |
| m_recurrence | -0.130 | -0.95 | -1.77 | 0.82 |
| f_ghz | +0.085 | -1.73 | -0.98 | 0.75 |
| stage_h_space_per_yr | -0.073 | -1.05 | -1.58 | 0.53 |

## Sensitivity — nathan_headline_ocean_linked_v5

ESS = 100000 of 100000 samples. Median share of N_now from G/K hosts: 0.964. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| l_stone_yr | +0.565 | 2.50 | 5.03 | 2.52 |
| f_plate_tectonics | +0.441 | 3.18 | 5.25 | 2.07 |
| f_land_and_ocean | +0.276 | 3.70 | 5.09 | 1.40 |
| f_large_moon | +0.276 | 3.59 | 4.85 | 1.26 |
| f_ocean_fecundity | +0.266 | 3.59 | 4.85 | 1.25 |
| f_jupiter_shield | +0.194 | 3.74 | 4.68 | 0.94 |
| f_ghz | +0.190 | 3.77 | 4.66 | 0.89 |
| m_recurrence | -0.187 | 4.54 | 3.66 | 0.88 |
| r_ster0_per_gyr | -0.118 | 4.34 | 3.58 | 0.76 |
| f_rocky_composition | +0.125 | 3.86 | 4.52 | 0.66 |
| stage_h_space_per_yr | -0.093 | 4.42 | 4.01 | 0.41 |
| stage_tau_agri_yr | +0.082 | 3.97 | 4.36 | 0.39 |
| f_exomoon_host | +0.067 | 4.13 | 4.51 | 0.38 |
| ne_K | +0.064 | 4.04 | 4.36 | 0.31 |
| f_k_activity | +0.054 | 4.04 | 4.34 | 0.29 |

## Sensitivity — baseline_ocean_linked_v5

ESS = 6945 of 100000 samples. Median share of N_now from G/K hosts: 0.958. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.44 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.42; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.510 | 0.73 | -3.28 | 4.01 |
| l_stone_yr | +0.326 | -3.24 | -0.33 | 2.91 |
| tau_complex_multicellularity | -0.274 | -0.12 | -2.72 | 2.60 |
| tau_eukaryogenesis | -0.287 | -0.39 | -2.96 | 2.57 |
| tau_abiogenesis | -0.274 | -0.64 | -3.12 | 2.49 |
| tau_oxygenic_photosynthesis_GOE | -0.288 | -0.18 | -2.59 | 2.41 |
| f_plate_tectonics | +0.250 | -2.56 | -0.34 | 2.21 |
| f_large_moon | +0.150 | -2.01 | -0.75 | 1.27 |
| f_land_and_ocean | +0.140 | -1.90 | -0.78 | 1.12 |
| f_ocean_fecundity | +0.140 | -1.93 | -0.87 | 1.06 |
| f_jupiter_shield | +0.118 | -2.01 | -1.06 | 0.95 |
| r_ster0_per_gyr | -0.078 | -1.38 | -2.17 | 0.79 |
| m_recurrence | -0.130 | -0.95 | -1.70 | 0.75 |
| stage_h_space_per_yr | -0.070 | -1.08 | -1.78 | 0.70 |
| f_ghz | +0.087 | -1.61 | -1.03 | 0.57 |

## Sensitivity — nathan_headline_ocean_linked_v8

ESS = 100000 of 100000 samples. Median share of N_now from G/K hosts: 0.982. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 6.84 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| l_stone_yr | +0.560 | 2.72 | 5.10 | 2.39 |
| f_plate_tectonics | +0.422 | 3.48 | 5.33 | 1.85 |
| f_large_moon | +0.294 | 3.77 | 5.06 | 1.29 |
| m_recurrence | -0.287 | 4.91 | 3.67 | 1.24 |
| f_ocean_fecundity | +0.234 | 3.96 | 4.98 | 1.02 |
| f_jupiter_shield | +0.206 | 3.93 | 4.86 | 0.93 |
| f_ghz | +0.203 | 3.93 | 4.85 | 0.92 |
| r_ster0_per_gyr | -0.116 | 4.53 | 3.82 | 0.71 |
| ne_K | +0.128 | 4.11 | 4.69 | 0.58 |
| f_rocky_composition | +0.111 | 4.10 | 4.66 | 0.56 |
| f_land_and_ocean | +0.102 | 4.11 | 4.61 | 0.50 |
| f_exomoon_host | +0.072 | 4.31 | 4.70 | 0.39 |
| stage_tau_agri_yr | +0.082 | 4.17 | 4.52 | 0.35 |
| f_k_activity | +0.057 | 4.23 | 4.52 | 0.29 |
| f_ocean_world_gk | -0.058 | 4.50 | 4.21 | 0.29 |

## Sensitivity — baseline_ocean_linked_v8

ESS = 6945 of 100000 samples. Median share of N_now from G/K hosts: 0.979. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 6.85 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.42; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.528 | 0.74 | -3.41 | 4.16 |
| l_stone_yr | +0.317 | -3.32 | -0.57 | 2.75 |
| tau_eukaryogenesis | -0.294 | -0.44 | -3.03 | 2.58 |
| tau_complex_multicellularity | -0.281 | -0.21 | -2.77 | 2.56 |
| tau_abiogenesis | -0.282 | -0.67 | -3.15 | 2.49 |
| tau_oxygenic_photosynthesis_GOE | -0.293 | -0.28 | -2.66 | 2.38 |
| f_plate_tectonics | +0.228 | -2.62 | -0.51 | 2.11 |
| f_large_moon | +0.153 | -2.12 | -0.77 | 1.36 |
| f_jupiter_shield | +0.120 | -2.07 | -1.05 | 1.02 |
| f_ocean_fecundity | +0.121 | -1.91 | -1.02 | 0.88 |
| m_recurrence | -0.141 | -0.94 | -1.81 | 0.87 |
| ne_K | +0.085 | -1.88 | -1.05 | 0.83 |
| r_ster0_per_gyr | -0.070 | -1.42 | -2.17 | 0.75 |
| f_ghz | +0.088 | -1.84 | -1.21 | 0.63 |
| f_exomoon_host | +0.041 | -1.56 | -1.00 | 0.56 |
