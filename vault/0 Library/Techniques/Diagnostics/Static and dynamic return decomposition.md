---
type: diagnostic
kind: attribution
aliases: [passive and dynamic components, timing vs average positioning, de-meaned signal sort, conditional vs unconditional carry, rolling-mean de-meaned sort]
sources: 3
---

# Static and dynamic return decomposition

> [!summary]
> Does the strategy earn its return from always holding the same assets (static), or from timing them as the signal moves (dynamic)?

## How it works

- **How**: for each asset, split the average of weight times next return into average weight times average return (static part) plus the time-series covariance of weight and return (dynamic part). Sum over assets, weighted by sample share. Variant: re-run the sort on the signal minus its own mean per asset; what survives de-meaning is the time-series part.
- **Reading**: a large dynamic share means the signal times assets. A large static share means the strategy mostly holds assets that do well on average, a passive tilt.
- **Data needed**: the strategy's weights per asset and date, and next-period asset returns.
- **Mean used for de-meaning**: full-sample mean, or a trailing rolling mean that is known at each date.

## What the sources say

### Parameters
- **Koijen 2013**
	- Static term: average weight of asset n times its average return, over the dates n is used, weighted by T_n / T (Eq. 27, p. 26).
	- Dynamic term: time-series covariance of the weight with the next return, same weighting (Eq. 27, p. 26).
	- Weights from the rank-based carry rule, monthly (Eq. 23, p. 18).
- **Gorton 2007**
	- Basis minus its full-sample mean, per commodity, then the same high/low half sort (p. 20).
- **Lustig 2013**
	- Same three-portfolio sort on short rates in levels and minus their past 10-year rolling mean; same for yield curve slopes (p. 14-15; Fig. 1).

### Why
- **Koijen 2013**: separates the passive return from always being long (short) assets with high (low) unconditional returns from how strongly variation in the signal predicts returns (p. 26).
- **Gorton 2007**: the basis can reflect time variation in inventories or fixed cross-sectional differences in storability; de-meaning tells the two apart (p. 20).
- **Lustig 2013**: a level sort captures the conditional premium (currently high rates) and the unconditional one (high average rates); the de-meaned sort only the conditional part (p. 14-15).

### Evidence
- **Koijen 2013**: real data, in-sample, gross of costs.
	- Dynamic share: equities 101%, bond level 86%, bond slope 99%, options 100% and 111% (Table V).
	- Dynamic share: Treasuries 42%, commodities 64%, currencies 58%, credit 30% (Table V).
	- Equity carry: dynamic share 53% of drawdown losses vs 93.5% of expansion gains, static part kept at full sample (Table XI, p. 32).
- **Gorton 2007**: real data, in-sample, gross of costs.
	- De-meaned basis sort: high minus low 10.13% a year (t = 3.52), not significantly different from the raw basis sort; results unreported in tables (p. 20).
- **Lustig 2013**: real data, in-sample, gross, G10 1975-2015.
	- Currency excess returns are larger with level sorts; the offset from local bond premia is slightly weaker (p. 14).
	- Cumulative log FX premium ≈1.4 (rate levels) vs ≈1.1 (rate deviations) (≈ Fig. 1).
	- Rate deviation sort, currency leg: 2.66% a year, Sharpe 0.36 (Table 3B).

### Limits
- **Koijen 2013**
	- The paper states dynamic share "about half" for credit (p. 3) where Table V gives 30%.
- **Gorton 2007**
	- The de-meaned result is not shown in a table (p. 20).
- **Lustig 2013**
	- Level sort results for the 10-year sample appear only as a chart (Fig. 1).
	- Rolling 10-year window not argued (p. 10).

## Sources

- [[2013 - Koijen Moskowitz Pedersen et al - Carry]] (Koijen 2013)
- [[2007 - Gorton Hayashi Rouwenhorst - The Fundamentals of Commodity Futures Returns]] (Gorton 2007)
- [[2013 - Lustig Stathopoulos Verdelhan - The Term Structure of Currency Carry Trade Risk Premia]] (Lustig 2013)
