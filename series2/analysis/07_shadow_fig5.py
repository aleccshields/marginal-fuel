"""
Zero Margin -- Figure 5
Nuclear revenue stack by scenario: LMP, capacity market, state/federal support, and restart cost floor

Three representative scenarios illustrating how revenue has changed across the series:

  2016 (ZEC era, Illinois/Clinton)
    LMP:      $22/MWh (Henry Hub ~$2.60-3.80, MISO low-gas era)
    Capacity: $0.14/MWh (MISO Zone 4, ~$3/MW-day non-manipulated years)
    ZEC:      $16.50/MWh (Illinois FEJA)
    IRA 45U:  $0 (not yet enacted)

  2023-24 (Pre-IRA trough, PJM, no ZEC)
    LMP:      $28/MWh (representative PJM, low-gas year)
    Capacity: $1.31/MWh ($28.92/MW-day, 2024/25 BRA)
    ZEC:      $0 (no ZEC for most PJM plants outside NJ/IL)
    IRA 45U:  $0 (started Jan 1, 2024; not fully reflected here)

  2025 (Current, PJM)
    LMP:      $35/MWh (representative, gas-linked)
    Capacity: $12.22/MWh ($269.92/MW-day, 2025/26 BRA)
    IRA 45U:  $15/MWh (up to; phases out as LMPs rise)

Crane Clean Energy Center restart cost floor: $50-54/MWh (see post for derivation)
Operating cost range (existing plants): $25-40/MWh

Output:
  posts/figures/fig05_revenue_stack_evolution.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 120,
})

C = {
    "lmp":      "#2471a3",
    "capacity": "#1a9850",
    "zec":      "#d4ac0d",
    "ira":      "#8e44ad",
    "opex":     "#c0392b",
    "restart":  "#e67e22",
}

SCENARIOS = ["2016\n(ZEC era,\nIllinois/MISO)", "2023–24\n(Trough,\nPJM)", "2025\n(Current,\nPJM)"]

# Revenue components ($/MWh)
lmp      = np.array([22.00, 28.00, 35.00])
capacity = np.array([ 0.14,  1.31, 12.22])
zec      = np.array([16.50,  0.00,  0.00])
ira      = np.array([ 0.00,  0.00, 15.00])

# Operating cost band (existing plants)
opex_low  = 25.0
opex_high = 40.0

# Crane Clean Energy Center restart cost floor
restart_low  = 50.0
restart_high = 54.0


def chart_figure5() -> None:
    x = np.arange(len(SCENARIOS))
    width = 0.50

    fig, ax = plt.subplots(figsize=(11, 7))
    fig.subplots_adjust(bottom=0.18, left=0.10, right=0.88)

    # Stacked bars
    b_lmp = ax.bar(x, lmp, width, color=C["lmp"],   alpha=0.85, label="Energy (LMP)")
    b_cap = ax.bar(x, capacity, width, bottom=lmp,
                   color=C["capacity"], alpha=0.85, label="Capacity market")
    b_zec = ax.bar(x, zec, width, bottom=lmp + capacity,
                   color=C["zec"], alpha=0.85, label="State ZEC (FEJA)")
    b_ira = ax.bar(x, ira, width, bottom=lmp + capacity + zec,
                   color=C["ira"], alpha=0.85, label="IRA Section 45U")

    # Total revenue labels
    totals = lmp + capacity + zec + ira
    for i, total in enumerate(totals):
        ax.text(x[i], total + 0.8, f"${total:.1f}/MWh",
                ha="center", va="bottom", fontsize=9, fontweight="bold")

    # Operating cost band (across all scenarios)
    ax.fill_between([-0.5, len(SCENARIOS) - 0.5], opex_low, opex_high,
                    color=C["opex"], alpha=0.12, linewidth=0, zorder=0)
    ax.axhline(opex_low,  color=C["opex"], lw=1.0, ls="--", alpha=0.7)
    ax.axhline(opex_high, color=C["opex"], lw=1.0, ls="--", alpha=0.7)
    ax.text(len(SCENARIOS) - 0.5 + 0.08, (opex_low + opex_high) / 2,
            "Existing plant\nopex range\n$25–40/MWh",
            va="center", fontsize=8, color=C["opex"])

    # Restart cost floor band (horizontal, right portion of chart)
    x_start = x[-1] - width / 2 - 0.1
    x_end   = len(SCENARIOS) - 0.5 + 0.06
    ax.fill_between([x_start, x_end], restart_low, restart_high,
                    color=C["restart"], alpha=0.20, linewidth=0, zorder=0)
    ax.plot([x_start, x_end], [restart_low,  restart_low],  color=C["restart"], lw=1.0, ls=":")
    ax.plot([x_start, x_end], [restart_high, restart_high], color=C["restart"], lw=1.0, ls=":")
    ax.text(len(SCENARIOS) - 0.5 + 0.08, (restart_low + restart_high) / 2,
            "Crane restart\ncost floor\n$50–54/MWh",
            va="center", fontsize=8, color=C["restart"])

    ax.set_xticks(x)
    ax.set_xticklabels(SCENARIOS, fontsize=10)
    ax.set_ylabel("Revenue ($/MWh)", fontsize=11)
    ax.set_ylim(0, 75)
    ax.set_xlim(-0.5, len(SCENARIOS) - 0.5 + 0.06)
    ax.set_title(
        "Nuclear Revenue Stack by Scenario: Energy, Capacity, and Support Mechanisms",
        fontsize=12,
    )

    legend_patches = [
        mpatches.Patch(color=C["lmp"],      alpha=0.85, label="Energy (LMP)"),
        mpatches.Patch(color=C["capacity"], alpha=0.85, label="Capacity market"),
        mpatches.Patch(color=C["zec"],      alpha=0.85, label="State ZEC (FEJA, 2016)"),
        mpatches.Patch(color=C["ira"],      alpha=0.85, label="IRA Section 45U (up to $15/MWh)"),
        mpatches.Patch(color=C["opex"],     alpha=0.20, label="Existing plant opex range"),
        mpatches.Patch(color=C["restart"],  alpha=0.25, label="Restart cost floor (Crane/TMI)"),
    ]
    ax.legend(handles=legend_patches, loc="upper left", fontsize=8.5, framealpha=0.9)

    fig.text(
        0.5, 0.04,
        "Sources: MISO/PJM capacity auction data; IL FEJA ($16.50/MWh); "
        "EIA nuclear capacity factors; IRA Section 45U; Constellation Energy disclosures.",
        ha="center", fontsize=7.5, color="gray",
    )

    path = FIG_DIR / "fig05_revenue_stack_evolution.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


if __name__ == "__main__":
    print("Generating Figure 5...")
    chart_figure5()
    print("Done. Run from: python analysis/07_shadow_fig5.py")
