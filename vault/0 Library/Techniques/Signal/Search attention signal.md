---
type: technique
brick: signal
aliases: [Investor attention signal, Google search signal, Google Trends signal, Twitter attention, Negative attention ratio]
sources: 1
tested_on: [crypto]
---

# Search attention signal

> [!summary]
> Reads a jump in search or social-media attention to a coin as a forecast of its returns over the next one or two weeks.

## How it works

- **Inputs**: weekly Google search count (or Twitter post count) for the coin's name.
- **Formula**: this week's count minus the average of the preceding four weeks, normalised. Regress the next returns on it, or sort weeks into quintiles of it.
- **Lookback / holding**: four-week baseline; returns read 1 to 4 weeks ahead.
- **Output**: a continuous attention score, or its quintile.
- **Direction**: high attention predicts high returns.
- **Tested on**: cryptocurrencies.
- **Variant**: negative attention, the ratio of searches for "coin hack" to searches for the coin; high values predict lower returns.

## What the sources say

### Parameters
- **Liu 2018**
	- Google deviation from the previous four-week average, normalised, matched to the coin's own returns (p. 23-24)
	- Twitter post count for "Bitcoin" built the same way (Table 26)
	- Negative attention: Google "Bitcoin hack" over "Bitcoin", normalised (Table 28)
	- Quintile sorts: full sample, since 2013, cutoffs from the first two years (Tables 20-22)

### Why
- **Liu 2018**: attention proxies are used following Da, Engelberg and Gao; no mechanism is given (p. 4)

### Evidence
- **Liu 2018**: real data, in-sample, gross
	- Bitcoin, one standard deviation of Google attention: +1.84% next week (t = 2.17), +2.30% two weeks ahead (Table 19)
	- Quintiles: top 11.20% next week, Sharpe 0.48; bottom 1.07% (Table 20)
	- Cutoffs from the first two years: top 8.10%, bottom 0.70% (Table 22)
	- Hack ratio: -2.75% next week (Table 28)

### Limits
- **Liu 2018**
	- Google deviations rise after price rises: coefficient 0.01 on the current and previous week's return (t 3.64 and 4.04) (Table 25)
	- Bootstrapped t-statistics are lower, for example 1.76 against 2.17 at one week (Table 19)
	- Ethereum predictability appears at weeks 1, 3 and 6 only (Table 24)
	- No trading rule, no costs (whole paper)

## Sources

- [[2020 - Liu Tsyvinski - Risks and Returns of Cryptocurrency]] (Liu 2018)
