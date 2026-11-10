"""
Where the P&L of a saved run comes from: by name, by day, and how concentrated it is.

    from lab.attribution import by_name, concentration
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

from lab.data import load

PPY = 365


def read_run(folder):
    folder = Path(folder)
    s = json.loads((folder / "summary.json").read_text())
    d = pd.read_parquet(folder / "daily.parquet")
    if len(d) > 1 and (d.index[1] - d.index[0]) < pd.Timedelta(days=1):     # intraday bars: read as daily sums
        d = d.resample("D").sum()
    return s, d.loc[s["start"]:s["end"]]


def by_name(folder, test_start):
    """Price and funding P&L per name, from the saved positions and the data (mark price, last as fallback)."""
    folder = Path(folder)
    if (folder / "by_name.csv").exists():                                   # computed by the engine, exact at any bar size
        c = pd.read_csv(folder / "by_name.csv", index_col=0)
        c["total"] = c["price"] + c["funding"]
        return c.sort_values("total", ascending=False)
    s, _ = read_run(folder)
    pos = pd.read_parquet(folder / "positions.parquet")
    open_test = s["period"] == "test"
    daily = load("crypto_daily", test_start=test_start, open_test=open_test)
    fund = load("crypto_funding", test_start=test_start, open_test=open_test)
    px = daily.pivot(index="date", columns="symbol", values="mark_close")
    px = px.fillna(daily.pivot(index="date", columns="symbol", values="close")).reindex(index=pos.index, columns=pos.columns)
    ret = (px / px.ffill().shift(1) - 1).fillna(0.0)
    f = fund[fund["symbol"].isin(pos.columns)]
    acct = (f["time"] - pd.Timedelta(microseconds=1)).dt.normalize()
    fr = f.assign(day=acct).groupby(["day", "symbol"])["rate"].sum().unstack().reindex(index=pos.index, columns=pos.columns).fillna(0.0)
    c = pd.DataFrame({"price": (pos * ret).sum(), "funding": (-pos * fr).sum()})
    c["total"] = c["price"] + c["funding"]
    return c.sort_values("total", ascending=False)


def concentration(d, names=None):
    """How much of the gross P&L a few days and a few names carry. d: the run's daily frame."""
    g = (d["price"] + d["funding"]).sort_values(ascending=False)
    tot = g.sum()
    n1 = max(1, int(round(len(g) * 0.01)))
    rest = (d["price"] + d["funding"]).drop(g.index[:n1])
    out = {
        "gross_pnl_pct": round(float(tot * 100), 2),
        "top_1pct_days": n1,
        "share_top_1pct_days": round(float(g.iloc[:n1].sum() / tot), 2) if tot > 0 else None,
        "share_top_10_days": round(float(g.iloc[:10].sum() / tot), 2) if tot > 0 else None,
        "gross_sharpe_without_top_1pct_days": round(float(rest.mean() / rest.std() * np.sqrt(PPY)), 2) if rest.std() > 0 else None,
        "top_10_days": [(str(i.date()), round(float(v * 100), 2)) for i, v in g.iloc[:10].items()],
    }
    if names is not None and tot > 0:
        out["share_top_5_names"] = round(float(names["total"].head(5).sum() / names["total"].sum()), 2)
    return out
