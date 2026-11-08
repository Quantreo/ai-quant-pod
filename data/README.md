# data

Scripts that download the market data of the pod. The data itself is never committed: each user builds it on their own machine, from the original public sources, for their own research.

```
poetry run python data/get_crypto_daily.py           # Binance USDT perps, daily, 2019-09 to 2026-09 -> data/crypto/
poetry run python data/get_fx_daily.py               # 9 FX majors against USD, daily (FRED H.10, noon NY), 2008-01 to 2026-09 -> data/fx/
poetry run python data/get_rates.py                  # G10 rates, T-bill, policy rates, CPI, US curve (FRED) -> data/rates/
poetry run python data/get_etf_daily.py              # about 220 ETFs (indexes, sectors, countries, bonds of every maturity, commodities...), daily, 2005-01 to 2026-09 (Yahoo Finance) -> data/etf/
```

Each script writes a quality report next to its files: read it once.

Raw data is read only. The test period is sealed by `lab.data.load` until a human opens it.

Each dataset has a data card in `vault/Toolbox/Data/`: source, licence, period, known gaps. The Data seat reads it before every check.
