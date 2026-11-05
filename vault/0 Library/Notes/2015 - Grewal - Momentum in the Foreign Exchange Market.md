---
type: reading-note
source: paper
title: Momentum in the Foreign Exchange Market
authors: Grewal
affiliations: University of Canterbury (New Zealand)
year: 2015
venue: Master of Commerce thesis in Finance, University of Canterbury
doi:
pdf: "[[2015 - Grewal - Momentum in the Foreign Exchange Market.pdf]]"
version: master's thesis (109 pages, not peer-reviewed, supervised work)
tier: 1
read: full
tags: [trend, fx, daily]
date: 2026-10-25
---

# Momentum in the FX market (Grewal 2015)

## Summary

- **Finding**: ranking 18 currencies against USD on the last day's return, long the best and short the worst, earned 5.58% a year excess (one pair each side, hold one day), 2002-2013. Longer formation or holding turns negative.
- **Mechanism**: noise traders, stop-loss orders, front-running, slow information across sessions: listed, none tested. Weekly and monthly profits tied to interest differentials.
- **Where it works best**: daily, one-day formation and holding, one pair per side: 6.79% before the crisis, 4.32% after. Weekly and monthly: only before the crisis, and in minors and exotics.
- **Weak spots**: 21 of 25 daily cells are negative (whole sample, one pair). Weekly returns negative after 2008. Majors weekly negative before the crisis.
- **Main caveats**: no costs, no t-statistic, no Sharpe, no drawdown, no out-of-sample. Master's thesis. Same-fix signal and trade not discussed.

Page numbers follow the printed thesis pagination, which equals the PDF page. Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

The thesis does not test a mechanism. The conclusion lists candidates.

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Noise traders extrapolate past moves and create short-term momentum | None from the thesis's data. Cites Okunev and White (2003), Malkiel (2003) | p. 51, 19 |
| 2 | Stop-loss and take-profit order clustering extends a move | None from the thesis's data. Cites Osler (2003) | p. 51, 27-29 |
| 3 | Rational speculators front-run positive feedback traders | None from the thesis's data. Cites De Long et al. (1990) | p. 52, 25-26 |
| 4 | Slow information diffusion from one trading session to the next | Not tested. Offered as "in line with" Jegadeesh and Titman (2001) | p. 52 |
| 5 | Weekly and monthly returns rely on interest rate differentials | Spot returns are negative where excess returns are positive before the crisis (Tables 3.3-3.6) | p. 46, 52 |
| 6 | Speculators add to positions before price continuation | Regressions of returns on lagged changes in speculative open interest (Table 5.1) | p. 50, 53 |

**Caveats raised by the authors**
- A range of short-term factors probably combine to give the one-day result (p. 52).
- The COT report is weekly with a delay, so causation is hard to argue (p. 53).
- The thesis does not say whether a portfolio gains in the first part of its holding period then loses in the latter part (p. 55).
- Practicality of the short-term result needs risk management, not yet added (p. 54).

**Ruled out**: nothing.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 18 pairs against USD: AUD, GBP, CAD, CZK, DKK, EUR, HKD, HUF, JPY, MXN, NZD, NOK, PLN, SGD, ZAR, SEK, CHF, TRY | Table 1, p. 62 |
| Sub-universes | Majors: AUD, GBP, CAD, EUR, JPY, NZD, CHF. Minors and exotics: the other 11 | Table 2, p. 63 |
| Period | Prices 1 July 2002 to 28 June 2013. COT 10 July 2006 to 24 June 2013 (8 pairs) | p. 32, 35 |
| Sub-periods | Before: 1 June 2002 to 31 May 2007. Crisis holdout, dropped: 1 June to 31 December 2007. After: 1 January 2008 to 28 June 2013 | p. 36 |
| Signal | Return against USD over the last p periods, ranked | p. 38 |
| Entry | End of each period, long the n best, short the n worst, equal weight, USD-neutral | p. 36, 38 |
| Exit | After q periods | p. 38 |
| Grid, daily | p, q in 1 to 5 days; n in 1 to 3: 75 portfolios | p. 38-39 |
| Grid, weekly | p, q in 1 to 5 weeks; n in 1 to 3 | p. 40 |
| Grid, monthly | p, q in 1, 3, 6, 9, 12 months; n in 1 to 3 | p. 40 |
| Sizing | Equal weight. No volatility scaling stated | p. 38 |
| Costs | None. "Low transaction costs" asserted for FX | p. 10 |
| Data | Datastream, WM/Reuters benchmark rates (London 4pm fix), spot and overnight, 1-week, 1-month forwards, foreign currency per USD | p. 32-33 |

**Rule** (as printed, p. 37)
- Long foreign currency X: spot return r(t+1) = s(t) - s(t+1); excess return R(t+1) = f(t) - s(t+1).
- Short: signs reversed. s and f are log spot and log 1-day forward, quoted as foreign currency per USD.
- Every portfolio with the same p, q, n over the sample is averaged and annualized (p. 39). Overlap handling and the annualization method are not stated.

**Data provenance**
- The fix is a median of bid and offer in a 60-second window around 4pm London, reported as the average of the two (p. 33).
- Pegged or managed currencies (HKD, DKK, SGD) sit in the sample with no comment.
- The thesis uses 18 pairs against up to 48 in Menkhoff et al. (p. 33).

## 3. Results

All results are real data, in-sample, excess return (forward-based, mid rates), gross of costs. In the tables rows are holding periods and columns are formation periods.

**Aggregate**
- Daily, one pair per side, whole sample: 5.58% (formation 1, holding 1); 2.41% (formation 2, holding 1); 1.42% (formation 1, holding 2); 0.33% (2, 2). The 21 other cells run from -0.06% to -3.66% (Table 3.1, p. 64). Counted.
- Formation 5, holding 1: -3.17%. Formation 1, holding 5: -0.61% (p. 43).
- Spot return of the best cell: 6.95% (Table 3.2, p. 65; p. 45).
- More pairs per side lower the best cell: 5.58% (n=1), 5.13% (n=2), 3.66% (n=3) (Table 3.1; p. 43).
- Weekly, one pair, whole sample: -5.73% (1, 1) to 1.41% (3, 3). Mostly within one point of zero (Table 3.3, p. 66).
- Monthly, one pair, whole sample: best 2.26% (formation 3, holding 1); worst -2.42% (formation 12, holding 1) (Table 3.5, p. 68).

**By sub-group**
- Majors, daily, n=1, whole sample, cell (1, 1): 5.29%. Minors and exotics: 4.24% (Tables 4.1, 4.2, p. 70-71). Authors: "little difference" (p. 47).
- Daily (1, 1), n=1, before the crisis: majors 5.73%, minors and exotics 4.51%. After: majors 3.59%, minors and exotics 4.74% (p. 47-48; Tables 4.1-4.2).
- Weekly, before the crisis, n=1: minors and exotics positive in every cell, up to 7.15% (formation 2, holding 1). Majors negative in every cell, -2.36% for the same cell (Tables 4.5-4.6, p. 74-75; p. 48-49).
- Weekly after the crisis: minors and exotics mostly negative, majors mixed (Tables 4.5-4.6).
- Monthly: majors slightly better on the whole sample. Minors better before the crisis, worse after (p. 49).

**Horizon and parameters**
- Daily returns fall as formation or holding rise from 1 to 5 days, in every sub-period (p. 43-44).
- Weekly: the 1-week formation and holding cell is the worst of the grid whole sample (p. 45).
- Monthly: short formations slightly positive, long formations slightly negative (p. 46).

**Over time**
- Daily (1, 1), n=1: 6.79% before, 4.32% after (Table 3.1, p. 44). Poor cells get worse after (p. 44).
- Weekly n=1, before: 0.55% loss in one cell, gains up to 3.84% elsewhere. After: every n=1 cell negative, from -10.28% to -0.44% (Table 3.3, p. 66).
- Monthly n=1, after: 0.01% (1, 1) and 0.26% (formation 1, holding 3), other cells negative (Table 3.5, p. 68).
- Authors tie the post-2008 drop in weekly and monthly returns to near-zero interest rates (p. 8, 13, 52).

**Link to other strategies**
- Spot against excess: weekly and monthly before the crisis, most spot returns negative while excess returns positive (p. 46, Tables 3.4, 3.6). The authors read this as interest differentials (carry).
- COT: higher long open interest, lower short open interest, are followed by positive returns. Whole sample, formation 1, lag 1: long coefficient 0.003359 (t = 2.32), short -0.003554 (t = -3.47). Formation 5, lag 1: 0.036119 (t = 12.56) and -0.0076 (t = -3.59). Significance fades by lag 4 to 5 (Table 5.1, p. 82). Newey-West, 2 lags (p. 42).
- After the crisis the coefficients are more significant (p. 50-51).
- Menkhoff et al. (2011), reported by the thesis, not tested: 1-month formation and 1-month holding give nearly 10% a year, 1976-2010 (p. 23).

**Inconsistencies in the source**
- Sample start: 1 July 2002 (p. 32), 1 June 2002 (p. 36, 42), "June 2002" in chart titles (p. 5).
- p. 45 says a holding period of five days gives -3.17% excess and -4.55% spot. Table 3.1 and 3.2 give these for formation 5, holding 1. Holding 5 gives -0.61%.
- p. 45 says every weekly portfolio is negative after the crisis. Table 3.3 (n=3, formation 4, holding 1) shows +0.31%.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| FX has "low transaction costs", so the effect is large in practice | p. 10 |
| Short-term momentum comes from noise traders, order flow or slow information | p. 51-52 |
| Post-2008 weakness is due to central bank rates near zero and easing | p. 8, 13 |
| Speculators drive momentum (only a predictive regression is shown) | p. 53 |
| Regressions for excess and spot returns are alike because the gap is small against open interest changes | p. 50 |
| Pegged currencies do not distort the sample | Not discussed |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Daily cross-sectional momentum: rank pairs on the last p days, long n best, short n worst, hold q days (USD-neutral, equal weight) | technique | signal | Extension of Menkhoff 2011 to shorter horizons. [[Cross-sectional momentum]] | p. 36-38 |
| 2 | Same ranking on weekly and monthly data | technique | signal | Same. [[Cross-sectional momentum]] | p. 39-40 |
| 3 | Compare spot and excess return of the same portfolio to see the interest differential share | principle | diagnostics | Not argued. [[Spot and roll return decomposition]] | p. 45-46 |
| 4 | Split sample before and after the 2008 crisis, 2007 dropped | principle | evaluation | To test the effect of the crisis | p. 36 |
| 5 | Split pairs into majors and minors and exotics | principle | universe | Neely and Weller (2011) found more momentum in emerging markets | p. 41 |
| 6 | Regress returns on lagged changes in speculative open interest (COT) | technique | signal | Wang (2000), COT as a continuation indicator | p. 41-42 |

## 6. Regime observations

- Authors place a drop in FX momentum in the early 1990s after the 1987 Louvre Accord and falling growth and inflation volatility (p. 12-13).
- Weekly and monthly returns before 2008 are positive, after 2008 negative (p. 45-46, 66, 68).
- Daily momentum is positive in both sub-periods, smaller after (p. 44).

## 7. Acknowledged limits

- No data of quicker positioning than weekly (p. 53).
- No risk management applied (p. 54).
- No reversal analysis inside the holding period (p. 55).
- The thesis could not tell whether the one-day pattern holds with intraday data (p. 53-54).

## 8. Not addressed

- Transaction costs, bid-ask spread, slippage, capacity.
- Statistical significance of any portfolio return (no t-statistic, no standard error).
- Sharpe ratio, volatility, drawdown, skewness.
- Out-of-sample test.
- Execution lag: ranking on the fix and trading at the same fix.
- Treatment of overlapping holding periods and of the annualization.
- Role of pegged currencies.
- Correlation with carry or with Menkhoff's portfolios.
