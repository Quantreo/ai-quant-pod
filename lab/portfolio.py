"""
The book, built from its strategies' saved daily returns: does a candidate deserve a place in it?

    poetry run python lab/portfolio.py \
        --strategy "Crypto Thin Losers" results/crypto_thin_losers/<train run> <validation run> <test run> \
        --strategy "Crypto XS Momentum" results/crypto_xs_momentum/<train run> <validation run> \
        --candidate "Crypto XS Momentum" --name "Book 2026-11" --haircut 0.35 [--since 2024-01-01] \
        [--family Carry carry --family Momentum momentum]

Each --strategy takes its runs of the frozen variant (run folders, or a returns file made outside the desk:
CSV or parquet with columns date, net and if possible gross, daily, in fraction of capital; give its family with
--family, since it has no strategy card on the desk), stitched in time (a later run wins on overlapping days). Only
the days every strategy covers are used: a strategy whose test is still sealed has no test run, so the common
window stops where its validation stops. Nothing here loads market data, so nothing here can open a test.

Returns: the net P&L (total) is what the book earns; independence is measured on the gross P&L (price plus
funding), before costs, as everywhere on the desk.

Sizing (vault/4 Book/Examples/Strategy Table.md): every strategy scaled to 15% annual volatility with its trailing
60-day realised volatility, known the day before (ex ante); equal risk weights between families, a family's
strategies sharing its budget; the book scaled to its 10% target by the IDM, capped at 2.5.

The rule (vault/Toolbox/My Research Routine.md): Sharpe(candidate) > correlation(candidate, book) x Sharpe(book);
the correlation in the book's worst 25% months; the book's Sharpe without and with the candidate; a stationary block
bootstrap (blocks of 20 days, 2000 histories): the share of histories where the book with the candidate has the
higher Sharpe. 90% or more: enter at half weight; 60 to 90%: paper, re-test next quarter; below 60%: no.
With no other strategy in the book, the candidate is compared with an empty book: the bootstrap reads the share of
histories where its own Sharpe is above zero.

Writes <out>/<name> - book.png (cumulative return in %, linear scale) and prints the tables in Markdown, for the PM.
"""
import argparse, json, re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                       # noqa: E402
import numpy as np                                                    # noqa: E402
import pandas as pd                                                   # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PPY = 365
STRAT_VOL, BOOK_VOL, IDM_CAP, VOL_WINDOW = 0.15, 0.10, 2.5, 60
BLOCK, DRAWS = 20, 2000


def read_runs(folders):
    """Net and gross daily returns of one strategy, stitched from its runs."""
    net, gross, info = [], [], []
    for f in folders:
        f = ROOT / f if not Path(f).is_absolute() else Path(f)
        if f.is_file():                                                # returns made outside the desk: date, net[, gross]
            d = pd.read_parquet(f) if f.suffix == ".parquet" else pd.read_csv(f)
            d = d.set_index(pd.to_datetime(d.pop("date"))).sort_index()
            n = d["net"] if "net" in d else d["total"]
            net.append(n); gross.append(d["gross"] if "gross" in d else n)
            info.append(f"imported {f.name} ({d.index[0].date()} to {d.index[-1].date()}"
                        + ("" if "gross" in d else ", no gross: correlations on net") + ")")
            continue
        s = json.loads((f / "summary.json").read_text())
        d = pd.read_parquet(f / "daily.parquet")
        if len(d) > 1 and (d.index[1] - d.index[0]) < pd.Timedelta(days=1):
            d = d.resample("D").sum()
        d = d.loc[s["start"]:s["end"]]
        net.append(d["total"]); gross.append(d["price"] + d["funding"])
        info.append(f"{s['period']} {s['variant']} ({s['start']} to {s['end']}, lab {s.get('lab_sha', '?')})")
    stitch = lambda xs: pd.concat(xs).groupby(level=0).last().sort_index()
    return stitch(net), stitch(gross), info


def family_of(name, given=None):
    if given and name in given:
        return given[name]
    for p in (ROOT / "vault" / "2 Strategies").glob(f"*/{name}/{name}.md"):
        m = re.search(r"^family:\s*(.+)$", p.read_text(), re.M)
        if m:
            return m.group(1).strip()
    return name


def scale(r):
    """Each strategy at 15% volatility, with the trailing realised volatility known the day before."""
    vol = r.rolling(VOL_WINDOW, min_periods=20).std().shift(1) * np.sqrt(PPY)
    return (r * STRAT_VOL / vol).dropna()


def weights(names, families):
    fam = pd.Series(families, index=names)
    return pd.Series({n: 1 / fam.nunique() / (fam == fam[n]).sum() for n in names})


def book(R, w):
    """Equal risk weights, then the IDM toward the 10% target, capped."""
    raw = R[w.index] @ w
    C = R[w.index].corr().to_numpy()
    idm = min(IDM_CAP, 1 / np.sqrt(w.to_numpy() @ C @ w.to_numpy())) if len(w) > 1 else 1.0
    return raw * idm * BOOK_VOL / STRAT_VOL, idm


def sharpe(r):
    r = np.asarray(r)
    return float(r.mean() / r.std() * np.sqrt(PPY)) if r.std() > 0 else float("nan")


def max_dd(r):
    eq = r.cumsum()
    return float((eq - eq.cummax()).min())


def block_bootstrap(T, rng):
    """Index arrays of DRAWS histories, stationary blocks of mean length BLOCK."""
    idx = np.empty((DRAWS, T), dtype=int)
    for k in range(DRAWS):
        out, pos = [], 0
        while pos < T:
            start, n = rng.integers(T), rng.geometric(1 / BLOCK)
            out.append((start + np.arange(n)) % T); pos += n
        idx[k] = np.concatenate(out)[:T]
    return idx


def boot_sharpes(x, idx):
    s = x[idx]
    return s.mean(axis=1) / s.std(axis=1) * np.sqrt(PPY)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strategy", nargs="+", action="append", required=True, metavar=("NAME", "RUN"))
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--name", default="Book")
    ap.add_argument("--out", default="vault/4 Book/Checklists")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--haircut", type=float, default=0.0,
                    help="Sharpe taken off the candidate before the rule: the luck line of its family and asset (Trials summary)")
    ap.add_argument("--family", nargs=2, action="append", default=[], metavar=("NAME", "FAMILY"),
                    help="family of a strategy with no card on the desk (imported returns); otherwise read from its card")
    ap.add_argument("--since", help="judge only from this date (e.g. the end of train): the rule on data the strategy was not fitted on")
    a = ap.parse_args()

    nets, grosses, infos = {}, {}, {}
    for name, *runs in a.strategy:
        nets[name], grosses[name], infos[name] = read_runs(runs)
    names = list(nets)
    if a.candidate not in names:
        raise SystemExit(f"--candidate {a.candidate!r} is not one of the --strategy names")
    fams = {n: family_of(n, dict(a.family)) for n in names}
    N = pd.DataFrame({n: scale(nets[n]) for n in names}).dropna()
    G = pd.DataFrame({n: scale(grosses[n]) for n in names}).reindex(N.index).dropna()
    N = N.loc[G.index]
    if a.since:
        N, G = N.loc[a.since:], G.loc[a.since:]
    if a.haircut:                                                      # the candidate's mean lowered by the luck line, in Sharpe units
        for X in (N, G):
            X[a.candidate] = X[a.candidate] - a.haircut * X[a.candidate].std() / np.sqrt(PPY)
    if len(N) < 250:
        raise SystemExit(f"only {len(N)} common days: not enough to judge a book")

    rest = [n for n in names if n != a.candidate]
    cand = N[a.candidate]
    w_all = weights(names, [fams[n] for n in names])
    with_c, idm_with = book(N, w_all)
    L = [f"## {a.name}: {a.candidate} against the book", "",
         f"Common window: {N.index[0].date()} to {N.index[-1].date()} ({len(N)} days). Each strategy at {STRAT_VOL:.0%} volatility "
         f"(trailing {VOL_WINDOW}-day, ex ante), equal risk weights by family, book at {BOOK_VOL:.0%} via the IDM (cap {IDM_CAP}). "
         f"Haircut on the candidate: {a.haircut:.2f} of Sharpe" + (f"; judged from {a.since} only." if a.since else "."), "",
         "| Strategy | Family | Runs | Net Sharpe | Gross Sharpe | Max DD (at 15% vol) | Risk weight with the candidate |",
         "| --- | --- | --- | --- | --- | --- | --- |"]
    for n in names:
        L.append(f"| {n} | {fams[n]} | {'; '.join(infos[n])} | {sharpe(N[n]):.2f} | {sharpe(G[n]):.2f} | {max_dd(N[n]) * 100:.1f}% | {w_all[n]:.2f} |")
    L += ["", "Correlations, gross (before costs), daily:", "", G.corr().round(2).to_markdown(), ""]

    rng = np.random.default_rng(a.seed)
    idx = block_bootstrap(len(N), rng)
    if rest:
        w_rest = weights(rest, [fams[n] for n in rest])
        without, idm_without = book(N[rest], w_rest)
        sb = sharpe(without)
        corr = float(pd.Series(G[a.candidate]).corr(G[rest] @ w_rest))
        m = pd.DataFrame({"book": without, "cand": cand}).resample("ME").sum()
        worst = m[m["book"] <= m["book"].quantile(0.25)]
        bad_days = without <= without.quantile(0.10)
        share = float((boot_sharpes(with_c.to_numpy(), idx) > boot_sharpes(without.to_numpy(), idx)).mean())
        L += ["| The rule | Value |", "| --- | --- |",
              f"| Sharpe of the candidate (net) | {sharpe(cand):.2f} |",
              f"| Sharpe of the book without it (net) | {sb:.2f} (IDM {idm_without:.2f}) |",
              f"| Correlation to the book, gross, all days | {corr:.2f} |",
              f"| Correlation to the book, gross, the book's worst 10% days | {float(G.loc[bad_days, a.candidate].corr((G[rest] @ w_rest)[bad_days])):.2f} |",
              f"| Correlation in the book's worst 25% months (net) | {worst['book'].corr(worst['cand']):.2f} (candidate {worst['cand'].mean() * 100:+.2f}%/month there) |",
              f"| Threshold = corr x Sharpe(book) | {corr * sb:.2f} |",
              f"| **Passes the rule?** | {'yes' if sharpe(cand) > corr * sb else 'no'} |",
              f"| Book Sharpe without → with, equal risk weights | {sb:.2f} → {sharpe(with_c):.2f} (IDM {idm_with:.2f}) |",
              f"| **Block bootstrap: share of histories where the book improves** | **{share:.0%}** |"]
    else:
        share = float((boot_sharpes(cand.to_numpy(), idx) > 0).mean())
        L += ["| The rule (empty book) | Value |", "| --- | --- |",
              f"| Sharpe of the candidate (net) | {sharpe(cand):.2f} |",
              f"| **Block bootstrap: share of histories with a Sharpe above zero** | **{share:.0%}** |"]
    verdict = "enter at half weight" if share >= 0.9 else "paper, re-test next quarter" if share >= 0.6 else "no"
    dd = max_dd(cand)
    L += ["", f"Routine reading: **{verdict}** ({share:.0%}; 90% or more enters, 60 to 90% paper, below 60% no).",
          f"Exit levels if it enters (at 15% vol): halve at {1.5 * dd * 100:.1f}% drawdown (1.5 x the worst, {dd * 100:.1f}%), cut at {2 * dd * 100:.1f}%."]

    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(11, 5))
    for n in names:
        (N[n].cumsum() * 100).plot(ax=ax, lw=1, alpha=0.8, label=f"{n} (15% vol)")
    if rest:
        (without.cumsum() * 100).plot(ax=ax, lw=2, color="grey", label="book without the candidate (10% target)")
    (with_c.cumsum() * 100).plot(ax=ax, lw=2.2, color="black", label="book with the candidate (10% target)")
    ax.axhline(0, color="grey", lw=0.5); ax.set_ylabel("cumulative net return %"); ax.legend(fontsize=8)
    ax.set_title(f"{a.name}: cumulative net return, linear scale")
    plt.tight_layout()
    png = out / f"{a.name} - book.png"
    fig.savefig(png, dpi=110); plt.close(fig)
    L += ["", f"![[{png.name}]]"]
    print("\n".join(L))


if __name__ == "__main__":
    main()
