---
name: ideation
description: Generate a few argued strategy ideas from the desk library (reading notes and technique cards) and write them to the Idea Journal. Use whenever the user asks for ideas, new strategies, variants, combinations or "what could we test", on a family, a market or the whole library.
---

# Ideation

1. From the repository root, run `python3 .claude/skills/ideation/scripts/library_index.py`. Add `--family`, `--asset` or `--horizon` when the user gives a theme (values in `vault/Toolbox/Tags.md`).
2. If the theme has no reading note in the index, stop. Say the library is empty on this theme and propose papers to import with the scout (`vault/Toolbox/Strategy Families.md` lists references by family). Generate nothing.
3. Choose the notes and cards to build on. Open only those in full, 2 or 3 notes; read their Weak spots, Claims without evidence and Regime observations.
4. Generate about 10 candidates with the operators in `reference/operators.md`. Fill every field of `assets/journal-entry.md` for each one.
5. Drop: duplicates of the journal or of a strategy (read only the headings: `grep -n "^### " "vault/1 Ideas/Idea Journal.md"` and `vault/2 Strategies/_Index.md`; dropped ideas included); ideas that a line of `vault/3 Research Log/Lessons.md` rules out, unless you say why this time is different; ideas needing data or trades the desk cannot have (`vault/Toolbox/Data Sources.md`; no high-frequency, no market making); ideas changing more than one brick of an existing strategy; ideas with no mechanism sentence.
6. Rank by mechanism strength, by what the idea adds to the book (a family or a payoff profile it lacks), and by the cost of its first kill test. Keep 5 at most.
7. With the user in the conversation: show a table (title, operator, what's new, mechanism sentence, first kill), wait for their picks and their reason for each rejected idea. As a subagent: keep your 5 and do not ask.
8. Write to `vault/1 Ideas/Idea Journal.md`, just above the first `### ` entry (insert with Edit; never read the whole journal): picks as **new**, rejected ideas as **dropped** with the user's reason.
9. Reply with one line per entry written (title, mechanism sentence, first kill), nothing else.

## Rules

- The mechanism sentence and "What's new" must make sense to someone who has not read the paper.
- At most one `replicate` idea per run.
- An idea that trades daily or intraday: its first kill is the cost. Estimate the yearly cost from turnover and spread before testing the signal.
- Every figure comes from a note or a card, with its source and page. Never a figure from memory.
- When the note qualifies a figure you cite (not significant, doubted by the authors, inconsistent, tested on another market), the entry says so in the same line.
- The core of each idea comes from the library: a mechanism, a brick or a result in a note. A `[hypothesis]` may extend it, never replace it. Never attach library figures to an idea that does not come from them.
- Label the mechanism sentence `[source: Author Year, p. X]` or `[hypothesis]`.
- Copy the page, table or figure the note gives. Never infer one; if the note gives none, cite the note without a number.
- Family: one general tag from `vault/Toolbox/Tags.md` (`trend`, not "trend XS").
- Never edit notes, cards or strategy sheets. Write only in the Idea Journal.
- Calibrate on `reference/examples.md`.
- Write in English. Never use a long dash.
