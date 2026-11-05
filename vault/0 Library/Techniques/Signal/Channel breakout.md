---
type: technique
brick: signal
aliases: [Channel breakout rule, Trading channel breakout, CB1, CB2, Support-resistance breakout]
sources: 3
tested_on: [crypto, fx, equities]
---

# Channel breakout

> [!summary]
> Goes long when the price breaks above a narrow recent trading range and short when it breaks below it.

## How it works

- **Inputs**: closing prices over a past window.
- **Formula**: a channel exists when the high of the last j periods is within c% of the low; the upper bound is c% above the low, the lower bound c% below the high. Enter when the price moves x% beyond a bound and stays there d periods.
- **Variant**: simple n-day high-low breakout with a small inaction band x, no channel condition (FX).
- **Lookback / holding**: window j; hold until the opposite signal, or a fixed k periods then flat.
- **Output**: +1, -1 or 0.
- **Direction**: long and short, in the direction of the break.
- **Tested on**: cryptocurrencies.
- **Variant**: support-resistance rule: break of the highest or lowest close of the last j periods, without the channel condition.

## What the sources say

### Parameters
- **Hudson 2019**
	- x in {0, 0.01, 0.05, 0.1, 0.5, 1, 5}%, d in {2, 3, 4, 5}, j from 2 to 200 days, c from 0.01 to 0.5, k in {3, 5} (Appendix, p. 217-218)
	- 4,536 channel rules; best in-sample CB2 25/0.05/0.025/5 for Bitcoin and Litecoin (Appendix; Table 9)
	- Daily, 2010-2017 (Bitcoin) to 2015-2017 (Ethereum) (p. 195-196)
- **Ivanova 2014**
	- Long if the rate is at least the maximum of the previous n closes times (1+x), short if at most the minimum times (1-x); n in {5, 10, 20}, x = 0.001 (p. 5, Eq. 2)
	- 21 USD rates and 19 cross rates, daily, 1973-2012 (Table 1)
- **Unknown 2026**
	- 52-week breakout (C6): close above the highest price of the previous 252 days, long only, used as an eligibility filter (Table 1 A)
	- 3,215 US ETFs, weekly, 2001-2026 (p. 6)

### Why
- **Hudson 2019**: a breach of drifting support and resistance signals sustained movement in the same direction (Appendix, p. 217)
- **Ivanova 2014**: studied in the literature, for example Taylor (1994) (p. 4)
- **Unknown 2026**: part of the canonical technical momentum combination with the golden cross (p. 15)

### Evidence
- **Hudson 2019**: real data, in-sample, gross unless noted
	- Average annualised return 7.89% (Bitstamp) to 15.99% (Ethereum) (Table 2)
	- Mean breakeven cost 30.42 to 144.03 bps (Table 6)
	- Out of sample H1 2018, best rule: annualised return as printed, CoinDesk -0.0010, Bitstamp -0.0091, Litecoin 0.0775 (Table 9)
	- Support-resistance variant: 1.96% to 4.73% a year, breakeven 7.88 to 16.16 bps (Tables 2, 6)
- **Ivanova 2014**: real data, inside a dynamic rule selection
	- Channel rules are the most used group in the top portfolio over the whole sample (p. 11, Fig. 2)
	- Most used pair of the top portfolio: CLP channel(20), 14.7% of the time (Table 2)
- **Unknown 2026**: real data, in-sample, net of 20 bp per side, no SL or TP
	- C6 alone: Sharpe 0.881, drawdown -13.81%, identical to four other trend filters (Table 2 A)
	- C2 and C6 together: same 0.881 (Table 2 B)

### Limits
- **Hudson 2019**
	- Profit comes from buy signals; sell signals near zero (Table 2)
	- Out of sample is six months, one rule per coin (p. 212-213)
	- No net returns at a fixed cost (p. 205)
- **Ivanova 2014**
	- Channel rules lose ground to momentum and moving average rules after 1985 (p. 11)
	- No result for channel rules alone (p. 11)
- **Unknown 2026**
	- Adds nothing over the golden cross alone in these data (Table 2)
	- No channel condition, no short side (Table 1)

## Sources

- [[2019 - Hudson Urquhart - Technical trading and cryptocurrencies]] (Hudson 2019)
- [[2014 - Ivanova Neely Weller et al - Can risk explain the profitability of technical trading in currency markets]] (Ivanova 2014)
- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
