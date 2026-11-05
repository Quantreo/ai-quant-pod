---
type: diagnostic
kind: performance
aliases: [drop one asset at a time, jackknife by asset, influential asset check, cross-validation by currency]
sources: 1
---

# Leave-one-out asset exclusion

> [!summary]
> Does the result survive the removal of any single asset from the universe?

## How it works

- **How**: rerun the strategy once per asset, each time with that asset removed from the universe. Record mean return, t-statistic and Sharpe ratio of each run.
- **Reading**: look at the worst run. A large drop when one asset leaves means the result leans on that asset.
- **Data needed**: the strategy, its universe and returns.

## What the sources say

### Parameters
- **Menkhoff 2016**
	- 22 runs, one per currency, rank portfolios on the fundamental-adjusted value signal (Table A.III, p. 22).
	- Repeated for the four ways of measuring fundamentals (Table A.III).

### Why
- **Menkhoff 2016**: to rule out that one particular currency drives the main result (p. 22).

### Evidence
- **Menkhoff 2016**: real data, 1976-2013, gross.
	- Mean 3.40% to 5.24% a year, Sharpe 0.67 to 0.96, over all runs (Table A.III).
	- Worst run: Korea removed, raw fundamentals, 3.40% (t 4.12), Sharpe 0.67 (Table A.III).
	- Full-sample reference: Sharpe 0.79 to 0.91 (Table 5).

### Limits
- **Menkhoff 2016**
	- One asset at a time only (Table A.III).
	- Run on the adjusted signal only, not on the standard value signal (Table A.III).

## Sources

- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
