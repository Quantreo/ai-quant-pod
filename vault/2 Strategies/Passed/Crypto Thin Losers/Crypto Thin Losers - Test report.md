# Crypto Thin Losers · Backtest report

Built 2026-10-24 from the saved runs, by `lab/report.py`. Sheet: [[Crypto Thin Losers]]. Every number comes from `results/`; nothing here is a verdict, the verdict is in Pass 2 of the sheet.

## Main run: test · base

Gross Sharpe 0.844, net Sharpe 0.378 (t 0.5), volatility 23.85%, max drawdown -29.58%, turnover 89.0×/yr, funding share of gross -0.47, liquidations 0.

![[Crypto Thin Losers - Test - main.png]]

## By year

|      |   Gross Sharpe |   Net Sharpe |   Price % |   Funding % |   Costs % |   Liquidations % |
|-----:|---------------:|-------------:|----------:|------------:|----------:|-----------------:|
| 2025 |           0.83 |         0.34 |     25.58 |       -5.2  |    -12.06 |                0 |
| 2026 |           0.86 |         0.43 |     26.17 |      -11.34 |     -7.38 |                0 |

## By leg (% of capital)

|               |   total |
|:--------------|--------:|
| price_long    |  -45.04 |
| price_short   |   96.78 |
| funding_long  |    2.2  |
| funding_short |  -18.74 |

## Runs compared

![[Crypto Thin Losers - Test - compare.png]]

| period     | variant   | start      | end        |   gross_sharpe |   net_sharpe |   net_t_stat |   net_vol_pct |   max_drawdown_pct |   turnover_per_year |   funding_share_of_gross |   liquidations | run_id                          |
|:-----------|:----------|:-----------|:-----------|---------------:|-------------:|-------------:|--------------:|-------------------:|--------------------:|-------------------------:|---------------:|:--------------------------------|
| test       | base      | 2025-01-01 | 2026-09-30 |          0.844 |        0.378 |         0.5  |         23.85 |             -29.58 |                89   |                   -0.47  |              0 | 20261024-083811-test-base       |
| train      | base      | 2021-01-01 | 2023-12-31 |          1.75  |        1.377 |         2.38 |         25.89 |             -20.67 |                79.6 |                   -0.027 |             23 | 20261024-083824-train-base      |
| validation | base      | 2024-01-01 | 2024-12-31 |          0.865 |        0.331 |         0.33 |         22.7  |             -24.33 |                98.1 |                   -0.037 |             23 | 20261023-164211-validation-base |
