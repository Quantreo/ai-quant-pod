---
type: technique
brick: signal
aliases: [Factor momentum, Time-series factor momentum, TSFM, Cross-sectional factor momentum, CSFM, Anomaly momentum, 1mMOM, 12mMOM]
sources: 1
tested_on: [equities]
---

# Factor momentum signal

> [!summary]
> Forecasts the next return of a long-short factor with its own recent return, and goes long the factors that did well and short those that did badly.

## How it works

- **Inputs**: monthly returns of a set of long-short factor portfolios.
- **Formula**: the forecast of a factor is its past return over a lookback, or its average monthly return over that lookback. Positive forecast: long the factor; negative: short it.
- **Lookback / holding**: one month or twelve months; monthly forecasts.
- **Output**: a forecast per factor, turned into weights by a long-short rule.
- **Direction**: long and short factors, whatever the factor's own sign.
- **Tested on**: US stock anomaly portfolios.
- **Variant**: apply the rule to the main principal components of the factors, then map the forecasts back to each factor.

## What the sources say

### Parameters
- **Kagkadis 2023**
	- 1mMOM: the return at t is the forecast for t + 1. 12mMOM: the average monthly return of the previous 12 months (p. 18)
	- Applied to each of 72 anomalies, decile 10 minus decile 1, 1990-2019 out of sample (p. 18, 20, 23)
	- Variant on the 5 PC portfolios, mapped back to the anomalies (p. 18, 41)
	- Weights: top and bottom 10%, or forecast over volatility capped at ±2 (see Long-short portfolio weighting) (p. 32-34)

### Why
- **Kagkadis 2023**
	- Used as a benchmark, not argued by the authors (p. 18)
	- Literature cited: strongest at the 1-month horizon, concentrated in the largest PCs (p. 7-8)

### Evidence
- **Kagkadis 2023**: real data, out of sample, gross, 1990-2019
	- Long-short of 10% extremes, monthly: 1mMOM 1.06% (t 2.28), 12mMOM 0.84% (t 1.84) (Table 4)
	- Total out-of-sample R²: 1mMOM -88.98%, 12mMOM -6.61% (Table 1)
	- Average cross-sectional correlation: 1mMOM 5.98%, 12mMOM 5.43%; the best characteristic models 7.74% to 9.04% (Table 3)
	- 1mMOM leads until the late 1990s, then flat; flat in 2010-2019 (≈ Figure 5, p. 37)

### Limits
- **Kagkadis 2023**
	- 1mMOM beats the historical mean error in only 20% of months (fn 20, p. 30)
	- Profitability erodes in later years (p. 39)
	- No transaction costs or turnover; lookbacks not tuned, only two tested (whole paper)

## Sources

- [[2023 - Kagkadis Nolte Nolte et al - Factor Timing with Portfolio Characteristics]] (Kagkadis 2023)
