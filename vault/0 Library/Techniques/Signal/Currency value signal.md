---
type: technique
brick: signal
aliases: [currency value, PPP value, real exchange rate value, 5-year real exchange rate change, fundamental-adjusted value, residual value signal, Bilson value signal, real exchange rate over 5-year smoothed lag, minus 5-year currency return, deviation from uncovered interest parity, real effective exchange rate against OECD fair value]
sources: 4
tested_on: [fx]
---

# Currency value signal

> [!summary]
> Goes long the currencies that have become cheap in real terms and short those that have become dear, optionally after removing the part of the cheapness that macro fundamentals explain.

## How it works

- **Inputs**: spot exchange rates and consumer price indexes against a base currency; optionally country fundamentals.
- **Formula**: log real exchange rate q = home price level minus foreign price level minus spot, so a higher q means a cheaper foreign currency. Signal = change of q over a long window. Variant: regress the signal on fundamentals across currencies each period and keep the residual. Variant: real exchange rate from absolute PPP price levels instead of a base-year index.
- **Lookback / holding**: multi-year lookback; hold one rebalance period.
- **Output**: a cross-sectional signal or rank, turned into long-short weights.
- **Direction**: long-short.
- **Tested on**: developed and emerging currencies against USD.
- **Variant**: real exchange rate level divided by its average around five years ago, then demeaned across currencies.
- **Variant**: minus the past 5-year return of the exchange rate, interest earned included; no price index needed.
- **Variant**: trade-weighted real effective exchange rate against an OECD fair value, turned into a z-score against its own history.

## What the sources say

### Parameters
- **Menkhoff 2016**
	- q(t) - q(t-5y), CPI-based, base 1970Q1 (p. 11, 43).
	- Residual: per-quarter regression on GDP per capita, export quality, NFA / GDP, output gap, raw or expected (EWMA φ = 0.98, VAR, panel VAR) (p. 15-16).
	- 22 currencies vs USD, quarterly (p. 13, 43).
- **Chernov 2020**
	- Q = S P*/P; signal = Q(t) over its average from t-66 to t-54 months, minus the cross-sectional mean (Eq. 5-6, p. 11-12).
	- CPI lagged 3 months; AUD and NZD quarterly CPI forward filled (p. 17).
	- Rank weights, monthly, nine G10 currencies vs USD, 1985-2020 (p. 16-17).
- **Asness 2013**
	- Signal = minus the 5-year return on the exchange rate, with interest earned at the local 3-month LIBOR (p. 9)
	- Rank-weighted factor, and top third minus bottom third, monthly (p. 10; see [[Long-short portfolio weighting]])
	- 10 currencies vs USD, 1979-2011 (p. 6)
- **Zhakanova 2019**
	- Value measure: real effective exchange rate against OECD fair value, trade-weighted sum of bilateral real rates in logs (Eq. 2-3, p. 1410)
	- Used as a z-score on JPY/USD and EUR/USD only, inside a multi-asset long-only portfolio (p. 1409-1411; see [[Value z-score signal]])

### Why
- **Menkhoff 2016**
	- 5 years: comparable with prior work, no base-year effect (fn. 8, p. 11).
	- Residual: removes expected real rate differentials and the long-run level, leaving the risk premium (p. 6-8).
- **Chernov 2020**
	- The long-run mean of the real exchange rate is ill-defined; a 5-year smoothed lag keeps the long-run nature of mean reversion (p. 11).
	- Demeaning removes time and currency fixed effects (p. 12).
	- CPI lag: every input observable at t (p. 17).
- **Asness 2013**
	- Simple, uniform with the other asset classes; equals the 5-year deviation from uncovered interest parity, or a 5-year change in PPP if real rates are constant across countries (p. 9)
	- Past 5-year return sorts correlate 0.83 with book-to-market sorts in US stocks (p. 9, Table A1)

- **Zhakanova 2019**: prices converge to purchasing power parity, so the deviation from it is a possible value measure (p. 1409)

### Evidence
- **Menkhoff 2016**: real data, 1976-2014, revised macro data, gross.
	- Standard: Sharpe 0.44 to 0.51 (Table 4).
	- Residual: Sharpe 0.79 to 0.91, lower volatility, similar mean (Table 5).
	- Residual alpha 4.62% a year (t 4.97) over carry and momentum (Table 6A).
	- Two-quarter lag: residual 0.39 to 0.61, standard 0.30 to 0.35 (Table A.V).
- **Chernov 2020**: real data, in-sample, gross, G10 1985-2020
	- CS-Value Sharpe 0.529, mean 4.02 (t 3.15) (Table 2B).
	- Adding value to carry in a mean-variance portfolio: Sharpe 0.871 to 0.998 (Table 1D).
	- Hedged of its unpriced part: Sharpe ≈0.92 (≈ Fig. 1).
- **Asness 2013**: real data, in-sample, gross, 1979-2011
	- Spread mean 3.3% (t = 1.89), Sharpe 0.34; factor 3.9% (t = 2.47), 0.44 (Table I Panel B)
	- Low, middle, high thirds earn -0.5%, 0.3%, 2.8% (Table I Panel B)
	- Correlation with currency momentum -0.42 (spread) and -0.43 (factor) (Table I Panel B)

- **Zhakanova 2019**: no result for the currency measure alone; only the portfolio results are given (Table 2)

### Limits
- **Menkhoff 2016**
	- No costs; T-bill differentials, not forwards (p. 46).
	- No real-time macro data (fn. 18, p. 23).
	- Standard, rank weights: drawdown ≈-25% in 1990-91 (≈ Fig. 3).
	- No theory says who pays the premium (p. 24).
	- Absolute-PPP table repeats Table 4 exactly (Table A.II).
- **Chernov 2020**
	- Optimal timing alpha -0.53 (t -0.62); volatility timing -0.76 (t -1.93) (Table 4).
	- No transaction costs (whole paper).
- **Asness 2013**
	- No costs (p. 29)
	- Spread t-stat 1.89 is below 2 (Table I Panel B)
	- Past return, not a price level: no inflation data used (p. 9)
- **Zhakanova 2019**
	- Only two currencies, no currency-only result (p. 1409)
	- No costs stated (whole paper)

## Sources

- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
- [[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks]] (Chernov 2020)
- [[2013 - Asness Moskowitz Pedersen - Value and Momentum Everywhere]] (Asness 2013)
- [[2019 - Zhakanova Isiksal Backhaus Jung - Value investing across asset classes]] (Zhakanova 2019)
