---
type: diagnostic
kind: performance
aliases: [R-multiple PnL, Average PnL per trade in R]
sources: 1
---

# PnL in R

> [!summary]
> Does the edge come from a few large winners against small capped losers, or from a high win rate?

## How it works

- **How**: express each trade's PnL as a multiple of its initial risk R (entry to stop); report the average PnL per trade, the average gain, the average loss and the win rate, all in R
- **Reading**: a low win rate with an average gain well above the average loss is a payoff-asymmetry profile; the average PnL per trade in R is the expectancy
- **Data needed**: the trade list with entry price, initial stop, exit price and size

## What the sources say

### Parameters
- **Zarattini 2023**
	- R is the distance from entry to the opposite extreme of the first 5-minute candle (p. 5)

### Why
- **Zarattini 2023**
	- Low win rate offset by the gain/loss asymmetry (p. 8)

### Evidence
- **Zarattini 2023**: in-sample, net of commissions, zero slippage, 2016 to 2023
	- QQQ: win rate 24%, average 0.13R per trade, average gain about 2.8R, average loss about -0.7R (p. 8, Fig. 3)
	- TQQQ: average 0.18R per trade, average gain about 3.8R, average loss about -1.0R (p. 12, Fig. 6)

### Limits
- **Zarattini 2023**
	- None stated
	- Many QQQ trades are below full size because of the leverage cap (p. 8, footnote 3)

## Sources

- [[2023 - Zarattini Aziz - Can Day Trading Really Be Profitable (ORB Strategy)]] (Zarattini 2023)
