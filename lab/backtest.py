"""
The desk's backtest engine for books of perpetual futures, at any bar size: day, hour, minute.
Weights in, P&L per bar out. Written once, tested once; every strategy calls it.

Timing convention (the same at every bar size):
    - Bars are indexed by their open time. A row of `weights` dated t is traded at the close of bar t
      (for daily bars, 00:00 UTC of the next day). The new position earns the price return of the bars after.
    - Funding (or any carry paid in prints): a print belongs to whoever holds the position at its time. A print at
      exactly the close of bar t is paid by the position held during bar t (the old one). A bar with no print pays
      nothing: most hours and minutes have no funding.
    - Between two rebalances the number of contracts is fixed, so the weight drifts with the price.

Prices: the mark price (signals, P&L, liquidation), with the last price as a fallback where the mark is missing,
counted. Costs: cost_bp per unit of notional traded, each way.

Liquidation (isolated margin): with `leverage`, each position gets margin = notional / leverage at each rebalance,
where it is reset. A long is liquidated when a bar's mark low reaches ref x (1 - 1/leverage + maintenance), a short
when a bar's mark high reaches ref x (1 + 1/leverage - maintenance), ref being the price at the last rebalance. The
position is closed at that price, the maintenance margin and the cost of the forced trade are lost on top, and the
name stays flat until the next rebalance.

Delisting: a held name with no price after its last bar is closed at its last mark close, with the cost of the exit.

Bars: the daily panel of lab.data ("crypto_daily": date, mark_*, last-price columns) is read as it is. Intraday
panels ("crypto_1h", "crypto_1m") have a "time" column and the same price columns.
"""
from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class Result:
    daily: pd.DataFrame            # per bar: price, funding, cost, liquidation, total, by leg, traded (name kept for daily use)
    positions: pd.DataFrame        # weight held at the start of each bar (sampled once a day for intraday bars)
    trades: pd.DataFrame           # per rebalance: traded, gross, net, names long, names short
    liquidations: pd.DataFrame     # time, symbol, side, weight, ref, trigger
    by_name: pd.DataFrame          # per symbol: price, funding, cost, liquidation P&L over the run
    notes: dict = field(default_factory=dict)


def _bars(bars):
    """Standard columns: time, symbol, close, high, low (mark), and close_last for the fallback."""
    tcol = "date" if "date" in bars.columns else "time"
    b = pd.DataFrame({"time": pd.DatetimeIndex(bars[tcol]), "symbol": bars["symbol"].to_numpy()})
    for c in ["close", "high", "low"]:
        mark, last = f"mark_{c}", c
        b[c] = bars[mark].to_numpy() if mark in bars else bars[last].to_numpy()
        b[c + "_last"] = bars[last].to_numpy() if (mark in bars and last in bars) else np.nan
    return b, tcol == "date"


def _infer_freq(times, is_daily):
    if is_daily:
        return "D"
    step = pd.Series(np.sort(np.unique(times))).diff().dropna().min()
    return "min" if step < pd.Timedelta(hours=1) else "h"


def backtest(weights, bars, funding=None, cost_bp=10.0, band=0.0, band_to="edge", leverage=None, maintenance=0.005,
             liquidation_cost_bp=None, end=None, freq=None):
    """
    weights   DataFrame: index = trade bars (their open time; dates for daily bars), columns = symbols, values =
              target position in units of capital (0.05 = 5% of capital long). Only rebalance bars. NaN means 0.
    bars      price panel already cut by lab.data.load: crypto_daily, or an intraday panel with a "time" column.
    funding   prints (symbol, time, rate), already cut by lab.data.load; None for no carry.
    cost_bp   cost per unit of notional traded, one way, in basis points.
    band      no-trade band, as a share of the target: a name trades only if |target - held| > band x |target|,
              then to the edge of the band (band_to="edge") or to the target (band_to="target").
    leverage  isolated-margin leverage per position: a number, "gross" (the gross book of each rebalance), or a
              Series indexed by rebalance bar. None: no liquidation check.
    liquidation_cost_bp  cost on the liquidated notional, on top of the maintenance margin; default cost_bp.
    end       last bar of the backtest (default: last bar of `bars`).
    freq      bar size, "D", "h" or "min"; inferred when None.
    """
    b, is_daily = _bars(bars)
    freq = freq or _infer_freq(b["time"], is_daily)
    weights = weights.sort_index().fillna(0.0)
    weights.index = pd.DatetimeIndex(weights.index).floor(freq)
    symbols = [c for c in weights.columns if (weights[c] != 0).any()]
    weights = weights[symbols]
    b = b[b["symbol"].isin(symbols)]
    start = weights.index.min()
    end = pd.Timestamp(end) if end is not None else b["time"].max()
    times = pd.date_range(start, end, freq=freq)

    def panel(col):
        return b.pivot_table(index="time", columns="symbol", values=col, aggfunc="last").reindex(index=times, columns=symbols)

    px, hi, lo = panel("close"), panel("high"), panel("low")
    fb = int((px.isna() & panel("close_last").notna()).to_numpy().sum())
    px, hi, lo = px.fillna(panel("close_last")), hi.fillna(panel("high_last")), lo.fillna(panel("low_last"))
    last_valid = px.apply(lambda s: s.last_valid_index())                  # NaT for a name with no price at all in the window
    last_pos = np.array([times.get_loc(i) if pd.notna(i) else -1 for i in last_valid])
    no_price = [s for s, i in last_valid.items() if pd.isna(i)]            # weighted but never priced: never traded
    ret = (px / px.ffill().shift(1) - 1).fillna(0.0).to_numpy()

    if funding is not None and len(funding):
        f = funding[funding["symbol"].isin(symbols)]
        acct = (f["time"] - pd.Timedelta(microseconds=1)).dt.floor(freq)        # a print at a bar's close belongs to that bar
        fund = f.assign(bar=acct).groupby(["bar", "symbol"])["rate"].sum().unstack().reindex(index=times, columns=symbols)
        fund = fund.fillna(0.0).to_numpy()
    else:
        fund = np.zeros((len(times), len(symbols)))

    P, H, L = px.to_numpy(), hi.to_numpy(), lo.to_numpy()
    reb = {t: weights.loc[t].to_numpy() for t in weights.index if t in times}
    liq_cost = (cost_bp if liquidation_cost_bp is None else liquidation_cost_bp) / 1e4
    n, k = len(times), len(symbols)
    cur, ref, lev = np.zeros(k), np.full(k, np.nan), np.full(k, np.nan)
    daily_rows = times.normalize() != np.roll(times.normalize(), 1) if freq != "D" else np.ones(n, bool)
    held_sample = []
    out = np.zeros((n, 9))
    per_name = np.zeros((k, 4))          # price, funding, cost, liquidation
    trades, liqs = [], []
    dead_exit = 0

    for i, t in enumerate(times):
        h = cur.copy()
        if daily_rows[i]:
            held_sample.append((t, h.copy()))
        gone = (h != 0) & np.isnan(P[i]) & (last_pos < i) & (last_pos >= 0)
        if gone.any():
            c = np.abs(h) * gone * cost_bp / 1e4
            out[i, 2] -= c.sum(); per_name[:, 2] -= c
            out[i, 8] += np.abs(h[gone]).sum()
            dead_exit += int(gone.sum())
            h[gone] = 0.0; cur[gone] = 0.0
        r = ret[i].copy()
        liq = np.zeros(k)
        if leverage is not None:
            mv = 1 / lev - maintenance
            hit = ((h > 0) & (L[i] <= ref * (1 - mv))) | ((h < 0) & (H[i] >= ref * (1 + mv)))
            for j in np.where(hit)[0]:
                trig = ref[j] * (1 - mv[j]) if h[j] > 0 else ref[j] * (1 + mv[j])
                prev = P[i - 1, j] if i > 0 and not np.isnan(P[i - 1, j]) else ref[j]
                r[j] = trig / prev - 1
                liq[j] = -abs(h[j]) * (trig / prev) * (maintenance + liq_cost)
                liqs.append((t, symbols[j], "long" if h[j] > 0 else "short", h[j], ref[j], trig))
        pr = h * r
        fu = -h * fund[i]                         # a long pays positive funding, a short collects it
        out[i, 0], out[i, 1], out[i, 3] = pr.sum(), fu.sum(), liq.sum()
        out[i, 4], out[i, 5] = pr[h > 0].sum(), pr[h < 0].sum()
        out[i, 6], out[i, 7] = fu[h > 0].sum(), fu[h < 0].sum()
        per_name[:, 0] += pr; per_name[:, 1] += fu; per_name[:, 3] += liq
        cur = h * (1 + r)
        cur[liq != 0] = 0.0
        if t in reb:
            tgt = reb[t].copy()
            tgt[np.isnan(P[i])] = 0.0
            if band > 0:
                lo_b, hi_b = tgt - band * np.abs(tgt), tgt + band * np.abs(tgt)
                inside = (cur >= lo_b) & (cur <= hi_b) & (tgt != 0)
                moved = np.clip(cur, lo_b, hi_b) if band_to == "edge" else tgt
                tgt = np.where(inside, cur, moved)
                tgt[reb[t] == 0] = 0.0
            trade = np.abs(tgt - cur)
            out[i, 2] -= trade.sum() * cost_bp / 1e4; per_name[:, 2] -= trade * cost_bp / 1e4
            out[i, 8] += trade.sum()
            cur = tgt
            ref = np.where(tgt != 0, P[i], np.nan)
            if leverage is not None:
                if isinstance(leverage, pd.Series):
                    L_now = float(leverage.loc[t])
                elif isinstance(leverage, str) and leverage == "gross":
                    L_now = float(np.abs(tgt).sum())
                else:
                    L_now = float(leverage)
                lev = np.where(tgt != 0, max(L_now, 1e-9), np.nan)
            trades.append((t, trade.sum(), np.abs(tgt).sum(), tgt.sum(), int((tgt > 0).sum()), int((tgt < 0).sum())))

    d = pd.DataFrame(out[:, :8], index=times, columns=["price", "funding", "cost", "liquidation", "price_long",
                                                         "price_short", "funding_long", "funding_short"])
    d.insert(4, "total", d[["price", "funding", "cost", "liquidation"]].sum(axis=1))
    d["traded"] = out[:, 8]
    hs = pd.DataFrame([x[1] for x in held_sample], index=[x[0] for x in held_sample], columns=symbols)
    return Result(
        daily=d,
        positions=hs,
        trades=pd.DataFrame(trades, columns=["date", "traded", "gross", "net", "names_long", "names_short"]).set_index("date"),
        liquidations=pd.DataFrame(liqs, columns=["date", "symbol", "side", "weight", "ref", "trigger"]),
        by_name=pd.DataFrame(per_name, index=symbols, columns=["price", "funding", "cost", "liquidation"]),
        notes={"freq": freq, "weighted_without_price": no_price, "price_fallback_bars": fb, "price_fallback_days": fb, "delisting_exits": dead_exit, "cost_bp": cost_bp,
               "band": band, "band_to": band_to, "leverage": leverage if not isinstance(leverage, pd.Series) else "series",
               "maintenance": maintenance, "liquidation_cost_bp": cost_bp if liquidation_cost_bp is None else liquidation_cost_bp},
    )
