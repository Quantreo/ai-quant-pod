---
type: technique
brick: signal
aliases: [absolute value risk premium, relative value risk premium, value risk premia, cheap against own history, standardised value measure, own-history value z-score]
sources: 1
tested_on: [multi-asset]
---

# Value z-score signal

> [!summary]
> Scores each asset by how cheap its own value measure is against its own history (absolute) or against the other assets (relative), and holds the cheap ones.

## How it works

- **Inputs**: one value measure per asset, in a form where high means cheap (yield, earnings yield, real exchange rate deviation, roll yield).
- **Formula**: z = (current value minus historical mean) / historical standard deviation, with an expanding or rolling window. Absolute: z against the asset's own history. Relative: z compared across assets, rank on it.
- **Lookback / holding**: a minimum history before the first signal; hold one rebalance period.
- **Output**: absolute, a hold or no-hold flag per asset, with a band on z; relative, a top-k selection.
- **Direction**: long-only, with cash when nothing qualifies.
- **Tested on**: a few liquid indices of different asset classes.
- **Variant**: absolute with a band, holding only assets with 0 < z < 1.5 (an upper cap on cheapness).
- **Variant**: relative, holding the 3 of 8 assets with the highest cross-sectional z.

## What the sources say

### Parameters
- **Zhakanova 2019**
	- Value measure per asset: earnings yield (1 / 12-month forward P/E) for MSCI World and MSCI EM; dividend yield for REITs; yield to maturity for US Treasuries; real effective exchange rate against OECD fair value for JPY/USD and EUR/USD; roll yield for the S&P GSCI; the US Treasury yield for gold (p. 1410-1411)
	- Expanding window, minimum 24 months, z up to month t-1 (p. 1411-1412)
	- Absolute: equal weight 1/N among assets with 0.0 < z < 1.5, money market if none (Eq. 9, p. 1412)
	- Relative: three highest cross-sectional z, 1/3 each (Eq. 11, p. 1412)
	- Monthly rebalancing, 8 assets, Jan 1995 to Dec 2015 (p. 1411, 1409)

### Why
- **Zhakanova 2019**
	- Picks assets that are undervalued against their own history or within the universe (p. 1407)
	- The upper bound of 1.5 is not argued (p. 1412)

### Evidence
- **Zhakanova 2019**: real data, in-sample, costs not stated
	- Annual return: relative 8.38%, absolute 7.54%, 60/40 6.24%, equal weight 3.65% (Table 2)
	- Sharpe: 0.63 and 0.65 against 0.70 for 60/40 and 0.38 for equal weight (Table 2)
	- Max drawdown 39.68% (relative) and 32.15% (absolute) against 34.17% for 60/40 (Table 2)

### Limits
- **Zhakanova 2019**
	- Negative alpha for at least seven years; poor years after the 2008 crisis (p. 1420)
	- No costs, no test of the difference with the benchmarks, no parameter variant (whole paper)
	- Text and tables disagree in several places (see the reading note)

## Sources

- [[2019 - Zhakanova Isiksal Backhaus Jung - Value investing across asset classes]] (Zhakanova 2019)
