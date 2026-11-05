---
type: reading-note
source: paper
title: Optimal Trend Following Trading Rules
authors: Dai, Zhang, Zhu
affiliations: Dai (National University of Singapore), Zhang (University of Georgia), Zhu (Western Michigan University)
year: 2011
venue: SSRN working paper 1762118, dated July 19, 2011
doi:
pdf: "[[2011 - Dai Zhang Zhu - Optimal Trend Following Trading Rules.pdf]]"
version: working paper
tier: 1
read: full
tags: [trend, equities, monthly]
date: 2026-10-21
---

# Optimal trend following rules (Dai, Zhang, Zhu 2011)

## Summary

- **Finding**: in a bull-bear model, buying when the bull probability crosses an upper threshold and selling at a lower one is optimal. Ex-ante S&P 500 1972-2011: 11.03% vs 9.8% buy-hold.
- **Mechanism**: a hidden two-state Markov chain drives the drift. The price reveals the state only through a filter. Why markets would behave this way: not stated by the authors.
- **Where it works best**: SSE index 2001-2011, long and flat: 14.0% a year vs 2.58% buy and hold, quarterly Sharpe 0.263 vs 0.083. Long and short: 18.48%.
- **Weak spots**: S&P 500 with shorts, 1972-2011: 2.57% vs 8.57% buy and hold. S&P 500 long-only edge is small (+1.2 points, computed). Single paths vary widely.
- **Main caveats**: two indexes only; costs and dividends in market tests not stated; initial parameters for SSE guessed; the authors say their model may be a crude approximation.

Page numbers follow the PDF, which matches the printed pagination (1 to 25). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | The drift of the price switches between an uptrend value (µ1 > 0) and a downtrend value (µ2 < 0) through a Markov chain that cannot be observed | Model assumption | p. 3-4 |
| 2 | Under this model the optimal rule, for a long or flat investor, is to buy when the bull probability p crosses an upper curve and sell when it crosses a lower curve | Theorem 2, verification theorem 3, numerical solution (Fig. 1) | p. 8-10 |
| 3 | The rule is trend following: p rises when the price rises and falls when it falls, so it buys only into rises and sells only into falls | Eq. 13 | p. 9 |
| 4 | Market trends are the result of many individual actions, so real trends are "more stable" than Brownian paths | None | p. 14 |
| 5 | No solid theory existed for moving averages | None | p. 2 |

**Caveats raised by the authors**
- Simulation results depend heavily on the single path (p. 11).
- Sensitivity to parameters is expected; apply test results with caution (p. 14).
- Short selling is harder: losses can exceed capital, so the exact problem is intractable and an approximation is used (p. 14).
- Shorting helps in simulation but is mixed on real data. Up and down trends are not symmetric, and the regime model may be a crude approximation of real markets (p. 17).

**Ruled out**: nothing.

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | S&P 500 index and Shanghai Stock Exchange (SSE) index. One asset at a time. | p. 12 |
| Period | S&P 500: May 1972 to 2011, closing data since 1962. SSE: 2001 to 2011. | p. 12, App. 7.2 |
| Signal | p_t, the probability of the bull state given the price path, from a discrete filter (Eq. 14). | p. 10 |
| Entry | Flat to long when p reaches p*b. | p. 9 |
| Exit | Long to flat when p falls to p*s. Forced sale at the terminal date T in the model. | p. 4, 9 |
| Horizon | Model: finite T, then constant thresholds for the long run. Real tests: 39 years (S&P 500), about 10 years (SSE). | p. 9, 12 |
| Sizing | All wealth in the stock or all in cash at the risk-free rate. No partial position. | p. 3, 4 |
| Calibration | µ1, µ2, λ1, λ2, σ estimated from past bull and bear markets (moves of at least 20%). Thresholds solved from the HJB equations. | p. 12, App. 7.2 |
| Rebalancing | Parameters and thresholds updated every January, using only trends confirmed before that date. | p. 12 |
| Costs | Model and simulations: 0.1% per trade (Kb = Ks = 0.001). Market tests: not stated. | p. 11 |
| Shorts | Optional extension: two thresholds more for short and cover (see Rule). Real tests use actual shorting with 50% margin. | p. 15-16 |

**Rule**

Filter, daily, dt = 1/252, price S, clipped to [0, 1] (Eq. 14, p. 10):

$$p_{t+1} = \min\Big(\max\Big(p_t + g(p_t)\,dt + \frac{(\mu_1-\mu_2)\,p_t(1-p_t)}{\sigma^2}\log\frac{S_{t+1}}{S_t},\ 0\Big),\ 1\Big)$$

with $g(p) = -(\lambda_1+\lambda_2)p + \lambda_2 - \frac{(\mu_1-\mu_2)p(1-p)\left((\mu_1-\mu_2)p+\mu_2-\sigma^2/2\right)}{\sigma^2}$ (p. 9; the paper writes $p_t$ inside g in places).

Long when p rises to p*b, flat when p falls to p*s (p. 9). The sell threshold tends to $(\rho-\mu_2+\sigma^2/2)/(\mu_1-\mu_2)$ near T (Theorem 2, p. 8).

Long, short, flat (p. 15). Trader A is long or flat with p*b and p*s. Trader B is short or flat, using the mirrored model: $q = 1-p$, $\hat\mu_1=\sigma^2-\mu_2$, $\hat\mu_2=\sigma^2-\mu_1$, $\hat\lambda_1=\lambda_2$, $\hat\lambda_2=\lambda_1$ (Eq. 15). Short when p falls below $1-q^*_b$, cover when p rises above $1-q^*_s$. Example order, Table 1 parameters: 0.589 < 0.774 < 0.849 < 0.947 (Eq. 19).

Short trade gain, 50% margin (Eq. 20, p. 16): $[S_s + S_s(1-K) - S_c(1+K)]/S_s$.

**Data provenance**
- S&P 500: closing data since 1962; source not named. Fig. 2 shows the index without dividends and a buy and hold curve with dividends (p. 12).
- SSE: closing prices already adjusted for dividends (p. 13-14). Source not named.
- 10-year bond return in Table 4: Federal Reserve series listed as reference [7], not cited in the text.
- Simulated prices: Table 1 parameters, 40-year horizon (p. 10).

## 3. Results

**Aggregate, real data, ex-ante** (Table 4, p. 14). Annualised return, quarterly Sharpe ratio in brackets. Gross or net: not stated.

| Index | Trend following | Buy and hold | 10-year bonds |
| --- | --- | --- | --- |
| S&P 500, 1972-2011 | 11.03% (0.217) | 9.8% (0.128) | 6.79% |
| SSE, 2001-2011 | 14.0% (0.263) | 2.58% (0.083) | 3% |

Both curves in Fig. 2 and 3 are on a log scale, so their levels are not read here. Table 4 values fit the end points of the curves (≈ 5,900 for trend following and ≈ 3,800 for buy and hold at 100 in 1972, my computation from the table). The authors say the trend following curve is smoother (p. 12).

**Aggregate, simulation inside the model** (Tables 2, 3, 5)
- Long and flat, ten runs of 5,000 paths, 40 years (Table 2, p. 11): trend following 75.76 times (11.4% a year) vs 5.62 (4.4%); 41.16 trades. Costs 0.1% per trade.
- Long, short, flat (Table 5, p. 16): 180.34 (13.9%) vs 5.77 (4.5%); 66.46 trades.
- Ten single paths (Table 3, p. 11): trend following beats buy and hold in all ten. Trend following ranges from 8.65 to 1,887.8; buy and hold from 0.08 to 257.75; 33 to 48 trades.
- Same model as the earlier paper [4]: only a slight improvement, not statistically distinguishable (p. 11, 17). No test shown.

**By sub-group**
- Shorts, real data (p. 16): SSE long, short, flat 18.48% a year, quarterly Sharpe 0.306. S&P 500 1972-2011: 2.57% vs 8.57% buy and hold. Shorts lose money there.

**Horizon and parameters**
- Yearly S&P 500 thresholds: p*s from 0.391 to 0.739, p*b from 0.703 to 0.900 (Table 7, p. 22). SSE: p*s from 0.186 to 0.487, p*b from 0.442 to 0.759 (Table 9, p. 23).
- Fig. 1 (≈): thresholds flat at p*s ≈ 0.8 and p*b ≈ 0.95 until close to T. Buy boundary goes to 1 in the last δ, with δ above 0.021 years (p. 8).
- No test of other values of N or of the 20% definition.

**Over time** (≈ Fig. 2, 3, log scale)
- S&P 500: the trend following curve stays above both others over the whole period, with flat stretches (in cash) around 2000-2003 and 2008.
- SSE: flat from 2001 to 2006 at ≈ 2,000 while buy and hold falls to ≈ 1,000. Both rise to a peak in 2008, ≈ 10,000 vs ≈ 6,000. Then trend following stays at ≈ 7,000 to 9,000 and buy and hold ends ≈ 2,700.
- Drawdown figures: not reported.

**Link to other strategies**
- Earlier paper [4] (SIAM J. Financial Math. 2010): footnote 12 corrects its S&P 500 1962-2008 returns to 54.6 (buy and hold) and 70.9 (trend following), instead of 33.5 and 64.98. Dividends had not been reinvested (p. 14). Units not stated.

**Inconsistencies in the source**
- S&P 500 buy and hold, 1972-2011: 9.8% in Table 4 (p. 14), 8.57% on p. 16.
- Thresholds for Table 1 parameters: 0.796 and 0.948 (p. 11), 0.795 and 0.948 (Table 3 text), 0.774 and 0.947 (p. 15).
- Risk-free rate: 0.0679 in Table 1 and Fig. 1, 0.0657 in the δ computation (p. 8). The result 0.021 holds with both (≈ 0.0206 and 0.0210, my computation).
- Buy and hold in simulation: 5.62 (4.4%) in Table 2, 5.77 (4.5%) in Table 5, same parameters. Not explained.
- Unit of the simulated returns is not stated; 75.76 and 11.4% agree over 40 years as a multiple of initial wealth (my computation). Trade counts are assumed to be for trend following.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Other initial SSE parameters (µ1 = 0.4, µ2 = -0.4, λ1 = 1, λ2 = 0.5) give similar results, "available upon request" | p. 12, fn 11 |
| Higher Sharpe ratio follows from a smoother curve (Sharpe shown only in Table 4) | p. 12 |
| Test is comparable to the ex-post test in [4] | p. 14 |
| The signal is robust to threshold changes (one comparison with [4]) | p. 11 |
| Trend following beats buy and hold "in almost all cases" on single paths | p. 17 |
| Inverse ETF approximates shorting only over the short term | p. 16 |
| Smaller gain from shorts than from longs is due to the upward bias of markets | p. 16 |
| Trends exist in China, shown by one 10-year sample | p. 14 |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | [[Regime probability filter\|Bull probability from a recursive filter on log returns]] | technique | signal | Only the price is observable (Wonham filter) | p. 5-6, 10 |
| 2 | [[No-trade band\|Two thresholds, buy high and sell lower, no trade between]] | technique | entry, exit | Solution of the HJB equations with transaction costs | p. 8-9 |
| 3 | Constant thresholds from the infinite horizon limit | technique | calibration | Interest in long-term investment | p. 9 |
| 4 | Parameters from past bull and bear episodes (moves of 20%) | technique | calibration | Not argued | p. 12 |
| 5 | Exponential update: new = (1 - 2/N) old + (2/N) new, N = 6 | technique | calibration | Overweights new data, avoids abrupt changes | p. 12 |
| 6 | Yearly update using only trends confirmed before the date | technique | rebalancing | Ex-ante test | p. 12 |
| 7 | Long and short as two separate traders, four thresholds | technique | entry, exit | Exact long, short, flat problem is too hard | p. 15 |
| 8 | Short side by mirrored model (1/S, q = 1 - p) | technique | signal | Same equations as the long case | p. 14-15 |
| 9 | Real shorting with 50% margin instead of inverse ETF | technique | evaluation | ETF holds only short term | p. 16 |
| 10 | Objective: expected log of terminal wealth | principle | economic intuition | Equals log utility with proportional costs | p. 5, fn 6 |
| 11 | Mean over 5,000 paths and separate single paths | technique | evaluation | Single paths vary widely; judge a rule by the average | p. 11 |

## 6. Regime observations

- SSE yearly parameters for 2009 to 2011 show very high µ and λ after the 2008 crash (Table 8, p. 23). No comment by the authors.
- Flat stretches (cash) in S&P 500 around 2000-2003 and 2008 (≈ Fig. 2). No text on them.

## 7. Acknowledged limits

- Exact long, short, flat solution not available (p. 3, 14).
- Results depend on the path and on parameters (p. 11, 14).
- Real trends are not symmetric (p. 17).

## 8. Not addressed

- Costs, dividends and risk-free rate used in the market tests.
- Number of trades, drawdowns, volatility on real data.
- Other markets, other periods, other parameter choices (N, 20% rule), capacity.
- Source of the price data.
- Statistical test of the gap with buy and hold (S&P 500 gap is 1.2 points).
- How σ is estimated each year.
