"""
A backtest report a human can read in Obsidian: one page next to the strategy sheet, with its charts.

    poetry run python lab/report.py "Crypto Funding Carry" <run folder> [<run folder> ...] [--suffix test]

Writes <Strategy> - Backtest report.md and its PNG charts in the strategy's folder (lab.sheets), next to the sheet:
cumulative return in % (linear scale, net and gross), drawdown, cumulative P&L by source (price, funding or
carry, costs, liquidations), P&L by year and by leg, and a side-by-side table of the runs. The first run is the
main one (usually the base on train plus validation); the others are compared with it.
"""
import json, sys
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                       # noqa: E402
import numpy as np                                                    # noqa: E402
import pandas as pd                                                   # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PPY = 365


def sharpe(r):
    return r.mean() / r.std() * np.sqrt(PPY) if r.std() > 0 else float("nan")


def read(folder):
    folder = Path(folder)
    s = json.loads((folder / "summary.json").read_text())
    d = pd.read_parquet(folder / "daily.parquet")
    if len(d) > 1 and (d.index[1] - d.index[0]) < pd.Timedelta(days=1):     # intraday bars: read as daily sums
        d = d.resample("D").sum()
    return s, d.loc[s["start"]:s["end"]]


def chart_main(d, title, path):
    fig, ax = plt.subplots(3, 1, figsize=(11, 10), height_ratios=[2, 1, 2], sharex=True)
    (d["total"].cumsum() * 100).plot(ax=ax[0], lw=2, label="net")
    ((d["price"] + d["funding"]).cumsum() * 100).plot(ax=ax[0], lw=1, alpha=0.7, label="gross")
    ax[0].set_ylabel("cumulative return %"); ax[0].legend(); ax[0].set_title(title); ax[0].axhline(0, color="grey", lw=0.5)
    eq = d["total"].cumsum()
    ((eq - eq.cummax()) * 100).plot(ax=ax[1], color="crimson"); ax[1].set_ylabel("drawdown %")
    for c in ["price", "funding", "cost", "liquidation"]:
        (d[c].cumsum() * 100).plot(ax=ax[2], label=c)
    ax[2].set_ylabel("cumulative P&L by source %"); ax[2].legend(); ax[2].axhline(0, color="grey", lw=0.5)
    plt.tight_layout(); fig.savefig(path, dpi=110); plt.close(fig)


def chart_compare(runs, path):
    fig, ax = plt.subplots(figsize=(11, 5))
    for s, d in runs:
        (d["total"].cumsum() * 100).plot(ax=ax, label=f"{s['period']} · {s['variant']}")
    ax.set_ylabel("cumulative net return %"); ax.legend(); ax.axhline(0, color="grey", lw=0.5)
    ax.set_title("Runs compared (net, cumulative %, linear scale)")
    plt.tight_layout(); fig.savefig(path, dpi=110); plt.close(fig)


def main():
    args = sys.argv[1:]
    suffix = ""
    if "--suffix" in args:                                             # a second page next to the first: "Test report"
        i = args.index("--suffix"); suffix = args[i + 1]; del args[i:i + 2]
    name, folders = args[0], args[1:]
    tag = f"{name} - {suffix}" if suffix else name
    runs = [read(f) for f in folders]
    sys.path.insert(0, str(ROOT))
    from lab.sheets import strategy_folder
    out = strategy_folder(name)
    s0, d0 = runs[0]
    chart_main(d0, f"{name} · {s0['period']} · {s0['variant']}", out / f"{tag} - main.png")
    if len(runs) > 1:
        chart_compare(runs, out / f"{tag} - compare.png")
    y = d0.groupby(d0.index.year)
    by_year = pd.DataFrame({"Gross Sharpe": y.apply(lambda x: sharpe(x["price"] + x["funding"])), "Net Sharpe": y.apply(lambda x: sharpe(x["total"])),
                            "Price %": y["price"].sum() * 100, "Funding %": y["funding"].sum() * 100,
                            "Costs %": y["cost"].sum() * 100, "Liquidations %": y["liquidation"].sum() * 100}).round(2)
    legs = (d0[["price_long", "price_short", "funding_long", "funding_short"]].sum() * 100).round(2)
    keys = ["period", "variant", "start", "end", "gross_sharpe", "net_sharpe", "net_t_stat", "net_vol_pct", "max_drawdown_pct",
            "turnover_per_year", "funding_share_of_gross", "liquidations", "run_id"]
    table = pd.DataFrame([{k: s.get(k) for k in keys} for s, _ in runs])
    md = [f"# {name} · Backtest report", "",
          f"Built {date.today()} from the saved runs, by `lab/report.py`. Sheet: [[{name}]]. Every number comes from `results/`; "
          "nothing here is a verdict, the verdict is in Pass 2 of the sheet.", "",
          f"## Main run: {s0['period']} · {s0['variant']}", "",
          f"Gross Sharpe {s0['gross_sharpe']}, net Sharpe {s0['net_sharpe']} (t {s0['net_t_stat']}), volatility {s0['net_vol_pct']}%, "
          f"max drawdown {s0['max_drawdown_pct']}%, turnover {s0['turnover_per_year']}×/yr, funding share of gross {s0['funding_share_of_gross']}, "
          f"liquidations {s0['liquidations']}.", "", f"![[{tag} - main.png]]", "",
          "## By year", "", by_year.to_markdown(), "",
          "## By leg (% of capital)", "", legs.to_frame("total").to_markdown(), ""]
    if len(runs) > 1:
        md += ["## Runs compared", "", f"![[{tag} - compare.png]]", "", table.to_markdown(index=False), ""]
    page = out / (f"{name} - {suffix} report.md" if suffix else f"{name} - Backtest report.md")
    page.write_text("\n".join(md))
    print(page)


if __name__ == "__main__":
    main()
