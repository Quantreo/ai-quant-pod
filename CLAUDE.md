# AI Quant Pod : the research pod

This repository is a systematic research pod run by Claude Code agents. Each agent holds one seat (scout, reader, ideator, economist, critic, data, developer, analyst, red team, portfolio manager) and works on the same Obsidian vault a human researcher would use.

The method is the one of **The Systematic Trading Lab**: write what you expect before you look at the result. The agents automate the work, they do not relax the method.

## Where things live

| Folder | What it holds |
| --- | --- |
| `vault/` | The shared memory of the pod. Agents talk to each other only through these notes. Start with `vault/README.md`. |
| `vault/0 Library/` | Sources (PDFs), reading notes and technique cards. What the pod knows. |
| `.claude/agents/` | One file per seat: its job, its allowed tools, its model. |
| `.claude/skills/` | Procedures a seat loads when it needs them (read a paper, judge an idea, build a strategy, write a report). |
| `lab/` | The Python library: universe, signal, sizing, backtest, diagnostics, trials. Agents call it, they never rewrite it. |
| `data/` | Download scripts. The data itself is built on each machine and is read only. |
| `strategies/`, `results/` | One file per strategy, and every saved run. |

## The pipeline

```
Library (run by hand):  Scout → Reader → Technique cards

The desk (/desk):       Ideator → Economist → Data → Developer (train gate)
                        → Critic → Economist → Developer (validation)
                        → Analyst + Red team → [you approve the tests]
                        → sealed test → Analyst → report → Portfolio manager
```

Each seat writes its output into a precise place of the vault (a reading note, a Pass 1, a review, a build note, a Pass 2, a test note, a report). The next seat reads it from there.

The user steps in twice: the theme at the start, and one approval of the batch of sealed tests near the end. Everything else runs on the defaults of `vault/Toolbox/Defaults.md`.

## Non-negotiables

1. Pass 1 of a strategy is written before any code is written for it.
2. Every backtest run is saved and logged, especially the bad ones. Every try counts.
3. The test period is opened once, only through `lab/run_test.py`, after the user approves it. The permissions in `.claude/settings.json` and the hook `.claude/hooks/test_guard.py` enforce it.
4. Entries in the book at half weight, exits on the written rule only. Nothing changes in the book outside the monthly slot. The book is the user's decision.

## House rules for every agent

- Talk to the user in English and write everything in English (vault, code, reports, messages).
- Never invent a source, a number or a citation. If you did not read it, say so.
- Reading notes paraphrase. Never copy a paper, a fund letter or an article into the vault; one short quote at most, with the link.
- Backtest charts: cumulative return in %, linear scale. Never "growth of $1", never log scale.
- Run Python with `poetry run python` (or `python3` for standard-library scripts).
- Write plainly, like a researcher writing for a colleague. No em dashes.
- When you are unsure, stop and write the question in the note rather than guessing.

## Status

The pod is built seat by seat, section by section. Only the agents in `.claude/agents/` and the skills in `.claude/skills/` exist. Do not call a seat that is not there.
