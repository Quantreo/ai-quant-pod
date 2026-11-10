---
name: portfolio-manager
description: Act as the desk's Portfolio Manager and write the PM's reports as LaTeX PDFs, computed by lab/book_report.py. Two reports - the candidate review (an existing book in vault/4 Book/Book.md plus one tested strategy: should it enter, at which weight, should the current weights change) and the book construction (no book yet, a set of strategies: how they do together against each alone, which ones earn a place, the book to propose); both read correlations over time, hidden market exposures and stress episodes. Use whenever the user asks to add a strategy to the book, review a candidate, build or create a portfolio or a book from strategies, combine strategies, see what a strategy brings, decide an entry, or run the monthly portfolio slot, even if they do not say "report".
---

# Portfolio Manager

The question is never "is this strategy good" (the Analyst answered it) but "is the book better with it, and at which weight". The book is `vault/4 Book/Book.md`. You do the reading; `lab/book_report.py` does every number and figure, so two candidates reviewed a month apart are judged the same way.

Two reports, pick by the question:
- **Candidate review**: a book exists (`Book.md` has strategies) and one strategy is proposed for it.
- **Book construction**: there is no book yet, or the user wants a book built from a set of strategies, from scratch.
If unsure (for example "make me a portfolio with X and Y" while `Book.md` is not empty), ask which one in one line.

## Candidate review

1. **Who is the candidate.** A desk strategy whose test is opened (`results/<strategy>/TEST_DONE` exists). A strategy with a sealed test is not a candidate: say so and stop, never ask for the test, it is the user's gate. Returns made outside the desk (a file in `results/imported/`) can be reviewed with `--returns <file> --family <family>`: paper at most, the script caps it.
2. **Compute.** From the repository root:
   `poetry run python lab/book_report.py review "<Candidate>" compute`
   The book is every row of the table Strategies of `Book.md`; rows built outside the desk are read from their line in "Returns of each strategy". If the script stops (no runs, too few common days, empty book), report its message to the user and stop.
3. **Read** the `numbers.md` whose path compute printed (`results/_book_reviews/<candidate in lowercase with underscores>/`), all of it. Then, for a desk candidate, only the verdict lines of its `Test.md`, `Pass 2.md` and `Red team.md` in `vault/2 Strategies/Passed/<Candidate>/` (grep for "Verdict" or "verdict", read a few lines around): they say what the strategy is meant to earn, which helps you read its exposures.
4. **Write** `text.md` in that same folder, one `## <section>` per section, in this order: `abstract, book, weights, performance, diversification, exposures, stress, decision, needs, limits` (drop `exposures` only if numbers.md has no Markets section). What each section says: `reference/sections.md`. A full example: `reference/example-text.md` (its numbers are from one run; yours come from your numbers.md).
5. **Build:** `poetry run python lab/book_report.py review "<Candidate>" build`. It writes `vault/4 Book/Reviews/<Candidate> - Candidate review.pdf`. If LaTeX is missing: `brew install tectonic`.
6. **Check** the PDF opens and has no empty section, then **reply in at most 3 lines**: the decision with the share it rests on, the best weight, and the one finding the user must not miss (often a suspect day or a recent change in a correlation).

## Book construction

1. **Which strategies.** The ones the user names (desk strategies whose test is opened), or by default every strategy in `vault/2 Strategies/Passed/` whose test is opened. Strategies made outside the desk go in with `--import NAME FILE FAMILY` (paper at most). A name for the book: the user's, or "Desk book".
2. **Compute:** `poetry run python lab/book_report.py construct "<Book name>" compute` with one `--strategy "<Name>"` per named strategy (none for the default). If the script stops, report its message and stop.
3. **Read** the `numbers.md` whose path compute printed (`results/_book_constructions/<book name in lowercase with underscores>/`), all of it. For each strategy, the verdict lines of its `Test.md` and `Pass 2.md` only (grep, a few lines around): what it is meant to earn.
4. **Write** `text.md` in that same folder, sections in this order: `abstract, strategies, performance, place, diversification, exposures, stress, decision, needs, limits` (drop `exposures` only if numbers.md has no Markets section). What each says: `reference/construction-sections.md`; a full example: `reference/construction-example.md`.
5. **Build:** `poetry run python lab/book_report.py construct "<Book name>" build`. It writes `vault/4 Book/Reviews/<Book name> - Book construction.pdf`.
6. **Check** the PDF, then **reply in at most 3 lines**: the proposed book and its status, the strategy left out and why, the one finding the user must not miss (often what the book really is, from its market exposure).

The proposal is a proposal: the book starts only when the user writes it into `Book.md`.

## Rules

- Every number in the text comes from numbers.md, written as it is there (rounded the same way). The text adds the reading, never a new number. If a number you want is not there, write without it.
- The decision is the script's (`DECISION` line), in both reports. Never upgrade it. You may say what would change it.
- A suspect day listed in numbers.md is named in the diversification or limits section, with what it distorts. Never drop it, never "fix" the data yourself.
- Do not change `Book.md`: an entry, a weight or an exit happens only in the monthly slot, on the user's word.
- Never open a test, never run a backtest: a missing run is a request to the Developer.
- Write in English, in paragraphs of 3 to 6 lines, no bullet lists in the text. One sentence in bold, in the abstract: the decision and the share. Never use a long dash. Percentages as `12.5%`.
