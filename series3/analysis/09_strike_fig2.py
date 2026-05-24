"""
Marginal Fuel -- Series 3 -- Post 9 -- Figure 2
Net option payoff vs. network upgrade cost assignment

No external data required. Extends the option valuation framework from Post 8.

Methodology:
  Development option value (same as Post 8 base case):
    = (PPA - LCOE) * annual_MWh * PV_annuity_factor

  Net payoff = development option value - upgrade cost assignment
    Positive = developer exercises (proceeds to interconnection agreement)
    Negative = developer withdraws

  Break-even upgrade cost = development option value (net payoff = 0)

Assumptions (100 MW utility solar in PJM, consistent with Post 8):
  Capacity factor:  25%
  PPA price:        $50/MWh
  LCOE:             $35/MWh
  Project life:     20 years
  Discount rate:    7%

Upgrade cost range: $0 to $200M, reflecting observed PJM distribution.
Published analyses (Brattle Group, FERC Order 2023 record) document
upgrade cost assignments spanning <$1M to >$500M for similar-sized projects.

Output: series3/posts/figures/fig09_02_strike_price.png

Run from repo root: python series3/analysis/09_strike_fig2.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from pathlib import Path

FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Base case assumptions (consistent with Post 8)
CAPACITY_FACTOR = 0.25
PPA_PRICE       = 50.0   # $/MWh
LCOE            = 35.0   # $/MWh
PROJECT_LIFE    = 20
DISCOUNT_RATE   = 0.07

PROJECT_SIZES_MW = [50, 100, 200, 500]

# Upgrade cost range ($M)
UPGRADE_COSTS_M = np.linspace(0, 200, 500)


def pv_annuity(r: float, n: int) -> float:
    return (1 - (1 + r) ** -n) / r


def dev_option_value(mw: float) -> float:
    annual_mwh    = mw * 8_760 * CAPACITY_FACTOR
    annual_margin = (PPA_PRICE - LCOE) * annual_mwh
    return annual_margin * pv_annuity(DISCOUNT_RATE, PROJECT_LIFE)


def chart() -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.subplots_adjust(bottom=0.18)

    colors = ["#2471a3", "#27ae60", "#e67e22", "#c0392b"]

    option_values = {}
    for mw, color in zip(PROJECT_SIZES_MW, colors):
        opt_val = dev_option_value(mw)
        option_values[mw] = opt_val
        net_payoff = (opt_val - UPGRADE_COSTS_M * 1e6) / 1e6   # in $M

        breakeven = opt_val / 1e6
        label = f"{mw} MW  (option ≈ ${opt_val/1e6:.0f}M)"
        ax.plot(UPGRADE_COSTS_M, net_payoff, color=color, lw=2, label=label)

        # Mark break-even
        ax.axvline(breakeven, color=color, lw=0.8, ls=":", alpha=0.6)
        ax.text(breakeven + 1, -28 + PROJECT_SIZES_MW.index(mw) * 7,
                f"${breakeven:.0f}M", fontsize=8, color=color)

    # Zero line
    ax.axhline(0, color="#333", lw=1.2)
    ax.fill_between(UPGRADE_COSTS_M, 0, 300, alpha=0.05, color="#27ae60")
    ax.fill_between(UPGRADE_COSTS_M, -300, 0, alpha=0.05, color="#c0392b")

    ax.text(195, 8, "Proceed", ha="right", fontsize=9, color="#27ae60", style="italic")
    ax.text(195, -8, "Withdraw", ha="right", fontsize=9, color="#c0392b", style="italic")

    ax.set_xlabel("Network upgrade cost assignment ($M)", fontsize=11)
    ax.set_ylabel("Net option payoff ($M)", fontsize=11)
    ax.set_title(
        "Net Option Payoff vs. Network Upgrade Cost Assignment\n"
        "(utility-scale solar, PJM; $50/MWh PPA, $35/MWh LCOE, 25% CF, 20yr, 7% discount rate)",
        fontsize=10,
    )
    ax.set_xlim(0, 200)
    ax.set_ylim(-100, 180)
    ax.legend(fontsize=9, framealpha=0.9, loc="upper right")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}M"))
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${v:.0f}M"))

    fig.text(
        0.5, 0.03,
        "Stated-assumption calculation. Net payoff = development option value minus upgrade cost. "
        "Break-even = project-size-specific option value. "
        "Assumptions consistent with Post 8 (LBNL Utility-Scale Solar 2024, Lazard LCOE 2024).",
        ha="center", fontsize=7.5, color="gray",
    )

    out = FIG_DIR / "fig09_02_strike_price.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    print("Development option values by project size:")
    for mw in PROJECT_SIZES_MW:
        opt = dev_option_value(mw)
        print(f"  {mw} MW: ${opt/1e6:.1f}M  (break-even upgrade cost: ${opt/1e6:.1f}M)")

    chart()

    print(f"\nAssumptions:")
    print(f"  PPA:    ${PPA_PRICE}/MWh")
    print(f"  LCOE:   ${LCOE}/MWh")
    print(f"  Margin: ${PPA_PRICE - LCOE}/MWh")
    print(f"  CF:     {CAPACITY_FACTOR:.0%}, Life: {PROJECT_LIFE}yr, Discount: {DISCOUNT_RATE:.0%}")
