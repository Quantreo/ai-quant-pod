---
type: diagnostic
kind: performance
aliases: [Jobson-Korkie test, Jobson-Korkie-Memmel test, Memmel correction, Paired Sharpe test]
sources: 1
---

# Sharpe ratio difference test

> [!summary]
> Is the Sharpe gap between two strategies on the same dates larger than sampling noise?

## How it works

- **How**: Z = (S_A - S_B) / sqrt(theta), with theta = (1/n) x [2 - 2 rho + 0.5 x (S_A^2 + S_B^2 - 2 S_A S_B rho^2)], rho the correlation of the two return series and n the number of observations. Z is compared with a standard normal, two-sided.
- **Reading**: a small p-value says the gap is unlikely to be noise for these two series. It does not account for how many rules were tried.
- **Data needed**: two return series on the same dates.

## What the sources say

### Parameters
- **Unknown 2026**
	- Weekly net returns, n up to 1,289; common sample when a benchmark lists later (Eq. 2, p. 9-11)
	- Applied to 63 filters, 144 SL/TP rules against SPY, and pairs among the leaders (p. 11)

### Why
- **Unknown 2026**: separates strategies that beat passive investing from those with a higher point Sharpe that cannot be told apart (p. 11)

### Evidence
- **Unknown 2026**: real data, in-sample, net of 20 bp per side
	- TSL07 against SPY: +0.812, p < 0.001 (Table 3 C)
	- TSL07 against MA_SMA200_OV_TP100: +0.016, p = 0.51 (Table 3 B)
	- C4 and C5 against C2 and C6: +0.056, p = 0.30 (Table 2 C)

### Limits
- **Unknown 2026**
	- p-values are not adjusted for 144 rules tried against SPY (p. 11)
	- The reported gaps against SPY do not match the Sharpe levels printed (Tables 2, 3)

## Sources

- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
