---
type: diagnostic
kind: attribution
aliases: [hedging out unpriced risk, hedged strategy, conditional beta hedge, systematic and idiosyncratic split, hedging portfolio, Daniel-Mota-Rottke-Santos hedge, covariance-sorted hedge portfolio]
sources: 2
---

# Priced and unpriced component split

> [!summary]
> How much of a strategy's return variation is compensated risk, and does the strategy improve once the uncompensated part is hedged out?

## How it works

- **How**: pick a pricing factor, a tradeable portfolio meant to carry all the priced risk of the assets. Each period, estimate the strategy's conditional beta on that factor from the asset covariance matrix and the two sets of weights known at t. The priced (hedged) component is beta times the factor return; the residual, strategy minus that, is the unpriced (hedging) component.
- **Reading**: if the factor is right, the unpriced component averages zero and the priced component has a higher Sharpe than the strategy. A low R² of the strategy on the factor means most of its variation is not compensated. Links of a strategy to macro variables can then be traced to one of the two parts.
- **Data needed**: strategy weights per asset, a conditional covariance matrix of the assets, the pricing factor's weights and returns.
- **Variant**: covariance-sorted hedge portfolio added to a characteristic factor.

## What the sources say

### Parameters
- **Chernov 2020**
	- Factor: the real-time mean-variance portfolio of nine G10 currencies vs USD (Eq. 9, p. 13).
	- β = w'Vw_U / w_U'Vw_U, with V the conditional covariance (p. 21).
	- Hedged = β R^U; hedging residual = R^P - β R^U, monthly (p. 21).
- **Liu 2019**: size bins at 30% and 70%, then three bins on expected covariance with the size factor over the past 365 days; equal-weighted hedge portfolio (p. 34)

### Why
- **Chernov 2020**: strategy R² on the factor is low, so a large unpriced part can be removed to raise performance, following Daniel et al. (2020) for equities (p. 20).
- **Liu 2019**: characteristic sorts carry unpriced risk; removing it may raise performance, following Daniel et al. (2018) (p. 34)

### Evidence
- **Chernov 2020**: real data, January 1985 to May 2020, expanding-window estimates, gross
	- Hedged Sharpe ≈1.1 for CS-Carry vs 0.469 original; ≈1.07 TS-Carry vs 0.685 (≈ Fig. 1; Table 2B).
	- Dollar strategy: hedged ≈0.22 vs 0.258 original (≈ Fig. 1).
	- "GRS hedged" joint test, p = 0.475; the paper's wording of what it tests is ambiguous (p. 21; Table 3).
	- CS-Carry relates to intermediary capital and FX variance (t 3.48, -6.63), its unpriced part too (t 3.57, -4.75), the factor not (Table 5B).
- **Liu 2019**: real data, in-sample
	- Squared weekly Sharpe of the size factor 0.057 to 0.076; momentum unchanged (p. 34)

### Limits
- **Chernov 2020**
	- Unpriced residual Sharpe ≈0.16 to ≈0.33 for six of nine strategies, not zero (≈ Fig. 1).
	- Hedging needs the full factor model; no costs of trading the factor shown (whole paper).
	- Volatility of the hedged portfolios not reported.
- **Liu 2019**
	- Hedge portfolio returns not shown (p. 34)
	- Momentum loadings may be too transient to hedge (p. 34-35)

## Sources

- [[2022 - Chernov Dahlquist Lochstoer - Pricing Currency Risks]] (Chernov 2020)
- [[2019 - Liu Tsyvinski Wu - Common Risk Factors in Cryptocurrency]] (Liu 2019)
