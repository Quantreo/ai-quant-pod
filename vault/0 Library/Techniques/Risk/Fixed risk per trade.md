---
type: technique
brick: risk
aliases: [Risk 1% per trade, Fixed fractional risk]
sources: 1
tested_on: [equities]
---

# Fixed risk per trade

> [!summary]
> Size each trade so that hitting the stop loses a fixed fraction of the account, capped by a maximum leverage.

## How it works

- **What it limits**: the loss on one trade, as a share of the account
- **Trigger / level**: shares = min(risk fraction x account / R, max leverage x account / entry price), rounded down, where R is the distance from entry to stop
- **How the level is set**: the risk fraction is a chosen constant; R comes from the stop of the entry rule; the leverage cap comes from the broker

## What the sources say

### Parameters
- **Zarattini 2023**
	- Risk 1% of the account per trade, maximum leverage 4x (p. 5)
	- Not stated whether the account is current equity or starting capital

### Why
- **Zarattini 2023**
	- 1% chosen because "the historical average daily move on QQQ is 1%" (p. 5)

### Evidence
- **Zarattini 2023**: in-sample, net of commissions, zero slippage, 2016 to 2023
	- Losses stay near -1R (p. 8)
	- On QQQ, 60% of trades ran at an exposure 40% below the unconstrained version because of the cap (Fig. 4, p. 10)
	- Unconstrained-leverage QQQ version: total return 1,630% vs 676% (p. 10)
	- On TQQQ the cap binds on 10% of days, cutting exposure by about 30% (p. 12)

### Limits
- **Zarattini 2023**
	- The broker leverage cap limits the upside on QQQ (p. 8-10)
	- Leverage raises risk and execution errors matter (p. 16)

## Sources

- [[2023 - Zarattini Aziz - Can Day Trading Really Be Profitable (ORB Strategy)]] (Zarattini 2023)
