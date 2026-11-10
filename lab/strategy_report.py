"""
The report of a strategy: the PDF a human reads before deciding, laid out like a research note (LaTeX, numbered
sections, tables with bootstrap ranges, numbered figures in the desk style).

Two steps, with the reporter (skill strategy-report) writing the text in between:

    poetry run python lab/strategy_report.py "ETF TSMOM 12-Month" compute
        finds the runs of the frozen version, computes every number and figure, and writes
        results/<strategy>/report/numbers.md (what the reporter reads) and numbers.json (what build reads).
    poetry run python lab/strategy_report.py "ETF TSMOM 12-Month" build
        reads results/<strategy>/report/text.md (written by the reporter), fills the template, compiles it with
        pdflatex (or tectonic), and writes "<Strategy> - Report.pdf" next to the strategy sheet.

What it reads, all of it already on disk: the strategy sheet (lab.sheets) for the status, family and asset; the
strategy file in strategies/ for TRAIN, VALIDATION and TEST_START; the runs in results/<strategy>/ (the frozen
version, given by TEST_DONE or "base"; the other runs as variants and stress tests); the benchmark (BTC for crypto,
SPY otherwise, none for FX); vault/3 Research Log/_desk/Trials summary.md for the luck line. The test period is read
only if results/<strategy>/TEST_DONE exists.

Every number in the PDF is computed here. The text adds the reading, never a new number.
"""
import argparse, json, math, re, shutil, subprocess, sys
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                       # noqa: E402
import numpy as np                                                    # noqa: E402
import pandas as pd                                                   # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lab.sheets import sheet_path                                     # noqa: E402

A = 365                      # the engine writes one row per calendar day
BLOCK, PATHS, SEED = 20, 2000, 7
PAL = ["#1D4A78", "#96282B", "#2C6E54", "#8A6D3B", "#4A7BA6", "#6B4E79", "#8C8C8C"]
BLUE, RED, GREEN, BRONZE, STEEL, PURPLE, GREY = PAL
PCOL = {"Train": BLUE, "Validation": BRONZE, "Test": GREEN}
SECTIONS = ["abstract", "hypothesis", "method", "performance", "exposure", "sources", "concentration",
            "implementation", "robustness", "luck", "risks", "decision"]


# ------------------------------------------------------------------ locating things
def results_dir(name):
    from lab.runs import slug
    for cand in [ROOT / "results" / slug(name), ROOT / "results" / name.lower().replace(" ", "_")]:
        if cand.exists():
            return cand
    for d in (ROOT / "results").iterdir():                 # names with dashes keep them (etf_tsmom_12-month)
        if d.is_dir() and d.name.replace("-", "_") == re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_"):
            return d
    raise SystemExit(f"no results folder for {name!r} in results/")


def frontmatter(path):
    fm = {}
    m = re.match(r"---\n(.*?)\n---", path.read_text(), re.S)
    for line in (m.group(1).splitlines() if m else []):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def periods_of(name):
    """TRAIN, VALIDATION, TEST_START from the strategy file whose NAME is this strategy."""
    for f in (ROOT / "strategies").glob("*.py"):
        t = f.read_text()
        if re.search(r'^NAME\s*=\s*["\']' + re.escape(name) + r'["\']', t, re.M):
            tr = re.search(r'^TRAIN\s*=\s*\(\s*"([\d-]+)"\s*,\s*"([\d-]+)"\s*\)', t, re.M)
            va = re.search(r'^VALIDATION\s*=\s*\(\s*"([\d-]+)"\s*,\s*"([\d-]+)"\s*\)', t, re.M)
            ts = re.search(r'^TEST_START\s*=\s*"([\d-]+)"', t, re.M)
            if tr and va and ts:
                return f, (tr.group(1), tr.group(2)), (va.group(1), va.group(2)), ts.group(1)
    raise SystemExit(f"no strategy file with NAME = {name!r} and TRAIN, VALIDATION, TEST_START in strategies/")


def list_runs(rdir):
    runs = []
    for d in sorted(rdir.iterdir()):
        if (d / "summary.json").exists() and (d / "daily.parquet").exists():
            s = json.loads((d / "summary.json").read_text())
            runs.append({"dir": d, "id": d.name, "period": s.get("period"), "variant": s.get("variant"), "s": s})
    return runs


def daily_of(run):
    d = pd.read_parquet(run["dir"] / "daily.parquet")
    d.index = pd.to_datetime(d.index)
    s = run["s"]
    return d.loc[s.get("start", d.index[0]):s.get("end", d.index[-1])]


# ------------------------------------------------------------------ statistics
def sharpe(x):
    x = np.asarray(x, float)
    return float(x.mean() / x.std() * math.sqrt(A)) if x.std() > 0 else float("nan")


def nw_t_mean(x, lags=10):
    x = np.asarray(x, float); n = len(x); e = x - x.mean(); v = e @ e / n
    for l in range(1, lags + 1):
        v += 2 * (1 - l / (lags + 1)) * (e[l:] @ e[:-l]) / n
    return float(x.mean() / math.sqrt(v / n))


def nw_ols(y, x, lags=10):
    X = np.column_stack([np.ones(len(x)), x]); b = np.linalg.lstsq(X, y, rcond=None)[0]; e = y - X @ b; n = len(y)
    S = (X * e[:, None]).T @ (X * e[:, None]) / n
    for l in range(1, lags + 1):
        G = (X[l:] * e[l:, None]).T @ (X[:-l] * e[:-l, None]) / n; S += (1 - l / (lags + 1)) * (G + G.T)
    Q = np.linalg.inv(X.T @ X / n); V = Q @ S @ Q / n
    return b, b / np.sqrt(np.diag(V))


def boot_index(T, rng):
    out = np.empty((PATHS, T), dtype=int)
    for k in range(PATHS):
        idx, n = [], 0
        while n < T:
            s, L = rng.integers(T), rng.geometric(1 / BLOCK); idx.append((s + np.arange(L)) % T); n += L
        out[k] = np.concatenate(idx)[:T]
    return out


def metrics(x, dates):
    s = pd.Series(x, index=dates); m = s.resample("ME").sum(); eq = s.cumsum()
    return {"ret": s.mean() * A, "vol": s.std() * math.sqrt(A), "sr": sharpe(s), "mdd": float((eq - eq.cummax()).min()),
            "worst": float(m.min()), "pos": float((m > 0).mean())}


def perf_block(x, rng):
    samp = metrics(x.to_numpy(), x.index); arr = x.to_numpy()
    B = [metrics(arr[p], x.index) for p in boot_index(len(arr), rng)]
    q = {k: [float(v) for v in np.percentile([b[k] for b in B], [5, 50, 95])] for k in samp}
    dist = {k: [float(b[k]) for b in B] for k in ("sr", "mdd")}
    return samp, q, dist


def norm_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def deflated(x, sr0_ann):
    """Probability that the true Sharpe exceeds sr0 (Bailey and Lopez de Prado), with skewness and kurtosis."""
    x = np.asarray(x, float); sr = x.mean() / x.std(); T = len(x); z = (x - x.mean()) / x.std()
    g3, g4 = float((z ** 3).mean()), float((z ** 4).mean())
    den = math.sqrt(max(1e-12, 1 - g3 * sr + (g4 - 1) / 4 * sr ** 2))
    return norm_cdf((sr - sr0_ann / math.sqrt(A)) * math.sqrt(T - 1) / den), g3, g4


# ------------------------------------------------------------------ inputs from the vault
def luck_rows(strategy, family, asset):
    p = ROOT / "vault" / "3 Research Log" / "_desk" / "Trials summary.md"
    out = {"tries": None, "family_asset": None, "desk": None}
    if not p.exists():
        return out
    for line in p.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0] == strategy:
            try: out["tries"] = int(cells[-1])
            except ValueError: pass
        if len(cells) == 8 and (cells[0] == f"family and asset: {family} · {asset}" or cells[0] == "desk"):
            row = {"N": cells[1], "rho": cells[2], "N_eff": cells[3], "years": cells[4], "luck": cells[5], "best": cells[6], "above": cells[7]}
            out["desk" if cells[0] == "desk" else "family_asset"] = row
    return out


def benchmark(asset, open_test, test_start):
    from lab.data import load
    asset = (asset or "").lower()
    try:
        if "crypto" in asset:
            d = load("crypto_daily", test_start=test_start, open_test=open_test)
            b = d[d["symbol"] == "BTCUSDT"].set_index("date").sort_index()["mark_close"]; name = "BTC"
        elif "fx" in asset:
            return None, None
        else:
            d = load("etf_daily", test_start=test_start, open_test=open_test)
            b = d[d["symbol"] == "SPY"].set_index("date").sort_index()["adj_close"]; name = "SPY"
    except Exception as e:                                   # no data on this machine: the report goes on without it
        print(f"benchmark skipped: {e}")
        return None, None
    b.index = pd.to_datetime(b.index)
    return b.pct_change().dropna(), name


# ------------------------------------------------------------------ figures
def style():
    plt.style.use(str(ROOT / "lab" / "desk.mplstyle"))


def mark_periods(ax, P, cuts):
    for c in cuts:
        ax.axvline(c, color="#555", lw=0.6, ls=":")
    for name, (a, b) in P.items():
        mid = pd.Timestamp(a) + (pd.Timestamp(b) - pd.Timestamp(a)) / 2
        ax.text(mid, 1.02, name, transform=ax.get_xaxis_transform(), ha="center", va="bottom", fontsize=9, color="#444")


def compute(name):
    sheet = sheet_path(name); fm = frontmatter(sheet)
    sfile, TR, VA, TS = periods_of(name)
    rdir = results_dir(name); out = rdir / "report"; out.mkdir(exist_ok=True)
    lock = rdir / "TEST_DONE"
    tested = lock.exists()
    frozen = json.loads(lock.read_text()).get("variant", "base") if tested else "base"
    runs = list_runs(rdir)
    base = [r for r in runs if r["variant"] == frozen]
    pick = lambda per: max([r for r in base if r["period"] == per], key=lambda r: r["id"], default=None)
    chain = [pick("train"), pick("validation"), pick("train+validation")]
    test_run = None
    if tested:
        test_id = json.loads(lock.read_text()).get("run")
        test_run = next((r for r in runs if r["id"] == test_id), pick("test"))
        chain.append(test_run)
    chain = [r for r in chain if r]
    if not chain:
        raise SystemExit(f"no run of variant {frozen!r} in {rdir}")
    D = pd.concat([daily_of(r) for r in chain]); D = D[~D.index.duplicated(keep="last")].sort_index()
    end = D.index.max()
    D = D.loc[TR[0]:end] if tested else D.loc[TR[0]:VA[1]]
    P = {"Train": (TR[0], TR[1]), "Validation": (VA[0], VA[1])}
    if tested:
        P["Test"] = (TS, str(end.date()))
    D = D.loc[D.index >= pd.Timestamp(D["total"].ne(0).idxmax())]                    # from the first trading day
    net = D["total"]; gross = D["price"] + D["funding"]
    rng = np.random.default_rng(SEED)
    N = {"name": name, "date": date.today().isoformat(), "status": fm.get("status", ""), "family": fm.get("family", ""),
         "asset": fm.get("asset", ""), "horizon": fm.get("horizon", ""), "version": fm.get("version", ""),
         "frozen_variant": frozen, "tested": tested, "periods": P, "start": str(net.index[0].date()), "end": str(end.date()),
         "runs": [r["id"] for r in chain], "strategy_file": sfile.name}
    full_lab = "Full sample" if tested else "Train and validation"
    N["full_label"] = full_lab
    s, q, dist_full = perf_block(net, rng); N["perf"] = {"full": {"sample": s, "q": q}}
    dists = {full_lab: dist_full}
    if tested:
        xt = net.loc[TS:]; s, q, dist_test = perf_block(xt, rng); N["perf"]["test"] = {"sample": s, "q": q}
        dists["Test"] = dist_test
    N["by_period"] = {}
    for k, (a, b) in P.items():
        x = net.loc[a:b]; arr = x.to_numpy(); bi = boot_index(len(arr), rng); y = arr[bi]
        srs = y.mean(1) / y.std(1) * math.sqrt(A)
        N["by_period"][k] = {"sr": sharpe(x), "sr_q": [float(v) for v in np.percentile(srs, [5, 50, 95])],
                             "ret": float(x.mean() * A), "gross_sr": sharpe(gross.loc[a:b]), "days": len(x)}
    N["t_full_nw"] = nw_t_mean(net.to_numpy())
    if tested:
        before = net.loc[:VA[1]].mean(); after = net.loc[TS:].mean(); ratio = after / before if before else float("nan")
        tt = nw_t_mean(net.loc[TS:].to_numpy())
        zone = "confirms" if after > 0.5 * before else ("contradicts" if after < -0.5 * before and tt < -1.5 else "ambiguous")
        N["zone"] = {"zone": zone, "ratio": float(ratio), "test_t": tt}
    N["yearly"] = {str(y): float(v) for y, v in (net.groupby(net.index.year).sum()).items()}
    eq = net.cumsum(); dd = eq - eq.cummax(); tr = dd.idxmin(); pk = eq.loc[:tr].idxmax()
    rec = eq.loc[tr:][eq.loc[tr:] >= eq.loc[pk]]
    under = (dd < 0).astype(int); runs_ = under.groupby((under != under.shift()).cumsum()).sum()
    N["drawdown"] = {"max": float(dd.min()), "peak": str(pk.date()), "trough": str(tr.date()),
                     "recovered": str(rec.index[0].date()) if len(rec) else "not recovered", "longest_days": int(runs_.max())}
    # benchmark
    b, bname = benchmark(N["asset"], tested, TS)
    N["benchmark"] = bname
    if b is not None:
        N["exposure"] = {}
        for lab, (a, z) in [("full", (N["start"], N["end"]))] + ([("test", (TS, N["end"]))] if tested else []):
            j = pd.concat([net, b], axis=1, keys=["n", "b"], sort=True).loc[a:z].dropna()
            j = j[j["b"] != 0]
            bb, t = nw_ols(j["n"].to_numpy(), j["b"].to_numpy())
            N["exposure"][lab] = {"beta": float(bb[1]), "beta_t": float(t[1]), "alpha": float(bb[0] * A), "alpha_t": float(t[0]),
                                  "corr": float(j["n"].corr(j["b"]))}
        bm = b.loc[N["start"]:N["end"]]
        k = int(math.ceil(len(bm) * 0.01))
        N["bench_cut"] = {"sr": sharpe(bm), "sr_ex1": sharpe(bm.drop(bm.nlargest(k).index))}
        mb = pd.concat([net.resample("ME").sum(), bm.resample("ME").apply(lambda x: (1 + x).prod() - 1)], axis=1, keys=["n", "b"]).dropna()
    # sources
    legs = ("price_long" in D and "price_short" in D and D["price_short"].abs().sum() > 1e-9 and D["price_long"].abs().sum() > 1e-9)
    crypto = "crypto" in N["asset"].lower()
    fund_label = "Funding" if crypto else "Financing at the T-bill rate"
    src = {}
    for k, (a, z) in P.items():
        x = D.loc[a:z]
        src[k] = {"price_long": float(x["price_long"].sum()) if legs else None, "price_short": float(x["price_short"].sum()) if legs else None,
                  "price": float(x["price"].sum()), "funding": float(x["funding"].sum()),
                  "costs": float((x["cost"] + x.get("liquidation", 0)).sum())}
    N["sources"] = {"legs": bool(legs), "funding_label": fund_label, "by_period": src}
    # concentration in time
    def cut(x, qq):
        kk = int(math.ceil(len(x) * qq)); top = x.nlargest(kk); rest = x.drop(top.index)
        return {"days": kk, "share": float(top.sum() / x.sum()) if x.sum() else float("nan"), "sr": sharpe(rest), "ret": float(rest.mean() * A)}
    N["conc_days"] = {"full": {"sr": sharpe(net), "top1": cut(net, .01), "top5": cut(net, .05)}}
    if tested:
        xt = net.loc[TS:]; N["conc_days"]["test"] = {"sr": sharpe(xt), "top1": cut(xt, .01), "top5": cut(xt, .05)}
    # regularity: each month, its 2 best days against the others, by year
    g = net.groupby(net.index.to_period("M"))
    mm = pd.DataFrame({"m": g.sum(), "b2": g.apply(lambda s_: s_.nlargest(2).sum())}); mm["rest"] = mm["m"] - mm["b2"]
    N["regularity"] = {"months_positive_without_best2": float((mm["rest"] > 0).mean()),
                       "by_year": {str(y): {"best2": float(v["b2"].sum()), "rest": float(v["rest"].sum())} for y, v in mm.groupby(mm.index.year)}}
    # concentration in names, by run
    N["conc_names"] = {}
    for r in chain:
        f = r["dir"] / "by_name.csv"
        if not f.exists():
            continue
        bn = pd.read_csv(f, index_col=0); tot = bn.sum(axis=1).sort_values(ascending=False)
        n = int((bn.abs().sum(axis=1) > 0).sum())
        if n < 5 or tot.sum() == 0:
            continue
        lab = {"train": "Train", "validation": "Validation", "train+validation": "Train and validation", "test": "Test"}.get(r["period"], r["period"])
        N["conc_names"][lab] = {"names": n, "top1": float(tot.iloc[:1].sum() / tot.sum()), "top5": float(tot.iloc[:5].sum() / tot.sum()),
                                "top10": float(tot.iloc[:10].sum() / tot.sum()), "ex5": float(tot.sum() - tot.iloc[:5].sum()), "best": str(tot.index[0])}
    # implementation, by period
    pos = []
    for r in chain:
        f = r["dir"] / "positions.parquet"
        if f.exists():
            p = pd.read_parquet(f).fillna(0); p.index = pd.to_datetime(p.index); pos.append(p)
    POS = pd.concat(pos).groupby(level=0).last().fillna(0) if pos else None
    N["implementation"] = {}
    for k, (a, z) in P.items():
        x = D.loc[a:z]; yrs = len(x) / A
        traded = float(x["traded"].sum()) if "traded" in x else float("nan")
        row = {"turnover": traded / yrs if yrs else float("nan"), "cost_drag": float(x["cost"].sum() / yrs),
               "breakeven_bp": float((x["price"] + x["funding"]).sum() / traded * 1e4) if traded else float("nan"),
               "liquidations": int((x.get("liquidation", pd.Series(0, index=x.index)) != 0).sum())}
        if POS is not None:
            p = POS.loc[a:z]; p = p.loc[:, (p != 0).any()]
            if len(p):
                on = (p != 0).astype(int); lens = []
                for c in on:
                    dlt = np.diff(np.r_[0, on[c].to_numpy(), 0]); lens += list(np.where(dlt == -1)[0] - np.where(dlt == 1)[0])
                row.update({"long": float((p > 0).sum(1).mean()), "short": float((p < 0).sum(1).mean()),
                            "gross": float(p.abs().sum(1).mean()), "holding_days": float(np.mean(lens)) if lens else float("nan")})
        N["implementation"][k] = row
    # robustness: the other runs, before the test
    rob = {}
    for r in runs:
        if r["variant"] == frozen or r["period"] == "test":
            continue
        rob.setdefault(r["variant"], {})[r["period"]] = r["s"].get("net_sharpe")
    N["robustness"] = rob
    N["base_sharpe_by_run_period"] = {r["period"]: r["s"].get("net_sharpe") for r in chain}
    # luck
    L = luck_rows(name, N["family"], N["asset"]); N["luck"] = L
    if L.get("family_asset"):
        try:
            line = float(L["family_asset"]["luck"]); x = net.loc[TR[0]:TR[1]].to_numpy()
            p_, g3, g4 = deflated(x, line)
            N["luck"]["deflated"] = {"train_net_sr": sharpe(x), "line": line, "minus_line": sharpe(x) - line, "prob": p_, "skew": g3, "kurt": g4}
        except ValueError:
            pass
    # monthly table
    mt = net.resample("ME").sum()
    N["monthly"] = {str(y): {str(m.month): float(v) for m, v in g_.items()} for y, g_ in mt.groupby(mt.index.year)}
    # ------------------------------------------------------------- figures
    style(); cuts = [pd.Timestamp(VA[0])] + ([pd.Timestamp(TS)] if tested else [])
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(7, 3.4), sharex=True, gridspec_kw={"height_ratios": [2.6, 1], "hspace": 0.08})
    ax.plot(gross.cumsum() * 100, color=GREY, lw=1.0, ls="--", label="Gross (before costs)")
    ax.plot(net.cumsum() * 100, color=BLUE, label="Net"); ax.axhline(0, color="#999", lw=0.5)
    mark_periods(ax, P, cuts); ax.set_ylabel("Cumulative return (%)"); ax.legend(loc="upper left")
    ddp = dd * 100
    ax2.fill_between(ddp.index, ddp, 0, color=RED, alpha=0.25, lw=0); ax2.plot(ddp, color=RED, lw=0.8)
    for c in cuts: ax2.axvline(c, color="#555", lw=0.6, ls=":")
    ax2.set_ylabel("Drawdown (%)")
    fig.savefig(out / "fig_cumulative.pdf"); plt.close(fig)
    fig, axes = plt.subplots(1, 2, figsize=(7, 2.5))
    cols = {full_lab: PURPLE, "Test": GREEN}
    for axx, key, lab, sc in [(axes[0], "sr", "Net Sharpe ratio", 1), (axes[1], "mdd", "Maximum drawdown (%)", 100)]:
        allv = np.concatenate([np.array(v[key]) * sc for v in dists.values()])
        bins = np.linspace(np.percentile(allv, 0.5), np.percentile(allv, 99.5), 45)
        for nm, dv in dists.items():
            vals = np.array(dv[key]) * sc
            axx.hist(vals, bins=bins, color=cols[nm], alpha=0.28, density=True)
            axx.hist(vals, bins=bins, color=cols[nm], histtype="step", lw=1.1, density=True, label=nm)
            sv = (N["perf"]["full"] if nm == full_lab else N["perf"]["test"])["sample"][key] * sc
            axx.axvline(sv, color=cols[nm], lw=1.0, ls="--")
        axx.set_xlabel(lab); axx.set_yticks([]); axx.grid(axis="y", visible=False)
        axx.tick_params(axis="x", top=False, which="both"); axx.tick_params(axis="y", which="both", left=False, right=False)
    axes[0].axvline(0, color="#555", lw=0.6, ls=":"); axes[0].legend(loc="upper left", fontsize=8.5)
    fig.tight_layout(w_pad=2.0); fig.savefig(out / "fig_distributions.pdf"); plt.close(fig)
    if b is not None and len(mb) > 6:
        fig, ax = plt.subplots(figsize=(7, 2.7))
        colors_ = [PCOL["Train"] if i <= pd.Timestamp(TR[1]) else PCOL["Validation"] if i <= pd.Timestamp(VA[1]) else PCOL["Test"] for i in mb.index]
        ax.scatter(mb["b"] * 100, mb["n"] * 100, s=14, c=colors_, alpha=0.85, edgecolors="none")
        fit = np.polyfit(mb["b"], mb["n"], 1); xs = np.linspace(mb["b"].min(), mb["b"].max(), 50)
        ax.plot(xs * 100, np.polyval(fit, xs) * 100, color=GREY, lw=1.0, ls="--")
        ax.axhline(0, color="#999", lw=0.5); ax.axvline(0, color="#999", lw=0.5); ax.grid(axis="x", visible=True)
        ax.set_xlabel(f"{bname} monthly return (%)"); ax.set_ylabel("Strategy monthly net return (%)")
        from matplotlib.lines import Line2D
        ax.legend(handles=[Line2D([], [], marker="o", ls="", color=PCOL[k], label=k, ms=4) for k in P], loc="upper left")
        fig.savefig(out / "fig_benchmark.pdf"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 2.5))
    if legs:
        ax.plot(D["price_long"].cumsum() * 100, color=GREEN, label="Long leg (price)")
        ax.plot(D["price_short"].cumsum() * 100, color=RED, label="Short leg (price)")
    else:
        ax.plot(D["price"].cumsum() * 100, color=BLUE, label="Price")
    ax.plot(D["funding"].cumsum() * 100, color=BRONZE, label=fund_label)
    ax.plot((D["cost"] + D.get("liquidation", 0)).cumsum() * 100, color=GREY, label="Costs" + (" and liquidations" if D.get("liquidation", pd.Series(0)).abs().sum() else ""))
    ax.axhline(0, color="#999", lw=0.5); mark_periods(ax, P, cuts); ax.set_ylabel("Cumulative P&L (%)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, fontsize=9)
    fig.savefig(out / "fig_sources.pdf"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 2.6))
    for qq, c, lab in [(0, BLUE, "All days"), (.01, BRONZE, "Without the best 1% of days"), (.05, RED, "Without the best 5% of days")]:
        y = net.copy()
        if qq: y.loc[y.nlargest(int(math.ceil(len(y) * qq))).index] = 0
        ax.plot(y.cumsum() * 100, color=c, lw=1.2, label=lab)
    ax.axhline(0, color="#999", lw=0.5); mark_periods(ax, P, cuts); ax.set_ylabel("Cumulative net return (%)"); ax.legend(loc="lower left", fontsize=8)
    fig.savefig(out / "fig_concentration.pdf"); plt.close(fig)
    (out / "numbers.json").write_text(json.dumps(N, indent=1, default=float))
    (out / "numbers.md").write_text(numbers_md(N))
    print(f"wrote {out / 'numbers.md'} and the figures; next: write {out / 'text.md'}, then run build")


# ------------------------------------------------------------------ the numbers, for the reporter
def pc(v, d=1):
    return "n/a" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v * 100:.{d}f}%"


def f2(v):
    return "n/a" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v:.2f}"


def numbers_md(N):
    L = [f"# {N['name']}: numbers for the report", "",
         f"Status {N['status']}, family {N['family']}, asset {N['asset']}, frozen variant {N['frozen_variant']}, "
         f"sample {N['start']} to {N['end']}, test {'opened' if N['tested'] else 'sealed'}. Runs: {', '.join(N['runs'])}.", ""]
    if N.get("zone"):
        z = N["zone"]; L += [f"Test zone: {z['zone']} (test mean / earlier mean {f2(z['ratio'])}, test NW t {f2(z['test_t'])}). "
                             f"Full-sample net NW t {f2(N['t_full_nw'])}: {'money possible (t >= 2)' if N['t_full_nw'] >= 2 else 'paper only (t < 2)'}.", ""]
    for k, v in N["perf"].items():
        s, q = v["sample"], v["q"]
        L.append(f"## Performance, {N['full_label'] if k == 'full' else 'Test'} (sample, then 5/50/95 bootstrap)")
        for m_, lab, pct in [("ret", "Annual return", 1), ("vol", "Volatility", 1), ("sr", "Sharpe", 0), ("mdd", "Max drawdown", 1), ("worst", "Worst month", 1), ("pos", "Positive months", 1)]:
            fmt = (lambda x: pc(x)) if pct else f2
            L.append(f"- {lab}: {fmt(s[m_])} [{', '.join(fmt(x) for x in q[m_])}]")
        L.append("")
    L.append("## By period")
    for k, v in N["by_period"].items():
        L.append(f"- {k}: net Sharpe {f2(v['sr'])} [{f2(v['sr_q'][0])}, {f2(v['sr_q'][2])}], gross Sharpe {f2(v['gross_sr'])}, annual return {pc(v['ret'])}")
    L += ["", "Net return by year: " + ", ".join(f"{y} {pc(v, 0)}" for y, v in N["yearly"].items()), ""]
    d = N["drawdown"]; L += [f"Drawdown: max {pc(d['max'])}, peak {d['peak']}, trough {d['trough']}, recovered {d['recovered']}; longest time under water {d['longest_days']} days.", ""]
    if N.get("exposure"):
        L.append(f"## Exposure to {N['benchmark']}")
        for k, e in N["exposure"].items():
            L.append(f"- {k}: beta {f2(e['beta'])} (t {f2(e['beta_t'])}), correlation {f2(e['corr'])}, alpha {pc(e['alpha'])} a year (t {f2(e['alpha_t'])})")
        L += [f"- {N['benchmark']} Sharpe {f2(N['bench_cut']['sr'])}, without its best 1% of days {f2(N['bench_cut']['sr_ex1'])}", ""]
    S = N["sources"]; L.append(f"## Sources of P&L (% of capital, {'long and short legs' if S['legs'] else 'one price leg'}; {S['funding_label']})")
    for k, v in S["by_period"].items():
        legs = f"long {pc(v['price_long'], 0)}, short {pc(v['price_short'], 0)}" if S["legs"] else f"price {pc(v['price'], 0)}"
        L.append(f"- {k}: {legs}, {S['funding_label'].lower()} {pc(v['funding'], 0)}, costs {pc(v['costs'], 0)}")
    L += ["", "## Concentration in time"]
    for k, v in N["conc_days"].items():
        L.append(f"- {k}: Sharpe {f2(v['sr'])}; best 1% ({v['top1']['days']} days) = {pc(v['top1']['share'], 0)} of net P&L, Sharpe without {f2(v['top1']['sr'])}, return without {pc(v['top1']['ret'])}; Sharpe without best 5% {f2(v['top5']['sr'])}")
    R = N["regularity"]; L.append(f"- Each month without its 2 best days: positive in {pc(R['months_positive_without_best2'], 0)} of months. By year (best 2 days of each month / all other days): "
                                   + "; ".join(f"{y} {pc(v['best2'], 0)} / {pc(v['rest'], 0)}" for y, v in R["by_year"].items()))
    if N["conc_names"]:
        L += ["", "## Concentration in names (net P&L by name, by run)"]
        for k, v in N["conc_names"].items():
            L.append(f"- {k}: {v['names']} names; best name {v['best']} {pc(v['top1'], 0)}, best 5 {pc(v['top5'], 0)}, best 10 {pc(v['top10'], 0)}; without the best 5: {pc(v['ex5'], 0)} of capital")
    L += ["", "## Implementation, by period"]
    for k, v in N["implementation"].items():
        L.append(f"- {k}: " + ", ".join(f"{kk} {pc(vv) if kk == 'cost_drag' else (f2(vv) if isinstance(vv, float) else vv)}" for kk, vv in v.items()))
    L += ["", "## Variants, controls and stress runs (net Sharpe by period; frozen version: " + N["frozen_variant"] + ")"]
    L.append(f"- frozen version: " + ", ".join(f"{p} {f2(v)}" for p, v in N["base_sharpe_by_run_period"].items()))
    for k, v in N["robustness"].items():
        L.append(f"- {k}: " + ", ".join(f"{p} {f2(x)}" for p, x in v.items()))
    Lk = N["luck"]; L += ["", "## Luck"]
    L.append(f"- Tries counted for this strategy: {Lk.get('tries')}")
    if Lk.get("family_asset"): L.append(f"- Family and asset: {Lk['family_asset']}")
    if Lk.get("desk"): L.append(f"- Desk: {Lk['desk']}")
    if Lk.get("deflated"):
        dd_ = Lk["deflated"]; L.append(f"- Train net Sharpe {f2(dd_['train_net_sr'])}, minus the luck line {f2(dd_['line'])} = {f2(dd_['minus_line'])}; probability the true train Sharpe exceeds the line {pc(dd_['prob'], 0)} (skewness {f2(dd_['skew'])}, kurtosis {f2(dd_['kurt'])})")
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ build
def tex_escape(t):
    t = t.strip()
    t = t.replace("\\", r"\textbackslash{}")
    for a, b in [("&", r"\&"), ("%", r"\,\%"), ("$", r"\$"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"), ("}", r"\}"), ("~", r"\textasciitilde{}"), ("^", r"\^{}")]:
        t = t.replace(a, b)
    t = t.replace(r"\textbackslash\{\}", r"\textbackslash{}")
    t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
    t = re.sub(r"(?<![\w.])-(?=\d)", "$-$", t)
    t = t.replace("\n\n", "\n\n")
    return t


def read_text(path):
    secs, cur = {}, None
    for line in path.read_text().splitlines():
        m = re.match(r"^##\s+(\w+)\s*$", line)
        if m:
            cur = m.group(1).lower(); secs[cur] = []
        elif cur:
            secs[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in secs.items()}


def m_(s):
    return s.replace("-", "$-$")


def fpc(v, d=1):
    return "" if v is None or (isinstance(v, float) and math.isnan(v)) else m_(f"{v * 100:.{d}f}") + r"\,\%"


def ff(v, d=2):
    return "" if v is None or (isinstance(v, float) and math.isnan(v)) else m_(f"{v:.{d}f}")


def table(header, rows, caption, label, cols, size=""):
    body = "\n".join(" & ".join(r) + r" \\[3pt]" for r in rows)
    return (rf"\begin{{table}}[H]{size}" "\n" rf"\begin{{tabular*}}{{\textwidth}}{{@{{\extracolsep{{\fill}}}}{cols}@{{}}}}" "\n"
            r"\toprule" "\n" + header + r" \\" "\n" r"\midrule" "\n" + body + "\n" r"\bottomrule" "\n" r"\end{tabular*}" "\n"
            rf"\caption{{{caption}}}" "\n" rf"\label{{{label}}}" "\n" r"\end{table}")


def figure(fname, caption, label):
    return (r"\begin{figure}[H]" "\n" rf"\centering\includegraphics[width=\textwidth]{{{fname}}}" "\n"
            rf"\caption{{{caption}}}" "\n" rf"\label{{{label}}}" "\n" r"\end{figure}")


def run_kind(v):
    """What a saved run is, from the name the desk gave it, and a readable label."""
    s = re.sub(r"^(base-)?(redteam-)?", "", v.lower())
    for pat, fmt in [(r"^costs?x(\d+(?:\.\d+)?)$|^cost(\d+)x$|^tiersx(\d+)$", "Costs x{n}"),
                     (r"^(?:delay|lag)(\d+)$", "Trades {n} day later"), (r"^lastprice$", "Last price instead of mark price"),
                     (r"^borrow(\d+)bp$", "Borrow at {n} bp a year"), (r"^spread(\d+)$", "Borrow spread {n} bp"),
                     (r"^cost(\d+(?:\.\d+)?)$", "Cost {n} bp"), (r"^fix\d+$", None), (r"^stress\w*$", None)]:
        m = re.match(pat, s)
        if m:
            n = next((g for g in m.groups() if g), "") if m.groups() else ""
            lab = fmt.format(n=n) if fmt else v
            if fmt and "day later" in lab and n not in ("1",):
                lab = lab.replace("day later", "days later")
            return "stress", (tex_escape(lab).replace("Costs x", r"Costs $\times$ ") if lab.startswith("Costs x") else tex_escape(lab))
    if re.search(r"control|twin|placebo", s):
        return "control", tex_escape(v)
    if "diagnostic" in s:
        return "diagnostic", tex_escape(v)
    return "variant", tex_escape(v)


def build(name):
    rdir = results_dir(name); out = rdir / "report"
    N = json.loads((out / "numbers.json").read_text())
    tf = out / "text.md"
    if not tf.exists():
        raise SystemExit(f"write {tf} first (sections: {', '.join(SECTIONS)})")
    T = {k: tex_escape(v) for k, v in read_text(tf).items()}
    missing = [k for k in SECTIONS if k not in T and not (k == "exposure" and not N.get("exposure"))]
    if missing:
        raise SystemExit(f"text.md misses the sections: {', '.join(missing)}")
    P = N["periods"]; tested = N["tested"]; full_lab = N["full_label"]
    rows_def = [("Annualised return", "ret", True), ("Annualised volatility", "vol", True), ("Sharpe ratio", "sr", False),
                ("Maximum drawdown", "mdd", True), ("Worst month", "worst", True), ("Positive months", "pos", True)]
    def perf(key, cap, lab):
        s, q = N["perf"][key]["sample"], N["perf"][key]["q"]
        rows = [[l] + [(fpc(x, 0 if k == "pos" else 1) if p else ff(x)) for x in [s[k]] + q[k]] for l, k, p in rows_def]
        return table(" & Sample & 5th percentile & Median & 95th percentile", rows, cap, lab, "lrrrr")
    rng_txt = r"Percentiles of a stationary block bootstrap of daily returns (blocks of 20 days, 2\,000 paths). Returns in fraction of capital, not compounded."
    span = lambda a, b: f"{pd.Timestamp(a):%B %Y} to {pd.Timestamp(b):%B %Y}"
    body = []
    body += [r"\section{Hypothesis and method}", T["hypothesis"], "", T["method"], ""]
    body += [r"\section{Performance}", T["performance"], ""]
    body.append(perf("full", f"Net performance, {full_lab.lower()}, {span(N['start'], N['end'] if tested else P['Validation'][1])}, after costs" + (" and funding" if N['sources']['funding_label'] == 'Funding' else " and financing") + f". {rng_txt}", "tab:perf"))
    if tested:
        body.append(perf("test", f"Net performance over the test alone, {span(P['Test'][0], P['Test'][1])}. Same method as Table~\\ref{{tab:perf}}.", "tab:perftest"))
    cutnote = "Dotted lines mark the start of the validation" + (" and of the test." if tested else ".")
    body.append(figure("fig_cumulative.pdf", f"Cumulative net and gross return (top) and drawdown of the net return (bottom), in percent of capital, linear scale. {cutnote}", "fig:cum"))
    body.append(figure("fig_distributions.pdf", "Bootstrap distributions of the net Sharpe ratio (left) and of the maximum drawdown (right). Dashed lines: the values measured on the sample.", "fig:dist"))
    if N.get("exposure"):
        bn = N["benchmark"]; body += [r"\section{Market exposure}", T["exposure"], ""]
        rows = []
        cols_ = ["full"] + (["test"] if tested else [])
        E = N["exposure"]
        rows.append([f"Beta to {bn} (daily)"] + [f"{ff(E[c]['beta'])} \\;(t {ff(E[c]['beta_t'])})" for c in cols_])
        rows.append([f"Correlation to {bn}"] + [ff(E[c]["corr"]) for c in cols_])
        rows.append([f"Alpha over {bn}, annualised"] + [f"{fpc(E[c]['alpha'])} \\;(t {ff(E[c]['alpha_t'])})" for c in cols_])
        body.append(table(" & " + " & ".join([full_lab] + (["Test"] if tested else [])), rows,
                          f"Exposure to the market. Regression of daily net returns on {bn} daily returns; t-statistics with Newey-West standard errors (10 lags).", "tab:expo", "l" + "r" * len(cols_)))
        if (out / "fig_benchmark.pdf").exists():
            body.append(figure("fig_benchmark.pdf", f"Monthly net return of the strategy against the monthly return of {bn}. Dashed line: least-squares fit.", "fig:bench"))
    body += [r"\section{Where the profit comes from}", T["sources"], ""]
    body.append(figure("fig_sources.pdf", "Cumulative P\\&L by source, in percent of capital: " + ("price of the long leg, price of the short leg, " if N["sources"]["legs"] else "price, ") + N["sources"]["funding_label"].lower() + ", and costs.", "fig:src"))
    body += [r"\section{Concentration}", T["concentration"], ""]
    C = N["conc_days"]; cols_ = ["full"] + (["test"] if tested else [])
    rows = [["Net Sharpe ratio, all days"] + [ff(C[c]["sr"]) for c in cols_],
            [r"Share of net P\&L from the best 1\,\% of days"] + [f"{fpc(C[c]['top1']['share'], 0)} \\;({C[c]['top1']['days']} days)" for c in cols_],
            [r"Net Sharpe ratio without the best 1\,\% of days"] + [ff(C[c]["top1"]["sr"]) for c in cols_],
            [r"Annualised return without the best 1\,\% of days"] + [fpc(C[c]["top1"]["ret"]) for c in cols_],
            [r"Net Sharpe ratio without the best 5\,\% of days"] + [ff(C[c]["top5"]["sr"]) for c in cols_]]
    if N.get("bench_cut"):
        rows.append([f"{N['benchmark']} Sharpe ratio, all days / without its best 1\\,\\%", f"{ff(N['bench_cut']['sr'])} / {ff(N['bench_cut']['sr_ex1'])}"] + [""] * (len(cols_) - 1))
    body.append(table(" & " + " & ".join([full_lab] + (["Test"] if tested else [])), rows,
                      "Concentration of the gains in time. A day removed is set to zero, as if the strategy had been flat that day." + (f" The {N['benchmark']} line gives the same cut on the market over the same span." if N.get("bench_cut") else ""), "tab:conc", "l" + "r" * len(cols_)))
    if N["conc_names"]:
        ks = list(N["conc_names"]); CN = N["conc_names"]
        rows = [["Names traded"] + [str(CN[k]["names"]) for k in ks],
                [r"Share of net P\&L, best name"] + [fpc(CN[k]["top1"], 0) for k in ks],
                [r"Share of net P\&L, best 5 names"] + [fpc(CN[k]["top5"], 0) for k in ks],
                [r"Share of net P\&L, best 10 names"] + [fpc(CN[k]["top10"], 0) for k in ks],
                [r"Net P\&L without the best 5 names, \% of capital"] + [fpc(CN[k]["ex5"], 0) for k in ks]]
        body.append(table(" & " + " & ".join(ks), rows, r"Concentration of the gains across names: net P\&L by name, best names first. A share above 100\,\% means the other names lost money together.", "tab:names", "l" + "r" * len(ks)))
    body.append(figure("fig_concentration.pdf", r"Cumulative net return with all days, and with the best 1\,\% and 5\,\% of days set to zero.", "fig:conc"))
    body += [r"\section{Implementation}", T["implementation"], ""]
    I = N["implementation"]; ks = list(I)
    def g(k, f_):
        return [f_(I[p].get(k)) for p in ks]
    rows = []
    if all("long" in I[p] for p in ks):
        rows.append(["Names held long / short, average"] + [f"{I[p]['long']:.0f} / {I[p]['short']:.0f}" for p in ks])
        rows.append(["Gross exposure, average"] + g("gross", ff))
        rows.append(["Holding period of a position, days"] + g("holding_days", lambda v: ff(v, 0)))
    rows += [["Turnover, times the capital a year"] + g("turnover", lambda v: ff(v, 1)),
             [r"Cost drag, \% of capital a year"] + g("cost_drag", lambda v: fpc(v)),
             ["Break-even cost, bp one way"] + g("breakeven_bp", lambda v: ff(v, 1))]
    if any(I[p]["liquidations"] for p in ks):
        rows.append(["Days with a liquidation"] + [str(I[p]["liquidations"]) for p in ks])
    body.append(table(" & " + " & ".join(ks), rows, r"Implementation. The break-even cost is the one-way cost per unit traded at which the gross P\&L of the period would be fully spent.", "tab:impl", "l" + "r" * len(ks)))
    body += [r"\section{Robustness}", T["robustness"], ""]
    nice = {"train": "Train", "validation": "Validation", "train+validation": "Train and validation"}
    base_sr = N["base_sharpe_by_run_period"]
    stress, other = {}, {}
    for v, d_ in N["robustness"].items():
        kind, lab = run_kind(v)
        if kind == "stress":
            merged = stress.setdefault(lab, (kind, lab, {}))[2]
            merged.update({p: x for p, x in d_.items() if x is not None})       # the same test run twice: one row
        else:
            other[v] = (kind, lab, d_)
    if stress:
        per_cols = [p for p in ["train", "validation", "train+validation"] if any(p in d_ for _, _, d_ in stress.values())]
        rows = [["Frozen version, as tested"] + [ff(base_sr.get(p)) for p in per_cols] + [""] * len(per_cols)]
        for v, (_, lab, d_) in stress.items():
            rows.append([lab] + [ff(d_.get(p)) for p in per_cols]
                        + [m_(f"{d_[p] - base_sr[p]:+.2f}") if d_.get(p) is not None and base_sr.get(p) is not None else "" for p in per_cols])
        hdr = " & " + " & ".join(nice[p] for p in per_cols) + " & " + " & ".join(r"$\Delta$ " + nice[p].lower() for p in per_cols)
        body.append(table(hdr, rows, "Stress tests of the frozen version, run by the Red team before the test: net Sharpe ratio, and its change from the frozen version on the same period.", "tab:stress", "l" + "r" * 2 * len(per_cols)))
    if other:
        rows = []
        kinds = {"control": "control", "diagnostic": "diagnostic", "variant": "variant"}
        for v, (kind, lab, d_) in other.items():
            for p, x in d_.items():
                rows.append([lab, kinds.get(kind, kind), nice.get(p, p), ff(x), ff(base_sr.get(p))])
        body.append(table(" & Kind & Run on & Net Sharpe & Frozen version", rows,
                          "Other versions run before the test, each on the period where the desk ran it: variants considered at the validation, controls and diagnostics that check the mechanism. They are not the strategy; the last column gives the frozen version on the same period for comparison.", "tab:other", "lllrr"))
    body += [r"\section{Luck and multiple testing}", T["luck"], ""]
    Lk = N["luck"]; rows = []
    if Lk.get("tries") is not None: rows.append(["Tries counted for this strategy", str(Lk["tries"])])
    if Lk.get("family_asset"):
        fa = Lk["family_asset"]; rows.append([f"Tries in the family, {tex_escape(N['family'])} on {tex_escape(N['asset'])} (effective number)", f"{fa['N']} \\;({fa['N_eff']})"])
        rows.append([f"Luck line: best Sharpe of {fa['N_eff']} tries with no skill, {fa['years']} years", fa["luck"]])
    if Lk.get("deflated"):
        d_ = Lk["deflated"]; rows.append(["Train net Sharpe ratio / minus the luck line", f"{ff(d_['train_net_sr'])} \\;/\\; {ff(d_['minus_line'])}"])
        rows.append(["Probability that the true train Sharpe exceeds the luck line", fpc(d_["prob"], 0)])
    if Lk.get("desk"):
        ds = Lk["desk"]; rows.append(["Whole desk: tries (effective number) / luck line", f"{ds['N']} \\;({ds['N_eff']}) \\;/\\; {ds['luck']}"])
    cap = r"Multiple testing. Luck line: expected best annual Sharpe ratio of $N_{\mathrm{eff}}$ independent tries with no skill (Bailey and L\'opez de Prado, 2014); $N_{\mathrm{eff}}$ discounts tries by their correlation before costs. The probability is the deflated Sharpe ratio"
    if Lk.get("deflated"):
        cap += f", corrected for the skewness ({ff(Lk['deflated']['skew'], 1)}) and the kurtosis ({ff(Lk['deflated']['kurt'], 0)}) of daily train returns."
    body.append(table(" & Value", rows, cap + ("" if cap.endswith(".") else "."), "tab:luck", "lr"))
    body += [r"\section{Risks and limits}", T["risks"], "", r"\section{Decision}", T["decision"], ""]
    mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    def cell(v):
        if v is None: return ""
        s = f"{v * 100:.1f}"; return r"\textcolor{brick}{" + m_(s) + "}" if v < 0 else s
    mrows = []
    for y, mm in N["monthly"].items():
        mrows.append(" & ".join([y] + [cell(mm.get(str(i + 1))) for i in range(12)] + [r"\textbf{" + cell(N["yearly"].get(y)) + "}"]) + r" \\[2pt]")
    body += [r"\appendix", r"\section{Monthly returns}",
             r"\begin{table}[H]\footnotesize" "\n" r"\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}l" + "r" * 13 + r"@{}}" "\n" r"\toprule" "\n"
             " & " + " & ".join(mon) + r" & Year \\" "\n" r"\midrule" "\n" + "\n".join(mrows) + "\n" r"\bottomrule" "\n" r"\end{tabular*}" "\n"
             r"\caption{Monthly net return, \% of capital.}" "\n" r"\end{table}"]
    status = f"Status: {N['status']}"
    if N.get("zone"):
        status += f", {N['zone']['zone']} test zone \\quad·\\quad full-sample t {ff(N['t_full_nw'])}"
    footer = "Runs: " + ", ".join(N["runs"]) + f". Strategy file: {N['strategy_file']}. Frozen version: {N['frozen_variant']}."
    tpl = (ROOT / "lab" / "strategy_report.tex").read_text()
    tex = (tpl.replace("<<TITLE>>", tex_escape(N["name"])).replace("<<DATE>>", f"{pd.Timestamp(N['date']):%d %B %Y}")
           .replace("<<STATUS>>", status).replace("<<ABSTRACT>>", T["abstract"]).replace("<<BODY>>", "\n\n".join(body))
           .replace("<<FOOTER>>", tex_escape(footer)))
    (out / "report.tex").write_text(tex)
    engine = shutil.which("pdflatex") or shutil.which("tectonic")
    if not engine:
        raise SystemExit("No LaTeX engine found. Install one: `brew install tectonic` (small) or MacTeX / BasicTeX, then run build again.")
    cmd = [engine, "-interaction=nonstopmode", "report.tex"] if engine.endswith("pdflatex") else [engine, "report.tex"]
    for _ in range(2 if engine.endswith("pdflatex") else 1):
        r = subprocess.run(cmd, cwd=out, capture_output=True, text=True)
    pdf = out / "report.pdf"
    if not pdf.exists():
        print(r.stdout[-3000:]); raise SystemExit("LaTeX failed: see results/<strategy>/report/report.log")
    dest = sheet_path(name).parent / f"{name} - Report.pdf"
    shutil.copy(pdf, dest)
    print(f"wrote {dest}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("strategy")
    ap.add_argument("step", choices=["compute", "build"])
    a = ap.parse_args()
    compute(a.strategy) if a.step == "compute" else build(a.strategy)
