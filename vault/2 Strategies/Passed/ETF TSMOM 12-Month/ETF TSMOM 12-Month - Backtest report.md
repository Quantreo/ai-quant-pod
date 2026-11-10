# ETF TSMOM 12-Month · Backtest report

Built 2026-11-09 from the saved runs, by `lab/report.py`. Sheet: [[ETF TSMOM 12-Month]]. Every number comes from `results/`; nothing here is a verdict, the verdict is in Pass 2 of the sheet.

## Main run: test · base

Gross Sharpe 0.632, net Sharpe 0.572 (t 1.36), volatility 7.76%, max drawdown -17.48%, turnover 7.5×/yr, funding share of gross -0.083, liquidations 0.

![[ETF TSMOM 12-Month - main.png]]

## By year

|      |   Gross Sharpe |   Net Sharpe |   Price % |   Funding % |   Costs % |   Liquidations % |
|-----:|---------------:|-------------:|----------:|------------:|----------:|-----------------:|
| 2021 |           0.93 |         0.88 |      6.14 |       -0.02 |     -0.29 |                0 |
| 2022 |           1.17 |         1.14 |     11.16 |        1.16 |     -0.35 |                0 |
| 2023 |          -0.92 |        -1.03 |     -6.83 |        1.76 |     -0.57 |                0 |
| 2024 |           0.34 |         0.27 |      4.19 |       -1.7  |     -0.56 |                0 |
| 2025 |           0.52 |         0.46 |      6.17 |       -2.11 |     -0.49 |                0 |
| 2026 |           1.43 |         1.37 |      9.28 |       -1.4  |     -0.34 |                0 |

## By leg (% of capital)

|               |   total |
|:--------------|--------:|
| price_long    |   35.85 |
| price_short   |   -5.72 |
| funding_long  |  -16.89 |
| funding_short |   14.58 |

## Runs compared

![[ETF TSMOM 12-Month - compare.png]]

| period           | variant   | start      | end        |   gross_sharpe |   net_sharpe |   net_t_stat |   net_vol_pct |   max_drawdown_pct |   turnover_per_year |   funding_share_of_gross |   liquidations | run_id                                |
|:-----------------|:----------|:-----------|:-----------|---------------:|-------------:|-------------:|--------------:|-------------------:|--------------------:|-------------------------:|---------------:|:--------------------------------------|
| test             | base      | 2021-01-29 | 2026-09-30 |          0.632 |        0.572 |         1.36 |          7.76 |             -17.48 |                 7.5 |                   -0.083 |              0 | 20261109-112907-test-base             |
| train+validation | base      | 2006-01-31 | 2020-12-31 |          0.457 |        0.409 |         1.58 |          8.09 |             -16.07 |                 6.6 |                   -0.082 |              0 | 20261109-103855-train+validation-base |
