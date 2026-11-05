---
type: diagnostic
kind: attribution
aliases: [leverage effect check, momentum-ness of volatility scaling, correlation of reciprocal volatility with past returns]
sources: 2
---

# Volatility scaling momentum check

> [!summary]
> Does scaling an asset by its volatility add a momentum bet (smaller after losses) or a mean reversion bet (smaller after gains)?

## How it works

- **How**: on monthly data, correlate the asset's return with the change in its variance (leverage effect). Also correlate the reciprocal of the volatility estimate, which is proportional to the scaled position, with the past 1, 3, 6 and 12-month returns.
- **Reading**: a negative return and variance-change correlation, or a positive correlation of reciprocal volatility with past returns, means scaling cuts exposure after losses, a momentum bet. A negative correlation means a mean reversion bet.
- **Data needed**: daily returns of the asset, a volatility estimate, and the Sharpe ratio of the scaled and unscaled versions if the reading is to be compared with the gain.

## What the sources say

### Parameters
- **Harvey 2018**
	- Monthly return against change in variance, and against variance level, variance from intra-month daily data (Fig. 13, p. 20).
	- Reciprocal of an EWMA volatility with 20-day half-life against past 21, 65, 130, 260-day returns (Fig. 14, p. 20-21).
	- Cross-section of Sharpe gains regressed on the 21-day correlation, half-lives 20 and 90 days (Fig. 15, p. 21).
- **Hood 2024**
	- Leverage effect: correlation of the 1-month return with the 1-month change in the volatility estimate, full period (p. 10).
	- Average trailing 1-, 3-, 12-month return by bucket of the volatility-targeting position, buckets (0, 0.5] to above 2.0 (Exhibit 5, p. 11).
	- Leverage effect against trend beta, asset by asset, 50 futures 2000-2023 (Exhibit 7, p. 14).

### Why
- **Harvey 2018**: the leverage effect makes volatility scaling a momentum bet, and time-series momentum has done well historically (p. 19-21).
- **Hood 2024**: a negative leverage effect gives a positive link between volatility-targeted positions and trend positions (p. 10-12).

### Evidence
- **Harvey 2018**: real data, in-sample, 1988-2017 for futures and credit, equities from 1926
	- Leverage effect appears for equities (full sample, subsamples, 10 industries) and credit, not for other assets (Fig. 13, p. 20).
	- Reciprocal volatility correlates positively with past returns only for risk assets; the correlation is mostly negative for other assets (Fig. 14, p. 20).
	- The 21-day correlation explains 45% (20-day half-life) and 60% (90-day) of the cross-section of Sharpe gains (Fig. 15, p. 21).
- **Hood 2024**: real data, in-sample, net of 2 bp
	- US market factor 1927-2023: leverage effect -0.31; average trailing return ≈-5% where the position is below 0.75, ≈+4% to +6% above 1.0 (Exhibit 4, 5).
	- Panels 2000-2023: equities -0.31, bonds -0.03, currencies -0.16, commodities -0.07; trend beta 0.35 for equities, 0.04 to 0.08 for the others (Exhibit 8).
	- S&P 500 future -0.33 and 10-year bond future 0.02; only the S&P 500 loads on trend (Exhibit D.1).

### Limits
- **Harvey 2018**
	- Results read from charts; no regression table or standard errors (Fig. 13-15).
	- The authors cite two opposite causal stories for the leverage effect and do not choose (fn 23, p. 19).
- **Hood 2024**
	- The authors give no proof of the link; the exact relation is called highly non-linear (p. 10).
	- Currency leverage effect is negative (-0.16) with no trend loading and negative alpha, left unexplained (fn 19, Exhibit 8).

## Sources

- [[2018 - Harvey Hoyle Korgaonkar et al - The Impact of Volatility Targeting]] (Harvey 2018)
- [[2024 - Hood Raughtigan - Volatility Targeting Is Trendy How Trend Following Explains Alpha in Volatility-Managed Strategies]] (Hood 2024)
