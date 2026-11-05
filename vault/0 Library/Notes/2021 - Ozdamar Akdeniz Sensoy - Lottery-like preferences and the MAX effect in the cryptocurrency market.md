---
type: reading-note
source: paper
title: Lottery-like preferences and the MAX effect in the cryptocurrency market
authors: Ozdamar, Akdeniz, Sensoy
affiliations: Faculty of Business Administration, Bilkent University
year: 2021
venue: Financial Innovation 7:74
doi: 10.1186/s40854-021-00291-9
pdf: "[[2021 - Ozdamar Akdeniz Sensoy - Lottery-like preferences and the MAX effect in the cryptocurrency market.pdf]]"
version: published (open access)
tier: 1
read: full
tags: [trend, crypto, weekly]
date: 2026-10-24
---

# Positive MAX effect in crypto (Ozdamar, Akdeniz, Sensoy 2021)

## Summary

- **Finding**: coins with the highest maximum daily return over the past month beat the lowest decile by 3.03% a week value-weighted (alpha 1.99%), 2.45% equal-weighted, 2014-2020, gross (Table 2).
- **Mechanism**: opposite sign to the equity MAX effect. Authors read it as continuation: extreme winners keep winning, "resembles" momentum and signals inefficiency. Lottery-preference story is not supported (p. 11).
- **Where it works best**: value-weighted after controlling for total skewness: 2.95% a week, t = 8.06, alpha 2.67% (Table 12). Holds in low and high sentiment weeks (Table 15).
- **Weak spots**: after controlling for IVOL the value-weighted spread drops to 0.91% (alpha 0.6%) (Table 10). VW returns of deciles 1 to 6 are between -0.9% and 0.2% a week (Table 2).
- **Main caveats**: no costs; high-MAX coins are small (median 22 million USD) and illiquid; shorting not discussed. The cumulative chart (Fig. 1) does not match the table averages.

Page numbers follow the journal pagination (1 to 27 of article 7:74). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | High-MAX coins keep extreme positive returns: buying winners and selling losers keeps paying, which signals inefficiency and resembles momentum | Positive 10-1 spreads; high-MAX coins have higher mean and upper percentiles next week | Tables 2, 5; p. 11 |
| 2 | Investors may expect extreme returns to last and pay higher prices for these coins | Argued from Tables 2-3 | p. 8 |
| 3 | The results give "evidence against" lottery-like preference in crypto | Sign of the effect, opposite to Bali et al. (2011) | p. 11 |
| 4 | MAX is not a proxy for volatility; the IVOL effect of Zhang and Li (2020) may proxy for MAX | VOL and IVOL sorts controlling for MAX are not significant | Table 10, Panel B; p. 19 |

**Caveats raised by the authors**
- Results contradict Grobys and Sapkota (2019), Jia et al. (2020), Grobys and Junttila (2021); authors attribute this to their smaller samples (p. 3).
- "Further research is necessary" before exploiting the anomaly (p. 25).

**Ruled out**
- Size, price, momentum, reversal, illiquidity: double sorts keep 1.48% to 2.73% (VW) (Table 7).
- Total and idiosyncratic skewness (Tables 12, 14).
- Investor sentiment as the driver: significant in both regimes (Table 15).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | All CoinMarketCap coins above 5 million USD market cap; a coin enters six months after launch. 17 coins at start, 523 at end, 973 in total (out of 2,000). | p. 3-5, fn 6, fn 8 |
| Period | January 2014 to September 2020, 348 weeks | p. 5, 15 |
| Signal | MAX = highest daily return over the past month (28 days) | Eq. 1, p. 6, fn 9 |
| Entry | Rank weekly into deciles | p. 7 |
| Exit | Hold one week | p. 7 |
| Horizon | Weekly | p. 7 |
| Sizing | Value weight and equal weight | Table 2 |
| Portfolio | Long decile 10 (high MAX), short decile 1 | Table 2 |
| Rebalancing | Weekly | Table 2 |
| Costs | Not stated by the authors | |
| Data and tools | CoinMarketCap daily prices, volumes, OHLC; value-weighted crypto market index; one-month T-bill; three-factor model (market, size, momentum on terciles); Newey-West t-stats; regressions winsorised at 5% each tail | p. 5-9 |

**Rule** (Eq. 1, p. 6): MAX(i,t) = max of daily returns R(i,d) over the last 28 days. Each week, long the top MAX decile, short the bottom decile, hold one week.

**Data provenance**
- A week is 7 trading days and a month 28 (fn 9).
- Coin list "available upon request" (fn 7). How dead coins are handled: not stated.
- Using all 2,000 coins without the 5 million USD filter gives "similar" results, not shown (fn 6).

## 3. Results

All results are real data, in-sample, gross of costs.

**Aggregate** (Table 2)
- VW: 10-1 return 3.0% a week (t = 4.10), alpha 2.0% (t = 3.72). Text: 3.03% and 1.99% (p. 3).
- EW: 2.5% (t = 3.22), alpha 2.4% (t = 3.34).
- VW decile returns: -0.9% (low) to 2.1% (high); deciles 1 to 6 between -0.9% and 0.2%.
- Fama-MacBeth (Table 8): MAX slope 0.082 (t = 3.14) alone; 0.284 (t = 6.14) with all controls. Other controls insignificant in the full model.

**By sub-group**
- Decile composition (Table 6): median MAX 5.4% to 59.6%; median size 426.8 to 21.9 million USD; ILLIQ and volatility rise with MAX.
- Next-week returns, coin level (Table 5): low MAX mean 0.5%, high MAX 3.8%; medians -0.1% and -0.3%; 99th percentile 50.5% vs 72.2%.
- Sentiment (Table 15, VW): low sentiment 2.8% (t = 3.16), high 3.3% (t = 1.98); alphas 2.5% and 3.0%.

**Horizon and parameters**
- MAX(N), average of N highest daily returns (Table 3): VW spread 1.8% to 3.0%, EW 2.1% to 2.5%, all N from 1 to 5 significant.
- Double sorts (Table 7): VW 1.5% (REV control) to 2.7% (SIZE); EW 1.6% to 2.1%.
- Volatility controls (Table 10, Panel A): VW 1.6% with VOL (t = 5.17), 0.9% with IVOL (t = 2.72); alpha 0.6% with IVOL (t = 2.13).
- Reverse sort (Panel B): VOL and IVOL spreads 0.1% to 1.4%, none significant.

**Over time** (≈ Fig. 1, cumulative VW long-short)
- Falls from 2014 to ≈ -0.04 in 2016, recovers from 2017, rises steadily to ≈ +0.05 in 2020.

**Link to other strategies**
- Univariate: MOM slope 0.039 (t = 2.32), REV 0.096 (t = 2.63), both positive (Table 8).
- Correlations: MAX with IVOL 0.80, with TVOL 0.77, with Garman-Klass VOL 0.0028 (Table 9).

**Inconsistencies in the source**
- Fig. 1 plots a cumulative long-short return between ≈ -0.05 and ≈ +0.05 over 2014-2020. Table 2 reports a mean of 3.0% a week over 348 weeks.
- p. 8 says average returns and alphas "increase monotonically" with MAX. Table 2 VW returns are not monotonic (decile 5: 0.002, decile 6: 0.000, decile 8: 0.007 after decile 7: 0.010).
- Stars disagree with the stated levels: t = 2.447, 2.431, 2.364 (Table 3) and 2.438 (Table 15) are marked *** (1%), while t = 2.212 is marked ** (Table 3).
- The title and abstract frame the paper as lottery-like preference; p. 11 says the results are evidence against it.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Results "similar" on all 2,000 coins without the size filter | fn 6 |
| Full 100-portfolio double sorts | fn 13 |
| MAX(5) instead of MAX gives "very similar" volatility results | fn 15 |
| Sentiment shows no persistence (Durbin-Watson, Ljung-Box) | fn 18 |
| "Coins with extreme positive returns are inclined to outperform in the following month", stated from a regression of MAX on lagged MAX (Table 4), whose dependent variable is MAX, not return | p. 10 |
| Investors turned from pessimistic short positions to optimistic long positions as sentiment rose | p. 24 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | MAX: max daily return over past 28 days, weekly decile sort | technique | signal | Follows Bali et al. (2011); weekly because crypto reacts faster. Card [[Maximum daily return signal]] | p. 3, 6 |
| 2 | MAX(N): average of N highest daily returns | technique | signal | Robustness of the single-day extreme. Card [[Maximum daily return signal]] | Table 3 |
| 3 | 5 million USD market cap floor and six-month seasoning for new coins | technique | universe | Low caps are illiquid; new coins behave oddly until adopted. Card [[Minimum price and size filter]] | fn 8 |
| 4 | Garman-Klass OHLC volatility as control | technique | evaluation | Low correlation with MAX avoids multicollinearity | fn 11 |
| 5 | Dimson beta with lag, current and lead market returns | technique | evaluation | Non-synchronous trading | Eq. 2 |
| 6 | Double sorts on a control then MAX, averaged across control deciles | technique | evaluation | Isolates MAX from other characteristics. Card [[Conditional double sort]] | p. 12 |
| 7 | Split weeks by median sentiment index (Augmento Bitcoin Sentiment) | technique | evaluation | Tests Fong and Toh (2014) sentiment dependence. Card [[Market state split]] | p. 22-23 |

## 6. Regime observations

- Spread is positive after both low and high sentiment weeks, slightly higher after high (Table 15, p. 24).
- The long-short loses in the early sample (2014-2016) and gains from 2017 (≈ Fig. 1).

## 7. Acknowledged limits

- Further research needed before exploiting the anomaly (p. 25).

## 8. Not addressed

- Transaction costs, bid-ask spreads, turnover.
- Shorting the low-MAX decile.
- Capacity, given high-MAX coins are small and less liquid.
- Drawdowns and Sharpe ratio.
- Out-of-sample test.
- Survivorship and how the coin list was built.
