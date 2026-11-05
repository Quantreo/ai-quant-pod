---
type: reading-note
source: paper
title: Currency Momentum Strategies
authors: Menkhoff, Sarno, Schmeling, Schrimpf
affiliations: Menkhoff and Schmeling (Leibniz Universität Hannover), Sarno (Cass Business School, Singapore Management University, CEPR), Schrimpf (Bank for International Settlements)
year: 2011
venue: BIS Working Papers No 366 (SSRN 1971680)
doi: not stated in the PDF
pdf: "[[2011 - Menkhoff Sarno Schmeling Schrimpf - Currency Momentum Strategies.pdf]]"
version: working paper, December 2011
tier: 1
read: full
tags: [trend, fx, monthly]
date: 2026-10-25
---

# Currency momentum strategies (Menkhoff, Sarno, Schmeling, Schrimpf 2011)

## Summary

- **Finding**: long past-winner, short past-loser currencies (six-portfolio sort, up to 48 currencies vs USD, 1976-2010) earns 9.46% a year at 1-month lookback and holding, Sharpe 0.95, gross. Net of full quoted spreads: 3.92%.
- **Mechanism (authors)**: under-reaction then over-reaction (returns peak 8 to 12 months after formation, then reverse), plus limits to arbitrage. Not explained by risk factors.
- **Where it works best**: 1-month lookback and holding; high idiosyncratic volatility and high country risk currencies; the period since 2001 (Sharpe 1.28 for f = 1). Almost uncorrelated with carry (0.04).
- **Weak spots**: 15 developed currencies only: 3.83% gross, 0.79% net (t = 0.44). 12-month holding is weak (f = 1: 5.75%, f = 12: 1.89%). Gross returns near zero after 2007 (≈ Fig. 7).
- **Main caveats**: quoted spreads are indicative and too high (authors); turnover 74% a month; only 16 currencies before 1983; no capacity or drawdown figures.

Page numbers follow the printed pagination of the working paper (text 1-42, tables and figures 49-68, appendix 70-86). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Under-reaction, then over-reaction to information | Cumulative post-formation return of the long-short portfolios rises for 8 to 12 months, then falls. f = 1: peak ≈4.5% near month 12, ≈1.3% at month 60. f = 12: peak ≈2.2% near month 8, ≈-5.3% at month 60. Same shape in spot changes. | Fig. 4, A.1; p. 25-26 |
| 2 | Limits to arbitrage: unstable profits, risky currencies | Returns vary over time (rolling 36-month, Fig. 7). Stronger in high idiosyncratic volatility, high country risk, high exchange-rate stability risk currencies. | Fig. 7, Table 11; p. 31-35 |
| 3 | Transaction costs explain part | Winners and losers have larger spreads than average; full spreads cut f = 1 from 9.46% to 3.92%. | Table 8, A.4; p. 27-29 |

The authors call the mechanism "consistent with" under- and over-reaction (p. 2, 26). They add that such irrationality should be arbitraged away in FX, hence the limits to arbitrage tests (p. 26).

**Caveats raised by the authors**
- Quoted bid-ask spreads are indicative and larger than effective spreads, so net results are a lower bound (p. 12, 27).
- Profits vary strongly over several years; short-horizon traders may not survive them (p. 31-32).
- Momentum sits in minor, costly, risky currencies; the conclusion links about half of the profit to them (p. 41).

**Ruled out**
- Business-cycle and macro factors, carry factor HML-FX, Fama-French factors and UMD: adjusted R² near zero, alphas large (Table 10, p. 29-31). One exception: global FX volatility for f = 12 (fn 23, p. 30).
- Carry: H-L correlation 0.04, 0.01, 0.07 (Table 5). Technical rules: largest R² 26% (Table 3).
- Capital controls, tradability, base currency, exchange-rate regimes, central bank intervention: do not remove the effect (Tables 12, 13, A.6, A.9, A.10; p. 35-40).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Up to 48 currencies vs USD, 16 from 1976 (BBI plus Reuters vs GBP), 9,403 currency-months, never above ≈40 at once; at least 6 each month. | p. 9-10, Fig. 1, Table A.1 |
| Period | January 1976 to January 2010, monthly. | p. 9 |
| Signal | Lagged excess return over the last f months (f = 1, 3, 6, 9, 12). | p. 12 |
| Entry | Month end: six portfolios, each one sixth of the available currencies. Long "High", short "Low". | p. 12-13 |
| Exit | Held h months (1, 3, 6, 9, 12), then re-sorted. | p. 12 |
| Sizing | Within-portfolio weights not stated. Dollar-neutral long-short. | p. 13 |
| Rebalancing | Monthly sort. Treatment of overlapping portfolios for h > 1 not stated. | p. 12 |
| Costs | Full quoted bid and ask; also 75% and 50% of the spread. | p. 11-12, 27-28 |

**Rule.** Excess return of currency k to a USD investor (Eq. 1, p. 11): rx(t+1) = i(k,t) - i(t) - Δs(k,t+1) ≈ f(k,t) - s(k,t+1), logs, 1-month forward f and spot s. Net long: f(bid,t) - s(ask,t+1). Net short: -f(ask,t) + s(bid,t+1). A currency that stays in the portfolio skips the spot leg cost, not the forward leg cost (p. 11-12). Spot-only version sorts on lagged spot changes (p. 13).

**Data provenance** (p. 9-10)
- End-of-month spot and 1-month forward rates, BBI and Reuters via Datastream, last trading day, not averaged.
- Before 1983, BBI is replaced by Reuters rates vs GBP converted to USD, 16 currencies.
- Bid and ask quotes for the whole period, indicative quotes.
- Country risk: ICRG, from January 1985 (p. 33). Capital openness: Chinn-Ito index (p. 36).

## 3. Results

Excess returns, annualised %, gross unless stated. Real data, in-sample choices (the lookback grid is reported in full).

**Aggregate**
- f = 1, h = 1: 9.46% (t = 5.31), Sharpe 0.95. Spot-only 7.91%. Gross (Table 1, p. 49).
- Long portfolio 5.28%, short portfolio -4.17%: both sides contribute (Table 4A, p. 52).
- Net of full quoted spreads: 3.92% (t = 2.20); at 75% of spread 5.28%; at 50% 6.64% (Tables 8, 9).
- Turnover of the f = 1, h = 1 portfolios: 74.3% (High), 72.2% (Low) a month. Spread markup of winners and losers: 2.6 and 3.1 bp (f = 1) to 3.3 and 6.9 bp (f = 12) (Table A.4).

**By lookback and holding** (Tables 1, 8; gross / net of full spread, f x h)
- Gross falls with h: f = 1: 9.46 (h=1), 5.75 (h=12). f = 12: 6.16 (h=1), 1.89 (h=12, t = 1.04).
- Net: best 4.41 (f = 3, h = 1), t = 2.39. Several cells with f of 6 or more and h of 6 or more are negative, down to -2.44 (f = 12, h = 12).
- Sharpe ranges 0.95 (f = 1, h = 1) to 0.19 (f = 12, h = 12) (Table 1B).
- Out of sample selection: 144 strategies (f, h = 1 to 12) ranked on lagged strategy returns. Best minus worst: 7.67% (lag 1, t = 4.31), 2.70% (lag 120, t = 2.03) (Table 2).

**By sub-group**
- Developed countries (15): f = 1, h = 1: 3.83% (t = 2.72) gross, 0.79% (t = 0.44) net. f = 3, h = 1 net 3.32% (t = 2.05) (Tables A.12, A.13).
- Developed, 1992-2010: 1.56% (t = 1.04) gross, -0.73% (t = -0.32) net (Table A.14).
- Idiosyncratic volatility, f = 1: 3.97% (t = 2.81) low vs 8.09% (t = 4.72) high (Table 11A).
- Country risk, f = 1: 4.50% (t = 3.12) low vs 8.72% (t = 4.19) high. Exchange-rate stability risk: 1.98% (t = 1.39) low vs 6.56% (t = 4.06) high (Table 11B-C).
- Investable list from four banks: 8.76% (t = 4.90); also without NDF currencies: 8.10% (Table 13). Chinn-Ito > 0: 9.22% (Table 12).
- Floating currencies only, from 1986: 9.50% (t = 2.76) for f = 1; floats and managed floats 13.19% (Tables A.9).
- Base currency GBP, CHF, CAD, SEK: 9.27% to 9.48% (Table A.6).
- Cross-section size, f = 1, h = 1 (simulation of random subsets): ≈4.2% with 6 currencies, ≈7.7% with 12, ≈9.4% from 36 (Fig. 3).
- Individual currency sign strategies (long if last month positive): average Sharpe 0.45; equal-weight portfolio 4.86%, Sharpe 0.76; cross-sectional 9.46%, 0.95 (Table A.3).

**Over time**
- Four equal sub-periods, f = 1 mean: 6.20, 7.79, 10.16, 12.37% (last: Sharpe 1.28, 2001-2010) (Table A.2).
- Since 1992: gross 11.69% (t = 4.54), net 7.27% (t = 2.85) for f = 1, h = 1 (Table A.11).
- Net cumulative MOM(1,1): ≈ -10 to -20% until about 1992, ≈+130% at the end; mostly gained 2000-2004 (≈ Fig. 5).
- Rolling 36-month gross return around 2.5% a month near 2003, close to 0 to 0.5% after 2007 (≈ Fig. 7). Authors: rolling net up to about 2% a month in 2000-2005 (p. 31).
- Average developed-country spread ≈15 bp in the 1970s and ≈9 bp in the 1990s, ≈4.5 bp from 2002 (≈ Fig. 6).
- July 2007 to June 2009: MOM(1,1) 0.80% a month, carry -0.05%, correlation -31% (p. 22).

**Link to other strategies**
- Carry H-L: correlation 0.04 (f = 1), 0.01 (f = 6), 0.07 (f = 12) (Table 5A). Carry 10.15%, Sharpe not given in the table (Table 4B).
- MOM(6,1) vs MOM(12,1): 0.73; MOM(1,1) vs MOM(12,1): 0.28 (Table 5B).
- Double sort on forward discount: momentum 5.06% (low rate) vs 5.36% (high rate), difference 0.30% (t = 0.17). Long high rate and high return, short low rate and low return: 10.52% (Table 6, p. 23).
- Moving average rules (1,20), (5,20), (1,200), equal-weighted over currencies: mean 5.27, 5.14, 5.23%; Sharpe 0.88, 0.83, 0.77. Alpha of MOM(1,1) on them 6.90 to 7.80% (t about 4); R² 0.68 to 26.00% (Table 3).
- Fama-MacBeth, 1 month: lagged excess return coefficient 0.16 (t = 5.65) alone; 0.12 (t = 4.42) with lagged forward discount at 0.57 (t = 4.68) (Table 7A).

**Inconsistencies in the source**
- Text p. 34 says low-country-risk currencies yield no significant momentum; Table 11B shows 4.50% (t = 3.12) for f = 1 and 3.31% (t = 2.67) for f = 6. Exchange-rate stability risk matches the text.
- Text p. 35 calls developed-country momentum "basically non-existent after transaction costs"; Table A.13 shows 3.32% (t = 2.05) for f = 3, h = 1.
- Table A.2 labels the third and second sub-periods "09/1984 - 07/2001" and "08/1984 - 01/1993": the dates overlap.
- The abstract and p. 2 say "up to 10%"; the maximum in Table 1 is 9.46%. Loose wording.
- Conclusion says minor currencies account for "roughly 50%" of momentum returns (p. 41); no table shows it.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Excluding EMS currencies improves 1990-1998 performance: chart only, no numbers | Fig. A.2, p. 40 |
| Intervention does not explain momentum: regression with a data issue the authors flag | Table A.10, p. 40 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Six-portfolio sort on lagged excess return, long top sixth, short bottom sixth ([[Cross-sectional momentum]]) | technique | signal | Same as equity momentum; a Deutsche Bank ETF uses top and bottom 3 of G10 | p. 12-13 |
| 2 | Momentum on the sign of each currency's own past return, equal weight ([[Time-series momentum signal]]) | technique | signal | Comparison with time-series literature | p. 20, Table A.3 |
| 3 | Moving average crossover (1,20), (5,20), (1,200), long when short average is above ([[Time-series momentum signal]]) | technique | signal | Benchmark from earlier literature | p. 18-19, Table 3 |
| 4 | Net return with bid and ask on forward and spot legs, haircut to 75% and 50% of spread ([[Break-even transaction cost]]) | technique | evaluation | Quoted spreads too high | p. 11-12, 28 |
| 5 | Double sort on lagged forward discount (or idiosyncratic volatility, country risk) and lagged return ([[Conditional double sort]]) | technique | evaluation | Separate momentum from carry and test limits to arbitrage | p. 23, 32-35 |
| 6 | Cumulative return of the portfolio 1 to 60 months after formation ([[Signal decay profile]]) | technique | evaluation | Jegadeesh-Titman test of under- and over-reaction | p. 25-26 |
| 7 | Momentum applied to the 144 momentum strategies themselves (no card: free choice of window, ex ante selection only) | technique | calibration | Ex ante strategy choice | p. 17-18 |
| 8 | Restrict to an investable list (bank survey, Chinn-Ito, no NDF) (no card: robustness check, lists dated to 2010) | technique | universe | Tradability | p. 35-37 |

## 6. Regime observations

- Profits unrelated to NBER recessions (≈ Fig. 2, p. 15).
- Momentum profits higher in later part of the sample, with the 2000-2005 peak (p. 31, Fig. 7).

## 7. Acknowledged limits

- Indicative spreads too high (p. 12). Several currencies may not have been tradable (p. 35).
- Bank survey: ten currencies not tradable before 1986 to 2001 (p. 37).
- Intervention data are not public, so the test is simple (p. 40).

## 8. Not addressed

- Volatility scaling or position size; weights inside the sixths.
- Drawdowns and maximum loss.
- Capacity, market impact, margin.
- Out-of-sample after January 2010.
