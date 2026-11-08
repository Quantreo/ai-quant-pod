"""
Look-ahead checks on a strategy's weights. The engine already makes a weight earn only the returns after
the close it is traded at; what it cannot see is a signal that reads the future while being computed
(a centred window, a wrong shift, the universe row of the trade day, a print after 00:00). These checks can.

    from lab.checks import truncation_test, delay_test
    truncation_test(build_weights, daily, funding, days, variant="base")

truncation_test: for a sample of trade days d, recompute the weights with the data cut at the close of d
(daily rows up to d, funding prints up to 00:00 of d+1). The row of d must be identical to the one computed
on the full data. Any difference means the weights of d used something that came after d.

delay_test: the same weights traded one day later. A strategy whose P&L collapses with a one-day delay is
either very fast (then Pass 1 says so) or leaking; the Analyst reads it, it is not a try.
"""
import numpy as np
import pandas as pd


def truncation_test(build_weights, daily, funding, days, n=12, seed=0, tol=1e-9, **kwargs):
    """build_weights(daily, funding, days, **kwargs) -> DataFrame of weights indexed by trade day."""
    full = build_weights(daily, funding, days, **kwargs)
    rng = np.random.default_rng(seed)
    live = [d for d in full.index if (full.loc[d].fillna(0) != 0).any()]
    picks = sorted(rng.choice(live, size=min(n, len(live)), replace=False)) if live else []
    rows = []
    for d in picks:
        d = pd.Timestamp(d)
        cut_daily = daily[daily["date"] <= d]
        cut_funding = funding[funding["time"] <= d + pd.Timedelta(days=1)]
        part = build_weights(cut_daily, cut_funding, [x for x in days if pd.Timestamp(x) <= d], **kwargs)
        a = full.loc[d].fillna(0.0)
        b = part.loc[d].reindex(a.index).fillna(0.0) if d in part.index else a * np.nan
        diff = float((a - b).abs().max())
        rows.append({"day": d.date(), "max_abs_diff": diff, "names": int((a != 0).sum()), "ok": bool(diff <= tol)})
    out = pd.DataFrame(rows)
    print(f"Truncation test on {len(out)} trade days: " + ("PASS" if len(out) and out["ok"].all() else "FAIL"))
    if len(out) and not out["ok"].all():
        print(out[~out["ok"]].to_string(index=False))
    return out


def delay_test(weights, days_late=1):
    """The same weights, traded days_late days later: run it through lab.backtest like any weights."""
    w = weights.copy()
    w.index = pd.DatetimeIndex(w.index) + pd.Timedelta(days=days_late)
    return w
