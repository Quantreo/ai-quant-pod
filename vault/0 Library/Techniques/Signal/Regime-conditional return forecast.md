---
type: technique
brick: signal
aliases: [Regime-conditional Sharpe forecast, Regime-weighted expected return, Probabilistic regime conditioning, Naive regime forecast]
sources: 1
tested_on: [equities]
---

# Regime-conditional return forecast

> [!summary]
> Forecasts each asset's next-month return from its past performance in the months that share the regime expected next.

## How it works

- **Inputs**: a monthly regime probability vector, a regime transition matrix, monthly asset returns.
- **Formula**: next-month regime probabilities = current probabilities times the transition matrix. Forecast = the asset's mean return or Sharpe ratio in past months of the most likely regime, or the probability-weighted sum over regimes of a per-regime model.
- **Lookback / holding**: a fixed estimation window, forecast one period ahead.
- **Output**: one forecast per asset, to be ranked or turned into weights.
- **Direction**: assets with high past performance in the expected regime get high forecasts.
- **Tested on**: equity ETFs.
- **Variant**: per-regime ridge regression of asset returns on macro features, averaged with the next-regime probabilities.

## What the sources say

### Parameters
- **Oliveira 2025**
	- Next-regime distribution: current distribution times the transition matrix of counted regime changes (Eq. 5, 7, p. 6, 13)
	- Naive: Sharpe ratio of the asset in past months of the most likely next regime (Eq. 8-10, p. 14)
	- Ridge: per regime and asset, returns on macro features of that regime, averaged by next-regime probabilities (Eq. 12-14, p. 14-15)
	- Fixed 48-month window, monthly, one month ahead; 10 US ETFs (p. 16)

### Why
- **Oliveira 2025**: fixing the current regime to the most likely one ignores its uncertainty and gives identical forecasts for months in the same regime (p. 13)

### Evidence
- **Oliveira 2025**: real data, walk-forward, gross, 2004 to 2022
	- Ridge long-only, l = 3: Sharpe 1.505 against 0.818 for SPY and 0.838 equal weight (Table 6)
	- Naive long-only, l = 4: Sharpe 1.065 (Table 4)
	- Against random regimes, ridge Sharpe p = 0.004, naive Sharpe p = 0.082 (Fig. 7, 9, p. 16-17)

### Limits
- **Oliveira 2025**
	- Eq. 8 and Eq. 14 index regimes 1 to r+1 and 1 to r, while regimes run from 0 to r (p. 14-15)
	- Regime estimation inside the window not stated (p. 7, 16)
	- No costs and no hold-out (whole paper)

## Sources

- [[2025 - Oliveira Sandfelder Fujita et al - Tactical Asset Allocation with Macroeconomic Regime Detection]] (Oliveira 2025)
