---
type: technique
brick: signal
aliases: [Volatility-scaled forecast, Standardised returns for ranking, EWMA standardisation]
sources: 1
tested_on: [commodities]
---

# Volatility-normalised signal

> [!summary]
> Divides returns by their own volatility before estimating a signal, so contracts can be ranked in volatility units.

## How it works

- **Inputs**: returns of each contract and an estimate of its conditional volatility.
- **Formula**: subtract an expanding mean from each return and divide by an EWMA volatility estimated only with past data in the window. Estimate the signal on these standardised returns.
- **Lookback / holding**: volatility estimated inside the same rolling window as the signal.
- **Output**: a score read as expected return in volatility units.
- **Direction**: as the underlying signal.
- **Tested on**: commodity futures.
- **Why it matters**: raw forecasts scale one for one with the size of returns, so a ranking on raw scores can favour the most volatile contracts.

## What the sources say

### Parameters
- **Kosch 2026**
	- EWMA variance with λ = 0.97 for monthly data, warm start from the first 12 observations of the window (p. 8-9)
	- Expanding mean from the first observation of the window (p. 8)
	- Applied to regression, SSA and robust SSA in a 120-month window (p. 8-9)

### Why
- **Kosch 2026**
	- Doubling the return series doubles the regression coefficient and the SSA forecasts, with no change in the seasonal pattern (Table 1, p. 8)
	- Aim: cross-contract comparability and less mechanical preference for volatile contracts (p. 9)

### Evidence
- **Kosch 2026**: real data, out of sample 2016-2024, net of cost
	- Historical cumulative return falls for SSA long (-32.41% to -57.76%), SSA short, RLSSA long and RLSSA short (Table 2)
	- DVR short improves, from -19.94% to -9.72% (Table 2)
	- Bootstrap average DVR short loss falls from 36.63% to 19.01% (Table 5)

### Limits
- **Kosch 2026**
	- Generally weakens the SSA-based portfolios (p. 18)
	- Amplitude may carry economic information that the scaling removes (p. 18-19)
	- No Holm-adjusted rejection against the classical version (Tables 4, 6)

## Sources

- [[2026 - Kosch Forsberg - Seasonal Trading in Commodity Futures Evidence from Regression and Singular Spectrum]] (Kosch 2026)
