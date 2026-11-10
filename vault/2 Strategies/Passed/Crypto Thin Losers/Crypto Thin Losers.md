---
type: strategy
name: Crypto Thin Losers
family: reversal
asset: crypto
horizon: weekly
status: passed
version: v2
idea: "[[Idea Journal]] · 2026-10 · Crypto perps: thin losers against liquid losers"
---

# Crypto Thin Losers

Among 14-day losers on Binance perps, long the thin names and short the liquid ones, beta-hedged: sellers of thin coins after a fall pay whoever absorbs their selling [hypothesis].

| Seat | Date | Verdict | File |
| --- | --- | --- | --- |
| Economist | 2026-10-23 | Go | [[Pass 1]] |
| Critic | 2026-10-23 | revise (1 blocking, 5 major, 2 minor) | [[Review]] |
| Data | 2026-10-23 | ready with reserves | [[Data check]] |
| Developer | 2026-10-23 | gate pass (train, base, v2: #1 NW t 3.04, #2 net 1.38); validation, V1, V2, stress tests, delay control run (base validation net 0.33) | [[Build]] |
| Economist | 2026-10-23 | v2: 5 fixed, 3 partly; gates #1 and #2 to rerun | [[Review]] |
| Analyst | 2026-10-23 | candidate for the test, with warning (1.11 #1 to #4 pass on train; 2024 net 0.33, break-even 20 bp) | [[Pass 2]] |
| Red team | 2026-10-23 | open the test (0 blocking, 2 major, 4 minor; 2024 placebo 13%, cost x2 net -0.19) | [[Red team]] |
| Analyst | 2026-10-24 | test: ambiguous zone (net mean 0.32 of train+validation, t 0.5): keep on paper only, no money; long thin leg -45%, profit from the short liquid leg | [[Test]] |

[[Changelog]]
