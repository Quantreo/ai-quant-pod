"""
SPY Volatility Managed: built from Pass 1 v1.1 of vault/2 Strategies/Proposed/SPY Volatility Managed/Pass 1.md and its Data check.

SPY weight w = min(c / RV2, 1.5), RV2 = sum of squared daily adj_close returns of the calendar month m (no demeaning), rest in
T-bills. The weight is dated the first trading day of month m+1 and trades at that close (the return of that day is earned by the
old weight, and is not in RV2 of m). Each held month runs first close to first close; the last train month (2017-12) therefore ends
at the first close of 2018-01 (one validation-month price used as an end mark, no signal reads it).

Engine mapping: the lab has one cost_bp and no cash. SPY is split in two legs with the same prices: SPY (weight min(w,1)) and
SPY_LEV (weight (w-1)+). Funding prints are the T-bill rate / 1200 a month for SPY, plus the borrow spread / 12 for SPY_LEV
(borrow only above 1x). The engine total is then the managed excess return over cash, net of cost.

    poetry run python strategies/spy_volatility_managed.py --check-lookahead
    poetry run python strategies/spy_volatility_managed.py --gate               # base on the file + base with 2008-10-13 at +11.6%
    poetry run python strategies/spy_volatility_managed.py --gate --spread-bp 100   # stress (reported, not a try)
"""
import argparse, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lab.backtest import backtest            # noqa: E402
from lab.checks import delay_test, truncation_test   # noqa: E402
from lab.data import ROOT, load              # noqa: E402
from lab.runs import save_run                # noqa: E402

NAME = "SPY Volatility Managed"

# 1.10 periods (train = months held 2005-02 to 2017-12; validation 2018-2020; test sealed)
TRAIN = ("2005-02-01", "2017-12-31")
VALIDATION = ("2018-01-01", "2020-12-31")
TEST_START = "2021-01-01"                     # never read here: lab.data.load cuts before it
FIRST_SIGNAL_MONTH = "2005-01"                # Data check: signal 2005-01 -> held 2005-02
TRAIN_END_MARK_MONTH = "2018-01"              # end mark of the last train month: first close of 2018-01

# 1.5 / 1.5b base version
CAP = 1.5                                     # 1.5b cap (Reg T)
COST_BP = 2.0                                 # 1.7 SPY 2 bp
SPREAD_BP = 50.0                              # 1.5 borrow above 1x: T-bill + 50 bp (stress 100)
CASH_LAG = 2                                  # Data check #3: signal month m uses TB3MS of m-1; held month M = m+1 -> M-2
LOOKBACK_MONTHS = 12                          # twin: 12-month excess return, no skip (Time-series momentum signal note)
FIX_DAY, FIX_RET = "2008-10-13", 0.116        # 1.11 / Data check #1: tested with this day set to +11.6%

# 1.11 gate
GATE_FIRST, GATE_LAST = "2006-02", "2017-12"  # 143 months
BAR_T = 2.0
DROP_YEARS = (2008, 2009)
N_DROP = 3
NW_RULE = lambda n: int(np.floor(4 * (n / 100) ** (2 / 9)))     # not in Pass 1; sister sheets' rule (4 for 116, 143, 155)

VARIANTS = ["base"]
PERIODS = {"train": TRAIN, "validation": VALIDATION, "train+validation": (TRAIN[0], VALIDATION[1])}


# ---------------------------------------------------------------- data
def spy_bars(fix=False, open_test=False):
    d = load("etf_daily", test_start=TEST_START, open_test=open_test)
    d = d[d["symbol"] == "SPY"].sort_values("date").reset_index(drop=True)
    p = d["adj_close"].to_numpy().copy()
    if fix:   # returns-only patch in memory: level after the day is scaled, every other daily return unchanged
        i = int(np.where(d["date"] == pd.Timestamp(FIX_DAY))[0][0])
        p[i:] *= (1 + FIX_RET) * p[i - 1] / p[i]
    return pd.DataFrame({"date": d["date"], "symbol": "SPY", "close": p, "high": p, "low": p})


def cash_table(open_test=False):
    """Data check #3: TB3MS monthly mean, % a year, stamped day 1 of its month. 'time' = day 1 of the next month (known then)."""
    t = pd.read_parquet(ROOT / "data/rates/tbill.parquet")
    if not open_test:
        t = t[t["date"] < pd.Timestamp(TEST_START)]
    t = t.sort_values("date")
    return pd.DataFrame({"month": t["date"].to_numpy(), "rate": t["rate"].to_numpy(),
                         "time": (t["date"] + pd.DateOffset(months=1)).to_numpy()})


def cash_month(cash, held_month):
    """Monthly cash return of the held month M: TB3MS of M-2 (signal month m = M-1 uses m-1), rate/1200."""
    key = (pd.Period(held_month, "M") - CASH_LAG).to_timestamp()
    r = cash.loc[cash["month"] == key, "rate"]
    assert len(r) == 1, f"cash missing for {held_month}"
    return float(r.iloc[0]) / 1200


def cash_12m(cash, signal_month, k=LOOKBACK_MONTHS):
    """Twin: compounded cash over months m-k..m-1 (monthly means, rate/1200); m = signal month. k = 12 or 1 (Pass 1 v1.3 1.5b)."""
    m = pd.Period(signal_month, "M").to_timestamp()
    c = cash[(cash["month"] >= m - pd.DateOffset(months=k)) & (cash["month"] < m)]
    assert len(c) == k and (c["time"] <= m + pd.DateOffset(months=1)).all()
    return float(np.prod(1 + c["rate"].to_numpy() / 1200) - 1)


def trade_days(px_days, first_signal=FIRST_SIGNAL_MONTH, last_held="2017-12"):
    """First trading day of each month m+1, for signal months first_signal.. (held months 2005-02 .. last_held)."""
    s = pd.Series(pd.DatetimeIndex(sorted(set(px_days))))
    first = s.groupby(s.dt.to_period("M")).min()
    held = [k for k in first.index if pd.Period(first_signal, "M") < k <= pd.Period(last_held, "M")]
    return [first[k] for k in held], first


# ---------------------------------------------------------------- signal and weights
def rv_before(ret, d, months=1):
    """RV2 of the calendar month before d's month (variant 1: the last 3 calendar months): sum of squared daily returns."""
    m = pd.Timestamp(d).to_period("M") - 1
    per = ret.index.to_period("M")
    r = ret[(per <= m) & (per > m - months)].dropna()
    return float((r ** 2).sum())


def build_weights(daily, cash, days, variant="base", c=None, cap=CAP, rv_months=1):
    """Weights per trade day d (first trading day of m+1), using data up to the close of m only (the twin: month-end m).
    base: columns SPY = min(w,1), SPY_LEV = (w-1)+. twin: column SPY = +-1 (sign of 12-month excess), for the look-ahead test
    and the regression only. Uses only days < the month of d."""
    px = daily.set_index("date")["close"].sort_index()
    ret = px.pct_change()
    idx = pd.Series(px.index, index=px.index)
    me = idx.groupby(idx.dt.to_period("M")).max()
    rows = {}
    for d in days:
        d = pd.Timestamp(d)
        m = d.to_period("M") - 1
        if variant in ("twin", "twin1"):
            k = 12 if variant == "twin" else 1
            if (m - k) not in me.index or m not in me.index:
                continue
            exc = px[me[m]] / px[me[m - k]] - 1 - cash_12m(cash, m, k)
            rows[d] = {"SPY": float(np.sign(exc))}
            continue
        rv = rv_before(ret, d, rv_months)
        w = min(c / rv, cap)
        rows[d] = {"SPY": min(w, 1.0), "SPY_LEV": max(w - 1.0, 0.0)}
    return pd.DataFrame.from_dict(rows, orient="index").fillna(0.0)


def month_table(bars, cash, days, end_mark=None, rv_months=1):
    """Per held month: d1 (trade day), d2 (next trade day, or the end mark), rv of the month before, SPY excess first close to
    first close, cash. Formula series (independent of the engine)."""
    px = bars.set_index("date")["close"].sort_index()
    ret = px.pct_change()
    if end_mark is None:
        _, first = trade_days(px.index, last_held="2099-12")
        end_mark = first[pd.Period(TRAIN_END_MARK_MONTH, "M")]
    d2s = list(days[1:]) + [end_mark]
    rows = []
    for d1, d2 in zip(days, d2s):
        k = pd.Timestamp(d1).to_period("M")
        rows.append({"month": k, "d1": d1, "d2": d2, "rv": rv_before(ret, d1, rv_months), "cash": cash_month(cash, k),
                     "spy_ex": float(px[d2] / px[d1] - 1 - cash_month(cash, k))})
    return pd.DataFrame(rows).set_index("month")


def fit_c(tab, cap=CAP):
    """1.5 c: managed vol = SPY vol on the train months (gross of borrow and cost), bisection. Full-train by design (source fn 5)."""
    target = tab["spy_ex"].std()
    f = lambda c: (np.minimum(c / tab["rv"], cap) * tab["spy_ex"]).std() - target
    lo, hi = 1e-6, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return (lo + hi) / 2


# ---------------------------------------------------------------- run
def run(period, variant="base", cost_bp=COST_BP, delay=0, open_test=False, fix=False, spread_bp=SPREAD_BP):
    """One run of the frozen configuration. train: held months 2005-02 to 2017-12 (end mark first close of 2018-01);
    train+validation: held months 2005-02 to 2020-12, the last month ends at the last close of 2020 (the loader cuts at the test
    start, so the first close of 2021-01 does not exist). c is always fitted on the train months only. delay = trading days
    the trade is made later (same signals)."""
    if period == "test":
        if not open_test:
            raise SystemExit("The test period is opened only by lab/run_test.py, by the user.")
    elif open_test:
        raise SystemExit("open_test is for the test period only.")
    assert period in ("train", "train+validation", "test"), period
    pooled = period == "train+validation"
    test = period == "test"
    rvm = 3 if variant == "variant1" else 1
    bars_all = spy_bars(fix=fix, open_test=test)
    cash = cash_table(open_test=test)
    last_day = bars_all["date"].max()
    # test (added 2026-10-26, same logic): held months from TEST_START to the last month of the data, which ends at the
    # last close, as train+validation does; c is still fitted on the train months only
    last_held = str(last_day.to_period("M")) if test else ("2020-12" if pooled else "2017-12")
    days_all, first = trade_days(bars_all["date"], last_held=last_held)
    end_mark = last_day if (pooled or test) else first[pd.Period(TRAIN_END_MARK_MONTH, "M")]
    if not test:
        assert end_mark < pd.Timestamp(TEST_START)
    bars = bars_all[bars_all["date"] <= end_mark]
    c = fit_c(month_table(bars, cash, days_all, end_mark, rvm).loc[:"2017-12"])        # train months only, never delayed
    if test:
        days_all = [d for d in days_all if d >= pd.Timestamp(TEST_START)]
    cal = pd.DatetimeIndex(sorted(bars["date"]))
    days_run = [cal[cal.get_loc(d) + delay] for d in days_all]
    tab = month_table(bars, cash, days_run, end_mark, rvm)
    w = build_weights(bars, cash, days_run, "base", c=c, rv_months=rvm)
    both = pd.concat([bars, bars.assign(symbol="SPY_LEV")], ignore_index=True)
    prints = []
    for sym, extra in [("SPY", 0.0), ("SPY_LEV", spread_bp / 1e4 / 12)]:
        for k, r in tab.iterrows():          # paid at the close of the bar d2 by the position held in the month
            prints.append({"symbol": sym, "time": r["d2"] + pd.Timedelta(days=1), "rate": r["cash"] + extra})
    funding = pd.DataFrame(prints)
    result = backtest(w, both, funding, cost_bp=cost_bp, end=end_mark)
    name = variant + ("-fix1013" if fix else "") + (f"-spread{int(spread_bp)}" if spread_bp != SPREAD_BP else "") \
        + (f"-cost{cost_bp:g}" if cost_bp != COST_BP else "") + (f"-lag{delay}" if delay else "")
    params = {"cost_bp": cost_bp, "delay_trading_days": delay, "fix": fix, "spread_bp": spread_bp, "c": c, "cap": CAP,
              "rv_months": rvm, "end_mark": str(end_mark.date())}
    folder, s = save_run(NAME, period, name, result, params=params, code_file=__file__)
    mo = monthly(result, tab, w, days_run, end_mark, bars, cash, spread_bp)
    mo.to_parquet(folder / "monthly.parquet")
    result.daily.to_parquet(folder / "daily.parquet")
    return folder, s, mo, w, c


def monthly(result, tab, w, days, end_mark, bars, cash, spread_bp):
    d = result.daily
    gross_d = d["price"] + d["funding"]
    rows = {}
    for (k, r) in tab.iterrows():
        seg = gross_d[(gross_d.index > r["d1"]) & (gross_d.index <= r["d2"])]
        gross = float(seg.sum())       # engine P&L is in units of initial capital (fixed contracts in the month): sum, not compound
        cost = float(d.loc[r["d1"], "cost"])               # entry cost of this month's position (negative)
        wt = w.loc[r["d1"]]
        rows[k] = {"net": gross + cost, "gross": gross, "cost": cost, "w": float(wt.sum()), "spy_ex": r["spy_ex"],
                   "formula": float(wt.sum() * r["spy_ex"] - wt["SPY_LEV"] * spread_bp / 1e4 / 12),
                   "traded": float(d.loc[r["d1"], "traded"])}
    mo = pd.DataFrame(rows).T
    # twin: sign of 12-month excess, executed like the vol rule, excess = sign x SPY excess of the held month
    tw = build_weights(bars, cash, days, "twin")
    mo["twin_w"] = pd.Series({pd.Timestamp(i).to_period("M"): v for i, v in tw["SPY"].items()})
    mo["twin"] = mo["twin_w"] * mo["spy_ex"]
    tw1 = build_weights(bars, cash, days, "twin1")
    mo["twin1_w"] = pd.Series({pd.Timestamp(i).to_period("M"): v for i, v in tw1["SPY"].items()})
    mo["twin1"] = mo["twin1_w"] * mo["spy_ex"]
    mo.index = pd.PeriodIndex(mo.index, freq="M")
    return mo


# ---------------------------------------------------------------- gate 1.11
def nw_ols(y, X, lags):
    X = np.column_stack([np.ones(len(y)), X])
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    e = y - X @ b
    XtXi = np.linalg.inv(X.T @ X)
    u = X * e[:, None]
    S = u.T @ u
    for L in range(1, lags + 1):
        G = u[L:].T @ u[:-L]
        S += (1 - L / (lags + 1)) * (G + G.T)
    V = XtXi @ S @ XtXi
    return {"alpha_m": float(b[0]), "betas": [float(x) for x in b[1:]], "t_nw": float(b[0] / np.sqrt(V[0, 0])),
            "n": len(y), "lags": lags, "resid": e}


def gate(mo):
    j = mo.loc[GATE_FIRST:GATE_LAST].dropna(subset=["twin"])
    assert len(j) == 143, len(j)
    y, X = j["net"].to_numpy(), j[["spy_ex", "twin"]].to_numpy()
    g1 = nw_ols(y, X, NW_RULE(len(j)))
    res = pd.Series(g1["resid"], index=j.index)
    keep = res[~res.index.year.isin(DROP_YEARS)]
    order = sorted(zip(-keep.to_numpy(), keep.index))               # largest signed first, earlier month first on ties
    top = [m for _, m in order[:N_DROP]]
    j2 = j.drop(index=[m for m in j.index if m.year in DROP_YEARS]).drop(index=top)
    assert len(j2) == 116, len(j2)
    g2 = nw_ols(j2["net"].to_numpy(), j2[["spy_ex", "twin"]].to_numpy(), NW_RULE(len(j2)))
    full = mo.dropna(subset=["spy_ex"])
    spy_only = nw_ols(full["net"].to_numpy(), full[["spy_ex"]].to_numpy(), NW_RULE(len(full)))
    spy_143 = nw_ols(j["net"].to_numpy(), j[["spy_ex"]].to_numpy(), NW_RULE(len(j)))
    strip = lambda g: {k: v for k, v in g.items() if k != "resid"}
    return {"g1": strip(g1), "g2": strip(g2), "dropped": [(str(m), round(float(res[m]), 5)) for m in top],
            "spy_only_155": strip(spy_only), "spy_only_143": strip(spy_143), "pass1": g1["t_nw"] >= BAR_T, "pass2": g2["t_nw"] >= BAR_T}


def report(folder, s, mo, w, c, spread_bp):
    ann = lambda x: float(x.mean() / x.std() * np.sqrt(12))
    n = len(mo)
    out = {"folder": str(folder.name), "c": c, "months_scored": n, "first": str(mo.index[0]), "last": str(mo.index[-1]),
           "gross_sharpe_m": ann(mo["gross"]), "net_sharpe_m": ann(mo["net"]), "spy_sharpe_m": ann(mo["spy_ex"]),
           "turnover_per_year": float(mo["traded"].sum() / (n / 12)), "months_at_cap": int((mo["w"] >= CAP - 1e-12).sum()),
           "months_w_gt_1": int((mo["w"] > 1).sum()), "months_at_cap_143": int((mo.loc[GATE_FIRST:GATE_LAST, "w"] >= CAP - 1e-12).sum()),
           "w_2008_11": float(mo.loc["2008-11", "w"]), "engine_vs_formula_max_abs": float((mo["net"] - mo["cost"] - mo["formula"]).abs().max()),
           "borrow_drag_pct_yr": float((w["SPY_LEV"] * spread_bp / 1e4).mean() * 100)}
    out["gate"] = gate(mo)
    return out


# ---------------------------------------------------------------- validation (Pass 1 v1.3, 1.11)
POOLED_FIRST, POOLED_LAST = "2006-02", "2020-12"     # 179 months: the 12-month twin needs 12 months
LUCK_LINE_POOLED = 0.13                              # budget.py, 2 tries, 14.92 years


def vgate(mo, first=POOLED_FIRST, last=POOLED_LAST, cols=("spy_ex", "twin", "twin1")):
    """V1: net on SPY and both sign twins, NW t. V2: same without calendar 2008-09 and the 3 largest signed residuals of V1."""
    j = mo.loc[first:last].dropna(subset=["twin", "twin1"])
    assert len(j) == 179, len(j)
    g1 = nw_ols(j["net"].to_numpy(), j[list(cols)].to_numpy(), NW_RULE(len(j)))
    res = pd.Series(g1["resid"], index=j.index)
    keep = res[~res.index.year.isin(DROP_YEARS)]
    top = [m for _, m in sorted(zip(-keep.to_numpy(), keep.index))[:N_DROP]]
    j2 = j.drop(index=[m for m in j.index if m.year in DROP_YEARS]).drop(index=top)
    assert len(j2) == 152, len(j2)
    g2 = nw_ols(j2["net"].to_numpy(), j2[list(cols)].to_numpy(), NW_RULE(len(j2)))
    spy = nw_ols(j["net"].to_numpy(), j[["spy_ex"]].to_numpy(), NW_RULE(len(j)))
    strip = lambda g: {k: (round(v, 4) if isinstance(v, float) else v) for k, v in g.items() if k != "resid"}
    return {"V1": strip(g1), "V2": strip(g2), "dropped": [(str(m), round(float(res[m]), 4)) for m in top], "spy_only": strip(spy)}


def lvl(folder, mo, tab_d1):
    j = mo.loc[POOLED_FIRST:POOLED_LAST]
    sm = float(j["net"].mean() / j["net"].std() * np.sqrt(12))
    d = pd.read_parquet(Path(folder) / "daily.parquet")
    x = (d["price"] + d["funding"] + d["cost"]).loc[tab_d1:].iloc[1:]
    sd = float(x.mean() / x.std() * np.sqrt(365))
    return {"monthly": (round(sm, 3), round(sm * np.sqrt(len(j) / 12), 2)), "daily": (round(sd, 3), round(sd * np.sqrt(len(x) / 365), 2)),
            "gross_monthly": round(float(j["gross"].mean() / j["gross"].std() * np.sqrt(12)), 3),
            "spy_monthly": round(float(j["spy_ex"].mean() / j["spy_ex"].std() * np.sqrt(12)), 3)}


def p3(tab):
    """Moreira Muir Fig. 1: next-month mean excess return over variance by tercile of the lagged variance (ratio of means)."""
    q = pd.qcut(tab["rv"], 3, labels=["low", "mid", "high"])
    r = tab.groupby(q, observed=True).apply(lambda g: g["spy_ex"].mean() / g["rv"].mean())
    return {k: round(float(v), 2) for k, v in r.items()}


def validate():
    import subprocess
    runs, out = {}, {}
    plan = [("base", dict()), ("base-fix1013", dict(fix=True)), ("base-spread150", dict(spread_bp=150)),
            ("base-spread25", dict(spread_bp=25)), ("base-cost4", dict(cost_bp=4.0)), ("base-lag2", dict(delay=2)),
            ("base-lag1", dict(delay=1))]
    for key, kw in plan:
        folder, s, mo, w, c = run("train+validation", "base", **kw)
        runs[key] = folder
        first_d1 = pd.read_parquet(folder / "monthly.parquet")  # noqa: F841
        d1 = mo.index.get_loc(pd.Period(POOLED_FIRST, "M"))
        out[key] = {"run": folder.name, "c": round(c, 5), "n_scored": len(mo), "level": None}
        # first d1 of the 2006-02 month: first trading day on or after 2006-02-01 (+ lag)
        bars = spy_bars(fix=kw.get("fix", False))
        cal = pd.DatetimeIndex(sorted(bars["date"]))
        d1d = cal[cal.searchsorted(pd.Timestamp("2006-02-01")) + kw.get("delay", 0)]
        out[key]["level"] = lvl(folder, mo, d1d)
        out[key].update(vgate(mo))
        out[key]["months_at_cap"] = int((mo["w"] >= CAP - 1e-12).sum())
        out[key]["turnover_yr"] = round(float(mo["traded"].sum() / (len(mo) / 12)), 2)
        if key == "base":
            base_mo = mo
            tab = month_table(bars[bars["date"] <= bars["date"].max()], cash_table(), trade_days(bars["date"], last_held="2020-12")[0], bars["date"].max())
            out[key]["P3_pooled"] = p3(tab)
            out[key]["P3_train"] = p3(tab.loc[:"2017-12"])
            old = sorted((ROOT / "results/spy_volatility_managed").glob("*-train-base"))[-1]
            om = pd.read_parquet(old / "monthly.parquet")
            out[key]["train_match_maxdiff"] = float((om["net"] - mo.loc[:"2017-12", "net"]).abs().max())
            out[key]["2020"] = {str(k): {"w": round(float(r["w"]), 2), "net": round(float(r["net"]), 4), "spy_ex": round(float(r["spy_ex"]), 4)}
                                for k, r in mo.loc["2020-02":"2020-04"].iterrows()}
            out[key]["validation_only"] = {"n": int(len(mo.loc["2018-01":"2020-12"])),
                                           "net_sharpe": round(float(mo.loc["2018-01":"2020-12", "net"].mean() / mo.loc["2018-01":"2020-12", "net"].std() * np.sqrt(12)), 3),
                                           "spy_sharpe": round(float(mo.loc["2018-01":"2020-12", "spy_ex"].mean() / mo.loc["2018-01":"2020-12", "spy_ex"].std() * np.sqrt(12)), 3)}
            out[key]["no_2020_03_V1_t"] = vgate_without(mo, "2020-03")
        (folder / "vreport.json").write_text(json.dumps(out[key], indent=1, default=str))
    ok = out["base"]["P3_pooled"]["low"] > out["base"]["P3_pooled"]["high"]
    out["P3_passes"] = bool(ok)
    if ok:
        folder, s, mo, w, c = run("train+validation", "variant1")
        bars = spy_bars(); cal = pd.DatetimeIndex(sorted(bars["date"]))
        out["variant1"] = {"run": folder.name, "c": round(c, 5), "level": lvl(folder, mo, cal[cal.searchsorted(pd.Timestamp("2006-02-01"))]),
                           "months_at_cap": int((mo["w"] >= CAP - 1e-12).sum())}
        out["variant1"].update(vgate(mo))
        (folder / "vreport.json").write_text(json.dumps(out["variant1"], indent=1, default=str))
    print(json.dumps(out, indent=1, default=str))


def vgate_without(mo, month):
    j = mo.loc[POOLED_FIRST:POOLED_LAST].drop(index=pd.Period(month, "M"))
    g = nw_ols(j["net"].to_numpy(), j[["spy_ex", "twin", "twin1"]].to_numpy(), NW_RULE(len(j)))
    return {"n": len(j), "alpha_ann_pct": round(g["alpha_m"] * 1200, 2), "t": round(g["t_nw"], 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-lookahead", action="store_true")
    ap.add_argument("--gate", action="store_true")
    ap.add_argument("--fix", action="store_true", help="2008-10-13 set to +11.6% in memory")
    ap.add_argument("--spread-bp", type=float, default=SPREAD_BP)
    ap.add_argument("--delay", type=int, default=0)
    ap.add_argument("--validate", action="store_true", help="pooled train+validation runs of Pass 1 v1.3")
    a = ap.parse_args()
    if a.validate:
        validate()
        return
    if a.check_lookahead:
        bars_all = spy_bars()
        cash = cash_table()
        days, first = trade_days(bars_all["date"])
        bars = bars_all[bars_all["date"] <= first[pd.Period(TRAIN_END_MARK_MONTH, "M")]]
        c = fit_c(month_table(bars, cash, days))
        for v in ["base", "twin", "twin1"]:
            truncation_test(build_weights, bars, cash, days, n=20, variant=v, c=c)
        c3 = fit_c(month_table(bars, cash, days, rv_months=3))
        truncation_test(build_weights, bars, cash, days, n=20, variant="base", c=c3, rv_months=3)
        return
    folder, s, mo, w, c = run("train", "base", delay=a.delay, fix=a.fix, spread_bp=a.spread_bp)
    print(json.dumps(report(folder, s, mo, w, c, a.spread_bp), indent=1, default=str))


if __name__ == "__main__":
    main()
