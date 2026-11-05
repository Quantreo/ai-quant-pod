---
type: diagnostic
kind: attribution
aliases: [Double sort, 3 x 3 sort, Conditional sort]
sources: 1
---

# Bivariate portfolio sort

> [!summary]
> Does a signal pay everywhere, or only inside one level of a second characteristic?

## How it works

- **How**: at each rebalance, rank assets on two characteristics and cut each into three groups. Hold the nine cells at equal weight. Build a zero-investment spread along each axis (top minus bottom of one characteristic, inside each group of the other).
- **Reading**: a spread that is significant in one group and not in the others shows where the signal lives.
- **Data needed**: both characteristics per asset and date, and asset returns.

## What the sources say

### Parameters
- **Begušić 2019**
	- Momentum (14-day return) by illiquidity (14-day Amihud), 30 / 40 / 30 cuts (p. 3)
	- Equal weight, rebalanced every 14 days (p. 3)
	- Spreads: winners minus losers (UMD) per liquidity group, illiquid minus liquid (IML) per momentum group (p. 3)
	- Test: two-tailed t-test at 5% (p. 3)

### Why
- **Begušić 2019**: to study how momentum interacts with liquidity (p. 1, 3).

### Evidence
- **Begušić 2019**: in-sample, Jan 2015 to Jan 2019, 711 coins, mean daily return, gross
	- Only two of the spreads are significant: UMD among liquid coins (0.26%) and IML among losers (0.52%) (Table 1, p. 3)
	- UMD: liquid 0.26, neutral -0.06, illiquid -0.33 (Table 1)
	- Best cell is illiquid losers at 1.07%, worst is liquid losers at 0.31% (Table 1)

### Limits
- **Begušić 2019**
	- Independent or sequential sorting is not stated
	- No t-statistics printed
	- Printed spreads do not equal the differences of the printed cell means (for example IML losers 0.52 printed, 0.76 computed from Table 1)

## Sources

- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
