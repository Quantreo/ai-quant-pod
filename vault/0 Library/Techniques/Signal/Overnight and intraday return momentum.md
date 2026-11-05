---
type: technique
brick: signal
aliases: [Overnight vs intraday return sort, Tug of war sort, Day-night session rule, Session reversal, 12h session strategy]
sources: 2
tested_on: [equities, crypto]
---

# Overnight and intraday return momentum

> [!summary]
> Ranks stocks on the overnight or the intraday part of their past return, and trades the next return of the same part and of the other part.

## How it works

- **Inputs**: daily open and close prices per stock, split into overnight and intraday returns.
- **Formula**: past overnight (or intraday) return over the lookback, sorted into deciles.
- **Lookback / holding**: one month each, rebalanced monthly. A long-memory variant averages the past components with an exponential weight.
- **Output**: a decile rank per stock, and a long-short portfolio of top minus bottom decile.
- **Direction**: past overnight return predicts higher future overnight return and lower future intraday return. Past intraday return predicts the reverse.
- **Tested on**: US stocks.
- **Variant**: 24h market split into two 12h sessions; per session, follow or oppose the previous same-session sign (crypto).

## What the sources say

### Parameters
- **Lou 2019**
	- Lookback one month, hold one month (p. 195-197).
	- Long top decile, short bottom decile, value-weighted, NYSE breakpoints (p. 195).
	- Lag between ranking and holding tested from 1 to 60 months (p. 197, Fig. 2).
	- Variant: exponentially weighted average of past components, half-life 60 months, last month skipped (p. 197, Table 4).
- **Wu 2026**
	- Hourly Kraken BTC and ETH, 2016-2025 (p. 5)
	- 12 boundaries x 25 night-day rule pairs; picks: BTC Reversal/Reversal at 08:00 UTC, ETH Long/Reversal at 05:00 UTC (p. 11, 16)
	- Costs 0, 1, 2 bps per unit of turnover (p. 12)

### Why
- **Lou 2019**: some investors trade near the open and others later. Their persistent order flow gives continuation in the same period, then non-informative price pressure reverses in the other period (p. 193, 197). The authors call this a conjecture, only partly tested.
- **Wu 2026**
	- Crypto has no official open or close, so the boundary is an empirical choice (p. 4-5)
	- Boundaries may match regional activity; not tested (p. 25)

### Evidence
- **Lou 2019**: real data, US stocks 1993-2013, gross of costs, decile 10 minus decile 1, monthly
	- Sort on past overnight: overnight 3.47% (t = 16.57), intraday -3.24% (t = -9.34) (Table 1, p. 197).
	- Sort on past intraday: overnight -1.81% (t = -8.44), intraday 2.19% (t = 6.72) (Table 1, p. 197).
- **Wu 2026**: real data, full sample in-sample, plus a 2021-2025 holdout
	- Reversal contrast per session: BTC 23.89 bps (night), 27.71 bps (day); ETH day 42.79 bps (Table 10)
	- Against buy-and-hold: no significant difference; SPA p 0.66 to 0.996 (Tables 11-12)
	- Holdout: ETH rule picked again, wealth ratio 13.4 at 0 bps; BTC pick fails (Table 13)

### Limits
- **Lou 2019**
	- Gross of costs, which the authors expect to cut profits much (p. 193).
	- Sample limited to 1993-2013 by the trade data (p. 194).
- **Wu 2026**
	- BTC optimum collapses one hour either side of 08:00 (p. 16)
	- Break-even about 2.1 bps (BTC) and 5.6 bps (ETH) (p. 26)
	- One exchange; shorting and funding costs ignored (p. 26)

## Sources

- [[2019 - Lou Polk Skouras - A Tug of War Overnight vs Intraday Returns]] (Lou 2019)
- [[2026 - Wu Pinsky - Lagged Momentum and Reversal Across Daytime and Overnight Sessions in Bitcoin and Ethereum]] (Wu 2026)
