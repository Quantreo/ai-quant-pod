---
type: technique
brick: signal
aliases: [Cyclical and defensive rotation, Sell in May sector rotation, Optimism cycle rotation, Seasonal sector rotation ETF]
sources: 1
tested_on: [equities]
---

# Seasonal sector rotation

> [!summary]
> Holds cyclical sectors in the strong half of the year and defensive sectors in the weak half, optionally shorting the other group.

## How it works

- **Inputs**: a split of the equity sectors into cyclical and defensive groups, and a calendar rule for the two seasons.
- **Formula**: in the strong season hold the cyclical group, in the weak season the defensive group, equal weight within the group. Long-short variant: also short the opposite group.
- **Lookback / holding**: no lookback; switch once at each season boundary.
- **Output**: a set of sectors to hold each month.
- **Direction**: long-only, or long-short between the two groups.
- **Tested on**: US equity sectors.
- **Variant**: the group lists differ by source (technology counted as cyclical or defensive, energy and utilities in or out); an earlier re-entry month.

## What the sources say

### Parameters
- **Dolvin 2024**
	- Strong season Nov-Apr, weak season May-Oct (p. 56)
	- Doeswijk lists: cyclical Energy, Discretionary, Industrials, Materials; defensive Staples, Utilities, Healthcare (Table 1, p. 52)
	- Pacer list: cyclical adds Technology and drops Energy; defensive Staples, Healthcare only (Table 1, p. 52)
	- Peloton list: Doeswijk's cyclicals; defensive adds Technology (Table 1, p. 52)
	- Communications, Financials and Real Estate excluded; equal weight within each group; US sectors, 1993-2023 (p. 52, 56)
	- Long-short: long cyclicals and short defensives in Nov-Apr, the reverse in May-Oct; leg sizes not stated (p. 58)

### Why
- **Dolvin 2024**: cyclical sectors outperform in strong market periods and defensive sectors in weak ones, following Doeswijk (2008) (p. 51, 56)

### Evidence
- **Dolvin 2024**: real data, in-sample, gross, no costs, equities
	- Long-only alpha 0.24 to 0.32 a month, beta 0.86 to 0.94; the base rule (index Nov-Apr, risk-free May-Oct) has 0.31 (Tables 3, 5, p. 56-57)
	- Long-short alpha 0.37 to 0.50 a month with beta about 0; significant over 1993-2023 for the three lists (Table 7, p. 59)
	- Long-only premium over the S&P 500 0.26 to 0.32, 1993-2023 (Table 4, p. 57)

### Limits
- **Dolvin 2024**
	- Long-only rotation adds no alpha over the base rule and carries a higher beta (p. 58)
	- 2009-2023 premium 0.07 to 0.17, none significant; long-short alphas not significant in either subperiod (Tables 4, 7, p. 57, 59)
	- Long-short average return is below the S&P 500 (premium -0.35 to -0.39) (Table 7, p. 59)
	- October re-entry lowers alpha for each list (Table 8, p. 60)
	- No transaction, borrow or short-sale costs (whole paper)

## Sources

- [[2024 - Dolvin Foltice - Update on Sector Rotation in the Sell in May and Go Away Strategy]] (Dolvin 2024)
