"""ETF TSMOM 12-Month validation phase: pooled train+validation (2006-02 to 2020-12), monthly, NW 4 lags (1.10, 1.11).
Runs the base, the controls, stresses and variant A of etf_tsmom_12m.py, then K1 to K5. Test never opened.
    poetry run python strategies/etf_tsmom_12m_validate.py
K4 regressors (fixed before the run, strictest reading): alpha must reach t 2 both on SPY and TLT excess returns together
(two regressors) and on their 50/50 monthly-rebalanced buy-and-hold excess (one regressor). Excess = adj_close monthly
return minus the T-bill rate of that month / 12."""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parent))
import etf_tsmom_12m as E

P = "train+validation"
LUCK_LINE = 0.30
RUNS = [("base", {}), ("control_long", {}), ("control_twin", {}), ("stress13", {}), ("stress9", {}), ("A", {}),
        ("base", {"borrow_rate": 0.01}), ("base", {"cost_mult": 2.0})]


def monthly_excess(sym, idx):
    b = E.etf_bars()
    px = b[b.symbol == sym].set_index("date")["close"]
    me = px.groupby(px.index.to_period("M")).last()
    r = me.pct_change()
    c = E.cash_table().assign(m=lambda x: x.month.dt.to_period("M")).set_index("m")["rate"] / 1200
    return (r - c.reindex(r.index)).reindex(idx)


def main():
    out, F = {}, {}
    for v, kw in RUNS:
        folder, s, p = E.run(P, v, **kw)
        key = v + ("-b1pct" if kw.get("borrow_rate") else "-cost2x" if kw.get("cost_mult") else "")
        F[key] = folder
        out[key] = pd.read_parquet(folder / "monthly.parquet")["net"]
        print(key, folder.name, {k: s[k] for k in ["gross_sharpe", "net_sharpe", "net_t_stat", "turnover_per_year"]}, p["scored_months"], p["first_scored_month"])
    res = {}
    b = out["base"]; n = len(b); years = n / 12; lags = int(np.floor(4 * (n / 100) ** (2 / 9)))
    def sharpe(y): return float(y.mean() / y.std(ddof=1) * np.sqrt(12))
    def reg(y, X): return E.nw_ols(y.to_numpy(), X.to_numpy(), lags)
    res["n_months"], res["years"], res["lags"] = n, round(years, 3), lags
    res["K1"] = reg(b, out["control_long"].to_frame()); res["K2"] = reg(b, out["control_twin"].to_frame())
    sh = sharpe(b); res["K3"] = {"net_sharpe": sh, "t": sh * np.sqrt(years), "bar": 2 / np.sqrt(years), "luck_line": LUCK_LINE}
    spy, tlt = monthly_excess("SPY", b.index), monthly_excess("TLT", b.index)
    X2 = pd.concat([spy, tlt], axis=1); ok = X2.notna().all(axis=1)
    res["K4_two"] = reg(b[ok], X2[ok]); bh = (0.5 * spy + 0.5 * tlt)[ok]
    res["K4_5050"] = reg(b[ok], bh.to_frame())
    d89 = ~((b.index >= pd.Period("2008-01")) & (b.index <= pd.Period("2009-12"))) & ok
    res["K4_two_ex0809"] = reg(b[d89], X2[d89])
    bn = pd.read_csv(F["base"] / "by_name.csv", index_col=0)["price"].sort_values(ascending=False)
    res["K5"] = {"top2": list(bn.index[:2]), "share": float(bn.iloc[:2].sum() / bn.sum()), "total_price_pct": float(bn.sum() * 100)}
    res["by_etf_price_pct"] = {k: round(float(v * 100), 2) for k, v in bn.items()}
    res["sharpe_monthly_net"] = {k: round(sharpe(v), 3) for k, v in out.items()}
    res["train_part_base_sharpe"] = round(sharpe(b[b.index <= pd.Period("2017-12")]), 3)
    res["validation_part_base_sharpe"] = round(sharpe(b[b.index > pd.Period("2017-12")]), 3)
    res["A_vs_base"] = {"K1_A": reg(out["A"], out["control_long"].to_frame()), "K4_two_A": reg(out["A"][ok], X2[ok])}
    res["folders"] = {k: v.name for k, v in F.items()}
    (F["base"] / "validation.json").write_text(json.dumps(res, indent=2, default=float))
    print(json.dumps(res, default=float))


if __name__ == "__main__":
    main()
