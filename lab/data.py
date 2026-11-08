"""
Load the desk's datasets, with the test period sealed.

Every strategy has a test period, fixed in its Pass 1 and looked at once, at the very end. This function cuts
every dataset just before it, so that nothing built on train and validation can see it by accident. Opening
the test period takes open_test=True: only the human passes it, once, when the strategy is ready to be judged.

    from lab.data import load
    daily = load("crypto_daily", test_start="2025-01-01")
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

# name: (file, time column, key columns)
DATASETS = {
    "crypto_daily": ("data/crypto/perps_daily.parquet", "date", ["symbol", "date"]),
    "crypto_funding": ("data/crypto/perps_funding.parquet", "time", ["symbol", "time"]),
    "crypto_mark_hourly": ("data/crypto/mark_hourly.parquet", "time", ["symbol", "time"]),
    "crypto_1h": ("data/crypto/perps_1h.parquet", "time", ["symbol", "time"]),
    "crypto_1m": ("data/crypto/perps_1m.parquet", "time", ["symbol", "time"]),
    "fx_daily": ("data/fx/fx_daily.parquet", "date", ["pair", "date"]),
    "rates": ("data/rates/rates_monthly.parquet", "date", ["currency", "date"]),
    "etf_daily": ("data/etf/etf_daily.parquet", "date", ["symbol", "date"]),
}


def load(name, test_start, open_test=False):
    """The dataset, strictly before test_start. open_test=True returns everything: for the human only."""
    path, time_col, key = DATASETS[name]
    df = pd.read_parquet(ROOT / path)
    if not open_test:
        df = df[df[time_col] < pd.Timestamp(test_start)]
    return df.sort_values(key).reset_index(drop=True)
