---
type: technique
brick: signal
aliases: [business cycle signal, relative output gap sort, GAP strategy, output gap differential, Hamilton filter output gap, macro cycle currency sort]
sources: 1
tested_on: [fx]
---

# Output gap signal

> [!summary]
> Goes long the currencies of economies running above their trend in activity relative to the base country, and short those running below.

## How it works

- **Inputs**: an activity series per country (industrial production), the same for the base country, and a way to estimate trend output.
- **Formula**: output gap = log activity minus its estimated trend. Signal = country gap minus base-country gap. The estimator of trend (filter, quadratic trend, regression on lagged activity) is a parameter. Real-time use needs the data as published at each date.
- **Lookback / holding**: monthly signal, one month hold.
- **Output**: a cross-sectional signal, turned into quintile, linear or rank weights; or a time-series sign against the base country.
- **Direction**: long-short.
- **Tested on**: developed and emerging currencies against USD.

## What the sources say

### Parameters
- **Colacito 2019**
	- Gap = log industrial production minus trend, minus the US gap (p. 9-10).
	- Full sample: Hodrick-Prescott (λ = 14400), Baxter-King (K = 36), linear projection, quadratic trend (IA p. 1-2).
	- Real time: regress y(t) on 12 lags from t-24 months, gap = residual, on OECD vintages (Eq. 3, p. 10).
	- Cross-section: five equal-weight quintiles, long P5, short P1; or linear or rank weights (p. 10-11).
	- Time series: long (short) each currency whose gap is above (below) the US gap, 1/N (p. 11-12).
	- Month-end sort, 27 currencies against USD (p. 7-11).

### Why
- **Colacito 2019**
	- Business cycle position is a state variable that carries a currency risk premium, the "GAP premium" (p. 3-4, 29).
	- Linear projection replaces filters that use revised or forward-looking data (p. 9-10).
	- Linear and rank weights trade all currencies, less reliant on extremes (p. 11).

### Evidence
- **Colacito 2019**: real data, real time, 1999-2016.
	- Cross-section Sharpe 0.72 gross, 0.50 net of 50% of quoted spreads; time series 0.65 and 0.50 (Table 4).
	- About 86% of the cross-section return is spot change (computed, Table 4A).
	- Correlation with carry 0.06; adding it lifts carry Sharpe 0.58 to 0.85 (Tables 5, 6).
	- Full sample 1983-2016, in-sample, gross: spread 4.56% to 6.66% across four gap measures (Table 1).

### Limits
- **Colacito 2019**
	- Cross-section cumulative return flat after about 2010 (≈ Fig. 2).
	- Time series loses 3.99% in US recessions, with a dollar exposure that flips sign (Table A6).
	- Time-series Sharpe for a Swiss investor is 0.14 (Table A8).
	- Costs use half the quoted spread; real-time sample is 17 years (p. 17, Table 4).

## Sources

- [[2019 - Colacito Riddiough Sarno - Business Cycles and Currency Returns]] (Colacito 2019)
