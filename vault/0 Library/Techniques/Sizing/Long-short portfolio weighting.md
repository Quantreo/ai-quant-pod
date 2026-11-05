---
type: technique
brick: sizing
aliases: [rank-based weights, rank weighting, spread weighting, signal-proportional weights, equal-weight top-k bottom-k, N v N basket, half/half sort, three-portfolio sort, tercile sort, linear weights, de-meaned signal weights, quartile sort, HML portfolio, Top-1 rule, Single-contract selection, HML portfolio, six-portfolio sort, rank-weighted factor, Forecast-proportional top-l weights, long-only instead, long or short by magnitude, mixed long-short, LSS, TSFM, CSFM, time-series factor momentum weights, cross-sectional factor momentum weights, forecast-over-volatility weights]
sources: 13
tested_on: [multi-asset, fx, commodities, equities, rates]
---

# Long-short portfolio weighting

> [!summary]
> Turns a cross-sectional ranking into position weights: equal weights in the extreme groups, weights by rank, or weights proportional to the signal.

## How it works

- **Rule**: rank assets on the signal each period, then weight them by one of three schemes: equal weight in the top and bottom groups (top k, top half), rank minus its cross-sectional mean, or the signal value itself (spread).
- **Risk estimate**: none. Weights ignore volatility unless combined with volatility targeting.
- **Aggregation**: weights normalised, typically longs summing to 1 and shorts to -1, or absolute weights summing to 1.
- **Implied leverage**: fixed by the normalisation.
- **Variant**: weights proportional to the signal minus its cross-sectional mean; the returns of the parts of an additive signal then add up to the full return.
- **Variant**: hold only the top-ranked and the bottom-ranked asset (k = 1), unit notional each.
- **Variant**: weights proportional to a return forecast, only on the l largest forecasts (long-only, or long and short, or by absolute size), divided by the sum of their absolute values.
- **Variant**: weights are the forecast over volatility, capped at ±2, each leg scaled to one dollar; subtract the median forecast first for a relative version.

## What the sources say

### Parameters
- **Koijen 2013**
	- w = z (rank - (N + 1) / 2), longs sum to 1, shorts to -1 (Eq. 23, p. 18).
	- Monthly rebalance, one-month hold (p. 18-19).
- **Daniel 2014**
	- EQ: sign of the rate differential vs USD, divided by N (p. 10).
	- SPD: differential divided by the sum of absolute differentials (Eq. 9, p. 10).
	- Monthly rebalance (p. 28).
- **Brunnermeier 2008**
	- Long the k highest-rate, short the k lowest, k = 1, 2, 3, equal weight (p. 11).
	- Rebalanced each week or quarter (p. 11).
- **Clarida 2009**
	- N v N: long the N highest yielders, short the N lowest, N = 1 to 5, equal weight within each leg (p. 6).
- **Gorton 2007**
	- Top half vs bottom half, equal weights, monthly (p. 19).
- **Lustig 2013**
	- Three portfolios of nine currencies vs USD; portfolio return = average of country log excess returns; long the top, short the bottom (p. 10).
	- Monthly rebalance, information at t only (p. 10).
	- Per-country variant: long foreign, short US by the sign of the rate or slope differential, then equal-weighted across countries (Table 2).
- **Menkhoff 2016**
	- Linear: w = c (x - cross-sectional mean of x), c sets absolute weights summing to 1 (Eq. 7, p. 13).
	- Rank: same formula on ranks (Eq. 8, p. 14).
	- Quartile sort: 4 equal-weight bins, long P4, short P1 (p. 14).
	- Quarterly rebalance (p. 13).
- **Chernov 2020**
	- w = κ (rank - mean rank), κ sets one dollar long and one dollar short (Eq. 11, p. 15-16).
	- Used for CS-Carry, CS-Mom 1 and 12, CS-Value; nine G10 currencies vs USD, monthly (p. 16-17).
- **Kosch 2026**
	- Top-1: long the highest-score contract, short the lowest, each at unit notional, reset monthly (p. 9-10)
	- 15 commodity futures, 2016-2024; long and short portfolios kept separate (p. 9-10, 12)
- **Lustig 2008**
	- Six portfolios on the signal, equal weight inside each; portfolio return = average of currency log excess returns; high minus low = portfolio 6 minus portfolio 1 (p. 8, 17).
	- Net returns: all foreign currencies of portfolio 1 shorted, all others long (p. 8).
	- Monthly rebalance (p. 8).
- **Asness 2013**
	- Three equal groups on the signal, P3 minus P1; stocks value-weighted, other classes equal-weighted (p. 10)
	- Factor: w = c (rank - mean rank), c sets one dollar long and one dollar short (Eq. 1, p. 10)
	- Monthly rebalance; yearly rebalancing to equal weights gives similar results (fn 8)
- **Oliveira 2025**
	- 10 ETFs, l = 2, 3, 4; weight = forecast over sum of absolute forecasts of the chosen set (Eq. 15-18, p. 15)
	- lns: l highest and l lowest; los: l largest absolute forecasts; lo: l highest only; mx: los if next regime is 0, else lo (p. 15)
	- Monthly, one month ahead (p. 16)
- **Kagkadis 2023**
	- LSS: equal weight, long the top 10% of 72 factors by forecast, short the bottom 10%, monthly (p. 32-33)
	- TSFM: s = forecast / in-sample monthly volatility, capped at ±2; long s > 0, short s <= 0, each leg divided by its sum (Eq. 9-10, p. 33)
	- CSFM: same with the cross-sectional median forecast subtracted first (Eq. 11, p. 34)

### Why
- **Koijen 2013**: used in prior work, and correlated with other weightings (p. 18).
- **Daniel 2014**: spread weighting invests more where differentials are larger (p. 10).
- **Brunnermeier 2008**: looks at carry against returns at portfolio level (p. 11).
- **Clarida 2009**: more currencies lower the volatility (p. 6, 8).
- **Gorton 2007**: a half/half sort controls cross-sectional dependence and is nonparametric (p. 16, 19).
- **Lustig 2013**: not argued; follows Lustig and Verdelhan (2007) (p. 10).
- **Menkhoff 2016**
	- Linear weights allow an exact decomposition of returns across signal parts (p. 13).
	- Rank weights give outliers less weight and keep the amount invested equal across signals (p. 14).
- **Chernov 2020**: not argued; follows prior carry and value-momentum papers. High-minus-low portfolios named as the alternative, not tested (p. 15).
- **Kosch 2026**: a transparent baseline, not a claim that one contract is optimally diversified (p. 10)
- **Lustig 2008**: not argued (p. 8).
- **Asness 2013**: ranks limit the influence of outliers; raw signal weights are similar and slightly better, not shown. The factor beats the spread because weights are linear in the signal and all securities are held (p. 10-11)
- **Oliveira 2025**: long-only is best except in economic difficulty, where shorts pay (p. 15)
- **Kagkadis 2023**
	- LSS looks at the extremes of the forecast distribution and ignores factors in the middle (p. 33-34)
	- TSFM trades the whole universe and lets the sign decide the side (p. 34)
	- CSFM still pays if forecasts rank well but have the wrong sign (p. 34)

### Evidence
- **Koijen 2013**: no test of the weighting itself.
	- Top and bottom 20-30% portfolios said to give robust results, not shown (p. 18).
- **Daniel 2014**: real data, in-sample, gross, G10 1976-2013
	- Mean return: EQ 3.96%, SPD 6.60% (Tables 1-2).
	- Worst month: SPD -7.26%, the worst of six strategies (p. 12).
	- Worst drawdown: EQ 12.0% over 94 days, SPD 21.5% over 163 days (p. 30).
	- Option-hedged, 2000-2013: SPD alpha significant, EQ not (p. 26).
- **Brunnermeier 2008**: real data, in-sample, gross, 1986-2006
	- Sharpe 0.592 (2x2 weekly) to 0.784 (3x3 quarterly) (Table 2).
- **Clarida 2009**: real data, in-sample, 1990-2009, gross or net not stated
	- All currencies: as N goes from 1 to 5, volatility falls and mean falls from 4.98% to 3.28% (p. 8; Table 1).
- **Gorton 2007**: no test of the weighting itself.
- **Lustig 2013**: no test of the weighting itself; real data, in-sample, gross, G10 1975-2015.
	- Three-portfolio rate deviation spread, currency leg: 2.66% a year, Sharpe 0.36 (Table 3B).
	- Per-country sign rule, equal-weighted, currency leg: 2.59%, Sharpe 0.47 (Table 2A).
- **Menkhoff 2016**: real data, 1976-2014, 22 currencies, value signal, gross.
	- Sharpe: quartile HML 0.44, rank 0.50, linear 0.51 (Table 4).
	- Volatility: HML 8.93%, rank 7.27%, linear 4.57% (Table 4).
	- Fundamental-adjusted value: Sharpe 0.79-0.91 with both linear and rank weights (Table 5).
- **Chernov 2020**: no test of the weighting itself; real data, in-sample, gross, G10 1985-2020.
	- Rank-weighted strategies: Sharpe 0.175 (CS-Mom 12) to 0.529 (CS-Value) (Table 2B).
- **Kosch 2026**: real data, out of sample, net of 8.6 bps one way
	- Top-1 SSA long: cumulative -32.41%, MaxDD -0.605; benchmark equal-weight long +14.30%, -0.415 (Table 2)
	- The leading contract is selected 53% to 77% of months on average (Table 7)
- **Lustig 2008**: no test of the weighting itself; real data, in-sample, net of bid-ask, 11/1983-03/2008.
	- Six-portfolio spread 4.83% a year, Sharpe 0.54; developed set of five portfolios 3.46%, 0.40 (Table 1).
- **Asness 2013**: real data, in-sample, gross, to July 2011
	- Currency value: factor Sharpe 0.44, spread 0.34 (Table I Panel B)
	- Currency momentum: factor 0.32, spread 0.34 (Table I Panel B)
	- All classes: value 0.73 vs 0.72, momentum 0.81 vs 0.76 (Table I Panel B)
- **Oliveira 2025**: real data, walk-forward, gross, 2004 to 2022
	- Ridge forecasts, l = 3: lo Sharpe 1.505, mx 1.330, los 1.051, lns 0.953 (Table 6)
	- Naive forecasts, l = 4: lo 1.065, los 0.788, mx 0.746, lns 0.734 (Table 4)
	- Maximum drawdown: ridge lo about -4.4 against lns -13 to -27 (Table 6)
- **Kagkadis 2023**: real data, out of sample, gross, 72 factors, 1990-2019, forecasts from PCA with LASSO
	- Monthly return: LSS 1.47%, TSFM 0.97%, CSFM 0.95% (Table 4)
	- Monthly Sharpe: LSS 0.18, TSFM 0.19, CSFM 0.19 (Table 4)
	- Maximum drawdown: LSS 16.76%, TSFM 13.93%, CSFM 12.16% (Table 4)

### Limits
- **Koijen 2013**
	- No transaction costs.
- **Daniel 2014**
	- No transaction costs (p. 4).
	- Spread weighting brings the deepest drawdown (p. 30).
- **Brunnermeier 2008**
	- No volatility scaling (p. 11).
- **Clarida 2009**
	- Rebalancing frequency and costs not stated.
- **Gorton 2007**
	- Treatment of an odd number of commodities not stated; only 7 commodities in December 1969 (p. 16).
- **Lustig 2013**
	- Number of countries per portfolio not stated.
	- No transaction costs.
- **Menkhoff 2016**
	- Linear weights: the amount invested varies across signals, so mean returns are not directly comparable (p. 13).
	- Rank weights: no exact decomposition (p. 14).
	- Rank scaling stated both as absolute sum 1 and as one dollar long, one dollar short (p. 14).
	- No transaction costs.
- **Chernov 2020**
	- One weighting scheme only; no transaction costs (whole paper).
- **Kosch 2026**
	- Forces a position when forecasts are small or of the wrong sign (p. 9-10)
	- Positive bootstrap means coexist with negative medians and deep drawdowns (Table 3)
- **Lustig 2008**
	- Number of currencies runs from 9 in 1983 to 26 in 2008, maximum 34 (p. 8).
	- No volatility scaling.
- **Asness 2013**
	- Naive monthly rebalancing whatever the expected gain per amount traded; no costs (p. 30)
- **Oliveira 2025**
	- Long-short with forecasts always opens both legs whatever their size (p. 15)
	- Only 10 US equity ETFs, l not chosen out of sample (p. 16)
	- No costs (whole paper)
- **Kagkadis 2023**
	- LSS ignores factors in the middle; TSFM can end up long only or short only (p. 33-34)
	- No transaction costs or turnover (whole paper)
	- Volatility is the in-sample monthly volatility of each factor (p. 33)

## Sources

- [[2013 - Koijen Moskowitz Pedersen et al - Carry]] (Koijen 2013)
- [[2014 - Daniel Hodrick Lu - The Carry Trade Risks and Drawdowns]] (Daniel 2014)
- [[2008 - Brunnermeier Nagel Pedersen - Carry Trades and Currency Crashes]] (Brunnermeier 2008)
- [[2009 - Clarida Davis Pedersen - Currency Carry Trade Regimes Beyond the Fama Regression]] (Clarida 2009)
- [[2007 - Gorton Hayashi Rouwenhorst - The Fundamentals of Commodity Futures Returns]] (Gorton 2007)
- [[2013 - Lustig Stathopoulos Verdelhan - The Term Structure of Currency Carry Trade Risk Premia]] (Lustig 2013)
- [[2016 - Menkhoff Sarno Schmeling et al - Currency Value]] (Menkhoff 2016)
- [[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks]] (Chernov 2020)
- [[2026 - Kosch Forsberg - Seasonal Trading in Commodity Futures Evidence from Regression and Singular Spectrum]] (Kosch 2026)
- [[2008 - Lustig Roussanov Verdelhan - Common Risk Factors in Currency Markets]] (Lustig 2008)
- [[2013 - Asness Moskowitz Pedersen - Value and Momentum Everywhere]] (Asness 2013)
- [[2025 - Oliveira Sandfelder Fujita et al - Tactical Asset Allocation with Macroeconomic Regime Detection]] (Oliveira 2025)
- [[2023 - Kagkadis Nolte Nolte et al - Factor Timing with Portfolio Characteristics]] (Kagkadis 2023)
