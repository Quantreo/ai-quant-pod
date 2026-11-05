---
type: reading-note
source: paper
title: "Can Day Trading Really Be Profitable? Evidence of Sustainable Long-term Profits from Opening Range Breakout (ORB) Day Trading Strategy vs. Benchmark in the US Stock Market"
authors: Zarattini, Aziz
affiliations: Zarattini (Concretum Research), Aziz (Peak Capital Trading, Bear Bull Traders)
year: 2023
venue: not stated in the PDF
doi: not stated in the PDF
pdf: "[[2023 - Zarattini Aziz - Can Day Trading Really Be Profitable (ORB Strategy).pdf]]"
version: 2025-04-21 (first version 2023-04-24)
tier: 2
read: full
tags: [trend, equities, intraday]
date: 2026-10-21
---

# Opening Range Breakout on QQQ (Zarattini, Aziz 2023)

## Summary

- **Finding**: 5-minute opening-range breakout on QQQ, 2016-2023: +676% vs +169% buy and hold, Sharpe 1.13 vs 0.73, net of commissions, zero slippage. Alpha 33% a year.
- **Mechanism**: Not stated by the authors.
- **Where it works best**: on TQQQ, a 3x ETF that avoids the 4x leverage cap: +1,484%, Sharpe 1.19, drawdown 28%. Best grid cell: stop 5% of ATR, exit at close.
- **Weak spots**: 24% win rate; flat stretches in 2017-2018 and late 2018 to early 2020 (≈ Fig. 2); edge concentrated in the tightest stops (≈ Fig. 7).
- **Main caveats**: one instrument, 7 years, no out-of-sample. Zero slippage, which the authors say can make the best cell unrealistic. Grid chosen on the full sample. Several figures inconsistent.

Page numbers follow the PDF (1-18); the paper has no other pagination. Values marked ≈ are read from a chart. All results are real data (Interactive Brokers), in-sample, from a single backtest.

## 1. Mechanism (authors' claim)

Not stated by the authors. No claim on who pays or why the edge exists.

Only rationale given: traders use ORB "to capitalize on the volatility that can occur at the beginning of the trading day" (p. 3).

Beta near zero is attributed to the long/short balance (51% long, 49% short over 1,795 trades), not to an economic cause (p. 8).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | QQQ, "the most liquid instrument available that replicates the Nasdaq Index". Then TQQQ (3x daily QQQ). | p. 4, 10 |
| Period | 1 Jan 2016 to 17 Feb 2023. Shorter sample chosen "due to changes in market dynamics and liquidity". | p. 4, Table 1 |
| Signal | Direction of the first 5-minute candle. Long if up, short if down, nothing if doji (open = close). | p. 4-5 |
| Entry | Open of the second 5-minute candle. No slippage assumed. | p. 5, Table 1 |
| Exit | Stop at the low (long) or high (short) of the first candle; distance = R. Target 10R, else liquidated at the close. No partial exit. | p. 5, Table 1 |
| Sizing | Risk 1% of the account per trade, capped by 4x leverage. 1% chosen because "the historical average daily move on QQQ is 1%". | p. 5 |
| Costs | Commission $0.0005 per share. No slippage. Benchmark without commission. | p. 5-6 |
| Capital | $25,000 start. | Table 1 |
| Data and tools | "Aggregated data provided by Interactive Brokers"; MATLAB R2022. | p. 6 |

**Rule** (p. 5), with A the account, P the entry price, R = P - stop price:

$$\text{Shares} = \text{int}\left(\min\left(\frac{0.01 \cdot A}{R}, \frac{4 \cdot A}{P}\right)\right)$$

The authors say the parameters were deliberately not optimised (p. 5), then test a stop and target grid (p. 13).

**Data provenance**: one source named, no detail on bar construction, session hours or adjustments (p. 6).

## 3. Results

Net of commissions, zero slippage, 2016-2023, unless stated.

**Aggregate** (Table 2, p. 13)

| Strategy | Total return | Yearly return | Volatility | Sharpe | Max drawdown |
| --- | --- | --- | --- | --- | --- |
| ORB TQQQ | 1,484% | 48% | 39% | 1.19 | 28% |
| ORB QQQ | 676% | 33% | 29% | 1.13 | 22% |
| Buy and hold TQQQ | 438% | 27% | 69% | 0.69 | 82% |
| Buy and hold QQQ | 169% | 15% | 23% | 0.73 | 36% |

**By instrument**

| Metric | ORB QQQ | ORB TQQQ | Where |
| --- | --- | --- | --- |
| Alpha vs QQQ, daily regression | 33% a year, p = 0.0025 | 48% a year, p = 0.0013 | p. 7, 11 |
| Beta | "not statistically different from zero", no value | same | p. 7, 11 |
| Average PnL per trade | 0.13R | 0.18R | p. 8, 12 |
| Average gain / average loss | ≈2.8R / ≈-0.7R | ≈3.8R / ≈-1.0R | Fig. 3, 6 |
| Win rate | 24% | not given | p. 8 |
| Final value | $192,806 | not given | p. 6 |

- Trades: 1,795 on QQQ; 51% long, 49% short. No results split by side (p. 8).
- Losses capped near -1R, gains capped at 10R; many trades below full size because of the 4x cap (p. 8, footnote 3).
- Unconstrained-leverage QQQ version: +1,630%; 60% of trades ran at an exposure 40% below it (p. 10, Fig. 4). No other statistics for it.
- TQQQ: leverage cap binds on 10% of days, exposure cut by about 30% then (p. 12).

**Horizon and parameters** (TQQQ, Fig. 7, p. 13-14)
- Grid: stop 5% to 100% of 14-day ATR (11 values), target 1R to 10R or close.
- Best cell: stop 5% of ATR, exit at close, ≈0.3R per trade. It sits at the edge of the grid (smallest stop tested).
- Stops of 25% of ATR or wider: ≈0.15R or below in most cells.
- Best cell over the full period: +9,350%, alpha 93% a year net of commissions (p. 13). In-sample choice.
- Slippage warning: at about $25 per share and 14-day ATR about $1.60, a 5% ATR stop is $0.08 wide; with a large account the stop "will likely be exceeded" (p. 14).

**Over time** (≈ Fig. 2, 5, 8; equity axes are in dollars, log-spaced)
- ORB QQQ flat from ≈ early 2017 to mid-2018 and from ≈ late 2018 to early 2020 (Fig. 2).
- 2022: ORB QQQ ends the year above its start; buy and hold falls (Fig. 2).
- Best-cell version falls roughly 40% to 50% from its peak in the second half of 2022 (≈ Fig. 8).

**Link to other strategies**: only buy and hold QQQ and TQQQ, and the unconstrained version above.

**Inconsistencies in the source**
- ORB QQQ: $192,806 from $25,000 is +671%; text says 675% (p. 6, 14), Table 2 says 676%.
- ORB QQQ: Sharpe 1.12 and yearly return 31% in the text (p. 8) vs 1.13 and 33% in Table 2.
- ORB TQQQ: yearly return 46% in the text (p. 11) vs 48% in Table 2.
- Best cell: +9,350% from $25,000 is about $2.4M; text says $6,400,000 (p. 13); Fig. 8 ends above $3.2M.
- Unconstrained version: 1,630% is about 2.4x of 676%; text says "approximately 2x" (p. 10).
- Text points to Table 2 for model inputs (p. 5, captions); inputs are in Table 1.
- Fig. 8 bear shading starts ≈ mid-2022; in Fig. 2, 4, 5 it covers all of 2022.
- A paragraph on p. 9 is garbled (two sentences interleaved).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| A longer sample would have made the results more significant | p. 4 |
| QQQ chosen "without any loss of generality"; no other instrument tested | p. 1 |
| ORB "consistently profitable in both bull and bear markets"; charts only, no statistics by regime | p. 12 |
| Small share sizes on QQQ and TQQQ trade with "small to no slippage" | p. 14 |
| Main risk is operational (slippage, discipline), not strategy failure | p. 16 |
| Mixing low and high frequency should give better risk-adjusted returns | p. 16 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Opening range breakout]]: trade the direction of the first 5-minute candle, enter at the open of the second; skip dojis | technique | signal | Simplified version of the n-minute ORB | p. 3-5 |
| 2 | Stop at the opposite extreme of the opening candle, defining R ([[Opening range breakout]]) | technique | exit | Not argued | p. 5 |
| 3 | [[Profit target in R multiples]]: target in multiples of R, else exit at the close | technique | exit | Not argued for 10R | p. 5 |
| 4 | [[Fixed risk per trade]]: risk 1% of the account per trade, capped by maximum leverage | technique | sizing | 1% matches QQQ's average daily move | p. 5 |
| 5 | 3x leveraged ETF to bypass the broker's intraday leverage cap | technique | sizing | The cap left 60% of trades undersized | p. 10 |
| 6 | [[ATR-based stop]]: stop as a fraction of the 14-day ATR | technique | exit | "A better and more stable representation of the volatility" | p. 13 |
| 7 | [[PnL in R]] to show payoff asymmetry | technique | evaluation | Low win rate offset by gain/loss asymmetry | p. 8 |
| 8 | Daily regression on the benchmark for alpha and beta | technique | evaluation | Return in excess of market risk | p. 7 |
| 9 | Compare with an unconstrained-leverage version | technique | evaluation | Measures the cost of the cap | p. 9-10 |
| 10 | Stop x target grid, average PnL in R | technique | evaluation | Sensitivity to stop and target | p. 13 |
| 11 | "Cut losses quickly, let profits run" | principle | exit | Authors say the grid "empirically confirms" it | p. 13 |

No turnover-reduction technique.

## 6. Regime observations

- Authors cite 2018 "Volmageddon", the March 2020 COVID crash and the 2022 rate-hike bear market as a challenging period (p. 12).
- Flat stretches in 2017-2018 and 2019 while QQQ rose (≈ Fig. 2).
- Outperformance most visible in bear markets, when buy and hold falls (p. 12, Fig. 2).

## 7. Acknowledged limits

- Broker leverage cap limits the upside on QQQ (p. 8-10).
- Best-cell result "can under certain circumstances be considered unrealistic": zero slippage (p. 13-14).
- Leverage raises risk; execution errors matter (p. 16).
- Leveraged ETFs unsuited to buy and hold: daily rebalancing, "beta slippage" (Lewis 2021) (p. 10, footnote 4).
- Parameters not optimised, may be suboptimal (p. 5, 13).

## 8. Not addressed

- Slippage, including stop fills.
- Short borrow costs and margin interest.
- Results by side, by year, by regime.
- Out-of-sample test; adjustment for the grid search; confidence interval on the Sharpe ratio.
- Any instrument other than QQQ and TQQQ.
- Whether A is current equity or starting capital in the sizing rule.
- Data details: bar construction, session hours, adjustments.
- Capacity, beyond the slippage remark.
