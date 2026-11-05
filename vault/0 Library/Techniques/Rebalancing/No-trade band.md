---
type: technique
brick: rebalancing
aliases: [Two-threshold buy and sell rule, Rate band]
sources: 2
tested_on: [equities, crypto]
---

# No-trade band

> [!summary]
> Two thresholds on a state variable: enter at the upper one, exit at the lower one, and do nothing in between.

## How it works

- **Frequency or trigger**: a trade happens only when the variable crosses a threshold. Flat to long at the upper threshold, long to flat at the lower one.
- **Band**: between the two thresholds the position does not change.
- **Cost rationale**: trading is costly, so the position changes only when the variable crosses a threshold.
- **Variant**: band between two market rates: trade only when one rate leaves the range set by two others (stablecoin deposit and borrow rates around the USD rate).

## What the sources say

### Parameters
- **Dai 2011**
	- Buy at p*b, sell at p*s, with p the bull probability (p. 9)
	- Constant until close to the end of the horizon, ≈ 0.8 (sell) and ≈ 0.95 (buy) in the example (≈ Fig. 1, p. 8-10)
	- S&P 500 yearly values: sell 0.391 to 0.739, buy 0.703 to 0.900 (Table 7, p. 22)
	- Cost in the model: 0.1% per trade (p. 11)
- **Fan 2024**
	- No trade when stablecoin deposit rate <= USD rate <= stablecoin borrow rate (p. 27)

### Why
- **Dai 2011**: thresholds solve the model's equations with transaction costs (p. 8-9)
- **Fan 2024**: profit from the rate spread only, without a bet on price (p. 26)

### Evidence
- **Dai 2011**: whole trend rule, not the band alone. Real data, ex-ante, gross or net not stated.
	- S&P 500 1972-2011: 11.03% a year vs 9.8% buy and hold (Table 4, p. 14)
	- SSE index 2001-2011: 14.0% vs 2.58% buy and hold (Table 4, p. 14)
	- Simulation inside the model: 41.16 trades over 40 years (Table 2, p. 11)
- **Fan 2024**: real data, in-sample, gross
	- USDT 9.28% a year, Sharpe 3.54; DAI 10.92%, Sharpe 1.54 (Table 9)

### Limits
- **Dai 2011**
	- Results depend on the path and on the parameters (p. 11, 14)
- **Fan 2024**
	- Effect of the band itself not isolated (Table 9)
	- USD deposit and borrow rates assumed equal (fn 20)

## Sources

- [[2011 - Dai Zhang Zhu - Optimal Trend Following Trading Rules]] (Dai 2011)
- [[2024 - Fan Jiao Lu et al - The Risk and Return of Cryptocurrency Carry Trade]] (Fan 2024)
