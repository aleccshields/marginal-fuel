# AI Runs on Gas

*The world's largest data center market runs on Appalachian natural gas. The electricity price in Northern Virginia traces back to a seventy-five-year-old pipe.*

---

Northern Virginia is the largest data center market in the world, accounting for roughly 13% of global operational capacity. Loudoun County alone, known as Data Center Alley, hosts over 300 facilities drawing close to 5,000 megawatts. Amazon, Microsoft, and Google together commissioned 38% of all new data center capacity in the region in 2024. Dominion Energy's contracted data center load grew by 7,000 megawatts in a single year.

All of it runs on electricity. In the mid-Atlantic, natural gas prices set what that electricity costs.

---

## The stack

The supply chain feeding a data center:

**Pipeline → gas turbine → generator → transmission lines → transformer → grid → UPS/cooling → servers**

PJM's generation mix includes nuclear, coal, and renewables, but gas-fired plants are the last units dispatched to meet demand. That makes gas fuel costs the clearing price for all electricity in the market, regardless of what generated it.

A $1 increase in the Henry Hub gas price pushes the wholesale electricity price up by roughly $5 to $6 per megawatt-hour. Gas suppliers don't absorb that cost. Utilities don't either. It lands on whoever buys power — including data center operators buying gigawatts of it.

---

## The Transco problem

Williams Companies owns the Transco system, the main gas pipeline serving the mid-Atlantic. Construction began in 1949; the first gas delivery reached Virginia in December 1950. The original mainline ran roughly 1,800 miles from South Texas to New York City. Since then Transco has grown to approximately 10,000 miles of total pipeline, but the mid-Atlantic corridor remains the critical artery for regional supply.

On a cold January morning, or as data center load climbs through the year, Transco hits capacity. Gas cannot flow fast enough from Appalachian and Gulf supply basins to the plants that need it.

The market signals this as a basis spread: the premium buyers in downstream markets pay above Henry Hub. Transco Zone 6 NY normally trades above Henry Hub, reflecting transportation costs from Louisiana. When the system binds, that premium blows out. Buyers in Northern Virginia and New York bid against each other for scarce pipeline capacity.

That premium flows into electricity prices, raising the wholesale price utilities pay for power and, eventually, the rates data center operators pay on their bills.

---

## What the data shows

The chart below plots weekly electricity prices in PJM's Dominion Zone alongside Henry Hub gas prices from 2020 through mid-2025.

*[Figure 1: Dominion Zone LMP vs. Henry Hub — weekly, Sept 2020–June 2025]*

Gas and power prices move together across the full period. The regression results in the next post put a number on it: a near-unit elasticity between Henry Hub and Dominion Zone LMPs. The more striking finding is what remains after controlling for gas prices. Dominion Zone LMPs have been rising at roughly 10% per year in real terms beyond what gas prices predict. Data center load tightens capacity and pushes prices up through that channel, not just through fuel costs. The distinction matters for investment decisions and regulatory policy alike.

---

## Why you can't just build more pipelines

Williams is trying to expand. The Southeast Supply Enhancement would add 1.6 billion cubic feet per day along existing rights of way. The Northeast Supply Enhancement has spent years in regulatory limbo after New York and New Jersey denied water quality certification.

New interstate gas pipeline capacity requires a certificate of public convenience and necessity from FERC. The process takes years. FERC revised its certificate policy in 2022 to weigh climate impacts more heavily, making approvals more contested than they were a decade ago.

The friction reflects legitimate concerns about locking in long-lived fossil fuel infrastructure. The financial consequence is that supply cannot respond to demand through new capacity, so the full demand signal goes into price. Electricity consumers in Northern Virginia pay more, for longer, than they would if pipeline capacity were elastic.

The energy transition debate has concentrated on generation: which plants to build, which to retire. In the near term, the binding constraint on power supply in data center markets may be the seventy-five-year-old pipe, not the generators.

---

## What's next

The next post presents the regression: a weekly panel using public FRED and EIA data with HAC-robust standard errors. The third post covers FERC certificate policy and pipeline rate regulation as constraints on AI infrastructure investment.

Data and code are on GitHub.

---

*Marginal Fuel covers energy markets, regulation, and the economics of the grid. Share it with someone who thinks about energy infrastructure.*
