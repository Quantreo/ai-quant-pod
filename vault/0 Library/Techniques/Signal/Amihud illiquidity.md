---
type: technique
brick: signal
aliases: [Illiquidity ratio, Return-to-volume ratio]
sources: 1
tested_on: [crypto]
---

# Amihud illiquidity

> [!summary]
> Average absolute daily return per dollar traded, used to rank assets from liquid to illiquid.

## How it works

- **Inputs**: daily return and daily traded volume in USD for each asset.
- **Formula**: mean over the window of |return| divided by volume.
- **Lookback / holding**: one window length, a parameter.
- **Output**: an illiquidity score per asset, cut into liquid, neutral and illiquid groups by quantile.
- **Direction**: none on its own. It conditions another signal.
- **Tested on**: crypto.

## What the sources say

### Parameters
- **Begušić 2019**
	- I(t) = mean over 14 days of |R| / V, V in USD (Eq. 2, p. 3)
	- Liquid: lowest 30%. Neutral: middle. Illiquid: highest 30% (p. 3)
	- Same 14-day window as the momentum signal (p. 3)

### Why
- **Begušić 2019**: the authors study how momentum interacts with liquidity. Momentum is stronger among liquid coins in international equities (p. 1).

### Evidence
- **Begušić 2019**: in-sample, Jan 2015 to Jan 2019, 711 coins, gross unless stated
	- Illiquid losers 1.07% daily vs illiquid winners 0.53%. The authors say this seems to confirm that illiquid coins mean-revert (Table 1, p. 3 to 4).
	- Illiquid minus liquid among losers: 0.52% daily, significant at 5% (Table 1, p. 3)
	- Long-only illiquid losers: IR 2.49 gross; 0.95%, IR 2.16 at 100 bps (Table 2, p. 5)

### Limits
- **Begušić 2019**
	- Authors expect illiquid losers to cost more than assumed, as bid-ask spreads are wider (p. 5)
	- Cost method not stated; no spread data (p. 5)
	- Volume quality of the single data source is not discussed (p. 2)
	- One window only, no robustness test

## Sources

- [[2019 - Begušić Kostanjčar - Momentum and liquidity in cryptocurrencies]] (Begušić 2019)
