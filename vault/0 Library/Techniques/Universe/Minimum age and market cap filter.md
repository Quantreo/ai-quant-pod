---
type: technique
brick: universe
aliases: [Dynamic universe, Size and age floor]
sources: 1
tested_on: [crypto]
---

# Minimum age and market cap filter

> [!summary]
> Keep an asset only if it has traded long enough and its market cap stayed above a small floor over that period.

## How it works

- **Selection rule**: asset enters when its history is at least T long and its market cap was never below M over that window. Pegged assets (stablecoins) are removed.
- **Liquidity filter**: the market cap floor, set low on purpose.
- **Point-in-time**: the universe is rebuilt over time, so assets enter and leave as they pass or fail the rule.

## What the sources say

### Parameters
- **Begušić 2019**
	- T = 26 weeks, M = 10^6 USD (p. 2)
	- Stablecoins removed (p. 2)
	- Data: daily market cap, price and volume from one source (p. 2)

### Why
- **Begušić 2019**: keep relevant and liquid coins, as a realistic investor would. A small floor avoids a large-cap bias (p. 2).

### Evidence
- **Begušić 2019**: description only, no test of the filter
	- 711 coins qualified at least once, Jan 2015 to Jan 2019 (p. 2)
	- Universe grows from about 15 coins in 2015 to 2016 to about 540 at the peak (Fig. 1)

### Limits
- **Begušić 2019**
	- No robustness test of T or M; how they were chosen is not stated
	- About 15 coins in 2015 to 2016, so early portfolios hold few coins (Fig. 1)
	- Treatment of delisted coins is not stated

## Sources

- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
