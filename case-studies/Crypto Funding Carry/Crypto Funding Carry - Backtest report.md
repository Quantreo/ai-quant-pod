# Crypto Funding Carry · Backtest report

Built 2026-10-25 from the saved runs, by `lab/report.py`. Sheet: [[Crypto Funding Carry]]. Every number comes from `results/`; nothing here is a verdict, the verdict is in Pass 2 of the sheet.

## Main run: train+validation · base

Gross Sharpe 1.383, net Sharpe 1.077 (t 2.15), volatility 20.1%, max drawdown -27.88%, turnover 44.9×/yr, funding share of gross 0.483, liquidations 27.

![[Crypto Funding Carry - main.png]]

## By year

|      |   Gross Sharpe |   Net Sharpe |   Price % |   Funding % |   Costs % |   Liquidations % |
|-----:|---------------:|-------------:|----------:|------------:|----------:|-----------------:|
| 2021 |           3.18 |         2.96 |     57.79 |       10.59 |     -4.58 |            -0.12 |
| 2022 |          -0.63 |        -0.92 |    -26.21 |       14.45 |     -5.23 |            -0.21 |
| 2023 |           0.76 |         0.4  |     -5.32 |       21.65 |     -7.36 |            -0.48 |
| 2024 |           2.08 |         1.72 |     31.1  |        6.87 |     -6.14 |            -0.27 |

## By leg (% of capital)

|               |   total |
|:--------------|--------:|
| price_long    |  126.71 |
| price_short   |  -69.34 |
| funding_long  |   20.03 |
| funding_short |   33.53 |

## Runs compared

![[Crypto Funding Carry - compare.png]]

| period           | variant        | start      | end        |   gross_sharpe |   net_sharpe |   net_t_stat |   net_vol_pct |   max_drawdown_pct |   turnover_per_year |   funding_share_of_gross |   liquidations | run_id                                          |
|:-----------------|:---------------|:-----------|:-----------|---------------:|-------------:|-------------:|--------------:|-------------------:|--------------------:|-------------------------:|---------------:|:------------------------------------------------|
| train+validation | base           | 2021-01-03 | 2024-12-31 |          1.383 |        1.077 |         2.15 |         20.1  |             -27.88 |                44.9 |                    0.483 |             27 | 20261025-153304-train+validation-base           |
| train            | base           | 2021-01-03 | 2023-12-31 |          1.179 |        0.887 |         1.54 |         20.69 |             -27.88 |                44   |                    0.64  |             22 | 20261025-151935-train-base                      |
| train+validation | stress-short40 | 2021-01-03 | 2024-12-31 |          1.383 |        0.838 |         1.67 |         20.13 |             -31.98 |                44.9 |                    0.483 |             27 | 20261025-153306-train+validation-stress-short40 |
| train            | stress-both20  | 2021-01-03 | 2023-12-31 |          1.179 |        0.738 |         1.28 |         20.7  |             -30.6  |                44   |                    0.64  |             22 | 20261025-151943-train-stress-both20             |
| train            | base-delay1    | 2020-07-06 | 2023-12-31 |          0.794 |        0.572 |         1.07 |         22.07 |             -35.4  |                46.5 |                    0.902 |             21 | 20261023-095319-train-base-delay1               |
| train+validation | base-todaytop  | 2020-07-05 | 2024-12-31 |          0.388 |        0.182 |         0.39 |         21.46 |             -48.72 |                40.4 |                    0.86  |             29 | 20261023-095317-train+validation-base-todaytop  |
