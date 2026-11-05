---
type: technique
brick: signal
aliases: [contrarian portfolio, buy losers sell winners, PAMR, passive aggressive mean reversion, Short-term reversal, Loser minus winner, REV]
sources: 2
tested_on: [equities, crypto]
---

# Cross-sectional mean reversion

> [!summary]
> Each day, moves weight from the assets that did better than average to those that did worse, expecting them to reverse the next day.

## How it works

- **Inputs**: daily price relatives (close over previous close) of the assets, the previous weights, a threshold ε and an optional cap C.
- **Formula**: portfolio return r = weights times price relatives. If r is at or below ε, keep the weights. Otherwise move weight from assets above the average price relative to assets below it. The step is (r - ε) divided by the squared spread of price relatives around their average. Then project the weights to long-only, fully invested. Variants cap the step at C, or add a constant to its denominator.
- **Lookback / holding**: the last day only, reset every day.
- **Output**: new long-only weights that sum to 1.
- **Direction**: long only.
- **Tested on**: stocks and equity indexes.
- **Variant**: short-term reversal sort: long last period's losers, short winners (crypto).

## What the sources say

### Parameters
- **Li 2012**
	- ε = 0.5 and C = 500 for all datasets; daily rebalance at the last close (p. 238, 224)
	- PAMR-1 step capped at C, PAMR-2 adds 1/(2C) to the denominator (p. 232-233)
- **Kozlowski 2021**
	- Prior day, week or month return; five equal-weight quintiles, long losers, short winners, hold one period (p. 3)
	- 199 coins from the top 200 by market cap on 28 Dec 2014; 2015 to mid-2019 (p. 2-3)
	- Drop coin-periods with monthly turnover below 1% (fn 2)

### Why
- **Li 2012**
	- A stock that did worse than others tends to do better the next day (p. 228-229)
	- Keeping the old weights when the return is low avoids stocks in a crash (p. 229)
- **Kozlowski 2021**: overreaction plus compensation for liquidity provision, read from size and liquidity splits (p. 1, 6-8)

### Evidence
- **Li 2012**: real data, in-sample backtests, gross of costs, long only.
	- NYSE (O) 1962-1984: wealth 5.14E+15 vs 14.50 for the market (Table 4, p. 242)
	- TSE 1994-1998: 264.86 vs 1.61. MSCI 2006-2010: 15.23 vs 0.91 (Table 4, p. 242)
	- DJIA 2001-2003: 0.68 vs 0.76 for the market (Table 4, p. 242)
- **Kozlowski 2021**: real data, in-sample, gross, crypto
	- Loser minus winner 7.37% a day, 10.03% a week, 28.22% a month (Table 1)
	- Small illiquid coins 18.63% a day; large liquid 0.44% a day and -1.58% a week (n.s.) (Table 3)
	- Similar in both halves of the sample and both VIX states (Table 3)

### Limits
- **Li 2012**
	- Needs mean reversion in the asset pool; fails on DJIA (p. 251)
	- NYSE (O) result leans on one volatile stock: 1.27E+08 without it (p. 243)
	- Can lose to the best constant rebalanced portfolio when one stock crashes and another explodes (p. 234)
- **Kozlowski 2021**
	- No costs and no shorting constraints (whole paper)
	- Significance legend of the tables contradicts the text (Tables 1-3, p. 4)

## Sources

- [[2012 - Li Zhao Hoi et al - PAMR Passive aggressive mean reversion strategy for portfolio selection]] (Li 2012)
- [[2021 - Kozlowski Puleo Zhou - Cryptocurrency return reversals]] (Kozlowski 2021)
