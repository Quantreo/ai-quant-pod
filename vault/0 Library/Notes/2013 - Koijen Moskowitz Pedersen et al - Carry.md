---
type: reading-note
source: paper
title: Carry
authors: Koijen, Moskowitz, Pedersen, Vrugt
affiliations: Koijen (London Business School), Moskowitz (Chicago Booth, NBER), Pedersen (Copenhagen Business School, NYU, NBER), Vrugt (Amsterdam address, no institution given). Moskowitz and Pedersen disclose an affiliation with AQR Capital Management.
year: 2013
venue: NBER Working Paper 19325, August 2013 (https://www.nber.org/papers/w19325)
doi: Not printed in the PDF
pdf: "[[2013 - Koijen Moskowitz Pedersen et al - Carry.pdf]]"
version: working paper (NBER, not peer reviewed). A later JFE 2017 version exists; this note covers only the NBER version.
tier: 1
read: full
tags: [carry, multi-asset, monthly]
date: 2026-10-22
---

# Carry (Koijen, Moskowitz, Pedersen, Vrugt 2013)

## Summary

- **Finding**: long high-carry, short low-carry, rank-weighted, monthly, in nine asset classes: every Sharpe ratio positive (0.37 to 1.80, average 0.74). Volatility-weighted global carry factor: Sharpe 1.10, gross.
- **Mechanism**: carry is a model-free part of expected return; its predictive power implies time-varying expected returns. Losses cluster in global recessions; macro risk versus funding/limits to arbitrage left open.
- **Where it works best**: put options (Sharpe 1.80), global equity index futures (0.88), and the diversified factor (1.10, skewness -0.02). Equity, bond and option profits come almost entirely from the dynamic component.
- **Weak spots**: bond level and slope carry Sharpe below passive long (0.52 vs 0.74; 0.66 vs 0.71). Commodity panel coefficient not significant. Call options weak. Every carry strategy loses in global carry drawdowns.
- **Main caveats**: no transaction costs; authors concede carry faces larger costs and funding issues than passive. Carry1-12 robustness mostly weaker than claimed. Several text vs table inconsistencies.

Page numbers follow the printed pagination of the NBER working paper (printed page = PDF page minus 2). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Return = carry + expected price appreciation + shock; carry is observable ex ante | Eq. 1, 6 | p. 1, 7 |
| 2 | Carry predicts returns, so expected returns vary over time and across assets, rejecting the expectations hypothesis / UIP | Panel regression coefficient c positive in every class with both fixed effects; significant except commodities and calls | p. 1, 27-28; Table VI |
| 3 | Carry unifies known predictors: dividend yield (equities), yield slope (bonds), convenience yield (commodities), rate differential (FX) | Derivations Eq. 7-17 | p. 8-14, 24-25 |
| 4 | Part of the premium may compensate for large losses in global recessions | All nine carry strategies negative in global carry drawdowns; recession indicator 0.33 in drawdowns vs 0.19 in expansions | p. 4, 31; Table VIII |
| 5 | Whether this is macro risk / risk aversion or limited capital, arbitrage and funding squeezes is "an open question"; both may contribute | None decisive | p. 4 |

**Caveats raised by the authors**: see section 7. Also: unconditional loadings may hide dynamic exposures (p. 24); drawdown correlation evidence "not overwhelming" (p. 31).

**Ruled out (or challenged)**
- Crash risk as a general explanation: negative skewness is not present in all classes (equities, Treasuries, credit positive), and the diversified factor has skewness -0.02 vs -0.38 for diversified passive (p. 3, 21-22; Table II).
- Spanning by value, momentum, TSMOM, local market: alphas stay positive in every class (Table IV).
- Equity carry is not the historical dividend yield: correlation of strategies 0.07, beta 0.07 (p. 25; App. D p. 44-45).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 13 equity index futures; 20 FX forwards (19 countries plus euro, US carry = 0); 24 commodity futures; 10 government bonds (10Y level and 10Y-2Y slope); 6 CRSP US Treasury maturity buckets; 8 US credit indices (AAA to BAA, intermediate and long); calls and puts on 9-10 US equity indexes, two delta groups | p. 16-18; Table I |
| Period | Starts vary: Treasuries Aug-71, credit Feb-73, commodities from Feb-80, FX and bonds from Nov-83, equities from Mar-88; options Jan-96 to Dec-11; others to Sep-12 | p. 17; Table I |
| Signal | Current carry at month end. Futures: C = (S - F) / F. Commodities: slope of the two nearest contracts per month. Bonds: carry of a synthetic 1-month future on a 10Y zero (slope plus roll down). Treasuries and credit: carry divided by duration. Options: price change if only time passes, theta and vol roll-down. | Eq. 5, 7-10, 16-22; p. 7-16 |
| Entry, exit, horizon | Monthly rebalance on new ranks; one-month hold; no other exit rule | p. 18-19 |
| Sizing | Weight proportional to carry rank minus its cross-sectional mean, scaled so longs sum to 1 and shorts to -1. Futures fully collateralised. | Eq. 23; p. 6-7, 18 |
| Portfolio | Global carry factor (GCF): each asset-class carry portfolio weighted by inverse full-sample volatility | p. 21; Table II |
| Costs | None; results gross | n/a |
| Variants | Carry1-12 (12-month average of carry); regional/group portfolios; timing (sign of carry; carry vs mean) | p. 19-20, 29; App. C; Table VII |

**Rule** (Eq. 23, p. 18), for asset i among N available at t:

$$w^i_t = z_t \left(\text{rank}(C^i_t) - \frac{N_t + 1}{2}\right), \quad r_{t+1} = \sum_i w^i_t r^i_{t+1}$$

GCF: volatility-weighted average of the nine class portfolios, using full-sample volatility (p. 21; Table II caption).

**Options**: 30 to 60 days to maturity, held one month; one option per index and delta group (|delta| 0.2-0.4, 0.4-0.6), chosen by volume then open interest (p. 17-18).

**Data provenance**

| Class | Source | Notes |
| --- | --- | --- |
| Equities | Bloomberg spot, first and second futures | Carry from futures interpolated to 1 month; returns from front contract rolled 3 days before expiry (p. 9, 36) |
| Currencies | Barclays Bank International before 1997:01, WMR/Reuters after; checked with HSBC, Thomson Reuters | Quotes flagged when implied rate differs from IBOR by more than 2% (p. 37-39) |
| Commodities | Bloomberg first to third futures; LME cash and 3-month for industrial metals | Returns from GSCI excess return indices, rolled 5th to 9th business day (p. 40) |
| Global bonds | Zero-coupon yields: Wright data to May 2009, Bloomberg after | Synthetic futures; correlation above 0.95 with real futures where they exist (p. 13, 42) |
| Treasuries, credit, options | CRSP portfolios with Gurkaynak-Sack-Wright yields; Barclays corporate indices; OptionMetrics | p. 17 |

## 3. Results

All real data, in-sample, gross. Annualised unless stated.

**Aggregate** (Table II A)
- GCF: mean 6.75%, volatility 6.12%, skewness -0.02, kurtosis 5.24, Sharpe 1.10. Diversified passive: Sharpe 0.47, skewness -0.38, kurtosis 7.94.
- GCF alpha vs all-asset market, value, momentum, TSMOM: 0.44% per month (t = 5.51), IR 1.24; no significant loading (Table IV A).
- Cross-class carry correlations mostly -0.15 to 0.21; FI level vs slope 0.66 (Table III A).
- Cumulative sum of GCF excess returns ends ≈2 vs ≈0.85 for currency carry at equal volatility (Fig. 1).

**By asset class** (individual securities)

| Class | Carry Sharpe / passive Sharpe | Carry skew | % dynamic | Alpha per month with all factors (t) |
| --- | --- | --- | --- | --- |
| Global equities | 0.88 / 0.32 | 0.22 | 101% | 0.77 (4.51) |
| Bonds 10Y | 0.52 / 0.74 | -0.43 | 86% | 0.33 (3.08) |
| Bonds 10Y-2Y | 0.66 / 0.71 | -0.22 | 99% | 0.29 (3.63) |
| US Treasuries | 0.68 / 0.57 | 0.47 | 42% | 0.02 (2.74) |
| Commodities | 0.60 / 0.08 | -0.40 | 64% | 0.64 (2.57) |
| Currencies | 0.68 / 0.36 | -0.68 | 58% | 0.30 (2.31) |
| Credit | 0.47 / 0.34 | 1.32 | 30% | 0.02 (1.70) |
| Calls | 0.37 / -0.23 | -2.82 | 111% | 6.93 (2.15) |
| Puts | 1.80 / -1.01 | -1.75 | 100% | 12.55 (4.55) |
| Where | Table II A | Table II A | Table V | Table IV A |

- Calls: alpha vs passive alone not significant (3.21, t = 1.07) (Table IV A).
- Commodity carry loads negatively on value, positively on momentum; alpha falls 29 bp to 64 bp per month (p. 24).
- Regional/group carry: Sharpe 0.44 to 0.59 (Table II B). Commodity and FX group alphas with factors not significant (t = 1.74, 1.40) (Table IV B).

**Predictive regressions** (Table VI, both fixed effects)
- c above one: equities 1.14, bond level 1.44, slope 2.51, credit 1.46. Below one: Treasuries 0.45, puts 0.54, calls 0.16 (t = 1.45), commodities 0.01 (t = 0.13). FX 1.09.
- No fixed effects: calls -0.05 (t = -0.25); commodities 0.06 (t = 0.79).

**Timing** (Table VII)
- Long if carry above zero, short if below: Sharpe 0.23 (calls) to 1.01 (puts); equities 0.40, commodities 0.40, FX 0.78.
- Relative to mean: calls -0.14; Treasuries 0.31; others 0.53 to 0.96.

**Over time** (real data, in-sample)
- Biggest GCF drawdowns: Aug 1972 to Sep 1975, Mar 1980 to Jun 1982, Aug 2008 to Feb 2009 (p. 30-31); depth ≈-0.20, ≈-0.27, ≈-0.07 in Fig. 2 units.
- In GCF drawdowns every carry strategy is negative: bond level -13.90 vs passive +8.33; puts -22 vs passive +132 (Table VIII).
- Drawdown correlations rise for FX-credit (0.03 to 0.48) (Table IX).
- Equities and bonds lose early in drawdowns, options late; commodities, FX, credit throughout (p. 32; Table X).
- Equity carry: dynamic share 53% of drawdown losses vs 93.5% of expansion gains (Table XI).

**Link to other strategies**
- Equity carry vs dividend yield sort: Sharpe 0.87 vs 0.50, correlation 0.07, alpha 8.70, beta 0.07 (App. D, p. 45).
- Bond carry vs 10Y-3M yield spread: signal correlation 0.90, returns 0.91 (p. 14).

**Inconsistencies in the source**
- p. 16 lists Norway (OMX) among equity futures; App. B (p. 36) and Table I list Sweden (OMX).
- Carry1-12 is the average "including the most recent" month (p. 19) vs "t - 12 to t - 1" (App. C, p. 42).
- p. 19: carry1-12 results "typically stronger". App. C: Sharpe lower in 7 of 9 classes (e.g. equities 0.53 vs 0.88, puts 0.50 vs 1.80); higher only for Treasuries and commodities. App. D: carry1-12 equity Sharpe 0.33.
- Table VII Panel B: text says carry vs its "sample mean" (p. 29); caption says "rolling sample mean over the last five years".
- Fig. 1 caption: sample from 1972; the plotted x-axis starts ≈1984.
- p. 29: currency predictability "cut roughly in half" with fixed effects; Table VI gives 1.28 without and 1.09 with both.
- p. 24: credit "significant carry alpha remains" with factors; Table IV A gives t = 1.70.
- p. 3: dynamic share "about half" for credit; Table V gives 30%.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Carry1-12 is a positive and significant predictor "even for commodities" in panel regressions; App. C repeats only Tables II and IV | p. 28 |
| Results stronger with all five delta groups for options | footnote 15, p. 17 |
| Robust to dropping the first trading day of the month and to omitting the DAX | p. 37 |
| FX results "do not strongly depend" on removing outliers | p. 37 |
| Top / bottom 20-30% portfolios give robust results | p. 18 |
| Timing strategies "all positive and significant": no t-statistics in Table VII | p. 29 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Carry signal]]: Carry = return if price stays unchanged, (S - F) / F | principle | signal | Model-free, observable ex ante, same across classes | p. 6-7 |
| 2 | [[Carry signal]]: Commodity carry from the slope of the two nearest futures, per month | technique | signal | Spot prices illiquid or missing | p. 11 |
| 3 | [[Carry signal]]: Bond carry from a synthetic 1-month future on a 10Y zero (slope plus roll-down) | technique | signal | Few liquid bond futures, cheapest-to-deliver issues | p. 13-14 |
| 4 | Duration-adjusted positions and carry for Treasuries and credit | technique | sizing | Put bonds of different risk on a common scale | p. 14-15 |
| 5 | [[Long-short portfolio weighting]]: Rank-based long/short weights, longs sum to 1, shorts to -1 | technique | sizing | Used in prior work; correlated with other weightings | p. 18 |
| 6 | [[Volatility targeting]]: Inverse full-sample volatility weighting across asset classes | technique | sizing | Options and commodities would dominate an equal weight | p. 21, footnote 18 |
| 7 | [[Carry signal]]: 12-month average of carry (carry1-12) | technique | calibration | Smooth dividend and commodity seasonality | p. 19 |
| 8 | [[Static and dynamic return decomposition]]: Static / dynamic decomposition of strategy return | technique | evaluation | Separate average positioning from timing | p. 26; Eq. 27 |
| 9 | [[Carry signal]]: Time-series carry timing: sign of carry, or carry vs its mean | technique | signal | Isolate dynamic component | p. 29; Table VII |
| 10 | [[Conditioning on factor drawdowns]]: Conditioning results on factor drawdown vs expansion periods | technique | evaluation | Unconditional correlations miss common risk | p. 30-31 |

## 6. Regime observations

Carry drawdowns coincide with global recessions (p. 31; Fig. 2). Details in section 3, "Over time".

## 7. Acknowledged limits

- Higher costs, funding and limits to arbitrage than passive (p. 22).
- Commodity current carry affected by seasonality (p. 28).
- Coefficient above one mostly not significantly different from one (p. 28).
- Option contracts less liquid than in prior work (footnote 14, p. 17).
- Why asset classes react at different times in drawdowns left for future research (p. 32).

## 8. Not addressed

- Transaction costs, slippage, margin and capacity: no figures.
- Out-of-sample or ex-ante test: none; GCF weights use full-sample volatility.
- Maximum drawdown in % of capital and drawdown duration in months: not reported as numbers.

**Questions for the desk**
- Table I: before 1980 only US Treasuries (Aug-71) and credit (Feb-73) have data. The 1972-75 drawdown, one of the three largest, may then reflect only these two classes. The paper does not say how the GCF is built when few classes exist.
- Table X: caption says annualised, but values look about one twelfth of Table VIII (e.g. puts expansions 23.5 and 20.3 vs 258). Monthly units? Not stated.
- The JFE 2017 version may differ in sample and numbers; this note only covers the NBER version.
