# The Price of Scarcity

*In July 2024, PJM Interconnection held the capacity auction for the delivery year beginning June 2025. The clearing price for most of PJM came in at $269.92 per megawatt-day, up from $28.92 the prior year. The Dominion Zone, where Northern Virginia's data centers concentrate, cleared at $444.26 per megawatt-day. A 9.3-fold increase, without a change in how the market operates.*

*This is the third post in Zero Margin. Post 2 showed that the state ZEC programs of 2016-2018 implied a value of roughly $133/kW-year for firm, zero-emission nuclear capacity. The 2025/26 base residual auction cleared at approximately $99/kW-year. Nine years later, through competitive clearing rather than administrative determination, the capacity market settled at a comparable number, after data-center load growth and coal retirements pushed offered supply below PJM's reserve requirement.*

---

## How PJM prices capacity

PJM's Reliability Pricing Model procures generation capacity three years ahead of delivery through annual Base Residual Auctions. Generators submit offers; load-serving entities submit demand. PJM clears these on a Variable Resource Requirement curve: a downward-sloping demand schedule that grows steep as offered capacity approaches the reserve margin floor.

When capacity is abundant, the VRR curve clears in its flat region at a low price. When the market is short, the clearing moves into the steep region and prices jump. The 2024/25 BRA cleared in the flat region. The 2025/26 BRA cleared in the steep region. The physical quantity balance shifted modestly between one auction and the next; because the VRR curve is nonlinear, the price moved far more than the quantity.

*[Figure 3: PJM Base Residual Auction clearing prices by delivery year, 2021/22 through 2025/26 (RTO-wide and Dominion Zone, $/MW-day)]*

---

## Three drivers

The move from $28.92 to $269.92/MW-day reflects three overlapping pressures, none of them new in isolation, but together large enough to push offered capacity below PJM's reserve requirement for the first time in the 2025/26 auction.

**Data center load growth.** Hyperscaler data centers in Northern Virginia added contracted load faster than the regional grid absorbed it. Dominion Energy contracted approximately 7,000 megawatts of new data center capacity in Virginia in a single year, according to the utility's integrated resource plan filings. Data center demand runs at high utilization around the clock, independent of season or weather. That profile challenges PJM's capacity planning framework. PJM calibrates its reserve margin requirements around peak-event reliability; a data center drawing 90% of nameplate capacity year-round adds persistent baseline load that peak metrics undercount.

The Dominion Zone premium makes the localization explicit. The zone cleared at $444.26/MW-day, $174.34 above the RTO-wide price. Transmission constraints limit power imports into Northern Virginia's footprint. When local supply falls short of local demand, the LDA constraint traps scarcity inside the zone and produces a premium the RTO-wide market cannot arbitrage away.

**Accelerating coal retirements.** Coal plants exit as they age past their economic recovery horizon and face rising compliance costs. Homer City Generating Station in western Pennsylvania, 1,884 megawatts, retired in December 2023. Retirements across Ohio, Maryland, and Virginia continued through 2024 and into 2025. Each exit removes megawatts that will not return; plant closure is irreversible in a way dispatch decisions are not. The PJM planning stack shrinks as coal leaves, and new entry has arrived more slowly than coal has left.

**Interconnection queue failure.** PJM's interconnection queue holds hundreds of gigawatts of proposed projects, most of which will not complete. Completion rates for queued projects run well below 50%, and those that do complete take five to seven years from application to commercial operation. FERC issued Order 2023 in July 2023, reforming the cluster study process to reduce the backlog, but that reform produces capacity in the mid-2030s, not the mid-2020s. New supply could not close a near-term shortfall in time for the 2025/26 auction.

One structural factor amplified all three. Following FERC's reversal of its expanded Minimum Offer Price Rule, PJM's 2022 MOPR reform allowed state-subsidized resources, including ZEC-backed nuclear and renewable capacity, to offer at their net cost after subsidy. This compressed 2024/25 clearing prices by letting those resources enter at lower offers. The 2025/26 spike showed that even with subsidized resources clearing, offered capacity fell short of the reserve requirement.

---

## The arithmetic of $269.92

The capacity clearing price converts directly into per-megawatt-hour nuclear revenue.

At $269.92/MW-day and a nuclear capacity factor of 92%:

$269.92 × 365 / 8,059 hours = **$12.22/MWh**

A nuclear plant in PJM earning a 2025 gas-linked LMP of roughly $30 to $40/MWh collects $42 to $52/MWh in combined energy and capacity revenue. Against operating costs of $25 to $40/MWh depending on the plant's age and configuration, most existing PJM nuclear plants now operate at or near break-even without state support. This is a shift from 2015 to 2018, when the same arithmetic produced an $8 to $18/MWh deficit at Clinton Power Station.

*[Figure 4: Nuclear capacity market revenue at selected PJM BRA clearing prices, converted to $/MWh at 92% capacity factor]*

**Comparison to ZEC-implied values.** Post 2 calculated that Illinois, by paying $16.50/MWh through FEJA, implied a value of roughly $133/kW-year for firm zero-emission capacity ($16.50 × 8,059 = $132,974/MW-year = $133/kW-year). The 2025/26 BRA cleared at $99/kW-year ($269.92 × 365 / 1,000 = $98.52/kW-year, roughly $99/kW-year). The capacity market's number is approximately 74% of what Illinois paid administratively, reached through competitive clearing rather than cost-of-service determination.

That convergence does not settle whether ZEC programs were cost-effective at the time. States paid ratepayers roughly $1 billion per year to retain capacity the wholesale market priced near zero. Whether those payments captured a genuine option value on capacity that would have been unrecoverable if lost, or anticipated a correction the market would eventually reach, remains a distributional question the capacity price cannot resolve. What the 2025/26 BRA confirms is that ZEC programs were not pricing nuclear's value arbitrarily high.

---

## Is the correction durable?

The durability of the 2025/26 clearing price turns on whether the forces that produced it are temporary or structural.

Coal retirements are irreversible. Demolished plants do not return to service. Data center commitments run 15 to 20 years and are backed by signed contracts. New supply from the interconnection queue, even under FERC Order 2023's accelerated timeline, takes roughly half a decade to reach commercial operation. The nuclear plants operating in PJM today are likely still operating in 2030; no new large-scale nuclear can enter the market before then. The physical conditions that produced the 2025/26 price don't reverse in one or two auction cycles.

The counterarguments are real but slower-acting. Grid-scale battery storage is entering PJM's capacity market in growing volumes. Storage provides capacity credit during peak hours, and if battery penetration accelerates, offered capacity rises and the VRR clearing moves back toward the flat portion. Data center load forecasts have historically outpaced realized buildout; contracted load doesn't always become operational load on schedule. PJM and FERC can also adjust VRR curve parameters in ways that dampen future price spikes without resolving the underlying physical shortfall.

The structural case is stronger through 2027 and 2028. Whether the correction holds into the 2030s depends on how fast storage and new supply enter relative to continued retirements and load growth. For existing nuclear economics, the relevant threshold isn't whether capacity prices stay exactly at $269.92. It's whether they stay above approximately $150/MW-day, the level at which capacity revenue combined with LMP covers operating costs for most plants in the fleet.

At $150/MW-day: $150 × 365 / 8,059 = **$6.79/MWh** in capacity revenue. Added to an LMP of $25/MWh, total revenue is $31.79/MWh, at the low end of operating cost ranges. At $269.92, total revenue reaches $42 to $52/MWh, above break-even for most existing plants. At $28.92, capacity revenue is $1.31/MWh; combined with a low-gas-era LMP of $22 to $25/MWh, total revenue falls to $23 to $26/MWh, the same territory that drove the 2015-2019 retirement wave.

---

## What the correction doesn't solve

The capacity market correction improves the economics of existing nuclear. It does not make new nuclear financeable from market revenue alone.

At $269.92/MW-day capacity plus LMP of $35/MWh, total market revenue for a nuclear plant in PJM is approximately $47/MWh. Lazard's Levelized Cost of Energy analysis places unsubsidized new large-scale nuclear in the United States at roughly $100 to $200/MWh, depending on capital cost assumptions and financing terms. Market revenue covers one-quarter to one-half of new-build LCOE at current capacity prices. The gap has narrowed since the retirement wave, but it hasn't closed.

Closing that gap requires three simultaneous revenue streams: capacity market revenue, the IRA's Section 45U nuclear production tax credit, and corporate PPAs priced at a premium to spot. The Crane Clean Energy Center (Three Mile Island Unit 1 restart) proceeds because Constellation assembled all three simultaneously: capacity auction revenue, Section 45U support, and a 20-year Microsoft PPA well above spot. None of those three streams individually made the project viable; the combination did.

Post 4 examines the hyperscaler PPA deals directly: what the Microsoft and Amazon agreements reveal about how large corporate buyers price firm, 24/7, carbon-free power, and whether demand from that buyer class is large enough to serve as the primary financing mechanism for the next wave of nuclear capacity.

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**PJM capacity auction results**
- PJM 2025/26 Base Residual Auction: $269.92/MW-day RTO-wide, $444.26/MW-day Dominion Zone (July 2024): S&P Global Market Intelligence, July 30, 2024; [PJM 2025/26 BRA Report](https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2025-2026/2025-2026-base-residual-auction-report.pdf)
- PJM 2024/25 Base Residual Auction: $28.92/MW-day (January 2023): S&P Global Market Intelligence; [PJM RPM auction results](https://www.pjm.com/markets-and-operations/rpm)
- PJM Reliability Pricing Model overview and VRR curve mechanics: [PJM RPM documentation](https://www.pjm.com/markets-and-operations/rpm)

**Load growth**
- Dominion Energy data center contracted load (~7,000 MW): Dominion Energy Integrated Resource Plan filings with the Virginia State Corporation Commission; [Virginia SCC utilities](https://www.scc.virginia.gov/pages/Electricity)
- PJM 2024 Load Forecast Report: [PJM load forecast](https://www.pjm.com/planning/resource-adequacy-planning/load-forecast)

**Coal retirements**
- Homer City Generating Station retirement (December 2023, 1,884 MW): [EIA Preliminary Monthly Electric Generator Inventory](https://www.eia.gov/electricity/data/eia860m/)
- PJM generator deactivation notices: [PJM planning and services](https://www.pjm.com/planning)

**Interconnection queue and FERC reform**
- FERC Order 2023, generator interconnection reform (July 28, 2023): FERC Docket No. RM21-17-000 (FERC.gov; order available via FERC eLibrary search)
- PJM interconnection queue statistics: [PJM generator interconnection queue](https://www.pjm.com/planning/new-services-queue/interconnection-queues)

**MOPR reform**
- FERC expanded MOPR (Order 872, December 2019) and subsequent reversal (2022): FERC Docket No. EL16-49-000

**New nuclear economics**
- Lazard Levelized Cost of Energy Analysis (unsubsidized new nuclear, ~$100–$200/MWh): [Lazard LCOE research](https://www.lazard.com/research/)
- Crane Clean Energy Center capex ($1.6B, 835 MW) and Microsoft PPA: [Constellation Energy press release](https://www.constellationenergy.com/news/2024/Constellation-to-Launch-Crane-Clean-Energy-Center-Restoring-Jobs-and-Carbon-Free-Power-to-The-Grid.html)

**IRA nuclear production tax credit**
- Section 45U zero-emission nuclear power production credit: [IRA Section 13105 tracker](https://iratracker.org/programs/ira-section-13105-zero-emission-nuclear-power-production-tax-credit/)

---

*Zero Margin examines the economics of firm, carbon-free power in a gas-priced electricity market.*
