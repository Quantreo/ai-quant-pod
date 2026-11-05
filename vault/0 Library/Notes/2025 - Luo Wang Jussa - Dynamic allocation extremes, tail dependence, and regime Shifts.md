---
type: reading-note
source: paper
title: Dynamic allocation: extremes, tail dependence, and regimes (DB Handbook of Portfolio Construction, Part 2)
authors: Luo, Wang, Jussa, Chen, Alvarez
affiliations: Deutsche Bank Quantitative Strategy
year: 2013
venue: Deutsche Bank Markets Research, Portfolios Under Construction, 10 September 2013
doi:
pdf: "[[2025 - Luo Wang Jussa - Dynamic allocation extremes, tail dependence, and regime Shifts.pdf]]"
version: broker report
tier: 2
read: full
tags: [low-vol, multi-asset, monthly]
date: 2026-10-25
---

# Dynamic allocation with a copula risk model and risk regimes (Luo 2013)

## Summary

- **Finding**: a copula-GARCH risk model, refit monthly, lifts average Sharpe of 11-asset risk-based portfolios from ≈1.14 (rolling) to ≈1.27 (Fig. 35). A risk regime lifts forecast IC/sd 1.53 to 2.31 (p. 48).
- **Mechanism**: Not stated by the authors. They cite stylised facts and say risk is easier to predict than returns (p. 7, 54).
- **Where it works best**: real data, monthly ex-ante refits: risk-based portfolios of 11 asset classes and 5 equity factors, and the regime split of factor returns (p. 26, 59-62).
- **Weak spots**: Sharpe not higher everywhere: risk parity ≈1.32 vs ≈1.37 rolling (Fig. 35). Alpha-strategy CVaR worse than expanding window (Fig. 78). Regime fit rests on Nov 2008 (p. 38-39).
- **Main caveats**: no costs or turnover, no separate hold-out, model structure chosen on the full sample, look-ahead in asset tilts and long-term alpha (p. 31, 46), results mostly bar charts.

Page numbers are the printed report pages, equal to the PDF pages. Values marked ≈ are read from a chart. The PDF file name says 2025, the report is dated 10 September 2013.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Returns show serial correlation, volatility clustering, outliers, time-varying correlation and tail dependence, so a normal-based covariance misses risk | ACF plots; tail dependence 28% vs correlation 19% for equities and commodities | p. 7-16, Fig. 19 |
| 2 | Risk is easier to predict than returns, and risk regimes are more stable than return regimes | Markov models on returns fail to converge for treasuries and high yield; EM equities model sits in one regime for 14 years | p. 54-55, Fig. 86 |
| 3 | Assets, portfolio rules and factors behave differently by regime | Regime-split return charts | p. 42-44, 52-54, 60-63 |
| 4 | High VRP means panic: markets overreact, so risky assets are bought at extreme VRP | Charts and correlations of lagged VRP with next-month returns | p. 32-33 |

**Caveats raised by the authors**
- Better risk accuracy does not always give a better portfolio (p. 21).
- The VRP and CVaR fit relies on a single point, Nov 2008 (p. 38-39).
- The risk-based gains come mostly from high-risk regimes, because the optimised portfolios hold more bonds than the 60-40 benchmark (p. 52-53).
- Low volatility factor mean return falls in high-risk regimes, driven by a few outliers; the median rises (p. 61).

**Ruled out**
- GJR-GARCH asymmetry dropped: significant for equities only, t 5.7; bonds t 1.1, commodities t -1.2 (p. 12, Fig. 14).
- Regime models on returns: Not addressed beyond the two failures above (p. 54-55).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Risk gauge: 50% MSCI World, 40% DB Aggregate Bond, 10% S&P GSCI. Allocation: 11 classes (Russell 1000 and 2000, EAFE, EM, REITs, treasuries, high yield, IG sovereign, EM credit, GSCI, gold), benchmark 30/30/20/20 US large cap, EAFE, treasuries, IG sovereign. Factors: value, momentum, quality, size, low vol in MSCI World | p. 5, 22, 56 |
| Period | Risk model from 31 Jan 1994 (data from 2 Jan 1989); regimes from Dec 1998; 11-asset weights from 2003; factors from Nov 1999, strategies from Nov 2004 | p. 18, Fig. 43, 58, 87; p. 64 |
| Signal | CVaR of the gauge, regime probability, VRP regression | p. 19, 38, 33 |
| Sizing | Risk-based rules (inverse vol, risk parity, max diversification, min variance, min CVaR, min tail dependence) and max Sharpe or max mean-CVaR with forecasts | p. 25, 34-35 |
| Rebalancing | Monthly, expanding window, models refit each month | p. 18-19 |
| Costs | Not reported | whole paper |
| Data | Bloomberg, MSCI, Russell, S&P, Worldscope | Fig. sources |

**Rule**
- Per asset: ARMA(1,1) mean, GARCH(1,1) variance. Residuals: DCC for correlation, t-copula for tail dependence. Simulate 21 days, 10,000 paths; CVaR and volatility of the gauge from the paths (p. 18-19). The 11-asset case uses the same setup, "not fine tuned" (p. 26).
- Risk regime: dynamic Markov switching, 2 states, on predicted CVaR: CVaR_t = mu(s_t) + phi(CVaR_{t-1} - mu(s_{t-1})) + sigma(s_t) eps_t, with mu(s_t) = b0(s_t) + b1(s_t) VRP_{t-1}. Transition probabilities depend on VRP_{t-1}; residual variance depends on the regime (p. 37-38). Same model on predicted correlation (fn 18).
- True out-of-sample probability: refit each period on data to that date; use last period's predicted probability. High risk if probability is 50% or more (p. 40-41).
- VRP = squared VIX minus realised variance from five-minute S&P 500 returns, lagged one month (p. 32, fn 19).
- Forecast: r_{t+1} = b0 + b1 VRP_t + b2 I(P(s_t=1) >= 0.5), OLS per asset at each month end, 60-month rolling window (p. 31, 33, 47).
- Factor weighting repeats the simulation and optimisation 20 times and averages the weights (p. 59, 64). Not stated for the 11-asset case.

**Data provenance**
- Equities, bonds and commodities for the gauge go back to 1989 (p. 18). Series behind the indices before launch: Not addressed.

## 3. Results

**Aggregate** (real data, ex-ante refits, gross or net not stated)
- Pearson vs copula tail dependence: equities-commodities 19% vs 28%; equities-bonds -4% vs 8%; bonds-commodities -11% vs 4% (Fig. 19).
- 11 assets, nine risk-based rules, average Sharpe: ≈1.14 rolling, ≈1.19 expanding, ≈1.27 GARCH-DCC-Copula; benchmark ≈0.83, equal weight ≈0.88 (Fig. 35).
- Average return ≈7.6, ≈7.9, ≈8.3% (Fig. 33). Volatility about the same, ≈6.9% (Fig. 34).
- Alpha strategies, average Sharpe ≈0.83, ≈1.15, ≈1.18 (Fig. 77). The weakest, max Sharpe on one-year average returns: ≈0.33 rolling vs ≈1.3 GARCH (Fig. 77).
- Case study, Dec 2008 to Jun 2009, risk parity: 5.2% vs 4.2% with the rolling window (p. 29).
- GTAA cross-sectional IC: VRP only avg 7.1%, sd 46.3%, ratio 1.53; with regime 10.1%, 43.8%, 2.31 (Fig. 73-74). Style rotation: 9.1%, 57.2%, 1.59 vs 11.1%, 58.9%, 1.88 (Fig. 103-104).
- Factor portfolios, risk parity: return 1.5%, vol 2.7%, Sharpe 0.54 rolling vs 1.5%, 2.5%, 0.60 GARCH. Max diversification: 1.5%, 2.4%, 0.63 vs 1.7%, 2.4%, 0.72 (Fig. 93-94).
- Factor rotation (VRP plus regime forecast, max mean-CVaR): 5.3% return, 5.9% vol, Sharpe 0.91 vs 0.54 and 0.63 for rolling risk parity and max diversification; max drawdown -9.2% vs -5.4% and -3.1%; CVaR -1.8% vs -2.1% and -1.5% (Fig. 106-107). Units of return not stated.
- Illustration with look-ahead, regime asset tilts: long only 16.5% return, 14.9% vol, Sharpe 1.11; long-short 16.2%, 15.8%, 1.02 (Fig. 72; fn 23).

**By sub-group**
- Portfolio CVaR is about 47% higher in high-risk regimes (p. 42). Equities and REITs earn less there; bonds and commodities more (Fig. 65).
- High correlation regimes (1999, since 2009): equities, high yield, EM credit earn more; bonds and commodities earn more in low correlation (Fig. 67).
- Four-state best and worst assets per regime listed in Fig. 70.
- Factors: value and quality do well in high risk, momentum and size the reverse; low vol falls in high risk (Fig. 97). Value, quality, size earn more in high correlation, momentum and low vol in low (Fig. 101).
- Risk-based portfolios earn more than the benchmark in high-risk, low-correlation states, because they hold more bonds (p. 52-53).

**Horizon and parameters**
- Regime threshold 0.5. ARMA(1,1) and GARCH(1,1) orders not varied. No sensitivity shown.

**Over time**
- Predicted CVaR peaks in 2008. Equities-commodities correlation rises from mid-2009 (p. 19). Gauge CVaR for bonds near a 20-year high in 2013 (p. 28).
- Factors since 1999: value highest cumulative return, low vol negative average (p. 56).

**Link to other strategies**
- Risk-based rules fall in four clusters: naive, diversification, risk reduction, alpha (Fig. 81-82).
- Value and momentum negatively correlated (p. 57).

**Inconsistencies in the source**
- p. 26: Sharpe improves "across the board" with the copula model; Fig. 35 shows risk parity ≈1.32 vs ≈1.37 rolling and max diversification equal (≈, chart).
- p. 48: alpha strategies have "lower downside risk"; Fig. 78 average CVaR ≈-24% vs ≈-22% for the expanding window, and the long-term alpha case is worse (≈, chart).
- p. 64: factor rotation has "slightly higher downside risk"; max drawdown -9.2% vs -5.4% and -3.1% (Fig. 107).
- p. 16: 28% is "almost 44% higher" than 19%; computed 47%.
- p. 44: the four states list "low risk and high correlation" twice; the fourth is low risk, low correlation by Fig. 68-70.
- p. 59: step 5 repeats "step 6" for the weights; the numbering is off.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Normality tests reject for all assets; "details available upon request" | p. 5, fn 4 |
| Portfolios are less crowded and more diversified with the copula model (bar charts only) | p. 26, Fig. 37-38 |
| Risk-based rules all beat the benchmark "regardless of the risk models" | p. 26 |
| Low vol factor tumbles in high risk, explained by cross-section vs time-series risk | p. 61 |
| Regime models fitted to factor returns had inferior power to linear regression (earlier work, not shown) | p. 55 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Markov-switching risk regime on predicted CVaR, VRP-driven transitions, refit each month ([[Regime probability filter]]) | technique | signal | Risk is easier to predict than returns | p. 37-41 |
| 2 | Regression forecast on lagged VRP, plus a high-risk regime dummy ([[Variance risk premium signal]]) | technique | signal | Markets overreact at extreme VRP | p. 32-33, 47 |
| 3 | GARCH-DCC-t-copula risk model, simulated scenarios feed the optimiser ([[GARCH-copula risk model]]) | technique | sizing | Captures clustering, outliers, tail dependence | p. 18, 26 |
| 4 | Max mean-CVaR weights from simulated scenarios ([[Mean-variance weighting]]) | technique | sizing | CVaR fits non-normal returns | p. 35-36 |
| 5 | Average the weights of 20 simulation and optimisation runs (no card, statistical device) | technique | sizing | Resampling, to answer "outperformance is random" | p. 59 |
| 6 | Asset and factor returns split by risk and correlation regime ([[Market state split]]) | technique | evaluation | Returns differ by regime | p. 42-44, 60-63 |
| 7 | Time-series IC of risk forecasts against next-month realised risk (no card, standard practice) | technique | evaluation | Risk is unobservable, so use look-ahead benchmark | p. 20-21 |
| 8 | Weighted average portfolio correlation, volatility-weighted (no card, calculation) | technique | evaluation | Correlation is not a plain weighted average | p. 14-15 |

## 6. Regime observations

- Two high-correlation regimes since 1998: around 1999 (equities and bonds) and since 2009 (equities and commodities) (p. 43, fn 22).
- 2002-2007 mostly low risk, low correlation; internet bubble mostly high risk, low correlation; since 2008 correlation high, risk on and off (p. 44).
- Filtered, smoothed and one-step probabilities differ from the true out-of-sample one: correlation with it 56%, 47%, 68% (Fig. 63).

## 7. Acknowledged limits

- Most optimised portfolios are bond-heavy, which explains much of the regime result (p. 52).
- Look-ahead in the asset tilts of Fig. 70-72 and in the long-term alpha model (fn 23, p. 31).
- "Most" academic regime papers fit parameters on the full sample; the authors refit each period for this reason (p. 40).

## 8. Not addressed

Transaction costs, turnover, slippage, capacity, leverage, shorting costs, gross or net, a held-out period, significance tests on any Sharpe difference, the sensitivity to the 50% threshold or the 60-month window, VIX and five-minute data availability before the sample.
