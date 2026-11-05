---
type: technique
brick: signal
aliases: [VRP, VRP regression forecast, implied minus realized variance, fear index signal, VRP and regime forecast]
sources: 1
tested_on: [multi-asset]
---

# Variance risk premium signal

> [!summary]
> Predicts next-month asset returns from the gap between implied and realised variance, optionally with a risk-regime dummy.

## How it works

- **Inputs**: an implied volatility index, realised variance of the same market from high-frequency returns, monthly asset returns. Optional: a high-risk regime flag.
- **Formula**: VRP = implied variance minus realised variance. Each month end, regress each asset's next-month return on lagged VRP (plus the regime flag); the fitted value is the forecast.
- **Lookback / holding**: rolling window for the regression, one-month horizon, VRP lagged one month.
- **Output**: a predicted return per asset, used as the expected return of an optimiser or to rank assets.
- **Direction**: high VRP is followed by higher returns on risky assets, low or negative VRP by lower.
- **Tested on**: equities, bonds, REITs, commodities, gold.

## What the sources say

### Parameters
- **Luo 2013**
	- VRP = VIX squared minus the realised variance of S&P 500 five-minute returns (p. 32)
	- Lagged one month; OLS per asset at each month end, 60-month rolling window (p. 31, 33; fn 19)
	- Regime variant: add I(P(high risk) >= 0.5) (p. 47)
	- 11 asset classes, 2003-2013 (Fig. 50)

### Why
- **Luo 2013**: high VRP is a panic state, the market overreacts, so risky assets are bought at extreme VRP and the reverse when VRP is low (p. 32)

### Evidence
- **Luo 2013**: real data, rolling refits, cross-sectional IC of forecasts against next-month returns, no portfolio costs
	- VRP only: IC average 7.1%, sd 46.3%, ratio 1.53 (Fig. 50, 73)
	- VRP and regime flag: IC average 10.1%, sd 43.8%, ratio 2.31 (Fig. 74)
	- Same on 5 equity factors: ratio 1.59 vs 1.88 (Fig. 103-104)

### Limits
- **Luo 2013**
	- Monthly IC sd is large against its mean; IC fell recently (Fig. 50, p. 33)
	- No test of the gain from the regime flag, no costs (whole paper)
	- Needs five-minute data; history before 2003 not described (p. 32)

## Sources

- [[2025 - Luo Wang Jussa - Dynamic allocation extremes, tail dependence, and regime Shifts]] (Luo 2013)
