---
type: technique
brick: signal
aliases: [Past-return rank, Winners minus losers]
sources: 1
tested_on: [crypto]
---

# Cross-sectional momentum

> [!summary]
> Rank assets on their cumulative past return and label the top group winners and the bottom group losers.

## How it works

- **Inputs**: price history of each asset in the universe at the rebalance date.
- **Formula**: cumulative return over a lookback window, then a rank across assets and a cut into groups by quantile.
- **Lookback / holding**: a lookback window and a rebalance interval, both parameters.
- **Output**: a group label per asset (losers, neutral, winners).
- **Direction**: long winners and short losers when momentum holds. The same labels can be used the other way where losers rebound.
- **Tested on**: crypto.

## What the sources say

### Parameters
- **Begušić 2019**
	- Cumulative return (P(t) - P(t-T)) / P(t-T) with T = 14 days (Eq. 1, p. 3)
	- Losers: lowest 30%. Neutral: 30% to 70%. Winners: highest 30% (p. 3)
	- Rebalanced every 14 days (p. 3)
	- Sorted inside three liquidity brackets (see [[Amihud illiquidity]]) (p. 3)
	- Variants studied: long-only liquid winners, and long-only illiquid losers (p. 4)

### Why
- **Begušić 2019**: momentum may come from investor herding and is stronger in liquid states, as in international equities. The herding link is cited from other studies, not tested (p. 1, 2, 4).

### Evidence
- **Begušić 2019**: in-sample, Jan 2015 to Jan 2019, 711 coins, gross unless stated
	- Winners minus losers among liquid coins: 0.26% daily, significant at 5% (Table 1, p. 3)
	- Same spread among neutral coins -0.06% and illiquid coins -0.33%, not significant (Table 1, p. 3)
	- Long-only liquid winners: 0.71% daily, IR 1.59 gross; 0.60%, IR 1.27 at 100 bps (Table 2, p. 5). IR is against a cap-weighted portfolio.

### Limits
- **Begušić 2019**
	- One setting only; no test of the window, the cutoffs or the rebalance interval
	- No t-statistics printed; four years of data (p. 2)
	- Shorting is limited in crypto, so long-only legs are studied (p. 4)
	- Cost method is not stated; Figure 2 assumes zero costs and zero market impact (p. 5)

## Sources

- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
