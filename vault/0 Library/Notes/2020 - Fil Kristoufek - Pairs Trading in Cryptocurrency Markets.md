---
type: reading-note
source: paper
title: Pairs Trading in Cryptocurrency Markets
authors: Fil, Kristoufek
affiliations: Institute of Economic Studies, Faculty of Social Sciences, Charles University, Prague
year: 2020
venue: IEEE Access, vol. 8, pp. 172644-172651
doi: 10.1109/ACCESS.2020.3024619
pdf: "[[2020 - Fil Kristoufek - Pairs Trading in Cryptocurrency Markets.pdf]]"
version: published
tier: 1
read: full
tags: [reversal, crypto, daily]
date: 2026-10-24
---

# Pairs trading in crypto (Fil, Kristoufek 2020)

## Summary

- **Finding**: on 26 Binance coins, 2018-2019, daily pairs trading earns -0.07% a month (distance) and 1.36% (cointegration). At 5-minute frequency distance earns 11.61% a month (Table 2). Net of 30 bps per trade.
- **Mechanism**: pairs trading is a mean reversion that exploits short-run spread divergence. Intraday profit is read as inefficiency of high-frequency crypto prices, not tested further.
- **Where it works best**: 5-minute and hourly data. Hourly distance 3.10% a month, 5-minute 11.61%. Cointegration is the steadier method at daily frequency (Table 2).
- **Weak spots**: daily distance method loses money. Stop-losses hurt at most settings. Randomly formed pairs earn 6.54% at 5 minutes, so intraday profit is not specific to pair selection (Table 2).
- **Main caveats**: short-selling costs excluded and shorting is barely possible for these coins. Thresholds tuned on the test data. Authors doubt intraday gains are tradable.

Page numbers follow the journal pagination (172644-172651). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Pairs trading profits come from short-run deviations of a pair from its long-run relation, reverting later | Background only. Literature cited: short-term Law of One Price violations, limits to arbitrage. Not tested here. | p. 172644-172645 |
| 2 | High-frequency crypto prices show simple mean reversion that daily prices do not | Random pairs earn 1.97% (hourly) and 6.54% (5-minute) a month, against -0.59% daily. | Table 2; p. 172649 |
| 3 | The daily market is efficient enough for the opportunity to be gone by the time a daily strategy trades | Distance profit grows with frequency. Execution lag matters about as much as costs. | Table 3; p. 172648-172649 |

**Caveats raised by the authors**
- Higher-frequency gains may not convert to real performance under liquidity limits (p. 172649).
- Dynamics in the test period are "likely largely different" from the formation period (p. 172649).
- Parameters taken from the literature are probably suboptimal. The 2 SD trigger looks like a local minimum (p. 172648).

**Ruled out**
- Daily crypto predictability as a general fact: the evidence "suggests otherwise, at least for daily sampling frequency" (p. 172649).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 26 Binance coins. Start: 181 coins. Keep coins traded from Jan 2018 to Sept 2019 (balanced panel), then the top 30% by volume. Bitcoin is the numeraire. | p. 172646 |
| Period | January 2018 to September 2019 | p. 172646 |
| Signal | Pair formation by distance method (top 20 pairs by SSD of normalised log prices, Eq. 1) or cointegration method (Engle-Granger test). | p. 172646-172647 |
| Entry | Short the spread when its normalised value exceeds 2, long below -2. Threshold 2 SD. | p. 172646, Table 1 |
| Exit | Close when the spread crosses zero, or at the end of the trading period. | p. 172646 |
| Horizon | Formation / trading windows: daily 4 months / 2 months; hourly 20 days / 10 days; 5-minute 6 days / 3 days. Average position 1.4 to 35 days. | Tables 1, 2 |
| Sizing | Not stated by the authors. Positions are on margin; PnL can exceed 100% in a period. | p. 172648 |
| Portfolio | Up to 20 pairs per window. | p. 172646 |
| Rebalancing | New formation window every "jump": 1 month (daily), 10 days (hourly), 3 days (5-minute). | Table 1 |
| Costs | 30 bps per trade: commission 10 bps plus market impact 20 bps (computed from Table 1 and p. 172647). Short-selling costs excluded. One-period execution lag. | p. 172647, Table 1 |
| Data and tools | Binance public API, daily, hourly and 5-minute bars. | p. 172646 |

**Rule** (Eq. 1-2, p. 172646): SSD(i,j) = sum over t of (P_it - P_jt)^2 on normalised log prices. Keep the 20 pairs with the lowest SSD. Spread = P_i - P_j. Trade at ±2 normalised standard deviations, close at zero.

**Data provenance**
- Binance has no fiat or stablecoin pairs at the time, so prices are in Bitcoin (p. 172646).
- The Bitcoin benchmark uses BTCUSDT as a proxy for the USD price (p. 172647).
- The unit of the monthly profit (BTC or USD) is not stated.

## 3. Results

All results are real data, in-sample, net of the 30 bps cost and one-period lag, unless noted. Parameters come from the literature, but the threshold and stop-loss were then compared by grid search on the same data (Table 4).

**Aggregate** (Table 2, monthly profit, annualised Sharpe)

| Frequency | Distance | Cointegration | Random pairs | Market (BTC) |
| --- | --- | --- | --- | --- |
| Daily | -0.07%, 0.034 | 1.36%, 1.1 | -0.59%, -0.62 | 0.43%, 0.19 |
| Hourly | 3.10%, 4.1 | 1.11%, 0.66 | 1.97%, 2.4 | |
| 5-minute | 11.61%, 22 | 4.16%, 12 | 6.54%, 12 | |

Maximum drawdown: daily distance 26.32%, cointegration 24.89%, BTC 67.44% (Table 2).

**By sub-group**
- Share of round-trip trades (daily distance): 23.65%; winning trades 46.06% (Table 2).
- Cointegrated pairs found: 22.2 (daily), 26.1 (hourly), 36.3 (5-minute) (Table 2).
- By coin or by pair: Not addressed.

**Horizon and parameters**
- Without execution lag (Table 3): daily 0.38% (distance), 1.53% (cointegration); hourly 5.97% and 4.17%; 5-minute 16.80% and 7.43%.
- Without costs (Table 3): daily 0.26% and 1.70%; hourly 5.60% and 4.06%; 5-minute 22.87% and 17.00%.
- Stop-loss and threshold grid, daily (Table 4): distance at 2 SD is negative for every stop-loss shown (-1.84% to -0.61%). Distance at 1 SD with the widest stop (6) earns 1.19%. Cointegration at 2 SD with stop 6 earns 1.89%, Sharpe 1.7.

**Over time**
- Daily, over the period (≈ Fig. 1): both pair methods and the market are close in the 2018 bear market. Cointegration then rises after spring 2019. It ends with 17.56% a year of excess return over the market's 5.25% a year. Distance ends at -1.33% a year (p. 172649).
- The daily series drops every second backtest to avoid overlap, so figures differ slightly from Table 2 (fn 3, p. 172648).

**Link to other strategies**
- Buy and hold Bitcoin: Sharpe 0.19, maximum drawdown 67.44% (p. 172649).
- Random pairs as the baseline of Gatev et al. (p. 172647).
- Return distributions (Table 5): mean significant only at 5 minutes (t = 3.5 distance, 2.8 cointegration). Kurtosis 33.8 to 619.

**Inconsistencies in the source**
- p. 172649 says random pairs beat cointegration in risk-adjusted return at hourly and 5-minute frequency. Table 2 shows Sharpe 12 for both at 5 minutes.
- p. 172648 says a stop-loss is "extremely harmful" and underperforms the base scenarios. Table 4 shows stop 6 above the base: cointegration 1.89% against 1.36%, distance (1 SD) 1.19% against -0.07% at 2 SD.
- p. 172648 puts daily profit "at roughly 0.5% monthly" without lag or costs. Table 3 gives 0.26% to 0.38% for distance and 1.53% to 1.70% for cointegration.
- The abstract says the strategies "underperform classical benchmarks". Figure 1 and p. 172649 show daily cointegration beating buy and hold. The benchmark is the equity pairs literature, not Bitcoin.
- Table 4 gives no unit for the stop-loss column (2 to 6).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Spuriously cointegrated pairs explain why stop-losses hurt | p. 172648 |
| Higher frequency could lift pairs trading in equities | p. 172649 |
| Short-selling is "literally impossible" for most of the coins | p. 172647 |
| Crypto efficiency is improving over time | p. 172646, citations only |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Pairs selection by distance (SSD of normalised log prices, top 20) | technique | signal | Follows Gatev; "most similar" price paths (p. 172646). Card [[Pairs trading spread signal]] | p. 172646 |
| 2 | Pairs selection by Engle-Granger cointegration, spread as regression residual | technique | signal | Follows Vidyamurthy. Card [[Pairs trading spread signal]] | p. 172646-172647 |
| 3 | Trade the spread at ±2 SD, close at zero | technique | entry | Taken from Gatev. Card [[Pairs trading spread signal]] | p. 172646 |
| 4 | Random pairs formed by bootstrap, same trading rule | technique | evaluation | Separates the value of pair selection from simple mean reversion. Card [[Random pairs placebo]] | p. 172647 |
| 5 | One-period execution lag | technique | entry | Approximates the bid-ask spread. Card [[Implementation lag test]] | p. 172647 |
| 6 | Top 30% volume filter and balanced panel | technique | universe | Limits liquidity problems. Card [[Minimum price and size filter]] | p. 172646 |
| 7 | Sliding-window formation and trading periods with a jump | technique | evaluation | Robustness. No card: standard practice | p. 172647 |
| 8 | Stop-loss in standard deviations, grid on threshold | technique | exit | Not argued. No card: grid search | Table 4 |

## 6. Regime observations

- Cointegration profit comes mostly after the spring 2019 bull market (≈ Fig. 1, p. 172649).
- The market benchmark's drawdown of 67.44% falls in the 2018 bear market (p. 172649).
- Literature cited: pairs trading does better in bear and illiquid markets. Not tested by the authors (p. 172645).

## 7. Acknowledged limits

- Sensitivity to parameters, costs and execution lag is large (p. 172648-172649).
- Gains at high frequency may not survive liquidity constraints (p. 172649).
- Short-selling is not modelled (p. 172647).

## 8. Not addressed

- Position sizing, leverage and margin.
- Results by coin or pair, and capacity.
- Borrowing cost for the short leg (excluded, Bitcoin rate 7.3% a year cited only).
- Out-of-sample test with parameters fixed in advance.
- Unit of profit (BTC or USD).
