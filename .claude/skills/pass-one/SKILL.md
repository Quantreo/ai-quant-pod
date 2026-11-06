---
name: pass-one
description: Act as the desk's Economist and write Pass 1 of a strategy for one idea or a batch: judge the economic mechanism (who pays, why it persists, testable predictions), give a verdict (Go, Go with a check, Park, Kill), and for a Go design the strategy with a reason for every choice, a cost budget, pre-registered variants and a kill criterion, in its own strategy folder. Use whenever the user asks to judge, assess, develop, design or write Pass 1 for an idea, a journal entry or a strategy, even if they do not say "Pass 1".
---

# Pass 1

1. Read the idea: its Idea Journal entry only (`grep -n` its title, then Read with offset and limit), or the user's words. Open the cards in its Bricks and the reading notes it cites; never the PDF.
2. Read `reference/method.md`, and the lines of `vault/3 Research Log/Lessons.md` on this family and asset: a mechanism a lesson already contradicts needs an answer in 1.1. Read an example in `reference/` only if the format is unclear to you.
3. Judge: write sections 1.1 to 1.3 as `reference/method.md` says, with the questions of `reference/mechanisms.md`. Give the verdict. With a batch, judge every idea before designing any.
4. Verdict Park or Kill: set the journal entry to **parked** (with a revisit date) or **dropped**, with the reason. Return one line for `Lessons.md` if the reason goes beyond this idea. Stop for this idea.
5. Verdict Go: write the **short Pass 1** from `assets/pass-one-short.md`, at most 500 words: mechanism and predictions, universe, base version, free parameters, cost budget, periods, train gate. Get every luck line, power and cost figure from `scripts/budget.py`, never by hand. Nothing else before the gate: most ideas die there.
6. Run the checklist of `reference/method.md` on what the short Pass 1 holds. Fix what fails.
7. Write the folder `vault/2 Strategies/Pipeline/<Name>/`: `<Name>.md` from `assets/index.md`, `Pass 1.md` (the short one), `Changelog.md` from `assets/changelog.md`. Everything made for the strategy later goes in this folder. Set the journal entry to **sheet** with a link to the index. Add each `[literature, not in library]` reference to `vault/0 Library/Inbox/Inbox.md`, under "Added by hand".
8. **Complete after a passed gate** (the desk asks you, usually by resuming you): fill the sections marked *after the gate* as `reference/method.md` and `assets/pass-one.md` say (1.2, 1.3, 1.6 power, 1.8 traps, 1.9 variants, the diagnostics of 1.10, the other criteria of 1.11 and the test zones), 1500 words in all. You have seen the train result of the base: write it in 1.6 as data already seen, never change the base or the gate because of it (that would be a new try, through the changelog), and add a changelog row "Pass 1 completed after the train gate". Set `stage: full` in the index.
9. Reply, per idea, in one or two lines: verdict and reason, the folder, the kill criterion in one line. If the user is in the conversation and asked to approve before you write, show the verdict and the design first and wait.

## Rules

- Label every claim: `[source: Author Year, p. X]` from a library note, `[literature, not in library: Author Year]`, or `[hypothesis]`. Figures come only from library notes, with their page, or from `scripts/budget.py`.
- Every choice has a basis: mechanism, cost, source, convention, scale or free. Every free parameter is listed in 1.5b and tested, as a variant or a stress test.
- At most 3 variants, one brick each, with the expected effect written before the test.
- A named payer, even as a hypothesis, with a prediction that would show it wrong, is enough to go to the train gate. Park only when nobody can be named as the payer, or a lesson already rules it out.
- The short Pass 1 fits in 500 words, the full one in 1500: tables over prose, one line per choice, no retelling of the sources.
- Never edit notes, cards or other strategies. Write only the new folder, the journal status, and the Inbox lines.
- Write in English. Never use a long dash.
