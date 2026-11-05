# Reading a research paper

The note replaces the PDF for the agents downstream. The Ideator scans summaries and techniques; the Economist reads full notes and builds the economic case with outside knowledge; the Data and Developer agents need the exact rule and data provenance. Each must be able to trust every line and check it at the page given.

Example of a finished note: `reference/example-paper.md`. Read it once to calibrate the level of detail; do not copy its content.

## Read

1. Extract the text: `poetry run python .claude/skills/reading-source/scripts/pdf_text.py "<pdf>"`. Read the whole `.txt` it writes, in parts (offset and limit), to the last page: text, footnotes, appendix. Never read the PDF itself with the Read tool: page images cost several times more tokens than the text.
2. Look at every table. Tables hold results the authors do not put forward.
3. Look at every chart: render only the pages the script lists as holding a figure (`--png 7,12`) and open the PNGs with the Read tool. Also render a page whose table came out garbled in the text. Use charts for shape: when, how long, how deep. Do not read a level off a chart when a table gives the number. Check every reading against the tables and keep the table figure when they disagree. Mark values read from a chart with ≈.
4. Cite the page number printed on the page (journal pagination) when there is one, else the PDF page. Say which, once, under the summary.

## Extract

- **Mechanism**: the authors' claim, the evidence they give, the caveats they raise against themselves, what they rule out. If none: "Not stated by the authors." Do not build one: that is the Economist's job.
- **Strategy, brick by brick**: universe, period, signal, entry, exit, horizon, sizing, portfolio, rebalancing, costs, data and tools. Then the exact rule as a formula.
- **Data provenance**: sources per asset class, backfills, what the series really is before the instrument existed.
- **Results**: aggregate; by sub-group (asset class, instrument, long / short, period); by horizon or parameter; over time (flat stretches, drawdowns); links to other strategies or factors.
- **Test type**: label every result: simulation inside the paper's own model, real data in-sample, or real data out-of-sample / ex-ante. Real data first. A simulation run in the model the rule was built for says little about markets.
- **Where it does not work**: weakest sub-groups, negative cells, losing periods. "Positive everywhere" is not "good everywhere".
- **Profit decomposition**, when the paper gives one: say where the profit comes from.
- **In-sample choices**: say when parameters were picked on the same sample as the reported results.
- **Admissions**: when the authors concede something that weakens their main result (no better than a simpler rule, not significant, fragile), it goes in the summary.
- **Inconsistencies**: text vs table, stated totals vs final values, captions vs content. An inconsistency is two statements that cannot both be true; loose wording ("about 2x" for 2.4x) is not one. Report each one; never fix one silently.
- **Claims without evidence shown**: "not reported", "robust to", "similar results", "without loss of generality", regime claims backed only by a chart. They are leads for later research.
- **Techniques**: every reusable method, its kind (technique or principle), its brick, the author's reason ("Not argued" if none), its page.
- **Regime observations**, **acknowledged limits**, **what the paper does not address** (costs, slippage, drawdowns, capacity, out-of-sample, data details).

## Write

- Under 2,000 words, counted as Obsidian does (frontmatter and table borders excluded). When too long, cut raw values before findings.
- Summary: five bullets, 30 words max each, headline figures only. "Where it works best" uses real data only; simulations go in Results and caveats.
- Summarise the paper's tables, do not copy them: range, best and worst cell, and the table number for the detail.
- One line, one fact, one source in a **Where** column.
- Short sentences. No filler, no explanation of what a section is for.
- Copy figures as printed. A rounded or computed figure says so ("computed").
- Always say gross or net, and which costs are included.
- Affiliations: who wrote it, nothing about what the firm does.
- Tags: exactly three, `[family, asset class, horizon]`, only from `vault/Toolbox/Tags.md`, e.g. `[trend, multi-asset, monthly]`. Never invent a tag.
- Tier: 1 peer-reviewed or academic working paper; 2 manager or practitioner research. See `vault/Toolbox/Source Registry.md`.
- Bricks: economic intuition, universe, signal, calibration, horizon, entry, exit, risk, sizing, rebalancing, evaluation.

## Checklist

- [ ] Every table and figure of the paper was looked at.
- [ ] Every row has a Where.
- [ ] Every number is in the PDF, marked ≈, or is a computation from PDF numbers shown as such.
- [ ] Summary: five bullets of 30 words max (finding, mechanism, where it works best, weak spots, main caveats), authors' admissions included.
- [ ] Every result labelled by test type; real data first.
- [ ] "Where it works best" from real data only.
- [ ] Chart readings checked against the tables.
- [ ] No paper table copied in full.
- [ ] Under 2,000 words (Obsidian count).
- [ ] Mechanism is the authors' claim, or "Not stated by the authors."
- [ ] Results include sub-groups and where it does not work, or "Not addressed" says the paper gives none.
- [ ] Gross or net is stated.
- [ ] No outside knowledge, no opinion, no idea.
- [ ] Three tags, all from `vault/Toolbox/Tags.md`. No long dash.
