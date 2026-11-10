"""
Crypto Thin Losers: built from Pass 1 v1 of vault/2 Strategies/Proposed/Crypto Thin Losers/Pass 1.md.

Among 14-day losers on Binance USDT perps, long the thin names (high Amihud), short the liquid ones (low Amihud),
equal weight, dollar neutral, 14 daily tranches, BTC beta hedge, vol target. The file decides the target weights;
the lab loads the data (test period sealed), builds the universe, computes the P&L and saves the run.

    poetry run python strategies/crypto_thin_losers.py --period train --variant base --check-lookahead
    poetry run python strategies/crypto_thin_losers.py --period train --variant base --gate   # 1.11 #1 to #4 (saves base + winners diagnostic)
    poetry run python strategies/crypto_thin_losers.py --period train --variant base --delay 1   # control
"""
import argparse, sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lab.backtest import backtest            # noqa: E402
from lab.checks import delay_test, truncation_test   # noqa: E402
from lab.data import load                    # noqa: E402
from lab.runs import save_run                # noqa: E402
from lab.universe import crypto_universe     # noqa: E402

NAME = "Crypto Thin Losers"

# 1.10 periods
TRAIN = ("2021-01-01", "2023-12-31")
VALIDATION = ("2024-01-01", "2024-12-31")
TEST_START = "2025-01-01"                     # never read here: lab.data.load cuts before it

# 1.4 universe + Data check: no volume floor (top above the number of listed names), age 180, min_names 1
TOP, VOLUME_WINDOW, MIN_AGE, MIN_NAMES = 1000, 14, 180, 1
STABLECOINS = ["USDCUSDT"]                    # Data check #1: dropped, close checked inside 0.97 to 1.03
HEDGE = "BTCUSDT"                             # 1.5 Hedge

# 1.5 base version
SIGNAL_DAYS = 14                              # 1.5 return signal and Amihud window, no skip
Q_LO, Q_HI = 0.30, 0.70                       # 1.5 Sort, 30/70 then 30/70 inside the group
HOLD = 14                                     # 1.5 Holding, 14 daily tranches (V2: 7)
BETA_WINDOW, BETA_LAGS = 60, 5                # 1.5 Hedge, 1.5b
VOL_TARGET, VOL_WINDOW, GROSS_CAP = 0.20, 60, 3.0   # 1.5 Sizing
COST_BP = 12.5                                # 1.7 central case: blended 5 bp liquid / 20 bp thin
BAND = 0.0                                    # Pass 1 has no band
MIN_LOSERS = 4                                # 1.5b Minimum cell: skip a formation under 4 losers ranked
FUNDING_GAP_NAMES = ["ICPUSDT", "TLMUSDT", "BNXUSDT"]   # Data check #3

VARIANTS = ["base", "v1", "v2", "winners", "depth"]   # 1.9 V1, V2; "winners" = 1.11 #3 spread, "depth" = 1.11 #1 control spread (1.5b)
THIN_BP, LIQUID_BP, HEDGE_BP = 20.0, 5.0, 5.0   # 1.5b cost tier: thin leg 20 bp [hypothesis], liquid leg and hedge 5 bp
LIQ_BP = 12.5                                 # forced trades (liquidation fee, delisting exit): tier not written in Pass 1, v1 figure kept


def rebalance_days(calendar):
    """1.5: a formation every day, traded at the close of that day."""
    return list(calendar)


def _panels(daily):
    d = daily[~daily["symbol"].isin(STABLECOINS)]
    cl = d.pivot(index="date", columns="symbol", values="mark_close").sort_index().asfreq("D")
    qv = d.pivot(index="date", columns="symbol", values="quote_volume").sort_index().asfreq("D")
    return cl, qv


def _formations(daily, variant, sort="seq", min_leg=1):
    """Formation weights f[d] (long thin = +1 in total, short liquid = -1), using data up to the close of d."""
    uni = crypto_universe(daily, top=TOP, volume_window=VOLUME_WINDOW, min_age_days=MIN_AGE, min_names=MIN_NAMES)
    cl, qv = _panels(daily)
    uni = uni.reindex(index=cl.index, columns=cl.columns).astype("boolean").fillna(False).astype(bool)
    ret1 = cl / cl.shift(1) - 1                                        # by dates: NaN across a gap
    mom = cl / cl.shift(SIGNAL_DAYS) - 1                               # 14-day return, no skip
    amihud = (ret1.abs() / qv.where(qv > 0)).rolling(SIGNAL_DAYS, min_periods=SIGNAL_DAYS).mean()
    if variant == "v1":
        illiq = -qv.rolling(SIGNAL_DAYS, min_periods=SIGNAL_DAYS).median()    # thin = low median volume
    else:
        illiq = amihud
    side = "high" if variant == "winners" else "low"
    # "depth": inside the losers, long the lowest 30% on 14-day return, short the highest 30% (1.5b)
    f = pd.DataFrame(0.0, index=cl.index, columns=cl.columns)
    cells = []
    for t in cl.index:
        ok = uni.loc[t] & mom.loc[t].notna() & illiq.loc[t].notna()
        if ok.sum() < 4:
            continue
        m = mom.loc[t][ok]
        grp = m[m <= m.quantile(Q_LO)] if side == "low" else m[m >= m.quantile(Q_HI)]
        if len(grp) < MIN_LOSERS:
            continue
        if sort == "ind":                                              # 1.5b stress: independent 30/70 on both signals
            a_all = illiq.loc[t][ok]
            thin = grp.index.intersection(a_all[a_all >= a_all.quantile(Q_HI)].index)
            liquid = grp.index.intersection(a_all[a_all <= a_all.quantile(Q_LO)].index)
        elif variant == "depth":
            g = grp
            thin = g[g <= g.quantile(Q_LO)].index
            liquid = g[g >= g.quantile(Q_HI)].index
        else:
            a = illiq.loc[t][grp.index]
            thin = a[a >= a.quantile(Q_HI)].index
            liquid = a[a <= a.quantile(Q_LO)].index
        if len(thin) < max(min_leg, 1) or len(liquid) < max(min_leg, 1):   # min_leg 5 = 1.5b stress "under 5 a leg"
            continue
        f.loc[t, thin] = 1.0 / len(thin)
        f.loc[t, liquid] = -1.0 / len(liquid)
        cells.append((t, len(grp), len(thin), len(liquid)))
    return f, ret1, uni, pd.DataFrame(cells, columns=["date", "group", "thin", "liquid"]).set_index("date")


def build_weights(daily, funding, days, variant="base", beta_window=BETA_WINDOW, beta_lags=BETA_LAGS, sort="seq", min_leg=1, hedge="btc"):
    """Weights per trade day, in units of capital, using only data up to the close of each day."""
    hold = 7 if variant == "v2" else HOLD
    f, ret1, uni, cells = _formations(daily, variant, sort, min_leg)
    book = f.rolling(hold, min_periods=1).sum() / hold                 # hold tranches, each 1/hold, fixed weights
    r = ret1.fillna(0.0)
    btc = r[HEDGE].to_numpy()
    cols = list(f.columns)
    bi = cols.index(HEDGE)
    if hedge == "ew20":                                                # 1.5b stress: equal-weight top 20 by 14-day volume
        top20 = crypto_universe(daily, top=20, volume_window=VOLUME_WINDOW, min_age_days=MIN_AGE, min_names=MIN_NAMES)
        top20 = top20.reindex(index=f.index, columns=cols).astype("boolean").fillna(False).astype(bool)
    Rall = r.to_numpy()
    out = {}
    idx = {t: i for i, t in enumerate(f.index)}
    for t in days:
        t = pd.Timestamp(t)
        if t not in idx:
            continue
        i = idx[t]
        w = book.iloc[i].to_numpy()
        if not (w != 0).any() or i < beta_window + beta_lags + 1:
            continue
        lo = i - beta_window + 1                                       # window of returns ending at t (inclusive)
        R = r.iloc[lo:i + 1].to_numpy()
        y = R @ w
        if hedge == "ew20":
            mem = np.where(top20.iloc[i].to_numpy())[0]
            if len(mem) == 0:
                continue
            hs = Rall[:, mem].mean(axis=1)                             # basket of today's top 20, past returns
        else:
            hs = btc
        X = np.column_stack([np.ones(beta_window)] + [hs[lo - k:i + 1 - k] for k in range(beta_lags + 1)])
        coef = np.linalg.lstsq(X, y, rcond=None)[0]
        beta = coef[1:].sum()                                          # today plus lags summed
        h = w.copy()
        if hedge == "ew20":
            h[mem] -= beta / len(mem)
        else:
            h[bi] -= beta
        hedged = y - beta * hs[lo:i + 1]
        sd = hedged.std(ddof=1) * np.sqrt(365)
        if not np.isfinite(sd) or sd <= 0:
            continue
        scale = VOL_TARGET / sd
        h = h * scale
        gross = np.abs(h).sum()
        if gross > GROSS_CAP:
            h = h * GROSS_CAP / gross
        out[t] = h
    return pd.DataFrame(out, index=cols).T.reindex(columns=cols)


def regression(y, x, lags=BETA_LAGS, nw=14):
    """y on x today plus lags (Dimson): intercept, OLS t, Newey-West t (nw lags), sum of betas."""
    X = pd.concat([x.shift(k) for k in range(lags + 1)], axis=1)
    X.columns = range(lags + 1)
    df = pd.concat([y.rename("y"), X], axis=1).dropna()
    A = np.column_stack([np.ones(len(df)), df[list(range(lags + 1))].to_numpy()])
    yy = df["y"].to_numpy()
    XtXi = np.linalg.inv(A.T @ A)
    b = XtXi @ A.T @ yy
    e = yy - A @ b
    n, k = A.shape
    t_ols = b[0] / np.sqrt(e @ e / (n - k) * XtXi[0, 0])
    S = (A * e[:, None]).T @ (A * e[:, None])
    for L in range(1, nw + 1):
        G = (A[L:] * e[L:, None]).T @ (A[:-L] * e[:-L, None])
        S += (1 - L / (nw + 1)) * (G + G.T)
    V = XtXi @ S @ XtXi
    return {"alpha_daily": b[0], "t_ols": t_ols, "t_nw": b[0] / np.sqrt(V[0, 0]), "beta_sum": b[1:].sum(), "n": n}


def tier_cost(res, w, daily, thin_bp=THIN_BP, hedge_cols=None):
    """1.5b cost tier from per-name traded notional: 20 bp on a trade in a net-long name (thin leg), 5 bp on a trade in a
    net-short name (liquid leg) and on the BTC hedge; forced trades (liquidation, delisting) keep LIQ_BP. The trade of a name on
    day t is |target - held after the bar's return|, rebuilt from the saved positions; its tier is the sign of the target, or of
    the held position when it is closed. Returns the daily tiered cost (positive number) and the reconstructed traded notional."""
    pos = res.positions
    cl = daily.pivot(index="date", columns="symbol", values="mark_close").sort_index().reindex(pos.index)
    cl = cl.reindex(columns=pos.columns)
    ret = (cl / cl.ffill().shift(1) - 1).fillna(0.0)
    pre = pos * (1 + ret)
    liq = res.liquidations
    for _, r in liq.iterrows():
        pre.loc[r["date"], r["symbol"]] = 0.0
    tgt = w.reindex(index=pos.index, columns=pos.columns).fillna(0.0)
    on = tgt.index.isin(w.index)
    tgt = tgt.where(~cl.isna(), 0.0)
    tgt.loc[~on] = pre.loc[~on]                                       # no rebalance that day: nothing traded
    trade = (tgt - pre).abs()
    sign = np.sign(tgt.where(tgt != 0, pre))
    bp = pd.DataFrame(np.where(sign > 0, thin_bp, LIQUID_BP), index=pos.index, columns=pos.columns)
    bp[HEDGE] = HEDGE_BP
    if hedge_cols is not None:
        bp[[c for c in hedge_cols if c in bp.columns]] = HEDGE_BP
    return (trade * bp / 1e4).sum(axis=1), trade.sum(axis=1)


def run(variant, period, start, end, daily, funding, cost_bp, delay=0, tiered=True, thin_bp=THIN_BP, **kw):
    cal = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
    days = [d for d in rebalance_days(cal) if pd.Timestamp(start) <= d <= pd.Timestamp(end)]
    w = build_weights(daily, funding, days, variant, **kw)
    if delay:
        w = delay_test(w, delay)
    if not tiered:
        res = backtest(w, daily, funding, cost_bp=cost_bp, band=BAND, leverage="gross", end=end)
    else:                                                              # engine at zero cost, then 1.5b tier from per-name trades
        res = backtest(w, daily, funding, cost_bp=0.0, liquidation_cost_bp=LIQ_BP, band=BAND, leverage="gross", end=end)
        d = res.daily
        forced = d["cost"]                                             # delisting exits are free at cost 0: added below
        tc, traded = tier_cost(res, w, daily, thin_bp)
        gone = (traded - d["traded"]).clip(lower=0)                    # exits of delisted names are not in d["traded"] at cost 0
        res.notes["tier_check_max_abs_diff"] = float((traded - d["traded"]).abs().max())
        d["cost"] = -tc.reindex(d.index).fillna(0.0)
        d["total"] = d[["price", "funding", "cost", "liquidation"]].sum(axis=1)
        res.notes["cost_tier_bp"] = {"thin": thin_bp, "liquid": LIQUID_BP, "hedge": HEDGE_BP, "forced": LIQ_BP}
    vname = variant + (f"-delay{delay}" if delay else "")
    return res, vname


def depth_regression(y, x, depth, lags=BETA_LAGS, nw=14):
    """1.11 #1: y on the market today plus lags and on the depth-of-fall spread today; intercept with OLS and NW t."""
    X = pd.concat([x.shift(k) for k in range(lags + 1)] + [depth], axis=1)
    X.columns = range(lags + 2)
    df = pd.concat([y.rename("y"), X], axis=1).dropna()
    A = np.column_stack([np.ones(len(df)), df[list(range(lags + 2))].to_numpy()])
    yy = df["y"].to_numpy()
    XtXi = np.linalg.inv(A.T @ A)
    b = XtXi @ A.T @ yy
    e = yy - A @ b
    n, k = A.shape
    t_ols = b[0] / np.sqrt(e @ e / (n - k) * XtXi[0, 0])
    S = (A * e[:, None]).T @ (A * e[:, None])
    for L in range(1, nw + 1):
        G = (A[L:] * e[L:, None]).T @ (A[:-L] * e[:-L, None])
        S += (1 - L / (nw + 1)) * (G + G.T)
    V = XtXi @ S @ XtXi
    return {"alpha_daily": b[0], "t_ols": t_ols, "t_nw": b[0] / np.sqrt(V[0, 0]), "beta_market_sum": b[1:1 + lags + 1].sum(),
            "beta_depth": b[-1], "n": n}


def gate(daily, funding, start, end, period, cost_bp):
    res, _ = run("base", period, start, end, daily, funding, cost_bp)
    folder, s = save_run(NAME, period, "base-tiered", res, params={"cost_tier_bp": res.notes["cost_tier_bp"], "delay": 0}, code_file=__file__)
    resw, _ = run("winners", period, start, end, daily, funding, cost_bp)
    fw, sw = save_run(NAME, period, "winners-diagnostic-tiered", resw, params={"cost_tier_bp": resw.notes["cost_tier_bp"], "delay": 0}, code_file=__file__)
    resd, _ = run("depth", period, start, end, daily, funding, cost_bp)
    fd, sd = save_run(NAME, period, "depth-diagnostic-tiered", resd, params={"cost_tier_bp": resd.notes["cost_tier_bp"], "delay": 0}, code_file=__file__)
    print("base run:", folder); print("winners diagnostic run:", fw); print("depth diagnostic run:", fd)
    print("reconstructed traded vs engine traded, max abs diff:", res.notes["tier_check_max_abs_diff"])
    for k, v in s.items():
        print(f"{k}: {v}")
    f, ret1, uni, cells = _formations(daily, "base")
    ew = ret1.where(uni.shift(1, fill_value=False)).mean(axis=1)
    first = res.trades.index.min()
    g = lambda r: (r.daily["price"] + r.daily["funding"]).loc[first:]
    gl, gw, gd = g(res), g(resw), g(resd)
    ew = ew.reindex(gl.index)
    out = {"losers": regression(gl, ew), "winners": regression(gw.reindex(gl.index), ew), "L_minus_W": regression(gl - gw.reindex(gl.index), ew),
           "#1 losers, market + depth spread": depth_regression(gl, ew, gd.reindex(gl.index)),
           "depth spread alone (market only)": regression(gd.reindex(gl.index), ew)}
    for k, v in out.items():
        print(k, {a: round(float(b), 5) for a, b in v.items()})
    d = res.daily.loc[first:]
    gross_pnl = d["price"].sum() + d["funding"].sum()
    print("price share of gross (all names):", round(float(d["price"].sum() / gross_pnl), 3))
    print("cost: tiered %.2f%%/yr-total %.2f%%" % (float(d["cost"].sum() * 100), float(d["cost"].sum() * 100)),
          "| depth spread gross Sharpe", sd["gross_sharpe"], "turnover", sd["turnover_per_year"])
    cc = cells.loc[start:end]
    print("min loser group size on train formations:", int(cc["group"].min()), "| formations skipped under 4:", int((cc["group"] < 4).sum()))
    print("avg gross:", round(float(res.trades["gross"].mean()), 3))
    return s


STRESS = {                                     # 1.5b "Tested as"
    "sort_ind": {"sort": "ind"}, "beta30": {"beta_window": 30}, "beta120": {"beta_window": 120}, "lags10": {"beta_lags": 10},
    "hedge_ew20": {"hedge": "ew20"}, "thin40": {"thin_bp": 40.0}, "minleg5": {"min_leg": 5},
}
# the d+1 fill stress of 1.5b is the --delay 1 control (same weights, traded a day later)


def diagnostics(daily, funding, run_folder, start, end):
    """Read-only items of the Data check and 1.10: liquidity-cell changes inside a holding, held name-days with no funding
    print by year and leg, largest single-name P&L day per leg, largest name weight per leg."""
    import json
    rf = Path(run_folder)
    pos = pd.read_parquet(rf / "positions.parquet")
    pos = pos.loc[start:end]
    f, ret1, uni, cells = _formations(daily, "base")
    f = f.loc[start:end]
    # cell changes: for every name formed on d (thin +, liquid -), its cell on d+1..d+13 under the same sequential sort
    sg = np.sign(f.to_numpy()); n = len(f)
    same = chg = opp = tot = 0
    ever_leave = ever_opp = names = 0
    for i in range(n - 13):
        for j in np.where(sg[i] != 0)[0]:
            fut = sg[i + 1:i + 14, j]
            names += 1
            ever_leave += int((fut != sg[i, j]).any())
            ever_opp += int((fut == -sg[i, j]).any())
            tot += 13; same += int((fut == sg[i, j]).sum()); opp += int((fut == -sg[i, j]).sum())
    print(f"cell changes {start} to {end}: {names} name-formations; share of the 13 following days in the same cell {same/tot:.3f}, "
          f"in the opposite cell {opp/tot:.3f}; share of names that leave their cell at least once {ever_leave/names:.3f}, "
          f"that sit in the opposite cell at least once {ever_opp/names:.3f}")
    # funding prints
    d = daily.pivot(index="date", columns="symbol", values="funding_prints").reindex(index=pos.index, columns=pos.columns)
    noprint = (d.isna() | (d == 0))
    rows = []
    for leg, m in (("long", pos > 0), ("short", pos < 0)):
        x = (m & noprint)
        rows.append(x.groupby(x.index.year).sum().sum(axis=1).rename(leg))
    held = pd.concat([((pos > 0).groupby(pos.index.year).sum().sum(axis=1)).rename("long held name-days"),
                      ((pos < 0).groupby(pos.index.year).sum().sum(axis=1)).rename("short held name-days")] + rows, axis=1)
    print("held name-days without a funding print, by year and leg:\n" + held.to_string())
    byname = ((pos != 0) & noprint).sum().sort_values(ascending=False).head(5)
    print("top names without a print:", byname[byname > 0].to_dict())
    # largest single-name P&L day, largest weight
    cl = daily.pivot(index="date", columns="symbol", values="mark_close").sort_index().reindex(columns=pos.columns)
    r = (cl / cl.shift(1) - 1).reindex(pos.index).fillna(0.0)
    pnl = pos * r
    for leg, m in (("long", pos > 0), ("short", pos < 0)):
        x = pnl.where(m, 0.0)
        s = x.stack(); lo_, hi_ = s.idxmin(), s.idxmax()
        wmax = pos.where(m).abs().max(axis=1)
        print(f"{leg}: worst name-day {lo_} {s.min():.4f}, best {hi_} {s.max():.4f}; largest weight {wmax.max():.4f} on {wmax.idxmax().date()}, median daily max weight {wmax.median():.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", choices=["train", "validation", "train+validation"], required=True)
    ap.add_argument("--variant", choices=VARIANTS, default="base")
    ap.add_argument("--cost-bp", type=float, default=COST_BP)
    ap.add_argument("--check-lookahead", action="store_true", help="truncation test only, no run")
    ap.add_argument("--gate", action="store_true", help="train gate 1.11 #1 to #4")
    ap.add_argument("--stress", choices=list(STRESS), default=None, help="1.5b stress test")
    ap.add_argument("--diag", default=None, help="run folder: read-only diagnostics")
    ap.add_argument("--delay", type=int, default=0, help="trade the same weights this many days later (control)")
    a = ap.parse_args()

    start, end = {"train": TRAIN, "validation": VALIDATION, "train+validation": (TRAIN[0], VALIDATION[1])}[a.period]
    daily = load("crypto_daily", test_start=TEST_START)
    funding = load("crypto_funding", test_start=TEST_START)
    px = daily.loc[daily["symbol"].isin(STABLECOINS), "mark_close"]
    assert px.between(0.97, 1.03).all(), "Data check #1: a listed stablecoin is not a peg"
    if a.check_lookahead:
        cal = pd.date_range(daily["date"].min(), daily["date"].max(), freq="D")
        days = [d for d in rebalance_days(cal) if pd.Timestamp(start) <= d <= pd.Timestamp(end)]
        kw = {k: v for k, v in STRESS.get(a.stress, {}).items() if k != "thin_bp"}
        truncation_test(build_weights, daily, funding, days, variant=a.variant, **kw)
        return
    if a.diag:
        diagnostics(daily, funding, a.diag, start, end)
        return
    if a.gate:
        gate(daily, funding, start, end, a.period, a.cost_bp)
        return
    kw = STRESS.get(a.stress, {})
    res, vname = run(a.variant, a.period, start, end, daily, funding, a.cost_bp, a.delay, **kw)  # tiered cost (1.5b)
    vname += f"-{a.stress}" if a.stress else ""
    folder, s = save_run(NAME, a.period, vname, res, params={"cost_tier_bp": res.notes.get("cost_tier_bp"), "delay": a.delay, "stress": a.stress}, code_file=__file__)
    print(folder)
    for k, v in s.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
