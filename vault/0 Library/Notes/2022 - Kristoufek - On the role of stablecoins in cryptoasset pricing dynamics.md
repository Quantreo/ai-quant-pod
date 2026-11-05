---
type: reading-note
source: paper
title: On the role of stablecoins in cryptoasset pricing dynamics
authors: Kristoufek
affiliations: Institute of Economic Studies, Faculty of Social Sciences, Charles University; Institute of Information Theory and Automation, Czech Academy of Sciences
year: 2022
venue: Financial Innovation 8:37
doi: 10.1186/s40854-022-00343-8
pdf: "[[2022 - Kristoufek - On the role of stablecoins in cryptoasset pricing dynamics.pdf]]"
version: published (open access)
tier: 1
read: full
tags: [seasonality-flows, crypto, daily]
date: 2026-10-24
---

# Stablecoin supply and crypto prices (Kristoufek 2022)

## Summary

- **Finding**: daily 2015-2020. Stablecoin market cap follows Bitcoin and altcoin market cap, not the reverse: about 80% of a Bitcoin shock and 50% of an altcoin shock pass into stablecoins over ≈ 180 days (p. 13, Fig. 2).
- **Mechanism**: author's reading: stablecoin issuance reflects investor demand to buy crypto after price gains ("demand pull"), not a bubble booster ("supply push"). Conditional on stablecoins being backed (p. 13-14, 19).
- **Where it works best**: the lead from Bitcoin and altcoins to stablecoins shows in the upper quantiles (≈ 0.55 to 0.95) and in extreme events (Fig. 3, Table 5).
- **Weak spots**: 2018-2020 subsample: no cointegration, no Granger causality at 90% (Table 8). In 2017, stablecoin shocks precede short negative moves in Bitcoin and altcoins (Fig. 6).
- **Main caveats**: no trading rule or portfolio returns. Market caps of a coin list chosen in July 2020. Effects from stablecoins to prices are about -4% and short-lived.

Page numbers follow the journal pagination (1 to 26 of article 8:37). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Stablecoin issuance comes after Bitcoin and altcoin gains: rising prices attract investors who buy in through stablecoins | Long-run Granger causality Bitcoin to stablecoins (p = 0.0282); IRFs; quantile and transfer-entropy tests | Table 4, Fig. 2-3, Table 5; p. 13, 19 |
| 2 | No spiral or self-boosting mechanism between stablecoins and other crypto | Flow runs one way, from crypto to stablecoins | p. 15, 19 |
| 3 | Interpretation depends on backing: if stablecoins are unbacked, the same dynamics mean new coins are created to inflate prices | Argument; Tether's backing never fully audited | p. 13-14, 19 |
| 4 | 2017 issuances preceded further corrections before prices resumed, "partially in sync" with Griffin and Shams (2020) | IRF dip from stablecoins to Bitcoin and altcoins in 2017 | Fig. 6; p. 14-15 |

**Caveats raised by the author**
- Reading 2017 as Tether smoothing corrections is "quite a stretch" from the IRFs; not contradicting is not validating (p. 15).
- Post-issuance bounces may come from crypto's own negative first-order autocorrelation rather than the issuance (p. 15).
- Granger causality shows direction of flow, not sign (p. 11).

**Ruled out**
- Stablecoins as the "ignition point" of bull runs (p. 14, 19).
- Stablecoins leading Bitcoin or altcoins in any quantile (Fig. 3, p. 16).

## 2. Strategy, brick by brick

No trading strategy is tested. Bricks below describe the empirical setup.

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 28 stablecoins above 1 million USD market cap on 12 Jul 2020 (24 USD, 2 EUR, 1 CHF, 1 CNY pegs). 14 non-stable cryptoassets: top 10 on 12 Jul 2020 plus "old-timers" (≈ 90% of non-stable market cap) | p. 4, fn 3, fn 5 |
| Period | 6 Mar 2015 to 11 Jul 2020, 1,955 daily observations; subsamples 2017 and 2018-2020 | p. 4, 14-15 |
| Signal | Log market capitalisation of three baskets: Bitcoin, altcoins, stablecoins | p. 4-6 |
| Horizon | Daily data; IRFs up to 180 days | p. 11 |
| Data and tools | CoinMarketCap series, Cryptoslate for stablecoin list; ADF, Johansen trace and Lmax, VECM with 2 lags and unrestricted trend, Toda-Yamamoto long-run causality, quantile Granger causality (Jeong et al. 2012), Rényi transfer entropy | p. 4, 8-9, 15-17 |
| Entry, exit, sizing, costs | Not applicable | |

**Rule**: none. Model (Eq. 1, p. 8): Δx(t) = Σ Γ(i) Δx(t-i) + αβ'x(t-1) + π + δt + ε(t), x = log market caps of stablecoins, Bitcoin, altcoins.

**Data provenance**
- Market cap used instead of price because stablecoin prices are nearly constant; market cap then measures stablecoin supply (p. 5-6).
- Total crypto market cap series rejected for "unreasonable capitalization jumps" (fn 5).
- Stablecoin share of total crypto market cap rose from below 0.0001% to ≈ 4% (above 11 billion USD) by July 2020 (p. 6).
- Dataset attached to the article (p. 24).

## 3. Results

All results are real data, in-sample. No returns or costs.

**Aggregate**
- One cointegrating vector (trace p = 0.0029, Lmax p = 0.0021, unrestricted trend) (Table 3).
- Short-run Granger (Table 4): stablecoins to Bitcoin p = 0.0493; stablecoins to altcoins p = 0.0252; altcoins to Bitcoin p = 0.0110; nothing to stablecoins.
- Long-run Granger (Table 4): Bitcoin to stablecoins p = 0.0282; altcoins to Bitcoin p = 0.0311; stablecoins to altcoins p = 0.0631.
- IRFs (Fig. 2): Bitcoin to altcoins ≈ 0.6 and persistent; Bitcoin to stablecoins rises to ≈ 0.8 after 180 days; altcoins to stablecoins ≈ 0.5.
- Short run (Fig. 5): stablecoins to Bitcoin and to altcoins dip to ≈ -0.04 within days; altcoins to Bitcoin ≈ -0.07 at day 1.

**By sub-group**
- Correlation of daily log changes: stablecoins with Bitcoin -0.0261, with altcoins -0.0006; Bitcoin with altcoins 0.6111 (p. 6).
- Stablecoin log changes: skew 7.76, excess kurtosis 104.9, max 0.6842 (Table 1).
- Alternative baskets (top 5 altcoins, USDT only, stablecoins above 100 million USD): "qualitatively the same", not shown (p. 17-18).

**Horizon and parameters**
- Quantile Granger causality (Fig. 3): Bitcoin to stablecoins and altcoins to stablecoins significant for quantiles ≈ 0.55 to 0.95; Bitcoin to stablecoins also ≈ 0.2 to 0.3.
- Rényi transfer entropy (Table 5): flows to stablecoins significant at q = 0.2 and 0.5 (p 0.0233 to 0.05); no flow from stablecoins significant at any q.

**Over time**
- 2017 (Table 7, Fig. 6): short-run stablecoins to Bitcoin (p = 0.0006) and to altcoins (p = 0.0016), negative sign; ≈ -0.3 dip within days.
- 2018-2020 (Table 8, Fig. 7): no cointegration; no Granger causality even at 90%; weak but significant IRF from Bitcoin and altcoins to stablecoins.

**Link to other strategies**
- Not addressed.

**Inconsistencies in the source**
- p. 4 counts 28 stablecoins; Table 1 caption says "the 23 stablecoins listed in the text".
- p. 11 calls the Bitcoin-to-stablecoins transmission "almost perfect (the effect close to 1)"; p. 13 says approximately 80%.
- p. 14 says that in 2017 "altcoins Granger-cause Bitcoin in the long term, which is different" from the full sample. Full sample already has it (p = 0.0311, Table 4); in 2017 it is p = 0.0556 (Table 7).
- Table 7 (one year of data) reports long-term df = [3, 1355].
- Fig. 3 caption calls the critical value the 95th percentile of the standard normal, "approximately 1.96".

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results with alternative baskets are qualitatively the same; tables "available upon request" | p. 17-18 |
| All IRF orderings tell the same story | p. 11 |
| Restricted-trend model gives the same conclusions | fn 6 |
| Griffin and Shams (2020) test of "demand pull" is methodologically weak | p. 18 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Stablecoin market cap as crypto "money supply" | principle | signal | Prices of stablecoins are nearly constant; supply carries the information | p. 5-6 |
| 2 | Market-cap index of a coin basket as a supply-adjusted price | technique | universe | Parallel to adjusted prices | p. 4-5 |
| 3 | VECM plus Toda-Yamamoto for short- and long-run causality | technique | evaluation | Series have unit roots and are cointegrated | p. 8-10 |
| 4 | Quantile-specific Granger causality | technique | evaluation | Heavy tails; dependence may sit in the tails | p. 15-16 |
| 5 | Rényi transfer entropy with q below 1 | technique | evaluation | Emphasises rare events in information flow | p. 17 |

## 6. Regime observations

- 2017 bull run: stablecoin issuance followed by short corrections, then trend resumes (Fig. 6, p. 14-15).
- 2018-2020: links much weaker, no causality (Table 8, p. 15).
- Stablecoin market cap grew from under 10 million to ≈ 2 billion USD between 2017 and 2018 (p. 6).

## 7. Acknowledged limits

- Backing of Tether unknown, which changes the interpretation (p. 13).
- Short 2017 sample gives wide confidence bands (p. 14).

## 8. Not addressed

- Any trading rule or portfolio built on stablecoin flows.
- Exchange-level flows or individual issuance events.
- Out-of-sample prediction.
- Effect of the coin list being chosen on 12 Jul 2020, the end date.
