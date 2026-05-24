"""
Marginal Fuel -- Series 3 -- Figure 3
Options valuation sensitivity: study deposit as a share of development option value

No external data required. All inputs are stated assumptions drawn from public sources.

Methodology:
  Development option value = PV of developer margin over project life
    = (PPA_price - LCOE) * annual_MWh * PV_annuity_factor

  PV annuity factor at discount rate r over N years = (1 - (1+r)^-N) / r

  Assumptions (base case, 100 MW utility solar in PJM):
    Capacity factor:  25%  (mid-Atlantic utility solar, LBNL Utility-Scale Solar 2024)
    PPA price:        $50/MWh  (LBNL median, PJM 2022-2024 contracts)
    LCOE:             $35/MWh  (Lazard LCOE Analysis 2024, utility solar midpoint)
    Margin:           $15/MWh
    Project life:     20 years
    Discount rate:    7%

  Deposit range reflects pre- and post-Order 2023 estimates from PJM's
  published interconnection procedures (Attachment O, OATT). Verify current
  amounts at pjm.com before citing specific figures.

Output: series3/posts/figures/fig03_options_sensitivity.png

Run: python series3/analysis/08_queue_fig3.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pathlib import Path

FIG_DIR = Path(__file__).parent.parent / "posts" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# --- Project size assumptions (MW) ---
PROJECT_SIZES_MW = [50, 100, 200, 500]

# --- Base case market assumptions ---
CAPACITY_FACTOR = 0.25      # utility solar, mid-Atlantic
PPA_PRICE       = 50.0      # $/MWh, LBNL median PJM 2022-2024
LCOE            = 35.0      # $/MWh, Lazard 2024 midpoint
MARGIN_PER_MWH  = PPA_PRICE - LCOE   # $15/MWh
PROJECT_LIFE    = 20        # years
DISCOUNT_RATE   = 0.07

# --- Deposit scenarios (total study deposits at risk on withdrawal, $000s) ---
DEPOSIT_LABELS = ["$50K", "$100K", "$200K", "$500K", "$1M", "$2M", "$5M"]
DEPOSIT_VALUES = [50_000, 100_000, 200_000, 500_000, 1_000_000, 2_000_000, 5_000_000]


def pv_annuity(r: float, n: int) -> float:
    return (1 - (1 + r) ** -n) / r


def dev_option_value(mw: float) -> float:
    annual_mwh = mw * 8_760 * CAPACITY_FACTOR
    annual_margin = MARGIN_PER_MWH * annual_mwh
    return annual_margin * pv_annuity(DISCOUNT_RATE, PROJECT_LIFE)


def build_table() -> np.ndarray:
    """
    Rows = project sizes, columns = deposit scenarios.
    Cell = deposit / option_value * 100 (percentage).
    """
    option_values = [dev_option_value(mw) for mw in PROJECT_SIZES_MW]
    table = np.zeros((len(PROJECT_SIZES_MW), len(DEPOSIT_VALUES)))
    for i, opt_val in enumerate(option_values):
        for j, deposit in enumerate(DEPOSIT_VALUES):
            table[i, j] = deposit / opt_val * 100
    return table, option_values


def chart(table: np.ndarray, option_values: list) -> None:
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 120,
    })

    fig, ax = plt.subplots(figsize=(11, 5))
    fig.subplots_adjust(bottom=0.26, left=0.18, right=0.96)

    # Cap color scale at 15% so cells near zero show clear contrast
    vmax = 15.0
    cmap = mcolors.LinearSegmentedColormap.from_list(
        "deposit_share",
        ["#eafaf1", "#27ae60", "#e74c3c"],
    )
    im = ax.imshow(table, aspect="auto", cmap=cmap, vmin=0, vmax=vmax)

    # Cell annotations
    for i in range(len(PROJECT_SIZES_MW)):
        for j in range(len(DEPOSIT_VALUES)):
            val = table[i, j]
            text_color = "white" if val > vmax * 0.55 else "#1a1a1a"
            ax.text(j, i, f"{val:.2f}%", ha="center", va="center",
                    fontsize=9, color=text_color, fontweight="bold")

    # Axis labels
    row_labels = [
        f"{mw} MW\n(option ≈ ${opt/1e6:.0f}M)"
        for mw, opt in zip(PROJECT_SIZES_MW, option_values)
    ]
    ax.set_yticks(range(len(PROJECT_SIZES_MW)))
    ax.set_yticklabels(row_labels, fontsize=9)
    ax.set_xticks(range(len(DEPOSIT_LABELS)))
    ax.set_xticklabels(DEPOSIT_LABELS, fontsize=9)

    ax.set_xlabel("Total study deposits at risk on withdrawal", fontsize=10)
    ax.set_ylabel("Project size", fontsize=10)
    ax.set_title(
        "Study Deposit as Share of Development Option Value\n"
        "(utility-scale solar, PJM; $50/MWh PPA, $35/MWh LCOE, 25% CF, 20yr, 7% discount rate)",
        fontsize=10,
    )

    cbar = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.02)
    cbar.set_label("Deposit / option value (%)", fontsize=9)

    fig.text(
        0.5, 0.04,
        "Stated-assumption calculation. PPA price: LBNL Utility-Scale Solar 2024. "
        "LCOE: Lazard 2024. Deposit ranges: PJM Attachment O (verify current amounts at pjm.com).",
        ha="center", fontsize=7.5, color="gray",
    )

    out = FIG_DIR / "fig03_options_sensitivity.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {out}")


if __name__ == "__main__":
    table, option_values = build_table()

    print("Development option values by project size:")
    for mw, val in zip(PROJECT_SIZES_MW, option_values):
        print(f"  {mw} MW: ${val/1e6:.1f}M")

    print("\nDeposit as % of option value:")
    header = f"{'MW':<8}" + "".join(f"{d:>10}" for d in DEPOSIT_LABELS)
    print(header)
    for i, mw in enumerate(PROJECT_SIZES_MW):
        row = f"{mw:<8}" + "".join(f"{table[i,j]:>9.2f}%" for j in range(len(DEPOSIT_VALUES)))
        print(row)

    chart(table, option_values)
    print("\nAssumptions used:")
    print(f"  PPA price:       ${PPA_PRICE}/MWh")
    print(f"  LCOE:            ${LCOE}/MWh")
    print(f"  Margin:          ${MARGIN_PER_MWH}/MWh")
    print(f"  Capacity factor: {CAPACITY_FACTOR:.0%}")
    print(f"  Project life:    {PROJECT_LIFE} years")
    print(f"  Discount rate:   {DISCOUNT_RATE:.0%}")
