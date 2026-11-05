---
type: technique
brick: exit
aliases: [R-multiple target, Target in multiples of R]
sources: 1
tested_on: [equities]
---

# Profit target in R multiples

> [!summary]
> Close the position when the gain reaches a chosen multiple of the initial risk R, otherwise hold until the close of the session.

## How it works

- **Trigger**: price reaches entry plus k times R, where R is the distance from entry to the initial stop; if neither target nor stop is hit, the position is closed at the end of the session
- **Link to entry**: R comes from the stop of the entry rule, so the target scales with the risk of each trade

## What the sources say

### Parameters
- **Zarattini 2023**
	- Target 10R, else liquidation at the close; no partial exit (p. 5, Table 1)
	- Grid on TQQQ: target from 1R to 10R, or close (p. 13)

### Why
- **Zarattini 2023**
	- Not argued for 10R (p. 5)

### Evidence
- **Zarattini 2023**: in-sample, net of commissions, zero slippage, 2016 to 2023
	- Gains capped at 10R, losses near -1R (p. 8)
	- On TQQQ the best cell of the stop x target grid exits at the close, about 0.3R per trade (Fig. 7, p. 13-14)

### Limits
- **Zarattini 2023**
	- Grid chosen on the full sample; best cell read in-sample (p. 13)
	- Parameters may be suboptimal (p. 13)

## Sources

- [[2023 - Zarattini Aziz - Can Day Trading Really Be Profitable (ORB Strategy)]] (Zarattini 2023)
