---
type: reading-note
source: paper
title: On the (almost) stochastic dominance of cryptocurrency factor portfolios and implications for cryptocurrency asset pricing
authors: Han, Newton, Platanakis, Sutcliffe, Ye
affiliations: University of Aberdeen; School of Management, University of Bath; ICMA Centre, Henley Business School, University of Reading; University of Exeter
year: 2023
venue: European Financial Management 30 (2024), pp. 1125-1164; published online 2023
doi: 10.1111/eufm.12431
pdf: "[[2023 - Han Newton Platanakis et al - On the (almost) stochastic dominance of cryptocurrency factor portfolios.pdf]]"
version: published (open access); Supporting Information Appendix not read
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-10-24
---

# Which crypto factors dominate, by almost stochastic dominance (Han et al. 2023)

## Summary

- **Finding**: of 29 weekly long-short crypto factor portfolios (2,353 coins, 2014 to mid-2021), eight dominate the S&P 500, T-bonds, T-bills and Bitcoin by AFSD and ASSD at 52-78 weeks: size, 1-2 week momentum, 1-4 week risk-adjusted momentum, MAXRET (p. 1142, 1146).
- **Mechanism**: Not stated by the authors as an economic mechanism; seven of the eight have significant alphas against the Liu-Tsyvinski-Wu model, read as "mispricing" (p. 1148, 1160).
- **Where it works best**: small coins with high risk-adjusted momentum: 5.35% a week (1-week RMOM); big coins with high RMOM 2.76%; big coins with low RMOM ≈ 0 (Table 16). Short horizons (1-3 weeks) beat long (Table 3).
- **Weak spots**: no factor dominates the S&P 500 at 4 weeks; 8- and 26-week momentum are negative; Bitcoin dominates five factor portfolios at 78 weeks (p. 1142). Three-factor R² only 1% to 25% (Table 7).
- **Main caveats**: long-short sign flipped to positive after the fact for negative spreads (p. 1135); no costs; shorting assumed; mispricing factor built from the same eight portfolios it then explains.

Page numbers follow the journal pagination (1125 to 1164). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Mean-variance metrics mislead for crypto because returns are highly non-normal; ASD needs no distribution or utility assumption | Jarque-Bera rejects normality for every series | Tables 1, 3; p. 1126, 1130 |
| 2 | Dominant factor returns reflect mispricing, since the LTW model leaves significant alphas | 7 of 8 alphas significant | Table 7; p. 1148 |
| 3 | Risk-adjusted momentum captures mispricing better than plain momentum | Spanning regressions drop MOM1-2, keep RMOM1, 2, 4 and MARCAP | p. 1154 |
| 4 | Size and momentum effects are stronger in the bull second half | More significant MispricingS and MispricingM loadings after Oct 2016 | Table 15; p. 1157-1158 |

Economic source of the size or momentum premia: Not stated by the authors.

**Caveats raised by the authors**
- Short selling is unavailable for most coins; tested with Bitcoin as the only short (Appendix A13, not read) (p. 1128, 1160).
- MV and CER find dominance counts that depend on the risk-aversion assumption (p. 1140-1141).

**Ruled out**
- Equity factor models (nine tested, Appendix) do not explain the eight portfolios (p. 1160).
- Network and attention factors add little (p. 1150-1152).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 2,353 coins above 1 million USD market cap from Coingecko (defunct coins included); over 90% of total cap on 30 Jun 2021 | p. 1127, 1130 |
| Period | 1 Jan 2014 to 30 Jun 2021, weekly | p. 1130 |
| Signal | 29 characteristics: size (MARCAP, LPRC, AGE), momentum 1-26 weeks, risk-adjusted momentum (Sharpe-based) 1-26 weeks, volume, volatility | Table 2 |
| Entry | Quintile sort each week | p. 1135 |
| Exit | Hold one week | p. 1135 |
| Horizon | Weekly rebalancing; dominance tested on rolling 4, 13, 26, 52, 78-week windows | p. 1140 |
| Sizing | Value-weighted within quintile | p. 1135 |
| Portfolio | Quintile 5 minus 1, or 1 minus 5 when 5-1 is negative | p. 1135 |
| Rebalancing | Weekly | Table 2 |
| Costs | Not stated by the authors | |
| Data and tools | Coingecko prices, volume, market cap; S&P 500 and 10-year T-bond from CRSP; network data from Blockchain.info and Coinmetrics; tweet counts for "blockchain" | p. 1130-1131 |

**Rule** (p. 1135): each week sort coins on the characteristic into quintiles, value-weight, hold one week, long-short the extremes in the direction that earned a positive mean.

Mispricing factor (p. 1154): Mispricing2 = simple average of the MARCAP, RMOM1, RMOM2 and RMOM4 long-short returns. New model (NTFM-SM): CMKT, CSMB, Mispricing2.

**Data provenance**
- Volume data start in the last week of 2013 (p. 1130).
- AGE is defined as weeks listed "on Coinmarketcap.com" while data come from Coingecko (Table 2).

## 3. Results

All results are real data, in-sample, gross of costs.

**Aggregate** (Table 3, weekly 5-1 means)
- MOM1 0.0359 (highest), MOM2 0.0349, RMOM3 0.0302, AGE -0.0272, MARCAP -0.0269, VOLPRC -0.0236.
- Momentum falls with horizon: MOM4 0.0137, MOM8 -0.0072, MOM26 -0.0177; RMOM26 -0.0110.
- All 29 spreads are non-normal; SD from 0.1046 (MARCAP) to 0.2256 (VOL).
- Benchmarks (Table 1): Bitcoin mean 0.0101 a week (SD 0.1039), CMKT 0.0145, S&P 500 0.0025.

**By sub-group**
- AFSD vs S&P 500: none at 4 weeks; 1 at 13 weeks; 4 at 26; 10 at 52; 12 at 78 (Table 5, p. 1142).
- AFSD vs Bitcoin: 5, 6, 6, 9, 10 dominant portfolios from 4 to 78 weeks; Bitcoin FSD-dominates MOM8, MOM26, RMOM8, RMOM26, RETSKEW at 78 weeks.
- LTW three-factor alphas (Table 7): MARCAP 0.0189, MOM1 0.0234, MOM2 0.025, RMOM1 0.0201, RMOM2 0.033, RMOM3 0.0223, RMOM4 0.0247 (all significant); MAXRET 0.0087 (n.s.). Adjusted R² 0.0106 to 0.2523.
- Size and RMOM double sort (Table 16): small coins earn 2.11% to 5.35% a week across RMOM groups and horizons; big low-RMOM coins earn -0.43% to 0.07% (n.s.).

**Horizon and parameters**
- Dominance counts rise with the evaluation horizon (Tables 5-6).
- NTFM-SM leaves one significant alpha of eight (vs seven under LTW); average R² 0.21 (p. 1155-1156).

**Over time**
- Split Jan 2014-Sep 2016 vs Oct 2016-Jun 2021: significant MispricingS loadings rise from three to five, MispricingM from three to six (Table 15).

**Link to other strategies**
- Long legs contribute more to performance than short legs (p. 1160; Appendix).

**Inconsistencies in the source**
- p. 1140 says BETA and BETA2 earn "around 0.0002"; Table 3 gives -0.0029 and -0.0014, and p. 1140 also says RETVOL and BETA2 have the lowest absolute return of 0.0014.
- Table 3 rows MEANABS and LIQ are identical in every column; their definitions differ only in the denominator wording (Table 2).
- p. 1142 says one more AFSD-dominant portfolio (AGE) appears against T-bonds than against the S&P 500 at 26-78 weeks, then calls RMOM4 "the worst of the 13 dominant portfolios" at 26 weeks; the S&P 500 count at 26 weeks is 4.
- p. 1144 says the ASSD count against T-bonds at 26 weeks (three) "is the same as for Panel A"; Panel A has two at 26 weeks.
- p. 1137 names the scaled volume portfolio "VOL"; VOL is log volume and VOLSCALE is the scaled measure (Table 2).
- Sign flipping is described as "not important" (p. 1135), yet it is chosen after seeing the full-sample mean.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Shorting only Bitcoin, the augmented model still beats LTW (Appendix A13) | p. 1128, 1160 |
| Nine equity models fail to explain the eight portfolios (Appendix) | p. 1160 |
| Electricity cost effect on the model (Appendix) | p. 1129 |
| SR and CER values behind Table 4 counts (Appendix A12) | Table 4 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Almost first- and second-order stochastic dominance (ε thresholds 5.9% and 3.2%) to compare strategies with benchmarks | technique | evaluation | No normality or utility assumption; handles skew and fat tails. Card [[Almost stochastic dominance test]] | p. 1132-1135 |
| 2 | Risk-adjusted momentum: rank on past Sharpe ratio, 1-4 weeks | technique | signal | Higher risk-adjusted returns and lower tail risk than plain momentum (cited). Card [[Cross-sectional momentum]] | p. 1135 |
| 3 | Mispricing factor as equal-weight average of anomaly long-shorts (Stambaugh and Yuan) | technique | evaluation | Parsimony with many anomalies | p. 1150 |
| 4 | Spanning regressions to drop redundant factors | technique | evaluation | Fama and French (2015, 2018) | p. 1153-1154 |
| 5 | Dependent size-then-momentum sort for CMOM | technique | signal | Control size inside momentum | p. 1147 |

## 6. Regime observations

- Size and risk-adjusted momentum loadings are stronger in the Oct 2016-Jun 2021 subperiod, described as the rapid-growth phase of Bitcoin (Table 15).
- Momentum is strongest among small coins (Table 16), opposite to Liu et al. (2022) who find it stronger among large coins; authors cite Hong et al. (2000) in support.

## 7. Acknowledged limits

- Short-selling availability (p. 1128).
- Results depend on investment horizon of evaluation (p. 1142).

## 8. Not addressed

- Transaction costs and turnover of weekly long-short portfolios.
- Out-of-sample test of the NTFM-SM model or of the factor selection.
- Look-ahead in choosing the long-short direction and the eight dominant factors on the full sample.
- Liquidity of small coins that drive the best results.
