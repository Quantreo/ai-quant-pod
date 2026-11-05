---
type: reference
updated: 2026-10-20
---

# Source Registry

> **What this is** : every source the Reader is allowed to open, ranked by how much you can trust it, and whether an agent can actually read it.
> **Open it** : when you add a source, or when a reading note looks thin and you wonder where it came from.
> **Rule** : a source not in this list is not read by the agents. New sources enter as **candidate**, and a human promotes them.

The human list of where to look is [[Reading Sources]]. This note is the same idea, written for the agents: tier, access, what to expect from it.

## The four tiers

| Tier | What it is | What it is good for | What the Reader must do |
| --- | --- | --- | --- |
| **1. Primary research** | Peer-reviewed papers, working papers, central bank research | The mechanism, the original test, the numbers | Read the abstract and the tables before writing a number |
| **2. Manager research** | Research papers published by asset managers | Practitioner versions of a premium, costs, capacity | Name what the manager sells: the paper is also marketing |
| **3. Manager commentary** | Monthly or quarterly letters, interviews, press quotes of managers | Which markets paid and which hurt, in which regime | Never derive a strategy from it alone. It feeds "works when / breaks when", not Pass 1 |
| **4. Practitioner blogs and aggregators** | Blogs, newsletters, strategy catalogues | Fast idea flow, replications, critiques | Trace the idea back to a tier 1 or 2 source before it reaches the Idea Journal |

## The registry

Scope: multi-asset, with **FX and crypto** first.

Access tested on 2026-10-20 with the agent fetch tool. **ok**: the text is readable. **partial**: readable but part of the content is missing (video, paywalled code). **index broken**: articles readable, list page not. **blocked**: the agent cannot read it, keep out.

### Tier 1 · Primary research

| Source | Link | Access | Notes |
| --- | --- | --- | --- |
| SSRN | https://www.ssrn.com | ok (abstract pages) | Search by family name, sort by downloads. Abstract and metadata readable. |
| arXiv q-fin | https://arxiv.org/list/q-fin.TR/recent | ok | Also q-fin.PM, q-fin.ST. Lots of ML and RL papers with weak tests: tier 1 by format, not by quality. |
| New York Fed staff reports and Liberty Street Economics | https://libertystreeteconomics.newyorkfed.org | ok | Macro, rates, announcement effects. |
| NBER working papers | https://www.nber.org/papers | index broken | The listing page shows no papers. Use paper pages found through search. To verify: a feed for the asset pricing programme. |
| BIS, Quarterly Review and working papers | https://www.bis.org/quarterlyreviews/index.htm | ok | FX market structure, dollar funding, carry, the Triennial Survey. The reference for FX. |

### Tier 2 · Manager research

| Source | Link | Access | Notes |
| --- | --- | --- | --- |
| AQR Insights, Research | https://www.aqr.com/Insights/Research | ok | Factor and trend research. Recent output is heavy on tax-aware investing: filter. |
| Graham Capital, research papers | https://www.grahamcapital.com/resource-center/research-papers/ | ok | Trend, tail risk, execution. A few papers a year. |
| Robeco, quantitative research | https://robeco.com/nl-nl/themas/quantitative-research | ok | Factors, low vol, ML. Slow pace. |
| Man Institute | https://www.man.com/insights | index broken, partial | The insights page lists nothing for an agent; some articles are videos. To verify: a feed or sitemap. |
| Research Affiliates | https://www.researchaffiliates.com | not tested | Value, fundamental indexation. |
| Galaxy Research | https://www.galaxy.com/insights/research | ok | Crypto. The quarterly "State of Crypto Leverage" report and liquidation post-mortems: funding, leverage and deleveraging regimes. |
| Glassnode Research | https://research.glassnode.com | partial | Crypto on-chain. Archive readable; recent publishing pace to verify. |
| Two Sigma Venn | https://venn.twosigma.com | **blocked** | Robots disallow agents. Keep out. |
| Coin Metrics | https://coinmetrics.io | **blocked** | Now redirects to Talos. Keep out until a stable research page exists. |
| Kaiko research | https://research.kaiko.com | **blocked** | Redirects to a login. Keep out. |

### Tier 3 · Manager commentary

| Source | Link | Access | Notes |
| --- | --- | --- | --- |
| HedgeNordic | https://hedgenordic.com | ok | Articles quote Nordic CTAs on what drove the month (sectors, speeds, models). Good regime evidence. |
| Manager letters dropped by hand | `vault/1 Ideas/Inbox/` | n/a | PDFs or texts the human adds (letters, subscriptions). The safest way to use letters you have the right to read. |
| Top Traders Unplugged, Systematic Investor series | https://www.toptradersunplugged.com | partial | The CTA podcast: managers and hosts discuss what trend did each month. Episode outlines only, no transcript. |
| ING THINK, FX | https://think.ing.com | partial | Bank FX research: monthly FX forecast tables (PDF) and outlooks. Some pieces are videos only. Read the reasoning, ignore the point forecasts. |
| Robin Brooks | https://robinjbrooks.substack.com | partial | Macro and FX, former IIF chief economist. Some posts are videos without transcript. |
| am/FX, Brent Donnelly (Spectra Markets) | https://www.spectramarkets.com/product/am-fx-subscription/ | paid | Daily FX and macro letter read by FX traders, from 69 $ a month. Only through the Inbox, if subscribed. |
| HedgeFundAlpha letters | https://hedgefundalpha.com/letters/ | **blocked** | Database scaled back in July 2026, paid. Keep out. |
| Seeking Alpha fund letters | https://seekingalpha.com | **blocked** | Paywalled. Keep out. |

### Tier 4 · Practitioner blogs and aggregators

| Source | Link | Access | Notes |
| --- | --- | --- | --- |
| Quantocracy | https://quantocracy.com | ok | Daily aggregator of quant blogs. The best single entry point for the nightly scan. |
| Alpha Architect | https://alphaarchitect.com/blog | ok | Digests of academic papers, with the link to the paper. |
| Quantpedia | https://quantpedia.com | ok | Blog and monthly recap free; strategy database partly paid. |
| Rob Carver | https://qoppac.blogspot.com | ok | Few posts a year, very high signal on trend, sizing, costs. |
| Quantitativo | https://www.quantitativo.com | partial | Text readable, code paywalled. |
| Concretum Group | https://concretumgroup.substack.com | partial | Text readable, rules and archive paywalled. |
| Robot Wealth | https://robotwealth.com | not tested | Practical research, honest about what fails. |
| Moontower, Kris Abdelmessih | https://moontower.substack.com | partial | Options and volatility from a former market maker. Page needs JavaScript; posts to test one by one. |
| Concoda | via Substack | not tested | Macro plumbing: funding markets, repo, dollar liquidity. Freemium, twice a week. |
| Money Stuff, Matt Levine (Bloomberg) | by email | Inbox only | Market structure and the stories behind trades. Free by email, paywalled on the web. |

## Candidates

Sources proposed by the Reader in exploration mode land here, with the reason. A human moves them up or deletes them.

| Source | Link | Proposed by / date | Why | Decision |
| --- | --- | --- | --- | --- |
| | | | | |

Related: [[Reading Sources]] · [[Reading Note Template]] · [[Idea Journal]]
