---
type: reading-note
source: paper
title: Factor Timing with Portfolio Characteristics
authors: Kagkadis, Nolte, Nolte, Vasilas
affiliations: Lancaster University Management School (all four authors)
year: 2023
venue: Working paper, 24 March 2023 (journal not stated)
doi:
pdf: "[[2023 - Kagkadis Nolte Nolte et al - Factor Timing with Portfolio Characteristics.pdf]]"
version: working paper with Internet Appendix (p. 1)
tier: 1
read: full
tags: [value, equities, monthly]
date: 2026-10-25
---

# Factor timing with portfolio characteristics (Kagkadis 2023)

## Summary

- **Finding**: on 72 US stock anomalies, 1990-2019 out of sample, forecasts from portfolio characteristics (PCA or PLS, then LASSO) give a long-short of factors at 1.47% a month (t 3.40), gross. Best benchmark 1.06% (Table 4).
- **Mechanism**: Not stated by the authors. They only say characteristics carry information on the factor portfolios beyond their own spread (p. 1-3).
- **Where it works best**: LASSO models, LSS strategy. Total OOS R² 0.52% to 1.53%, cross-sectional correlation 7.7% to 9.0% (Tables 1, 3). Positive in 2010-2019 (≈ Figure 5).
- **Weak spots**: a single characteristic factor has negative Total OOS R² (Table 1). Percent-change accounting anomalies are not predicted (p. 25). Gains over book-to-market are not significant (Table 2).
- **Main caveats**: no transaction costs, no turnover, no capacity. Long-short deciles of 72 anomalies, shorts assumed free. Number of PCs, window and gamma fixed by the authors.

Page numbers follow the printed pagination (PDF page minus 1). Internet Appendix pages are written IA p. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Characteristics used to sort stocks, aggregated to the portfolio, predict factor returns | OOS R², cross-sectional correlation, strategy returns | p. 1-3, 23-37 |
| 2 | Many stocks sit in several factor portfolios, so characteristics other than a portfolio's own can predict it | Own-characteristic model does worse than all-characteristics (Table 5, 6) | p. 2, 41-44 |
| 3 | Predicting only the dominant PCs isolates common predictability and drops spurious predictability of small PCs | Cited no-near-arbitrage argument; 5 PCs hold about 67% of variance | p. 2, 6, 11-12 |
| 4 | PLS is better than PCA to compress characteristics, because PCA mixes relevant and irrelevant variation | Table 3, 4 single factor | p. 3, 29, 35 |
| 5 | The signal in characteristics varies over time, so the number of components should vary | Figure 4: number of non-zero LASSO coefficients varies, at times zero | p. 31-32 |

**Caveats raised by the authors**
- Low-eigenvalue PCs "reflect risk or mispricing" is left open (fn 6, p. 6).
- Total OOS R² does not say whether a model ranks well (p. 28).
- Anomalies with low covariance to the rest are not captured by the 5 PCs (p. 25).

**Ruled out**
- Decay over time: the timing strategies show no decay in return performance (p. 4, 39).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 72 characteristics of Green et al. (2017). CRSP and Compustat, NYSE, AMEX, NASDAQ common stocks. Price under $5 removed at formation. NYSE breakpoints. | p. 20, IA p. 14 |
| Period | Monthly, 01/1970 to 12/2019. First estimation 01/1970-12/1989. Forecasts out of sample 01/1990-12/2019 (360 months, computed). | p. 20, 23 |
| Factor portfolios | Value-weighted deciles on each characteristic at t-1. Long decile 10, short decile 1, even when the characteristic relates negatively to returns. | p. 20-21 |
| Signal | Portfolio characteristics standardised cross-sectionally each month, mapped to PC portfolios, rotated by PCA or PLS, forecasts by OLS on the first component or LASSO on all. | p. 11-16 |
| Entry | Three rules from the forecasts: LSS, TSFM, CSFM (see Rule). | p. 32-34 |
| Exit | Positions reset each month. | p. 32 |
| Horizon | One month. | p. 23 |
| Sizing | LSS equal weights. TSFM and CSFM: forecast divided by monthly volatility, capped at ±2, unit dollar on each leg. | p. 33-34 |
| Portfolio | Long-short portfolio of factor portfolios, from 72 anomalies. | p. 32 |
| Rebalancing | Monthly. PC portfolios and forecasts re-estimated each month. | p. 13 |
| Costs | Not mentioned. | whole paper |
| Tools | PCA, RPPCA (Lettau and Pelger), PLS (SIMPLS), LASSO (coordinate descent). | IA p. 2-6 |

**Rule**
- Each month t, standardise the 72 portfolio characteristics C_t cross-sectionally (subtract mean, divide by standard deviation). Winsorise stock characteristics at 99% (p. 14, 20).
- Estimate the first 5 PCs of factor returns on an expanding window of at least 240 months. PCA: eigenvectors of the covariance. RPPCA: eigenvectors of (1/T) R'R + γ mean mean', γ = 10 (p. 13-14, IA p. 3-4).
- PC characteristics H_i = w_i' C_t. Scores X_i = H_i Q_i, Q from PCA of H_i, or PLS of H_i on the PC return (Eq. 3, p. 11-12).
- Forecast z_{t+1,i} = β0 + Σ β_m X_m. Either m = 1 with OLS, or all m with LASSO (Eq. 4, p. 12, 15).
- LASSO penalty: the last 60 months of the in-sample window are a validation sample. A geometric grid of penalties is run recursively. The one with the lowest squared error is kept, then the model is refit on the full window (p. 15).
- Factor forecasts = Σ_i w_i z_{t+1,i} (Eq. 5, p. 12).
- LSS: long the top 10% of anomalies by forecast, short the bottom 10%, equal weights (p. 32-33).
- TSFM: s = min(max(forecast / σ, -2), 2). Long positive s, short negative s, each leg scaled to unit dollar (Eq. 9-10, p. 33).
- CSFM: same, after subtracting the cross-sectional median forecast (Eq. 11, p. 34).

**Data provenance**
- Accounting data lag: at least 6 months after fiscal year end, 4 for quarterly (p. 20).
- Sentiment: Baker-Wurgler index (p. 19). Issuer-repurchaser spread: Greenwood-Hanson (p. 19).

## 3. Results

All results are real data, out of sample, 1990-2019, gross (no cost mentioned). The estimation is expanding-window, with no look-ahead (p. 13-14).

**Aggregate** (Table 4, monthly average return in %, monthly Sharpe)
- Panel B (LASSO), LSS: PCA 1.47 (Sharpe 0.18, t 3.40), PCA-PLS 1.38, RPPCA 1.21, RPPCA-PLS 1.23. TSFM 0.84 to 0.97, CSFM 0.83 to 0.97.
- Best monthly Sharpe 0.21 (RPPCA and RPPCA-PLS, under TSFM and CSFM). The abstract's annualised 0.73 matches 0.21 × √12 (computed).
- Benchmarks, LSS: 1mMOM 1.06, 12mMOM 0.84, PCA-BM 0.79, IR spread 0.87, sentiment 0.74, historical mean 0.48. Best benchmark monthly Sharpe 0.16 (PCA-BM, TSFM).
- Total OOS R² (Table 1): single factor from -1.55% to -0.38%. LASSO from 0.52% to 1.53%. 1mMOM -88.98%, 12mMOM -6.61%, BM 0.43%, IR spread 0.13%, sentiment 0.42%.
- Average cross-sectional correlation (Table 3): LASSO 7.74% to 9.04%. Single factor PLS 9.12% and 9.17%, PCA 0.70%. Benchmarks 3.24% to 5.98%.
- Sign hit rate (Table 3): 49.90% to 52.75%. Close to a coin flip for every model.

**By sub-group**
- By PC (Table 1, LASSO): PC2 is most predictable (0.60% to 6.97%). PCA PC5 is -0.78%.
- By anomaly (Figure 3, heat map): value (bm) and sales to price (sp) are highly predictable. Percent-change accounting anomalies (pchsale_pchrect, pchcurrat) are not (p. 25).
- PC meaning (IA p. 22-23): PC1 loads on volatility (beta, idiovol, maxret, retvol), PC2 on value and profitability, PC3 on momentum, PC4 on R&D, PC5 on salerec. Loadings stable over time (IA Figure IA.9).
- Trading (IA p. 25-26): the strategy rotates among many anomalies. It goes long mom6m, mom12m and short beta, chmom, retvol most often. Anomalies with small PC loadings are hardly traded.

**Horizon and parameters**
- Number of LASSO features varies by PC, by time, and falls to zero at times (Figure 4, p. 31-32). PCA uses more features than PLS.
- Single factor vs LASSO: LASSO raises every model (Tables 1, 3, 4).
- Rotation method: with LASSO, PCA vs PLS and PCA vs RPPCA differences are small (p. 4, 36).
- Alternatives (Tables 5, 6): own characteristic only, LSS 0.46%. All characteristics per anomaly with LASSO 1.02%. 5 PCs with all characteristics and LASSO 1.09%. All below the main 1.21% to 1.47%.
- Benchmarks with PCs or LASSO added (Table 6): best 5 PCs-1mMOM 1.13%, Anom-All IR Spreads 1.24%.

**Over time**
- 1mMOM leads until the late 1990s. All strategies jump around 2000. Characteristic models hold after the burst and after 2008 (≈ Figure 5, p. 37-38).
- 2010-2019: characteristic models trend up. IR spread, sentiment, factor momentum and the historical mean are flat (≈ Figure 5, p. 37).
- Cumulative LSS scale ≈ 5 for PCA over 1990-2019. Unit not defined; 1.47% × 360 months gives 529% (computed).
- Maximum drawdown (Table 4, LSS, Panel B): 15.00% to 38.11%. Benchmarks 18.45% to 34.74%.

**Link to other strategies**
- Factor momentum 1 month beats the historical mean error in only 20% of months, with a large gain then and large losses in the other 80% (p. 30, fn 20).
- Unconditional factors: only 22 of 72 have significant mean returns, 10 out of sample (p. 21). Timing strategies beat them (p. 39, Table IA.4).

**Inconsistencies in the source**
- Text p. 23 says "only the second PC portfolio being predictable" in Panel A. Table 1 shows positive R² for PC4 and PC5 under PCA, and PC4 under PCA-PLS.
- Text p. 36 says PCA on the left gives a higher hit rate than RPPCA irrespective of strategy or model. Table 4 LSS: PCA 55.71% against RPPCA 57.66%.
- Text p. 36 says RPPCA gives higher Sharpe ratios irrespective of strategy or model. Table 4 LSS: PCA 0.18 against RPPCA 0.17.
- Text p. 44 says even the best modified benchmark is weaker than the main models. Table 6 LSS: Anom-All IR Spreads 1.24% against RPPCA 1.21% and RPPCA-PLS 1.23% (Table 4). TSFM and CSFM are lower (0.80, 0.81 against 0.84, 0.86).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| PC portfolios have a clear economic interpretation, stable over time | p. 22; IA Figures IA.8-IA.9 |
| The main source of time variation in characteristics is the higher moments of their cross-section | p. 30; IA p. 6-9 (figures only) |
| Weighting vectors remain relatively stable over time | p. 30, fn 21; IA Figures IA.6-IA.7 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Forecast the 5 dominant PCs of factor returns from their own aggregated characteristics, PCA or PLS then LASSO. Card [[Factor timing on dominant components]] | technique | signal | Focus on common variation, regularise both sides | p. 11-17 |
| 2 | Risk Premium PCA: PCA of second moment plus γ times the mean outer product | technique | universe | Favours factors with high average return. Inside card [[Factor timing on dominant components]] | p. 2-3; IA p. 3-4 |
| 3 | Time-varying LASSO with rolling 60-month validation for the penalty | technique | calibration | Characteristic signal varies over time. Inside card [[Factor timing on dominant components]] | p. 15-17 |
| 4 | Past factor return as forecast, 1 or 12 months, per factor | technique | signal | Benchmark from the literature. Card [[Factor momentum signal]] | p. 18 |
| 5 | LSS: long top 10%, short bottom 10% of forecasts | technique | sizing | Targets extremes of the forecast distribution. Card [[Long-short portfolio weighting]] | p. 32-33 |
| 6 | TSFM and CSFM: forecast over volatility, capped ±2, unit dollar per leg | technique | sizing | Uses the whole universe. Card [[Long-short portfolio weighting]] | p. 33-34 |
| 7 | Cross-sectional correlation and sign rate between forecasts and realised returns, next to OOS R² | technique | evaluation | R² does not rank. Card [[Forecast ranking accuracy]] | p. 28-30 |
| 8 | Modified Diebold-Mariano test between models | technique | evaluation | Pairwise accuracy. No card: standard practice | p. 26-27 |
| 9 | Standardise characteristics cross-sectionally each month | technique | signal | Equal scale, cross-sectional focus. Inside card [[Factor timing on dominant components]] | p. 14 |
| 10 | Replace each anomaly's own characteristic by all characteristics, then PCs, then LASSO | technique | evaluation | Where does predictability come from? No card: ablation design | p. 40-44 |

## 6. Regime observations

- Factor momentum 1 month is best in the early years, then falls behind (≈ Figure 5, p. 37).
- Spike in all strategies around 2000 and again in 2009 (≈ Figure 5, p. 37).

## 7. Acknowledged limits

- Total OOS R² and portfolio performance can disagree (p. 28).
- Anomalies with low PC loadings are not predicted (p. 25, 40).

## 8. Not addressed

- Transaction costs, turnover, capacity, short-selling costs.
- Subperiod statistics beyond a chart; no table for 2010-2019.
- Out-of-sample choice of the number of PCs (5), γ (10), validation length (60 months), cap (±2).
- Non-US stocks and other asset classes.
