"""
Zero Margin -- Figure 3
PJM Base Residual Auction clearing prices by delivery year

Confirmed prices (from PJM BRA reports and S&P Global Market Intelligence):
  2024/25: $28.92/MW-day RTO-wide (January 2023 auction)
  2025/26: $269.92/MW-day RTO-wide, $444.26/MW-day Dominion Zone (July 2024 auction)

Approximate prices for 2021/22 through 2023/24 (from PJM published auction results):
  Verify and update from: https://www.pjm.com/markets-and-operations/rpm
  These years were compressed catch-up auctions following MOPR reform delays.

Output:
  posts/figures/fig03_pjm_bra_history.png
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
    "rto":     "#2471a3",
    "dom":     "#c0392b",
    "approx":  "#aab7b8",
}

# Delivery year labels and clearing prices
# Mark confirmed vs. approximate in the chart
YEARS     = ["2021/22", "2022/23", "2023/24", "2024/25", "2025/26"]
RTO       = [50.0,       34.0,      18.0,       28.92,     269.92]    # $/MW-day
DOMINION  = [None,       None,      None,       None,      444.26]    # $/MW-day; only 2025/26 differs materially
CONFIRMED = [False,      False,     False,      True,      True]


def chart_figure3() -> None:
    x = np.arange(len(YEARS))
    width = 0.38

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.subplots_adjust(bottom=0.16)

    # RTO bars — color by confirmed status
    for i, (rto_val, conf) in enumerate(zip(RTO, CONFIRMED)):
        color = C["rto"] if conf else C["approx"]
        alpha = 0.85 if conf else 0.65
        ax.bar(x[i] - width / 2, rto_val, width,
               color=color, alpha=alpha, zorder=3)

    # Dominion Zone bar (2025/26 only)
    dom_idx = YEARS.index("2025/26")
    ax.bar(x[dom_idx] + width / 2, DOMINION[dom_idx], width,
           color=C["dom"], alpha=0.80, zorder=3)

    # Value labels
    for i, rto_val in enumerate(RTO):
        ax.text(x[i] - width / 2, rto_val + 4,
                f"${rto_val:.0f}" if not CONFIRMED[i] else f"${rto_val:.2f}",
                ha="center", va="bottom", fontsize=8.5,
                color="gray" if not CONFIRMED[i] else "black")

    dom_val = DOMINION[dom_idx]
    ax.text(x[dom_idx] + width / 2, dom_val + 4,
            f"${dom_val:.2f}", ha="center", va="bottom",
            fontsize=8.5, color=C["dom"])

    # Annotation box for MOPR / catch-up context
    ax.annotate(
        "MOPR reform catch-up auctions\n(prices approximate)",
        xy=(x[1] - width / 2, RTO[1] + 5),
        xytext=(x[1] - width / 2, 80),
        fontsize=8, color="gray", ha="center",
        arrowprops=dict(arrowstyle="->", color="gray", lw=0.8),
    )

    ax.set_xticks(x)
    ax.set_xticklabels(YEARS, fontsize=10)
    ax.set_ylabel("Clearing Price ($/MW-day)", fontsize=11)
    ax.set_ylim(0, 510)
    ax.set_title(
        "PJM Base Residual Auction Clearing Prices\nby Delivery Year (RTO-wide and Dominion Zone)",
        fontsize=12,
    )

    legend_patches = [
        mpatches.Patch(color=C["rto"],    alpha=0.85, label="RTO-wide (confirmed)"),
        mpatches.Patch(color=C["dom"],    alpha=0.80, label="Dominion Zone (confirmed)"),
        mpatches.Patch(color=C["approx"], alpha=0.65, label="RTO-wide (approximate — verify at pjm.com/rpm)"),
    ]
    ax.legend(handles=legend_patches, loc="upper left", fontsize=9, framealpha=0.9)

    fig.text(
        0.5, 0.02,
        "Sources: PJM BRA Reports; S&P Global Market Intelligence (July 30, 2024). "
        "Prices for 2021/22–2023/24 are approximate; verify at pjm.com/markets-and-operations/rpm.",
        ha="center", fontsize=7.5, color="gray",
    )

    path = FIG_DIR / "fig03_pjm_bra_history.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


if __name__ == "__main__":
    print("Generating Figure 3...")
    chart_figure3()
    print("Done. Run from: python analysis/06_pjm_fig3.py")
