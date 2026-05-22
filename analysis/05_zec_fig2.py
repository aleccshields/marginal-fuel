"""
Zero Margin -- Figure 2
Nuclear revenue stack vs. operating cost: energy, capacity, and ZEC
for each state ZEC program, 2016-2018 representative values

Revenue inputs derived from post arithmetic:
  Energy:   mid-range 2016 LMP, $22/MWh (low-gas era, similar across MISO/NYISO/PJM zones)
  Capacity: MISO Zone 4    $0.14/MWh  ($3/MW-day x 365 / 8,059 hr at 92% CF)
            NYISO Zones C/E $0.37/MWh ($3,000/MW-yr / 8,059 hr at 92% CF)
            PJM RTO         $4.53/MWh  ($100/MW-day x 365 / 8,059 hr at 92% CF)
  ZEC:      IL $16.50, NY ~$17, NJ $10/MWh (from state program orders)

Operating cost ranges ($/MWh):
  Illinois (Clinton, single-unit):    $30-40  per Exelon retirement notice and FEJA testimony
  New York (Nine Mile Pt., multi-unit): $25-35  per NY PSC independent cost study estimates
  New Jersey (Salem, multi-unit):     $28-38  per PSEG ZEC petition to NJ BPU

Output:
  posts/figures/fig02_revenue_stack.png
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
    "energy":   "#2471a3",
    "capacity": "#1a9850",
    "zec":      "#d4ac0d",
    "opex":     "#c0392b",
}

LABELS = ["Illinois\n(Clinton)", "New York\n(Nine Mile Pt.)", "New Jersey\n(Salem)"]

energy   = np.array([22.00, 22.00, 22.00])
capacity = np.array([ 0.14,  0.37,  4.53])
zec      = np.array([16.50, 17.00, 10.00])

opex_low  = np.array([30.0, 25.0, 28.0])
opex_high = np.array([40.0, 35.0, 38.0])


def chart_figure2() -> None:
    x = np.arange(len(LABELS))
    width = 0.45

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.subplots_adjust(bottom=0.14)

    # Stacked revenue bars
    ax.bar(x, energy,   width, label="Energy (LMP)",    color=C["energy"],   alpha=0.85)
    ax.bar(x, capacity, width, bottom=energy,           label="Capacity market", color=C["capacity"], alpha=0.85)
    ax.bar(x, zec,      width, bottom=energy + capacity, label="ZEC payment", color=C["zec"], alpha=0.85)

    # Operating cost range: shaded band + dashed boundary lines per state
    for i in range(len(LABELS)):
        left  = x[i] - width / 2
        right = x[i] + width / 2
        ax.fill_between(
            [left, right], opex_low[i], opex_high[i],
            color=C["opex"], alpha=0.18, linewidth=0, zorder=3,
        )
        for y_val in (opex_low[i], opex_high[i]):
            ax.plot([left, right], [y_val, y_val],
                    color=C["opex"], lw=1.3, ls="--", zorder=4)

    # Label total revenue above each bar
    for i in range(len(LABELS)):
        total = energy[i] + capacity[i] + zec[i]
        ax.text(x[i], total + 1.5, f"${total:.1f}/MWh",
                ha="center", va="bottom", fontsize=9, fontweight="bold")

    # Label operating cost band for the first state only
    mid_opex_0 = (opex_low[0] + opex_high[0]) / 2
    ax.annotate(
        "Operating\ncost range",
        xy=(x[0] - width / 2, mid_opex_0),
        xytext=(x[0] - width / 2 - 0.55, mid_opex_0),
        fontsize=8.5, color=C["opex"], va="center", ha="right",
        arrowprops=dict(arrowstyle="-", color=C["opex"], lw=0.8),
    )

    ax.set_xticks(x)
    ax.set_xticklabels(LABELS, fontsize=11)
    ax.set_ylabel("$/MWh", fontsize=11)
    ax.set_ylim(0, 52)
    ax.set_title(
        "Nuclear Revenue Stack vs. Operating Cost by State ZEC Program, 2016–2018",
        fontsize=12,
    )

    legend_patches = [
        mpatches.Patch(color=C["energy"],   alpha=0.85, label="Energy (LMP)"),
        mpatches.Patch(color=C["capacity"], alpha=0.85, label="Capacity market"),
        mpatches.Patch(color=C["zec"],      alpha=0.85, label="ZEC payment"),
        mpatches.Patch(color=C["opex"],     alpha=0.25, label="Operating cost range"),
    ]
    ax.legend(handles=legend_patches, loc="upper right", fontsize=9, framealpha=0.9)

    fig.text(
        0.5, 0.02,
        "Sources: MISO/NYISO/PJM capacity auction data; EIA nuclear capacity factors; "
        "state ZEC program orders (IL FEJA, NY CES, NJ S-2313).",
        ha="center", fontsize=8, color="gray",
    )

    path = FIG_DIR / "fig02_revenue_stack.png"
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path.name}")


if __name__ == "__main__":
    print("Generating Figure 2...")
    chart_figure2()
    print("Done. Run from: python analysis/05_zec_fig2.py")
