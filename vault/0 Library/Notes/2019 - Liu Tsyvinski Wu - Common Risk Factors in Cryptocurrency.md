---
type: reading-note
source: paper
title: Common Risk Factors in Cryptocurrency
authors: Liu, Tsyvinski, Wu
affiliations: Department of Economics, Yale University; NBER; Stern School of Business, New York University
year: 2019
venue: NBER Working Paper 25882
doi:
pdf: "[[2019 - Liu Tsyvinski Wu - Common Risk Factors in Cryptocurrency.pdf]]"
version: NBER working paper, May 2019 (not peer-reviewed per its cover page). OpenAlex lists a 2022 journal version, not read.
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-10-24
---

# Crypto three-factor model (Liu, Tsyvinski, Wu 2019)

## Summary

- **Finding**: of 25 equity-style factors, 9 give significant weekly long-short returns across 1,707 coins, 2014-2018: size, momentum (1 to 4 weeks), dollar volume, volume volatility. About 3% a week, gross (Tables 3-6).
- **Mechanism**: Not stated by the authors. They offer the factors as stylized facts for future theory (p. 1, 35).
- **Where it works best**: three-week momentum 4.1% a week (t = 2.74); momentum in above-median-size coins 4.2% a week, below-median only 0.6% (n.s.) (Tables 4, A.2).
- **Weak spots**: momentum is not significant in Fama-MacBeth regressions on all coins (Table 13). Shorting Bitcoin instead of the loser quintile kills 1-, 2-, 4-week momentum (Table 12).
- **Main caveats**: no trading costs, shorting "not readily available" for most coins (authors). Momentum factor uses the window with "the largest spread" in the data (fn 7). Value-weighted results only.

Page numbers follow the printed pagination of the working paper (1 to 41). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Crypto returns can be analysed with standard asset-pricing tools; size and momentum matter as in other asset classes | Long-short sorts and factor regressions | p. 1, 35 |
| 2 | Small coins are also more illiquid and trade less, as in stocks | Size factor loads on volume and price strategies | p. 21 |
| 3 | Dollar volume volatility mostly reflects price levels, hence size | Footnote, then CSMB explains the strategy | fn 5; Table 9 |
| 4 | Momentum loadings may be more transient than size loadings | Hedging unpriced risk helps size, not momentum | p. 34-35 |

Economic source of the size and momentum premia: Not stated by the authors.

**Caveats raised by the authors**
- Strategies ignore trading costs and the feasibility of short selling (p. 8).
- Fama-MacBeth weighs coins equally, which may explain why momentum fails there (p. 28).

**Ruled out**
- Equity factor models: FF3, Carhart, FF5 alphas stay close to raw spreads (Table 14, Tables A.3-A.4, p. 33-34).
- Coin market (crypto CAPM) alone: alphas fall only 8.61% on average (p. 16, Table 8).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | All CoinMarketCap coins with price, volume and market cap, market cap above 1 million USD. 109 coins in 2014 to 1,583 in 2018; 1,707 in total. Active and defunct coins listed. | p. 4-5, Table 1 |
| Period | January 2014 to December 2018, weekly | p. 4 |
| Signal | 25 characteristics in four groups: size (MCAP, PRC, MAXDPRC, AGE), momentum (1 to 100 weeks), volume, volatility | Table 2 |
| Entry | Sort into quintiles each week on the characteristic | p. 8 |
| Exit | Hold one week | p. 8 |
| Horizon | Weekly | p. 8 |
| Sizing | Value-weighted within quintile | Tables 3-7 notes |
| Portfolio | Quintile 5 minus quintile 1 | p. 8 |
| Rebalancing | Weekly | p. 10 |
| Costs | Not included | p. 8 |
| Factors | CMKT (value-weighted coin market minus one-month T-bill); CSMB (bottom 30% minus top 30% by market cap, value-weighted); CMOM (top 30% minus bottom 30% on three-week return) | p. 5, 15-16 |
| Data and tools | CoinMarketCap daily close, volume-weighted across exchanges; non-return variables winsorised at 1%/99% each week; Fama-French factors from Kenneth French | p. 4-5 |

**Rule** (p. 8, p. 15-16): each week, rank coins on three-week past return; long the top quintile, short the bottom quintile, value-weighted, hold one week. Size: long smallest quintile, short largest.

**Data provenance**
- Weeks: 52 per year; the last week of the year has 8 days (9 in 2016) (p. 4, fn 2).
- Volume data start in the last week of 2013, which sets the start date (p. 4).
- Some coins are not tracked because their exchanges have no accessible API (fn 1).

## 3. Results

All results are real data, in-sample, gross of costs.

**Aggregate** (Tables 3-6, weekly 5-1)
- Size: MCAP -3.4% (t = -2.56), PRC -3.9%, MAXDPRC -4.1%.
- Momentum: 1-week 2.7%, 2-week 3.3%, 3-week 4.1% (t = 2.74), 4-week 2.5%.
- Dollar volume -3.2%; volume volatility -3.0%.
- Factor means (Table A.1): CMKT 1.3% a week (SD 0.117), CSMB 2.0% (SD 0.143, skew 3.07), CMOM 3.8% (SD 0.184).

**By sub-group**
- Size double sort (Table A.2): momentum 5-1 in small coins 0.6% (t = 0.30), in large coins 4.2% (t = 2.57).
- Fama-MacBeth above 10 million USD (Table 13, Panel E): 2- and 3-week momentum significant alone (0.007).
- Short Bitcoin instead of quintile 1 (Table 12): size strategies 3.4% to 4.0%, 3-week momentum 3.0% (t = 2.25); 1-, 2-, 4-week momentum not significant.

**Horizon and parameters**
- 8-, 16-, 50-, 100-week momentum: not significant (0.6%, 0.4%, -0.8%, -1.1%) (Table 7).
- 16 factors are insignificant, including beta, idiosyncratic volatility, max return, Amihud, age (Table 7).
- Factor models (Tables 8-11): CMKT alone leaves all nine alphas; CMKT + CSMB explains five non-momentum strategies; CMKT + CMOM explains the four momentum ones; the three-factor model leaves no significant alpha.
- Hedging unpriced risk (Daniel et al. 2018): squared weekly Sharpe of size rises from 0.057 to 0.076; momentum unchanged (p. 34).

**Over time**
- Coin market and the three majors peak around January 2018; coin market ≈ 33x its 2014 value at the peak, ≈ 4x at end-2018 (≈ Fig. 1).
- No results by subperiod.

**Link to other strategies**
- Correlations (Table A.1): CMKT with Bitcoin 0.927; CSMB with CMOM -0.033; CMOM with CMKT -0.001.
- FF3-adjusted alphas: MCAP -3.2% (t = -2.37), 3-week momentum 4.2% (t = 2.80) (p. 33-34).

**Inconsistencies in the source**
- p. 8 and fn 4 say tercile-portfolio results for all strategies are in the Appendix. The Online Appendix holds Tables A.1 to A.4 only (factor statistics, size-momentum double sort, Carhart, FF5).
- p. 10-11 call the momentum quintile patterns "almost universally monotonic". Table 4: one-week momentum quintile 4 earns 4.2%, quintile 5 2.1%.
- Table 8's continuation page is headed "Table 3 Continued"; Table 10 and Table 11 equations label the momentum loading as βCSMB and βCHML.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results robust to alternative size measures | fn 6 |
| Results "qualitatively similar" with other momentum windows | fn 7 |
| CoinMarketCap listing of defunct coins "alleviates" survivorship bias | p. 4 |
| Hedge portfolios carry no significant return spread | p. 34 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Port equity price-and-volume factors to crypto (Feng et al.; Chen and Zimmermann list) | principle | signal | No accounting data for coins | p. 8 |
| 2 | Weekly value-weighted quintile sorts, 5-1 | technique | evaluation | Standard asset-pricing test | p. 8 |
| 3 | Crypto factors CMKT, CSMB, CMOM built like Fama-French 30/40/30 | technique | evaluation | Span the successful strategies with few factors | p. 15-16 |
| 4 | Three-week past return as the momentum signal | technique | signal | Largest long-short spread in the data. Card [[Cross-sectional momentum]] | fn 7 |
| 5 | Replace the short quintile by short Bitcoin | technique | portfolio | Most coins cannot be shorted. Card [[Cross-sectional momentum]] | p. 27 |
| 6 | Size-then-momentum double sort at the median | technique | evaluation | Where momentum works. Card [[Conditional double sort]] | Table A.2 |
| 7 | Hedge unpriced risk with covariance-sorted hedge portfolio (Daniel et al. 2018) | technique | risk | Raise squared Sharpe ratio. Card [[Priced and unpriced component split]] | p. 34 |
| 8 | 1 million USD market-cap floor; weekly winsorising of characteristics | technique | universe | Outliers. Card [[Minimum price and size filter]] | p. 4 |

## 6. Regime observations

- Not addressed: no subperiod or market-state split.

## 7. Acknowledged limits

- No trading costs, short selling limited (p. 8, 27).
- Momentum fails in equal-weight style tests (p. 28).

## 8. Not addressed

- Net returns and turnover.
- Drawdowns and crash risk of the momentum factor.
- Results by year.
- Out-of-sample test.
- Liquidity of the smallest quintile, capacity.
