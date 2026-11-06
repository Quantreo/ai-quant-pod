"""Numbers for a Pass 1: luck line, statistical power, cost budget. Standard library only.

Usage:
  python budget.py --tries 4 --years 5.2
  python budget.py --tries 4 --years 12 --trades 100
  python budget.py --tries 4 --years 5.2 --turnover 50 --cost-bp 5 --vol-target 0.20
  python budget.py --tries 4 --years 6.2 --rotation 0.4 --rebalances 52 --cost-bp 5 --vol-target 0.20
  python budget.py --tries 4 --years 3 --expected-sharpe 0.8
  python budget.py --tries 4 --years 3 --trades 156 --effect 0.15

luck line   expected best annual Sharpe of N tries with no skill, on T years
            (Bailey and Lopez de Prado, as in vault/Toolbox/Deflated Sharpe.md)
power       with n trades, the mean per trade must be at least bar / sqrt(n) of its standard deviation (bar: 1 under 5 years, else 2)
pass prob.  chance the gate's t clears the bar if the true edge is the one expected:
            Phi(Sharpe x sqrt(years) - bar), or Phi(effect x sqrt(trades) - bar); with no edge, 1 - Phi(bar)
turnover    times the whole capital is traded per year = rotation (share of the capital traded at each rebalance) x rebalances per year
cost        yearly cost = turnover x cost per unit traded; the gross Sharpe needed for costs to take
            less than half the edge = 2 x yearly cost / volatility target
"""
import argparse, math
from statistics import NormalDist

EULER = 0.5772156649


def luck_line(n, years):
    if n <= 1:
        return 0.0
    z = NormalDist().inv_cdf
    return math.sqrt(1 / years) * ((1 - EULER) * z(1 - 1 / n) + EULER * z(1 - 1 / (n * math.e)))


Phi = NormalDist().cdf


def pass_probability(expected_t, t_bar=2.0):
    """Chance that the measured t-stat clears t_bar when its true mean is expected_t (normal approximation)."""
    return Phi(expected_t - t_bar)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tries", type=float, required=True, help="independent tries: base version plus variants")
    ap.add_argument("--years", type=float, required=True)
    ap.add_argument("--trades", type=int, help="number of independent trades or periods in the sample")
    ap.add_argument("--turnover", type=float, help="times the capital is traded per year")
    ap.add_argument("--rotation", type=float, help="share of the capital traded at each rebalance, e.g. 0.4")
    ap.add_argument("--rebalances", type=float, help="rebalances per year, e.g. 52 for weekly")
    ap.add_argument("--cost-bp", type=float, help="cost per unit traded, in basis points, one way")
    ap.add_argument("--vol-target", type=float, help="annual volatility target, e.g. 0.20")
    ap.add_argument("--expected-sharpe", type=float, help="annual Sharpe the strategy is expected to have, for the pass probability")
    ap.add_argument("--effect", type=float, help="expected mean per trade divided by its standard deviation, for the pass probability")
    ap.add_argument("--t-bar", type=float, help="t-stat the gate asks for (default: 1 if --years is under 5, the train gate of a short train; 2 otherwise)")
    a = ap.parse_args()
    if a.t_bar is None:
        a.t_bar = 1.0 if a.years < 5 else 2.0
        print(f"Gate t-stat bar: {a.t_bar:g} ({a.years:g} years{' < 5: short train, the gate only kills what is clearly dead' if a.years < 5 else ''}).")
    print(f"Luck line: best of {a.tries:g} tries over {a.years:g} years reaches a Sharpe of {luck_line(a.tries, a.years):.2f} with no skill.")
    if a.trades:
        print(f"Power: with {a.trades} trades, a t-stat of {a.t_bar:g} needs a mean per trade of at least {a.t_bar / math.sqrt(a.trades):.2f} of its standard deviation.")
    if a.expected_sharpe is not None or a.effect is not None:
        print(f"False pass: with no edge, the gate passes {1 - Phi(a.t_bar):.1%} of the time (one-sided t > {a.t_bar:g}).")
    if a.expected_sharpe is not None:
        p = pass_probability(a.expected_sharpe * math.sqrt(a.years), a.t_bar)
        print(f"Pass probability: a true Sharpe of {a.expected_sharpe:g} over {a.years:g} years gives t > {a.t_bar:g} {p:.0%} of the time.")
    if a.effect is not None and a.trades:
        p = pass_probability(a.effect * math.sqrt(a.trades), a.t_bar)
        print(f"Pass probability: a true mean of {a.effect:g} sd per trade over {a.trades} trades gives t > {a.t_bar:g} {p:.0%} of the time.")
    if a.rotation and a.rebalances and not a.turnover:
        a.turnover = a.rotation * a.rebalances
        print(f"Turnover: {a.rotation:.0%} of the capital traded at each of {a.rebalances:g} rebalances is {a.turnover:.1f}x a year.")
    if a.turnover and a.cost_bp:
        cost = a.turnover * a.cost_bp / 1e4
        print(f"Cost: {a.turnover:g}x a year at {a.cost_bp:g} bp is {cost:.2%} of capital a year.")
        if a.vol_target:
            print(f"Budget: at {a.vol_target:.0%} volatility, a gross Sharpe of at least {2 * cost / a.vol_target:.2f} keeps costs under half the edge.")


if __name__ == "__main__":
    main()
