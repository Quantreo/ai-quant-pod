---
type: technique
brick: signal
aliases: [Triangular arbitrage, Currency arbitrage detection, FX statistical arbitrage LP]
sources: 1
tested_on: [fx]
---

# Triangular arbitrage linear program

> [!summary]
> Chooses how much to exchange along each currency pair so that a cycle of exchanges, such as A to B to C to A, ends with more home currency than it started with.

## How it works

- **Inputs**: exchange rates between every directly tradable currency pair, observed or forecast for the execution date.
- **Formula**: a cycle gains when the product of its rates exceeds 1. A linear program picks non-negative trade weights that maximise home-currency inflow minus outflow, with zero net holding in every other currency and a fixed total trade size.
- **Lookback / holding**: no lookback in the base form. Holding is as long as the cycle takes, or until the next rate observation when positions are held.
- **Output**: one trade weight per currency pair, summing to the fixed total.
- **Direction**: market neutral by construction, no net foreign currency left open.
- **Tested on**: currencies (spot).
- **Variant**: when rates are forecast, the weights depend on the forecast and on how long the gap between observation and execution is.

## What the sources say

### Parameters
- **Hong 2025**
	- Total trade 1 unit of home currency per day, scaled if another size (p. 3, Eq. 5)
	- Constraints: zero net holding outside home currency, weights at least 0 (p. 3, Eq. 4, 6)
	- Rates: next-day forecast from a graph neural network, same forecast fed to the benchmark and to the authors' method (p. 6)
	- 10 currencies, home currency USD, EUR or JPY (p. 6)

### Why
- **Hong 2025**: triangular violations exist in real FX data according to cited studies, and the cycle gain is a riskless profit if known in advance (p. 1-3)

### Evidence
- **Hong 2025**: real data, rolling refits, gross of costs, daily, execution one day after observation
	- Information ratio 27.21, 27.10, 26.87 (%) for home currency USD, EUR, JPY (Table 1)
	- Annual return about 6.1% to 6.2%, volatility 1.41% (Table 1)
	- Maximum drawdown 1.60% to 1.72% (Table 1)

### Limits
- **Hong 2025**
	- No transaction costs or bid-ask spreads (p. 4-5)
	- Unlimited borrowing assumed at the risk-free rate (p. 4-5)
	- It is the authors' benchmark. Its own result is given only next to their neural-network sizing (Table 1)
	- Ignoring the lag between observation and execution exposes the method to look-ahead bias, the authors say of earlier versions (p. 2)

## Sources

- [[2025 - Hong Klabjan - Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage]] (Hong 2025)
