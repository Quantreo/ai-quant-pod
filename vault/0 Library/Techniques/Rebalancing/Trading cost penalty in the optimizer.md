---
type: technique
brick: rebalancing
aliases: [Trade aversion term, Turnover penalty, L1 trading cost term, Linear transaction cost term]
sources: 1
tested_on: [multi-asset]
---

# Trading cost penalty in the optimizer

> [!summary]
> Subtracts the expected linear trading cost from the optimiser objective, so weights move only when the gain is worth the cost.

## How it works

- **Frequency or trigger**: evaluated at every rebalance, inside a single-period optimisation.
- **Band**: none fixed; the penalty is the one-way cost rate times the sum of absolute weight changes from the previous weights, times a trade aversion parameter.
- **Cost rationale**: stops trading on noise in the return forecasts. A parameter of 0 removes the term.

## What the sources say

### Parameters
- **Shu 2024**
	- Term: gamma_trade times a times the L1 norm of (w minus previous weights), a = 5 bp one-way (Eq. 2, p. 17)
	- gamma_trade = 1 for the regime-aware MinVar and MV; 0 for plain MV; plain MinVar has no term (p. 19)
	- Daily rebalancing, 12 asset indexes, long-only (p. 17, 20)

### Why
- **Shu 2024**: prevents excessive trading and lowers sensitivity to noise in forecasts; a minimal solution, multi-period models would be better (p. 18)

### Evidence
- **Shu 2024**: real data, walk-forward 2007-2023, MinVar with regime inputs, net of 5 bp
	- Turnover 11.80 without the term, 2.06 with it (Table 8, p. 27)
	- Sharpe 1.02 without, 1.12 with; MDD -12.8% against -7.1% (Table 8)

### Limits
- **Shu 2024**
	- Only gamma_trade 0 and 1 compared; one portfolio (Table 8)
	- Turnover unit not defined (p. 24)

## Sources

- [[2024 - Shu Yu Mulvey - Dynamic Asset Allocation with Asset-Specific Regime Forecasts]] (Shu 2024)
