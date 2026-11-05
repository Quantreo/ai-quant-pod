---
type: technique
brick: signal
aliases: [Absolute plus relative momentum, Dual momentum asset allocation, Antonacci dual momentum, Absolute and relative strength]
sources: 1
tested_on: [multi-asset]
---

# Dual momentum

> [!summary]
> Ranks asset classes on past return and holds only the winners that also pass an absolute momentum test, else a safe asset.

## How it works

- **Inputs**: past return of each asset class over a lookback, and a safe asset.
- **Formula**: relative step ranks the assets on past return; absolute step keeps a selected asset only if its own momentum passes a trend test (positive excess return, or price above a moving average).
- **Lookback / holding**: a lookback in months; reviewed at a monthly rebalance.
- **Output**: a set of held assets, the rest in the safe asset.
- **Direction**: long only.
- **Tested on**: ETFs across equities, bonds, real assets and cash.

## What the sources say

### Parameters
- **Prior-Sanz 2026**
	- Lookbacks, number of assets held and safe asset are not stated; they are set by each published design (p. 3, 6).
	- Coded as dual when a strategy uses both absolute and relative momentum (p. 7).
	- Monthly, month-end close, 0.2% round trip (p. 6).
	- 37 of the 86 strategies are plain dual momentum or dual momentum with a breadth or optimised-weight add-on (Table 1, computed from groups 2 to 4).

### Why
- **Prior-Sanz 2026**: pairing relative strength with an absolute filter harvests risk premia more efficiently than either alone; cited from Antonacci, not tested (p. 3).

### Evidence
- **Prior-Sanz 2026**: real data, vendor-run rules, 1995-April 2025, net of 0.2% round trip
	- Group 2 (14 strategies, no filters): Sharpe 0.72, MaxDD -16.7% against 0.61 and -23.6% for static allocations (p. 26).
	- Sharpe gap +0.11 against the static group, p = 0.123, not significant; indicative figure (Table 13).
	- Dual dummy in the 30-year Sharpe regression: -0.05 (0.07), not significant; in the 2020-23 window -0.43*** (Tables 4, 10).
	- 2008-09: dual, absolute and relative strategies had negative median Sharpe with large dispersion (p. 21).

### Limits
- **Prior-Sanz 2026**
	- No rule is given, only group averages; per-strategy results are not tabulated.
	- Dual dummy variance inflation factor 8.78, above the threshold of 5 by construction (Table 12).
	- Dual momentum adds spread in Sharpe, not a higher median (p. 12).

## Sources

- [[2026 - Prior-Sanz Vizuete-Luciano Cruz-Zayash et al - The long-term efficiency of tactical asset allocation Evidence from 86 systematic strategies (1995-2025)]] (Prior-Sanz 2026)
