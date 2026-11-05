---
type: technique
brick: sizing
aliases: [GARCH-DCC-Copula, ARMA-GARCH-DCC-t-copula, copula risk model, simulated scenario risk model, dynamic correlation tail dependence risk model]
sources: 1
tested_on: [multi-asset]
---

# GARCH-copula risk model

> [!summary]
> Estimates volatility, correlation and tail dependence of a set of assets by simulation, to feed the weights of a risk-based portfolio.

## How it works

- **Rule**: weights come from a risk-based allocation rule (inverse volatility, risk parity, minimum variance, minimum CVaR, maximum diversification). The risk inputs come from simulated returns, not from the sample.
- **Risk estimate**: per asset, a mean model and a GARCH variance; a dynamic conditional correlation on the residuals; a t-copula for tail dependence. Simulate many paths of the next month, then compute covariance or CVaR from them.
- **Aggregation**: the allocation rule applied to the simulated risk; the model is refit each month on an expanding window.
- **Implied leverage**: none, weights sum to 1, long only.

## What the sources say

### Parameters
- **Luo 2013**
	- ARMA(1,1) mean and GARCH(1,1) variance per asset; DCC on the residuals; t-copula on the DCC residuals (p. 18)
	- Monthly expanding-window refit, first fit on about five years of daily data (p. 18)
	- 21-day paths, 10,000 simulations; "not fine tuned" (p. 19, 26)

### Why
- **Luo 2013**: returns show serial correlation, volatility clustering, outliers, changing correlation and tail dependence, which a sample covariance misses (p. 7-8, 18)

### Evidence
- **Luo 2013**: real data, monthly refits (ex-ante), gross or net not stated
	- 11 assets, nine risk-based rules, average Sharpe ≈1.14 rolling, ≈1.19 expanding, ≈1.27 copula model (≈ Fig. 35)
	- Factors, risk parity Sharpe 0.54 rolling vs 0.60 copula (Fig. 93-94)
	- Equities-commodities tail dependence 28% against correlation 19% (Fig. 19)

### Limits
- **Luo 2013**
	- Risk parity Sharpe ≈1.32 vs ≈1.37 rolling; max diversification equal (≈ Fig. 35)
	- Average CVaR of alpha strategies ≈-24% vs ≈-22% with the expanding window (≈ Fig. 78)
	- Structure chosen on the full sample; no costs, turnover or significance test (whole paper)
	- A more accurate risk model does not always give a better portfolio (p. 21)

## Sources

- [[2025 - Luo Wang Jussa - Dynamic allocation extremes, tail dependence, and regime Shifts]] (Luo 2013)
