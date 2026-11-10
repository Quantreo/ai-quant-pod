# Pipeline

The lane: the cheap test comes first, the review machinery only for what survives it. The user comes in twice: the theme at the start, one approval of the tests near the end.

| # | Step | Agent (model) | Skill | Reads | Writes |
| --- | --- | --- | --- | --- | --- |
| 1 | Ideas | ideator (sonnet) | ideation | library index, 2 or 3 notes, journal headings | entries in the Idea Journal |
| 2 | Judge | economist (opus), one call per batch | pass-one | the journal entries, the notes they cite, method | folder: `<Name>.md`, short `Pass 1.md` (500 words), `Changelog.md`; journal status |
| 3 | Data | data (sonnet) | data-check | `Pass 1.md`, data cards | `Data check.md` |
| 4 | Gate | developer (sonnet), phase gate, one call per batch, one run per idea | build-strategy | `Pass 1.md`, `Data check.md` | `strategies/`, `results/`, `Build.md` (with its **Assumptions**) |
| 4b | Complete | economist (resumed) | pass-one, step 8 | `Pass 1.md`, the gate and the assumptions in `Build.md` | full `Pass 1.md` (1500 words), changelog row |
| 5 | Review | critic (sonnet), only after a passed gate and the completion | pass-one-review | `Pass 1.md` (never `Build.md`) | `Review.md` |
| 6 | Revise | economist (resumed with SendMessage) | revise-strategy | `Review.md`, `Pass 1.md` | `Pass 1.md` in place, answers in `Review.md`, `Changelog.md` |
| 7 | Validation | developer (resumed), phase validation | build-strategy | `Pass 1.md`, `Data check.md`, `Build.md` | runs, `Build.md` |
| 8 | Analyst | analyst (sonnet), in parallel with the Red team | analyze-backtest | `Pass 1.md`, `Build.md`, `Changelog.md`, runs | `Pass 2.md`, report page, Trials rows |
| 9 | Red team | red-team (sonnet), fresh | red-team | `Pass 1.md`, `Data check.md`, `Build.md`, code (`Pass 2.md` only after its findings) | `Red team.md` |
| 10 | Report | you | strategy-report | `numbers.md` from `lab/strategy_report.py`, index, Pass 1 1.1 and 1.4-1.5, verdicts of Pass 2, Red team | `<Strategy> - Report.pdf` in the folder |
| 11 | Tests | you, one command for the batch; the user approves it | | the reports | `lab/run_test.py --batch`: test runs and `TEST_DONE` locks |
| 12 | Post-test | analyst (fresh, one per strategy, in parallel) | analyze-backtest | the test run | `Test.md`: passed or killed, folder moved; then the report again |
| 13 | Book | pm (sonnet) | portfolio-manager | `Book.md`, the passed strategies | candidate review or book construction PDF in `vault/4 Book/Reviews/`; the book changes only on the user's word |
| 14 | Final report | you | | the Desk log | `vault/3 Research Log/Desk reports/<date>.md`: tests, assumptions, decisions |

Not in the lane: Scout (haiku) and Reader (a general-purpose agent with `model: sonnet`, told to follow `.claude/skills/reading-source/SKILL.md`) run only when the user asks. Later seat: Monitor.

Every question with a default is answered by `vault/Toolbox/Defaults.md`; nothing waits for the user before step 11.

## Prompt of an agent

The strategy folder, the step and phase in one line, the line on defaults, and nothing that would steer it. Example: `Strategy folder: vault/2 Strategies/Pipeline/Crypto TSMOM/. Phase gate. Do not wait for an answer: take the default of vault/Toolbox/Defaults.md, write it as an assumption, and go on.`

## Where the strategies are

`vault/2 Strategies/`: `Pipeline/` (in progress, from the Economist's Go to the test), `Passed/` (passed the sealed test, any zone but "contradicts": the library the books are built from), `Killed/` (with the reason, and a `revisit:` line when something could bring it back). Which strategies are traded is `vault/4 Book/Book.md`, never a folder.

## Where the logs are

`vault/3 Research Log/`: `Desk reports/` and `Lessons.md` (read by the user); `_desk/` holds the agents' logs: `Desk log.md`, `Research Log.md`, `Trials.csv`, `Trials summary.md`, `Desk economics.csv`.

## Desk log line

`YYYY-MM-DD HH:MM · <Strategy or idea> · <seat> → <outcome in a few words> · <next step> · <tokens>k tok`, with `assumption: ...` or `decision for the user: ...` when one was taken or raised.
