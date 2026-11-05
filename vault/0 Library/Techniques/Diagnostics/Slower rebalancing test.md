---
type: diagnostic
kind: performance
aliases: [Rebalancing frequency test, Turnover and slow trading check, Fully discrete rebalancing matrix]
sources: 2
---

# Slower rebalancing test

> [!summary]
> Does the strategy keep its performance when weights change less often, and how much does turnover fall?

## How it works

- **How**: rebuild the portfolio with weights held fixed for one, three, six or twelve months. For each version report the Sharpe ratio, the utility, average turnover and the correlation with the baseline version.
- **Reading**: if Sharpe and correlation hold up while turnover falls, the signal is persistent and the monthly trading is not what drives the result.
- **Data needed**: the signal history and the portfolio weights.

## What the sources say

### Parameters
- **Haddad 2020**
	- Pure anomaly timing portfolio rebalanced monthly, quarterly, semi-annually, annually (Table A.5)
	- Turnover each month = sum of absolute weight changes divided by the sum of absolute initial weights (A13)
- **Unknown 2026**
	- Five dominant rules at six frequencies: weekly, biweekly, monthly, quarterly, semiannual, annual (p. 11)
	- Fully discrete: entries, exits and stops evaluated only on rebalancing dates; portfolio frozen between them (p. 11)

### Why
- **Haddad 2020**: high-frequency movements in the predictors are not the main source of the result; gives a first view on implementability (p. 39)
- **Unknown 2026**: a typical retail investor trades less often than every two weeks (p. 11)

### Evidence
- **Haddad 2020**: real data, 1974-2017, gross
	- Sharpe 0.71 monthly, 0.72, 0.82, 0.79 annual (Table A.5)
	- Turnover 0.41, 0.20, 0.13, 0.08; correlation with the monthly version 1.00, 0.98, 0.92, 0.88 (Table A.5)
	- Expected utility falls from 1.26 to 0.81 (Table A.5)
- **Unknown 2026**: authors' statement, no table shown
	- From monthly rebalancing on, no active rule beats passive investing (p. 23-24)

### Limits
- **Haddad 2020**
	- No transaction cost model, so implementability is not settled (p. 39, A13)
	- Compared with hedge fund turnover of 8.5% a month from other work, not tested here (A13)
- **Unknown 2026**
	- The 30 simulations are described, not reported (p. 11, 23-24)

## Sources

- [[2020 - Haddad Kozak Santosh - Factor Timing]] (Haddad 2020)
- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
