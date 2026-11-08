# strategies

One file per strategy, written by the Developer from Pass 1 of its sheet, on top of the lab. A strategy file decides the target weights; `lab/` loads the data (test period sealed), builds the universe, computes the P&L and saves each run in `results/` (never committed).

The file is frozen once the test is run: the test runs this exact file, once, by a human.
