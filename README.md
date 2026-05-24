# Marginal Fuel

Energy markets, regulation, and the economics of the grid.

A Substack research project. Code and data pipelines are fully reproducible from free public sources.

---

## Series 1: Gas to Power (Posts 1–3)

How natural gas pipeline constraints transmit into electricity prices in data-center-heavy markets.

**Posts**
1. **AI Runs on Gas** — the data center energy stack, Transco constraints, and the basis spread
2. **The Basis Spread That Moves Electricity Prices** — price transmission regression and structural break test
3. **Why FERC Certificate Policy Is Now a Data Center Issue** — regulatory constraint analysis

**Regression results (238 weeks, Sept 2020 – June 2025)**

| Model | Specification | Key coefficient | R² |
|-------|--------------|-----------------|-----|
| M1 | d(LMP) ~ d(HH) + seasonal | **5.61*** $/MWh per $/MMBtu | 0.28 |
| M2 | d(Congestion) ~ d(HH) + seasonal | 0.15 (n.s.) | 0.01 |
| M3 | d(LMP) ~ d(HH) × post-AI + seasonal | pre: 6.18\*\*\*, interaction: -4.04 (n.s.) | 0.28 |
| M4 | log(LMP) ~ log(HH) + trend + seasonal | elasticity: **0.89\*\*\***, trend: **+9.7%/yr\*\*\*** | 0.73 |

HAC standard errors (Newey-West, 4 lags). \* p<.10 \*\* p<.05 \*\*\* p<.01

The AI-era demand shock shows up as a level shift in LMPs (the year trend in M4), not as stronger gas price pass-through.

---

## Series 2: The Queue (Posts 8–10)

The financial and regulatory mechanics of U.S. generator interconnection — why the queue is broken and what it would take to fix it.

**Posts**
8. **The Option Nobody Priced** — interconnection queue positions as call options; study deposits priced at under 1% of development option value; rational speculative flooding; FERC Order 2023 analysis
9. **The Strike Price** — network upgrade costs as floating-strike barrier options; 44.8% of exits at System Impact Study; cascade instability; ERCOT CREZ structural contrast
10. **The Repair** — reform scorecard; Order 2023 accomplishments and limits; 2024 entry drop (38%); value-indexed deposits, early cost disclosure, and Order 1920 as the three-part repair

**Key numbers (LBNL Queued Up, data through 2024)**

| Year | GW in queue | Installed capacity | Ratio |
|------|------------|-------------------|-------|
| 2010 | 1,288 GW | 1,039 GW | 1.2x |
| 2016 | 1,681 GW | 1,087 GW | 1.5x |
| 2020 | 2,376 GW | 1,125 GW | 2.1x |
| 2024 | 4,390 GW | 1,260 GW | 3.5x |

Withdrawal rate by entry cohort: 74% (2015) → 96% (2020). Of projects entering 2000–2018, 85% withdrew before commercial operation.

---

## Repository structure

```
series1/
  analysis/
    01_fetch_data.py         — download Henry Hub (FRED) and PJM Dominion Zone LMPs (EIA)
    02_build_panel.py        — merge into weekly panel, compute first differences and logs
    03_regression_charts.py  — four regression models + four publication charts
  posts/
    01_ai_runs_on_gas.md
    02_the_regression.md
    03_certificate_policy.md
    figures/                 — generated charts (gitignored)

series2/
  analysis/
    08_queue_fig1.py         — Figure 1: queue GW vs. installed capacity by year (LBNL)
    08_queue_fig2.py         — Figure 2: withdrawal rate by entry year (LBNL)
    08_queue_fig3.py         — Figure 3: deposit vs. option value sensitivity table
    09_strike_fig1.py        — Figure 1: withdrawal phase distribution (LBNL)
    09_strike_fig2.py        — Figure 2: net option payoff vs. upgrade cost
    10_repair_fig1.py        — Figure 1: withdrawal rate trend by cohort (LBNL)
    10_repair_fig2.py        — Figure 2: queue entry volume with Order 2023 timeline (LBNL)
    10_repair_fig3.py        — Figure 3: reform scorecard matrix
  posts/
    08_the_option_nobody_priced.md
    09_the_strike_price.md
    10_the_repair.md
    figures/                 — generated charts (gitignored)

data/                        — downloaded files (gitignored)
```

---

## Data sources

| Source | Data | Access |
|--------|------|--------|
| FRED API | Henry Hub daily spot price (series: DHHNGSP) | Free key at fred.stlouisfed.org |
| EIA wholesale markets | PJM Dominion Zone day-ahead LMPs + congestion | Annual CSVs, no auth required |
| LBNL Queued Up | U.S. generator interconnection queue, project-level | Free download at emp.lbl.gov/publications/queued-characteristics-power-plants |

---

## Setup

```bash
pip install pandas numpy matplotlib statsmodels requests openpyxl
```

Set API keys as environment variables (never hardcode):

```bash
export FRED_API_KEY=your_key_here
export EIA_API_KEY=your_key_here   # optional, for Transco Zone 6 basis spread data
```

Run Series 1 pipeline in order:

```bash
python series1/analysis/01_fetch_data.py
python series1/analysis/02_build_panel.py
python series1/analysis/03_regression_charts.py
```

Series 2 figures run independently (download LBNL data file first — see data sources above):

```bash
python series2/analysis/08_queue_fig1.py     # requires LBNL data file in data/
python series2/analysis/08_queue_fig2.py     # requires LBNL data file in data/
python series2/analysis/08_queue_fig3.py     # no external data required
python series2/analysis/09_strike_fig1.py    # requires LBNL data file in data/
python series2/analysis/09_strike_fig2.py    # no external data required
python series2/analysis/10_repair_fig1.py    # requires LBNL data file in data/
python series2/analysis/10_repair_fig2.py    # requires LBNL data file in data/
python series2/analysis/10_repair_fig3.py    # no external data required
```

Charts save to `seriesN/posts/figures/`.
