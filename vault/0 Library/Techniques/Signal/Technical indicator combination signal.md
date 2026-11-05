---
type: technique
brick: signal
aliases: [CTREND, Trend factor, Aggregate trend signal, Combined elastic net forecast, CS-C-ENet, Forecast combination of technical indicators]
sources: 1
tested_on: [crypto]
---

# Technical indicator combination signal

> [!summary]
> Turns many technical indicators into one expected-return forecast per asset, then sorts assets on it.

## How it works

- **Inputs**: a set of technical indicators per asset (oscillators, moving averages, volume, volatility bands) and past returns.
- **Formula**: rank-transform each indicator; estimate a cross-sectional return forecast from each indicator; keep the informative ones with a shrinkage step; average the kept forecasts.
- **Lookback / holding**: rolling estimation window; forecast for the next period; rebalance each period.
- **Output**: one forecast per asset; long the top quantile, short the bottom.
- **Direction**: long-short, relative.
- **Tested on**: cryptocurrencies.

## What the sources say

### Parameters
- **Fieberg 2025**
	- 28 indicators: rsi, stochastics, cci, price SMAs 3-200 days scaled by price, macd, volume SMAs, chaikin, Bollinger bands (p. 3122-3124)
	- Univariate Fama-MacBeth forecasts, WLS by market cap, coefficients averaged over 52 weeks (p. 3127-3129)
	- Elastic net, α = 0.5, λ by corrected AIC, keep forecasts with positive weight, equal average (p. 3128-3129)
	- Value-weighted quintiles, weekly, Apr 2015 to May 2022 (p. 3129)

### Why
- **Fieberg 2025**
	- Single indicators are noisy; combining avoids arbitrary indicator choice (p. 3126-3127)
	- Crypto lacks fundamentals, so investors infer value from past prices (p. 3120)

### Evidence
- **Fieberg 2025**: real data, forecast out of sample week by week, design fixed on full period
	- Top minus bottom quintile 3.87% a week, t = 5.19, Sharpe 1.94; LTW alpha 2.62% (Table 3)
	- Net 2.35% to 2.90% a week; turnover 68%; breakeven 1.41% (Table 9)
	- Top 100 coins: 3.39% gross (Table 8)

### Limits
- **Fieberg 2025**
	- Momentum beta 0.79 (Table 3)
	- Baseline Sharpe at the upper edge of 55,296 design variants; median 1.34 (p. 3138-3139)
	- 2-week rebalancing drops returns to 2.34%; insignificant beyond 4 weeks (p. 3148)

## Sources

- [[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns]] (Fieberg 2025)
