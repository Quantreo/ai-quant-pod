"""
The desk's trial count: every try of every strategy, in one file, so that the best result is always judged
against everything that was tried to find it.

    poetry run python lab/trials.py add results/<strategy>/<run id> --sheet "vault/2 Strategies/Pipeline/<Strategy>/<Strategy>.md" \
        --counts yes --why "base, train gate"
    poetry run python lab/trials.py report

`add` appends one row to vault/3 Research Log/_desk/Trials.csv: date, strategy, family, asset, horizon, universe,
period, variant, gross and net Sharpe, years, whether it counts as a try, why, run id. A try is the base and each
variant Pass 1 counted, plus any change decided on a result; stress tests and controls are added with
--counts no, so the file is the full history.

`report` prints, and writes to vault/3 Research Log/_desk/Trials summary.md: tries by strategy, by family and by asset;
then, for the desk and for each family, the number of tries N, the effective number N_eff = N / (1 + (N - 1) rho)
with rho the mean correlation of the tries' daily returns, the luck line for the best of N_eff tries with no
skill, and the best gross Sharpe against it. Correlations and Sharpes are taken before costs (price plus funding):
the edge, and whether two tries are the same bet, is in the gross P&L; costs depend on the asset and the turnover
and would make two identical bets look different.

Gate bar: a new strategy's luck line uses N_eff of its family and asset (the row "family and asset") plus
its own tries, so every earlier try on the same data raises its bar by what it was really worth.

Budget: at most TRY_BUDGET tries per family and asset (one data set). Past it, the luck line of that group keeps
rising and a pass means less: the desk stops trying in that group and looks for new data instead.
"""
import argparse, csv, json, math, re
from datetime import date
from pathlib import Path
from statistics import NormalDist

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "vault" / "3 Research Log" / "_desk" / "Trials.csv"
SUMMARY = ROOT / "vault" / "3 Research Log" / "_desk" / "Trials summary.md"
COLS = ["date", "strategy", "family", "asset", "horizon", "universe", "period", "variant", "gross_sharpe", "net_sharpe",
        "years", "counts", "why", "run"]
EULER = 0.5772156649
TRY_BUDGET = 10                                                        # tries per family and asset


def luck_line(n, years):
    if n <= 1:
        return 0.0
    z = NormalDist().inv_cdf
    return math.sqrt(1 / years) * ((1 - EULER) * z(1 - 1 / n) + EULER * z(1 - 1 / (n * math.e)))


def frontmatter(sheet):
    text = Path(sheet).read_text()
    p1 = Path(sheet).parent / "Pass 1.md"                              # strategy split into files: the index plus its sections
    if p1.exists():
        text += "\n" + p1.read_text()
    m = re.search(r"^---\n(.*?)\n---", text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    uni = re.search(r"^## 1\.4 Universe\s*\n+(.*?)\n", text, re.M)
    out["universe"] = (uni.group(1).lstrip("- ").strip()[:80] if uni else "")
    return out


def add(a):
    run = ROOT / a.run if not Path(a.run).is_absolute() else Path(a.run)
    s = json.loads((run / "summary.json").read_text())
    fm = frontmatter(ROOT / a.sheet)
    row = {"date": str(date.today()), "strategy": s["strategy"], "family": fm.get("family", ""), "asset": fm.get("asset", ""),
           "horizon": fm.get("horizon", ""), "universe": fm.get("universe", ""), "period": s["period"], "variant": s["variant"],
           "gross_sharpe": s["gross_sharpe"], "net_sharpe": s["net_sharpe"], "years": s["years"], "counts": a.counts,
           "why": a.why, "run": str(run.relative_to(ROOT))}
    new = not FILE.exists()
    FILE.parent.mkdir(parents=True, exist_ok=True)
    with FILE.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if new:
            w.writeheader()
        w.writerow(row)
    print(f"Added: {row['strategy']} · {row['period']} · {row['variant']} · counts {row['counts']}")


def returns(run):
    p = ROOT / run
    s = json.loads((p / "summary.json").read_text())
    d = pd.read_parquet(p / "daily.parquet").loc[s["start"]:s["end"]]
    return (d["price"] + d["funding"]).rename(run)


def group_line(t, label):
    n = len(t)
    if n == 0:
        return None
    R = pd.concat([returns(r) for r in t["run"]], axis=1)
    rho = 0.0
    if n > 1:
        c = R.corr(min_periods=60).to_numpy()
        rho = float(np.nanmean(c[np.triu_indices(n, 1)])) if np.isfinite(c[np.triu_indices(n, 1)]).any() else 0.0
    n_eff = n / (1 + (n - 1) * max(rho, 0.0))
    years = float(t["years"].astype(float).median())
    line = luck_line(n_eff, years)
    best = t.loc[t["gross_sharpe"].astype(float).idxmax()]
    return (f"| {label} | {n} | {rho:.2f} | {n_eff:.1f} | {years:.1f} | {line:.2f} | {float(best['gross_sharpe']):.2f} "
            f"({best['strategy']}, {best['variant']}, {best['period']}) | {float(best['gross_sharpe']) - line:+.2f} |")


def report(_):
    if not FILE.exists():
        print("No trials yet.")
        return
    t = pd.read_csv(FILE)
    tries = t[t["counts"] == "yes"]
    L = [f"# Trials summary · {date.today()}", "",
         f"All rows: {len(t)}; tries (counted): {len(tries)}; strategies: {t['strategy'].nunique()}.", "",
         "## Tries by strategy", "", tries.groupby(["strategy", "family", "asset"]).size().rename("tries").reset_index().to_markdown(index=False), "",
         "## Tries by family and by asset", "", tries.groupby("family").size().rename("tries").to_frame().to_markdown(), "",
         tries.groupby("asset").size().rename("tries").to_frame().to_markdown(), "",
         "## Luck", "", "Best gross Sharpe of the tries against the best of N_eff tries with no skill (Bailey and Lopez de Prado).", "",
         "| Group | N | mean rho | N_eff | years | luck line | best gross Sharpe | above luck |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    rows = ([group_line(tries, "desk")] + [group_line(g, f"family: {f}") for f, g in tries.groupby("family")]
            + [group_line(g, f"family and asset: {f} · {x}") for (f, x), g in tries.groupby(["family", "asset"])])
    L += [r for r in rows if r]
    b = tries.groupby(["family", "asset"]).size().rename("tries").reset_index()
    b["budget"] = TRY_BUDGET
    b["left"] = (TRY_BUDGET - b["tries"]).clip(lower=0)
    b["status"] = np.where(b["left"] == 0, "spent: new data needed", "open")
    L += ["", f"## Budget of tries (per family and asset, {TRY_BUDGET} each)", "", b.to_markdown(index=False)]
    text = "\n".join(L) + "\n"
    SUMMARY.write_text(text)
    print(text)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("add")
    p.add_argument("run")
    p.add_argument("--sheet", required=True)
    p.add_argument("--counts", choices=["yes", "no"], required=True)
    p.add_argument("--why", default="")
    sub.add_parser("report")
    a = ap.parse_args()
    {"add": add, "report": report}[a.cmd](a)


if __name__ == "__main__":
    main()
