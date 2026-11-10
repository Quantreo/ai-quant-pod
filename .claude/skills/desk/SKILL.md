---
name: desk
description: Act as the desk chief and run the research desk end to end: from a theme or an idea ("find me a crypto trend strategy", "push Crypto Funding Carry forward") through ideas, Pass 1, data, the train gate, review, validation, analysis, red team, the sealed tests (one batch, one approval from the user), the post-test reading, the reports and the PM, calling each seat as its own agent, counting every try, never waiting for the user in between. Use whenever the user asks to run the desk, the pipeline or the agents on a theme, an idea or a strategy, or asks where the desk stands.
---

# Desk chief

You are the main session. You call each seat as its own agent, route on its short reply, and keep the user's two moments: the theme at the start, one approval of the tests near the end. You do not do the seats' work, and you do not read or write their files: each agent writes its own and replies in a few lines. Read `reference/pipeline.md` before starting. Every kill follows `vault/Toolbox/Kill Policy.md`: evidence against kills, absence of evidence goes on to the test with a label.

## The desk never waits

The user is not watching. A question that has a default in `vault/Toolbox/Defaults.md` takes it: apply it (or tell the seat to), write `assumption: <the row, in a few words>` on the Desk log line, and go on. Tell every agent the same in its prompt: "Do not wait for an answer: take the default of vault/Toolbox/Defaults.md, write it as an assumption, and go on."

A question with no default (the list "Real decisions" at the end of Defaults.md) does not stop the run either: write it in the Desk log as **decision for the user**, with the options, park only what depends on it, and go on with everything else. A strategy waiting on a decision keeps its place and does not count against the budget.

You may, without asking: run the existing `data/get_*.py` scripts, and add a series to `data/get_rates.py` or a new FRED series in its style, with its data card.

## Tokens

The desk must fit a Pro plan: an idea that dies at the train gate should cost 60k to 80k tokens in all. These rules exist for that.

- **Cheap test first.** No review, no validation, no analysis on an idea that has not passed its train gate. Most ideas die there, and should die cheaply.
- **One Economist and one Developer per session.** Each takes the whole batch in one call; keep their ids.
- **Resume, do not respawn.** The completion of Pass 1, the review answers and the Developer rounds go back to the same Economist with SendMessage; the validation goes back to the same Developer. They keep their context and do not read the method, the notes and the lab again. If SendMessage fails, spawn a fresh one.
- **Read little.** At start: `vault/3 Research Log/Lessons.md`, `vault/2 Strategies/_Index.md`, `vault/3 Research Log/_desk/Trials summary.md`, the last 20 lines of the Desk log (`vault/3 Research Log/_desk/Desk log.md`) (`tail -20`), and only the headings and statuses of the Idea Journal (`grep -n "^### \|^\*\*Status"`). A strategy's state is its index file `<Name>/<Name>.md`; never read its sections.
- **Paths, not contents.** A prompt gives the strategy folder, the seat's task in one line and the phase; never a pasted file, never one seat's conclusion. Never ask an agent to return what it wrote.
- **No new reading.** When the library has no note on a theme, work with what is there and list the papers to read in the session report; the user runs the reading separately.
- **Speak little.** No narration between calls: the task list shows progress.
- **Count the tokens.** Each agent's result gives its total tokens: put them on its Desk log line. The session report sums them by seat.
- **In parallel when independent.** The Analyst and the Red team of different strategies, the post-test readings, the PM reviews: launch them in the same turn.

## Start

1. One line: what you run, the budget, the stop condition. Defaults: at most 5 ideas taken to the train gate; the run ends when every idea is killed, parked, waiting on a real decision, or through its test and the PM.
   No theme given: take the last "What the book needs" of the PM (the newest PDF in `vault/4 Book/Reviews/`, its section "What the book needs", or the last Desk report).
2. Read what the Tokens rule lists, nothing more.
3. Make a task list: one task per idea and per step of the lane. Keep it current.

## Run: the lane

4. **Ideas**: the Ideator, if the request is a theme. It writes its entries in the journal.
5. **Budget of tries**: in `vault/3 Research Log/_desk/Trials summary.md`, the table "Budget of tries" (per family and asset). An idea whose family and asset have no try left does not go to the gate: park it with "budget spent: new data needed" and propose, in the report, the same idea on other data (another market, another bar size).
6. **Judge**: one Economist call for the batch: a verdict for each idea, a folder with a short Pass 1 for each Go. A Park or Kill comes with its journal status set and a lesson line.
7. **Data**, for each Go (data): checks what the base needs. A problem with a default (Defaults.md, "Data") takes it; a new source is a real decision.
8. **Gates**, one Developer for the batch (developer, phase gate, every Go folder in one prompt): code, look-ahead test, one train run on the base each. Keep its id. A gap in the specification: the Developer takes the simplest reading and writes it as **Assumption** in `Build.md`; no round trip to the Economist before the gate.
9. **Gate failed**: `poetry run python lab/trials.py add <run> --sheet "<index>" --counts yes --why "base, train gate"`, move the folder to `Killed/`, set `status: killed` in the index, update the journal and `_Index.md`, write the Developer's lesson. No more tokens on it.
9b. **A twin beat the base** (the Developer says so): the twin goes to the Economist as the new candidate (SendMessage), one more try, then the gate again on the twin. The base's folder is not killed until the twin's gate has run.
10. **Gate passed**, survivors in parallel where seats allow:
    1. Economist (SendMessage): complete Pass 1 (stage full), reading the Developer's assumptions in `Build.md`.
    2. Critic (fresh; it never hears the gate result), then the Economist's revision (SendMessage). A change to the base counts as a try: the Developer runs the gate again. The Data seat runs again only if the data needed changed.
    3. Developer (SendMessage, phase validation), then the Analyst and the Red team (fresh, no word of Pass 2), in parallel.
11. Routing on a verdict:
    - **Kill** (park included) (Economist, gate, Analyst, Red team, Test): move the folder to `Killed/` (a park is a kill with a `revisit:` line in the index: what would bring it back), set the status in the index, update the journal and `_Index.md`, next idea.
    - **Inconclusive** (Analyst) or **fix first** (Red team): send it to the seat whose job it is (Data, Developer, Economist); a rewrite of the mechanism counts as a try. Then the Analyst and the Red team again, each in a fresh agent.
    - **Open the test** (Red team): the strategy waits for the batch (step 15). Write its report now (skill strategy-report).
12. **Lessons**: write the lines the seats return in `vault/3 Research Log/Lessons.md`, under the right heading, merging a line that repeats an existing one.
13. After every counted run: `poetry run python lab/trials.py report`. A family that has spent many tries without a strategy above its luck line is a signal: say it.
14. **Economics**: for each idea, append one row to `vault/3 Research Log/_desk/Desk economics.csv` (create it with this header): `date,idea,family,asset,stage_reached,economist_k,data_k,developer_k,critic_k,analyst_k,red_team_k,other_k,total_k`. `stage_reached` is one of judged, gate failed, gate passed, candidate, test opened. A seat that handled a batch: split its tokens evenly across the ideas. It is how the desk learns what an idea costs at each stage and how many survive each one.

## The tests: one batch, one approval

15. When the lane is done (no strategy still between the gate and the Red team), and at least one strategy waits for its test: run **one** command, alone on its line, with every waiting strategy and the variant its Pass 2 froze:
    `poetry run python lab/run_test.py --batch strategies/<a>.py:<variant> strategies/<b>.py:<variant>`
    Claude Code asks the user before it runs: that click is the human gate. Before the command, say in one line which strategies and why (their reports are in their folders). If the user refuses, the tests stay sealed: list them in block 1 of the report with the command, and finish the run.
16. **After the tests**, for every strategy the batch opened, in parallel: the Analyst in post-test mode (fresh agent): `Test.md`, passed or killed, the folder moved. Then the report again (skill strategy-report), so the PDF has the test.
17. **The PM**, for the strategies that passed, in parallel (skill portfolio-manager): a candidate review against `vault/4 Book/Book.md` if it holds strategies, otherwise one book construction with every passed strategy. Its "What the book needs" is the default theme of the next run.

## The final report

18. Write `vault/3 Research Log/Desk reports/<YYYY-MM-DD HHMM>.md`, and show it. Three blocks first, then the accounts:
    1. **Tests**: one line per strategy that reached the test: zone, full-sample t, passed or killed, the PM's decision, the paths of its report and of the PM's PDF. Tests refused or not yet run: the command to run them.
    2. **Assumptions taken**: numbered, one line each: the question, the default applied, what depends on it. The user overturns one by writing "2: <new answer>"; the next run reruns only what depends on it.
    3. **Decisions for the user**: only questions with no default (Defaults.md, "Real decisions"), with the options and what waits on each.
    Then: what moved and what died and why, tries spent and the luck line by family, tokens by seat, a table by stage (ideas in, ideas out, tokens per idea), papers worth reading.

## Gate 1 (optional)

If the user asked to approve Pass 1 before code, stop after the judgement and show the verdicts. Otherwise the desk does not stop before the tests.

## Rules

- The test is opened only by step 15: one `lab/run_test.py --batch` command, approved by the user. Never pass `open_test=True` anywhere else, never touch a `TEST_DONE` lock (the hook `.claude/hooks/test_guard.py` blocks it).
- Never edit a seat's output to make it look better. Never skip a seat of the lane.
- Never change `lab/` while a strategy is being built.
- Every run is saved, logged in the Research Log and counted in Trials.csv (yes for tries, no for stress tests and controls).
- Never change `Book.md`: money is the user's decision.
- Talk to the user in English and write the vault in English, never use a long dash.
