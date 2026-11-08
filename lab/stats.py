"""
Summary numbers of a backtest run, the same for every strategy. The Analyst computes the rest.
"""
import numpy as np


def summary(result, ppy=365):
    d = result.daily
    if result.notes.get("freq", "D") != "D":                          # intraday bars: Sharpe and risk on daily sums
        d = d.resample("D").sum()
    if len(result.trades):
        d = d.loc[d.index >= result.trades.index.min()]              # from the first trade, its cost included
    years = len(d) / ppy
    gross = d["price"] + d["funding"]
    net = d["total"]
    sharpe = lambda r: float(r.mean() / r.std() * np.sqrt(ppy)) if r.std() > 0 else float("nan")
    eq = net.cumsum()
    traded = float(d["traded"].sum())
    return {
        "start": str(d.index.min().date()), "end": str(d.index.max().date()), "years": round(years, 2),
        "gross_sharpe": round(sharpe(gross), 3), "net_sharpe": round(sharpe(net), 3),
        "net_t_stat": round(float(net.mean() / net.std() * np.sqrt(len(net))), 2) if net.std() > 0 else None,
        "net_vol_pct": round(float(net.std() * np.sqrt(ppy) * 100), 2),
        "max_drawdown_pct": round(float((eq - eq.cummax()).min() * 100), 2),
        "pnl_price_pct": round(float(d["price"].sum() * 100), 2), "pnl_funding_pct": round(float(d["funding"].sum() * 100), 2),
        "pnl_cost_pct": round(float(d["cost"].sum() * 100), 2), "pnl_liquidation_pct": round(float(d["liquidation"].sum() * 100), 2),
        "funding_share_of_gross": round(float(d["funding"].sum() / gross.sum()), 3) if gross.sum() > 0 else None,
        "turnover_per_year": round(traded / years, 1) if years else None,
        "breakeven_cost_bp": round(float(gross.sum() / traded * 1e4), 1) if traded else None,
        "liquidations": int(len(result.liquidations)), "bar": result.notes.get("freq", "D"),
        "price_fallback_days": result.notes.get("price_fallback_days"), "delisting_exits": result.notes.get("delisting_exits"),
    }
