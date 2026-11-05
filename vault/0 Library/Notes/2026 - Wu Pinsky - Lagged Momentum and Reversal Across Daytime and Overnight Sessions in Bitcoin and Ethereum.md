---
type: reading-note
source: paper
title: On the Performance of Lagged Momentum and Reversal Strategies Across Daytime and Overnight Sessions in Bitcoin and Ethereum Cryptocurrencies
authors: Wu, Pinsky
affiliations: Department of Mathematical Finance, Questrom School of Business, Boston University; Department of Computer Science, Metropolitan College, Boston University
year: 2026
venue: Journal of Risk and Financial Management 19(9), 692
doi: 10.3390/jrfm19090692
pdf: "[[2026 - Wu Pinsky - Lagged Momentum and Reversal Across Daytime and Overnight Sessions in Bitcoin and Ethereum.pdf]]"
version: published (open access), 6 September 2026
tier: 1
read: full
tags: [reversal, crypto, intraday]
date: 2026-10-24
---

# Day and night session rules for BTC and ETH (Wu, Pinsky 2026)

## Summary

- **Finding**: hourly Kraken 2016-2025, 12h/12h sessions. Full-sample best: BTC reversal in both sessions (day 08:00 UTC), ETH long overnight plus daytime reversal (day 05:00 UTC). Gross wealth ratios vs buy-and-hold 4.70 and 57.69 (Tables 8, 11).
- **Mechanism**: authors suggest the boundaries may match regional activity (Asia to Europe at 05:00, Europe at 08:00); "plausible but not causal"; liquidity, order flow, investor mix are untested rivals (p. 25-26).
- **Where it works best**: ETH Long/Reversal: chosen again on 2016-2020 alone, beats buy-and-hold out of sample 2021-2025 (wealth ratio 13.4 gross, 6.4 at 2 bps). Daytime reversal significant in both halves for both coins (Tables 10, 13).
- **Weak spots**: paired tests never significant; Hansen SPA p = 0.66 to 0.996 over 300 combinations. BTC holdout-selected rule (11:00 Momentum/Long) loses 29.1% and reaches 23.6% of buy-and-hold (Tables 11-13).
- **Main caveats**: costs of only 0-2 bps per turnover; break-even ≈ 2.1 bps (BTC), 5.6 bps (ETH). No slippage, spread, shorting or funding costs. Boundary and rule selected on terminal wealth; one exchange.

Page numbers follow the journal pagination (1 to 31 of article 692). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | BTC returns show conditional reversal within each 12h session type | Negative-minus-positive lag contrast: night 23.89 bps, day 27.71 bps per session (Holm p 0.003, 0.002) | Table 10 |
| 2 | ETH combines a positive overnight drift with daytime reversal | Night mean 24.15 bps; day reversal contrast 42.79 bps | Table 10 |
| 3 | The selected start hours may reflect the global distribution of activity | Cited time-of-day evidence (Baur et al. 2019; Wang et al. 2020); not tested | p. 25-26 |

**Caveats raised by the authors**
- Signal predictability does not translate into significant outperformance vs buy-and-hold; test power is low (would need ≈ two decades for ETH) (p. 22-23).
- BTC optimum is boundary-sensitive: best wealth 95,015 at 08:00 vs 31,648 at 07:00 and 20,226 at 09:00 (p. 15-16).
- Comparison is not exposure-matched: rules can be short or flat while buy-and-hold is always long (p. 26).
- ETH nighttime mean weakens in 2021-2025 (7.37 bps, 10% level) (Table 10).

**Ruled out**
- A single universal "nighttime effect" across the two coins (p. 2, 16).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | BTCUSD and ETHUSD on Kraken | p. 5 |
| Period | 1 Jan 2016 to 31 Dec 2025, 87,672 hourly closes, 3,652 days, no missing hours | p. 5 |
| Signal | Same-session lagged return sign: Momentum = sign(R(t-1,s)), Reversal = -sign(R(t-1,s)); also Cash, Long, Short | Eq. 5, p. 7 |
| Entry | At the start of each 12h session, position in {-1, 0, 1} | p. 7 |
| Exit | End of the session | p. 7 |
| Horizon | 12 hours | p. 6 |
| Sizing | Unit position, no leverage | p. 7 |
| Portfolio | One coin at a time; 25 night-day rule pairs x 12 boundaries = 300 candidates | p. 11 |
| Rebalancing | Twice a day | p. 6-7 |
| Costs | 0, 1, 2 bps per unit of turnover; flip long to short counts 2 | Eq. 17-18, p. 12 |
| Data and tools | Kraken official historical archive; stationary block bootstrap (5,000 draws, 7-day blocks); Holm adjustment; Hansen SPA | p. 5, 13-14 |

**Rule**: BTC: day 08:00-20:00 UTC, night 20:00-08:00 UTC; in each session take the opposite sign of that session's previous-day return. ETH: night 17:00-05:00 UTC always long; day 05:00-17:00 UTC take the opposite sign of the previous day-session return (p. 16).

**Data provenance**
- Single exchange (Kraken); no cross-venue merge or interpolation (p. 5).
- Hourly close-to-close returns; execution assumed at the session-boundary close (p. 5, 26).

## 3. Results

Results are real data. Full-sample selection is in-sample; Table 13 is a chronological holdout (select on 2016-2020, test on 2021-2025).

**Aggregate** (Tables 8, 9, 11)
- BTC Reversal/Reversal: terminal wealth 95,015 at 0 bps vs 20,216 buy-and-hold; CAGR ≈ 98.5% vs 70.0%. At 2 bps: 21,258 vs 20,212 (ratio 1.05).
- ETH Long/Reversal: 18,443,599 at 0 bps, 4,255,551 at 2 bps; CAGR ≈ 236.2% vs 124.1%.
- Risk at 0 bps (Table 9): BTC Rev/Rev MDD -75.1%, Sharpe 1.4, vol 67.5% vs buy-and-hold -83.6%, 1.1, 67.2%. ETH Long/Rev MDD -73.0%, Sharpe 1.7, vol 94.9% vs -94.0%, 1.3, 95.3%.
- Paired log differential (Table 11): BTC 4.24 bps a day (0 bps) to 0.14 (2 bps); ETH 11.10 to 7.09; all confidence intervals include zero.

**By sub-group**
- Only ETH Long/Reversal beats ETH buy-and-hold among 24 active rules (p. 16).
- Single-session static rules (Table 9): Long-only night BTC Sharpe 0.8, ETH 1.3; Long-only day ETH Sharpe 0.5.

**Horizon and parameters**
- ETH result holds for 05:00 to 08:00 day starts (same best rule); BTC optimum collapses one hour either side (p. 16).
- Break-even one-way cost ≈ 2.1 bps (BTC), ≈ 5.6 bps (ETH), by linear extrapolation (p. 26).

**Over time**
- BTC Rev/Rev vs buy-and-hold: 2016-2020 wealth ratio 0.38 (0 bps) to 0.18 (2 bps); 2021-2025 12.64 to 5.90 (Table 11).
- ETH Long/Rev: 2016-2020 ratio 4.30 to 2.07; positive in 2021-2025 too.
- Holdout (Table 13): BTC 11:00 Momentum/Long ends at 70.9 vs 300.8 (0 bps); ETH 05:00 Long/Reversal ends at 5,483 vs 409 (0 bps), 2,625 vs 408 (2 bps).
- Yearly (Figs. 4-5): BTC Rev/Rev keeps a positive Sharpe in 2018 and 2022 when buy-and-hold is negative, but has deeper drawdowns in 2016, 2017, 2021.

**Link to other strategies**
- ETF transfer, 2025 only (Tables 14-15): IBIT Rev/Rev 194.5 vs 93.6 buy-and-hold; ETHA Long/Rev 357.0 vs 88.8; sessions redefined as Nasdaq close-to-open and open-to-close. Exploratory.

**Inconsistencies in the source**
- p. 11 says transaction costs "are introduced separately in Section 3.3"; Section 3.3 defines sessions and costs are in Section 4.4.
- p. 8 says the illustrative wealth values "are not part of the empirical results presented in Section 4"; the empirical results are in Section 5.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| 05:00 and 08:00 UTC boundaries line up with Asian-European activity shifts | p. 25 |
| Short positions would need a derivatives or margin account with extra constraints | p. 26 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Split the 24h crypto day into two 12h sessions and test every boundary | technique | horizon | No official open or close in crypto; boundary is an empirical choice. Card [[Overnight and intraday return momentum]] | p. 4-5, 11 |
| 2 | Same-session lagged sign as signal (momentum or reversal) | technique | signal | Parameter-free, uses only past same-session return. Card [[Overnight and intraday return momentum]] | p. 7 |
| 3 | Conditional contrast E[r given lag < 0] minus E[r given lag > 0] with block bootstrap | technique | evaluation | Tests the mechanism separately from strategy P&L. Card [[Mean reversion existence test]] | p. 13-14 |
| 4 | Hansen SPA over the full search universe | technique | evaluation | Accounts for search over 300 combinations. Card [[Multiple testing adjustment]] | p. 14 |
| 5 | Chronological holdout: select on first half, freeze, test on second | technique | evaluation | Separates selection from evaluation. Card [[Chronological holdout test]] | p. 13, 24 |
| 6 | Paired daily log differential vs benchmark (sums to log wealth ratio) | technique | evaluation | Links the test to terminal wealth. Card [[Always-long benchmark comparison]] | Eq. 26-27 |

## 6. Regime observations

- Yearly volatility peaks 2017-2018 and 2021, lowest in 2023 (≈ Fig. 3).
- BTC reversal advantage concentrates in bear years (2018, 2022); BTC rule underperforms in the 2016-2020 trending half (p. 19-20, Table 11).
- ETH overnight drift fades in 2021-2025 (Table 10).

## 7. Acknowledged limits

- Costs exclude spread, slippage, impact, borrowing, funding, taxes (p. 12, 26).
- Kraken only; cross-exchange replication untested (p. 26).
- No volume or liquidity controls (p. 25).

## 8. Not addressed

- Results on other coins.
- Execution at a price other than the hourly close.
- Perpetual futures implementation of the short side.
