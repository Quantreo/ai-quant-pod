---
type: diagnostic
kind: performance
aliases: [passive long comparison, de-biased t-stat, long-bias removal, long-only Sharpe comparison, Equal-weight long benchmark, Buy-and-hold comparison, Paired log return differential]
sources: 6
---

# Always-long benchmark comparison

> [!summary]
> Does the strategy earn more than a passive long position in the same instrument?

## How it works

- **How**: measure the strategy's alpha over the always-long position of the same instrument, instrument by instrument. Also compare cumulative return with a passive long portfolio at the same ex-ante volatility.
- **Variant**: regress the strategy P&L on the long-only P&L of the same pool and take the t-stat of the residual (de-biased t-stat). Compare it with the t-stat of the long-only drift.
- **Reading**: the share of instruments with positive alpha, and the share where it is significant; or how far the t-stat falls once the long bias is removed.
- **Data needed**: strategy and passive long returns per instrument.
- **Variant**: bootstrap test of the paired daily log return difference.

## What the sources say

### Parameters
- **Moskowitz 2012**
	- Always-long on the same contract (p. 236).
	- Passive portfolio matched on ex-ante volatility (Fig. 3).
- **Lempérière 2014**
	- Long-only is the drift µ, the average return of each instrument (p. 3).
	- Applied to the pool, by sector and by period (p. 4; Tables 1-3, 8).
- **Christensen 2020**
	- Long-only e-mini S&P 500 over the same year, 2011, as the benchmark (p. 13)
	- Compared by annualised Sharpe ratio from daily returns and by cumulative return (p. 13, Fig. 6, 8)
- **Kosch 2026**
	- Equal-weight long in all available contracts, same cost convention, used for both the long and the short strategies (p. 10)
	- Compared by cumulative return, Sharpe and maximum drawdown, historically and over 500 bootstrap paths (p. 12-14)
- **Hudson 2019**: buy-and-hold of each coin; share of rules beating it on return, Sharpe, Sortino and Calmar (Table 7)
- **Wu 2026**: d = ln(1 + strategy return) - ln(1 + buy-and-hold return), daily; stationary bootstrap, 5,000 draws, 7-day blocks (Eq. 26-27, p. 14)

### Why
- **Moskowitz 2012**: gives the return beyond a passive long (p. 236).
- **Lempérière 2014**: removes the long bias that comes from the upward drift of most markets (p. 4).
- **Christensen 2020**: the strategy signals are zero mean, so any gain is not long bias (p. 13, 18)
- **Kosch 2026**: a low-discretion reference that is easy to read and hard to overfit (p. 11)
- **Hudson 2019**: crypto prices trended up, so buy-and-hold may beat the rules (p. 211)
- **Wu 2026**: links the test directly to terminal wealth (p. 14)

### Evidence
- **Moskowitz 2012**: real data, in-sample, gross of costs, 1985-2009.
	- Alpha positive in 90% of contracts (p. 236).
	- Alpha significant in 26% of contracts (p. 236).
- **Lempérière 2014**: real data, in-sample, gross of costs.
	- Correlation of trend with long-only: +15% (p. 4).
	- Futures since 1960: t from 5.9 to 5.0 once de-biased (p. 4).
	- Since 1800: 10.5 to 9.8 (Fig. 4); bonds 3.9 to 2.7, indices 10.2 to 6.3 (Table 8).
	- Commodities since 1800: the de-biased t (3.1) is below the long-only t (4.5) (p. 9; Table 8).
- **Christensen 2020**: real data, one year, pre-cost
	- Long-only Sharpe 0.4, about its long-run average (p. 18)
	- IOHMM strategies ≈2.0 to ≈2.5; correlation with long-only ≈0.08 and ≈ -0.12 (≈ Fig. 8)
- **Kosch 2026**: real data, out of sample 2016-2024, net of cost
	- Benchmark bootstrap average: 16.81% cumulative, Sharpe 0.191, MaxDD -0.414; no model beats it on all three (Table 3)
	- Historical DVR long beats it: Sharpe 0.245 against 0.183 (Table 2); not significant after Holm (Table 4)
- **Hudson 2019**: real data, in-sample, gross
	- 4.96% to 15.69% of rules beat buy-and-hold on return; 27.99% to 57.64% on Sortino or Calmar (Table 7)
- **Wu 2026**: real data, full sample
	- BTC 4.24 bps a day, ETH 11.10 bps at 0 bps; all confidence intervals include zero (Table 11)
	- Wealth ratios 4.70 (BTC) and 57.69 (ETH) (Table 11)

### Limits
- **Moskowitz 2012**
	- Not stated.
- **Lempérière 2014**
	- The regression is not detailed (one beta, full sample, not stated) (p. 4).
	- The drift is defined as an average daily return, but the data are monthly (p. 3).
- **Christensen 2020**
	- One year only (p. 17)
- **Kosch 2026**
	- A short strategy against a long benchmark mixes direction and selection, so it is not a test of short selection (p. 10, 14)
	- A single-contract portfolio against a 15-contract benchmark mixes concentration and selection (p. 10)
- **Hudson 2019**: shares of rules only, no test (Table 7)
- **Wu 2026**
	- Not exposure-matched: rules can be short or flat (p. 26)
	- Low power (p. 22-23)

## Sources

- [[2012 - Moskowitz Ooi Pedersen - Time Series Momentum]] (Moskowitz 2012)
- [[2014 - Lempérière Deremble Seager et al - Two centuries of trend following]] (Lempérière 2014)
- [[2020 - Christensen - Hidden Markov Models Applied To Intraday Momentum Trading With Side Information]] (Christensen 2020)
- [[2026 - Kosch Forsberg - Seasonal Trading in Commodity Futures Evidence from Regression and Singular Spectrum]] (Kosch 2026)
- [[2019 - Hudson Urquhart - Technical trading and cryptocurrencies]] (Hudson 2019)
- [[2026 - Wu Pinsky - Lagged Momentum and Reversal Across Daytime and Overnight Sessions in Bitcoin and Ethereum]] (Wu 2026)
