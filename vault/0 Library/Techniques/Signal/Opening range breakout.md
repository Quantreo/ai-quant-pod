---
type: technique
brick: signal
aliases: [ORB, First-candle breakout]
sources: 1
tested_on: [equities]
---

# Opening range breakout

> [!summary]
> Trade the direction of the first candle of the session, with a stop at the opposite extreme of that candle.

## How it works

- **Inputs**: open, high, low and close of the first n-minute candle of the day
- **Formula**: long if the first candle closes up, short if it closes down, nothing if open equals close; enter at the open of the next candle; stop at the opposite extreme of the first candle, which defines R
- **Lookback / holding**: one session; out at the stop, the target or the close
- **Output**: direction (+1, -1, 0) and a stop level, once a day
- **Direction**: long and short
- **Tested on**: a US equity index ETF, intraday

## What the sources say

### Parameters
- **Zarattini 2023**
	- First candle of 5 minutes, entry at the open of the second (p. 4-5)
	- Target 10R, else exit at the close; no partial exit (Table 1)

### Why
- **Zarattini 2023**
	- Simplified version of the n-minute ORB (p. 3)
	- Traders use it "to capitalize on the volatility that can occur at the beginning of the trading day" (p. 3)
	- No claim on who pays or why the edge exists

### Evidence
- **Zarattini 2023**: QQQ, 2016 to 2023, in-sample, net of commissions, zero slippage
	- Total return 676% vs 169% buy and hold; Sharpe 1.13 vs 0.73 (Table 2)
	- Win rate 24%, average 0.13R per trade (p. 8)
	- Curve flat from early 2017 to mid-2018 and from late 2018 to early 2020 (≈ Fig. 2)

### Limits
- **Zarattini 2023**
	- One instrument, 7 years, no out-of-sample test
	- Zero slippage assumed (p. 13-14)
	- No results by side, year or regime

## Sources

- [[2023 - Zarattini Aziz - Can Day Trading Really Be Profitable (ORB Strategy)]] (Zarattini 2023)
