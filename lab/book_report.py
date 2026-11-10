"""
The candidate review: the PDF a portfolio manager reads before adding a strategy to an existing book.
Same layout as the strategy report (LaTeX, numbered sections, tables with bootstrap ranges, figures in the desk style).

Two steps, with the PM (skill portfolio-manager, reference/candidate-review.md) writing the text in between:

    poetry run python lab/book_report.py review "ETF TSMOM 12-Month" compute
        reads the book (vault/4 Book/Book.md) and the candidate, computes every number and figure, and writes
        results/_book_reviews/<candidate>/numbers.md (what the PM reads) and numbers.json (what build reads).
    poetry run python lab/book_report.py review "ETF TSMOM 12-Month" build
        reads results/_book_reviews/<candidate>/text.md (written by the PM), fills the template, compiles it with
        pdflatex (or tectonic), and writes "vault/4 Book/Reviews/<Candidate> - Candidate review.pdf".

    A candidate made outside the desk (no strategy card, no sealed test): add --returns <csv> --family <family>.
    It can be reviewed, never entered: paper at most.

The book: every row of the table "Strategies" of Book.md. A row whose strategy appears in the table "Returns of each
strategy" with a `--strategy NAME <file or runs> --family NAME FAMILY` line is read from there (built outside the
desk); any other row is a desk strategy, read from the runs of its frozen version, like the candidate.

The candidate: a desk strategy whose test is opened (results/<strategy>/TEST_DONE); its runs of the frozen version,
train, validation and test, stitched. A strategy whose test is still sealed is not a candidate.

Sizing (lab/portfolio.py): each strategy at 15% volatility with its trailing 60-day volatility known the day before;
equal risk by family; the book at its 10% target by the IDM, capped at 2.5. The candidate enters at half the weight
equal risk by family would give it, the others shrinking in proportion: that is the weight tested.

The rule (vault/Toolbox/My Research Routine.md): Sharpe(candidate, after the luck haircut) > correlation x Sharpe(book);
then a stationary block bootstrap (blocks of 20 days, 2000 histories): the share of histories where the book with the
candidate at entry weight has the higher Sharpe, on the whole common window and on the days after the candidate's
train (data it was not fitted on). The stricter of the two decides: 90% or more enters at half weight (only if the
candidate's full-sample t is 2 or more, and never for imported returns), 60 to 90% paper, below 60% stays out.

Book construction (no book yet, a set of strategies):

    poetry run python lab/book_report.py construct "Desk book" compute [--strategy "A" --strategy "B"] [--import NAME FILE FAMILY]
    poetry run python lab/book_report.py construct "Desk book" build
        default: every strategy in vault/2 Strategies/Passed whose test is opened. Work files in
        results/_book_constructions/<name>/, PDF in "vault/4 Book/Reviews/<Name> - Book construction.pdf".
        A strategy earns its place if dropping it lowers the book's Sharpe in 60% of bootstrap histories or more; it can carry
        money with status passed, a full-sample t of 2 or more and a Sharpe ratio after the luck haircut above zero.

Every number in the PDF is computed here. The text adds the reading, never a new number.
"""
import argparse, json, math, re, shlex, shutil, subprocess, sys
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                       # noqa: E402
import numpy as np                                                    # noqa: E402
import pandas as pd                                                   # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lab.portfolio import read_runs                                   # noqa: E402
from lab.strategy_report import (results_dir, frontmatter, periods_of, list_runs, daily_of, luck_rows,  # noqa: E402
                                 nw_t_mean, style, tex_escape, read_text, m_, fpc, ff, table, PAL)
from lab.sheets import sheet_path                                     # noqa: E402

A = 365
STRAT_VOL, BOOK_VOL, IDM_CAP, VOL_WINDOW = 0.15, 0.10, 2.5, 60
BLOCK, PATHS, SEED = 20, 2000, 7
ROLL_DAYS, ROLL_WEEKS = 182, 26
BLUE, RED, GREEN, BRONZE, STEEL, PURPLE, GREY = PAL
COLS = [BRONZE, RED, STEEL, PURPLE, GREY, BLUE]                       # members; the candidate is always green
BOOK_FILE = ROOT / "vault" / "4 Book" / "Book.md"
WORK = ROOT / "results" / "_book_reviews"
OUT_PDF = ROOT / "vault" / "4 Book" / "Reviews"
SECTIONS = ["abstract", "book", "weights", "performance", "diversification", "exposures", "stress", "decision", "needs", "limits"]
FACTORS = [("SPY", "etf_daily", "US equities (SPY)"), ("TLT", "etf_daily", "long Treasuries (TLT)"),
           ("UUP", "etf_daily", "the dollar (UUP)"), ("GLD", "etf_daily", "gold (GLD)"), ("BTC", "crypto_daily", "bitcoin")]
EPISODES = [("Global financial crisis", "2008-09-01", "2009-03-09"), ("Euro debt crisis", "2011-07-22", "2011-10-03"),
            ("Taper tantrum", "2013-05-22", "2013-06-24"), ("China devaluation", "2015-08-10", "2015-08-25"),
            ("Volatility spike", "2018-01-26", "2018-02-08"), ("Q4 2018 sell-off", "2018-10-01", "2018-12-24"),
            ("Covid crash", "2020-02-19", "2020-03-23"), ("Crypto crash, China ban", "2021-05-12", "2021-07-20"),
            ("Equity and bond bear market", "2022-01-03", "2022-10-12"), ("Terra and 3AC", "2022-05-05", "2022-06-18"),
            ("FTX collapse", "2022-11-06", "2022-11-21"), ("US regional banks", "2023-03-08", "2023-03-17"),
            ("Yen carry unwind", "2024-07-31", "2024-08-05"), ("US tariff shock", "2025-04-02", "2025-04-08")]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def sharpe(x):
    x = np.asarray(x, float)
    return float(x.mean() / x.std() * math.sqrt(A)) if len(x) > 2 and x.std() > 0 else float("nan")


def boot_index(T, rng):
    out = np.empty((PATHS, T), dtype=int)
    for k in range(PATHS):
        idx, n = [], 0
        while n < T:
            s, L = rng.integers(T), rng.geometric(1 / BLOCK); idx.append((s + np.arange(L)) % T); n += L
        out[k] = np.concatenate(idx)[:T]
    return out


def boot_sr(x, idx):
    y = np.asarray(x)[idx]
    return y.mean(1) / y.std(1) * math.sqrt(A)


def metrics(s):
    m = s.resample("ME").sum(); eq = s.cumsum(); q = np.quantile(s, 0.05)
    return {"ret": float(s.mean() * A), "vol": float(s.std() * math.sqrt(A)), "sr": sharpe(s),
            "mdd": float((eq - eq.cummax()).min()), "worst": float(m.min()), "cvar": float(s[s <= q].mean()), "pos": float((m > 0).mean())}


def scale(r):
    vol = r.rolling(VOL_WINDOW, min_periods=20).std().shift(1) * math.sqrt(A)
    return r * STRAT_VOL / vol


def nw_multi(y, X, lags=3):
    X = np.column_stack([np.ones(len(X)), X]); b = np.linalg.lstsq(X, y, rcond=None)[0]; e = y - X @ b; n = len(y)
    S = (X * e[:, None]).T @ (X * e[:, None]) / n
    for l in range(1, lags + 1):
        G = (X[l:] * e[l:, None]).T @ (X[:-l] * e[:-l, None]) / n; S += (1 - l / (lags + 1)) * (G + G.T)
    Q = np.linalg.inv(X.T @ X / n); V = Q @ S @ Q / n
    r2 = 1 - (e @ e) / ((y - y.mean()) @ (y - y.mean()))
    return b, b / np.sqrt(np.diag(V)), float(r2)


# ------------------------------------------------------------------ inputs
def read_book(path):
    """Rows of the table Strategies, and the --strategy / --family lines of the table Returns of each strategy."""
    text = path.read_text(); fm = frontmatter(path)
    rows, sec = [], None
    for line in text.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            sec = h.group(1).strip().lower(); continue
        if sec == "strategies" and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and cells[0] not in ("Strategy", "") and not set(cells[0]) <= set("-: "):
                rows.append({"name": cells[0], "family": cells[1] if len(cells) > 1 else "", "status": cells[2] if len(cells) > 2 else ""})
    files, fams = {}, {}
    for chunk in re.findall(r"`([^`]*--strategy[^`]*)`", text):
        tok = shlex.split(chunk); i = 0
        while i < len(tok):
            if tok[i] == "--strategy":
                name = tok[i + 1]; j = i + 2; paths = []
                while j < len(tok) and not tok[j].startswith("--"):
                    paths.append(tok[j]); j += 1
                files[name] = paths; i = j
            elif tok[i] == "--family":
                fams[tok[i + 1]] = tok[i + 2]; i += 3
            else:
                i += 1
    return {"name": fm.get("name", "Book"), "rows": rows, "files": files, "families": fams}


def desk_series(name):
    """Net and gross daily returns of the frozen version of a desk strategy: train, validation, and test if opened."""
    _, TR, VA, TS = periods_of(name)
    rdir = results_dir(name); lock = rdir / "TEST_DONE"; tested = lock.exists()
    L = json.loads(lock.read_text()) if tested else {}
    frozen = L.get("variant", "base"); allr = list_runs(rdir)
    runs = [r for r in allr if r["variant"] == frozen]
    pick = lambda p: max([r for r in runs if r["period"] == p], key=lambda r: r["id"], default=None)
    chain = [pick("train"), pick("validation"), pick("train+validation")]
    if tested:
        chain.append(next((r for r in allr if r["id"] == L.get("run")), pick("test")))
    chain = [r for r in chain if r]
    if not chain:
        raise SystemExit(f"no run of variant {frozen!r} in {rdir}")
    ds = []
    for r in chain:
        d = daily_of(r)
        if len(d) > 1 and (d.index[1] - d.index[0]) < pd.Timedelta(days=1):
            d = d.resample("D").sum()
        ds.append(d)
    D = pd.concat(ds); D = D[~D.index.duplicated(keep="last")].sort_index()
    if not tested:
        D = D.loc[:VA[1]]
    D = D.loc[D.index >= D["total"].ne(0).idxmax()]
    return D["total"], D["price"] + D["funding"], {"runs": [r["id"] for r in chain], "train_end": TR[1], "test_start": TS,
                                                     "tested": tested, "variant": frozen}


def market_prices(test_start):
    from lab.data import load
    px = {}
    for sym, ds, _ in FACTORS:
        try:
            d = load(ds, test_start=test_start, open_test=True)
            d = d[d["symbol"] == ("BTCUSDT" if sym == "BTC" else sym)].set_index("date").sort_index()
            s = d["mark_close" if sym == "BTC" else "adj_close"]; s.index = pd.to_datetime(s.index).tz_localize(None)
            px[sym] = s[~s.index.duplicated()]
        except Exception as e:                       # no data on this machine: that factor is left out
            print(f"market {sym} skipped: {e}")
    return pd.DataFrame(px)


# ------------------------------------------------------------------ the book arithmetic
class Book:
    def __init__(self, N, fam):
        self.N, self.fam = N, fam

    def eq_weights(self, names):
        f = pd.Series({n: self.fam[n] for n in names})
        return pd.Series({n: 1 / f.nunique() / (f == f[n]).sum() for n in names})

    def run(self, w):
        w = w[w > 0]; C = self.N[w.index].corr().to_numpy(); v = w.to_numpy()
        idm = min(IDM_CAP, 1 / math.sqrt(v @ C @ v)) if len(w) > 1 else 1.0
        k = idm * BOOK_VOL / STRAT_VOL
        return self.N[w.index] @ w * k, w * k, float(idm)


def shaded(ax, mask, color=RED):
    mask = mask.fillna(False)
    if not mask.any():
        return
    blocks = (mask != mask.shift()).cumsum()
    for _, g in mask[mask].groupby(blocks[mask]):
        ax.axvspan(g.index[0], g.index[-1] + pd.Timedelta(days=1), color=color, alpha=0.08, lw=0)


# ------------------------------------------------------------------ compute
def compute(cand, returns=None, family=None, book_file=BOOK_FILE):
    B = read_book(book_file)
    out = WORK / slug(cand); out.mkdir(parents=True, exist_ok=True)
    members = [r["name"] for r in B["rows"] if r["name"] != cand]
    if not members:
        raise SystemExit("the book is empty: nothing to review against (book construction is another report)")
    nets, grosses, info, fam = {}, {}, {}, {}
    for r in B["rows"]:
        n = r["name"]
        if n == cand:
            continue
        if n in B["files"]:
            nets[n], grosses[n], inf = read_runs(B["files"][n]); info[n] = "; ".join(inf)
            fam[n] = B["families"].get(n) or r["family"]
        else:
            nets[n], grosses[n], inf = desk_series(n); info[n] = "runs " + ", ".join(inf["runs"])
            fam[n] = frontmatter(sheet_path(n)).get("family", r["family"])
    imported = returns is not None
    if imported:
        nets[cand], grosses[cand], inf = read_runs([returns]); info[cand] = "; ".join(inf)
        fam[cand] = family or cand; asset = "imported"; ci = {"tested": False, "train_end": None, "runs": []}
        status, haircut = "imported", 0.0
    else:
        fm = frontmatter(sheet_path(cand)); fam[cand] = fm.get("family", cand); asset = fm.get("asset", "")
        nets[cand], grosses[cand], ci = desk_series(cand); info[cand] = "runs " + ", ".join(ci["runs"])
        if not ci["tested"]:
            raise SystemExit(f"{cand}: its test is still sealed, so it is not a candidate yet")
        status = fm.get("status", "")
        lk = luck_rows(cand, fam[cand], asset).get("family_asset") or {}
        try:
            haircut = float(re.findall(r"-?\d+\.?\d*", str(lk.get("luck", "0")))[0])
        except (IndexError, ValueError):
            haircut = 0.0
    ALL = members + [cand]
    N = pd.DataFrame({n: scale(nets[n]) for n in ALL}).dropna()
    G = pd.DataFrame({n: scale(grosses[n]) for n in ALL}).reindex(N.index).dropna(); N = N.loc[G.index]
    if len(N) < 250:
        raise SystemExit(f"only {len(N)} common days between the book and the candidate: not enough to judge")
    bk = Book(N, fam)
    w0 = bk.eq_weights(members); wf = bk.eq_weights(ALL)
    we = wf.copy(); we[cand] = wf[cand] / 2; we[members] = we[members] * (1 - we[cand]) / we[members].sum()
    B0, W0, I0 = bk.run(w0); BE, WE, IE = bk.run(we); BF, WF, IF = bk.run(wf)
    rng = np.random.default_rng(SEED); T = len(N); idx = boot_index(T, rng)
    S0 = boot_sr(B0, idx); SE = boot_sr(BE, idx); SF = boot_sr(BF, idx)
    R = {"window": [str(N.index[0].date()), str(N.index[-1].date())], "days": T, "book": B["name"], "candidate": cand,
         "date": date.today().isoformat(), "imported": imported, "status": status, "asset": asset, "members": members}
    # composition
    R["comp"] = [{"name": n, "family": fam[n], "info": info[n], "sr": sharpe(N[n]), "w0": float(w0.get(n, 0)),
                  "we": float(we[n]), "wf": float(wf[n]), "cand": n == cand} for n in ALL]
    # performance with bootstrap ranges
    perf = {}
    for k, x in [("now", B0), ("entry", BE), ("full", BF)]:
        bs = [metrics(pd.Series(x.to_numpy()[i], index=x.index)) for i in idx[:1000]]
        perf[k] = {"s": metrics(x), "lo": {m: float(np.percentile([b[m] for b in bs], 5)) for m in bs[0]},
                   "hi": {m: float(np.percentile([b[m] for b in bs], 95)) for m in bs[0]}}
    R["perf"] = perf
    # alternatives
    alts = [("Current book", w0), ("Add the candidate at entry weight", we), ("Add the candidate at full weight", wf)]
    if len(members) >= 2:
        weakest = min(members, key=lambda n: sharpe(N[n])); rest = [n for n in members if n != weakest]
        alts += [(f"Drop {weakest}", bk.eq_weights(rest)), (f"Candidate in place of {weakest}", bk.eq_weights(rest + [cand]))]
        R["weakest"] = weakest
    R["alts"] = []
    for lab, w in alts:
        b, _, i = bk.run(w); s = boot_sr(b, idx); eq = b.cumsum()
        R["alts"].append({"label": lab, "sr": sharpe(b), "idm": i, "beats": None if lab == "Current book" else float((s > S0).mean()),
                          "mdd": float((eq - eq.cummax()).min()), "worst": float(b.resample("ME").sum().min())})
    # weight curve
    curve = []
    for c in np.arange(0.025, 0.401, 0.025):
        w = w0 * (1 - c); w[cand] = c; b, _, _ = bk.run(w); d = boot_sr(b, idx) - S0
        curve.append({"w": float(c), "sr": sharpe(b), "q": [float(v) for v in np.percentile(d, [5, 25, 50, 75, 95])], "share": float((d > 0).mean())})
    R["curve"] = curve; best = max(curve, key=lambda r: r["sr"]); R["curve_best"] = best
    # the rule
    cg = G[cand] - haircut * G[cand].std() / math.sqrt(A); cn = N[cand] - haircut * N[cand].std() / math.sqrt(A)
    corr = float(G[cand].corr(G[members] @ w0)); bad = B0 <= B0.quantile(0.10)
    mm = pd.DataFrame({"b": B0, "c": N[cand] * WE[cand]}).resample("ME").sum(); worstm = mm[mm["b"] <= mm["b"].quantile(0.25)]
    since = None
    if ci.get("train_end"):
        since = str((pd.Timestamp(ci["train_end"]) + pd.Timedelta(days=1)).date())
    share_after = None
    if since and pd.Timestamp(since) <= N.index[0]:
        since = None                                   # the whole common window is after the candidate's train
    if since and (N.index >= since).sum() >= 250:
        mask = N.index >= since; ia = boot_index(int(mask.sum()), np.random.default_rng(SEED))
        share_after = float((boot_sr(BE[mask], ia) > boot_sr(B0[mask], ia)).mean())
    t_full = nw_t_mean(nets[cand].to_numpy())
    share_entry = float((SE > S0).mean()); decide = min([s for s in [share_entry, share_after] if s is not None])
    money_ok = (not imported) and t_full >= 2 and status == "passed"
    decision = ("enter at half weight" if decide >= 0.9 and money_ok else "paper" if decide >= 0.6 else "stays out")
    if decision == "enter at half weight" and not (money_ok and sharpe(cn) > corr * sharpe(B0)):
        decision = "paper"                            # money needs the full-sample t, a desk test and the marginal rule
    R["rule"] = {"haircut": haircut, "sr_cand": sharpe(cn), "sr_book": sharpe(B0), "corr": corr, "thr": corr * sharpe(B0),
                 "passes": bool(sharpe(cn) > corr * sharpe(B0)), "corr_bad_days": float(G.loc[bad, cand].corr((G[members] @ w0)[bad])),
                 "cand_in_worst_months": float(worstm["c"].mean()), "share_entry": share_entry, "share_full": float((SF > S0).mean()),
                 "since": since, "share_after": share_after, "decide_on": decide, "t_full": t_full, "money_ok": money_ok,
                 "median_gain_entry": float(np.median(SE - S0)), "decision": decision}
    # diversification
    R["div"] = {"now": {"idm": I0}, "entry": {"idm": IE}, "full": {"idm": IF}}
    C = N[ALL].corr(); R["corr"] = {a: {b: float(C.loc[a, b]) for b in ALL} for a in ALL}
    roll = {}
    for n in ALL:
        rest = [m for m in ALL if m != n]; rb = N[rest] @ bk.eq_weights(rest); roll[n] = N[n].rolling(ROLL_DAYS).corr(rb)
    pairs = [N[a].rolling(ROLL_DAYS).corr(N[b]) for i, a in enumerate(ALL) for b in ALL[i + 1:]]
    avgp = pd.concat(pairs, axis=1).mean(axis=1)
    R["roll"] = {n: {"min": float(roll[n].min()), "min_date": str(roll[n].idxmin().date()), "max": float(roll[n].max()),
                     "max_date": str(roll[n].idxmax().date()), "last": float(roll[n].dropna().iloc[-1])} for n in ALL}
    R["avg_pair"] = {"max": float(avgp.max()), "max_date": str(avgp.idxmax().date()), "min": float(avgp.min()), "last": float(avgp.dropna().iloc[-1])}
    rcs = []
    for t_ in N.index[ROLL_DAYS::7]:
        S = N.loc[:t_].iloc[-ROLL_DAYS:][list(WE.index)].cov().to_numpy(); w = WE.to_numpy(); pv = w @ S @ w
        rcs.append(pd.Series(w * (S @ w) / pv, index=WE.index, name=t_))
    RC = pd.DataFrame(rcs)
    R["risk_share"] = {n: {"mean": float(RC[n].mean()), "min": float(RC[n].min()), "max": float(RC[n].max())} for n in ALL}
    # suspect days: a scaled daily return beyond 8 daily standard deviations
    z = N / N.std(); sus = []
    for t_, row in z.iterrows():
        big = row[row.abs() > 8]
        if len(big):
            sus.append({"date": str(t_.date()), "moves": {n: float(nets[n].get(t_, np.nan)) for n in big.index}})
    R["suspect_days"] = sus[:10]
    # markets
    px = market_prices(ci.get("test_start") or R["window"][1])
    reg, mk = {}, {}
    if len(px.columns):
        fac = [f for f in px.columns]
        pm = px.resample("ME").last().pct_change()
        for lab, x in [(n, N[n] * BOOK_VOL / STRAT_VOL) for n in ALL] + [("Current book", B0), ("Book with the candidate", BE)]:
            J = pd.concat([x.resample("ME").sum().rename("y"), pm[fac]], axis=1).dropna()
            if len(J) >= 24:
                b, t, r2 = nw_multi(J["y"].to_numpy(), J[fac].to_numpy())
                reg[lab] = {"alpha": float(b[0] * 12), "alpha_t": float(t[0]), "betas": {f: [float(b[i + 1]), float(t[i + 1])] for i, f in enumerate(fac)},
                            "r2": r2, "months": len(J)}
        wk = pd.concat([BE.resample("W").sum().rename("book"), px.resample("W").last().pct_change()], axis=1).dropna()
        for f in [f for f in ("SPY", "BTC") if f in wk]:
            rc = wk["book"].rolling(ROLL_WEEKS).corr(wk[f]); mk[f] = rc
            R.setdefault("mkt", {})[f] = {"full": float(wk["book"].corr(wk[f])), "max": float(rc.max()), "max_date": str(rc.idxmax().date()),
                                          "min": float(rc.min()), "min_date": str(rc.idxmin().date()), "last": float(rc.dropna().iloc[-1]),
                                          "share_above_03": float((rc.dropna().abs() > 0.3).mean())}
    R["reg"] = reg
    # stress episodes
    eps = []
    for name, a, b in EPISODES:
        if (N.loc[a:b].shape[0]) < 3:
            continue
        e = {"name": name, "a": a, "b": b, "now": float(B0.loc[a:b].sum()), "entry": float(BE.loc[a:b].sum()),
             "cand": float((N[cand] * WE[cand]).loc[a:b].sum())}
        for f in ("SPY", "BTC"):
            s = px[f].loc[a:b].dropna() if f in px else pd.Series(dtype=float)
            e[f] = float(s.iloc[-1] / s.iloc[0] - 1) if len(s) > 1 else None
        eps.append(e)
    R["episodes"] = eps
    R["yearly"] = {str(y): {"now": float(B0[B0.index.year == y].sum()), "entry": float(BE[BE.index.year == y].sum())} for y in sorted(set(N.index.year))}
    # figures
    style(); col = {n: COLS[i % len(COLS)] for i, n in enumerate(members)}; col[cand] = GREEN
    short = {n: n for n in ALL}
    x = BE.index
    fig, ax = plt.subplots(figsize=(7, 2.6)); X = [0] + [r["w"] * 100 for r in curve]; Q = np.vstack([np.zeros(5), [r["q"] for r in curve]])
    ax.fill_between(X, Q[:, 0], Q[:, 4], color=BLUE, alpha=0.12, lw=0, label="Bootstrap 5 to 95%")
    ax.fill_between(X, Q[:, 1], Q[:, 3], color=BLUE, alpha=0.25, lw=0, label="Bootstrap 25 to 75%")
    ax.plot(X, Q[:, 2], color=BLUE, lw=1.3, label="Bootstrap median"); ax.axhline(0, color="#555", lw=0.8, ls=":")
    for c, lab in [(we[cand] * 100, "entry"), (wf[cand] * 100, "full")]:
        ax.axvline(c, color=GREY, lw=0.7, ls="--"); ax.text(c + 0.4, 0.92, lab, fontsize=8, color=GREY, transform=ax.get_xaxis_transform())
    ax.set_xlabel("Risk weight of the candidate (%)"); ax.set_ylabel("Change in book Sharpe")
    ax2 = ax.twinx(); ax2.plot(X[1:], [r["share"] * 100 for r in curve], color=RED, lw=1.1, ls="-.", label="Histories where the book improves (right)")
    ax2.set_ylabel("Book improves (%)", color=RED); ax2.set_ylim(0, 100); ax2.grid(False); ax2.tick_params(axis="y", colors=RED)
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax.legend(h1 + h2, l1 + l2, loc="lower left", fontsize=7.5)
    fig.savefig(out / "fig_weight.pdf"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 2.8)); paths = np.cumsum(BE.to_numpy()[idx], axis=1) * 100; q = np.percentile(paths, [5, 25, 50, 75, 95], axis=0)
    ax.fill_between(x, q[0], q[4], color=BLUE, alpha=0.12, lw=0, label="Bootstrap 5 to 95%")
    ax.fill_between(x, q[1], q[3], color=BLUE, alpha=0.22, lw=0, label="Bootstrap 25 to 75%")
    ax.plot(x, q[2], color=BLUE, lw=0.9, ls="--", label="Bootstrap median"); ax.plot(BE.cumsum() * 100, color=BLUE, lw=1.4, label="With the candidate at entry weight")
    ax.plot(B0.cumsum() * 100, color=GREY, lw=1.1, label="Current book"); ax.axhline(0, color="#999", lw=0.5)
    ax.set_ylabel("Cumulative return (%)"); ax.legend(loc="upper left", fontsize=8); fig.savefig(out / "fig_fan.pdf"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 1.9))
    for s, c, lab in [(B0, GREY, "Current book"), (BE, BLUE, "With the candidate at entry weight")]:
        eq = s.cumsum() * 100; ax.plot(eq - eq.cummax(), color=c, lw=1.0, label=lab)
    eq = BE.cumsum() * 100; ax.fill_between(x, eq - eq.cummax(), 0, color=BLUE, alpha=0.12, lw=0)
    ax.set_ylabel("Drawdown (%)"); ax.legend(loc="lower left", fontsize=8); fig.savefig(out / "fig_dd.pdf"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 2.6)); shaded(ax, avgp > avgp.quantile(0.9))
    for n in ALL:
        ax.plot(roll[n], color=col[n], lw=1.0, label=f"{short[n]} vs the rest")
    ax.plot(avgp, color="k", lw=1.2, ls="--", label="Average pairwise"); ax.axhline(0, color="#999", lw=0.5)
    ax.set_ylabel("6-month correlation"); ax.legend(loc="lower left", fontsize=7.5, ncol=2); fig.savefig(out / "fig_roll.pdf"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 2.4))
    ax.stackplot(RC.index, *[RC[n].clip(lower=0) * 100 for n in ALL], colors=[col[n] for n in ALL], alpha=0.75, labels=[short[n] for n in ALL])
    ax.set_ylabel("Share of risk (%)"); ax.set_ylim(0, 100); ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=min(5, len(ALL)), fontsize=8)
    fig.savefig(out / "fig_risk.pdf"); plt.close(fig)
    if mk:
        fig, ax = plt.subplots(figsize=(7, 2.3)); hi = None
        for f, c in [("SPY", BLUE), ("BTC", BRONZE)]:
            if f in mk:
                ax.plot(mk[f], color=c, lw=1.1, label=f"Correlation to {f}"); h = mk[f].abs() > 0.4; hi = h if hi is None else (hi | h)
        shaded(ax, hi); ax.axhline(0, color="#999", lw=0.5); ax.set_ylim(-0.9, 0.9)
        ax.set_ylabel("26-week correlation"); ax.legend(loc="lower left", fontsize=8); fig.savefig(out / "fig_mkt.pdf"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(4.0, 3.1)); M = C.to_numpy(); im = ax.imshow(M, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(ALL))); ax.set_yticks(range(len(ALL))); ax.set_xticklabels(ALL, fontsize=8, rotation=30, ha="right"); ax.set_yticklabels(ALL, fontsize=8)
    for i in range(len(ALL)):
        for j in range(len(ALL)):
            ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", fontsize=8, color="white" if abs(M[i, j]) > 0.6 else "black")
    ax.grid(False); ax.minorticks_off(); ax.tick_params(which="both", top=False, right=False, bottom=False, left=False)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04); fig.savefig(out / "fig_corr.pdf"); plt.close(fig)
    (out / "numbers.json").write_text(json.dumps(R, indent=1, default=float))
    (out / "numbers.md").write_text(numbers_md(R))
    print(f"wrote {out / 'numbers.md'}")


def pc(v, d=1):
    return "n/a" if v is None else f"{v * 100:.{d}f}%"


def numbers_md(R):
    c = R["candidate"]; r = R["rule"]; L = [f"# Candidate review numbers: {c} in {R['book']}", "",
        f"Common window {R['window'][0]} to {R['window'][1]} ({R['days']} days). Candidate status: {R['status']}"
        + (" (imported returns: paper at most)" if R["imported"] else "") + ".", "", "## Composition (Sharpe net at 15% vol; risk weights before IDM: now / entry / full)"]
    for x in R["comp"]:
        L.append(f"- {x['name']} ({x['family']}): Sharpe {x['sr']:.2f}; weights {pc(x['w0'])} / {pc(x['we'])} / {pc(x['wf'])}; {x['info']}")
    L += ["", "## Weights tried (Sharpe, IDM, share of histories beating the current book, max DD, worst month)"]
    for a in R["alts"]:
        L.append(f"- {a['label']}: {a['sr']:.2f}, IDM {a['idm']:.2f}, beats {pc(a['beats'], 0)}, max DD {pc(a['mdd'])}, worst month {pc(a['worst'])}")
    b = R["curve_best"]; L += ["", f"## Weight curve: best sample Sharpe {b['sr']:.2f} at {pc(b['w'])} of the risk (median gain {b['q'][2]:+.3f}, improves in {pc(b['share'], 0)})"]
    for x in R["curve"]:
        L.append(f"- {pc(x['w'])}: Sharpe {x['sr']:.2f}, median gain {x['q'][2]:+.3f}, 5-95% gain {x['q'][0]:+.2f} to {x['q'][4]:+.2f}, improves {pc(x['share'], 0)}")
    L += ["", "## Performance (sample, 5th to 95th percentile)"]
    for k, lab in [("now", "Current book"), ("entry", "With the candidate at entry weight"), ("full", "At full weight")]:
        p = R["perf"][k]
        L.append(f"- {lab}: " + "; ".join(f"{m} {p['s'][m]:.3f} ({p['lo'][m]:.3f} to {p['hi'][m]:.3f})" for m in p["s"]))
    L += ["", "## Rule",
          f"- Luck haircut {r['haircut']:.2f}; candidate Sharpe after it {r['sr_cand']:.2f}; book {r['sr_book']:.2f}; correlation (gross) {r['corr']:.2f}; threshold {r['thr']:.2f}; passes {r['passes']}",
          f"- Correlation on the book's worst 10% days {r['corr_bad_days']:.2f}; candidate in the book's worst 25% months {pc(r['cand_in_worst_months'], 2)}/month",
          f"- Share improving at entry weight, whole window {pc(r['share_entry'], 0)}; " + (f"after the candidate's train (from {r['since']}) {pc(r['share_after'], 0)}" if r['since'] else "the whole window is after the candidate's train (or too short after it)") + f"; at full weight {pc(r['share_full'], 0)}",
          f"- Median Sharpe gain at entry weight {r['median_gain_entry']:+.3f}; candidate full-sample t {r['t_full']:.2f}; money allowed by its status {r['money_ok']}",
          f"- DECISION (stricter share {pc(r['decide_on'], 0)}): {r['decision']}", "", "## Diversification"]
    for k, v in R["div"].items():
        L.append(f"- {k}: IDM {v['idm']:.2f}")
    names = list(R["corr"])
    for i, a in enumerate(names[:-1]):
        L.append(f"- corr {a}: " + ", ".join(f"{b} {R['corr'][a][b]:+.2f}" for b in names[i + 1:]))
    for n, v in R["roll"].items():
        L.append(f"- 6-month corr of {n} vs the rest: min {v['min']:+.2f} ({v['min_date']}), max {v['max']:+.2f} ({v['max_date']}), last {v['last']:+.2f}")
    a = R["avg_pair"]; L.append(f"- average pairwise 6-month corr: max {a['max']:+.2f} ({a['max_date']}), min {a['min']:+.2f}, last {a['last']:+.2f}")
    for n, v in R["risk_share"].items():
        L.append(f"- risk share {n} (entry weight, 6-month): mean {pc(v['mean'], 0)}, min {pc(v['min'], 0)}, max {pc(v['max'], 0)}")
    L += ["", "## Suspect days (a scaled daily return beyond 8 standard deviations; raw net returns)"]
    L += [f"- {s['date']}: " + ", ".join(f"{k} {pc(v)}" for k, v in s["moves"].items()) for s in R["suspect_days"]] or ["- none"]
    L += ["", "## Markets (monthly regression on all at once; betas with Newey-West t; strategies at 10% vol)"]
    for k, v in R["reg"].items():
        L.append(f"- {k}: alpha {pc(v['alpha'])}/yr (t {v['alpha_t']:.1f}), " + ", ".join(f"{f} {b:+.2f} (t {t:.1f})" for f, (b, t) in v["betas"].items()) + f", R2 {v['r2']:.2f}, {v['months']} months")
    for f, v in (R.get("mkt") or {}).items():
        L.append(f"- book (entry) 26-week corr to {f}: full {v['full']:+.2f}, max {v['max']:+.2f} ({v['max_date']}), min {v['min']:+.2f} ({v['min_date']}), last {v['last']:+.2f}, |corr|>0.3 in {pc(v['share_above_03'], 0)} of weeks")
    L += ["", "## Stress episodes (price change of SPY and BTC; book now; book with the candidate; candidate's contribution)"]
    for e in R["episodes"]:
        L.append(f"- {e['name']} ({e['a']} to {e['b']}): SPY {pc(e['SPY'], 0)}, BTC {pc(e['BTC'], 0)}, now {pc(e['now'])}, with {pc(e['entry'])}, candidate {pc(e['cand'])}")
    L += ["", "## Yearly (now, with the candidate at entry weight)"] + [f"- {y}: {pc(v['now'])}, {pc(v['entry'])}" for y, v in R["yearly"].items()]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ build
def fig(fname, cap, lab, w=r"\textwidth"):
    return (r"\begin{figure}[H]" "\n" rf"\centering\includegraphics[width={w}]{{{fname}}}" "\n"
            rf"\caption{{{cap}}}" "\n" rf"\label{{{lab}}}" "\n" r"\end{figure}")


def build(cand):
    out = WORK / slug(cand); R = json.loads((out / "numbers.json").read_text())
    tf = out / "text.md"
    if not tf.exists():
        raise SystemExit(f"write {tf} first (sections: {', '.join(SECTIONS)})")
    T = {k: tex_escape(v) for k, v in read_text(tf).items()}
    miss = [k for k in SECTIONS if k not in T and not (k == "exposures" and not R["reg"])]
    if miss:
        raise SystemExit(f"text.md misses the sections: {', '.join(miss)}")
    r = R["rule"]; C = R["comp"]
    t_comp = table(r"Strategy & Family & Sharpe & \multicolumn{3}{c}{Risk weight} \\ \cmidrule(l){4-6}" "\n" r" & & & now & entry & full",
                   [[tex_escape(x["name"]) + (" (candidate)" if x["cand"] else ""), tex_escape(x["family"]), ff(x["sr"]),
                     fpc(x["w0"]) if x["w0"] else "", fpc(x["we"]), fpc(x["wf"])] for x in C],
                   r"The book and the candidate. Sharpe: net, each strategy at 15\,\% volatility, common window. Risk weights before the "
                   r"diversification multiplier: now, with the candidate at half its equal-risk weight (entry), and at full weight. "
                   r"Sources: Appendix~\ref{app:src}.", "tab:comp", "llrrrr")
    t_alt = table(r"Book & Sharpe & IDM & Beats now & Max DD & Worst month",
                  [[tex_escape(a["label"]), ff(a["sr"]), ff(a["idm"]), fpc(a["beats"], 0) if a["beats"] is not None else "", fpc(a["mdd"]), fpc(a["worst"])] for a in R["alts"]],
                  r"Weights tried. Beats now: share of 2\,000 bootstrap histories in which the book's Sharpe ratio is above the current book's. "
                  r"All books at the 10\,\% volatility target.", "tab:alt", "lrrrrr")
    rows = [("Annualised return", "ret", 1), ("Annualised volatility", "vol", 1), ("Sharpe ratio", "sr", None), ("Maximum drawdown", "mdd", 1),
            ("Worst month", "worst", 1), (r"Daily CVaR 5\,\%", "cvar", 2), ("Positive months", "pos", 0)]
    fm = lambda v, d: ff(v) if d is None else fpc(v, d)
    P = R["perf"]
    t_perf = table(r" & \multicolumn{2}{c}{Current book} & \multicolumn{2}{c}{With the candidate at entry weight} \\ \cmidrule(lr){2-3}\cmidrule(l){4-5}"
                   "\n" r" & Sample & 90\,\% range & Sample & 90\,\% range",
                   [[l, fm(P["now"]["s"][k], d), fm(P["now"]["lo"][k], d) + " to " + fm(P["now"]["hi"][k], d),
                     fm(P["entry"]["s"][k], d), fm(P["entry"]["lo"][k], d) + " to " + fm(P["entry"]["hi"][k], d)] for l, k, d in rows],
                   rf"Book performance, net, {R['window'][0]} to {R['window'][1]}, at the 10\,\% volatility target. Ranges: 5th to 95th "
                   r"percentile of a stationary block bootstrap (blocks of 20 days, 2\,000 paths).", "tab:perf", "lrrrr")
    t_reg = ""
    if R["reg"]:
        fac = list(next(iter(R["reg"].values()))["betas"])
        cell = lambda bt: (r"\textbf{" + ff(bt[0]) + "}") if abs(bt[1]) >= 2 else ff(bt[0])
        t_reg = table(r" & Alpha & $t$ & " + " & ".join(fac) + r" & $R^2$",
                      [[tex_escape(k), fpc(v["alpha"]), ff(v["alpha_t"], 1)] + [cell(v["betas"][f]) for f in fac] + [ff(v["r2"])] for k, v in R["reg"].items()],
                      r"Monthly net returns regressed on the markets at once: " + ", ".join(lab for s, _, lab in FACTORS if s in fac)
                      + r". Strategies at 10\,\% volatility. Alpha annualised, Newey-West $t$ (3 lags). Betas in bold: $|t|\geq2$.",
                      "tab:reg", "lr" + "r" * (len(fac) + 2), r"\small")
    d = lambda s: date.fromisoformat(s).strftime("%b %Y")
    t_eps = table(r"Episode & Dates & SPY & BTC & Now & With & Candidate",
                  [[tex_escape(e["name"]), d(e["a"]) if d(e["a"]) == d(e["b"]) else d(e["a"]) + "--" + d(e["b"]),
                    fpc(e["SPY"], 0) if e["SPY"] is not None else "", fpc(e["BTC"], 0) if e["BTC"] is not None else "",
                    fpc(e["now"]), fpc(e["entry"]), fpc(e["cand"])] for e in R["episodes"]],
                  r"Stress episodes. SPY and BTC: price change over the episode. Now and With: cumulative return of the current book and "
                  r"of the book with the candidate at entry weight. Candidate: its contribution to the second.", "tab:eps", "llrrrrr", r"\small")
    rule_rows = [[rf"Net Sharpe of the candidate, after the luck haircut ({ff(r['haircut'])})", ff(r["sr_cand"])],
                 ["Net Sharpe of the current book", ff(r["sr_book"])], ["Correlation to the book, before costs", ff(r["corr"])],
                 [r"Correlation on the book's worst 10\,\% of days", ff(r["corr_bad_days"])],
                 [r"Threshold: correlation $\times$ Sharpe of the book", ff(r["thr"])], ["Passes the marginal rule", "yes" if r["passes"] else "no"],
                 ["Book improves in the bootstrap, full weight, whole window", fpc(r["share_full"], 0)],
                 ["Book improves in the bootstrap, entry weight, whole window", fpc(r["share_entry"], 0)]]
    if r["share_after"] is not None:
        rule_rows.append([rf"Book improves in the bootstrap, entry weight, from {r['since']}", fpc(r["share_after"], 0)])
    rule_rows += [["Median gain in Sharpe at entry weight", ff(r["median_gain_entry"])],
                  [r"Full-sample $t$ of the candidate", ff(r["t_full"])], [r"\textbf{Decision}", r"\textbf{" + r["decision"] + "}"]]
    t_rule = table(r" & Value", rule_rows, r"The entry rule, at the entry weight, on the stricter of the two windows: 90\,\% or more of improving "
                   r"histories enters at half weight (if the candidate's full-sample $t$ is 2 or more), 60 to 90\,\% goes on paper, below 60\,\% stays out.",
                   "tab:rule", "lr")
    t_year = table(r" & Current book & With the candidate & Difference",
                   [[y, fpc(v["now"]), fpc(v["entry"]), m_(f"{(v['entry'] - v['now']) * 100:+.1f}") + r"\,\%"] for y, v in R["yearly"].items()],
                   "Book net return by year, the candidate at entry weight.", "tab:year", "lrrr")
    t_src = table(r"Strategy & Source of the returns", [[tex_escape(x["name"]), tex_escape(x["info"])] for x in C]
                  + [["Markets", "SPY, TLT, UUP, GLD adjusted close; BTCUSDT mark price"], ["Sizing and rule", r"lab/book\_report.py, lab/portfolio.py"]],
                  "Sources.", "tab:src", "lp{0.68\\textwidth}", r"\small")
    figs = {"weight": fig("fig_weight.pdf", r"Change in the book's Sharpe ratio as a function of the candidate's risk weight, the other strategies "
                          r"shrinking in proportion: bootstrap median and bands (left axis), and share of the 2\,000 histories in which the book "
                          r"improves (right axis). Dashed lines: entry and full weight.", "fig:weight"),
            "fan": fig("fig_fan.pdf", r"Cumulative return of the book with the candidate at entry weight, with the bands of its bootstrap "
                       r"histories, and the current book. Linear scale.", "fig:fan"),
            "dd": fig("fig_dd.pdf", "Drawdown of the two books.", "fig:dd"),
            "roll": fig("fig_roll.pdf", r"Six-month rolling correlation of each strategy with the rest of the book, and the average pairwise "
                        r"correlation (dashed). Shaded: the 10\,\% of days when the average pairwise correlation was highest.", "fig:roll"),
            "risk": fig("fig_risk.pdf", r"Share of the book's risk carried by each strategy, with the candidate at entry weight, from a "
                        r"six-month rolling covariance.", "fig:risk"),
            "mkt": fig("fig_mkt.pdf", r"26-week rolling correlation of the book with the candidate at entry weight to US equities and to "
                       r"bitcoin, weekly returns. Shaded: periods when either correlation is above 0.4 in absolute value.", "fig:mkt") if R.get("mkt") else "",
            "corr": fig("fig_corr.pdf", "Daily correlation of net returns over the whole window.", "fig:corr", r"0.55\textwidth")}
    sec = lambda title, key, *blocks: rf"\section{{{title}}}" "\n" + T.get(key, "") + "\n\n" + "\n\n".join(b for b in blocks if b) + "\n"
    body = (sec("The book and the candidate", "book", t_comp) + sec("Should the weights change?", "weights", t_alt, figs["weight"])
            + sec("Performance", "performance", t_perf, figs["fan"], figs["dd"]) + sec("Diversification over time", "diversification", figs["roll"], figs["risk"])
            + (sec("Hidden exposures", "exposures", t_reg, figs["mkt"]) if R["reg"] else "")
            + (sec("Stress episodes", "stress", t_eps) if R["episodes"] else "") + sec("Decision", "decision", t_rule)
            + sec("What the book needs", "needs") + sec("Limits", "limits")
            + r"\appendix" "\n" + r"\section{Returns by year}" "\n" + t_year + "\n" + r"\section{Correlation matrix}" "\n" + figs["corr"] + "\n"
            + r"\section{Sources}\label{app:src}" "\n" + t_src + "\n")
    tpl = (ROOT / "lab" / "strategy_report.tex").read_text()
    tpl = tpl.replace(r"Strategy report \quad·\quad Research desk", r"Portfolio manager report \quad·\quad " + tex_escape(R["book"]))
    head = date.fromisoformat(R["date"]).strftime("%-d %B %Y").lstrip("0")
    status = rf"Decision: {r['decision']} \quad·\quad book improves in {fpc(r['decide_on'], 0)} of histories at entry weight"
    tex = (tpl.replace("<<TITLE>>", "Candidate review: " + tex_escape(cand)).replace("<<DATE>>", head).replace("<<STATUS>>", status)
           .replace("<<ABSTRACT>>", T["abstract"]).replace("<<BODY>>", body).replace("<<FOOTER>>", ""))
    (out / "review.tex").write_text(tex)
    compile_tex(out, "review", OUT_PDF / f"{cand} - Candidate review.pdf")


def compile_tex(out, stem, dest):
    engine = shutil.which("pdflatex") or shutil.which("tectonic")
    if not engine:
        raise SystemExit("No LaTeX engine found. Install one: `brew install tectonic` (small) or MacTeX / BasicTeX, then run build again.")
    cmd = [engine, "-interaction=nonstopmode", f"{stem}.tex"] if engine.endswith("pdflatex") else [engine, f"{stem}.tex"]
    for _ in range(2 if engine.endswith("pdflatex") else 1):
        res = subprocess.run(cmd, cwd=out, capture_output=True, text=True)
    pdf = out / f"{stem}.pdf"
    if not pdf.exists():
        print(res.stdout[-3000:]); raise SystemExit(f"LaTeX failed: see {out / (stem + '.log')}")
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy(pdf, dest); print(f"wrote {dest}")

# ================================================================== book construction
# A set of strategies, no book yet: how they do together against each alone, whether each earns its place, and the book
# to propose. Same sizing as the review; same figures where they make sense.
WORK_C = ROOT / "results" / "_book_constructions"
SECTIONS_C = ["abstract", "strategies", "performance", "place", "diversification", "exposures", "stress", "decision", "needs", "limits"]
KEEP_AT, MIN_OOS_DAYS = 0.60, 120


def passed_strategies():
    out = []
    for d in sorted((ROOT / "vault" / "2 Strategies" / "Passed").iterdir()):
        if d.is_dir() and (d / f"{d.name}.md").exists():
            try:
                if (results_dir(d.name) / "TEST_DONE").exists():
                    out.append(d.name)
            except SystemExit:
                pass
    return out


def construct_compute(name, strategies=None, imports=()):
    out = WORK_C / slug(name); out.mkdir(parents=True, exist_ok=True)
    names = list(strategies or []) or ([] if imports else passed_strategies())
    nets, fam, info = {}, {}, {}
    for n in names:
        nets[n], _, ci = desk_series(n); fm = frontmatter(sheet_path(n))
        if not ci["tested"]:
            raise SystemExit(f"{n}: its test is still sealed, so it cannot go into a book yet")
        lk = luck_rows(n, fm.get("family", ""), fm.get("asset", "")).get("family_asset") or {}
        try:
            hc = max(0.0, float(re.findall(r"-?\d+\.?\d*", str(lk.get("luck", "0")))[0]))
        except (IndexError, ValueError):
            hc = 0.0
        fam[n] = fm.get("family", n)
        info[n] = {"family": fam[n], "asset": fm.get("asset", ""), "status": fm.get("status", ""), "haircut": hc, "imported": False,
                   "unseen_from": ci["test_start"], "t_full": nw_t_mean(nets[n].to_numpy()), "source": "runs " + ", ".join(ci["runs"])}
    for n, f, fa in imports:
        nets[n], _, inf = read_runs([f]); fam[n] = fa; names.append(n)
        info[n] = {"family": fa, "asset": "imported", "status": "imported", "haircut": 0.0, "imported": True, "unseen_from": None,
                   "t_full": nw_t_mean(nets[n].to_numpy()), "source": "; ".join(inf)}
    if len(names) < 2:
        raise SystemExit("a book needs at least two strategies")
    N = pd.DataFrame({n: scale(nets[n]) for n in names}).dropna()
    if len(N) < 250:
        raise SystemExit(f"only {len(N)} common days: not enough to build a book")
    bk = Book(N, fam); w = bk.eq_weights(names); BK, W, IDM = bk.run(w)
    rng = np.random.default_rng(SEED); idx = boot_index(len(N), rng); SB = boot_sr(BK, idx)
    alone = {n: N[n] * BOOK_VOL / STRAT_VOL for n in names}
    R = {"name": name, "date": date.today().isoformat(), "window": [str(N.index[0].date()), str(N.index[-1].date())], "days": len(N), "names": names}
    for n in names:
        m = metrics(alone[n]); s = boot_sr(alone[n], idx)
        info[n].update({"sr": m["sr"], "sr_after_luck": m["sr"] - info[n]["haircut"], "vol": m["vol"], "mdd": m["mdd"], "worst": m["worst"],
                        "w": float(w[n]), "book_beats_alone": float((SB > s).mean())})
    R["strats"] = info
    bs = [metrics(pd.Series(BK.to_numpy()[i], index=BK.index)) for i in idx[:1000]]
    R["book"] = {"s": metrics(BK), "lo": {k: float(np.percentile([b[k] for b in bs], 5)) for k in bs[0]},
                 "hi": {k: float(np.percentile([b[k] for b in bs], 95)) for k in bs[0]}, "p_sr_pos": float((SB > 0).mean()),
                 "idm": IDM, "sr_alone_avg": float(np.mean([info[n]["sr"] for n in names]))}
    R["loo"] = {}
    for n in names:
        rest = [m for m in names if m != n]; b, _, i = bk.run(bk.eq_weights(rest)); eq = b.cumsum()
        R["loo"][n] = {"sr": sharpe(b), "idm": i, "drop_hurts": float((SB > boot_sr(b, idx)).mean()) if len(rest) else None,
                       "mdd": float((eq - eq.cummax()).min()), "worst": float(b.resample("ME").sum().min())}
    # out of sample: from the day every strategy is in its sealed test
    starts = [info[n]["unseen_from"] for n in names if info[n]["unseen_from"]]
    R["oos"] = None
    if starts and not any(info[n]["imported"] for n in names):
        o = max(starts); msk = N.index >= o
        if msk.sum() >= MIN_OOS_DAYS:
            R["oos"] = {"from": o, "days": int(msk.sum()), "book": metrics(BK[msk]), "before_sr": sharpe(BK[~msk]) if (~msk).sum() > 60 else None,
                        "alone": {n: sharpe(alone[n][msk]) for n in names}}
    # the proposal
    keep = [n for n in names if (R["loo"][n]["drop_hurts"] or 0) >= KEEP_AT]
    for n in names:
        s = info[n]
        s["earns_place"] = n in keep
        s["money_ok"] = (not s["imported"]) and s["status"] == "passed" and s["t_full"] >= 2 and s["sr_after_luck"] > 0
        s["proposed"] = ("in the book, money allowed" if s["money_ok"] else "in the book, paper") if n in keep else "out, in the library"
    prop = {"members": keep}
    if len(keep) >= 2:
        b, _, i = bk.run(bk.eq_weights(keep)); m = metrics(b); sp = boot_sr(b, idx)
        prop.update({"sr": m["sr"], "vol": m["vol"], "mdd": m["mdd"], "worst": m["worst"], "idm": i,
                     "beats_all": float((sp > SB).mean()) if len(keep) < len(names) else None,
                     "status": "money" if all(info[n]["money_ok"] for n in keep) else "paper"})
        prop["decision"] = (f"{' and '.join(keep)}, " + ("money allowed" if prop["status"] == "money" else "on paper"))
    else:
        prop["decision"] = "no book: fewer than two strategies earn their place"
    R["proposal"] = prop
    # diversification
    C = N.corr(); R["corr"] = {a: {b_: float(C.loc[a, b_]) for b_ in names} for a in names}
    roll = {}
    for n in names:
        rest = [m for m in names if m != n]; roll[n] = N[n].rolling(ROLL_DAYS).corr(N[rest] @ bk.eq_weights(rest))
    avgp = pd.concat([N[a].rolling(ROLL_DAYS).corr(N[b_]) for i, a in enumerate(names) for b_ in names[i + 1:]], axis=1).mean(axis=1)
    R["roll"] = {n: {"min": float(roll[n].min()), "min_date": str(roll[n].idxmin().date()), "max": float(roll[n].max()),
                     "max_date": str(roll[n].idxmax().date()), "last": float(roll[n].dropna().iloc[-1])} for n in names}
    R["avg_pair"] = {"max": float(avgp.max()), "max_date": str(avgp.idxmax().date()), "min": float(avgp.min()), "last": float(avgp.dropna().iloc[-1])}
    rcs = []
    for t_ in N.index[ROLL_DAYS::7]:
        S = N.loc[:t_].iloc[-ROLL_DAYS:][names].cov().to_numpy(); v = W[names].to_numpy(); pv = v @ S @ v
        rcs.append(pd.Series(v * (S @ v) / pv, index=names, name=t_))
    RC = pd.DataFrame(rcs)
    R["risk_share"] = {n: {"mean": float(RC[n].mean()), "min": float(RC[n].min()), "max": float(RC[n].max())} for n in names}
    R["return_share"] = {n: float((N[n] * W[n]).sum() / BK.sum()) for n in names}
    z = N / N.std()
    R["suspect_days"] = [{"date": str(t_.date()), "moves": {k: float(nets[k].get(t_, np.nan)) for k in row[row.abs() > 8].index}}
                         for t_, row in z.iterrows() if (row.abs() > 8).any()][:10]
    # markets
    px = market_prices(R["window"][1]); R["reg"], mk = {}, {}
    if len(px.columns):
        fac = list(px.columns); pm = px.resample("ME").last().pct_change()
        for lab, x in [(n, alone[n]) for n in names] + [("Book", BK)]:
            J = pd.concat([x.resample("ME").sum().rename("y"), pm[fac]], axis=1).dropna()
            if len(J) >= 24:
                b, t, r2 = nw_multi(J["y"].to_numpy(), J[fac].to_numpy())
                R["reg"][lab] = {"alpha": float(b[0] * 12), "alpha_t": float(t[0]), "betas": {f: [float(b[i + 1]), float(t[i + 1])] for i, f in enumerate(fac)},
                                 "r2": r2, "months": len(J)}
        wk = pd.concat([BK.resample("W").sum().rename("book"), px.resample("W").last().pct_change()], axis=1).dropna()
        for f in [f for f in ("SPY", "BTC") if f in wk]:
            rc = wk["book"].rolling(ROLL_WEEKS).corr(wk[f]); mk[f] = rc
            R.setdefault("mkt", {})[f] = {"full": float(wk["book"].corr(wk[f])), "max": float(rc.max()), "max_date": str(rc.idxmax().date()),
                                          "min": float(rc.min()), "min_date": str(rc.idxmin().date()), "last": float(rc.dropna().iloc[-1]),
                                          "share_above_03": float((rc.dropna().abs() > 0.3).mean())}
    R["episodes"] = []
    for en, a, b in EPISODES:
        if N.loc[a:b].shape[0] < 3:
            continue
        e = {"name": en, "a": a, "b": b, "book": float(BK.loc[a:b].sum()), "contrib": {n: float((N[n] * W[n]).loc[a:b].sum()) for n in names}}
        for f in ("SPY", "BTC"):
            s = px[f].loc[a:b].dropna() if f in px else pd.Series(dtype=float)
            e[f] = float(s.iloc[-1] / s.iloc[0] - 1) if len(s) > 1 else None
        R["episodes"].append(e)
    R["yearly"] = {str(y): {"book": float(BK[BK.index.year == y].sum()), **{n: float(alone[n][alone[n].index.year == y].sum()) for n in names}}
                   for y in sorted(set(N.index.year))}
    # figures
    style(); col = {n: [BRONZE, GREEN, STEEL, RED, PURPLE, GREY][i % 6] for i, n in enumerate(names)}; x = BK.index
    fig_, ax = plt.subplots(figsize=(7, 2.8)); q = np.percentile(np.cumsum(BK.to_numpy()[idx], axis=1) * 100, [5, 25, 75, 95], axis=0)
    ax.fill_between(x, q[0], q[3], color=BLUE, alpha=0.12, lw=0, label="Bootstrap 5 to 95%"); ax.fill_between(x, q[1], q[2], color=BLUE, alpha=0.22, lw=0, label="Bootstrap 25 to 75%")
    ax.plot(BK.cumsum() * 100, color=BLUE, lw=1.6, label="Book")
    for n in names:
        ax.plot(alone[n].cumsum() * 100, color=col[n], lw=0.9, label=f"{n} alone")
    if R["oos"]:
        ax.axvline(pd.Timestamp(R["oos"]["from"]), color="#555", lw=0.6, ls=":")
        ax.text(pd.Timestamp(R["oos"]["from"]), 1.02, "all out of sample", transform=ax.get_xaxis_transform(), fontsize=8, color="#444")
    ax.axhline(0, color="#999", lw=0.5); ax.set_ylabel("Cumulative return (%)"); ax.legend(loc="upper left", fontsize=7.5, ncol=2)
    fig_.savefig(out / "fig_book.pdf"); plt.close(fig_)
    fig_, ax = plt.subplots(figsize=(7, 2.1))
    for n in names:
        ax.hist(boot_sr(alone[n], idx), bins=60, color=col[n], alpha=0.25, density=True)
        ax.hist(boot_sr(alone[n], idx), bins=60, color=col[n], histtype="step", density=True, label=f"{n} alone")
    ax.hist(SB, bins=60, color=BLUE, alpha=0.3, density=True); ax.hist(SB, bins=60, color=BLUE, histtype="step", lw=1.4, density=True, label="Book")
    ax.axvline(0, color="#555", lw=0.8, ls=":"); ax.set_xlabel("Sharpe ratio across 2,000 bootstrap histories"); ax.set_yticks([])
    ax.grid(axis="y", visible=False); ax.legend(loc="upper right", fontsize=7.5); fig_.savefig(out / "fig_dist.pdf"); plt.close(fig_)
    fig_, ax = plt.subplots(figsize=(7, 2.0))
    for n in names:
        e = alone[n].cumsum() * 100; ax.plot(e - e.cummax(), color=col[n], lw=0.8, label=f"{n} alone")
    e = BK.cumsum() * 100; ax.fill_between(x, e - e.cummax(), 0, color=BLUE, alpha=0.18, lw=0); ax.plot(e - e.cummax(), color=BLUE, lw=1.3, label="Book")
    ax.set_ylabel("Drawdown (%)"); ax.legend(loc="lower left", fontsize=7, ncol=2); fig_.savefig(out / "fig_dd.pdf"); plt.close(fig_)
    fig_, ax = plt.subplots(figsize=(7, 2.5)); shaded(ax, avgp > avgp.quantile(0.9))
    for n in names:
        ax.plot(roll[n], color=col[n], lw=1.0, label=f"{n} vs the rest")
    ax.plot(avgp, color="k", lw=1.2, ls="--", label="Average pairwise"); ax.axhline(0, color="#999", lw=0.5)
    ax.set_ylabel("6-month correlation"); ax.legend(loc="lower left", fontsize=7, ncol=2); fig_.savefig(out / "fig_roll.pdf"); plt.close(fig_)
    fig_, ax = plt.subplots(figsize=(7, 2.3))
    ax.stackplot(RC.index, *[RC[n].clip(lower=0) * 100 for n in names], colors=[col[n] for n in names], alpha=0.75, labels=names)
    ax.set_ylabel("Share of risk (%)"); ax.set_ylim(0, 100); ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=min(4, len(names)), fontsize=7.5)
    fig_.savefig(out / "fig_risk.pdf"); plt.close(fig_)
    if mk:
        fig_, ax = plt.subplots(figsize=(7, 2.3)); hi = None
        for f, c in [("SPY", BLUE), ("BTC", BRONZE)]:
            if f in mk:
                ax.plot(mk[f], color=c, lw=1.1, label=f"Correlation to {f}"); h = mk[f].abs() > 0.4; hi = h if hi is None else (hi | h)
        shaded(ax, hi); ax.axhline(0, color="#999", lw=0.5); ax.set_ylim(-0.95, 0.95); ax.set_ylabel("26-week correlation")
        ax.legend(loc="lower left", fontsize=8); fig_.savefig(out / "fig_mkt.pdf"); plt.close(fig_)
    k = len(names); fig_, ax = plt.subplots(figsize=(3.4 + 0.3 * k, 2.6 + 0.3 * k)); M = C.to_numpy(); im = ax.imshow(M, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(k)); ax.set_yticks(range(k)); ax.set_xticklabels(names, fontsize=7.5, rotation=30, ha="right"); ax.set_yticklabels(names, fontsize=7.5)
    for i in range(k):
        for j in range(k):
            ax.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", fontsize=8, color="white" if abs(M[i, j]) > 0.6 else "black")
    ax.grid(False); ax.minorticks_off(); ax.tick_params(which="both", top=False, right=False, bottom=False, left=False)
    fig_.colorbar(im, ax=ax, fraction=0.046, pad=0.04); fig_.savefig(out / "fig_corr.pdf"); plt.close(fig_)
    (out / "numbers.json").write_text(json.dumps(R, indent=1, default=float))
    (out / "numbers.md").write_text(construct_md(R))
    print(f"wrote {out / 'numbers.md'}")


def construct_md(R):
    S, B = R["strats"], R["book"]
    L = [f"# Book construction numbers: {R['name']}", "", f"Common window {R['window'][0]} to {R['window'][1]} ({R['days']} days). "
         "Each strategy alone at 10% vol; the book: equal risk by family, IDM, 10% target.", "", "## Strategies alone"]
    for n, s in S.items():
        L.append(f"- {n} ({s['family']}, {s['asset']}, {s['status']}): Sharpe {s['sr']:.2f}, after luck ({s['haircut']:.2f}) {s['sr_after_luck']:.2f}, "
                 f"full-sample t {s['t_full']:.2f}, vol {pc(s['vol'])}, max DD {pc(s['mdd'])}, worst month {pc(s['worst'])}, "
                 f"risk weight {pc(s['w'])}, unseen from {s['unseen_from'] or 'n/a (imported)'}; book beats it alone in {pc(s['book_beats_alone'], 0)}")
    L += ["", "## Book (sample, 5th to 95th percentile)"] + [f"- {k}: {B['s'][k]:.3f} ({B['lo'][k]:.3f} to {B['hi'][k]:.3f})" for k in B["s"]]
    L += [f"- Sharpe above zero in {pc(B['p_sr_pos'], 1)} of histories; average Sharpe of the strategies alone {B['sr_alone_avg']:.2f}; IDM {B['idm']:.2f}"]
    o = R["oos"]
    L += ["", "## Out of sample (every strategy in its sealed test)"]
    if o:
        L.append(f"- from {o['from']} ({o['days']} days): book Sharpe {o['book']['sr']:.2f}, max DD {pc(o['book']['mdd'])}; before that {o['before_sr']:.2f}" if o["before_sr"] is not None
                 else f"- from {o['from']} ({o['days']} days): book Sharpe {o['book']['sr']:.2f}, max DD {pc(o['book']['mdd'])}")
        L.append("- alone: " + ", ".join(f"{n} {v:.2f}" for n, v in o["alone"].items()))
    else:
        L.append("- not measured (imported returns, or fewer than 120 days with every strategy unseen)")
    L += ["", "## Leave one out (book without each strategy)"]
    for n, l in R["loo"].items():
        L.append(f"- without {n}: Sharpe {l['sr']:.2f}, IDM {l['idm']:.2f}, max DD {pc(l['mdd'])}, worst month {pc(l['worst'])}; dropping it hurts in {pc(l['drop_hurts'], 0)} of histories")
    p = R["proposal"]
    L += ["", f"## Proposal (a strategy earns its place if dropping it hurts in {pc(KEEP_AT, 0)} or more; money needs status passed, t >= 2, Sharpe after luck > 0)"]
    L += [f"- {n}: {s['proposed']}" for n, s in S.items()]
    if len(p["members"]) >= 2:
        L.append(f"- proposed book ({', '.join(p['members'])}): Sharpe {p['sr']:.2f}, vol {pc(p['vol'])}, max DD {pc(p['mdd'])}, worst month {pc(p['worst'])}, IDM {p['idm']:.2f}" + (f", beats the book of all strategies in {pc(p['beats_all'], 0)} of histories" if p["beats_all"] is not None else ""))
    L.append(f"- DECISION: {p['decision']}")
    L += ["", "## Diversification"]
    names = R["names"]
    for i, a in enumerate(names[:-1]):
        L.append(f"- corr {a}: " + ", ".join(f"{b} {R['corr'][a][b]:+.2f}" for b in names[i + 1:]))
    for n, v in R["roll"].items():
        L.append(f"- 6-month corr of {n} vs the rest: min {v['min']:+.2f} ({v['min_date']}), max {v['max']:+.2f} ({v['max_date']}), last {v['last']:+.2f}")
    a = R["avg_pair"]; L.append(f"- average pairwise 6-month corr: max {a['max']:+.2f} ({a['max_date']}), min {a['min']:+.2f}, last {a['last']:+.2f}")
    for n in names:
        v = R["risk_share"][n]; L.append(f"- {n}: risk share mean {pc(v['mean'], 0)} (min {pc(v['min'], 0)}, max {pc(v['max'], 0)}), return share {pc(R['return_share'][n], 0)}")
    L += ["", "## Suspect days (a scaled daily return beyond 8 standard deviations; raw net returns)"]
    L += [f"- {s['date']}: " + ", ".join(f"{k} {pc(v)}" for k, v in s["moves"].items()) for s in R["suspect_days"]] or ["- none"]
    L += ["", "## Markets (monthly regression on all at once; Newey-West t; at 10% vol)"]
    for k, v in R["reg"].items():
        L.append(f"- {k}: alpha {pc(v['alpha'])}/yr (t {v['alpha_t']:.1f}), " + ", ".join(f"{f} {b:+.2f} (t {t:.1f})" for f, (b, t) in v["betas"].items())
                 + f", R2 {v['r2']:.2f}, {v['months']} months")
    for f, v in (R.get("mkt") or {}).items():
        L.append(f"- book 26-week corr to {f}: full {v['full']:+.2f}, max {v['max']:+.2f} ({v['max_date']}), min {v['min']:+.2f} ({v['min_date']}), "
                 f"last {v['last']:+.2f}, |corr|>0.3 in {pc(v['share_above_03'], 0)} of weeks")
    L += ["", "## Stress episodes (SPY and BTC price change; book; each strategy's contribution)"]
    for e in R["episodes"]:
        L.append(f"- {e['name']} ({e['a']} to {e['b']}): SPY {pc(e['SPY'], 0)}, BTC {pc(e['BTC'], 0)}, book {pc(e['book'])}; "
                 + ", ".join(f"{n} {pc(v)}" for n, v in e["contrib"].items()))
    L += ["", "## Yearly (book, then each alone at 10% vol)"] + [f"- {y}: " + ", ".join(f"{k} {pc(v)}" for k, v in d.items()) for y, d in R["yearly"].items()]
    return "\n".join(L) + "\n"


def construct_build(name):
    out = WORK_C / slug(name); R = json.loads((out / "numbers.json").read_text()); tf = out / "text.md"
    if not tf.exists():
        raise SystemExit(f"write {tf} first (sections: {', '.join(SECTIONS_C)})")
    T = {k: tex_escape(v) for k, v in read_text(tf).items()}
    miss = [k for k in SECTIONS_C if k not in T and not (k == "exposures" and not R["reg"])]
    if miss:
        raise SystemExit(f"text.md misses the sections: {', '.join(miss)}")
    S, B, names, P = R["strats"], R["book"], R["names"], R["proposal"]
    nm = lambda n: tex_escape(n)
    hd = lambda n: r"\parbox[b]{1.6cm}{\raggedleft\strut " + tex_escape(n) + "}"      # long names wrap in column headers
    t_str = table(r"Strategy & Family & Sharpe & After luck & $t$ & Max DD & Worst month & Unseen from",
                  [[nm(n), tex_escape(s["family"]), ff(s["sr"]), ff(s["sr_after_luck"]), ff(s["t_full"]), fpc(s["mdd"]), fpc(s["worst"]),
                    date.fromisoformat(s["unseen_from"]).strftime("%b %Y") if s["unseen_from"] else "imported"] for n, s in S.items()],
                  r"The strategies, each alone at 10\,\% volatility on the common window, net. After luck: minus the luck line of its family and "
                  r"asset (Trials summary). $t$: Newey-West, the strategy's full sample. Unseen from: start of its sealed test. In the book each "
                  r"family takes an equal share of the risk.", "tab:str", "llrrrrrr", r"\footnotesize\setlength{\tabcolsep}{3pt}")
    rows = [("Annualised return", "ret", 1), ("Annualised volatility", "vol", 1), ("Sharpe ratio", "sr", None), ("Maximum drawdown", "mdd", 1),
            ("Worst month", "worst", 1), (r"Daily CVaR 5\,\%", "cvar", 2), ("Positive months", "pos", 0)]
    fmt = lambda v, d: ff(v) if d is None else fpc(v, d)
    t_perf = table(r" & Sample & 90\,\% range", [[l, fmt(B["s"][k], d), fmt(B["lo"][k], d) + " to " + fmt(B["hi"][k], d)] for l, k, d in rows],
                   rf"The book, net, {R['window'][0]} to {R['window'][1]}, at its 10\,\% target (IDM {ff(B['idm'])}). Range: 5th to 95th percentile "
                   r"of a stationary block bootstrap (blocks of 20 days, 2\,000 paths).", "tab:perf", "lrr")
    t_oos = ""
    if R["oos"]:
        o = R["oos"]
        t_oos = table(r" & Book & " + " & ".join(hd(n) for n in names),
                      [["Sharpe, every strategy unseen", ff(o["book"]["sr"])] + [ff(o["alone"][n]) for n in names]],
                      rf"Out of sample: from {o['from']}, when every strategy is in its sealed test ({o['days']} days).", "tab:oos", "l" + "r" * (len(names) + 1), r"\small")
    loo = [["All strategies", ff(B["s"]["sr"]), ff(B["idm"]), "", fpc(B["s"]["mdd"]), fpc(B["s"]["worst"]), ""]]
    loo += [["Without " + nm(n), ff(l["sr"]), ff(l["idm"]), fpc(l["drop_hurts"], 0), fpc(l["mdd"]), fpc(l["worst"]), fpc(S[n]["book_beats_alone"], 0)] for n, l in R["loo"].items()]
    t_loo = table(r"Book & Sharpe & IDM & Drop hurts & Max DD & Worst month & Beats alone", loo,
                  r"Does each strategy earn its place? Drop hurts: share of bootstrap histories in which the book of all strategies has a higher "
                  r"Sharpe ratio than the book without that one. Beats alone: share in which the book's Sharpe ratio is above that strategy's alone.",
                  "tab:loo", "lrrrrrr", r"\footnotesize\setlength{\tabcolsep}{3pt}")
    t_reg = ""
    if R["reg"]:
        fac = list(next(iter(R["reg"].values()))["betas"])
        cell = lambda bt: (r"\textbf{" + ff(bt[0]) + "}") if abs(bt[1]) >= 2 else ff(bt[0])
        t_reg = table(r" & Alpha & $t$ & " + " & ".join(fac) + r" & $R^2$",
                      [[nm(k), fpc(v["alpha"]), ff(v["alpha_t"], 1)] + [cell(v["betas"][f]) for f in fac] + [ff(v["r2"])] for k, v in R["reg"].items()],
                      r"Monthly net returns regressed on the markets at once: " + ", ".join(lab for s, _, lab in FACTORS if s in fac)
                      + r". At 10\,\% volatility. Alpha annualised, Newey-West $t$ (3 lags). Betas in bold: $|t|\geq2$.", "tab:reg", "lr" + "r" * (len(fac) + 2), r"\small")
    d = lambda s: date.fromisoformat(s).strftime("%b %y")
    wide = len(names) <= 4
    hdr = r"Episode & Dates & SPY & BTC & Book & " + (" & ".join(hd(n) for n in names) if wide else "Best & Worst")
    eps = []
    for e in R["episodes"]:
        c = e["contrib"]
        tail = [fpc(c[n]) for n in names] if wide else [nm(max(c, key=c.get)), nm(min(c, key=c.get))]
        eps.append([tex_escape(e["name"]), d(e["a"]) if d(e["a"]) == d(e["b"]) else d(e["a"]) + "--" + d(e["b"]),
                    fpc(e["SPY"], 0) if e["SPY"] is not None else "", fpc(e["BTC"], 0) if e["BTC"] is not None else "", fpc(e["book"])] + tail)
    t_eps = table(hdr, eps, r"Stress episodes. SPY and BTC: price change over the episode. Book: its cumulative return; then "
                  + (r"each strategy's contribution to it." if wide else r"the strategies that contributed most and least."), "tab:eps",
                  "llrrr" + ("r" * len(names) if wide else "ll"), r"\footnotesize\setlength{\tabcolsep}{2pt}")
    dec = [[nm(n), fpc(R["loo"][n]["drop_hurts"], 0), ff(s["sr_after_luck"]), ff(s["t_full"]), s["proposed"]] for n, s in S.items()]
    if len(P["members"]) >= 2:
        dec.append([r"\textbf{Proposed book}", r"\multicolumn{4}{r}{\textbf{" + rf"Sharpe {ff(P['sr'])}, max DD {fpc(P['mdd'])}, {P['status']}" + "}}"])
    t_dec = table(r"Strategy & Drop hurts & After luck & $t$ & Proposed", dec,
                  rf"The proposal. A strategy earns its place if dropping it hurts the book in {fpc(KEEP_AT, 0)} of histories or more; it can carry money "
                  r"with status passed, a full-sample $t$ of 2 or more and a Sharpe ratio after luck above zero. The book carries money only if all its members can.",
                  "tab:dec", "lrrrl")
    t_year = table(r" & Book & " + (" & ".join(hd(n) for n in names) if len(names) <= 5 else "Best alone & Worst alone"),
                   [[y, fpc(v["book"])] + ([fpc(v[n]) for n in names] if len(names) <= 5 else
                                            [fpc(max(v[n] for n in names)), fpc(min(v[n] for n in names))]) for y, v in R["yearly"].items()],
                   r"Net return by year, the book and each strategy alone at 10\,\% volatility.", "tab:year", "l" + "r" * (len(names) + 1 if len(names) <= 5 else 3), r"\small")
    t_src = table(r"Strategy & Source of the returns", [[nm(n), tex_escape(s["source"])] for n, s in S.items()]
                  + [["Markets", "SPY, TLT, UUP, GLD adjusted close; BTCUSDT mark price"], ["Sizing", r"lab/book\_report.py (construct)"]],
                  "Sources.", "tab:src", "lp{0.68\\textwidth}", r"\small")
    F = {"book": fig("fig_book.pdf", r"Cumulative net return of the book and of each strategy alone, all at 10\,\% volatility, with the bands of the "
                     r"book's bootstrap histories" + (r". Dotted line: from here every strategy is in its sealed test" if R["oos"] else "") + ". Linear scale.", "fig:book"),
         "dist": fig("fig_dist.pdf", r"Sharpe ratio of the book and of each strategy alone across 2\,000 bootstrap histories.", "fig:dist"),
         "dd": fig("fig_dd.pdf", "Drawdown of the book (shaded) and of each strategy alone.", "fig:dd"),
         "roll": fig("fig_roll.pdf", r"Six-month rolling correlation of each strategy with the rest of the book, and the average pairwise correlation "
                     r"(dashed). Shaded: the 10\,\% of days when the average was highest.", "fig:roll"),
         "risk": fig("fig_risk.pdf", "Share of the book's risk carried by each strategy, six-month rolling covariance.", "fig:risk"),
         "mkt": fig("fig_mkt.pdf", r"26-week rolling correlation of the book to US equities and to bitcoin, weekly returns. Shaded: either correlation "
                    r"above 0.4 in absolute value.", "fig:mkt") if R.get("mkt") else "",
         "corr": fig("fig_corr.pdf", "Daily correlation of net returns over the whole window.", "fig:corr", r"0.55\textwidth")}
    sec = lambda title, key, *blocks: rf"\section{{{title}}}" "\n" + T.get(key, "") + "\n\n" + "\n\n".join(b for b in blocks if b) + "\n"
    body = (sec("The strategies", "strategies", t_str) + sec("The book against its strategies", "performance", t_perf, F["book"], F["dist"], F["dd"], t_oos)
            + sec("Does each strategy earn its place?", "place", t_loo) + sec("Diversification over time", "diversification", F["roll"], F["risk"])
            + (sec("Hidden exposures", "exposures", t_reg, F["mkt"]) if R["reg"] else "")
            + (sec("Stress episodes", "stress", t_eps) if R["episodes"] else "") + sec("Proposed book", "decision", t_dec)
            + sec("What the book needs", "needs") + sec("Limits", "limits")
            + r"\appendix" "\n" r"\section{Returns by year}" "\n" + t_year + "\n" r"\section{Correlation matrix}" "\n" + F["corr"] + "\n"
            + r"\section{Sources}\label{app:src}" "\n" + t_src + "\n")
    tpl = (ROOT / "lab" / "strategy_report.tex").read_text().replace(r"Strategy report \quad·\quad Research desk", r"Portfolio manager report \quad·\quad Book construction")
    tex = (tpl.replace("<<TITLE>>", "Book construction: " + tex_escape(R["name"]))
           .replace("<<DATE>>", date.fromisoformat(R["date"]).strftime("%-d %B %Y"))
           .replace("<<STATUS>>", "Proposed: " + tex_escape(P["decision"])).replace("<<ABSTRACT>>", T["abstract"]).replace("<<BODY>>", body).replace("<<FOOTER>>", ""))
    (out / "construction.tex").write_text(tex)
    compile_tex(out, "construction", OUT_PDF / f"{R['name']} - Book construction.pdf")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="The PM's reports: review (a candidate against the book) or construct (a book from a set of strategies).")
    ap.add_argument("kind", choices=["review", "construct"])
    ap.add_argument("name", help="review: the candidate; construct: the name of the book to build")
    ap.add_argument("step", choices=["compute", "build"])
    ap.add_argument("--returns", help="review: returns file of a candidate made outside the desk (date, net[, gross])")
    ap.add_argument("--family", help="review: family of that candidate")
    ap.add_argument("--book", default=str(BOOK_FILE), help="review: the book file")
    ap.add_argument("--strategy", action="append", default=[], help="construct: a desk strategy to include (repeat); default: every passed strategy with an opened test")
    ap.add_argument("--import", dest="imports", nargs=3, action="append", default=[], metavar=("NAME", "FILE", "FAMILY"),
                    help="construct: a strategy made outside the desk, from its returns file (paper at most)")
    a = ap.parse_args()
    if a.kind == "review":
        compute(a.name, a.returns, a.family, Path(a.book)) if a.step == "compute" else build(a.name)
    else:
        construct_compute(a.name, a.strategy, a.imports) if a.step == "compute" else construct_build(a.name)
