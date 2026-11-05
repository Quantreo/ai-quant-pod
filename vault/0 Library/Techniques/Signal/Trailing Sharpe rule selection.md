---
type: technique
brick: signal
aliases: [Ex ante dynamic rule selection, Sharpe-ranked rule-rate pairs, Dynamic technical trading strategy]
sources: 1
tested_on: [fx]
---

# Trailing Sharpe rule selection

> [!summary]
> Ranks every rule and market pair by its past Sharpe ratio, re-ranks on a fixed schedule and trades the top-ranked pairs.

## How it works

- **Inputs**: daily returns of every rule-market pair, from a pool of rules applied to a pool of markets.
- **Formula**: at each re-ranking date, compute each pair's Sharpe ratio over the whole available history, keeping pairs with a minimum history. Rank them. Buckets of equal size, for example ranks 1 to 25, are equal-weighted portfolios.
- **Lookback / holding**: expanding window; re-ranked every k days; each pair's own rule keeps trading daily in between.
- **Output**: the set of pairs to trade, each with its own long or short signal.
- **Direction**: long and short, set by each rule.
- **Tested on**: currencies.
- **Variant**: rank by Sortino ratio or mean return instead of Sharpe; re-rank every 250 days; restrict the market pool.

## What the sources say

### Parameters
- **Ivanova 2014**
	- 16 rules (7 filters, 3 moving averages, 3 momentum, 3 channels) on 21 USD and 19 cross rates (p. 4-5)
	- Start after 1020 days; pairs need at least 250 days of data (p. 8-9, fn 8)
	- Re-rank every 20 business days; top 300 pairs split into 12 portfolios of 25 (p. 9-10)
	- Daily data, 1976 to 2012 (p. 8, Table 1)

### Why
- **Ivanova 2014**
	- Mimics a trader who backtests rules and picks the best, with no look-ahead (p. 8)
	- Sharpe, not return: a more volatile market would otherwise look better for the same rule (fn 9)

### Evidence
- **Ivanova 2014**: real data, ex ante selection, net or gross not stated
	- Mean excess return 4.41% a year for ranks 1-25 against 0.69% for ranks 276-300 (p. 10, Fig. 1)
	- Sharpe 0.81 for ranks 1-25 against 0.17 for ranks 276-300 (p. 10)
	- Only the top bucket keeps rising after about 1993; ≈155% cumulative by 2012 (≈ Fig. 3)
	- Inference similar with Sortino or mean-return ranking, 250-day re-ranking, USD-only or G10-only rates (fn 10; appendices not seen)

### Limits
- **Ivanova 2014**
	- The pool of rules was fixed by prior literature (p. 4)
	- Sharpe falls with rank but not strictly: ranks 126-150 are at 0.14 (≈ Fig. 1)
	- Turnover and number of pair switches not reported (whole paper)

## Sources

- [[2014 - Ivanova Neely Weller et al - Can risk explain the profitability of technical trading in currency markets]] (Ivanova 2014)
