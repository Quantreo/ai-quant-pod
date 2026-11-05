---
type: reading-note
source: paper
title: Carry trades and currency crashes
authors: Brunnermeier, Nagel, Pedersen
affiliations: Brunnermeier (Princeton, NBER), Nagel (Michigan Ross, NBER), Pedersen (Copenhagen Business School, NYU, NBER; also affiliated with AQR Capital Management)
year: 2008
venue: NBER Working Paper 14473, November 2008
doi: not given in the PDF (http://www.nber.org/papers/w14473)
pdf: "[[2008 - Brunnermeier Nagel Pedersen - Carry Trades and Currency Crashes.pdf]]"
version: working paper, not peer reviewed (cover page)
tier: 1
read: full
tags: [carry, fx, monthly]
date: 2026-10-22
---

# Carry trades and currency crashes (Brunnermeier, Nagel, Pedersen 2008)

## Summary

- **Finding**: high rate differentials predict higher FX excess returns and more negative skewness, eight currencies vs USD, 1986-2006. Carry portfolios: Sharpe 0.59 to 0.78, skewness -0.54 to -0.98, gross.
- **Mechanism**: authors' claim: crashes come from sudden unwinding of carry trades when speculators hit funding constraints (rising VIX, TED). Slow capital makes FX under-react to rate shocks.
- **Where it works best**: 3 long / 3 short quarterly, Sharpe 0.784 (Table 2). Interest rate differential predicts skewness strongly up to 10 quarters ahead (Table 3).
- **Weak spots**: skewness not diversified away; carry loses when VIX rises; rate differential loses significance once signed VIX is added; TED results mostly insignificant; CFTC link only marginally significant.
- **Main caveats**: no costs; sample ends 2006; only eight currencies vs USD; regressions, not traded strategies; peso problem admitted; long-run over-reaction not ruled out.

Page numbers follow the printed pagination of the working paper (PDF page minus 1; the abstract page is unnumbered). Values marked ≈ are read from a chart. All results are real data, in-sample. The paper has no simulation and no out-of-sample test.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Negative skewness of investment currencies comes from sudden unwinding of carry trades when speculators near funding constraints ("liquidity spirals" of Brunnermeier and Pedersen 2008) | Rate differential predicts negative skewness (Table 3); rising signed VIX goes with futures unwinding, higher crash insurance price and carry losses (Table 5) | p. 2-3, 22-24 |
| 2 | Crash risk is partly endogenous: carry gains build positions, which raise future crash risk | Past return z_t predicts lower skewness and "drives out" futures positions | Table 4 col. 2, p. 17-18 |
| 3 | After losses, speculators unwind and buy insurance: insurance price rises while future crash risk falls | Risk reversal predicts lower future skewness (-0.16); past return raises risk reversal (7.87) | Table 4 col. 3, 5; p. 18 |
| 4 | FX under-reacts to interest rate shocks (slow-moving capital); carry trading pushes FX toward fundamentals in the short run | Cumulated excess return rises for 15 quarters after a rate shock and starts below the UIP-implied jump | Fig. 5, 6; p. 19-22 |
| 5 | Funding liquidity risk partly explains the UIP violation | With signed VIX added, the rate differential coefficient is about half that of Table 3 and less significant | Table 8, p. 25 |
| 6 | Common unwinding makes currencies with similar rates co-move | Pairwise FX correlation falls with the absolute rate differential, with controls | Table 9, p. 28-29 |
| 7 | Crash risk may deter speculators from taking positions large enough to enforce UIP | Stated as a possibility, no direct test | p. 3, 12 |

**Caveats raised by the authors**
- Possible peso problem in realised skewness; risk reversals are immune to it (p. 5, footnote 3).
- CFTC data imperfect: noisy trader classification, most FX liquidity is in OTC forwards (p. 9).
- A fall in risk reversals under rising VIX may be a higher insurance price or a higher objective crash probability (p. 5).
- Long-run over-reaction (bubble) cannot be ruled out: long-run VAR conclusions depend on specification and lag length (p. 4, 20-22).
- Futures link to rate differentials only marginally significant (p. 14).
- Bivariate correlation of risk reversal and skewness is positive; the negative sign appears only with controls (p. 18).

**Ruled out**
- Cross-country fundamental differences: time series tests use country fixed effects (p. 12).
- Co-movement controls: correlated monetary policy, pair fixed effects (e.g. CAD-AUD mining), common FX factor (p. 28).
- VIX is not mechanically linked to FX: it comes from equity options (p. 5).

## 2. Strategy, brick by brick

Most tests are vs USD, not the cross pairs investors trade (p. 8). Only Tables 2 and 7 use a portfolio.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | AUD, CAD, JPY, NZD, NOK, CHF, GBP, EUR (DEM before 1999), vs USD | p. 7 |
| Period | Quarterly 1986-2006; weekly 1992-2006; risk reversals 1998-2006; VIX regressions 1990-2006 | Tables 1-9 |
| Signal | Rank by 3-month interbank rate | p. 7, 11 |
| Entry | Long the k highest-rate currencies, short the k lowest, k = 1, 2, 3 | p. 11 |
| Exit | At the next rebalance. No stop | p. 11 |
| Horizon | One week or one quarter | Table 2 |
| Sizing | Equal weight per currency. No volatility scaling | p. 11 |
| Rebalancing | Start of each week or quarter | p. 11 |
| Costs | None. Results gross | Not stated in paper |

**Rule** (p. 8, 11). Excess return of a long foreign currency position funded in USD:

$$z_{t+1} = (i^*_t - i_t) - \Delta s_{t+1}$$

with s the log of foreign currency units per USD. Portfolio return: equal-weighted average of z over the k highest-rate currencies minus over the k lowest.

**Data provenance**

| Series | Source | Note | Where |
| --- | --- | --- | --- |
| Spot FX, 3-month interbank rates | Datastream, daily | EUR spliced with DEM and German 3-month rate before 1/1/1999 | p. 7 |
| USD rate | Eurodollar LIBOR | | p. 7 |
| Speculator positions | CFTC, non-commercial net (long minus short) / non-commercial open interest; last report of each quarter | From 1986 for CAD, JPY, CHF, GBP, EUR only | p. 8 |
| Crash insurance price | JPMorgan Chase quotes, 25 delta 1-month risk reversals | 1998-2006 | p. 9 |
| Funding liquidity | CBOE VIX; TED = 3-month USD LIBOR minus 3-month T-bill | | p. 23 |

## 3. Results

**Aggregate** (real data, in-sample, gross)

| Metric | Value | Where |
| --- | --- | --- |
| Skewness vs average rate differential, cross-section of 8 currencies | R² 81% | Fig. 2A, p. 4 |
| Carry portfolios, annualised Sharpe | 0.592 (2x2 weekly) to 0.784 (3x3 quarterly) | Table 2 |
| Carry portfolios, skewness | -0.537 (2x2 weekly) to -0.977 (3x3 quarterly) | Table 2 |
| Carry portfolios, kurtosis; mean quarterly return | 0.661 to 2.851; 0.016 to 0.022 | Table 2 |
| US stock market (CRSP VW), same periods | skewness -0.41 weekly, -0.88 quarterly; Sharpe 0.44, 0.41 | p. 12 |
| Rate differential on next-quarter z | 2.17 (SE 0.78) | Table 3 |
| Rate differential on next-quarter skewness | -23.92 (SE 3.87) | Table 3 |
| Signed ΔVIX on weekly z, same week | -0.43 (SE 0.11) | Table 5 |
| ΔVIX on 3x3 portfolio weekly return | -0.94 (SE 0.25) same week; -0.07 (SE 0.23) next week | Table 7 |

**By sub-group** (Table 1, quarterly means)
- Highest differential and excess return: NZD (0.009, 0.013). Lowest: JPY (-0.007, -0.004).
- Most negative skewness: AUD -0.322, NZD -0.297. Most positive: JPY 0.318.
- Speculators net short JPY (-0.097) and CHF (-0.067), net long CAD, GBP, EUR. No CFTC data for AUD, NZD, NOK.
- Risk reversals: JPY 1.059 highest, NZD -0.467 lowest.
- Low-rate currencies: long right tail (Fig. 3).

**Horizon and parameters**
- FX return coefficient on the rate differential declines from 2.17 at t+1 to -0.04 at t+10 (Table 3).
- Skewness coefficient stays between -21 and -24 to t+7, then -11.14 at t+10, still significant (Table 3).
- Futures coefficient: 8.26 at t+1, -0.96 at t+10, marginal significance (Table 3).
- Adding more currencies does not reduce skewness or kurtosis (Table 2, p. 11).
- Signed VIX level predicts carry returns from t+2 to about t+8, not t+1; signed TED only at t+6 and t+7 (Table 8, p. 25).

**Over time**
- USD/JPY fell sharply on 7-8 October 1998, without news; the authors separate it from LTCM and from the Fed cut of 15 October (Fig. 1, footnote 1).
- After a rate shock, the differential keeps rising ≈4 quarters, then reverts (Fig. 5).
- Cumulated excess return after a rate shock ≈0.048 at 15 quarters, still rising (Fig. 5). UIP-implied level ≈0.027; VAR path crosses it ≈quarter 8 (Fig. 6).
- Skewness response ≈-0.075 on impact, back near zero ≈15 quarters (Fig. 5).

**Link to other strategies**
- Parallel drawn with the equity premium and short index options; no factor regression (p. 12).

**Where it does not work**
- Risk reversals on the rate differential: -15.51 (SE 29.20), -30.70 (SE 25.91), not significant (Table 4).
- Signed TED: not significant same week; significant only for next-week risk reversal (-25.05, SE 13.89) and marginally next-week return (Table 6, p. 24).
- Rate differential with signed VIX: 1.35 (SE 1.36) at t+1, not significant (Table 8).
- With signed TED the rate differential coefficient is not reduced: 2.58 at t+1 vs 2.17 in Table 3 (Table 8 vs Table 3; comparison computed, samples differ).
- Weekly 2x2 portfolio has the lowest Sharpe, 0.592 (Table 2).

**Inconsistencies in the source**
- Figure 1 caption says 1998 to 2000; the axis runs 1996 to 2000 (p. 2).
- p. 4 calls AUD and NZD the currencies with "the second-highest" differentials; Table 1 and p. 10 give NZD the highest (0.009).
- p. 29: a 1% lower differential raises FX correlation by "more than 0.1"; column (2) of Table 9 gives -6.62, i.e. 0.066 (computed).
- p. 24 calls the TED effect on next-week risk reversal significant (t ≈ 1.80, computed) and on next-week return marginal (t ≈ 1.84, computed): the weaker t-stat is called significant.
- Table 1 and p. 8 give no CFTC data for AUD, yet Tables 4-6 include AUD in regressions with futures positions (Table 5 note: six currencies "since 1992").

**Questions (not proven inconsistencies)**
- Table 6 control coefficients, standard errors and R² (Futures_{t-1}, RiskRev_{t-1}) are identical to Table 5. Possible copy across tables; not checkable from the PDF.
- Table 9: coefficient of 2.54 on the average pairwise correlation. Is this the intended scale?
- p. 4 says skewness uses "overlapping" quarterly windows; p. 8 and Table 3 use within-quarter skewness. Which one is used in the regressions?
- Is USD a candidate leg in the k long / k short portfolio, or only the eight currencies? Not stated.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Futures positions at end of quarter t strongly related to z_t "(not reported in the table)" | p. 17 |
| Risk reversal and skewness bivariate correlation positive (untabulated) | p. 18 |
| Dropping Futures and Skewness from the VAR has little effect on cumulated returns | p. 21 |
| Diversified equity indexes more negatively skewed than single stocks | p. 12 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Carry signal]], [[Long-short portfolio weighting]]: Long top k, short bottom k currencies by 3-month rate, equal weight | technique | signal | Look at carry vs returns at portfolio level | p. 11 |
| 2 | Realised skewness of daily FX changes within each quarter | technique | evaluation | Measures crash risk | p. 8 |
| 3 | 25 delta 1-month risk reversal as price of crash insurance | technique | risk | Risk-neutral skewness; immune to peso problem | p. 9, footnote 3 |
| 4 | CFTC non-commercial net position / non-commercial open interest | technique | economic intuition | Proxy for speculator carry positions | p. 8 |
| 5 | [[Volatility regime filter]]: ΔVIX or ΔTED times sign of the rate differential | technique | risk | VIX and TED do not flip sign with trade direction | p. 23 |
| 6 | [[Volatility regime filter]]: Signed VIX level as predictor of carry returns 2-8 quarters ahead | technique | signal | Contemporaneous losses reflect a risk premium change | Table 8, p. 25 |
| 7 | Kernel densities of returns split by rate differential bucket | technique | evaluation | Shows crash risk visually | Fig. 3, p. 15 |
| 8 | VAR impulse response vs UIP-implied jump | technique | evaluation | Separates under-reaction from over-reaction | p. 20-22 |
| 9 | Pairwise FX correlation on absolute rate differential with fixed effects | technique | evaluation | Tests co-movement from common unwinding | Table 9 |
| 10 | Carry skewness is not diversified away by adding currencies | principle | risk | Crashes correlated across countries, common liquidity factor | p. 11, 25 |

## 6. Regime observations

- Rising VIX: positions cut, insurance price up, carry losses (Table 5). VIX spikes cited: 1998, summer 2007 (p. 23).
- High signed VIX: higher carry returns some quarters later (Table 8).
- One short quote: carry currencies "go up by the stairs and down by the elevator" (p. 4, [NBER w14473](http://www.nber.org/papers/w14473)).

## 7. Acknowledged limits

- See caveats in section 1. Also: analysis vs USD, not the cross pairs traders use (p. 8).

## 8. Not addressed

- Transaction costs, bid-ask, financing frictions, slippage.
- Drawdowns, worst loss, recovery time of the carry portfolio.
- Capacity, leverage, margin levels.
- Out-of-sample test; sample stops in 2006 though the paper is dated November 2008.
- A traded rule using VIX or risk reversals as a filter.
