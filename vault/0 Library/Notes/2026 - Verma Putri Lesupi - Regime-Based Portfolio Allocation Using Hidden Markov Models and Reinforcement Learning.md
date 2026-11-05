---
type: reading-note
source: paper
title: Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning
authors: Verma, Putri, Lesupi
affiliations: Independent researchers (one author at Aenimatica Tech Research and Development)
year: 2026
venue: Preprint dated November 2025, no venue stated
doi:
pdf: "[[2026 - Verma Putri Lesupi - Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning.pdf]]"
version: preprint, 9 pages
tier: 1
read: full
tags: [low-vol, multi-asset, daily]
date: 2026-10-25
---

# HMM regime rotation across SPY, TLT, GLD (Verma, Putri, Lesupi 2026)

## Summary

- **Finding**: on SPY, TLT, GLD daily 2004-2025, a 3-state HMM plus a state-to-asset policy gets test-window Sharpe 0.83 (RL), against 0.83 equal-weight and 0.65 SPY. No costs (Table 7, p. 6).
- **Mechanism**: volatility regimes persist and assets pay differently by regime: SPY wins when calm, gold or Treasuries protect in the stress state (p. 3-4). No test beyond state means.
- **Where it works best**: test window about 2019-2025, RL cumulative 131.4% against SPY 118.4%; max drawdown -23.5% against -35.7% (Table 7, p. 6).
- **Weak spots**: the RL Sharpe ties equal-weight (0.83) and beats 60/40 by 0.01; Top-1 drawdown is smaller (-21.8%). Rule maps contradict the RL map (Tables 4 and 5).
- **Main caveats**: zero costs, one 30% split (about 6.3 years, computed), regime counts not reported, whether regimes are filtered or smoothed not stated (p. 6, 7).

Page numbers are the PDF pages, which match the printed ones (the preprint has no journal pagination). Values marked ≈ are read from a chart.

## 1. Mechanism (authors' claim)

| # | Claim | Evidence given | Where |
| --- | --- | --- | --- |
| 1 | Volatility clustering and structural breaks make markets regime dependent | Charts of returns and rolling volatility (Figures 1-6); citations | p. 1-2 |
| 2 | Three regimes (calm, transitional, crisis) fit better than two | Table 1 AIC and BIC; interpretability argument | p. 3 |
| 3 | Regimes are persistent | Diagonal of the transition matrix 0.87 to 0.94 (Table 2b) | p. 3 |
| 4 | SPY leads in calm, GLD and TLT protect in stress | State-conditional means (Table 3) | p. 4 |
| 5 | The RL policy "internalizes" regime payoffs and is interpretable | Table 5 maps three states to three allocations | p. 5 |

**Caveats raised by the authors**
- Gaussian emissions miss heavy tails and jumps; sharp regime boundaries; tabular MDP is limited; no costs, slippage or liquidity; Markov property may fail (p. 7).
- Even small frictions can matter for regime-switching strategies (p. 7).

**Ruled out**
- Four or more states: "reduce BIC only marginally", unstable smoothed probabilities. No table (p. 3).

## 2. Strategy, brick by brick

| Brick | Paper | Where |
| --- | --- | --- |
| Universe | SPY, TLT, GLD; VIX used as the volatility input | p. 1 |
| Period | Daily 2004-2025. Chronological 70% train, 30% test | p. 1, 5 |
| Signal | 3-state Gaussian HMM, EM estimation, forward (Hamilton) filter, RTS smoother, Viterbi path for plots | p. 2-3 |
| Entry | Hold the allocation tied to the current predicted regime | p. 4-5 |
| Exit | Allocation changes when the regime changes | p. 4 |
| Horizon | Daily, one-day execution lag | p. 4-5 |
| Sizing | Top-1: 100% to best-mean asset. 60/40: 60% best, 40% second. RL: one of 7 discrete weight sets | p. 4 |
| Portfolio | Long-only, 3 assets, fully invested | p. 4-5 |
| Rebalancing | On regime change. Benchmark equal-weight rebalanced monthly | p. 4, 6 |
| Costs | Zero in the baseline (p. 6, 7) | p. 6 |
| Data and tools | Yahoo Finance closes, log returns | p. 1 |

**Rule**: each day, predict the regime S_t. Top-1 holds the asset with the highest state-conditional mean return (Table 4). RL: tabular policy iteration, Q(s,a) = R(s,a) + γ Σ P(s,s') V(s'), with R the expected next-period return in state s, P the HMM transition matrix. The discount factor γ is not given (p. 5). The action chosen at t applies to returns at t+1 (p. 5-6).

**Data provenance**: Yahoo Finance daily closes for SPY, TLT, GLD, VIX. No adjustment details. The authors say the data are "aligned" to reduce survivorship bias (p. 2).

## 3. Results

**Aggregate** (all real data, gross: costs zero, p. 6)
- Test window 30% (Table 7): RL 131.4% cumulative, 14.3% a year, vol 17.3%, Sharpe 0.83, max drawdown -23.5%.
- Same table: Top-1 110.4%, Sharpe 0.79, -21.8%. 60/40 86.9%, 0.82, -29.3%. Equal-weight 72.5%, 0.83, -24.0%. SPY 118.4%, 0.65, -35.7%.
- Full sample (Table 6, RL not shown): Top-1 407.8%, Sharpe 0.52, -28.3%. 60/40 317.0%, 0.58, -29.3%. Equal-weight 376.1%, 0.80, -24.0%. SPY 476.3%, 0.46, -59.6%.
- The Sharpe equals annualised return over volatility (computed), so zero risk-free rate.

**By sub-group**
- Regimes by share of time: 50.83%, 42.98%, 6.18% (Table 3).
- SPY daily mean by state: +0.1295%, +0.0014%, -0.4749% (Table 3).
- TLT mean in the crisis state +0.1673%, GLD +0.0476% (Table 3).
- Policy: Table 4 rules and Table 5 RL map differ by state. No per-asset contribution is shown.

**Horizon and parameters**
- 2 against 3 states: BIC 18010 against 17385 (Table 1). No 4-state numbers.

**Over time**
- Test window starts about 2019-2020 (≈ Figure 11). The authors point to the post-2020 divergence and the 2020 volatility surge (p. 6).
- Full-sample SPY drawdown -59.6% is the 2008 episode on Figure 10 (≈, not discussed).

**Link to other strategies**: Not addressed.

**Inconsistencies in the source**
- Table 7 labels RL "(net)" while p. 6 and p. 7 say costs are zero.
- Table 3: in state 2 TLT has the highest mean (+0.1673%), so Table 4 maps state 2 to TLT. The text (p. 4) says GLD "has the most favorable profile" and Table 5 sends state 2 to GLD.
- Table 4 puts state 1 in GLD; Table 5 puts state 1 in SPY, whose state 1 mean is +0.0014% (Table 3), "slightly positive" per p. 5.
- Table 2 states 0 and 2 means are -0.0606 and +0.6120 with sds 0.61 and 5.93, which match neither SPY nor the Table 3 sds (0.55%, 3.38%). The series fed to the HMM is not stated; Figure 7's legend shows the same μ values on a VIX chart.
- The abstract says RL has "materially lower drawdowns" and "the strongest Sharpe ratio". Table 7 shows equal-weight tied at 0.83 and Top-1 with a smaller drawdown.
- Section 7 says the HMM is estimated on the training sample. Tables 1-3 and Figures 7-8 are not said to be train-only, and Table 3 time shares are not labelled.

## 4. Claims without evidence shown

| Claim | Where |
| --- | --- |
| Four or more states are unstable and economically ambiguous | p. 3 |
| Sensitivity analysis "confirms robustness" of three states | Abstract; only Table 1 is shown |
| Bond hedge fails with positive stock-bond correlation, hence no TLT | p. 5 |
| The 70/30 split mitigates backtest overfitting; no count of tried variants | p. 5 |
| RL "consistently" beats rotation | p. 7; one window |

## 5. Techniques

| # | Technique | Kind | Brick | Why (author) | Where |
| --- | --- | --- | --- | --- | --- |
| 1 | Gaussian HMM with 3 volatility states, filtered state as the regime label | technique | signal | Volatility clusters. Card [[Regime probability filter]] | p. 2-3 |
| 2 | Hold the asset with the best mean return in the current state (Top-1, 60/40) | technique | sizing | Payoffs differ by state. Card [[Regime-conditional strategy combination]] | p. 4 |
| 3 | Tabular policy iteration over regimes with 7 weight sets | technique | sizing | Interpretable RL. No card: γ not given, learned map is one weight set per state | p. 5 |
| 4 | Number of states by AIC and BIC | technique | calibration | Fit and parsimony. No card: standard practice | p. 3 |
| 5 | 3 quantile bins of ΔVIX as an observable Markov chain | technique | signal | Persistence. No card: cutoffs not given | p. 2 |
| 6 | State-conditional mean and sd of each asset | technique | evaluation | Links regimes to rules. Card [[Market state split]] | p. 4 |
| 7 | 70/30 chronological split, one-day execution lag | technique | evaluation | Avoid look-ahead. Card [[Chronological holdout test]] | p. 5 |

## 6. Regime observations

- Crisis state: 6.18% of days, 0.87 chance of staying a day (Tables 2b, 3). Shaded stretches on Figure 7 sit near 2008-09 and 2020 (≈). Number of separate episodes: not reported.
- Calm state about half of the days (Table 3).
- SPY mean is negative only in the crisis state (Table 3).

## 7. Acknowledged limits

- See section 1: Gaussian tails, hard regime boundaries, tabular RL, no costs, Markov assumption (p. 7).
- Future work lists costs, macro inputs, deep RL, more assets (p. 8).

## 8. Not addressed

- Transaction costs, turnover, number of regime switches, capacity.
- Filtered versus smoothed regime in the test window; HMM re-estimation in the test window.
- Number of independent regime episodes in the test; significance tests; confidence intervals.
- Risk-free rate; ETF dividends and fees; Yahoo adjustment.
- A test window other than the single 30% split.
