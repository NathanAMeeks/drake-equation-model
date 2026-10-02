# Results — time-aware extended Drake model (stone-age-or-greater)

**Headline scenario: `nathan_headline`** (user-approved). Literature baseline for comparison: `baseline`.

N = expected number of Milky Way worlds with stone-age-or-greater tool users alive at the same time (present day, other than Earth). Percentiles are over parameter uncertainty (posterior after the Earth-timing update where enabled).

| scenario | median (50/50) | mean | 10th pct | 90th pct | P(N<1) | P(no other, Poisson) | P(1<=N<=3) | time-avg N over history | median N_ever (by now) | ESS |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 0.00238 | 4.31e+03 | 4.27e-07 | 10.4 | 0.820 | 0.791 | 0.042 | median 5.26e-04 / mean 1.05e+03 | 0.851 | 68255 |
| baseline_no_exomoons | 0.00187 | 3.76e+03 | 3.23e-07 | 8.36 | 0.829 | 0.801 | 0.041 | median 4.13e-04 / mean 895 | 0.66 | 68255 |
| snyder_beattie_priors | 5.51e-21 | 0.643 | 3.60e-30 | 1.04e-11 | 0.999 | 0.999 | 0.000 | median 1.17e-21 / mean 0.227 | 4.70e-18 | 3151 |
| user_inputs | 9.93e-05 | 34.4 | 3.94e-08 | 0.251 | 0.934 | 0.916 | 0.021 | median 2.57e-05 / mean 12.3 | 0.875 | 34101 |
| user_fast_intelligence | 571 | 6.01e+05 | 0.736 | 2.06e+05 | 0.110 | 0.097 | 0.042 | median 218 / mean 3.36e+05 | 967 | 200000 |
| similarity_weighted | 895 | 4.69e+05 | 2.68 | 2.08e+05 | 0.067 | 0.058 | 0.038 | median 356 / mean 1.78e+05 | 4.39e+04 | 200000 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 2.12e+08 | 1.75e+05 | 5.41e+08 | 0.000 | 0.000 | 0.000 | median 7.50e+06 / mean 8.11e+07 | 7.87e+08 | 200000 |
| earth_random_draw | 157 | 2.32e+05 | 0.225 | 5.9e+04 | 0.159 | 0.141 | 0.057 | median 50.4 / mean 7.91e+04 | 1.2e+04 | 200000 |
| nathan_headline | 3.18e+03 | 9.55e+05 | 12.8 | 5.53e+05 | 0.030 | 0.026 | 0.022 | median 1.35e+03 / mean 3.89e+05 | 5.06e+04 | 200000 |
| nathan_headline_no_superhab | 3.03e+03 | 9.09e+05 | 12.1 | 5.26e+05 | 0.031 | 0.027 | 0.023 | median 1.27e+03 / mean 3.70e+05 | 4.79e+04 | 200000 |
| nathan_headline_no_tooluse | 964 | 5.10e+05 | 2.83 | 2.24e+05 | 0.065 | 0.056 | 0.038 | median 386 / mean 1.96e+05 | 4.71e+04 | 200000 |
| classic_static_SDO_style | 28.8 | 8.05e+06 | 3.14e-60 | 1.49e+06 | 0.465 | 0.463 | 0.007 | (static) | – | – |

## Worlds vs tool-using species (species_per_tool_world)

species_now = N_now x concurrent hominin-grade species per tool world (log-uniform 1-5, best 2.38, from Smithsonian date spans); species_ever = N_ever x cumulative species per tool world (uniform 8-16, best 15). The factor multiplies species, not worlds.

| scenario | median worlds now | median species now | species 10th-90th | mean species now | median worlds ever | median species ever | best-estimate species now |
|---|---|---|---|---|---|---|---|
| baseline | 0.00238 | 0.00534 | 9.15e-07 – 23.3 | 1.24e+04 | 0.851 | 10 | 7.87e+03 |
| baseline_no_exomoons | 0.00187 | 0.00422 | 6.99e-07 – 18.9 | 1.07e+04 | 0.66 | 7.78 | 7.7e+03 |
| snyder_beattie_priors | 5.51e-21 | 1.29e-20 | 6.98e-30 – 2.21e-11 | 0.954 | 4.70e-18 | 5.56e-17 | 7.87e+03 |
| user_inputs | 9.93e-05 | 2.20e-04 | 8.56e-08 – 0.6 | 85.2 | 0.875 | 10.2 | 206 |
| user_fast_intelligence | 571 | 1.28e+03 | 1.58 – 4.75e+05 | 1.50e+06 | 967 | 1.14e+04 | 1.29e+05 |
| similarity_weighted | 895 | 1.99e+03 | 5.91 – 4.81e+05 | 1.14e+06 | 4.39e+04 | 5.19e+05 | 6.68e+03 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 4.20e+07 | 3.79e+05 – 1.27e+09 | 5.29e+08 | 7.87e+08 | 9.26e+09 | 1.34e+07 |
| earth_random_draw | 157 | 352 | 0.492 – 1.35e+05 | 6.09e+05 | 1.2e+04 | 1.42e+05 | 7.87e+03 |
| nathan_headline | 3.18e+03 | 7.13e+03 | 28.1 – 1.28e+06 | 2.39e+06 | 5.06e+04 | 5.95e+05 | 3.08e+04 |
| nathan_headline_no_superhab | 3.03e+03 | 6.79e+03 | 26.7 – 1.22e+06 | 2.27e+06 | 4.79e+04 | 5.65e+05 | 2.97e+04 |
| nathan_headline_no_tooluse | 964 | 2.16e+03 | 6.2 – 5.23e+05 | 1.27e+06 | 4.71e+04 | 5.55e+05 | 6.94e+03 |
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

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 3.18e+03 | 9.55e+05 | 12.8 – 5.53e+05 | 0.030 | 0.022 | 5.06e+04 |
| conservative_k10 | 0.243 | 904 | 2.74e+05 | 3.63 – 1.57e+05 | 0.057 | 0.036 | 1.44e+04 |
| conservative_k2 | 0.726 | 2.71e+03 | 8.16e+05 | 10.9 – 4.71e+05 | 0.033 | 0.024 | 4.32e+04 |
| conservative_k3 | 0.623 | 2.33e+03 | 7.00e+05 | 9.36 – 4.05e+05 | 0.035 | 0.026 | 3.7e+04 |
| conservative_k5 | 0.466 | 1.74e+03 | 5.24e+05 | 6.98 – 3.02e+05 | 0.041 | 0.028 | 2.77e+04 |
| optimistic_k1 | 0.865 | 3.24e+03 | 9.73e+05 | 13 – 5.64e+05 | 0.030 | 0.022 | 5.15e+04 |
| optimistic_k10 | 0.281 | 1.05e+03 | 3.18e+05 | 4.23 – 1.84e+05 | 0.053 | 0.034 | 1.67e+04 |
| optimistic_k2 | 0.751 | 2.81e+03 | 8.45e+05 | 11.3 – 4.90e+05 | 0.032 | 0.024 | 4.47e+04 |
| optimistic_k3 | 0.655 | 2.45e+03 | 7.38e+05 | 9.88 – 4.27e+05 | 0.034 | 0.025 | 3.9e+04 |
| optimistic_k5 | 0.505 | 1.89e+03 | 5.70e+05 | 7.61 – 3.29e+05 | 0.039 | 0.028 | 3.01e+04 |

## Similarity-weight variants — nathan_headline_no_superhab

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 3.03e+03 | 9.09e+05 | 12.1 – 5.26e+05 | 0.031 | 0.023 | 4.79e+04 |
| conservative_k10 | 0.243 | 860 | 2.60e+05 | 3.44 – 1.50e+05 | 0.058 | 0.036 | 1.36e+04 |
| conservative_k2 | 0.726 | 2.59e+03 | 7.76e+05 | 10.4 – 4.49e+05 | 0.034 | 0.025 | 4.09e+04 |
| conservative_k3 | 0.623 | 2.22e+03 | 6.66e+05 | 8.9 – 3.85e+05 | 0.036 | 0.026 | 3.51e+04 |
| conservative_k5 | 0.466 | 1.66e+03 | 4.98e+05 | 6.64 – 2.88e+05 | 0.042 | 0.029 | 2.62e+04 |
| optimistic_k1 | 0.865 | 3.09e+03 | 9.25e+05 | 12.4 – 5.37e+05 | 0.031 | 0.023 | 4.88e+04 |
| optimistic_k10 | 0.281 | 1e+03 | 3.03e+05 | 4.03 – 1.75e+05 | 0.054 | 0.035 | 1.58e+04 |
| optimistic_k2 | 0.751 | 2.68e+03 | 8.04e+05 | 10.7 – 4.67e+05 | 0.033 | 0.024 | 4.24e+04 |
| optimistic_k3 | 0.655 | 2.34e+03 | 7.02e+05 | 9.4 – 4.07e+05 | 0.035 | 0.026 | 3.7e+04 |
| optimistic_k5 | 0.505 | 1.8e+03 | 5.42e+05 | 7.25 – 3.15e+05 | 0.040 | 0.028 | 2.86e+04 |

## Similarity-weight variants — nathan_headline_no_tooluse

p = ESI^k per body; weight = bootstrap mean over the Archive HZ-rocky ESI population (conservative n=26 / optimistic n=41). Exact rescaling of the same draws (N is linear in the weight).

| population, exponent | median weight | median N_now | mean | 10th–90th | P(N<1) | P(1<=N<=3) | median N_ever |
|---|---|---|---|---|---|---|---|
| conservative_k1 | 0.850 | 964 | 5.10e+05 | 2.83 – 2.24e+05 | 0.065 | 0.038 | 4.71e+04 |
| conservative_k10 | 0.243 | 274 | 1.46e+05 | 0.803 – 6.39e+04 | 0.109 | 0.051 | 1.34e+04 |
| conservative_k2 | 0.726 | 823 | 4.36e+05 | 2.41 – 1.92e+05 | 0.069 | 0.039 | 4.02e+04 |
| conservative_k3 | 0.623 | 706 | 3.74e+05 | 2.07 – 1.65e+05 | 0.074 | 0.041 | 3.45e+04 |
| conservative_k5 | 0.466 | 527 | 2.80e+05 | 1.55 – 1.23e+05 | 0.084 | 0.043 | 2.58e+04 |
| optimistic_k1 | 0.865 | 982 | 5.20e+05 | 2.88 – 2.29e+05 | 0.064 | 0.037 | 4.79e+04 |
| optimistic_k10 | 0.281 | 319 | 1.70e+05 | 0.937 – 7.42e+04 | 0.103 | 0.050 | 1.56e+04 |
| optimistic_k2 | 0.751 | 853 | 4.52e+05 | 2.5 – 1.99e+05 | 0.068 | 0.039 | 4.16e+04 |
| optimistic_k3 | 0.655 | 744 | 3.94e+05 | 2.18 – 1.73e+05 | 0.073 | 0.040 | 3.63e+04 |
| optimistic_k5 | 0.505 | 573 | 3.04e+05 | 1.68 – 1.33e+05 | 0.081 | 0.043 | 2.8e+04 |

## nathan_headline: effect of each new factor (paired draws: per comparison (see table))

| comparison | median N_now of comparison | nathan_headline median / comparison median | per-sample log10(N_headline/N_comparison): median [10th, 90th] |
|---|---|---|---|
| without superhabitability (tool-use change only) | 3.03e+03 | ×1.05 | 0.011 [0.001, 0.056] |
| without cross-lineage tool use (superhab only) | 964 | ×3.30 | 0.555 [0.168, 0.782] |
| without both (= similarity_weighted) | 895 | ×3.55 | n/a (independent draws; compare medians) |

## Spacing: equal-cube side and median nearest-neighbour distance (disk volume ~7.9e12 ly³, user-supplied)

Cube side = (V/N)^(1/3). Nearest-neighbour: random (Poisson) placement; 3D median r = (3 ln2/(4πn))^(1/3), or the thin-disk 2D form when r exceeds the 1,000-ly thickness (R = 50,000 ly). Values for N < 1 mean no neighbour is expected; they are shown only formally.

| scenario | median N | cube side at median (ly) | median NN distance at median (ly) | regime | NN at 90th-pct N (ly) | NN at 10th-pct N (ly) |
|---|---|---|---|---|---|---|
| baseline | 0.00238 | 1.49e+05 | 8.53e+05 (N<1: none expected) | 2D thin disk | 1.29e+04 | 6.37e+07 (N<1: none expected) |
| baseline_no_exomoons | 0.00187 | 1.62e+05 | 9.64e+05 (N<1: none expected) | 2D thin disk | 1.44e+04 | 7.33e+07 (N<1: none expected) |
| snyder_beattie_priors | 5.51e-21 | 1.13e+11 | 5.61e+14 (N<1: none expected) | 2D thin disk | 1.29e+10 (N<1: none expected) | 2.20e+19 (N<1: none expected) |
| user_inputs | 9.93e-05 | 4.30e+05 | 4.18e+06 (N<1: none expected) | 2D thin disk | 8.31e+04 (N<1: none expected) | 2.10e+08 (N<1: none expected) |
| user_fast_intelligence | 571 | 2.4e+03 | 1.74e+03 | 2D thin disk | 185 | 4.85e+04 (N<1: none expected) |
| similarity_weighted | 895 | 2.07e+03 | 1.39e+03 | 2D thin disk | 185 | 2.54e+04 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 74.6 | 41 | 3D | 13.4 | 195 |
| earth_random_draw | 157 | 3.69e+03 | 3.32e+03 | 2D thin disk | 281 | 8.77e+04 (N<1: none expected) |
| nathan_headline | 3.18e+03 | 1.35e+03 | 744 | 3D | 133 | 1.16e+04 |
| nathan_headline_no_superhab | 3.03e+03 | 1.38e+03 | 756 | 3D | 135 | 1.2e+04 |
| nathan_headline_no_tooluse | 964 | 2.02e+03 | 1.34e+03 | 2D thin disk | 180 | 2.48e+04 |
| classic_static_SDO_style | 28.8 | 6.49e+03 | 7.75e+03 | 2D thin disk | 95.7 | 2.35e+34 (N<1: none expected) |

## Comparison with the user's claims

| scenario | median N_now | P(1<=N_now<=3) ('1-3 at a time') | P(N_now>=1) | median N_ever by now | P(50<=N_ever<=100) | P(N_ever>=50) |
|---|---|---|---|---|---|---|
| baseline | 0.00238 | 0.042 | 0.180 | 0.851 | 0.038 | 0.230 |
| baseline_no_exomoons | 0.00187 | 0.041 | 0.171 | 0.66 | 0.036 | 0.217 |
| snyder_beattie_priors | 5.51e-21 | 0.000 | 0.001 | 4.70e-18 | 0.000 | 0.001 |
| user_inputs | 9.93e-05 | 0.021 | 0.066 | 0.875 | 0.039 | 0.233 |
| user_fast_intelligence | 571 | 0.042 | 0.890 | 967 | 0.047 | 0.723 |
| similarity_weighted | 895 | 0.038 | 0.933 | 4.39e+04 | 0.014 | 0.982 |
| similarity_weighted_no_rare_earth | 1.90e+07 | 0.000 | 1.000 | 7.87e+08 | 0.000 | 1.000 |
| earth_random_draw | 157 | 0.057 | 0.841 | 1.2e+04 | 0.030 | 0.924 |
| nathan_headline | 3.18e+03 | 0.022 | 0.970 | 5.06e+04 | 0.013 | 0.984 |
| nathan_headline_no_superhab | 3.03e+03 | 0.023 | 0.969 | 4.79e+04 | 0.013 | 0.983 |
| nathan_headline_no_tooluse | 964 | 0.038 | 0.935 | 4.71e+04 | 0.013 | 0.982 |

## Exomoon effect (paired, same draws)
Median N_now with exomoons 0.00238 vs without 0.00187; per-sample log10(N_with/N_without): median 0.008 dex, 90th pct 0.343, 99th pct 1.146. Median share of G/K habitable bodies that are moons: 0.0241 (90th pct 0.608).


## Deterministic best-estimate point calculations

All parameters at their `best` values; hard-step expected times set equal to Earth's observed intervals (a 'Copernican / Earth-is-typical' choice).

| scenario | N_now | time-avg N | N_ever by now | fraction from G/K hosts |
|---|---|---|---|---|
| baseline | 3.31e+03 | 1.93e+03 | 8.26e+04 | 0.733 |
| baseline_no_exomoons | 3.24e+03 | 1.89e+03 | 8.09e+04 | 0.733 |
| snyder_beattie_priors | 3.31e+03 | 1.93e+03 | 8.26e+04 | 0.733 |
| user_inputs | 86.5 | 41.8 | 8.63e+04 | 0.82 |
| user_fast_intelligence | 5.44e+04 | 2.79e+04 | 9.17e+04 | 0.825 |
| similarity_weighted | 2.81e+03 | 1.64e+03 | 7.02e+04 | 0.733 |
| similarity_weighted_no_rare_earth | 5.63e+06 | 3.29e+06 | 1.41e+08 | 0.733 |
| earth_random_draw | 3.31e+03 | 1.93e+03 | 8.26e+04 | 0.733 |
| nathan_headline | 1.3e+04 | 8.01e+03 | 7.82e+04 | 0.754 |
| nathan_headline_no_superhab | 1.25e+04 | 7.67e+03 | 7.47e+04 | 0.745 |
| nathan_headline_no_tooluse | 2.91e+03 | 1.71e+03 | 7.34e+04 | 0.743 |

## Sensitivity — baseline

ESS = 68255 of 1000000 samples. Median share of N_now from G/K hosts: 0.749. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.450 | -0.52 | -4.65 | 4.13 |
| l_stone_yr | +0.363 | -4.71 | -1.24 | 3.46 |
| f_land_and_ocean | +0.350 | -4.22 | -0.90 | 3.32 |
| tau_eukaryogenesis | -0.278 | -1.57 | -4.25 | 2.69 |
| tau_abiogenesis | -0.269 | -1.61 | -4.14 | 2.53 |
| tau_complex_multicellularity | -0.252 | -1.51 | -3.90 | 2.38 |
| tau_oxygenic_photosynthesis_GOE | -0.252 | -1.50 | -3.87 | 2.37 |
| f_plate_tectonics | +0.190 | -3.53 | -1.80 | 1.74 |
| r_ster0_per_gyr | -0.139 | -2.20 | -3.83 | 1.63 |
| f_large_moon | +0.135 | -3.20 | -1.92 | 1.28 |
| f_jupiter_shield | +0.099 | -3.11 | -2.12 | 0.99 |
| m_recurrence | -0.106 | -2.05 | -2.95 | 0.90 |
| f_ghz | +0.092 | -3.05 | -2.19 | 0.86 |
| th_gk_gyr | +0.081 | -3.05 | -2.33 | 0.73 |
| f_m_flares | +0.048 | -2.87 | -2.34 | 0.53 |

## Sensitivity — baseline_no_exomoons

ESS = 68255 of 1000000 samples. Median share of N_now from G/K hosts: 0.729. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 0.50 -> posterior 0.19; posterior P(tau_intelligence<5 Gyr) = 0.36.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| tau_stone_tool_intelligence | -0.448 | -0.62 | -4.76 | 4.14 |
| l_stone_yr | +0.362 | -4.79 | -1.35 | 3.44 |
| f_land_and_ocean | +0.348 | -4.33 | -1.02 | 3.31 |
| tau_eukaryogenesis | -0.277 | -1.67 | -4.35 | 2.68 |
| tau_abiogenesis | -0.268 | -1.71 | -4.22 | 2.51 |
| tau_oxygenic_photosynthesis_GOE | -0.251 | -1.60 | -3.98 | 2.38 |
| tau_complex_multicellularity | -0.251 | -1.64 | -4.00 | 2.37 |
| f_plate_tectonics | +0.189 | -3.64 | -1.90 | 1.74 |
| r_ster0_per_gyr | -0.139 | -2.32 | -3.93 | 1.60 |
| f_large_moon | +0.157 | -3.44 | -1.95 | 1.49 |
| f_jupiter_shield | +0.115 | -3.30 | -2.16 | 1.14 |
| m_recurrence | -0.106 | -2.16 | -3.08 | 0.92 |
| f_ghz | +0.091 | -3.16 | -2.29 | 0.87 |
| th_gk_gyr | +0.078 | -3.16 | -2.43 | 0.73 |
| f_m_flares | +0.050 | -2.96 | -2.42 | 0.54 |

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

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.837. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.606 | 1.88 | 5.24 | 3.36 |
| l_stone_yr | +0.497 | 1.70 | 4.42 | 2.73 |
| f_plate_tectonics | +0.315 | 2.64 | 4.40 | 1.76 |
| f_large_moon | +0.225 | 2.90 | 4.18 | 1.28 |
| m_recurrence | -0.207 | 4.02 | 2.83 | 1.18 |
| r_ster0_per_gyr | -0.164 | 3.77 | 2.76 | 1.01 |
| f_ghz | +0.158 | 3.05 | 3.96 | 0.91 |
| f_jupiter_shield | +0.157 | 3.07 | 3.95 | 0.87 |
| ne_gk | +0.095 | 3.24 | 3.81 | 0.57 |
| th_gk_gyr | +0.086 | 3.18 | 3.68 | 0.50 |
| f_exomoon_host | +0.066 | 3.41 | 3.87 | 0.46 |
| f_m_habitable | +0.057 | 3.38 | 3.70 | 0.32 |
| f_m_flares | +0.058 | 3.39 | 3.70 | 0.31 |
| tau_stone_tool_intelligence | -0.041 | 3.63 | 3.39 | 0.24 |
| n_tool_origins | +0.041 | 3.39 | 3.63 | 0.24 |

## Sensitivity — nathan_headline_no_superhab

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.827. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.606 | 1.86 | 5.21 | 3.36 |
| l_stone_yr | +0.497 | 1.67 | 4.40 | 2.73 |
| f_plate_tectonics | +0.315 | 2.61 | 4.38 | 1.76 |
| f_large_moon | +0.224 | 2.88 | 4.16 | 1.28 |
| m_recurrence | -0.207 | 3.99 | 2.81 | 1.18 |
| r_ster0_per_gyr | -0.165 | 3.75 | 2.74 | 1.01 |
| f_ghz | +0.158 | 3.03 | 3.94 | 0.91 |
| f_jupiter_shield | +0.156 | 3.05 | 3.93 | 0.87 |
| ne_gk | +0.094 | 3.23 | 3.78 | 0.55 |
| th_gk_gyr | +0.085 | 3.16 | 3.66 | 0.50 |
| f_exomoon_host | +0.068 | 3.38 | 3.85 | 0.47 |
| f_m_habitable | +0.059 | 3.35 | 3.69 | 0.34 |
| f_m_flares | +0.060 | 3.36 | 3.69 | 0.33 |
| tau_stone_tool_intelligence | -0.041 | 3.61 | 3.38 | 0.23 |
| n_tool_origins | +0.041 | 3.38 | 3.61 | 0.23 |

## Sensitivity — nathan_headline_no_tooluse

ESS = 200000 of 200000 samples. Median share of N_now from G/K hosts: 0.833. Median epoch of peak N(t): 0.01 Gyr ago. Median mean-age of habitable planets: 7.43 Gyr.
P(tau_abiogenesis<1 Gyr): prior 1.00 -> posterior 1.00; posterior P(tau_intelligence<5 Gyr) = 1.00.

| parameter | Spearman rho vs log10 N | median log10N (param low 10%) | (param high 10%) | swing (dex) |
|---|---|---|---|---|
| f_land_and_ocean | +0.570 | 1.35 | 4.70 | 3.35 |
| l_stone_yr | +0.560 | 1.00 | 4.16 | 3.16 |
| f_plate_tectonics | +0.297 | 2.12 | 3.88 | 1.76 |
| m_recurrence | -0.238 | 3.63 | 2.21 | 1.42 |
| f_large_moon | +0.213 | 2.39 | 3.67 | 1.28 |
| r_ster0_per_gyr | -0.161 | 3.26 | 2.21 | 1.05 |
| f_ghz | +0.149 | 2.53 | 3.44 | 0.91 |
| f_jupiter_shield | +0.148 | 2.54 | 3.44 | 0.90 |
| ne_gk | +0.090 | 2.72 | 3.29 | 0.56 |
| th_gk_gyr | +0.086 | 2.65 | 3.17 | 0.52 |
| f_exomoon_host | +0.062 | 2.88 | 3.33 | 0.45 |
| f_m_habitable | +0.055 | 2.87 | 3.19 | 0.32 |
| f_m_flares | +0.056 | 2.86 | 3.18 | 0.32 |
| r_self_per_gyr | -0.029 | 3.03 | 2.82 | 0.20 |
| m_disk_now | +0.030 | 2.88 | 3.08 | 0.20 |
