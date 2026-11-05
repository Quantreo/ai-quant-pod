---
type: technique
brick: signal
aliases: [Momentum-liquidity double sort, Amihud illiquidity sort, Liquid winners, Illiquid losers]
sources: 1
tested_on: [crypto]
---

# Liquidity-conditioned momentum

> [!summary]
> Reads momentum separately inside liquidity groups, and trades winners where assets are liquid and losers where they are illiquid.

## How it works

- **Inputs**: past return of each asset over a lookback; an illiquidity measure such as Amihud (mean of absolute daily return over dollar volume) over a lookback.
- **Formula**: sort assets on past return and on illiquidity; form the cross of the groups. Hold the winners in the most liquid group; hold the losers in the most illiquid group.
- **Lookback / holding**: short lookbacks for both measures; ranking redone at each rebalance.
- **Output**: membership of a liquidity-by-momentum portfolio.
- **Direction**: continuation among liquid assets, reversal among illiquid ones. Long-only or long-short.
- **Tested on**: cryptocurrencies.

## What the sources say

### Parameters
- **Begušić 2019**
	- Return and Amihud illiquidity both over 14 days, no skip (Eq. 1-2, p. 3)
	- Breakpoints at the 30th and 70th percentiles on each measure, 3x3 portfolios; independent or sequential sort not stated (p. 3)
	- Equal weight, rebalanced and held 14 days (p. 3)
	- Coinmarketcap coins, Jan 2015 to Jan 2019, 711 eligible at least once (p. 2)

### Why
- **Begušić 2019**
	- Herding and positive social feedback make momentum strongest in liquid coins; cited, not tested (p. 4)
	- Illiquid coins show mean reversion, in line with earlier work (p. 4)
	- Long-only because shorting crypto is limited (p. 4)

### Evidence
- **Begušić 2019**: real data, in-sample, one specification
	- Winners minus losers, liquid coins: 0.26% a day, significant at 5%; illiquid coins -0.33%, not significant (Table 1)
	- Illiquid minus liquid among losers: 0.52% a day, significant (Table 1)
	- Long-only gross: illiquid losers 1.07% a day, IR 2.49; liquid winners 0.71%, IR 1.59, vs cap-weighted (Table 1)
	- At 100 bps: IR 2.16 and 1.27; cost method not stated (Table 2)

### Limits
- **Begušić 2019**
	- Illiquid losers may lose more to bid-ask costs in practice (p. 5)
	- Printed spreads differ from the differences of cell means (reading note, Table 1)
	- Number of coins per portfolio not reported; ≈ under 20 eligible coins before 2017 (≈ Fig. 1)
	- All portfolios fall ≈ from Jan 2018 to the end of the sample (≈ Fig. 2)

## Sources

- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
