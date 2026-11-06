---
type: reference
updated: 2026-10-26
---

# Defaults

> **What this is** : the answer the desk takes, without asking, to every question that has a sensible default. The desk never waits for the user: it applies the default, writes it in the Desk log as `assumption: <row>`, and lists it in block 2 of its final report, where the user can overturn it ("2: borrow at 50 bp"). The desk then reruns only what depends on it.
> **What is not here** : block 3 of the report, the real decisions, the ones with no default (list at the end). A question of that kind never stops the run either: the strategy that needs it waits, the rest goes on.
> **Change a default** : edit the row. The next run uses it.

## Costs and financing

| Question | Default | Why |
| --- | --- | --- |
| Cost of a market listed in [[Cost Assumptions]] | the row of that note | confirmed or estimated before any test |
| Cost of a market not listed there | the closest listed market, doubled, marked "to confirm" in the sheet | a cost too high kills a weak edge, which is cheaper than trading a fake one |
| Short borrow on ETFs | 25 bp a year | Cost Assumptions |
| Leverage above 1x | T-bill + 50 bp a year, stress at T-bill + 150 bp | Cost Assumptions (estimate) |
| FX spreads by tier, when no minute data | EUR, JPY, GBP 1 bp; CHF, CAD, AUD 2 bp; NZD, NOK, SEK 5 bp, one way | desk proposal 2026-10-25, stress at 2x |
| Crypto per-name cost tiers | inside the strategy file, as Crypto Thin Losers does (5 bp ranks 1 to 25, 10 bp ranks 26 to 50) | never change `lab/` while a strategy is built |
| A position cap in % of volume needs a capital | base run without the cap; the cap as a read-only sensitivity at 1 m, 10 m and 100 m dollars | the base answers "is there an edge", the cap "how big can it be" |
| Every strategy | a stress at 2x all costs, logged with counts no | house rule |

## Data

| Question | Default | Why |
| --- | --- | --- |
| A doubtful print or a suspect day | run with and without the correction, keep the less favourable result, say which one decides | the doubt must never help the strategy |
| An instrument mislabelled by the exchange or the source | leave it out, list it in the report | adding it back by hand is a choice with no evidence |
| Thin instruments (ETF T5, illiquid names) | filtered in the universe, point in time; the data file is not changed | the raw data stays as downloaded |
| Data starts too late for the signal's first window | start the train where the signal is first defined, say how many periods were lost | do not move the test start |
| A series the existing `data/get_*.py` scripts can download, or a new FRED series | download it (with its data card) | allowed to the desk |

## Method

| Question | Default | Why |
| --- | --- | --- |
| Daily or monthly Sharpe, net or gross, when two figures differ | the less favourable one decides; both are written | the same rule as for doubtful data |
| A gap in the specification found while coding | the simplest reading, written as **Assumption** in `Build.md`; the Economist reads it only if the gate passes | no round trip before the cheap test |
| A twin beats the base | the twin becomes the candidate, one more counted try | Kill Policy |
| Pass 1 longer than its template | cut to the template, keep the numbers | the reader's time |
| An idea already parked or killed comes back | judged again only with new data or a new reason, written on its `revisit:` line | otherwise it is the same try |
| A strategy that reached "open the test" | its test is requested in the single batch at the end of the run (desk skill) | one human click for every test |
| A passed strategy and a book exists | the PM writes its candidate review against `vault/4 Book/Book.md` | the book is the question |
| A passed strategy and no book exists | the PM writes a book construction from every passed strategy | idem |

## Real decisions (no default: block 3 of the report)

- A new data source, a new download script, or a paid source.
- A new test window, or any change of TRAIN, VALIDATION or TEST_START (burns the test).
- A change to `lab/` (the shared library).
- Money: a strategy entering `Book.md`, a weight, an exit. The PM proposes; the user decides in the monthly slot.
- A rule of the method (Kill Policy, luck line, gates).
