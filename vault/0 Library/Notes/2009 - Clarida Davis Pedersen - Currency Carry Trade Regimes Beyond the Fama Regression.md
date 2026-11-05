---
type: reading-note
source: paper
title: "Currency Carry Trade Regimes: Beyond the Fama Regression"
authors: Clarida, Davis, Pedersen
affiliations: Clarida (Columbia University and NBER), Davis and Pedersen (PIMCO)
year: 2009
venue: NBER Working Paper 15523, November 2009
doi: none printed in the PDF (http://www.nber.org/papers/w15523)
pdf: "[[2009 - Clarida Davis Pedersen - Currency Carry Trade Regimes Beyond the Fama Regression.pdf]]"
version: working paper, not peer reviewed (p. 1)
tier: 1
read: full
tags: [carry, fx, monthly]
date: 2026-10-22
---

# Currency carry trade regimes (Clarida, Davis, Pedersen 2009)

## Summary

- **Finding**: G10 carry baskets earn 2.38% to 5.66% a year, 1990-2009. When realized FX volatility is in its top quartile, all-currency 1v1 to 3v3 baskets lose money (1v1: -9.75%).
- **Mechanism**: Not stated as a model. Authors document co-movement: carry returns fall when volatility rises, rise with relative yield curve level, fall with relative slope and VIX.
- **Where it works best**: low volatility quartile. 4v4 ex JPY/USD earns 7.23% at m/v 1.34; all-currency 1v1 earns 13.61% at m/v 1.33.
- **Weak spots**: high volatility quartile, mostly yen-funded baskets. Fama slope flips sign across regimes but no Table 3 coefficient is significant. 1997-98 crisis not explained by the factors.
- **Main caveats**: no costs stated; regimes use full-sample quartiles, so no tradable rule is tested; CIP breakdown in 2007-08 acknowledged, not explored.

Page numbers follow the printed working-paper pagination, which matches the PDF page from p. 3 on (pp. 1-2 are unnumbered cover and abstract). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

The paper is empirical. It documents relationships and defers a pricing model to future work (p. 27).

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Carry returns are inversely related to realized and implied FX volatility | Z-scored EWMA return vs minus log EWMA volatility, 3v3: correlation 0.55, 0.65 from 1996 | p. 10-11, Fig. 2 |
| 2 | Same as 1, by regime | Returns much lower in top volatility quartile | Table 2, p. 12 |
| 3 | Same as 1, nonparametric | Kernel regressions of return on volatility, bootstrap bands | Fig. 3, p. 13-14 |
| 4 | Rises in implied volatility go with carry losses, falls with gains, nearly symmetric | Panel kernel regression on change in 1-month ATM implied vol | Fig. 4, p. 15-16 |
| 5 | The change in conditional volatility drives the predictable part of carry returns | E-GARCH with h_t and h_t-1: cannot reject -θ1 = θ2 | p. 16-17, Table 2b |
| 6 | Negative Fama slope is an artifact of the volatility regime | Slope negative in low vol, above 1 in high vol | Table 3, Table 4, p. 19-21 |
| 7 | Carry returns co-move with relative yield curve level (+), slope (-) and VIX change (-) | Weekly regressions on six pairs and pooled | Table 5, p. 23-24 |
| 8 | Crisis 2007-09 differs from non-crisis by a larger VIX loading, not by yield curve loadings | Pooled VIX -4.10 vs -2.51; level 1.70 vs 1.60; slope -1.13 vs -1.15 | Table 5, p. 24 |

Reading of 7: level proxies real rates or inflation, which a credible central bank answers with higher rates and a stronger currency; slope proxies the business cycle (p. 24-25). The VIX link supports a fundamental explanation (p. 27-28).

**Caveats raised by the authors**
- They do not separate risk premium from expectations components of yield changes (p. 22-23).
- CIP deviations in 2007-08 mean forward premia and rate differentials are not interchangeable, yet the paper treats them so; possible US Libor under-reporting. "have not explored this further" (p. 26).
- The robustness to excluding the yen holds only "to a point" (p. 3).

**Ruled out**
- The 2008 yen/dollar unwind is not statistically unusual given the 4v4 ex JPY/USD basket returns (p. 25-26, Fig. 5).

## 2. Strategy, brick by brick

No trading rule is tested. The portfolios below are the objects studied.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | G10 currencies. Three variants: all, ex JPY, ex JPY and USD | p. 6-7, Table 1 |
| Period | Table 1: 1990-2009. Fig. 1a from 1992. E-GARCH 1993-2009. Table 3: 1991-2009. Implied vol data: 1 Oct 1996 to 14 Jan 2009 | Table 1, 2b, 3; p. 15 |
| Signal | Rank by interest rate. N v N: long the N highest yielders, short the N lowest, N = 1 to 5 (1 to 4 ex JPY/USD) | p. 6 |
| Sizing | Equal weight within each leg | p. 6 |
| Rebalancing | Not stated by the authors | |
| Horizon | Daily returns (Tables 1-2), weekly (Table 2b, Table 5), 1-month (Fama regressions) | Tables |
| Regime | Low: EWMA realized volatility below the full-sample 25th percentile; high: above the 75th | p. 11 |
| Costs | Not mentioned. Gross or net not stated | |

**Rule** (as defined, p. 10-11), on daily carry return r_t, λ = 0.95 (half-life 14 days):

$$\sigma_t = \frac{\sum_{i=0}^{T}\lambda^i (r_{t-i}-\bar r)^2}{\sum_{i=0}^{T}\lambda^i}, \qquad \text{high vol if } \sigma_t > P_{75}(\sigma), \text{ low vol if } \sigma_t < P_{25}(\sigma)$$

Percentiles are over the full sample. As written, σ_t includes r_t itself (i = 0).

Fama regression (Eq. 9, p. 19): Δx_t+1 = α + β(i^H_t - i^L_t) + ε_t. UIP implies β = 1.

**Data provenance**

| Item | Source | Where |
| --- | --- | --- |
| Carry basket returns | Bloomberg, "realized carry returns", daily | p. 6, 10 |
| Implied vol, spot, ATM 1-month options, G10 vs USD | Citibank (called Citigroup on p. 21) | p. 15, 21 |
| Interest differential in Table 4 | Backed out of spot and option strike via CIP | p. 15, Eq. 5 |
| Yield curve factors | Level = 10-year yield, slope = 10y minus 2y, high-yield country relative to low | Table 5 note |
| VIX | Percentage change in US implied volatility index | Table 5 note |

## 3. Results

All results are real data, in-sample. No out-of-sample test, no simulation.

**Aggregate** (Table 1, 1990-2009, annualized)
- Mean 2.38% to 5.66%, vol 6.18% to 15.06%, m/v 0.25 to 0.66. Best m/v: 3v3 ex JPY (0.66). Worst: 2v2 all currencies (0.25).
- Volatility falls as N rises; mean falls too, from 4.98% (1v1) to 3.28% (5v5), all currencies (p. 8).
- Fig. 1a: the three 3v3 indexes rise from 100 to peaks ≈270-330 in 2007-08, then drop sharply into 2009.

**By sub-group**
- Ex JPY/USD baskets have higher mean and lower vol than all-currency from 1v1 to 3v3 (p. 8-9, Table 1).
- USD/JPY carry alone (vol 11.59%) gave about the same total return as 4v4 ex JPY/USD (vol 6.88%) over 1993-2009 (Fig. 1b, p. 9). End values ≈160 vs ≈147.
- High volatility state (Table 2): all-currency 1v1, 2v2, 3v3 negative (-9.75%, -5.01%, -1.89%). Ex JPY: 1v1 and 2v2 negative. Ex JPY/USD: 1v1 to 3v3 positive (1.14% to 4.72%), 4v4 negative (-0.67%).
- Low volatility state (Table 2): all 14 cells positive, 2.87% to 13.61%, m/v 0.38 to 1.34.
- Fig. 3 kernel fits (3v3): all-currency return ≈+7% at 6% vol, ≈-12% at 19% vol. Ex JPY and ex JPY/USD curves flatten near ≈0 above ≈15% vol, with wide bands.
- E-GARCH (Table 2b, weekly 1993-2009): 4v4 in-mean coefficient negative in all four specifications; t from -1.56 (dynamic symmetric, not significant) to -19656.5. USD/JPY: t -0.33 in the symmetric level model, -2.38 to -16.71 elsewhere. Asymmetry term D negative for 4v4 (t -1.90 and -4.20), not for USD/JPY.
- Fama regression by country (Table 4, implied vol regimes): low-vol slope negative for all 9 currencies (-0.44 to -9.21). High-vol slope above 1 for 6 of 9 (NZD 1.72 to NOK 11.27); negative for CAD, EUR, JPY. Standard errors 4.66 to 11.40 in high vol.
- Factor regressions (Table 5, weekly): pooled R-square 0.06 (1997-98), 0.20 (2007-09), 0.13 (non-crisis).

**Horizon and parameters**
- Threshold changes: "consistent across a wide range" (p. 12), not shown.
- Only λ = 0.95 is used.

**Over time**
- 3v3 return/volatility correlation rises from 0.55 (full) to 0.65 (from 1996) (p. 10-11).
- Large drawdowns: Asian crisis, LTCM (p. 7-8), 2008 (Fig. 1a-b). Yen/dollar unwinds in 1994, 1998, 2002, 2008 (p. 25).
- Fig. 5: largest negative residual ≈-0.14 in late 1998; 2008 residuals ≈-0.06 at worst.
- 1997-98: factors do not span returns; level loadings insignificant, slope loadings positive (Table 5, p. 25).

**Link to other strategies**
- Payoff compared to selling OTM puts on high-yield currencies, following Bhansali (2007) (p. 2, 5). No option strategy is tested.
- USD/JPY weekly returns on 4v4 ex JPY/USD: correlation 0.27, slope 0.46, t = 8.14 (p. 26).

**Inconsistencies in the source**
- Text says the Fama slope goes from "significant and very negative" to "significant and very positive" (p. 20). Table 3: -3.29 (s.e. 4.31) and 2.73 (s.e. 2.41), t ≈ -0.76 and 1.13 (computed). Neither is significant; R-square 0.00 and 0.01.
- Text says level, slope and VIX loadings "remain significant across the board with the same respective signs" (p. 24). Table 5: CHFUSD VIX in 2007-09 is +0.50 (t 0.78); CHFNZD level t 1.21 and slope t -1.60 in 2007-09; JPYNZD slope t -1.23 non-crisis.
- Text says implied-vol Fama slopes show "a clear pattern" with high-vol coefficients "far greater than 1" (p. 21). Table 4: CAD -2.39, EUR -1.13, JPY -1.34 in high vol.
- Several citation years differ from the reference list (e.g. Jurek 2008 vs 2007, p. 5, 30).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Regime results robust to a wide range of thresholds | p. 12 |
| Carry Sharpe ratios comparable or superior to equities, citing Burnside et al. | p. 8 |
| Results robust to excluding the yen | p. 3, 27 |
| "Can't reject" -θ1 = θ2: no test statistic reported | p. 17 |
| The 2008 yen/dollar episode is "not statistically unusual": only residual chart and full-sample regression shown | p. 25-26 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Carry signal]], [[Long-short portfolio weighting]]: N v N equal-weight carry basket ranked by interest rate | technique | signal | Diversification lowers volatility | p. 6, 8 |
| 2 | [[Currency exclusion filter]]: Exclude JPY and USD from the carry universe | principle | universe | Literature dominated by yen and dollar; USD is a safe haven | p. 7 |
| 3 | [[Volatility regime filter]]: EWMA realized volatility, λ = 0.95, half-life 14 days | technique | risk | Not argued | p. 10 |
| 4 | [[Volatility regime filter]]: Volatility regimes from quartiles of realized or implied vol | technique | evaluation | Returns depend strongly on volatility | p. 11, 21 |
| 5 | Fama regression run separately by volatility regime | technique | evaluation | Shows the negative slope is regime driven | p. 19-21 |
| 6 | Nadaraya-Watson kernel regression with residual bootstrap bands | technique | evaluation | Robust to misspecification and nonlinearity | p. 13, 31 |
| 7 | E-GARCH-in-mean with lagged conditional variance | technique | evaluation | Isolate the role of the change in volatility | p. 16-17 |
| 8 | Implied rate differential from option strike and spot via CIP | technique | universe | Matched dataset with implied vol | p. 15 |
| 9 | Regress carry returns on VIX change and relative yield curve level and slope | technique | evaluation | Link carry to bond risk factors | p. 22-23 |
| 10 | Regress a single pair on a diversified basket and inspect residuals to judge an unwind | technique | evaluation | Check whether a crisis is unusual | p. 25 |

## 6. Regime observations

- Carry losses concentrate in high volatility (Table 2, Fig. 3-4); there low-yield currencies appreciate by more than the rate differential (p. 4, 21).
- See claim 8 and Over time for crisis loadings.

## 7. Acknowledged limits

- No asset pricing model; future work (p. 23, 27).
- Risk premium and expectations not separated in yields (p. 22-23).
- CIP deviations and Libor under-reporting in 2007-08 may affect Section 4-5 results (p. 26).

## 8. Not addressed

- Transaction costs, slippage, gross vs net.
- Basket rebalancing frequency, which rates are used to rank currencies in the Bloomberg data.
- An ex-ante tradable rule: regimes use full-sample percentiles.
- Out-of-sample tests.
- Drawdown statistics, skewness, capacity.
- The γ coefficient on the rate differential in Eq. 10 is not reported in Table 5.

**Open questions for the desk**
- Table 2 text speaks of "subsequent returns" (p. 12), but σ_t includes r_t and regime days are not said to be lagged. Are regime returns contemporaneous with the volatility that defines them? If so, Table 2 is not a predictive test.
- Sample start is unclear: abstract says 18 years, Table 1 says 1990-2009, Fig. 1a starts 1992, Table 3 says 1991-2009.
- Table 2b reports t-statistics such as -19656.5 and -754.7 with standard errors of 0.000 to 0.005 (asymmetric models). These look implausible; not explained in the text.
- Eq. 1 defines σ_t as a weighted mean of squared deviations, which is a variance, yet it is called volatility. Which one sets the regimes?
