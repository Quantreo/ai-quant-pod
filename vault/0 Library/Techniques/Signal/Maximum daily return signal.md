---
type: technique
brick: signal
aliases: [MAX effect, MAX, Lottery demand signal, Extreme positive return sort, MAX(N)]
sources: 2
tested_on: [crypto]
---

# Maximum daily return signal

> [!summary]
> Ranks assets on their largest daily return over a recent window and trades the next period's spread between high-MAX and low-MAX assets.

## How it works

- **Inputs**: daily returns of each asset over a recent window.
- **Formula**: MAX = highest daily return in the window; sort assets into quantiles on MAX.
- **Lookback / holding**: window of a week to a month; hold one week, rebalance weekly.
- **Output**: quantile membership; long-short between extreme quantiles.
- **Direction**: depends on the source: long low-MAX and short high-MAX (lottery overpricing), or the reverse (continuation).
- **Tested on**: cryptocurrencies.
- **Variant**: MAX(N), the average of the N highest daily returns in the window.
- **Variant**: skip the most recent day when computing MAX.

## What the sources say

### Parameters
- **Grobys 2021**
	- MAX over the last 7 days, weekly quintile sort, equal weight (p. 6, 10)
	- 20 coins ranked 2 to 21 by market cap on 2 Jan 2016, Bitcoin excluded; 2016-2019 (p. 4)
	- Variant: skip the most recent day (p. 9)
- **Ozdamar 2021**
	- MAX over the past 28 days, weekly decile sort, value and equal weight (p. 6-7)
	- All coins above 5 million USD, entered after six months; 2014 to Sep 2020 (p. 5)
	- Variant: MAX(N), N = 2 to 5 (Table 3)

### Why
- **Grobys 2021**
	- Investors pay up for coins with extreme positive returns (lottery demand), so they earn less next (p. 3, 11)
	- Weekly horizon because crypto returns are short-memory and monthly data are too few (p. 2, 6)
- **Ozdamar 2021**
	- Follows Bali et al. (2011); weekly because crypto reacts faster (p. 3)
	- Authors read their positive sign as continuation, close to momentum, against lottery preference (p. 11)

### Evidence
- **Grobys 2021**: real data, in-sample, gross
	- High minus low MAX: -1.54% a week, bootstrap t = -2.68 (Table 1)
	- Bitcoin-adjusted alpha -1.75% (Table A3); skip one day: -1.82% (Table 3)
	- Standard t-statistic -1.57, not significant (Table A8)
- **Ozdamar 2021**: real data, in-sample, gross
	- High minus low MAX, value weight: +3.0% a week, t = 4.10; alpha 2.0% (Table 2)
	- MAX(N), N = 1 to 5: +1.8% to +3.0% a week, all significant (Table 3)
	- Controlling for idiosyncratic volatility: +0.9% (t = 2.72) (Table 10)

### Limits
- **Grobys 2021**
	- Four coins per quintile (p. 6)
	- Shorting constrained; long-only version untested (p. 11)
	- No costs (whole paper)
- **Ozdamar 2021**
	- High-MAX coins are small and illiquid (Table 6)
	- Cumulative long-short chart does not match table averages (Fig. 1, Table 2)
	- No costs (whole paper)

## Sources

- [[2021 - Grobys Junttila - Speculation and lottery-like demand in cryptocurrency markets]] (Grobys 2021)
- [[2021 - Ozdamar Akdeniz Sensoy - Lottery-like preferences and the MAX effect in the cryptocurrency market]] (Ozdamar 2021)
