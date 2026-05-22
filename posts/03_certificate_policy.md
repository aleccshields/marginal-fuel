# Certificate Policy as Price Floor

*The pipeline that would relieve mid-Atlantic gas supply constraints needs a FERC certificate, a state water quality certification, and a financing structure that can survive years of regulatory proceedings. Several candidates have been trying for a decade. Northern Virginia's data center load keeps adding megawatts.*

---

Posts 1 and 2 established the empirical case: gas prices set electricity prices in PJM, Transco pipeline constraints amplify that link when capacity binds, and Dominion Zone LMPs have risen roughly 10% per year in nominal terms beyond what fuel costs alone explain. Post 2 noted that the year trend in M4 picks up multiple contributors: coal retirements, transmission constraints, general cost inflation, and demand growth from various sources.

This post covers the supply-side constraint most traceable to a specific regulatory decision: the process governing new interstate gas pipeline capacity. It runs through two federal statutes.

---

## Section 7 and the certificate requirement

The Natural Gas Act of 1938 gives FERC jurisdiction over interstate gas transportation. [Section 7(c)](https://www.law.cornell.edu/uscode/text/15/717f) requires any company constructing or operating an interstate natural gas pipeline to obtain a "certificate of public convenience and necessity" from FERC. No certificate, no pipe. This applies to new construction, compression expansions, and loop lines added alongside existing right of way.

The certificate requirement was designed to prevent duplicative infrastructure and protect landowners from unnecessary condemnation. The secondary consequence: every significant capacity addition must pass through a federal regulatory proceeding before construction begins. That proceeding involves competing interventions, environmental review under NEPA, and commissioners appointed by the President and confirmed by the Senate.

For two decades, FERC evaluated certificate applications under a framework it established in a 1999 Policy Statement (Docket PL99-3-000). The core test weighed market need against adverse impacts on landowners, communities, and the environment. Developers demonstrated market need by showing firm, long-term gas purchase agreements from creditworthy shippers. If utilities and industrial buyers had signed contracts, FERC treated that as sufficient evidence the capacity served a public purpose. Projects that cleared this bar were generally approved, though often after years of proceedings.

FERC changed that framework in 2022.

---

## What changed in 2022

In February 2022, FERC issued a revised Certificate Policy Statement alongside an Interim Policy Statement on greenhouse gas emissions (Docket PL18-1-000). Together they directed FERC staff to require project sponsors to quantify upstream and downstream greenhouse gas emissions from proposed capacity, assess those emissions against climate targets, and explain why the project is necessary given those costs.

The revision changed how projects get evaluated, not just how they get documented. Under the previous framework, a developer who showed executed shipper contracts largely satisfied the market-need test; the environmental inquiry centered on site-specific impacts. Under the revised framework, a developer must address whether adding gas capacity is consistent with broader decarbonization goals, a question that generates contested expert testimony, extended comment periods, and exposure to reversal on judicial review.

FERC has continued revising its approach through additional policy statements. Certificate proceedings for new capacity additions are longer, more contested, and less predictable than they were a decade ago. Developers financing 30- to 40-year infrastructure cannot close capital when the pipeline certificate is unresolved. Several projects have died in pre-application rather than reach a FERC vote.

---

## The state veto

[Section 401 of the Clean Water Act](https://www.law.cornell.edu/uscode/text/33/1341) gives states authority to certify that a federally licensed or permitted project complies with state water quality standards. A state denial blocks the federal approval. For an interstate gas pipeline, a single state environmental agency can stop a project FERC has already approved.

**Constitution Pipeline.** Williams Companies and partners proposed a 124-mile pipeline from Susquehanna County, Pennsylvania to New York markets, carrying approximately 650 million cubic feet per day. New York DEC denied the Section 401 certification in 2016, citing impacts to wetlands and streams. Williams challenged; the Second Circuit upheld the denial in 2017, ruling that Section 401 denials are not preempted by the Natural Gas Act (*Constitution Pipeline Co. v. N.Y. State Dep't of Envtl. Conservation*, 868 F.3d 87 (2d Cir. 2017)). Williams abandoned the project in February 2020.

**Northeast Supply Enhancement.** Williams proposed adding compression and looping to the existing Transco system to bring roughly 400 million cubic feet per day of incremental capacity to New York and New Jersey markets, the markets where Transco Zone 6 NY basis spreads spike during winter demand events. FERC issued the certificate in February 2018. New York DEC denied the Section 401 certification in May 2019. New Jersey DEP denied it the same month. Williams reapplied. New York denied again. The project remains unbuilt.

The table below places these projects alongside Atlantic Coast Pipeline and Mountain Valley Pipeline, the two other major mid-Atlantic and Southeast capacity additions of the past decade:

| Project | Developer | FERC Filing | Certificate | Outcome |
|---|---|---|---|---|
| Constitution Pipeline | Williams | 2013 | Dec 2014 | Abandoned Feb 2020 — Section 401 denial |
| Northeast Supply Enhancement | Williams | Oct 2017 | Feb 2018 | Blocked, unbuilt — Section 401 denial |
| Atlantic Coast Pipeline | Dominion / Duke | Sep 2015 | Oct 2017 | Cancelled Jul 2020 — legal uncertainty |
| Mountain Valley Pipeline | Equitrans | Sep 2015 | Oct 2017 | In service Jun 2024 — Congress required to intervene |

Three of the four projects either failed or required extraordinary measures to complete. All four received FERC certificates. The certificate was not the binding constraint. The processes that followed it were.

Together, Constitution and Northeast Supply Enhancement would have added close to 1 billion cubic feet per day of transport capacity to markets that, during polar vortex events, see basis spreads above $10/MMBtu. Those spreads pass through to electricity prices. Using the M1 transmission coefficient from Post 2 ($5.61/MWh per $/MMBtu), a $10 basis spike implies a $56/MWh premium on Dominion Zone power prices during constraint hours.

---

## The cost of inelastic supply: illustrative arithmetic

When pipeline capacity cannot expand to meet demand, the demand signal goes into price rather than quantity. Post 2's M4 regression captures this in the year trend coefficient: 0.097 log points per year, holding gas prices and seasonality constant, implies electricity prices have risen roughly 10% per year in nominal terms above what fuel costs predict.

How much of that trend reflects supply inelasticity is not separable from this data alone. The regression cannot isolate pipeline constraints from coal retirements or transmission bottlenecks. One indicator that is separable — and already in the dataset — is the implied gas-to-power heat rate.

The implied heat rate is the ratio of the electricity price to the gas price: LMP ($/MWh) divided by Henry Hub ($/MMBtu), yielding a result in MMBtu/MWh. It approximates which type of generator is setting the marginal price. An efficient combined-cycle gas turbine runs at roughly 7 MMBtu/MWh; an open-cycle gas peaker runs at 10 or higher. When the system is tight and gas supply is constrained, grid operators dispatch less efficient units to meet demand. The implied heat rate rises.

*[Figure 5: Implied gas-to-power heat rate, Dominion Zone — weekly, Sept 2020–June 2025]*

A rising trend in the implied heat rate over the sample period is consistent with the pipeline constraint story: if Transco cannot deliver enough gas at low basis spreads to the region's most efficient generators, less efficient units set the price more often. The chart distinguishes whether that trend accelerated in the AI era.

The order-of-magnitude cost calculation is straightforward. Loudoun County's data centers draw approximately 5,000 megawatts of load. At a 90% capacity factor, that is roughly 39 billion kilowatt-hours per year. Dominion Zone day-ahead prices averaged $40-50/MWh across the sample period. A 10% annual price increment on a $45/MWh baseline adds roughly $4.50/MWh per year, around $175 million in additional annual cost across the full Loudoun County load base in year one, compounding each year after.

Over a 10-year contract horizon, that cumulative incremental cost runs to roughly $2-3 billion, assuming no acceleration in load growth. The calculation is not a causal estimate traceable to pipeline policy. It illustrates what price growth above the gas-cost trend costs buyers at scale, and why long-run power procurement models for large data center operators are sensitive to whether that trend continues or moderates.

---

## Rate regulation as a secondary constraint

FERC also regulates what pipelines can charge. Interstate gas pipelines operate under cost-of-service rate regulation: FERC sets allowed transportation rates based on prudently incurred costs plus a reasonable return on equity. Pipeline owners cannot charge what constrained markets will bear.

When Transco Zone 6 NY trades at $10 above Henry Hub during a constraint event, the scarcity premium does not accrue to Williams as revenue it can reinvest in new capacity. Shippers with firm transportation contracts can resell that capacity through the capacity release market, capturing part of the spread. The pipeline itself earns its regulated rate whether gas is at $2 or $12.

High basis spreads signal that more pipe would be valuable. They do not increase the pipeline's revenue from a capacity expansion, because any new segment would earn only the regulated rate. Cost-of-service regulation was designed to protect captive shippers from monopoly pricing. The second-order effect is that it mutes the financial signal that high scarcity rents would send to developers considering new capacity. Transco earns returns on its existing rate base; the incremental return on new segments is subject to rate-setting that limits upside, dampening the expansion incentive relative to an unregulated market.

---

## The stack, end to end

Northern Virginia's data centers drew close to 5,000 megawatts in 2024. In PJM's Dominion Zone, natural gas sets the marginal price for that electricity. The gas reaches the generators through the Transco system, a pipeline that began construction in 1949. When Transco hits capacity, basis spreads spike and electricity prices follow.

Adding capacity to Transco requires a FERC certificate that now demands a greenhouse gas accounting a developer would not have faced under the 1999 framework. It may also require Section 401 water quality certification from states along the route, states that have used that authority to block projects FERC already approved. Any new segment must earn returns under cost-of-service rate regulation that caps what the pipeline can charge.

The data center buildout in Northern Virginia has been among the fastest capacity additions in the history of U.S. real estate. Dominion contracted 7,000 megawatts of new data center load in a single year. The pipeline regulatory process has not moved at that pace. The M4 year trend, electricity prices rising 10% per year beyond what gas costs predict, is consistent with a market where that gap persists.

Mountain Valley Pipeline entered service in June 2024. The first FERC filing was in 2015. Congress had to authorize the project's completion in the Fiscal Responsibility Act of 2023 after courts repeatedly halted construction. Dominion contracted its 7,000 megawatts of new data center load in roughly the same span of years it took to build one pipeline through West Virginia.

For anyone underwriting a long-term power purchase agreement in this market, the relevant question is not what Henry Hub trades at today. It is whether the pipeline can ever grow fast enough to stop the trend.

---

## Sources

**Data**
- Henry Hub daily spot price: [FRED series DHHNGSP](https://fred.stlouisfed.org/series/DHHNGSP), Federal Reserve Bank of St. Louis
- PJM Dominion Zone day-ahead LMPs: [EIA Wholesale Electricity Markets](https://www.eia.gov/electricity/wholesalemarkets/), annual zone CSV files
- Analysis code and panel data: [github.com/aleccshields/marginal-fuel](https://github.com/aleccshields/marginal-fuel)

**Statutes**
- Natural Gas Act § 7(c): [15 U.S.C. § 717f](https://www.law.cornell.edu/uscode/text/15/717f), Cornell Legal Information Institute
- Clean Water Act § 401: [33 U.S.C. § 1341](https://www.law.cornell.edu/uscode/text/33/1341), Cornell Legal Information Institute

**Regulatory**
- FERC 1999 Certificate Policy Statement: Docket PL99-3-000
- FERC 2022 Revised Certificate Policy Statement and Interim GHG Policy Statement: Docket PL18-1-000 (available at ferc.gov)

**Case law**
- *Constitution Pipeline Co. v. N.Y. State Dep't of Envtl. Conservation*, 868 F.3d 87 (2d Cir. 2017)

---

*Marginal Fuel covers energy markets, regulation, and the economics of the grid.*
