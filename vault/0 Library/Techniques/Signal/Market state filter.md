---
type: technique
brick: signal
aliases: [Panic state indicator, Bear market indicator, Momentum crash filter, Bear market times market variance, Loser portfolio breakpoint, Past 36-month market return]
sources: 2
tested_on: [equities, fx, commodities, rates, multi-asset]
---

# Market state filter

> [!summary]
> Flags "panic" states, after a market decline and when market volatility is high, in which momentum returns are forecast to be low.

## How it works

- **Inputs**: past cumulative return of the asset class market index and the recent variance of its daily returns.
- **Formula**: a bear indicator (past market return over a long window below zero), the market variance, and their product; the product can be normalised by its mean in bear months.
- **Lookback / holding**: a long window for the bear indicator, a shorter window for variance; read at each rebalance, ex ante.
- **Output**: a state flag or a continuous panic score, used to forecast the strategy's mean return or to scale it.
- **Direction**: high panic score, lower expected momentum return.
- **Tested on**: equities, index futures, currencies, commodities, government bonds.
- **Variant**: the return threshold to enter the loser portfolio, as a direct gauge of how far losers have fallen.

## What the sources say

### Parameters
- **Daniel 2016**
	- I_B = 1 if the cumulative market return over the past 24 months is negative (p. 15)
	- σ²_m: variance of daily market returns over the 126 days before the month (p. 20)
	- I_Bσ² = I_B·σ²_m divided by the full-sample mean of σ²_m in bear months (p. 22)
	- Market per class: local index; equal-weight average for currencies and bonds (p. 30)
- **Daniel 2012**
	- Cumulative market return over the past 36 months; realized volatility of daily market returns over 12 months; loser breakpoint, the 12-2 return at the 10th percentile (p. 10)
	- Groups: top and bottom 20%, middle 60% (p. 10)

### Why
- **Daniel 2016**: after bear markets losers carry high, option-like beta, so momentum is short a call and its premium is low (p. 15-16, 19)
- **Daniel 2012**: these variables proxy losers' leverage; window lengths are arbitrary (p. 9-10, 12-13)

### Evidence
- **Daniel 2016**: real data, in-sample regressions, gross
	- US 1927-2013: interaction I_B·σ²_m on WML returns -0.323 (t = -2.2) with both terms included (Table 5)
	- US 1990-2013: 31.48% a year outside panic states, 58.62% lower inside (t = -5.2) (Table 6)
	- International equities: panic coefficient -6.5% to -11.4% a year, significant in EU, JP, UK, US (Table 8 D)
	- Currencies -4.655 (t = -2.1); commodities and index futures negative but not significant; bonds about zero (Table 9 D)
- **Daniel 2012**: real data, in-sample, gross, US 1927-2013
	- Losses below -20%: 11 of 13 in the low 36-month market group, 13 of 13 in the high RV group, 12 of 13 in the low breakpoint group (Tables 3C, 14)
	- Before crashes: 36-month market -37.23% vs 38.37% on average; 12-month RV 36.39% vs 14.82% (Table 2)
	- False positives at -20%: market RV 12m 184, past 36-month market return 484, vs 114 for the HMM (Table 8)

### Limits
- **Daniel 2016**
	- The normaliser is a full-sample mean, known only ex post (p. 22)
	- Outside equities only FX and the all-asset composite are significant at 5% (p. 34)
- **Daniel 2012**
	- Group cut-offs are full-sample percentiles (p. 10)
	- Results for other windows claimed, not shown (fn 15)

## Sources

- [[2016 - Daniel Moskowitz - Momentum crashes]] (Daniel 2016)
- [[2012 - Daniel Jagannathan Kim - Tail Risk in Momentum Strategy Returns]] (Daniel 2012)
