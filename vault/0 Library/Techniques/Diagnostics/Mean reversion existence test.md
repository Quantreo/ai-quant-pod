---
type: diagnostic
kind: attribution
aliases: [naive contrarian test, conditional reversal contrast, negative-lag minus positive-lag mean]
sources: 2
---

# Mean reversion existence test

> [!summary]
> Does buying the recent losers earn a positive average daily return in this asset pool?

## How it works

- **How**: each day, build a naive contrarian portfolio with weights proportional to the gap between each asset's return and the best asset's return of the last day. The best asset gets zero and the worst the largest weight. Compute the average daily return of this portfolio.
- **Reading**: an average daily return above 1 means buying losers pays in the pool. Below 1 means it loses on average.
- **Data needed**: daily price relatives of the pool.
- **Variant**: mean next-period return after a negative lagged return minus after a positive one, with a bootstrap confidence interval.

## What the sources say

### Parameters
- **Li 2012**
	- Weights proportional to the gap to the last best stock; average daily return compared with 1 (p. 252)
- **Wu 2026**: Δ = E[r | lag < 0] - E[r | lag > 0], same session type, 12h sessions; stationary bootstrap, 5,000 draws, Holm-adjusted (Eq. 24, p. 13-14)

### Why
- **Li 2012**
	- Checks whether the mean reversion behind the strategy exists in the data (p. 252)
- **Wu 2026**: tests the mechanism separately from the strategy's profit (p. 13)

### Evidence
- **Li 2012**: real data, in-sample. Gross or net not stated.
	- Average daily return above 1 on five datasets, from 1.000431 (TSE) to 1.000940 (NYSE (O)) (Table 9, p. 252)
	- DJIA: 0.999848, where the strategy it supports also fails (Table 9, p. 252)
- **Wu 2026**: real data
	- BTC 23.89 bps (night), 27.71 bps (day); ETH day 42.79 bps; Holm p at most 0.003 (Table 10)
	- BTC night not significant in 2016-2020, p = 0.120 (Table 10)

### Limits
- **Li 2012**
	- The authors cannot claim it identifies successful pools with certainty (p. 252)
- **Wu 2026**: a significant signal does not give a significant gain over buy-and-hold (p. 22-23)

## Sources

- [[2012 - Li Zhao Hoi et al - PAMR Passive aggressive mean reversion strategy for portfolio selection]] (Li 2012)
- [[2026 - Wu Pinsky - Lagged Momentum and Reversal Across Daytime and Overnight Sessions in Bitcoin and Ethereum]] (Wu 2026)
