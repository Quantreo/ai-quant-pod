---
type: technique
brick: signal
aliases: [Pairs trading, Statistical arbitrage pairs, Distance method, SSD pairs, Cointegration pairs, Engle-Granger pairs]
sources: 1
tested_on: [crypto]
---

# Pairs trading spread signal

> [!summary]
> Picks pairs of assets whose prices moved together in a formation window, then trades the gap between them when it stretches.

## How it works

- **Inputs**: price history of each asset over a formation window, and a trading window that follows.
- **Formula**: select pairs that look related, define a spread per pair, normalise it. Short the spread above a threshold, long below minus the threshold, close at zero or at the window end.
- **Lookback / holding**: formation window, then trading window; the pairs are re-selected at each jump.
- **Output**: long or short spread position per selected pair.
- **Direction**: market neutral within the pair; contrarian on the spread.
- **Tested on**: cryptocurrencies.
- **Variant**: pairs chosen by distance (smallest squared gaps between normalised prices) or by cointegration test (spread is the residual).

## What the sources say

### Parameters
- **Fil 2020**
	- Distance: top 20 pairs by sum of squared differences of normalised log prices (Eq. 1, p. 172646)
	- Cointegration: Engle-Granger test, spread is the residual (p. 172646-172647)
	- Threshold 2 standard deviations; close at zero crossing or end of trading (p. 172646)
	- Formation / trading / jump: daily 4 months / 2 / 1; hourly 20 / 10 / 10 days; 5-minute 6 / 3 / 3 days (Table 1)
	- 26 Binance coins, 2018-2019, prices in Bitcoin (p. 172646)

### Why
- **Fil 2020**: a short-run divergence of a pair from its long-run relation should revert; the rules follow Gatev and Vidyamurthy (p. 172644, 172646)

### Evidence
- **Fil 2020**: real data, in-sample, net of 30 bps per trade and a one-period lag
	- Daily: distance -0.07% a month, cointegration 1.36% (Table 2)
	- Hourly 3.10% and 1.11%; 5-minute 11.61% and 4.16% (Table 2)
	- Daily maximum drawdown 26.32% and 24.89% (Table 2)

### Limits
- **Fil 2020**
	- No lag lifts 5-minute distance to 16.80% (Table 3)
	- Threshold and stop-loss compared on the same data (Table 4)
	- Short-selling costs excluded; shorting is hardly possible for these coins (p. 172647)
	- Random pairs earn 6.54% at 5 minutes: see [[Random pairs placebo]] (Table 2)

## Sources

- [[2020 - Fil Kristoufek - Pairs Trading in Cryptocurrency Markets]] (Fil 2020)
