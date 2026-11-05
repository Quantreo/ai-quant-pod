---
type: reading-note
source: paper
title: A tug of war, overnight versus intraday expected returns
authors: Lou, Polk, Skouras
affiliations: Lou and Polk (London School of Economics, CEPR), Skouras (Athens University of Economics and Business)
year: 2019
venue: JFE 134, 192-213
doi: 10.1016/j.jfineco.2019.03.011
pdf: "[[2019 - Lou Polk Skouras - A Tug of War Overnight vs Intraday Returns.pdf]]"
version: published
tier: 1
read: full
tags: [seasonality-flows, equities, monthly]
date: 2026-10-21
---

# Tug of war, overnight vs intraday (Lou, Polk, Skouras 2019)

## Summary

- **Finding**: past overnight (intraday) returns predict future overnight (intraday) returns and the opposite in the other period. Momentum and short-term reversal profits are overnight; nine other anomalies earn intraday.
- **Mechanism (authors)**: clienteles trade persistently near the open or later in the day; price pressure reverses when the other clientele trades. Institutions trade intraday against momentum. A conjecture, only partly tested.
- **Where it works best**: US stocks 1993-2013. Overnight winners minus losers: 3.47% a month overnight (t = 16.83). Momentum overnight CAPM alpha 0.98% (t = 3.84), Sharpe 0.77 against 0.31 close to close.
- **Weak spots**: size is not significant in either period at 5%. Momentum is mostly intraday outside the US full sample and in 1927-1962. TugOfWar forecasts: 5 of 11 not significant.
- **Main caveats**: gross of costs, which the authors expect to cut profits much. Open price is a 30-minute VWAP. Several robustness claims and appendix tables are not in the PDF.

Page numbers follow the journal pagination (192-213; PDF page = printed page minus 191). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Some investors trade near the open, others later. Their persistent order flow gives continuation in the same period. Non-informative price pressure then reverses in the other period. | Table 1; t-statistics stay significant up to five years of lag (Fig. 2); same in nine non-US markets (appendix table, not in PDF). | p. 193, 197 |
| 2 | Institutions trade intraday, individuals near the open. | Institutional ownership rises more with intraday than overnight returns (Table 6); trade size by half hour (Fig. 3, 1993-2000, "speculative but suggestive"). | p. 194, 206-208 |
| 3 | Institutions as a class trade against momentum. | Value-weighted coefficient -0.260 (s.e. 0.119); none when equal-weighted (Table 7A). | p. 206-208 |
| 4 | The momentum tug of war is larger when institutions trade more against momentum (low comomentum, high active weight). | Tables 7B-C, 8. | p. 208-211 |
| 5 | A larger overnight-intraday gap means more unexploited anomaly return, so it forecasts higher strategy returns. | Limits-to-arbitrage model (proof in Internet Appendix, not in PDF); Table 5. | p. 193, 204 |
| 6 | Intraday anomalies have an opposite overnight premium: the riskier side earns a positive premium overnight. | Table 2. Tests cannot link this to a formal risk model. | p. 193-194 |

**Caveats raised by the authors**
- Fundamental drivers of the clienteles are not observed (p. 193).
- Trade size stopped identifying institutions after 2000, as they began splitting orders (p. 206, fn 18).
- Institutional trading can both drive and follow returns; three arguments against reverse causality are given (p. 207).
- Costs will make the strategies "much less attractive" (p. 193).
- Pre-1962 open prices are not traded prices (p. 211).

**Ruled out**
- Bid-ask bounce: overnight sort gives 3-factor alphas of 1.88% (t = 8.75) overnight and -1.43% (t = -7.05) intraday with the quote midpoint as open. Untabulated (p. 197).
- Simple aggregation of an earlier paper's half-hour effect: past overnight and intraday components both stay significant with that control in Table 4 (p. 198).
- Macro news (FOMC days) and firm news: no clear overnight or intraday pattern. Appendix Table A6, not in PDF (p. 204-205).
- Dividend months: results "nearly identical" without them (fn 9).

## 2. Strategy, brick by brick

A decomposition study, not a trading rule. The long-short portfolios below are its test portfolios.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | US CRSP-Compustat stocks, excluding price below $5 and the bottom NYSE size quintile. | p. 194-195 |
| Period | 1993-2013 (limited by TAQ). Time-series momentum: 22 equity index futures, 1996-2016. | p. 194, 201 |
| Signal | Past one-month overnight or intraday return, in deciles. Also 14 known characteristics. | p. 195-197 |
| Entry | Long top decile, short bottom decile, value-weighted, NYSE breakpoints. | p. 195 |
| Horizon | Hold one month, rebalance monthly. Lag from ranking to holding tested from 1 to 60 months. | p. 197, Fig. 2 |
| Open price | VWAP of 9:30-10:00 from TAQ; observations with under 1,000 shares excluded. | p. 194 |
| Costs | None. Gross. | p. 193 |
| Evaluation | Excess return, CAPM and 3-factor alpha; t-statistics with 12 lags; Fama-MacBeth WLS. | Tables 1, 2, 4 |

**Rule**

$$r^i_{intraday,s} = \frac{P^i_{close,s}}{P^i_{open,s}} - 1, \qquad r^i_{overnight,s} = \frac{1 + r^i_{close\text{-}to\text{-}close,s}}{1 + r^i_{intraday,s}} - 1$$

Daily components are compounded within the month, so overnight and intraday multiply to the monthly return for a stock. For portfolios there is a small interaction term (p. 195).

TugOfWar (Eq. 1, p. 204), with EWMA half-life 60 months: overnight EWMA minus intraday EWMA for overnight strategies, the reverse for intraday strategies. Regression: $r^s_{t+1} = \beta \, TugOfWar^s_t + \varepsilon^s_{t+1}$, expected β > 0. Controls: EWMA of past strategy return and volatility, 12-month market return and volatility, characteristic spread, short interest difference.

**Data provenance**
- Stocks: CRSP-Compustat; open prices from TAQ (p. 194).
- Ownership: Thomson Financial 13F quarterly; daily flows inferred from large TAQ trades (p. 194, 207).
- Non-US stocks and futures: Thomson Reuters Tick History. Non-US returns from Datastream, whose open prices "can be quite misleading" (p. 211, fn 22).
- Futures: front contract; "open" is the busiest minute before noon, "close" the busiest after noon (Table 3).
- 1927-1962 opens: CRSP, sourced from the Wall Street Journal (p. 211).

## 3. Results

Real data, in-sample, gross of costs, US 1993-2013 unless stated.

**Aggregate** (Table 1, p. 197). Monthly, decile 10 minus decile 1.

| Sort on | Overnight excess / 3-factor | Intraday excess / 3-factor |
| --- | --- | --- |
| Past overnight | 3.47% (t 16.57) / 3.47% (16.83) | -3.24% (-9.34) / -3.02% (-9.74) |
| Past intraday | -1.81% (-8.44) / -1.77% (-7.89) | 2.19% (6.72) / 2.41% (7.70) |

- Lag up to 60 months: joint t-statistics "well over 20" (p. 193).
- Market (CRSP value-weight): 0.55% overnight (t 3.62), 0.38% intraday (t 1.87). The market is open about 27% of the 24 hours and earns roughly 40% of the premium (p. 198, Table 2).
- Fama-MacBeth, all components together (Table 4, p. 202): next-month overnight on ewma_night 16.836 (s.e. 2.804), intraday on ewma_night -21.685; ewma_day: overnight -15.564, intraday 13.583. Close-to-close coefficients on all four are not significant except ret_day (-2.959).
- TugOfWar (Table 5, p. 206): coefficient positive in 10 of 11 strategies, significant in six (MOM 1.967, ROE 1.100, IVOL 1.207, ISSUE 2.277, TURNOVER 2.098, STR 1.402). Joint test rejects zero (p < 0.01). One standard deviation forecasts +1.01% close to close the next month, about 18% of its monthly volatility (p. 204).

**By sub-group** (Table 2, p. 200, CAPM alpha per month, long-short, overnight / intraday)

| Group | Strategies | Result |
| --- | --- | --- |
| Overnight only | MOM 0.98% / -0.02%; SUE 0.56% / 0.21%; INDMOM 1.07% / -0.63%; STR 0.93% / -1.05% | Intraday not significant, except INDMOM and STR (negative) |
| Intraday only | ROE -0.95% / 1.42%; INV -0.28% / 0.97%; BETA -0.49% / 0.70%; IVOL -1.46% / 2.48%; ISSUE -0.52% / 1.13%; ACCRUALS -0.47% / 1.10%; TURNOVER -0.29% / 0.57% | Overnight premium of opposite sign, all significant at 5% |
| Size, value | ME 0.11% / 0.43% (t 1.85); BM -0.10% / 0.48% (t 2.21) | Size is not significant in either period |

- Time-series momentum (Table 3, p. 201): overnight 1.40% CAPM alpha (t 3.24), intraday -0.10% (t -0.24). Raw close to close 0.81% is not significant (t 1.39).
- MOM overnight: standard deviation 4.02% against 7.85% close to close; Sharpe 0.77 against 0.31 (p. 199).
- Momentum by comomentum tercile, overnight, year 1 / year 2 (Table 7B): low 1.20% / 0.86%; high 0.17% / -1.28%. Intraday: low -0.90% / -0.70%; high -0.18% / 0.41% (7C).
- Momentum by institutional active weight, overnight (Table 8B): top minus bottom quintile 1.15% (t 5.39); intraday -0.76% (t -2.70).

**Horizon and parameters**
- Fig. 2 (≈): lag-1 t-statistics near 17 (overnight to overnight), 7 (intraday to intraday), -9 and -8 (cross-period). Overnight to overnight stays highest but dips toward 2 mid-range. Intraday to intraday hovers around +2, intraday to overnight stays mostly below -2, overnight to intraday drifts toward -2 and is ≈ 0 at lag 60.
- Fig. 1: first half hour holds 14.25% of daily dollar volume, last ≈ 13%.

**Over time**
- Not shown by sub-period inside 1993-2013. Other samples:
- Non-US, nine markets: overnight sort 2.31% (t 6.90), intraday sort 2.80% (t 6.23), reversal in every country; no close-to-close short-term reversal (p. 198).
- Non-US momentum, value-weight: full sample 1.28% (t 2.55), of which intraday 0.96% and overnight 0.23% (t 0.58). Large caps: 1.24%, intraday 0.44%, overnight 0.80% (t 2.50) (p. 211).
- US 1927-1962 momentum 3-factor alpha 1.45% (t 4.43): intraday 1.03%, overnight 0.21% (t 0.97). Large caps: overnight 0.34% (t 2.05) (p. 212).
- Negative skewness of momentum: overnight -1.08, intraday -1.53 (fn 12); time-series momentum intraday -2.77 (Table 3).

**Link to other strategies**: controls for an earlier paper's half-hour intraday momentum (Table 4); comomentum comes from an earlier paper by two of the authors (p. 207).

**Inconsistencies in the source**
- Table 2 caption says CAPM alphas. The text calls the INV overnight (-0.28%) and STR overnight (0.93%) figures three-factor alphas (p. 203). Table 2 values used.
- Text calls the year-1 comomentum differences significant; their t-statistics are -1.82 and 1.68 (p. 207, Table 7), below the 1.96 of the other results.
- Text says all four Table 1 strategies are significant up to five years (p. 197); Fig. 2 shows several lags near or inside ±2.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results robust to other open and close definitions and to excluding small caps ("available upon request") | fn 2, 8 |
| Patterns are neither a statistical fluke nor microstructure | p. 193 |
| Results robust to other holding periods for momentum, to other half-lives | fn 11, 16 |
| Equity premium of the top 1% NYSE stocks is nearly all overnight (appendix figure, not in PDF) | p. 198 |
| Size effect in momentum spread stronger for large stocks (appendix table, not in PDF) | p. 211 |
| High-frequency strategies "may be profitable after transaction costs", "particularly likely" for trend following on liquid equity index futures | p. 212 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Split return into overnight and intraday parts, compounded to the close-to-close return. Card: [[Overnight and intraday return split]] | technique | evaluation | Shows when expected returns accrue | p. 195 |
| 2 | Open price as VWAP of the first 30 minutes, minimum 1,000 shares | technique | entry | Robust open price | p. 194 |
| 3 | Exclude price under $5 and bottom NYSE size quintile. Card: [[Minimum price and size filter]] | technique | universe | Microstructure issues | p. 195 |
| 4 | Sort on the overnight or intraday part of past return. Card: [[Overnight and intraday return momentum]] | technique | signal | Tests clientele persistence | p. 196 |
| 5 | EWMA of components, half-life 60 months, skip last month. Variant in [[Overnight and intraday return momentum]] | technique | signal | Not a repackaging of the one-month result | p. 197 |
| 6 | Signed EWMA gap as strategy timing variable | technique | signal | Limits-to-arbitrage model | p. 204 |
| 7 | Scale overnight and intraday coefficients by 24/17.5 and 24/6.5 | technique | evaluation | Tests proportionality to clock time | Table 4 |
| 8 | Infer institutional trades from trade size ($50,000 or more) until 2000 | technique | economic intuition | Large orders linked to institutions | p. 206 |
| 9 | Condition momentum on comomentum and institutional active weight. Card: [[Momentum crowding filter]] | technique | economic intuition | Proxies for momentum crowding and rebalancing | p. 207-210 |
| 10 | Execute at the open or the close depending on the strategy | technique | entry | Premium accrues in one period (suggested, not tested) | p. 212 |

## 6. Regime observations

- Overnight momentum turns negative when comomentum is high (Table 7B).
- Negative skewness of momentum sits in the intraday leg (fn 12, Table 3).

## 7. Acknowledged limits

- No formal risk model for the overnight premia (p. 194).
- Futures sample covers equity indexes only (p. 201).

## 8. Not addressed

- Costs, turnover, capacity, slippage at the open VWAP window.
- Drawdowns and net Sharpe ratios of the decile portfolios.
- Out-of-sample test of TugOfWar (the regressions are in-sample).
- Why Table 5 covers 11 of the 14 strategies.
- Stock data after 2013; asset classes other than equities.
- Sub-period stability within 1993-2013.
