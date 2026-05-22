# The Shadow Price of Firm Power

*In September 2024, Microsoft and Constellation Energy signed a 20-year power purchase agreement covering 835 megawatts from a reactor that had been retired for five years. The price was not disclosed. It rarely is.*

*This is the final post in Zero Margin. Posts 1 through 3 traced how the wholesale electricity market systematically underprices nuclear generation, how state ZEC programs filled part of that gap at ratepayer expense, and how the 2025/26 PJM capacity auction partially corrected the reliability component at $269.92/MW-day. The corporate PPA is the fourth mechanism, pricing what the preceding three don't: not just reliability and zero-emission generation, but price certainty across decades and guaranteed hourly delivery. What buyers commit to pay for those attributes, beyond what the market pays, is the series' final analytical question.*

---

## The PPA landscape

Three hyperscaler deals since 2023 have moved corporate nuclear procurement from aspiration to transaction.

**Microsoft / Crane Clean Energy Center.** Constellation's restart of Three Mile Island Unit 1, 835 megawatts, under a 20-year PPA announced September 20, 2024, five years to the day after the reactor's retirement. Constellation is investing roughly $1.6 billion to refurbish and restart the plant; the Department of Energy added a $1 billion loan in late 2025. The plant targets commercial operation in 2028. Microsoft receives the full output.

**Amazon Web Services / Susquehanna.** Amazon acquired a data center campus adjacent to Talen Energy's Susquehanna Steam Electric Station in Pennsylvania and negotiated to receive power directly from the approximately 2,520-megawatt nuclear plant. FERC rejected the co-location arrangement in spring 2024, finding that nuclear plants cannot exit their PJM capacity obligations by routing output to a behind-the-meter buyer. The deal was restructured; negotiations continued into late 2024 under FERC's emerging standards for co-location at nuclear sites.

**Google / Kairos Power.** Google signed a PPA with Kairos Power for up to 500 megawatts from small modular reactors, with the first unit targeted for 2030 and the remainder by 2035. It is the first major corporate contract for SMR capacity. The Kairos KP-FHR reactor design has not yet reached commercial operation; the deal is a forward commitment contingent on development milestones.

All three buyers share the same commercial constraint. Microsoft, Amazon, and Google each operate under corporate commitments to match their electricity consumption with carbon-free generation on a 24/7 hourly basis, not just on an annual average. Wind and solar satisfy that target in many hours. They cannot in all hours. Nuclear can.

---

## What project economics reveal

The Microsoft PPA price is confidential. Project economics bound what it must be.

Constellation's all-in cost to restart and operate Crane Clean Energy Center:

- Capital expenditure: $1.6 billion (equipment refurbishment, fuel preparation, regulatory re-certification)
- Financing: $1 billion DOE loan at below-market rates; the remainder as equity
- Annual generation at 835 MW and 92% capacity factor: 835 × 8,760 × 0.92 = **6.73 million MWh/year**
- 20-year PPA lifetime output: **134.5 million MWh**

Annual capital service at representative financing terms (10% required return on $600M equity; 5% DOE debt on $1B, 20-year term):

- Equity tranche: $600M × 0.10 / (1 − 1.10^−20) ≈ **$70M/year**
- Debt tranche: $1B × 0.05 / (1 − 1.05^−20) ≈ **$80M/year**
- Total capital service: **~$150M/year**, or **$22/MWh**

Add operating costs for a refurbished single-unit plant: roughly **$28 to $32/MWh**, below Clinton's $30 to $40/MWh range from Post 2, which reflected deferred maintenance before the ZEC era.

Total cost floor: **$50 to $54/MWh**.

Partially offset by:
- IRA Section 45U nuclear PTC: up to $15/MWh, phasing out as LMPs rise
- PJM capacity market revenue: ~$12/MWh at 2025/26 BRA prices

Net cost after subsidies and capacity revenue: **$23 to $27/MWh**, the minimum value Constellation requires from the PPA to recover costs.

Whether the PPA price sits at this floor or substantially above it is unknown from public filings. What is known is that the project required a 20-year commitment from a creditworthy buyer before Constellation would proceed, and that no shorter or cheaper contract produced the same result despite five years of available capacity sitting idle. The excess above cost recovery is the shadow price of attributes the wholesale market won't pay for: two decades of price certainty; 92% capacity factor firm delivery; hourly carbon-free matching without unbundled RECs.

*[Figure 5: Nuclear revenue stack by scenario — LMP, capacity market, IRA 45U, and PPA floor — for 2016 (ZEC era), 2022 (trough), and 2025 (current)]*

---

## The co-location problem

The Amazon/Susquehanna dispute surfaced a structural tension the PPA market hadn't previously had to resolve.

Co-location means a large load physically connects to the output of a nuclear plant's high-voltage switchyard, receiving power before it flows into the regional transmission grid. For the buyer, co-location delivers three things a standard PPA cannot: guaranteed physical delivery regardless of transmission congestion; hourly carbon-free matching tied to actual nuclear output rather than purchased renewable energy certificates; and a direct contractual link between consumption and generation.

FERC's rejection established that nuclear plants cannot achieve co-location by reducing their capacity market obligations proportionally. The reasoning matters for market design. Nuclear plants that clear PJM's capacity market commit to provide reliability services the grid depends on. Routing their output to one behind-the-meter buyer removes those services from the grid, which harms reliability for all other load-serving entities. The co-located buyer captures the firm-delivery premium it wants; the rest of the grid loses what it was counting on.

FERC's subsequent guidance recognized that co-location at nuclear sites can be compatible with grid reliability under specific conditions: the nuclear plant must maintain its full capacity obligations to PJM, and the co-located load may only consume power the plant produces above that committed capacity. In practice, a nuclear plant running at 92% capacity factor has limited unconstrained output available. Buyers seeking the full physical certainty of direct connection may find it incompatible with the capacity obligations that make nuclear plants reliable to the grid in the first place.

The co-location dispute reveals what corporate buyers want: not financial exposure to nuclear economics, but physical delivery. The PPA model as practiced, a financial contract for the unit's output settled against market prices, is a second-best substitute for what Amazon's engineers were trying to build in Pennsylvania.

---

## Four mechanisms, one problem

Zero Margin has traced a single market failure through four successive mechanisms:

| Mechanism | Period | Attribute priced | $/MWh above energy |
|---|---|---|---|
| Wholesale LMP | Continuous | Energy only | $0 |
| State ZEC programs | 2016-2018 | Reliability + carbon-free | $10–17/MWh |
| PJM capacity market | 2025/26 BRA | Reliability (partial) | $12.22/MWh |
| IRA Section 45U | 2024–present | Carbon-free, existing plants | Up to $15/MWh |
| Corporate PPAs | 2023–present | Price certainty + 24/7 CF + firmness | $23–27/MWh floor (estimated) |

No single mechanism prices all five attributes. The ZECs came closest, capturing reliability and carbon-free generation simultaneously, but administratively and at ratepayer expense. The capacity market correction was partial and realized only in favorable auction conditions. The IRA credit is administrative, subject to congressional modification, and structured for existing plants only. Corporate PPAs capture price certainty and hourly delivery, but through bilateral, opaque contracts at a scale that cannot match the size of the problem.

What the progression shows: successive mechanisms have addressed attributes the preceding one missed, each arriving years after the underlying value was demonstrable. Illinois paid $16.50/MWh administratively in 2016 for attributes the capacity market priced at $12.22/MWh in 2025. The capacity market took nine years to reach a comparable number. Corporate buyers committed to 20-year contracts in 2024 for attributes neither the capacity market nor the IRA credit fully captures.

**The temporal firming gap.** PJM has no market for temporal firmness: the value of generation available in every hour, not just when the wind blows or the sun shines. A nuclear plant at 92% capacity factor provides 8,059 hours per year of reliable, predictable output. A wind farm at 35% capacity factor provides 3,066 hours, and not always the hours that load needs. The hourly gap between them is precisely what Microsoft contracted to close with the TMI deal. No wholesale market mechanism prices it. The bilateral PPA is the market of last resort for that gap.

---

## The scale problem

Whether corporate PPAs can serve as the primary financing mechanism for the next wave of nuclear capacity depends on arithmetic.

The Crane Clean Energy Center provides 6.73 million MWh per year. Microsoft's electricity consumption exceeded 24 TWh in 2022 and has grown at roughly 30 percent per year since then, driven by AI workloads. By 2030, Microsoft's own load could approach or exceed the annual generation of the entire Crane facility many times over. Amazon, Google, and Meta face comparable growth trajectories and comparable 24/7 CFE commitments. The U.S. nuclear fleet generates roughly 775 to 800 TWh per year from approximately 95 gigawatts of capacity. If hyperscaler demand for firm, 24/7, carbon-free power continues on its current trajectory, it will exceed what the existing U.S. nuclear fleet could provide even if the entire fleet were under bilateral PPA contracts.

New nuclear could resolve the arithmetic but not on the timeline corporate buyers need. The Google/Kairos deal targets first SMR delivery in 2030 — optimistic given that the reactor design hasn't yet reached commercial operation. Large-scale new nuclear takes 10 to 15 years from licensing to commercial operation under the most favorable regulatory conditions. The bilateral PPA model works for Crane Clean Energy Center specifically because it restarts a reactor whose structure and site are already licensed. That path doesn't repeat once the stock of retired-but-restartable capacity is exhausted.

For greenfield nuclear, the PPA model faces a financing gap that bilateral deals alone can't close. A 20-year corporate PPA at cost-recovery prices can backstop debt financing and reduce the cost of capital. It cannot substitute for equity investment, federal loan support, or regulatory certainty on licensing timelines. The Crane Clean Energy Center required a DOE loan and a Microsoft PPA in combination; neither individually was sufficient.

---

## What a functional market would look like

Each post in this series documented a market failure and the workaround it produced. ZECs were a workaround for a market that wouldn't price carbon-free generation. Capacity market prices were volatile rather than forecastable, requiring a spike to reach values states had determined administratively nine years earlier. The IRA credit is administrative rather than market-derived, and the One Big Beautiful Bill Act of 2025 added restrictions that reduced its universality. Corporate PPAs are bilateral, opaque, and accessible only to counterparties large enough to commit to 20-year obligations.

A wholesale market that priced all five attributes directly would need three structural additions.

**A clean energy standard or carbon price applied to wholesale electricity.** The IRA's 45U credit is a partial approximation: administratively determined, plant-specific, and capped. A per-MWh market signal for zero-emission generation, applied uniformly across the dispatch stack, would price the carbon-free attribute in the hourly clearing price rather than through a separate administrative process.

**A reformed capacity market that compensates for temporal firmness, not just available megawatts.** PJM's capacity market applies Unforced Capacity (UCAP) derating that reduces wind and solar's effective capacity credit below their nameplate rating, reflecting lower availability during peak stress events. But UCAP derating is a probability-weighted average, not a guarantee of hourly delivery. A nuclear plant at 92% capacity factor provides predictable output in every high-demand hour. A wind farm at 35% capacity factor provides its output in hours the wind determines, not hours load needs. UCAP derating adjusts for average availability; it does not price temporal firmness. A capacity product that compensates for guaranteed hourly delivery, not just statistical availability, would capture the attribute that corporate 24/7 CFE commitments are actually trying to procure.

**Active markets for synchronous grid services.** Rotating mass from nuclear and gas turbines stabilizes grid frequency under sudden generation or load changes. Inverter-based resources do not provide this service without additional inverter programming. As wind and solar penetration rises, the value of synchronous inertia from nuclear plants rises with it. PJM and other ISOs are developing ancillary service markets for frequency regulation and inertia, but those markets remain early-stage. The value currently accrues to the grid without compensation to the providers.

Without those three reforms, nuclear plants will continue to be priced through a patchwork of state programs, bilateral contracts, and federal credits. Each mechanism addresses part of the market failure. None addresses it at scale, and none produces the stable, forecastable revenue that project finance for new nuclear construction requires.

---

## Closing

Zero Margin set out to ask whether the electricity market adequately compensates nuclear for reliability, carbon-free generation, and grid inertia. The answer across four posts is: no, and the workarounds reveal the size of the gap.

State ZECs priced nuclear's non-energy attributes at $10 to $17/MWh above market from 2016 to 2018. The capacity market, after nine years and a data-center-driven demand shock, priced reliability at $12.22/MWh in the 2025/26 BRA. The IRA added up to $15/MWh for zero-emission generation in 2024.

For an existing PJM nuclear plant today: LMP of roughly $35/MWh plus $12/MWh capacity plus $15/MWh IRA equals $62/MWh, above operating costs of $25 to $40/MWh for most of the fleet. For the Crane Clean Energy Center restart, the same three streams must clear a cost floor of $50 to $54/MWh all-in; the PPA structure provides the price certainty that makes the project's debt serviceable. Neither outcome generalizes easily: the existing fleet faces the next capacity auction, and the restart model runs out once the stock of retirable-but-restartable capacity is exhausted.

The Three Mile Island plant ran from 1974 to 2019 and earned the gas-set LMP throughout. The market it ran in could not support it. Five years after retirement, one buyer needed exactly what it produced, signed a 20-year contract, and triggered a $2.6 billion restart. The market failed. The bilateral deal filled the gap. Neither outcome is a solution: the first left value unpriced, the second left scale unaddressed.

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**Microsoft / Crane Clean Energy Center**
- 20-year PPA, announced September 20, 2024; $1.6B Constellation capex, 835 MW, 2028 target: [Constellation Energy press release](https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html)
- DOE $1 billion loan (November 2025): DOE Loan Programs Office announcement, November 2025

**Amazon / Talen Energy / Susquehanna**
- Co-location arrangement and FERC rejection (spring 2024): FERC proceedings on nuclear co-location; FERC technical conference on co-location at nuclear facilities (late 2024)
- Talen Energy / Amazon data center campus acquisition: Talen Energy press releases, 2023

**Google / Kairos Power**
- Up to 500 MW SMR PPA, first delivery 2030: [Google sustainability blog](https://blog.google/outreach-initiatives/sustainability/google-kairos-power-nuclear-energy-agreement/)

**24/7 carbon-free energy matching**
- Corporate 24/7 CFE methodology and commitments: [24/7 Carbon-Free Energy Compact](https://gocarbonfree247.com/)

**Nuclear fleet data**
- U.S. nuclear fleet annual generation (~775–800 TWh) and capacity (~95 GW): [EIA Electric Power Annual](https://www.eia.gov/electricity/annual/), Table 3.1
- Nuclear capacity factor (~92%): [EIA Electric Power Monthly](https://www.eia.gov/electricity/monthly/), Table 6.2

**IRA nuclear production tax credit**
- Section 45U zero-emission nuclear power production credit, modified by One Big Beautiful Bill Act of 2025: [IRA Section 13105 tracker](https://iratracker.org/programs/ira-section-13105-zero-emission-nuclear-power-production-tax-credit/)

**PJM capacity market**
- 2025/26 BRA clearing prices, capacity revenue conversion: previously cited in Post 3

**Microsoft electricity consumption**
- 24 TWh in FY2022; AI-driven growth trajectory: Microsoft Environmental Sustainability Report 2023 and 2024, available at microsoft.com/en-us/corporate-responsibility/sustainability/report

**New nuclear costs**
- Lazard Levelized Cost of Energy Analysis: [Lazard LCOE research](https://www.lazard.com/research/)

---

*Zero Margin examines the economics of firm, carbon-free power in a gas-priced electricity market.*
