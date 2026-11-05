---
type: technique
brick: signal
aliases: [Time-of-day signal, Intraday seasonal spline, Seasonality index]
sources: 1
tested_on: [equities]
---

# Intraday seasonality signal

> [!summary]
> Forecasts the next return from the time of day, using the average shape of returns across the trading day.

## How it works

- **Inputs**: intraday returns on a regular grid and the position of each bar inside the day.
- **Formula**: normalise returns, bucket them by position in the day, fit a smooth curve of return on the time-of-day index over a rolling window, and read the curve at the current time. The curve is forced to zero mean.
- **Lookback / holding**: curve refit each day on a rolling window of previous days; the position is reset every bar.
- **Output**: a signed forecast, positive at times of day with positive average return.
- **Direction**: long and short.
- **Tested on**: an equity index future.

## What the sources say

### Parameters
- **Christensen 2020**
	- 1-minute bars, 856 a day, 01:00 to 15:15 Chicago time; index X = [1, ..., 856] (p. 12, 17)
	- B-spline with 10 knots, integral set to zero (p. 11, 13)
	- Returns normalised by an EWMA mean and volatility; spline refit on the previous 66 trading days (p. 11)
	- E-mini S&P 500, 2011, signal lagged one period (p. 17)

### Why
- **Christensen 2020**
	- Intraday seasonality is a documented effect with a period known in advance (p. 12)
	- Splines are chosen because the cycle length is known, the shape is non-linear and the time domain is preferred (p. 12)

### Evidence
- **Christensen 2020**: real data, one year, pre-cost
	- Sharpe ≈1.85 against long-only ≈0.45 (≈ Fig. 6, p. 14)
	- Correlation with long-only ≈ -0.48 (≈ Fig. 6)
	- Spline positive early in the day, negative from about 07:00 (≈ Fig. 5)

### Limits
- **Christensen 2020**
	- The spline is an empirical shape; it needs a stronger belief in the economic story (p. 13)
	- Knot count chosen by intuition (p. 13)
	- One contract, one year, no cost model (p. 17-18)

## Sources

- [[2020 - Christensen - Hidden Markov Models Applied To Intraday Momentum Trading With Side Information]] (Christensen 2020)
