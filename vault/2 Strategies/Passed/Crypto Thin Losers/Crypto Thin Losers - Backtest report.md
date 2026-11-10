# Crypto Thin Losers · Backtest report

Built 2026-10-24 from the saved runs, by `lab/report.py`. Sheet: [[Crypto Thin Losers]]. Every number comes from `results/`; nothing here is a verdict, the verdict is in Pass 2 of the sheet.

## Main run: train · base-tiered

Gross Sharpe 1.75, net Sharpe 1.377 (t 2.38), volatility 25.89%, max drawdown -20.67%, turnover 79.6×/yr, funding share of gross -0.027, liquidations 23.

![[Crypto Thin Losers - main.png]]

## By year

|      |   Gross Sharpe |   Net Sharpe |   Price % |   Funding % |   Costs % |   Liquidations % |
|-----:|---------------:|-------------:|----------:|------------:|----------:|-----------------:|
| 2021 |           1.41 |         1.21 |     42.91 |        1.13 |     -6.39 |            -0.02 |
| 2022 |           1.99 |         1.58 |     49.86 |       -3.29 |     -9.44 |            -0.06 |
| 2023 |           2.04 |         1.45 |     47.04 |       -1.48 |    -12.99 |            -0.34 |

## By leg (% of capital)

|               |   total |
|:--------------|--------:|
| price_long    |  228.48 |
| price_short   |  -88.67 |
| funding_long  |  -16.5  |
| funding_short |   12.87 |

## Runs compared

![[Crypto Thin Losers - compare.png]]

| period     | variant     | start      | end        |   gross_sharpe |   net_sharpe |   net_t_stat |   net_vol_pct |   max_drawdown_pct |   turnover_per_year |   funding_share_of_gross |   liquidations | run_id                                 |
|:-----------|:------------|:-----------|:-----------|---------------:|-------------:|-------------:|--------------:|-------------------:|--------------------:|-------------------------:|---------------:|:---------------------------------------|
| train      | base-tiered | 2021-01-01 | 2023-12-31 |          1.75  |        1.377 |         2.38 |         25.89 |             -20.67 |                79.6 |                   -0.027 |             23 | 20261023-164156-train-base-tiered      |
| validation | base        | 2024-01-01 | 2024-12-31 |          0.865 |        0.331 |         0.33 |         22.7  |             -24.33 |                98.1 |                   -0.037 |             23 | 20261023-164211-validation-base        |
| validation | base-delay1 | 2024-01-02 | 2024-12-31 |          0.836 |        0.323 |         0.32 |         23.18 |             -25.4  |                96.5 |                   -0.029 |             22 | 20261023-164225-validation-base-delay1 |
| validation | v1          | 2024-01-01 | 2024-12-31 |          0.807 |        0.258 |         0.26 |         21.34 |             -28.97 |                96.3 |                   -0.041 |             13 | 20261023-164216-validation-v1          |
| validation | v2          | 2024-01-01 | 2024-12-31 |          1.093 |        0.373 |         0.37 |         22.04 |             -26.23 |               128.8 |                   -0.054 |             13 | 20261023-164220-validation-v2          |
