---
type: reading-note
source: paper
title: A Decade of Evidence of Trend Following Investing in Cryptocurrencies
authors: Rozario, Holt, West, Ng
affiliations: Rozario (University of Cambridge), West and Ng (Globe Research); no affiliation printed for Holt
year: 2020
venue: arXiv:2009.12155v1 [q-fin.ST], 25 Sep 2020
doi:
pdf: "[[2020 - Rozario Holt West et al - A Decade of Evidence of Trend Following Investing in Cryptocurrencies.pdf]]"
version: preprint (v1)
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-10-24
---

# Trend following in Bitcoin (Rozario, Holt, West, Ng 2020)

## Summary

- **Finding**: moving-average crossover rules on hourly BTCUSD, Sept 2011 to Dec 2019, give best in-sample Sharpe ratios of 1.09 (SMA), 1.35 (EMA), 1.32 (DEMA). Walk-forward SMA is reported at 255% a year (p. 1, 4).
- **Mechanism**: not stated by the authors. Crypto is compared to 20th century commodities, with no test.
- **Where it works best**: walk-forward test years 2012-2016 show Sharpe ratios of about 0.5 to 1.9 for SMA, EMA and DEMA (≈ Fig. 3a). Optimal windows are long, 150 to 1000 hours.
- **Weak spots**: 2017-2018 is negative for SMA (≈ -0.8) and EMA (≈ -0.55); DEMA is slightly negative in 2018-2019. The authors find no attractive 1-year-ahead Sharpe on the S&P 500.
- **Main caveats**: no costs, no slippage; parameters tuned on the same data; walk-forward parameters picked "without great care"; headline 255% does not match the 73700% total.

Page numbers follow the printed pagination of the preprint (1 to 8). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

Not stated by the authors. The paper gives analogies, not a mechanism.

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Crypto markets share features of 20th century commodity markets, so trend following fits | Analogy and citations only. No commodity data in the paper. | p. 1, 3 |
| 2 | Trend following diversifies equities | Small negative correlation of BTCUSD and S&P 500 returns, not significant, no figure given. 20-day rolling correlation of the two strategies ranges about -0.7 to 0.6. | p. 5, ≈ Fig. 4a |

**Caveats raised by the authors**
- Sample of rolling windows is very small and Bitcoin is young; retest when markets mature (p. 4-5).
- No data covering a prolonged recession (p. 6).
- The 1-year training slices show no predictable, attractive Sharpe ratio, to be retested with more data (p. 4).

**Ruled out**
- Profitable intraday trend following on BTCUSD spot: "notable absence" (p. 6).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | BTCUSD spot, Bitstamp. S&P 500 as a comparison (daily Yahoo! Finance data). | p. 2 |
| Period | 13 Sept 2011 to 12 Dec 2019. Hourly resample, 72,299 rows, 5,835 missing values filled forward. | p. 2 |
| Signal | Buy when the short moving average is above the long one, sell when below. SMA, EMA, DEMA. | p. 2-3 |
| Entry | On the crossover signal. "Maximal volume" bought or sold per signal, starting from 10,000 USD. | p. 2 |
| Exit | On the opposite crossover. Whether "sell" means short or flat: Not stated by the authors. | p. 2 |
| Horizon | Windows 1 to 1000 hours for BTCUSD, 1 to 50 days for the S&P 500. | p. 2 |
| Sizing | Maximal volume; no volatility scaling. | p. 2 |
| Portfolio | One asset. | p. 2 |
| Rebalancing | On each signal. | p. 2 |
| Costs | None: negligible fees, spread, slippage and impact assumed. Gross. | p. 2 |
| Data and tools | bitcoincharts.com, Yahoo! Finance. Code at the Globe-Research bittrends repository. | p. 1-2 |

**Rule** (Eq. 1-2, p. 3): SMA(n) is the mean of the last N prices. EMA uses α = 2/(N+1): EMA(n) = α·Y(n) + (1-α)·EMA(n-1). DEMA(n) = 2·EMA(n) - EMA(EMA)(n).

**Data provenance**
- The mean date of missing values is 14 March 2012; filling is said not to affect results because early data are "irrelevant" (p. 2).
- Missing share: 5,835 of 72,299 rows, about 8% (computed).

## 3. Results

**Aggregate** (Table 1, p. 5; best possible over the full period, so in-sample)

| Strategy | Short (hrs) | Long (hrs) | Sharpe | Sortino |
| --- | --- | --- | --- | --- |
| SMA | 141 | 781 | 1.0907 | 0.7969 |
| EMA | 721 | 951 | 1.3515 | 12.9827 |
| DEMA | 791 | 981 | 1.3165 | 2.2121 |

Walk-forward SMA, 2011 to 2019: total return 73700%, stated as 255% annualised (p. 4). Real data, parameters from the prior year, gross of costs.

**By sub-group**
- Per year, test Sharpe ratio, walk-forward (≈ Fig. 3a): SMA about 1.6 (2012-13) down to about -0.8 (2017-18), about 0.7 (2018-19). EMA about 0.4 or lower in 2013-14, about -0.55 in 2017-18. DEMA about 1.9 in 2014-15, about -0.15 in 2018-19.
- Best possible Sharpe per year, in-sample (≈ Fig. 3c): about 1.4 to 2.7 for SMA, all positive.
- S&P 500 test years (≈ Fig. 3b): mostly negative or near zero for the three rules.

**Horizon and parameters**
- Optimal short window mostly above 200 hours; long window 480 to 990 hours (≈ Fig. 3d, p. 5).
- For EMA and DEMA the long and short windows correlate above 0.65 (p. 5).
- Heat maps for 2019 (Fig. 2, 5, 6): Sharpe surface by short and long window. The S&P 500 maxima are called unstable (p. 4).

**Over time**
- Sharpe ratios "consistently around the 0.5 to 1.5 range (with only one year loss making)" for 10 and 40 day SMAs, with a slight drop in recent times (p. 6).
- Evidence by year: Fig. 3a above.

**Link to other strategies**
- S&P 500 correlation: not significant (p. 5-6).
- Commodity trend following: compared in words only (p. 1, 5).

**Inconsistencies in the source**
- 73700% in total is a factor of about 738. Over 7 to 8 years this compounds to about 130% to 160% a year (computed), not 255%. The method of annualising is not given.
- p. 4 finds "no predictable and attractive Sharpe ratios" from 1-year training slices. The conclusion (p. 5) says "consistent and attractive returns" and "consistently profitable regardless of averaging strategy".
- The conclusion says "only one year loss making". Fig. 3a shows three negative cells: SMA 2017-18, EMA 2017-18, DEMA 2018-19.
- The conclusion says 10 and 40 day SMAs perform well. Table 1 gives 141 and 781 hours (about 6 and 33 days).
- The abstract claims "strong bear market diversification". The paper has no prolonged bear market (p. 6) and the correlation is not significant.
- Table 1: EMA Sortino 12.98 against Sharpe 1.35; SMA Sortino 0.80 below its Sharpe. Not explained.
- Fig. 4 caption: rolling correlation of the two SMA strategy returns. Text p. 5: correlation of BTCUSD and equity returns.
- Fig. 3 caption says 2011 to 2020; data end Dec 2019.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Bottom-up AUM capacity of $323m | p. 1; no method given |
| Crypto risk-adjusted returns similar to commodities | Abstract, p. 5 |
| Results carry over to other cryptocurrencies | p. 5 |
| Missing early data do not affect results | p. 2 |
| Trend following is a diversifier against equities in recessions | Abstract, p. 6 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Short and long moving-average crossover (SMA, EMA, DEMA) | technique | signal | Standard trend estimation. Card [[Time-series momentum signal]] | p. 2-3 |
| 2 | Yearly walk-forward: next year's windows are last year's Sharpe-optimal windows | technique | calibration | Not argued; "without great care" (p. 3). No card: standard practice | p. 3 |
| 3 | Sharpe heat map over short and long window | technique | evaluation | Shows risk-adjusted surface. No card: a tool to pick the best cell | Fig. 2 |
| 4 | Rolling correlation with the S&P 500 | technique | evaluation | Diversification. No card: standard practice | p. 5 |

## 6. Regime observations

- Window length and performance: optimal windows large at hourly scale; small windows give no profit (p. 4, 6).
- 2017-2018 is weak for all three rules (≈ Fig. 3a).
- Pre-2016 EMA and DEMA often beat SMA (p. 4).

## 7. Acknowledged limits

- Very small sample of rolling windows; young market (p. 5).
- No recession in the data (p. 6).
- Walk-forward done without care for robustness of the parameters (p. 3).

## 8. Not addressed

- Transaction costs, funding, borrowing for shorts, exchange risk.
- Whether the strategy is long-flat or long-short; exposure and drawdown figures (noted but not printed, p. 2).
- Number of trades, turnover, holding period.
- Out-of-sample parameters fixed in advance.
- Other cryptocurrencies.
