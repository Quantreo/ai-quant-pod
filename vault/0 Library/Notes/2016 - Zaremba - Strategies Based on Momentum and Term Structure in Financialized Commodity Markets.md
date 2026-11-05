---
type: reading-note
source: paper
title: Strategies Based on Momentum and Term Structure in Financialized Commodity Markets
authors: Zaremba
affiliations: Poznan University of Economics
year: 2016
venue: Business and Economics Research Journal 7(1), 31-46
doi: 10.20409/berj.2016116803
pdf: "[[2016 - Zaremba - Strategies Based on Momentum and Term Structure in Financialized Commodity Markets.pdf]]"
version: published
tier: 1
read: full
tags: [carry, commodities, monthly]
date: 2026-10-25
---

# Momentum and term structure in financialized commodity markets (Zaremba 2016)

## Summary

- **Finding**: 26 commodity futures, 1987-2013. Term structure long-short earns 0.92% a month (t = 4.14, Sharpe 0.80); 12-month momentum 0.74% (t = 2.79). Excess returns, no costs.
- **Mechanism**: hedgers pay speculators for insurance; more speculators dilute the premium. Momentum fades when speculators crowd in and follow the same signals. Both are hypotheses, not tested directly.
- **Where it works best**: markets with a low non-commercial share of open interest. Term structure 1.43% a month there vs 0.41% in high-share markets; difference 1.02% (t = 2.18).
- **Weak spots**: momentum difference between the two groups is not significant in any variant. Term structure difference loses significance on the 1-3 and 1-4 spreads. 1-month momentum is not significant overall (t = 1.38).
- **Main caveats**: no costs, small sample, median split of about 26 markets, mixed CFTC start dates (2011 for Brent). Table 4 Sharpe ratios repeat Table 2.

Page numbers follow the journal pagination (31-46). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Term structure premium is the price of insurance paid by hedgers to speculators (hedging pressure). Short hedgers push futures down (backwardation), long speculators earn the premium. Long speculators in the majority imply contango. | Cited literature only. | p. 32 |
| 2 | More speculators lower the speculator-to-hedger ratio, so the premium per speculator falls. | Term structure returns higher in low-share markets (Tables 2-3). | p. 33, 37-39 |
| 3 | More speculators mean crowding of momentum investors following similar signals, so momentum profits wear out. | Momentum returns higher in low-share markets, not significant (Tables 4-5). | p. 33, 43 |
| 4 | Sources of momentum are unsettled: microstructure, risk management, behavioural biases. | Citations only. | p. 32 |

**Caveats raised by the authors**
- Momentum results are "far from being conclusive", no significance (p. 43).
- Small sample, hard to enlarge because the number of commodities is limited (p. 43).
- No standard measure of financialization; the paper defines its own (p. 35).

**Ruled out**: nothing is ruled out.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 26 commodity futures: agriculture, industrial and precious metals, energy. NYMEX, ICE, CBOT, CME. | p. 34, Table 1 |
| Period | Data January 1986 to December 2013. Returns February 1987 to December 2013. Start dates differ by commodity. | p. 34-35 |
| Signal, term structure | Implied yield between nearest and second nearest contract (Eq. 1). Robustness: first-third and first-fourth. Rank is relative, the sign of the yield does not matter. | p. 34, 36 |
| Signal, momentum | Excess return of the month before formation. Robustness: 3 and 12 months. | p. 34 |
| Conditioning variable | Financialization: non-commercial long + short + spread positions over all reported positions (CFTC), end of previous month (Eq. 2). | p. 35 |
| Entry | Single sort: median split, long top half, short bottom half. Double sort: median split on financialization, then median split on the signal inside each half. | p. 36 |
| Exit | Monthly rebuild. | p. 36 |
| Sizing | Equal weight in each leg. Fully collateralized in a risk-free asset (one-month USD LIBOR). | p. 36 |
| Costs | None stated. | not addressed |
| Data | Returns from S&P-GSCI single-commodity indices (excess and total); fallback Credit Suisse, then JP Morgan and CIBC. USD. Open interest from CFTC. | p. 35 |

**Rule** (Eq. 1, p. 35), with P nearest and distant contract prices, N days to expiry:

$$R_t = [\ln(P_{t,n}) - \ln(P_{t,d})] \times \frac{365}{N_{t,d} - N_{t,n}}$$

Financialization (Eq. 2, p. 35): fin_t = (NCNL_t + NCNS_t + SPR_t) / TR_t.

**Data provenance**: CFTC history starts between 1986 and 2011 by commodity; price history starts between 1986 and 2008 (Table 1, p. 35). Which index source applies to which commodity is not stated.

## 3. Results

Excess returns, per month, gross of costs, real data in-sample, 1987-2013.

**Aggregate**

| Metric | Value | Where |
| --- | --- | --- |
| Term structure 1-2, all markets | 0.92% (t = 4.14), vol 4.00%, Sharpe 0.80 | Table 2 |
| Term structure 1-3 / 1-4, all | 0.97% (t = 4.46) / 0.68% (t = 3.07) | Table 2 |
| Momentum 1m / 3m / 12m, all | 0.39% (t = 1.38) / 0.65% (t = 2.60) / 0.74% (t = 2.79) | Table 4 |
| Term structure 1-2 alpha, three models | 0.88% (t = 3.97), 0.90% (4.00), 0.66% (3.17) | Table 3 |
| Momentum alpha, 12m, three models | 0.72% (t = 2.69), 0.76% (2.80), 0.31% (1.44) | Table 5 |

**By sub-group** (low share = "non-fin", high share = "fin")

| Strategy | Low share | High share | Difference (t) | Where |
| --- | --- | --- | --- | --- |
| Term structure 1-2 | 1.43% | 0.41% | 1.02% (2.18) | Table 2 |
| Term structure 1-3 | 1.02% | 0.53% | 0.49% (1.02) | Table 2 |
| Term structure 1-4 | 0.60% | 0.33% | 0.26% (0.59) | Table 2 |
| Momentum 1m | 0.65% | 0.15% | 0.50% (0.99) | Table 4 |
| Momentum 3m | 0.76% | 0.36% | 0.40% (0.79) | Table 4 |
| Momentum 12m | 0.93% | 0.66% | 0.26% (0.52) | Table 4 |

- Term structure 1-2 alpha of the difference: 0.88% (t = 1.92) index model, 1.07% (t = 2.24) traditional, 1.06% (t = 2.32) fundamental. Bootstrap t: 2.32, 2.64, 2.73 (Table 3).
- High-share term structure alpha is not significant in any model (t = 0.84 to 1.47, Table 3).
- Momentum difference alphas: 0.15% to 0.52%, none significant (Table 5, p. 43).
- Low-share legs are riskier: term structure 1-2 vol 7.12% vs 4.98%, worst month -24.63% vs -18.58%, kurtosis 3.54 (Table 2). Momentum 1m low-share kurtosis 9.83, best month 53.73% (Table 4).
- Factor loadings: term structure 1-2 loads on the TS factor (0.49, t = 6.36) and on GSCI (0.14, t = 3.57). The difference portfolio loads negatively on hedging pressure (-0.77, t = -4.59) (Table 3). Momentum loads on the MOM factor and, for the 1-month version, negatively on TS (-0.25, t = -2.43) (Table 5).

**Horizon and parameters**
- Momentum returns rise with lookback: 0.39%, 0.65%, 0.74% (Table 4).
- Term structure: financialization effect strongest on the nearest spread (p. 37).

**Over time**
- Fig. 2 (log scale): 1-2 spread, one dollar in 1987 ends ≈128 low share, ≈40 all, ≈6 high share. The text gives 134 dollars and 647% (p. 40).
- Fig. 3 (log scale): momentum 1m, ends ≈10 low share, ≈7 all, ≈3 high share. The text gives 9 and 2.12 (p. 41).
- Fig. 1: non-commercial share of open interest rises from 23% (1986) to 45% (2013); natural gas above 50%, rough rice 20% (p. 32-33).
- Sub-period results by year: not shown.

**Link to other strategies**: Both strategies are tested against bond, equity and commodity indexes, Fama-French factors and the TS, MOM, HP factors (Tables 3, 5). Alpha stays positive in all models. Only SMB is significant among the Fama-French factors, loading 0.22 (t = 3.00) on the all-markets 1-2 strategy (Table 3).

**Inconsistencies in the source**
- Table 4 Sharpe ratios (0.80, 0.70, 0.28, 0.42 / 0.86, 0.50, 0.36, 0.20 / 0.59, 0.31, 0.23, 0.11) are identical to Table 2. Mean over volatility in Table 4 gives about 0.27 annualised for 1m all (computed: 0.39 / 5.09 x sqrt(12)).
- Text says momentum returns are "higher than returns in longer formation periods" (p. 40); Table 4 shows 1-month the lowest (0.39% vs 0.74%).
- Fig. 3 caption says term structure strategies; the figure is momentum (p. 41).
- Text calls the index-model difference alpha significant (p. 39); its parametric t is 1.92 (Table 3).
- Text says 134 dollars, chart shows ≈128 (p. 40); 2.12 vs ≈3 (p. 41).
- Table 1 labels COMEX as Chicago Mercantile Exchange, with feeder cattle and lean hogs under COMEX (p. 35).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Financialization explains cross-sectional variation in futures returns and could enter a formal pricing model | p. 43 |
| Investors "could benefit" from avoiding financialized markets | p. 43 |
| Speculator share rising lowers the premium per speculator | p. 33 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Carry signal]]: implied yield between nearest and second nearest contract, long top half, short bottom half | technique | signal | Shape of the curve reflects hedging pressure | p. 32, 35-36 |
| 2 | [[Cross-sectional momentum]]: past 1, 3 or 12-month excess return, median split | technique | signal | Standard in the field | p. 34, 36 |
| 3 | [[Momentum crowding filter]]: non-commercial share of open interest as conditioning variable | technique | signal | Crowding of speculators | p. 35 |
| 4 | [[Conditional double sort]]: median split on the conditioning variable, then long-short within each half, difference of halves | technique | evaluation | Small universe, avoids small-sample bias of deciles | p. 36 |
| 5 | Alpha on three factor models, parametric and bootstrap t (no card: standard practice) | principle | evaluation | Not argued | p. 36-37 |

## 6. Regime observations

- Non-commercial share rises over 1986-2013 (Fig. 1). Low-share term structure curve in Fig. 2 stays above the high-share curve throughout (≈ chart).
- Not stated by the authors beyond this.

## 7. Acknowledged limits

- Small sample and small number of commodities (p. 43).
- Momentum results lack statistical significance (p. 43).

## 8. Not addressed

Transaction costs, roll costs, slippage, capacity, number of instruments per leg, sub-period stability, choice of median vs other breakpoints, whether low share is a stable property of a commodity or moves with time, and the relation of results to the post-2005 index flows.
