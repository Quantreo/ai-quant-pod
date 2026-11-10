## Data check

**Verdict: ready with reserves** · 2026-10-23 · data before 2025-01-01 only; test period: coverage counted, not read.

**Load**: `load("crypto_daily", test_start="2025-01-01")`, `load("crypto_funding", test_start="2025-01-01")` · universe: `crypto_universe(daily, top=1000, volume_window=14, min_age_days=180, min_names=1)` (no volume floor in Pass 1, so `top` is set above the number of listed names; `volume_window=14` only gates who has a rankable volume, the Amihud uses its own 14 days). Pass 1 has no `Review.md` round open.

| Need (Pass 1) | Dataset | Field | Period | Status |
| --- | --- | --- | --- | --- |
| 14-day return, beta, volatility, liquidation | crypto_daily | mark_open/high/low/close | 2020-07 to 2024-12 (train 2021 to 2023, validation 2024) | ok (0 NaN mark, 0 bad mark bars in the universe) |
| Amihud (abs return over USDT quote volume) | crypto_daily | quote_volume | same | ok (0 zero-volume days) |
| Funding | crypto_funding, crypto_daily.funding_rate | rate, interval_hours | same | issue 3 (3 names) |
| Underlying type, listing age, multipliers | perps_meta.csv | underlying_type, first_day, last_day | all | issue 1 |
| BTC perp for the hedge, equal-weight universe return | crypto_daily | mark_close | same | ok |
| Costs, thin-cell volume | crypto_daily | quote_volume | train | ok, see below |

**Universe** (listed 180+ days, coins, no volume floor): names per rebalance 2020 median 3 (flat 180 days, before train), 2021 min 31 / median 79 / max 114, 2022 113 / 125 / 135, 2023 131 / 143 / 184, 2024 185 / 222 / 251. 296 distinct names ever. 49 of them are dead before 2025 and stay in until their last bar. Entries 0.2 per day, exits near 0. Two relisted tickers (ICPUSDT.2, TLMUSDT.2), split by the build.

**Precondition (cell counts, counted from ranks only, no returns of the strategy)**: formation at day close, mark price, 14-day return 30/70 then Amihud 30/70 inside the group. Train 2021 to 2023: mean loser cell 10.95 names (thin and liquid cells are the same size by construction), min 3. By year, median: 2021 7, 2022 12, 2023 13 (2024: 20). **Passes the "at least 8 on average" bar.** But 200 formation days of 2021 (the first months, universe of 31 to about 80) have a cell under 8; the Developer should expect noisy 2021 and report cells by year.

**Thin loser cell**: median quote volume of the 7-day sampled formations, per name per day: 2021 30.2M USDT, 2022 15.0M, 2023 8.5M, 2024 6.4M; share of cell names under 1M a day: 0 in each year. So "thin" is relative to Binance perps: the thinnest 30% of a universe that already cleared 180 days. The 20 bp thin-side cost is a guess on names of 6 to 30M a day; 40 bp stress is reasonable.

| # | Issue | Evidence | Effect on the test | Instruction to the Developer |
| --- | --- | --- | --- | --- |
| 1 | A stablecoin is typed COIN and enters the universe | USDCUSDT, 481 days in the universe (2023-03-12 to 2024-12-31), close 0.9845 to 1.0015, median 2.6M a day. Pass 1 says stablecoins out | Amihud near zero, 14-day return near zero: it would sit in the liquid middle, adds a name to the denominators and could land in the liquid-winner/loser cell on small moves | Drop USDCUSDT after `crypto_universe` (explicit list of stablecoins, checked by close within 0.97 to 1.03 over its life). Keep USTCUSDT (a collapsed coin trading 0.013 to 0.061 from 2023-11, not a peg) and TUSDT (Threshold token) |
| 2 | Last price and mark price disagree on collapse days | LUNAUSDT 2022-05-12: close 0.0080, mark_close 0.00032 (96%), volume 5.3B. 22 name-days in the universe over 5% (next worst BONDUSDT 2024-12-16, 30%) | Signals and P&L on last price would show a false rebound on LUNA | Use mark OHLC everywhere, as the desk does. Fall back to last price only on days with no mark (none in the universe before 2025). Pass 1's 15 bad mark OHLC dates: the checker finds 0 inconsistent mark bars before 2025 (on the universe), so no fix is needed on train and validation; do not silently re-add one |
| 3 | Days with a price and no funding print, held names | ICPUSDT, TLMUSDT, BNXUSDT: 491 rebalance days in the universe with no print (ICP 396, TLM 329, BNX 306 name-days in the panel). QTUMUSDT 10 days, USDCUSDT 1 | The P&L silently misses funding on these days; P4 (price share of gross) is computed on a funding that is incomplete | Do not treat NaN as zero without counting. Charge no funding on those days, but report the held name-days without a print by year and leg, and rerun the P4 share excluding these three names; say which of the two is used in the gate |
| 4 | Funding timing at a 00:00 rebalance | The daily `funding_rate` sums the UTC day's prints; the book is formed and filled at 00:00 and tranches roll daily | The print at 00:00 belongs to whoever holds at that time: a daily sum mixes old and new positions | Use the universe row of t-1 for a 00:00 fill (the row of t uses t's volume). Pay funding at print level (`crypto_funding`) to the holder at the print time, or state the daily-sum approximation and its size in the P&L split. Annualise per actual interval (62 names changed interval) |
| 5 | Quote volume spikes move the Amihud | 354 name-days above 50x the name's own 14-day median volume (worst BNTUSDT 2023-10-08, 643x; NMRUSDT 2023-09-02, 593x) | A spike day lowers the Amihud of the name for 14 days, so a name can switch cell on one print | Keep the plain 14-day mean of abs return over volume as written; report how often a name changes liquidity cell inside one holding and, in V1, the median volume is robust to this by design |

**Harmless warnings**:
- Missing fingerprint file: no fingerprint written yet, nothing to compare.
- 37 one-bar moves above 80% (UNFIUSDT 2022-06-07 +450%, DOGEUSDT 2021-01-28 +390%, PNUTUSDT 2024-11-13 +282%): real pumps of listed names; the book holds 14 days with a vol target so a pump hits a tranche of at most 1/14 of the book. Developer: report the largest single-name P&L day by leg.
- BNXUSDT 10 missing bars (2023-02-22, an 11-day gap): returns across the gap span several days; compute the 14-day return and Amihud by dates, never by 14 rows, and do not annualise the gap return as one day.
- Funding prints above 1% in absolute value: 521, mostly TRB, BLZ, LPT, LOOM, RARE; real extreme funding on small names, and the strategy pays what it holds. Flagged for P4 only.
- Multipliers (1000BONK, 1000FLOKI, 1000LUNC, 1000PEPE, 1000RATS, 1000SATS, 1000SHIB, 1000XEC): returns and Amihud are scale free; only a price-level filter would care and Pass 1 has none.
- Underlying type: all 296 universe names are COIN; no stock or metal perps before 2025.
- Zombie bars: 0 names with the price unchanged 5 bars or more, 0 zero-volume days; the build already dropped them.
- 2020 universe flat for 180 days: before the train start.

**Proposed line for `reference/checks.md`** (crypto): "Stablecoins typed COIN: `underlying_type` does not separate USDC (USDCUSDT) from coins; Pass 1 sheets that exclude stablecoins need an explicit list, checked by a close inside 0.97 to 1.03."
