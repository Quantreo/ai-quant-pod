---
type: reading-note
source: paper
title: Speculation and lottery-like demand in cryptocurrency markets
authors: Grobys, Junttila
affiliations: University of Vaasa, School of Accounting and Finance; University of Jyväskylä, School of Business and Economics
year: 2021
venue: Journal of International Financial Markets, Institutions and Money 71, 101289
doi: 10.1016/j.intfin.2021.101289
pdf: "[[2021 - Grobys Junttila - Speculation and lottery-like demand in cryptocurrency markets.pdf]]"
version: published (open access)
tier: 1
read: full
tags: [low-vol, crypto, weekly]
date: 2026-10-24
---

# Lottery demand and the MAX effect in crypto (Grobys, Junttila 2021)

## Summary

- **Finding**: on 20 large coins, 2016-2019, the high-MAX minus low-MAX quintile earns -1.54% a week (bootstrap t = -2.68), -1.75% after Bitcoin adjustment. Gross (Tables 1, A3).
- **Mechanism**: investors pay up for coins with extreme positive daily returns (lottery-like demand), so those coins earn less next week. Borrowed from equity MAX literature, not tested directly (p. 3, 11).
- **Where it works best**: skipping one day before formation: -1.82% raw, -2.14% Bitcoin-adjusted a week (Tables 3, A4). Low-MAX quintile earns 1.33% to 1.65% a week.
- **Weak spots**: with standard t-statistics the raw spread is not significant (t = -1.57); Newey-West with one lag gives -1.89 (Table A8). Quintiles hold four coins each.
- **Main caveats**: no costs; shorting "constrained", authors suggest long-only low-MAX but leave it untested. Universe fixed on 2 Jan 2016; many coins fall below rank 100 by 2019.

Page numbers follow the journal pagination (1 to 15 of article 101289). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Investors find coins with high past payoffs desirable and pay more for them, so these coins earn lower future returns | Negative H-L spread; parallels Bali et al. (2011) in equities | p. 3, 11 |
| 2 | Crypto markets are more speculative than a medium of exchange, so lottery demand should be present | Literature on bubbles and speculation (Baur et al. 2018) | p. 2 |
| 3 | Past MAX is a rational predictor of future MAX | Transition matrix: 33.94% of high-MAX coins stay high next week, 27.05% of low stay low, against 20% under randomness | Table 5; p. 8 |
| 4 | Lottery demand is priced in the cross-section | Cross-sectional premium on MAX beta 3.47, bootstrap t = 3.83; R² 61% | p. 9 |

**Caveats raised by the authors**
- Short-selling constraints mean the strategy could only be run long-only (p. 11).
- Lottery-prone investors may focus on small coins, not covered here (p. 11-12).

**Ruled out**
- Tail observations driving the result: trimming 2.5% per tail widens the spread to -1.89% (Table 1, p. 7).
- Bitcoin market exposure: alpha -1.75%, beta 0.16 not significant (Table A3).
- Microstructure: skipping the latest day keeps the effect (Tables 3, A4).
- Survivorship: coins chosen by market cap at the start date (p. 9).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | 20 coins ranked 2 to 21 by market cap on 2 Jan 2016 (Bitcoin excluded, used as market factor). YbCoin replaced by MonaCoin for missing data. | p. 4, fn 4, Table A2 |
| Period | 1 Jan 2016 to 31 Dec 2019; 1,463 daily, 209 weekly observations | p. 4 |
| Signal | MAX = highest daily log return over the past seven days | p. 6 |
| Entry | Sort into quintiles at the start of each week | p. 6 |
| Exit | Hold one week | p. 6 |
| Horizon | Weekly | p. 6 |
| Sizing | Equal weight | p. 10 |
| Portfolio | H-L: long high-MAX quintile, short low-MAX quintile (four coins per leg) | p. 6 |
| Rebalancing | Weekly | p. 6 |
| Costs | Not stated by the authors | |
| Data and tools | CoinMarketCap daily USD prices; US risk-free rate from Kenneth French; stationary block bootstrap (expected block 20, B = 1,000) for t-statistics | p. 4-5 |

**Rule** (p. 6): each week, rank the 20 coins on their maximum daily log return of the last seven days. The profitable side is long the lowest-MAX quintile, short the highest (the paper's H-L is the reverse and is negative).

**Data provenance**
- Weekly returns are non-overlapping seven-day log returns (p. 4).
- Market-cap ranks drift: by 28 Dec 2019, PPC is rank 413, RBY 1,303, CLAM 1,261; rank correlation start-to-end 0.4496 (Table A6, p. 9).

## 3. Results

All results are real data, in-sample, gross of costs. t-statistics are block-bootstrap unless noted.

**Aggregate** (Tables 1, 2, A3)
- Quintile mean weekly returns, low to high MAX: 1.33, 1.38, 0.55, 1.08, -0.22.
- H-L: -1.54% a week (t = -2.68); trimmed -1.89% (t = -2.83). SD 14.21%, min -40.81%, max 59.87%.
- Bitcoin-adjusted alpha -1.75% (t = -2.42 to -2.81 across block lengths 10 to 30); beta 0.16.
- Past MAX across quintiles: 3.18% to 21.39%; past volatility 1.33% to 4.42%, rising with MAX.

**By sub-group**
- Including Bitcoin and dropping NEM: H-L -1.37% (t = -2.27), trimmed -1.68% (Table A7).
- Coin-level time-series betas on MAX range from -1.85 (NXT) to 0.92 (XMR); average -0.1938 (Table A5, p. 8-9).
- Long and short legs against a benchmark: not reported.

**Horizon and parameters**
- Skip one day: H-L -1.82% (t = -2.43), trimmed -2.24%; alpha -2.14% (t = -2.32 to -2.46) (Tables 3, A4).
- Inference choice (Table A8): standard t -1.57 (raw), -1.78 (adjusted), -1.75 (skip), -2.08 (skip, adjusted). Newey-West lag 1: -1.89, -2.14, -1.76, -2.14. Lag 5: -2.51, -2.77, -2.48, -2.78.

**Over time** (≈ Fig. 1, cumulative sum of H-L)
- Rises to ≈ +60 by late 2016, back near 0 in spring 2017.
- Falls steadily from mid 2017 to ≈ -320 at end 2019. Authors: "virtually linearly decrease" (p. 6).

**Link to other strategies**
- Cross-sectional premiums (p. 9): constant 0.39, MAX 3.47, reversal 4.43, IVOL 0.51; t = 2.54, 3.83, 3.18, 2.03. OLS t-stats would be 3.34, 6.99, 4.12, 4.06 (fn 7).

**Inconsistencies in the source**
- Sign convention: p. 6 and table captions define H-L as long high-MAX, short low-MAX (spread -1.54%). Eq. 1 (p. 8) and Tables A3-A4 captions define the portfolio as long low-MAX, short high-MAX, yet report negative alphas (-1.75%, -2.14%).
- p. 3 says controlling for Bitcoin risk raises the spread "by 21 basis points per month". The figures are weekly: -1.54% to -1.75% (Tables 1, A3).
- p. 6 says the average return "linearly decreases" from low to high MAX. Table 1 is not monotonic: 1.33, 1.38, 0.55, 1.08, -0.22.
- p. 8 says 207 transitions because "we need one month" to set the first MAX values; MAX uses only the last seven days (p. 6).
- Table A2 numbers two coins as 13 (FCT and BCN).

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Other coins (unreported) show regime and volatility patterns like Ethereum | p. 5 |
| A long-only low-MAX strategy could be implemented | p. 11 |
| Investors' expectations about MAX persistence "appear to be rational" | p. 8 |
| Bitcoin is the only crypto underlying for derivatives | fn 8 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | MAX: max daily return over the last 7 days, weekly quintile sort | technique | signal | Weekly horizon because crypto returns are short-memory and monthly data are too few. Card [[Maximum daily return signal]] | p. 2, 6 |
| 2 | Skip the most recent day between formation and holding | technique | entry | Microstructure (bid-ask, price pressure), as Jegadeesh-Titman. Card [[Implementation lag test]] | p. 9 |
| 3 | Stationary block bootstrap t-statistics, geometric block length (mean 20) | technique | evaluation | Robust to regimes, fat tails and volatility clustering; Newey-West can be size-distorted | p. 4-5, 11 |
| 4 | Week-to-week quintile transition matrix | technique | evaluation | Tests whether extreme returns persist | p. 8 |
| 5 | Trim 2.5% of each tail of the payoff | technique | evaluation | Checks rare observations do not drive the spread | p. 7 |
| 6 | Bitcoin excess return as the single market factor | technique | evaluation | Controls crypto market exposure | p. 8 |
| 7 | Universe fixed by market cap at the sample start | principle | universe | Avoids survivorship bias; information available ex ante | p. 9 |

## 6. Regime observations

- Ethereum's mean daily log return was 1.23% (t = 3.33) in 2017 and not significant in 2018 (p. 4).
- The H-L losses accumulate from mid 2017 onward (≈ Fig. 1).

## 7. Acknowledged limits

- Weekly rather than monthly data, by necessity (p. 4, 11).
- Short-selling constraints (p. 11).
- Small coins and tokens not studied (p. 11-12).

## 8. Not addressed

- Transaction costs and turnover.
- Long-only version performance.
- Sharpe ratio, drawdowns of the long-short.
- Results by year.
- Out-of-sample test.
- Value-weighted portfolios.
