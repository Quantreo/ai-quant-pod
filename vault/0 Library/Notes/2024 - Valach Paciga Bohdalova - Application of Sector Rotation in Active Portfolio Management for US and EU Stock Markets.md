---
type: reading-note
source: paper
title: Application of Sector Rotation in Active Portfolio Management for US and EU Stock Markets
authors: Valach, Paciga, Bohdalova
affiliations: Comenius University Bratislava, Faculty of Management
year: 2024
venue: Conference paper, Innovations in Science and Education (Economics and Business), Prague Economic Papers series, p. 22-29
doi: 10.12955/peb.v4.389
pdf: "[[2024 - Valach Paciga Bohdalova - Application of Sector Rotation in Active Portfolio Management for US and EU Stock Markets.pdf]]"
version: published
tier: 1
read: full
tags: [trend, equities, monthly]
date: 2026-10-25
---

# Sector rotation on monetary policy and momentum (Valach, Paciga, Bohdalova 2024)

## Summary

- **Finding**: long-only, equal-weight top 3 momentum sector ETFs, taken from cyclical sectors when the central bank eases and defensive sectors when it tightens, March 2004 to March 2023. Europe beats STOXX 600 on some metrics; the US does not beat the S&P 500 overall.
- **Mechanism**: sectors do not perform alike across the cycle, so the basket follows the policy regime. Investor psychology is mentioned, not tested.
- **Where it works best**: tightening months. US 98 months: J1K12 0.79% a month, Sharpe 0.25, risk 3.20%, against S&P 0.74%, 0.21, 3.58% (Table 4). Europe, 50 tightening months: benchmark loses.
- **Weak spots**: in easing months no portfolio has lower risk than the benchmark, US or Europe. European tightening portfolios have Sharpe about 0 (Table 5). The US benchmark beats the portfolios overall (authors).
- **Main caveats**: transaction costs set to zero, no hold-out, best cell picked on the full sample, ETF price returns against a total-return US benchmark, short sample (authors).

Page numbers follow the journal pagination (22-29). Values marked ≈ are read from a chart. Sharpe ratios in the paper are monthly.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Not all sectors perform well at the same time, so the portfolio should rotate ahead of the best and worst sector | Cited from Erickson 2014, no test | p. 22 |
| 2 | Easing favours cyclical sectors, tightening favours defensive ones | Used as the design rule. Table 3: cyclical sectors have the highest average returns, defensive sectors the best Sharpe ratios (text, p. 27). No direct test of the link. | p. 23, 26-27 |
| 3 | Investors read easing as growth and tightening as decline | Stated as an interesting trend: yields fall after a tightening announcement and rise after easing. No data shown. | p. 26 |

**Caveats raised by the authors**
- Short historical period lowers explanatory power (p. 28).
- Sectors equally weighted, benchmarks cap-weighted; company size may have affected results (p. 28).
- Length of policy cycles could have influenced results; authors judge the effect minimal, no evidence (p. 28).

**Ruled out**: nothing.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 9 US sector ETFs (Select Sector SPDR): defensive Energy, Staples, Health Care, Utilities; cyclical Materials, Industrials, Discretionary, Financials, Technology. 10 European iShares STOXX Europe 600 ETFs: defensive Oil & Gas, Food & Beverage, Health Care, Utilities; cyclical Basic Resources, Industrial Goods, Travel & Leisure, Banks, Technology, Telecommunications. Split "based on GICS"; the rule behind it is not given. | p. 23, Table 3 |
| Period | March 2003 to March 2023 data. Portfolio tables March 2004 to March 2023. Start set by ETF creation dates. | p. 23, Tables 4-5 |
| Regime | Fed Funds Target Rate (US), ECB Refinancing Rate (Europe). Rate falling: easing, cyclical basket. Rate rising: tightening, defensive basket. | p. 23, Tables 1-2 |
| Signal | Return over the last J months, J in 1, 3, 6, 12. Rank sectors inside the basket of the current regime. | p. 23 |
| Entry | Buy the top 3 sectors of the basket, equal weight, long only. | p. 23-24 |
| Exit and horizon | Hold K months, K in 1, 3, 6, 12; then redo the ranking. 16 (J, K) portfolios per market. | p. 23-24 |
| Sizing | Equal weight, no leverage. Risk is the standard deviation of monthly returns. | p. 23 |
| Costs | Set to zero (tracking error, spread and commissions "complex"). | p. 24 |
| Data | Yahoo Finance, monthly close. | p. 23 |

**Rule**: r_t = (P_t - P_{t-1}) / P_{t-1} (Eq. 1, p. 23). At each rebalance, if the policy rate is in an easing period, rank the cyclical ETFs on the J-month cumulative return; if in a tightening period, rank the defensive ETFs. Hold the top 3, equal weight, for K months. The text says the portfolio is rebalanced "after J months" (p. 24) while K is the holding period; not reconciled. Cumulated returns use the arithmetic mean (p. 24).

**Data provenance**: ETF closing prices from Yahoo Finance, so price returns; the text does not say whether they are adjusted for dividends. Benchmarks: S&P 500 Total Return Index and STOXX Europe 600 EUR Price Index (p. 23). Not stated: how regime dates are assigned to months, and whether the regime is known when the trade is made.

## 3. Results

All results are real data, in-sample, gross (costs zero), no hold-out.

**Aggregate**
- US: the benchmark exceeds all portfolios in the authors' words (abstract, p. 28). Figure 1 (J12K1, best by monthly return): portfolio ends ≈520 to ≈570 against S&P ≈520, from 100 in 2004. It tracks below the S&P from about 2019.
- Europe: Figure 2 (J12K12): portfolio ends ≈310, STOXX 600 ≈190. Abstract says all metrics beat the benchmark; Table 5 does not support that for easing months.
- Whole-sample portfolio figures are not tabulated, only the two charts and the split by regime.

**By sub-group**
- US easing, 130 months (Table 4): portfolios 0.78% to 0.96% a month, risk 5.42% to 6.03%, Sharpe 0.13 to 0.17. S&P: 0.87%, 4.81%, 0.18. None has lower risk.
- US tightening, 98 months: portfolios 0.61% to 0.87%, risk 3.20% to 4.09%, Sharpe 0.18 to 0.25. S&P: 0.74%, 3.58%, 0.21. J1K12 lowest risk and highest Sharpe.
- Europe easing, 178 months (Table 5): portfolios 0.49% to 0.76%, risk 4.44% to 4.98%, Sharpe 0.10 to 0.17. STOXX: 0.57%, 4.01%, 0.14. None has lower risk.
- Europe tightening, 50 months: portfolios -0.29% to 0.14%, risk 3.76% to 4.30%, Sharpe -0.08 to 0.03. STOXX: -0.36%, 4.72%, -0.08. Lowest risk J1K3 (3.76%).
- Single sectors (Table 3): US Technology 1.10% a month, Sharpe 0.21; Financials 0.46%, 0.07. Europe Industrial Goods 0.82%; Banks 0.02%, Sharpe 0.00. US average sector 0.77% against Europe 0.54% (excluding the communication sector, p. 27).

**Horizon and parameters**
- No pattern is described. US tightening Sharpe ranges 0.18 to 0.25 across the 16 cells; Europe tightening mostly 0.00 to 0.03.
- Europe easing is highest at J12K3 and J12K12 (0.17).

**Over time**: Figures show regime bands only. No sub-period results, no drawdowns.

**Link to other strategies**: none.

**Inconsistencies in the source**
- Abstract: portfolios beat STOXX 600 "across all metrics". Table 5 and text p. 27-28: no portfolio has lower risk in easing months.
- Conclusion: US strategies worse in all metrics (p. 28). Table 4 tightening: several portfolios beat the S&P on Sharpe and risk.
- Text p. 27: Europe healthcare has the second highest risk, 7.16%. Table 3: Banks 7.16%, Health Care 3.56%.
- Text p. 26: "consumer materials" 0.91%. Table 3: Consumer Discretionary 0.91%.
- Conclusion: European average return 0.11% against US 0.8% (p. 28). Table 3 gives 0.54% (excluding telecom) and the STOXX index 0.47%; 0.11 is the STOXX Sharpe.
- Text p. 25: European rate peak 4.20% on 1 December 2009. Table 2: 4.20% is the end of tightening in 2008.
- Table titles: US 2000-2023, EU 2001-2023; text says 2003-2023.
- Sharpe ratio computes as mean over standard deviation with no risk-free rate (computed from Tables 3, 4, 5).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Yields fall after tightening announcements and rise after easing; psychological explanation | p. 26 |
| Mid and small caps may offer larger opportunities | p. 28 |
| Policy cycle length has minimal impact on results | p. 28 |
| Portfolio "buckled the trend" in tightening and outperformed during changes | p. 26 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Cross-sectional momentum]]: top 3 of a sector basket on past J-month return, long only, equal weight, held K months | technique | signal | Sectors peak at different times | p. 23-24 |
| 2 | [[Monetary policy sector rotation]]: cyclical basket in easing, defensive basket in tightening, from the direction of the policy rate | technique | signal | Sectors react differently across the cycle | p. 23 |
| 3 | [[Market state split]]: portfolio and benchmark statistics split by easing and tightening months | technique | evaluation | Not argued | p. 27-28 |

## 6. Regime observations

- Easing: 130 months US, 178 months Europe. Tightening: 98 and 50 (p. 27-28).
- Defensive rotation reduces risk against the benchmark in tightening months in both markets (Tables 4-5).
- The ECB stays in easing most of the period (p. 25).

## 7. Acknowledged limits

Short period; equal weights against cap weights; costs ignored; sectors limited to large-cap ETFs (p. 24, 28).

## 8. Not addressed

Transaction costs and slippage, drawdowns, significance tests, out-of-sample or hold-out, the choice of best (J, K) cell, regime timing at trade date, dividends in ETF returns, capacity, whole-sample table for the portfolios, comparison with an unconditioned sector momentum portfolio, comparison with a defensive-only or cyclical-only basket.
