---
type: reading-note
source: paper
title: Perpetual Futures Pricing
authors: Ackerer, Hugonnier, Jermann
affiliations: EPFL and Swissblock Technologies AG; EPFL and Swiss Finance Institute; The Wharton School, University of Pennsylvania, and NBER
year: 2024
venue: NBER Working Paper 32936
doi: 10.3386/w32936
pdf: "[[2024 - Ackerer Hugonnier Jermann - Perpetual Futures Pricing.pdf]]"
version: NBER working paper, September 2024 (merges two 2023 papers with the same title; not peer-reviewed per its cover page)
tier: 1
read: full
tags: [carry, crypto, daily]
date: 2026-10-24
---

# No-arbitrage price of perpetual futures (Ackerer, Hugonnier, Jermann 2024)

## Summary

- **Finding**: theory only. The no-arbitrage perpetual futures price is the risk-neutral expected spot at a random time set by the funding rule; with constant rates, f/x = (κ - ι)(1 + rb) / (rb - ra + κ(1 + rb)) (Theorem 1, Prop. 1).
- **Mechanism**: funding payments (premium κ(f - x) plus interest ιx) replace expiry convergence; the basis sign follows the interest spread δ = ra - rb, its size shrinks as κ grows (p. 7-12).
- **Where it works best**: setting ι = (ra - rb)/(1 + rb) makes the perpetual equal spot at all times and replicable by a cash-and-carry in the two currencies (Corollary 1, 3).
- **Weak spots**: no empirical test of the formulas on market prices. Quanto prices need a model of exchange rates (p. 23).
- **Main caveats**: frictionless markets, free currency exchange, predictable funding, constant parameters for closed forms. Demand-driven deviations of the basis are outside the model.

Page numbers follow the printed pagination of the working paper (1 to 29 for the main text). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Funding payment κ(f - x) works like mean reversion: when f > x, longs pay, shorts become attractive, f falls | Argument | p. 7-8 |
| 2 | The perpetual price equals the expected spot at a random time θ; with constant κ and ι = 0, θ is geometric (discrete) or exponential (continuous) with mean 1/κ | Theorem 1, Theorem 3 | p. 9, 19 |
| 3 | Basis sign is driven by the interest spread: f > x when ra > rb, f < x when ra < rb; deviation grows with the spread and falls with κ | Prop. 1, Fig. 2 | p. 10-12 |
| 4 | With the right interest factor the perpetual equals spot and is replicable by borrowing a and lending b | Corollaries 1-4 and proofs | p. 12, 15, 19, 21, 31 |

**Caveats raised by the authors**
- No-bubble and integrability conditions cannot be relaxed (p. 9-10).
- Quanto pricing requires a joint model of the two exchange rates (p. 23).

**Ruled out**
- He et al. (2022) original formula x·κ/(κ - ra): its cash flow specification is inconsistent with costless entry unless ra = 0 (Appendix B).

## 2. Strategy, brick by brick

No trading strategy is tested. The paper prices contracts.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | Linear, inverse, quanto perpetuals; everlasting options | p. 2-4, 20-28 |
| Signal | Not applicable. Basis f - x and funding are model outputs | |
| Funding | Premium κ(f - x) plus interest ι·x, paid each period (8h on most platforms); variant with mark price at period end handled by rescaling (κ, ι) by (1 + ra)/(1 + rb) | p. 2, 7-8, 12-13 |
| Costs | Not modelled | |
| Data | Figure 1 only: daily BTC perpetual volumes Jan 2019 to Dec 2023 and exchange shares | Fig. 1 |

**Rule**: none. Key formulas:
- Linear, discrete, constant parameters (Eq. 12, p. 10): f = (κ - ι)(1 + rb) / (rb - ra + κ(1 + rb)) · x.
- Linear, continuous (Prop. 3, p. 19): f = (κ - ι)/(κ + rb - ra) · x.
- Spot-equal interest factor: ι = (ra - rb)/(1 + rb) discrete; ι = ra - rb continuous (Corollaries 1, 3).
- Inverse, continuous (Prop. 4, p. 21): fI = (κI + ra - rb)/(κI - ιI) · x.
- Quanto in Black-Scholes (Prop. 5, p. 24): fq = (κ - ι) z / (rc - σx'σz - ra + κ).

**Data provenance**
- Not applicable beyond Fig. 1 (source of volumes not named).

## 3. Results

All results are theory or numerical illustrations inside the model. No real-data test.

**Aggregate**
- Fig. 2 (ι = 0, annual rates of 0, 5%, 10% converted to 8h periods): f/x between ≈ 0.9995 and ≈ 1.0005 for κ from 0.2 to 1; deviation shrinks as κ rises.
- Fig. 3: same picture for inverse contracts.
- Fig. 4: everlasting call with κ = K = 1 has price and delta close to a European call with maturity 1/κ.

**By sub-group**
- Inverse price rises with the interest factor, linear price falls with it; this comes from ι applying to x* in one case and x in the other (p. 16).

**Horizon and parameters**
- κ → ∞ drives f to x (Props. 1-5).

**Over time** (≈ Fig. 1, real data, descriptive)
- Linear BTC perpetual volume grows from near zero in 2019 to frequent days of ≈ 50 billion USD from 2021; inverse volume peaks in 2021 then falls.
- Average share of open interest: Binance ≈ 36%, Bybit ≈ 24%; share of volume: BitMEX ≈ 43%.
- H1 2023: perpetuals are 75% of the 27 billion USD daily BTC futures volume and 94% of the 8 billion USD open interest (p. 4).

**Link to other strategies**
- Cites empirical work on crypto carry trades (Schmeling, Schrimpf, Todorov 2022; Christin et al. 2023), not used (p. 5).

**Inconsistencies in the source**
- p. 12 says the futures price is "below the spot when δ > 0"; the same sentence says above the spot if δ > 0. Fig. 2 shows below for δ < 0.
- p. 12 calls δ < 0 "contango" while the paragraph and Fig. 2 put the futures below spot in that case.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Perpetuals will "soon find traction" in commodities and other asset classes | p. 2 |
| H1 2023 shares of perpetuals in BTC futures volume and open interest (no source given) | p. 4 |
| Fig. 1 data source | Fig. 1 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Perpetual price as expected spot at a random time with mean 1/κ | principle | evaluation | Links perpetuals to standard futures pricing | p. 9, 19 |
| 2 | Fair basis from interest spread and funding premium: f/x = κ(1 + rb)/(κ(1 + rb) - δ) | technique | signal | Closed form, model-free under constant rates | p. 10-11 |
| 3 | Cash-and-carry replication of a perpetual: borrow x/(1 + rb) in a, hold 1/(1 + rb) units of b | technique | portfolio | Replicates the long cash flow when ι is set to the spot-equal value | p. 12, 31 |
| 4 | Rescale (κ, ι) by (1 + ra)/(1 + rb) when funding uses an end-of-period mark price | technique | calibration | Keeps the formulas valid across exchange specifications | p. 12-13 |

## 6. Regime observations

- Not addressed (theory). Fig. 1 shows the 2021 volume peak.

## 7. Acknowledged limits

- Future work: joint multifactor model estimated on observed rates, funding and prices; equilibrium model of exchange-set funding (p. 29).

## 8. Not addressed

- Empirical fit of the formulas to observed basis and funding.
- Funding as a trading signal or carry strategy returns.
- Transaction costs, margin, liquidation risk.
- Exchange counterparty risk.
