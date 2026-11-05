---
type: diagnostic
kind: performance
aliases: [MEB, Paired bootstrap Sharpe test, Path sensitivity bootstrap, Holm-adjusted Sharpe comparison, Stationary block bootstrap Sharpe difference]
sources: 2
---

# Maximum entropy bootstrap Sharpe test

> [!summary]
> Do the strategy's results survive alternative return paths, and is its Sharpe ratio reliably different from a benchmark's?

## How it works

- **How**: resample each return series with the maximum entropy bootstrap, which keeps the temporal rank order and perturbs magnitudes. Rerun the whole strategy and the benchmark on each simulated panel. Compare Sharpe ratios in pairs, and adjust the p-values for the several comparisons made.
- **Reading**: the spread of cumulative return, Sharpe and drawdown over paths shows path sensitivity. A paired Sharpe difference that is not rejected is inconclusive, not equal.
- **Variant**: stationary block bootstrap of the two return series together; the p-value is the share of draws where the managed minus benchmark Sharpe gap is below zero.
- **Data needed**: monthly or daily returns per contract and the full strategy code, since the model is re-estimated on every path.

## What the sources say

### Parameters
- **Kosch 2026**
	- 500 paths, seed 42, 10% trim, boundary reaching on; each contract bootstrapped separately; all models refit on every path (p. 11)
	- Paired nonstudentized test on the Sharpe difference; p = (1 + count of |d* - d| ≥ |d|) / (B + 1), B = 500 (p. 11-12)
	- Holm correction across the three models in each of six families (p. 12)
	- Sharpe: arithmetic mean over sample standard deviation of monthly returns, times √12 (p. 11)

- **DeMiguel 2024**
	- Stationary block bootstrap (Politis, Romano 1994), 10,000 samples, mean block size 5, on the managed and unmanaged return series (fn 15, p. 12-13).
	- One-sided p-value: frequency of a Sharpe difference below zero (fn 15).
	- Where the difference is zero in every draw, p is set to 0.5 (fn 19).

### Why
- **Kosch 2026**
	- One backtest gives a single path; MEB suits ordered, possibly nonstationary data where i.i.d. resampling is not valid (p. 11)

- **DeMiguel 2024**: the Sharpe gap needs inference; three other tests are in the Internet Appendix (fn 15, p. 13).

### Evidence
- **Kosch 2026**: real data, 2016-2024
	- None of 18 paired Sharpe tests rejects after Holm; smallest adjusted p-value 0.192 (Table 4, p. 14)
	- Benchmark average Sharpe 0.191; classical SSA 0.131 on average with a median cumulative return of -11.30% (Table 3)
	- Average path results differ from the historical ones, e.g. DVR long Sharpe 0.095 against 0.245 historically (Tables 2, 3)

- **DeMiguel 2024**: real data, out of sample, net, 1977-2020
	- Multifactor Sharpe 1.062 against 0.940, p 0.006 (Table II).
	- Managed single factors: p 0.917 for the market, 0.097 for UMD, 0.029 for IA (Table I E).

### Limits
- **Kosch 2026**
	- Keeps temporal ranks, so it is not a null that destroys seasonal timing (p. 11)
	- Does not keep cross-contract dependence (p. 11)
	- The 500 paths are not independent market histories (p. 11)

- **DeMiguel 2024**
	- Series are resampled as given; the portfolio is not rebuilt on each draw, unlike Kosch 2026 (fn 15).

## Sources

- [[2026 - Kosch Forsberg - Seasonal Trading in Commodity Futures Evidence from Regression and Singular Spectrum]] (Kosch 2026)
- [[2024 - DeMiguel Martin-Utrera Uppal - A Multifactor Perspective on Volatility-Managed Portfolios]] (DeMiguel 2024)
