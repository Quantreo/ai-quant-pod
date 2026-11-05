---
type: technique
brick: sizing
aliases: [diversified reward-risk parity, ratio-proportional weights, Sharpe-weighted portfolio, Calmar-weighted portfolio, STAR ratio weights, Rachev ratio weights]
sources: 1
tested_on: [equities]
---

# Reward-risk parity weighting

> [!summary]
> Weights each asset in proportion to its own past reward-risk ratio (Sharpe, Calmar, STAR, Rachev), floored at zero and normalised to sum to 1, with no optimiser.

## How it works

- **Rule**: w_i = f(ρ_i) / Σ f(ρ_j), with ρ the asset's reward-risk ratio over a trailing window. Raw form f = max(ρ, 0). Linear form f = max(1 + ρ, 0), which stays close to equal weight.
- **Risk estimate**: the ratio's own risk term: standard deviation, maximum drawdown, or CVaR; estimated from raw history or a fitted time-series model.
- **Aggregation**: weights sum to 1, long-only; assets with a negative ratio get zero (raw form).
- **Implied leverage**: 1 by construction, no volatility target.
- **Variant**: pure risk measures use 1/ρ or 1 − ρ instead (see [[Volatility targeting]]).

## What the sources say

### Parameters
- **Choi 2021**
	- Ratios: Sharpe (marginal and conditional), Calmar over 6 months, STAR (CVaR 90/95/99%), Rachev (several tail pairs) (p. 7-10).
	- Raw rule max(ρ, 0); linear rule max(1 + ρ, 0) (Table 2, p. 12, 24).
	- Window: last 6 months of daily data; hold 6 months, a sixth of the book re-set monthly (p. 12).
	- Dow Jones constituents, also indexes, funds, ETFs, sector ETFs, 1999-2020 (p. 11-12).
	- Risk-free: 91-day T-bill (p. 12).

### Why
- **Choi 2021**: investors prefer assets with better reward per unit of risk, and the rule is simple like equal weight (p. 3, 5-6).

### Evidence
- **Choi 2021**: real data, in-sample, gross, Dow Jones 1999-2020, against equal weight (Tables 3, 5)
	- Raw Calmar: mean 10.32% vs 9.84%, Sharpe 0.5524 vs 0.4967, max drawdown 39.46% vs 57.81%, turnover 66.07% vs 6.75%.
	- Raw Sharpe: Sharpe 0.5136, CVaR 1.62 vs 1.26, turnover 58.46%.
	- Linear rules: Sharpe 0.497 to 0.516, turnover 5.79% (Sharpe) to 26.33% (Calmar).
	- Raw Sharpe Carhart monthly alpha 0.1628, not significant, vs 0.2129 for equal weight; momentum beta +0.1253.

### Limits
- **Choi 2021**
	- No transaction costs; raw rules turn over 13% to 69% against 6.75% (Table 3).
	- VaR and CVaR of the raw Sharpe and Calmar rules are worse than equal weight (Table 3).
	- No significance test of the gap to equal weight; one window and one holding scheme.
	- Only the Dow Jones table is shown; other universes described in words (p. 15).

## Sources

- [[2021 - Choi Kim Kim - Diversified reward-risk parity in portfolio construction]] (Choi 2021)
