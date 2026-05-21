# Marginal Fuel

Energy markets, regulation, and the economics of the grid.

A Substack-first research project analyzing how natural gas pipeline constraints transmit into electricity prices in data-center-heavy markets. Written as a three-post series; code and data pipeline are fully reproducible from free public sources.

## Structure

```
analysis/
  01_fetch_data.py         — download Henry Hub (FRED) and PJM Dominion Zone LMPs (EIA)
  02_build_panel.py        — merge into weekly panel, compute first differences and logs
  03_regression_charts.py  — four regression models + four publication charts

posts/
  01_ai_runs_on_gas.md     — Post 1: explainer (the stack, Transco, the basis spread)
  figures/                 — generated charts (gitignored)

data/                      — downloaded CSVs (gitignored)
```

## Data sources (all free, no cost)

| Source | Data | Access |
|--------|------|--------|
| FRED API | Henry Hub daily spot price (series: DHHNGSP) | Free key at fred.stlouisfed.org |
| EIA wholesale markets | PJM Dominion Zone day-ahead LMPs + congestion | Annual CSVs, no auth required |

## Setup

```bash
pip install pandas numpy matplotlib statsmodels requests openpyxl
```

Get a free FRED API key at https://fred.stlouisfed.org/docs/api/api_key.html then set it as an environment variable:

```bash
export FRED_API_KEY=your_key_here
# optional, for Transco Zone 6 basis spread data:
export EIA_API_KEY=your_key_here
```

Then run the pipeline in order:

```bash
python analysis/01_fetch_data.py
python analysis/02_build_panel.py
python analysis/03_regression_charts.py
```

Charts are saved to `posts/figures/`. The regression table prints to stdout.

## Regression results (238 weeks, Sept 2020 – June 2025)

| Model | Specification | Key coefficient | R² |
|-------|--------------|-----------------|-----|
| M1 | d(LMP) ~ d(HH) + seasonal | **5.61*** $/MWh per $/MMBtu | 0.28 |
| M2 | d(Congestion) ~ d(HH) + seasonal | 0.15 (n.s.) | 0.01 |
| M3 | d(LMP) ~ d(HH) × post-AI + seasonal | pre: 6.18***, interaction: -4.04 (n.s.) | 0.28 |
| M4 | log(LMP) ~ log(HH) + trend + seasonal | elasticity: **0.89***, trend: **+9.7%/yr*** | 0.73 |

HAC standard errors (Newey-West, 4 lags). \* p<.10 \*\* p<.05 \*\*\* p<.01

The AI-era demand shock shows up as a level shift in LMPs (the year trend in M4), not as stronger gas price pass-through. That distinction matters for both investment and regulatory analysis.

## Series outline

1. **AI Runs on Gas** — the data center energy stack, Transco constraints, and the basis spread
2. **The Basis Spread That Moves Electricity Prices** — price transmission regression and structural break test
3. **Why FERC Certificate Policy Is Now a Data Center Issue** — regulatory constraint analysis
