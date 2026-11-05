---
type: diagnostic
kind: attribution
aliases: [Risk and correlation regime split, State-conditional asset returns, Performance by regime, VIX split, Sentiment split, Bull and bear split, High and low volatility split, Uncertainty split, Performance by monetary policy regime, stress and stress-free regression, binary market stress indicator]
sources: 8
---

# Market state split

> [!summary]
> Does the strategy earn its return in every market state, or only in some?

## How it works

- **How**: classify each period by a state variable known at the start (volatility, VIX, uncertainty index, sentiment, past market return) above or below its median; compute the strategy's mean return and alpha in each group.
- **Reading**: similar significant returns in both groups mean no dependence on that state; a return concentrated in one group shows where the profit comes from.
- **Data needed**: strategy returns and the state variable, aligned in time.
- **Variant**: the state is an ex-ante regime from a two-state model (probability of 50% or more), on risk, on correlation, or on both (a four-state grid); compute the mean return of each asset, strategy or factor per state.
- **Variant**: the state is a binary stress indicator built from the mean of expanding z-scores of several stress series; regress strategy returns on factors multiplied by the indicator (stress-free) or by one minus it (stress), and compare the loadings.
- **Variant**: regress returns on binary regime dummies with HAC errors, then repeat on two halves and on rolling windows to check stability.

## What the sources say

### Parameters
- **Kozlowski 2021**
	- VIX above or below its sample median (p. 8)
- **Ozdamar 2021**
	- Augmento Bitcoin Sentiment Index above or below its median (p. 22-23)
- **Fieberg 2025**
	- Crypto market volatility, crypto uncertainty index, 12-month market return; each split at the median (p. 3134)
- **Verma 2026**
	- Three HMM states, each asset's mean and sd of daily return per state, with the time share of each state (Table 3, p. 4)
- **Valach 2024**
	- States: easing or tightening, from the direction of the policy rate; mean monthly return, risk and Sharpe of each portfolio and of the benchmark per state (Tables 4-5, p. 27-28)
- **Luo 2013**
	- Risk regime and correlation regime from out-of-sample Markov-switching models, 50% probability cut; four-state grid of the two (p. 41, 44)
	- Mean returns of 11 asset classes, 9 risk-based rules and 5 equity factors per state (Fig. 65, 67, 69, 83-85, 97, 101-102)
- **Zhakanova 2019**
	- Indicator: mean of expanding z-scores of MSCI World, Citi Eco Surprise G10, TED spread, Baa minus Treasury spread and VIX; 1 means no stress; the cut-off between 1 and 0 is not stated (p. 1414-1415)
	- Regimes: each factor multiplied by the indicator or by 1 minus it, one regression per strategy; 2001 to 2015 (p. 1416-1417)
- **Unknown 2026**
	- Weekly returns regressed on four dummies: VIX above 25 (17.8% of weeks), NBER recession (7.4%), 10Y minus 3M spread under 1 pp (36.3%), BAA minus 10Y spread above its historical 75th percentile (30.3%); HAC errors, 5 lags (Eq. 3, Table 1 C)
	- Conditional annualized Sharpe with the regime on and off (p. 12)
	- Same regression on two halves, 2001-2013 and 2014-2026, and on 519 rolling windows of 260 weeks (p. 12, Table 4)

### Why
- **Kozlowski 2021**: reversal profits track VIX in stocks as a liquidity premium proxy (Nagel 2012) (p. 8)
- **Ozdamar 2021**: tests whether sentiment drives the MAX effect (Fong and Toh 2014) (p. 22)
- **Fieberg 2025**: mispricing can vary with sentiment, uncertainty and limits to arbitrage (p. 3134)
- **Verma 2026**: links each regime to an allocation rule (p. 3-4)
- **Valach 2024**: not argued for the split; the regimes are the ones the strategy rotates on (p. 23)
- **Luo 2013**: decides which assets and factors suit which regime (p. 42-44, 60)
- **Zhakanova 2019**: shows which factors drive the value strategies in stress and stress-free months (p. 1415)
- **Unknown 2026**: a positive average alpha can hide regimes where it reverses, as the Adaptive Markets Hypothesis allows (p. 20)

### Evidence
- **Kozlowski 2021**: real data, in-sample, gross
	- Daily reversal 7.55% (low VIX) vs 7.17% (high VIX) (Table 3C)
- **Ozdamar 2021**: real data, in-sample, gross
	- MAX spread 2.8% (low) vs 3.3% (high sentiment) a week (Table 15)
- **Fieberg 2025**: real data, gross
	- CTREND 5.46% (low vol) vs 2.27% (high vol); 4.49% (bull) vs 3.25% (bear) (Table 5)
- **Verma 2026**: real data, in-sample, gross, SPY, TLT, GLD
	- SPY mean per day +0.1295%, +0.0014%, -0.4749% in states 0 to 2 (Table 3)
	- TLT +0.1673% in the crisis state, 6.18% of days (Table 3)
- **Valach 2024**: real data, in-sample, gross, sector ETFs 2004-2023
	- US: 130 easing and 98 tightening months; J1K12 Sharpe 0.14 (easing) and 0.25 (tightening) (Table 4)
	- Europe: 178 easing and 50 tightening months; benchmark Sharpe 0.14 and -0.08 (Table 5)
- **Luo 2013**: real data, 1998-2013, gross or net not stated
	- Portfolio CVaR about 47% higher in high-risk regimes (p. 42)
	- Equities and REITs earn less in high-risk regimes, bonds and commodities more (Fig. 65)
	- Value and quality do better in high-risk regimes, momentum and size the reverse (Fig. 97)
	- Risk-based portfolios beat the 60-40 benchmark mostly in high-risk, low-correlation states, because they hold more bonds (p. 52-53)
- **Zhakanova 2019**: real data, 2001-2015, gross or net not stated
	- VIX loading -0.2870 (absolute) and -0.4075 (relative) in stress, -0.3224 and -0.4121 in stress-free (Table 7)
	- Credit spread loading -0.0519 (t -2.90) for absolute in stress only (Table 7)
	- Gold loading 0.5241 in stress against 0.1926 in stress-free, absolute strategy (Table 5)
- **Unknown 2026**: real data, in-sample, net of 20 bp per side, 1,289 weeks
	- VIX above 25 adds -0.46 (TSL07) to -0.62 (baseline) pp a week, t about -4.3 to -4.9 (Table 4 A)
	- Same sign in both halves, more negative after 2014; significant in 80% to 92% of rolling windows (Table 4 B-D)
	- NBER, term spread and credit spread: not significant for any rule (Table 4)

### Limits
- **Kozlowski 2021**
	- Median split of a short sample, no test of the difference (Table 3)
- **Ozdamar 2021**
	- High-sentiment spread only t = 1.98 (Table 15)
- **Fieberg 2025**
	- No test of the difference between states (Table 5)
- **Verma 2026**
	- States come from an HMM fitted with the whole path, not known at the start (p. 3)
	- No test of the differences between states (Table 3)
- **Valach 2024**
	- No test of the differences; 50 tightening months in Europe (Table 5)
	- Not stated whether the state is known at the start of each month (p. 23)
- **Luo 2013**
	- Results are bar charts, no test of the difference between states (whole paper)
	- Best and worst assets per state are picked on the data they are tested on (fn 23, p. 46)
- **Zhakanova 2019**
	- Threshold of the indicator and its timing not stated (p. 1414)
	- Text and tables disagree on the sign and size of some loadings (see the reading note)
- **Unknown 2026**
	- Four binary regimes with thresholds set by the authors, five rules from the same selection (Table 4)
	- Conditional Sharpe table is supplementary, not in the PDF (p. 22)

## Sources

- [[2021 - Kozlowski Puleo Zhou - Cryptocurrency return reversals]] (Kozlowski 2021)
- [[2021 - Ozdamar Akdeniz Sensoy - Lottery-like preferences and the MAX effect in the cryptocurrency market]] (Ozdamar 2021)
- [[2025 - Fieberg Liedtke Poddig et al - A Trend Factor for the Cross Section of Cryptocurrency Returns]] (Fieberg 2025)
- [[2026 - Verma Putri Lesupi - Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning]] (Verma 2026)
- [[2024 - Valach Paciga Bohdalova - Application of Sector Rotation in Active Portfolio Management for US and EU Stock Markets]] (Valach 2024)
- [[2025 - Luo Wang Jussa - Dynamic allocation extremes, tail dependence, and regime Shifts]] (Luo 2013)
- [[2019 - Zhakanova Isiksal Backhaus Jung - Value investing across asset classes]] (Zhakanova 2019)
- [[2026 - Unknown authors - Momentum Strategies in ETFs under Simple Operational Rules]] (Unknown 2026)
