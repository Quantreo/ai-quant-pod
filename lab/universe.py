"""
Point-in-time universes: who could have been traded at each date, using only what was known at that date.

The data scripts keep every symbol, dead ones included. This module turns that into a universe with the rule
of a strategy's Pass 1. Every strategy calls the same function with its own parameters, so the look-ahead
checks are written once.

Convention: the universe at date t is known at the close of t (it uses the volume of day t) and is traded
after that close. A symbol that has no bar on t is out on t.
"""
from pathlib import Path

import pandas as pd

META = Path(__file__).resolve().parent.parent / "data" / "crypto" / "perps_meta.csv"


def crypto_universe(daily, top, volume_window=30, min_age_days=90, min_names=0, underlying=("COIN",)):
    """
    daily: data/crypto/perps_daily.parquet (columns date, symbol, quote_volume).
    Returns a boolean table, one row per calendar day, one column per symbol: True if in the universe.

    top            how many names, ranked by average quote volume
    volume_window  days in the volume average; a symbol needs that many days of volume to be ranked
    min_age_days   days since its first bar before a symbol can enter
    min_names      if fewer names are eligible on a day, the universe is empty that day (the book stays flat)
    underlying     which perps count: coins only by default; Binance also lists stocks, metals and indices.
                   None keeps every type.
    """
    if underlying is not None:
        meta = pd.read_csv(META)
        keep = set(meta.loc[meta["underlying_type"].isin(underlying), "symbol"])
        daily = daily[daily["symbol"].isin(keep)]
    vol = daily.pivot(index="date", columns="symbol", values="quote_volume").sort_index().asfreq("D")
    vol = vol.where(vol > 0)                                               # a day with no trade is a day out
    avg = vol.rolling(volume_window, min_periods=volume_window).mean()
    first = vol.notna().idxmax()                                           # first day with a bar, per symbol
    age = pd.DataFrame(vol.index.values[:, None] - first.values[None, :], index=vol.index, columns=vol.columns)
    eligible = vol.notna() & avg.notna() & (age >= pd.Timedelta(days=min_age_days))
    rank = avg.where(eligible).rank(axis=1, ascending=False, method="first")
    universe = rank <= top
    universe[eligible.sum(axis=1) < max(min_names, 1)] = False
    return universe
