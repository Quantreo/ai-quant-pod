---
type: reference
updated: 2026-10-22
---

# Tags

> **What this is** : the only tags allowed in the library. Agents and humans use these, and nothing else.
> **Rule** : a reading note has exactly three tags, one per list, in this order: `[family, asset class, horizon]`. Technique cards use the asset class list in `tested_on`.
> **No fit** : take the closest tag and say so in the reply. Never invent a tag; a new tag is added here first, by a human.

## Family
The seven families of [[Strategy Families]]. If two fit, take the one the authors' mechanism points to.

| Tag | Family |
| --- | --- |
| `trend` | Trend and momentum, time-series or cross-sectional |
| `carry` | Carry, roll yield, funding, rate differential |
| `reversal` | Short-term reversal, liquidity provision |
| `value` | Value, fundamental anchor |
| `low-vol` | Low volatility, defensive, betting against beta |
| `event-driven` | Scheduled announcements, events |
| `seasonality-flows` | Calendar effects, known-date flows, time-of-day clienteles |

## Asset class

| Tag | Covers |
| --- | --- |
| `fx` | Currencies, spot and forwards |
| `crypto` | Crypto spot and perpetuals |
| `equities` | Stocks, equity indexes, equity ETFs |
| `rates` | Government bonds, rate futures |
| `commodities` | Commodity futures |
| `multi-asset` | Two asset classes or more |

## Horizon
Typical holding period of the strategy.

| Tag | Holding period |
| --- | --- |
| `intraday` | Less than a day |
| `daily` | 1 to 5 days |
| `weekly` | 1 to 4 weeks |
| `monthly` | A month or more |
