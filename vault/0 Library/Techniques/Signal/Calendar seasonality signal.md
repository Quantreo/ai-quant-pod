---
type: technique
brick: signal
aliases: [Month-of-year effect, Dummy-variable regression seasonality, DVR, Singular spectrum analysis, SSA, Robust SSA, RLSSA, Seasonal forecast, Same-weekday seasonality, SEAS, Cross-sectional seasonality, Sell in May and go away, Halloween indicator, Nov-Apr rule]
sources: 3
tested_on: [commodities, crypto, equities]
---

# Calendar seasonality signal

> [!summary]
> Estimates on a rolling window how each calendar month tends to behave, and uses it to forecast the next month's return of each contract.

## How it works

- **Inputs**: monthly log returns of each contract over a rolling window of past years.
- **Formula**: either a regression of returns on a dummy for the target calendar month, or a decomposition of the return series into components (singular spectrum analysis) with a one-step-ahead forecast. Contracts are ranked on the score.
- **Lookback / holding**: window of 120 months, re-estimated each month; hold one month.
- **Output**: a score per contract and month; long the highest, short the lowest.
- **Direction**: long and short, relative across contracts.
- **Tested on**: commodity futures.
- **Variant**: regression with a significance filter (cash if none); same-weekday mean over 20 weeks (crypto); SSA with a fixed rank; SSA with a robust L1 decomposition; fixed half-year switch of an equity index (long Nov-Apr, risk-free May-Oct).

## What the sources say

### Parameters
- **Kosch 2026**
	- Regression: return = α + β · dummy of month m; long needs β > 0 and Newey-West p ≤ 0.10, short β < 0 and p ≤ 0.10; cash if none (p. 7)
	- SSA: N = 120, L = 36, first r = 12 components, recurrent forecast; robust SSA uses an alternating L1 SVD (p. 7-8)
	- Top-1 contract, unit notional, monthly; 15 futures, 2016-2024; 8.6 bps one way (p. 9-10, 12)
- **Dolvin 2024**
	- Long the S&P 500 in Nov-Apr, risk-free asset in May-Oct; monthly returns, 1993-2023 (p. 54)
	- Subperiods 1993-2007 and 2009-2023, 2008 left out (p. 53)
- **Long 2020**
	- SEAS = mean of log returns at t-7, t-14, ..., t-140 (Eq. 1, p. 3)
	- Daily quintiles, equal and value weight; 151 coins chosen by size on 16 Dec 2019; Aug 2016 to Dec 2019 (p. 2-3)

### Why
- **Dolvin 2024**: Not stated by the authors. Seasonal affective disorder and vacation timing are cited and said to lack support (p. 51)
- **Kosch 2026**
	- Regression is transparent; SSA allows overlapping cycles; robust SSA limits outliers (p. 2)
	- L = 36 spans three annual cycles; r = 12 fixed (p. 7)
- **Long 2020**: recurring demand by weekday pushes prices away from fundamentals, following Keloharju et al. (p. 2)

### Evidence
- **Kosch 2026**: real data, out of sample 2016-2024, net of cost
	- Historical DVR long: 29.66%, Sharpe 0.245; equal-weight long 14.30%, 0.183 (Table 2)
	- Bootstrap averages, long: SSA 12.96% (median -11.30%), DVR 1.01%; benchmark 16.81% (Table 3)
	- No Holm-adjusted rejection in 18 Sharpe tests (Tables 4, 6)
- **Long 2020**: real data, in-sample, gross, crypto
	- High minus low 0.31% a day equal weight, 0.43% value weight, t about 2.05 (Table 2)
	- Remains significant with momentum, size, beta and liquidity controls (Table 3)
- **Dolvin 2024**: real data, in-sample, gross, no costs, equities
	- Fama-French 5-factor alpha 0.31% a month, market beta 0.50 (Table 3, p. 56)
	- Sharpe 0.26 against 0.21 for the S&P 500, 1993-2023 (Table 2, p. 56)
	- Alpha 0.32 in 1993-2007 (p = .091) and 0.25 in 2009-2023 (p = .26) (Table 3, p. 56)

### Limits
- **Kosch 2026**
	- DVR short loses 36.63% on average over the bootstrap paths (Table 5)
	- Top-1 forces a position even when the forecast is small or of the wrong sign (p. 9-10)
- **Dolvin 2024**
	- Post-2008 mean 0.90 against 1.19 for the S&P 500, Sharpe 0.22 against 0.27 (Table 2, p. 56)
	- No transaction costs; no held-out period (whole paper)
- **Long 2020**
	- Coin list chosen on the last day of the sample (p. 2)
	- Robustness tables only in an online appendix (p. 6)
	- No costs on a daily rebalance (whole paper)

## Sources

- [[2026 - Kosch Forsberg - Seasonal Trading in Commodity Futures Evidence from Regression and Singular Spectrum]] (Kosch 2026)
- [[2024 - Dolvin Foltice - Update on Sector Rotation in the Sell in May and Go Away Strategy]] (Dolvin 2024)
- [[2020 - Long Zaremba Demir et al - Seasonality in the Cross-Section of Cryptocurrency Returns]] (Long 2020)
