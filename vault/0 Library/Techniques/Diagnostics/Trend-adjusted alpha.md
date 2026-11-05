---
type: diagnostic
kind: attribution
aliases: [trend control regression, trend twin regression, alpha net of trend exposure, trend exposure of a timing strategy]
sources: 1
---

# Trend-adjusted alpha

> [!summary]
> Is the alpha of a timing or sizing strategy over buy-and-hold really exposure to a trend strategy on the same asset?

## How it works

- **How**: regress the strategy's return on the buy-and-hold return of the same asset, then again with the return of a trend strategy on that asset added. The intercept is the alpha. Compare the two intercepts and read the trend coefficient.
- **Reading**: the share of the first alpha that disappears is the share attributed to trend; the trend coefficient is the amount of trend the strategy holds, per unit of notional. The alpha that remains is the part trend does not explain.
- **Variant**: repeat with other trend rules (single lookbacks, a weighted mix) and compare the share removed.
- **Variant**: pool several assets in a panel with standard errors clustered by date.
- **Data needed**: daily returns of the strategy, of buy-and-hold, and of the trend strategy, on the same dates.

## What the sources say

### Parameters
- **Hood 2024**
	- Trend twin: average of the sign of the 1-, 3-, 12-month returns, 1-day lag (p. 6).
	- OLS with Newey-West standard errors, 10 lags; panels with errors clustered by date (fn 10, p. 15).
	- Alpha annualised; sample 1927-2023 for the US market factor, 2000-2023 for 50 futures (p. 4, 12).
	- Alternatives: single 1, 3, 6, 9, 12-month trend signs and a CTA-style mix (Appendix C).

### Why
- **Hood 2024**: a timing strategy is more likely to load on another timing strategy than on a cross-sectional factor, so trend is the natural control (p. 4).

### Evidence
- **Hood 2024**: real data, in-sample, net of 2 bp, volatility targeting on the US market factor
	- Alpha 3.07% (t 2.9) falls to 1.25% (t 1.3) with trend; trend coefficient 0.30 (t 12.0); R² 0.75 to 0.79 (Exhibit 4).
	- Other trend rules remove 21% (1-month) to 60% (CTA-style mix) of the alpha (Exhibit C.1).
	- Equity panel 2000-2023: 1.57% falls to 0.65%; bonds, currencies, commodities barely move (Exhibit 8).
	- Same test on SMB and HML: alpha unchanged, trend coefficient 0.00 (Exhibit B.2).

### Limits
- **Hood 2024**
	- A lower alpha is not a zero alpha: part of the outperformance stays (p. 9).
	- Broad-sample alphas are not significant before the control, so the reduction has little to explain (p. 16, Exhibit 6).
	- The result depends on the trend rule: 6, 9, 12-month signs remove 39% to 49% on the long sample, over 90% on the equity panel (Exhibit C.1, C.2).
	- Rebalancing frequency of the regressed returns not stated (Exhibit 1B notes).

## Sources

- [[2024 - Hood Raughtigan - Volatility Targeting Is Trendy How Trend Following Explains Alpha in Volatility-Managed Strategies]] (Hood 2024)
