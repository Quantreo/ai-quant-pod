# Trials summary · 2026-11-10

All rows: 44; tries (counted): 9; strategies: 5.

## Tries by strategy

| strategy                | family   | asset       |   tries |
|:------------------------|:---------|:------------|--------:|
| Bond Trend Demeaned     | trend    | rates       |       1 |
| Crypto Low-MAX Long Leg | low-vol  | crypto      |       1 |
| Crypto Thin Losers      | reversal | crypto      |       3 |
| ETF TSMOM 12-Month      | trend    | multi-asset |       2 |
| SPY Volatility Managed  | low-vol  | equities    |       2 |

## Tries by family and by asset

| family   |   tries |
|:---------|--------:|
| low-vol  |       3 |
| reversal |       3 |
| trend    |       3 |

| asset       |   tries |
|:------------|--------:|
| crypto      |       4 |
| equities    |       2 |
| multi-asset |       2 |
| rates       |       1 |

## Luck

Best gross Sharpe of the tries against the best of N_eff tries with no skill (Bailey and Lopez de Prado).

| Group | N | mean rho | N_eff | years | luck line | best gross Sharpe | above luck |
| --- | --- | --- | --- | --- | --- | --- | --- |
| desk | 9 | 0.35 | 2.4 | 10.9 | 0.20 | 1.75 (Crypto Thin Losers, base-tiered, train) | +1.55 |
| family: low-vol | 3 | 0.98 | 1.0 | 12.9 | -0.21 | 0.65 (SPY Volatility Managed, base, train) | +0.86 |
| family: reversal | 3 | 0.89 | 1.1 | 1.0 | -0.39 | 1.75 (Crypto Thin Losers, base-tiered, train) | +2.14 |
| family: trend | 3 | 0.60 | 1.4 | 11.9 | 0.03 | 0.59 (ETF TSMOM 12-Month, base, train) | +0.56 |
| family and asset: low-vol · crypto | 1 | 0.00 | 1.0 | 3.0 | 0.00 | 0.24 (Crypto Low-MAX Long Leg, base, train) | +0.24 |
| family and asset: low-vol · equities | 2 | 0.98 | 1.0 | 14.4 | -0.21 | 0.65 (SPY Volatility Managed, base, train) | +0.86 |
| family and asset: reversal · crypto | 3 | 0.89 | 1.1 | 1.0 | -0.39 | 1.75 (Crypto Thin Losers, base-tiered, train) | +2.14 |
| family and asset: trend · multi-asset | 2 | 0.94 | 1.0 | 13.4 | -0.16 | 0.59 (ETF TSMOM 12-Month, base, train) | +0.75 |
| family and asset: trend · rates | 1 | 0.00 | 1.0 | 10.9 | 0.00 | -0.21 (Bond Trend Demeaned, base, train) | -0.21 |

## Budget of tries (per family and asset, 10 each)

| family   | asset       |   tries |   budget |   left | status   |
|:---------|:------------|--------:|---------:|-------:|:---------|
| low-vol  | crypto      |       1 |       10 |      9 | open     |
| low-vol  | equities    |       2 |       10 |      8 | open     |
| reversal | crypto      |       3 |       10 |      7 | open     |
| trend    | multi-asset |       2 |       10 |      8 | open     |
| trend    | rates       |       1 |       10 |      9 | open     |
