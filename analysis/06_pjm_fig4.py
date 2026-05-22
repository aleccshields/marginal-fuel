"""
Zero Margin -- Figure 4
Nuclear capacity market revenue at selected PJM BRA clearing prices
Converted to $/MWh at 92% capacity factor (8,059 hours/year)

Formula: revenue ($/MWh) = clearing_price ($/MW-day) x 365 / 8,059

Key reference prices:
  $28.92  -- 2024/25 BRA (low era)
  $150.00 -- approximate break-even threshold for existing fleet
  $269.92 -- 2025/26 BRA RTO-wide
  $444.26 -- 2025/26 BRA Dominion Zone

Output:
  posts/figures/fig04_capacity_revenue_conversion.png
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

CF   = 0.92
HRS  = 8760 * CF   # 8,059 hours/year at 92% CF

C = {
    "line":     "#2471a3",
    "markers":  "#c0392b",
    "opex":     "#d4ac0d",
    "ref":      "#aab7b8",
}

# Reference clearing prices and labels
REF_PRICES = {
    "$28.92\n(2024/25 BRA)":      28.92,
    "$150\n(break-even threshold)": 150.00,
    "$269.92\n(2025/26 RTO)":     269.92,
    "$444.26\n(2025/26 Dominion)": 444.26,
}

# Representative nuclear operating cost band ($/MWh)
OPEX_LOW  = 25.0
OPEX_HIGH = 40.0

# Representative 2025 LMP (gas-linked, $/MWh)
LMP = 35.0


def cap_revenue(price_mw_day: float) -> float:
    return price_mw_day * 365 / HRS


def chart_figure4() -> None:
    # Continuous line: capacity revenue across a range of BRA prices
    bra_range = np.linspace(0, 500, 500)
    cap_rev   = bra_range * 365 / HRS
    total_rev = LMP + cap_rev

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.subplots_adjust(bottom=0.16)

    # Total revenue curve (LMP + capacity)
    ax.plot(bra_range, total_rev, color=C["line"], lw=2,
            label=f"Total revenue (LMP ${LMP:.0f}/MWh + capacity)")

    # Capacity-only revenue curve
    ax.plot(bra_range, cap_rev, color=C["line"], lw=1.5, ls="--",
            alpha=0.6, label="Capacity revenue only")

    # Operating cost band
    ax.fill_between(bra_range, OPEX_LOW, OPEX_HIGH,
                    color=C["opex"], alpha=0.15, label="Operating cost range")
    ax.axhline(OPEX_LOW, color=C["opex"], lw=0.8, ls="--")
    ax.axhline(OPEX_HIGH, color=C["opex"], lw=0.8, ls="--")
    ax.text(510, (OPEX_LOW + OPEX_HIGH) / 2,
            f"Opex\n${OPEX_LOW:.0f}–${OPEX_HIGH:.0f}/MWh",
            va="center", fontsize=8, color=C["opex"])

    # Reference price markers
    offsets = {
        "$28.92\n(2024/25 BRA)":       (-30, 18),
        "$150\n(break-even threshold)": (10, 15),
        "$269.92\n(2025/26 RTO)":       (10, 10),
        "$444.26\n(2025/26 Dominion)":  (10, 10),
    }

    for label, price in REF_PRICES.items():
        cr  = cap_revenue(price)
        tr  = LMP + cr
        dx, dy = offsets[label]
        ax.axvline(price, color=C["markers"], lw=0.8, ls=":", alpha=0.7)
        ax.scatter([price], [tr], color=C["markers"], s=60, zorder=5)
        ax.annotate(
            f"${tr:.1f}/MWh",
            xy=(price, tr), xytext=(price + dx, tr + dy),
            fontsize=8, color=C["markers"], ha="left",
            arrowprops=dict(arrowstyle="-", color=C["markers"], lw=0.6),
        )
        # Price label on x-axis
        ax.text(price, -3, f"${price:.0f}", ha="center", fontsize=7.5,
                color=C["markers"], rotation=30)

    ax.set_xlim(-10, 510)
    ax.set_ylim(0, 65)
    ax.set_xlabel("PJM BRA Clearing Price ($/MW-day)", fontsize=11)
    ax.set_ylabel("Revenue ($/MWh)", fontsize=11)
    ax.set_title(
        "Nuclear Revenue at Selected PJM Capacity Prices\n"
        f"Capacity at 92% CF + representative LMP of ${LMP:.0f}/MWh",
        fontsize=12,
    )

    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)

    fig.text(
        0.5, 0.02,
        "Capacity revenue = BRA clearing price x 365 / (8,760 x 0.92). "
        "LMP represents a representative 2025 gas-linked wholesale price; actual LMPs vary by zone and period.",
        ha="center", fontsize=7.5, color="gray",
    )

    path = FIG_DIR / "fig04_capacity_revenue_conversion.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


if __name__ == "__main__":
    print("Generating Figure 4...")
    chart_figure4()
    print("Done. Run from: python analysis/06_pjm_fig4.py")
