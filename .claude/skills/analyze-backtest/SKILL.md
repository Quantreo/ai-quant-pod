---
name: analyze-backtest
description: Act as the desk's Analyst: read the saved runs of a built strategy against the rules its Pass 1 wrote before any result (kill criteria, predictions, luck line, controls) and give a verdict, kill or candidate for the test; after the test, apply the three-zone rule and say keep or kill. Use whenever the user asks to analyse, read, judge or diagnose a backtest, the results of a strategy, or the result of its test.
---

# Analyse a backtest

1. Read in the strategy folder: `Pass 1.md` (1.1 predictions, 1.6 luck line, 1.10 diagnostics, 1.11 kill criteria), `Build.md` (runs, gate), `Changelog.md`; `Data check.md` only for its instructions. The tries are the strategy's lines in `vault/3 Research Log/_desk/Research Log.md` (`grep`, not the whole file).
2. Read `reference/rules.md`.
3. For each run the Build lists, run `scripts/run_report.py`, all runs of one comparison in one call (the base with its delay control, its survivorship control, its variants). Check that all the runs share the same `lab_sha`.
4. Compute what 1.10 asks and the scripts do not give: the factors of a regression, built point in time from `lab.data.load`, saved in `results/<strategy>/analysis/`, then `scripts/regress.py`. Never change the strategy file, never run a new backtest: a missing run is a request to the Developer.
5. Count: add every run you read to the desk's trial file with `poetry run python lab/trials.py add <run> --sheet <sheet> --counts yes|no --why "<base, variant, change decided on a result | stress test | control>"`, then `poetry run python lab/trials.py report`. Use its luck line (by family and for the desk) next to the strategy's own.
6. Go through 1.11 criterion by criterion: the number, the threshold, pass or fail. Then each prediction: confirmed, not confirmed, or not measurable, with its number; a prediction said to separate the mechanism from its rival weighs more than one read only. Then luck: tries counted, luck line with `.claude/skills/pass-one/scripts/budget.py`, Sharpe minus the luck line. Then the controls (one-day delay, survivorship) and what they say.
7. Write the human report: `poetry run python lab/report.py "<Strategy>" <main run> <compared runs...>`, the main run first (the base on train plus validation), then validation, the delay control, the survivorship control and the variants. It writes a page with its charts next to the sheet; link it from Pass 2.
8. Verdict, by the rules of `reference/rules.md`: **kill**, **candidate for the test**, or **inconclusive** (a criterion cannot be computed: say what is missing). Write what the result is, not what you hoped. Then one to three **lessons** for `vault/3 Research Log/Lessons.md`, in its line format: what this result teaches beyond this strategy (a market fact, a design trap, a data trap, a method point). "The strategy failed" is not a lesson; "in G10 FX on 2010 to 2023, spot gave back 99% of the carry: UIP held" is.
9. Write `Pass 2.md` in the strategy folder from `assets/pass-two.md`, its Research Log lines, and your row in the index. Reply in at most 6 lines: the verdict, the worst number, the lessons.
10. After the test (a run with period "test" and the lock `results/<strategy>/TEST_DONE`): the same read on the test run, then the three-zone rule of 1.11, and the verdict **passed** (zone "confirms" or "ambiguous"; label it with the zone, the full-sample t, money possible at t 2 or more, otherwise paper only, and the labels of Pass 2) or **killed** (zone "contradicts", or a kill of the Kill Policy). Passed: move the folder to `vault/2 Strategies/Passed/`, `status: passed`. Killed: to `Killed/`. Ambiguous strategies stay in Passed: alone they may be weak, in a book they may help. Every mean and Sharpe in a zone rule is net of fees. Written in `Test.md`, with its index row.

## Rules

- Pass 1 decides, you apply. A threshold is never moved, a criterion is never reinterpreted after the result. If a rule is ambiguous, say so, do not kill on it, and write the question for the user. Kill only on evidence against (`vault/Toolbox/Kill Policy.md`); a criterion that would kill on absence of evidence is read as a label.
- A good Sharpe is not an argument. A prediction that fails, a control that collapses, a P&L made by another mechanism than the one written: each is written in plain words, at the top.
- Never open the test period before the lock exists.
- Write in English. Never use a long dash. Backtest charts, if any: cumulative return in %, linear scale.
