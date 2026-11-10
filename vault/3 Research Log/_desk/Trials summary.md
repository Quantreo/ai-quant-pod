# Trials summary · 2026-11-09

All rows: 16; tries (counted): 4; strategies: 3.

## Tries by strategy

| strategy                | family   | asset       |   tries |
|:------------------------|:---------|:------------|--------:|
| Bond Trend Demeaned     | trend    | rates       |       1 |
| Crypto Low-MAX Long Leg | low-vol  | crypto      |       1 |
| ETF TSMOM 12-Month      | trend    | multi-asset |       2 |

## Tries by family and by asset

| family   |   tries |
|:---------|--------:|
| low-vol  |       1 |
| trend    |       3 |

| asset       |   tries |
|:------------|--------:|
| crypto      |       1 |
| multi-asset |       2 |
| rates       |       1 |

## Luck

Best gross Sharpe of the tries against the best of N_eff tries with no skill (Bailey and Lopez de Prado).

| Group | N | mean rho | N_eff | years | luck line | best gross Sharpe | above luck |
| --- | --- | --- | --- | --- | --- | --- | --- |
| desk | 4 | 0.60 | 1.4 | 11.4 | 0.05 | 0.59 (ETF TSMOM 12-Month, base, train) | +0.54 |
| family: low-vol | 1 | 0.00 | 1.0 | 3.0 | 0.00 | 0.24 (Crypto Low-MAX Long Leg, base, train) | +0.24 |
| family: trend | 3 | 0.60 | 1.4 | 11.9 | 0.03 | 0.59 (ETF TSMOM 12-Month, base, train) | +0.56 |
| family and asset: low-vol · crypto | 1 | 0.00 | 1.0 | 3.0 | 0.00 | 0.24 (Crypto Low-MAX Long Leg, base, train) | +0.24 |
| family and asset: trend · multi-asset | 2 | 0.94 | 1.0 | 13.4 | -0.16 | 0.59 (ETF TSMOM 12-Month, base, train) | +0.75 |
| family and asset: trend · rates | 1 | 0.00 | 1.0 | 10.9 | 0.00 | -0.21 (Bond Trend Demeaned, base, train) | -0.21 |

## Budget of tries (per family and asset, 10 each)

| family   | asset       |   tries |   budget |   left | status   |
|:---------|:------------|--------:|---------:|-------:|:---------|
| low-vol  | crypto      |       1 |       10 |      9 | open     |
| trend    | multi-asset |       2 |       10 |      8 | open     |
| trend    | rates       |       1 |       10 |      9 | open     |
