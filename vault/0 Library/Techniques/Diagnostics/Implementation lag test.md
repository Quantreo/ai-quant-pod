---
type: diagnostic
kind: performance
aliases: [signal delay test, publication lag test, execution lag, lagged signal, no-lag comparison, skip the most recent day]
sources: 4
---

# Implementation lag test

> [!summary]
> How much of the return survives when the portfolio is formed some periods after the signal date?

## How it works

- **How**: rerun the strategy with k extra periods between the date the signal is observed and the date the portfolio is formed. Compare mean, t-statistic and Sharpe ratio with the run without lag.
- **Reading**: a strategy that loses most of its return under a realistic delay depended on data not yet available at the signal date, or on information that decays fast.
- **Data needed**: signal and return history.

## What the sources say

### Parameters
- **Menkhoff 2016**
	- Two extra quarters, quarterly rebalance (p. 23; Table A.V).
	- Applied to the standard, fitted and residual value signals, linear and rank weights (Table A.V).
- **Fil 2020**
	- One-period execution lag in the base case: 1 day, 1 hour or 5 minutes by frequency (p. 172647, Table 1)
	- Rerun with no lag; pairs trading on 26 crypto coins (Table 3)
- **Grobys 2021**: skip the most recent day when computing the weekly MAX signal (p. 9)
- **Fieberg 2025**: 1-day lag between signal and portfolio, among 55,296 design variants (p. 3136)

### Why
- **Menkhoff 2016**: macro variables are published with a lag and real-time vintages do not exist for the sample (p. 23, fn. 18).
- **Fil 2020**: the lag approximates the bid-ask spread of contrarian trades, which may buy at the bid and sell at the ask (p. 172647)
- **Grobys 2021**: microstructure, bid-ask and price pressure, following Jegadeesh and Titman (p. 9)
- **Fieberg 2025**: immediate implementation is not always feasible (p. 3136)

### Evidence
- **Menkhoff 2016**: real data, 1976-2013, gross.
	- Standard value: Sharpe 0.53-0.60 without lag, 0.30-0.35 with it, t 1.83-2.04 (Tables 5, A.V).
	- Residual value: Sharpe 0.79-0.91 without lag, 0.39-0.61 with it, t 2.41-3.53 (Tables 5, A.V).
	- The order of the signals is unchanged (p. 23).
- **Fil 2020**: real data, 2018-2019, net of 30 bps per trade
	- Daily distance: -0.07% a month with lag, 0.38% without (Tables 2, 3)
	- 5-minute distance: 11.61% with lag, 16.80% without (Tables 2, 3)
	- Hourly cointegration: 1.11% with lag, 4.17% without (Tables 2, 3)
- **Grobys 2021**: real data, in-sample, gross
	- High minus low MAX -1.54% a week without skip, -1.82% with skip (Tables 1, 3)
- **Fieberg 2025**: real data
	- Median CTREND Sharpe 1.46 without lag, 1.24 with lag (Table 6)

### Limits
- **Menkhoff 2016**
	- A fixed lag only approximates real-time data; revised data are still used (fn. 18).
- **Fil 2020**
	- Lag is also read as a liquidity proxy; no actual spread measured (p. 172648)
- **Grobys 2021**: the skip shortens the signal window; execution timing unchanged (p. 9)
- **Fieberg 2025**: reported only as medians across variants (Table 6)

## Sources

- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
- [[2020 - Fil Kristoufek - Pairs Trading in Cryptocurrency Markets]] (Fil 2020)
- [[2021 - Grobys Junttila - Speculation and lottery-like demand in cryptocurrency markets]] (Grobys 2021)
- [[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns]] (Fieberg 2025)
