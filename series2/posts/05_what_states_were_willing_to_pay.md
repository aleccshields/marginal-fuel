# What States Were Willing to Pay

*On June 2, 2016, Exelon announced that Clinton Power Station and Quad Cities would retire unless Illinois enacted new support legislation. Combined capacity: roughly 2,900 megawatts of zero-marginal-cost, carbon-free baseload generation, both plants operating since the 1970s and 1980s. Six months later, Illinois passed the Future Energy Jobs Act. The program pays those plants $16.50 per megawatt-hour on top of whatever the electricity market delivers. That number, $16.50, is the market gap made explicit.*

*This is the second post in Zero Margin. Post 1 established the mechanism: nuclear plants earn the gas-set LMP despite near-zero fuel cost, which made their economics a function of gas prices they could not control. Post 1 also described three things the LMP fails to price: reliability, carbon-free generation, and grid inertia. This post examines what happened when three states decided to price those attributes themselves.*

---

## The instrument

A zero-emission credit is a per-megawatt-hour payment from a state program to a qualifying nuclear plant, paid on top of wholesale market revenues. It functions like a production tax credit, tied to output not capacity, and ratepayers fund it through a distribution surcharge.

The design reflects what ZEC architects argued the wholesale market was failing to price: the reliability value of firm, 24/7 generation and the carbon-free attribute of nuclear electricity. The LMP compensates a plant for energy. The capacity market compensates for available capacity. Neither compensates for being carbon-free. ZECs acknowledged directly that the combined energy plus capacity payment was insufficient to retain the plants states wanted to keep.

---

## Three programs

Between August 2016 and May 2018, New York, Illinois, and New Jersey each enacted ZEC programs to prevent announced or threatened nuclear retirements.

| State | Program | Enacted | Plants | Combined Capacity | ZEC Rate | Annual Program Cost |
|---|---|---|---|---|---|---|
| New York | Clean Energy Standard | Aug 2016 | Ginna, FitzPatrick, Nine Mile Point 1&2 | ~3,340 MW | ~$17/MWh | ~$480M/yr |
| Illinois | Future Energy Jobs Act | Dec 2016 | Clinton, Quad Cities 1&2 | ~2,880 MW | $16.50/MWh | ~$235M/yr |
| New Jersey | S-2313; BPU order | May 2018 / Apr 2019 | Salem 1&2, Hope Creek | ~3,500 MW | $10/MWh | ~$300M/yr |

Total: roughly 9,700 megawatts of capacity across three interconnected markets (NYISO, MISO, and PJM) at an aggregate annual cost approaching $1 billion.

New York and Illinois ZECs followed specific, firm retirement announcements: Exelon had set hard closure dates for Clinton (June 2017) and Quad Cities (June 2018), while Entergy had announced FitzPatrick's retirement for January 2017. New Jersey's program came after threatened rather than firm closures, and the state set the ZEC price lower at $10/MWh versus $16 to $17 in the other two states.

---

## The arithmetic of the gap

Nuclear plants in competitive wholesale markets earn two streams of revenue: the hourly LMP for each megawatt-hour dispatched, and an annual capacity payment from the regional capacity market. The LMP tracks the fuel cost of the marginal generator, overwhelmingly gas in the Midwest, upstate New York, and mid-Atlantic. The capacity payment covers the cost of being available.

**Energy revenue.** From 2015 through 2017, Henry Hub averaged $2.60 to $3.80/MMBtu. At a gas combined-cycle heat rate of 7 MMBtu/MWh, that translates to an LMP of roughly $18 to $27/MWh in the affected zones through this period.

**Capacity market revenue, converted to per-MWh terms.** A nuclear plant running at 92% capacity factor generates approximately 8,059 hours of output per year. Dividing the annual capacity payment by that figure yields the per-MWh contribution.

- **MISO Zone 4 (Illinois):** MISO Zone 4 capacity prices were structurally near zero for most of the 2014-2017 period, typically clearing below $5/MW-day. The 2015/16 Planning Resource Auction cleared anomalously high after Dynegy withheld capacity to inflate prices; FERC found market manipulation in December 2016 and ordered refunds. Excluding that anomaly, Zone 4 rates ran roughly $1 to $5/MW-day. At $3/MW-day: $3 × 365 / 8,059 = **$0.14/MWh.**
- **NYISO Zone C and E (upstate New York):** Installed capacity prices in the zones where Nine Mile Point and FitzPatrick operate ran approximately $2,000 to $4,000/MW-year. At $3,000/MW-year: $3,000 / 8,059 = **$0.37/MWh.**
- **PJM (New Jersey):** PJM's base residual auctions cleared at roughly $60 to $120/MW-day RTO-wide during the 2016-2018 period. At $100/MW-day: $100 × 365 / 8,059 = **$4.53/MWh.**

**Total market revenue vs. operating cost.** Clinton Power Station, running at 92% capacity factor and earning a mid-range 2016 LMP of $22/MWh, collected approximately $22.14/MWh in combined energy plus capacity revenue. NRC-mandated staffing, physical security infrastructure, and periodic refueling outages pushed operating costs for a single-unit plant like Clinton to roughly $30 to $40/MWh. Clinton was losing $8 to $18 per megawatt-hour it generated.

The $16.50/MWh ZEC closed that gap.

*[Figure 2: Nuclear revenue stack vs. operating cost by component (energy, capacity, ZEC) for each state program, 2016-2018]*

---

## The implied prices

ZEC amounts are administrative determinations, not market prices. Each state commissioned independent cost studies and set the ZEC rate to cover the estimated shortfall between a plant's operating costs and its projected market revenues. The rate each state was willing to pay establishes a floor on the value it assigned to retaining the plant.

**The implied price of reliability.** By paying $16.50/MWh above market, Illinois determined that nuclear's reliability and carbon-free attributes together were worth at least that much per megawatt-hour. At 8,059 hours per year, that implies a value of roughly $133/kW-year for firm, zero-emission capacity. By comparison, PJM's 2025/26 base residual auction cleared at $269.92/MW-day, approximately $99/kW-year. The capacity market arrived at a number in the same range as what Illinois paid administratively nine years earlier, under very different demand conditions.

**The implied carbon price.** Attributing the ZEC payment to the carbon-free attribute alone, and using a gas combined-cycle emissions rate of approximately 0.37 metric tons of CO2 per MWh (116.65 lbs CO2/MMBtu at 7 MMBtu/MWh heat rate):

- Illinois ($16.50/MWh) / 0.37 tCO2/MWh = **$45/ton CO2**
- New Jersey ($10/MWh) / 0.37 tCO2/MWh = **$27/ton CO2**

The Regional Greenhouse Gas Initiative, the active carbon market covering New England and Mid-Atlantic states, cleared at roughly $3 to $5 per ton during 2016 to 2018. ZEC programs priced the carbon attribute of nuclear electricity at five to fifteen times what the regional carbon market valued a ton of avoided emissions. The excess reflects what a per-ton carbon price cannot capture: reliability, firm capacity, and grid stability services that emit no carbon but also deliver no carbon credit.

---

## The empirical design and its limits

ZEC programs create the structure for a natural experiment. Three states enacted policies at different dates. Each program targets specific plants in specific grid zones. Adjacent zones without ZEC-supported plants serve as potential control groups. A difference-in-differences design would compare gas-price-adjusted LMPs in treated zones to LMPs in control zones before and after each program took effect.

The expected finding: if ZECs prevented economically motivated retirements, treated zones should show smaller LMP increases relative to gas price movements than control zones. Zero-marginal-cost plants, kept online by the ZEC, hold down the marginal cost of generation in those zones, reducing how far the system has to climb the dispatch stack toward higher-cost gas.

Two problems limit this design.

First, the treatment is counterfactual. ZECs did not change how much the plants were currently generating; they were already running at near-full capacity. The programs changed whether the plants would continue operating in future years. The LMP effect flows through retirements that did not happen, not through any contemporaneous change in dispatch. A before-after comparison in treated zones cannot separate the ZEC effect from simultaneous changes in gas prices, renewable buildout, or demand. What we observe is not "LMPs fell after ZEC" but "LMPs did not rise as much as they would have if the plant had retired." Measuring the latter requires modeling the counterfactual retirement.

Second, interconnection spreads the effect across regions. A nuclear plant in MISO Zone 4 exports power to neighboring zones when prices are higher elsewhere. Its impact on LMPs diffuses across the grid, attenuating the geographic contrast between treated and control zones.

The cleanest identification would come from the retirement announcements themselves. When Exelon set firm closure dates for Clinton and Quad Cities in spring 2016, forward power prices in MISO Zone 4 should have risen, pricing in the future loss of roughly 2,880 MW of zero-marginal-cost capacity. When FEJA passed in December 2016 and reversed those retirements, prices should have adjusted. That event-study design is feasible with MISO forward contract data at daily resolution.

The cost arithmetic establishes a lower bound on the market gap. States paid $10 to $17/MWh to retain capacity the wholesale market valued at $0.14 to $4.53/MWh through the capacity channel. The implied value of nuclear's non-energy attributes (reliability, carbon-free generation, grid inertia) was roughly 3 to 100 times what capacity markets were pricing during the retirement wave.

---

## What's next

Post 3 examines the PJM capacity market's spike between the 2024/25 and 2025/26 base residual auctions: from $28.92/MW-day to $269.92/MW-day across most of PJM, and $444/MW-day in the Dominion Zone serving Northern Virginia's data centers. That spike, driven by accelerating load growth, coal retirements, and a backlogged interconnection queue, produced a capacity price closer to what ZEC programs revealed as nuclear's true value nine years earlier. Whether that correction holds, or whether it is a transient response to the AI-era demand shock, determines whether new nuclear becomes financeable without the ZEC workaround.

Data and code are on [GitHub](https://github.com/aleccshields/marginal-fuel).

---

## Sources

**Illinois ZEC program (FEJA)**
- Future Energy Jobs Act, signed December 7, 2016: [Illinois Governor's press release](https://www.illinois.gov/news/press-release.15176.html). ZEC rate ($16.50/MWh initial), annual program cost (~$235M/year), plants (Clinton, Quad Cities): [Utility Dive, FEJA summary](https://www.utilitydive.com/news/illinois-energy-law-revives-renewables-while-aiding-nuclear/522195/)

**New York ZEC program**
- Clean Energy Standard ZEC requirement, PSC order August 2016. Plants: Ginna, FitzPatrick, Nine Mile Point 1&2. Annual cost (~$480M/year over first two-year tranche): [Utility Dive, PSC approval](https://www.utilitydive.com/news/updated-new-york-psc-approves-50-clean-energy-standard-nuclear-subsidies/423635/)

**New Jersey ZEC program**
- ZEC legislation (S-2313), signed May 2018. BPU approval order: April 18, 2019. ZEC rate ($10/MWh), plants (Salem 1&2, Hope Creek), annual cost (~$300M/year): NJ BPU docket, April 18, 2019; [NJ BPU newsroom, 2021 ZEC extension](https://www.nj.gov/bpu/newsroom/2021/approved/20210427.html) (supplementary context on program continuation)

**Price data**
- Henry Hub spot price 2015–2017: [FRED series DHHNGSP](https://fred.stlouisfed.org/series/DHHNGSP), Federal Reserve Bank of St. Louis
- MISO Planning Resource Auction prices: [MISO market reports and data](https://www.misoenergy.org/markets-and-operations/market-reports-and-data/)
- MISO Zone 4 2015/16 market manipulation (Dynegy): FERC Docket No. IN16-3-000, order finding market manipulation and ordering refunds, December 2016
- NYISO installed capacity market prices: [NYISO market data](https://www.nyiso.com/market-data)
- PJM base residual auction history: [PJM RPM auction results](https://www.pjm.com/markets-and-operations/rpm)

**Carbon markets**
- RGGI CO2 allowance prices 2016–2018: [RGGI auction results](https://www.rggi.org/auctions/auction-results)

**Nuclear emissions**
- Gas combined-cycle CO2 emissions rate (0.37 tCO2/MWh at 116.65 lbs CO2/MMBtu × 7 MMBtu/MWh heat rate): [EIA CO2 emissions coefficients](https://www.eia.gov/environment/emissions/co2_vol_mass.php)

---

*Zero Margin examines the economics of firm, carbon-free power in a gas-priced electricity market.*
