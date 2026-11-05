---
type: diagnostic
kind: performance
aliases: [Kelly-Pruitt placebo test, Simulated predictor placebo, Stambaugh bias bootstrap, OOS R2 critical values]
sources: 1
---

# Placebo predictor R2 test

> [!summary]
> Is the out-of-sample R² of a predictive regression larger than what random predictors with the same persistence would give?

## How it works

- **How**: simulate predictors as AR(1) processes with the same mean, autocorrelation and covariance as the real ones, independent of returns. Build out-of-sample forecasts of the real returns with them and record the R². Repeat many times and take percentiles as critical values. A second check simulates data from a VAR(1) with no predictability, with resampled errors, to get the small-sample bias and bootstrap p-values.
- **Reading**: an observed R² above the 95th percentile of the placebo is unlikely to come from persistence and finite-sample bias alone.
- **Data needed**: the predictors, the returns, and a split between estimation and test periods.

## What the sources say

### Parameters
- **Haddad 2020**
	- Placebo: six AR(1) processes matched on the first half of the data, 1,000 repetitions; 90th, 95th and 99th percentiles (p. 23)
	- Bootstrap: restricted VAR(1), 10,000 histories, errors resampled from the empirical distribution (p. 20-21)
	- Out-of-sample R² = 1 minus var(r - forecast) over var(r), coefficients from the first half (p. 21)

### Why
- **Haddad 2020**: valuation ratios are persistent and their innovations correlate with returns, which biases predictive coefficients upward (Stambaugh) (p. 21, A4)

### Evidence
- **Haddad 2020**: real data, 1974-2017, gross
	- 95th percentile critical values: market 0.68, PC1 0.97, PC2 0.48, PC3 0.37, PC4 1.19, PC5 0.96 (Table 2)
	- Observed out-of-sample R²: 1.00, 4.82, 0.97, 0.47, 3.52, 0.55; all beat the 95th percentile except PC5 (Table 2, p. 23)
	- Bias is 0.68 for the market coefficient 0.76 and 0.36 for PC1 coefficient 4.32 (Table 2)

### Limits
- **Haddad 2020**
	- Out-of-sample significance holds for the split sample; PC2, PC3 and the market turn negative in expanding and rolling windows (Table A.1)
	- Matched moments come from the first half only (p. 23)

## Sources

- [[2020 - Haddad Kozak Santosh - Factor Timing]] (Haddad 2020)
