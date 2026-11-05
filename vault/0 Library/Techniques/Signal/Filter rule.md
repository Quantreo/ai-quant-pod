---
type: technique
brick: signal
aliases: [Filter trading rule, Alexander filter, F1, F2]
sources: 2
tested_on: [crypto, fx]
---

# Filter rule

> [!summary]
> Buys when the price has risen x% above its most recent low and sells short when it has fallen x% below its most recent high.

## How it works

- **Inputs**: closing prices.
- **Formula**: most recent low (high) = latest close below (above) the j previous closes. Long when the price is x% above that low for d periods; short when x% below that high for d periods.
- **Lookback / holding**: j sets the reference extreme; hold until the opposite signal, or k periods then flat.
- **Output**: +1, -1 or 0.
- **Direction**: long and short, trend following.
- **Tested on**: cryptocurrencies.

## What the sources say

### Parameters
- **Hudson 2019**
	- x in {0, 0.01, 0.05, 0.1, 0.5, 1, 5}%, d in {1 to 5}, j from 2 to 200 days, k in {3, 5} (Appendix, p. 216)
	- 963 filter rules, daily data (Appendix)
- **Ivanova 2014**
	- y in {0.5, 1, 2, 3, 4, 5, 10}% above the latest local low or below the latest local high; position kept until the opposite signal (p. 5, Eq. 1)
	- 21 USD rates and 19 cross rates, daily, 1973-2012 (Table 1)
### Why
- **Hudson 2019**: one of the first and simplest trend rules (Appendix, p. 216)
- **Ivanova 2014**: among the most studied FX rules (p. 4)
### Evidence
- **Hudson 2019**: real data, in-sample, gross
	- Average annualised return 7.97% (Bitstamp) to 16.45% (Ethereum) (Table 2)
	- 92.80% to 99.68% of filter rules significant at 5% before multiple-testing correction (Table 4)
	- Mean breakeven cost 30.66 to 147.56 bps (Table 6)
- **Ivanova 2014**: real data, inside a dynamic rule selection
	- Small filters (y up to 2%) and large filters are two of the five rule groups tracked in the top portfolio (p. 10-11, Fig. 2)
	- Best single rule by Sharpe: RUB filter 0.5%, Sharpe 1.19, mean 9.40% a year, 2000-2012 (Table 2)
### Limits
- **Hudson 2019**
	- Highest number of trades of the five rule families (Table 6)
	- Sell signals add nothing (Table 2)
	- Appendix rule counts do not add up (Appendix, p. 216)
- **Ivanova 2014**
	- No result for filters alone; they are mixed with other rules in the portfolios (p. 11)

## Sources

- [[2019 - Hudson Urquhart - Technical trading and cryptocurrencies]] (Hudson 2019)
- [[2014 - Ivanova Neely Weller et al - Can risk explain the profitability of technical trading in currency markets]] (Ivanova 2014)
