---
type: technique
brick: risk
aliases: [Stop as a fraction of ATR, Volatility-scaled stop]
sources: 1
tested_on: [equities]
---

# ATR-based stop

> [!summary]
> Place the stop at a distance equal to a fraction of the average true range, so the stop width follows volatility.

## How it works

- **What it limits**: the loss on one trade, and the stop distance R used for sizing and targets
- **Trigger / level**: stop at entry minus (long) or plus (short) k x ATR over n days
- **How the level is set**: n (ATR lookback) and k (fraction of the ATR) are parameters

## What the sources say

### Parameters
- **Zarattini 2023**
	- ATR over 14 days (p. 13)
	- Stop from 5% to 100% of the ATR, 11 values (p. 13)

### Why
- **Zarattini 2023**
	- The ATR is "a better and more stable representation of the volatility" (p. 13)

### Evidence
- **Zarattini 2023**: grid on TQQQ, in-sample, net of commissions, zero slippage, 2016 to 2023
	- Best cell: stop 5% of ATR, exit at the close, about 0.3R per trade (Fig. 7, p. 13-14)
	- Stops of 25% of ATR or wider: about 0.15R or below in most cells (Fig. 7, p. 14)
	- Best cell over the full period: total return 9,350%, alpha 93% a year (p. 13)

### Limits
- **Zarattini 2023**
	- Best cell sits at the edge of the grid and was chosen on the full sample
	- At about $25 a share and a 14-day ATR near $1.60, a 5% ATR stop is $0.08 wide; with a large account it "will likely be exceeded" (p. 14)

## Sources

- [[2023 - Zarattini Aziz - Can Day Trading Really Be Profitable (ORB Strategy)]] (Zarattini 2023)
