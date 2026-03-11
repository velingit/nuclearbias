---
layout: default
title: Methodology
permalink: /methodology/
---

# About This Project

My reason for choosing Germany is that I had moved to the country in 2019 and prior to that was somewhat unaware of the general disdain there is around here for nuclear. There was little theoretical reasoning besides an argument with a friend which ended without a proper conclusion. Because of that, I wanted to explore the energy sector in more detail and hopefully strengthen my arguments going forward. The inclusion of other countries in the mix is done because first data was available and I was interested and second as a reference. 

I had firstly thought about creating a synthetic control in order to prove once and for all how much better nuclear is, but upon thinking about it for more than 90 seconds, I realized that it does not in any way achieve what I am aiming to do. 

I first started out looking at the relation of energy production and household prices excluding taxes, I will expand it to wholesale prices too, but without a big educational investment from my side, I do not believe I can infer information about the economic effects of the phase-out which is its most critiqued point internationally. 

I had decided on the year 2000 as a starting point, since that's around when the first liberalization package was impelemented in Western Europe and reliable data was available (1996). Furthermore, my cutoff is 2020, because the pandemic and the gas shortage had effects on electricity outside of the scope of this naive throwing of assumptions I am doing.  

## Project Objective

This project investigates the relationship between nuclear power's role in electricity generation and electricity pricing across European countries during the period 2000-2020. By combining generation statistics with price data, I aim to understand how different countries' nuclear energy strategies correlate with their electricity market outcomes.

## Research Questions

1. **Does nuclear capacity percentage correlate with electricity prices?**
2. **How stable or volatile are these relationships across different countries?**
3. **What can we learn from different national strategies?**
4. **How does the Energiewende (Germany's energy transition) compare internationally?**

## Visualization Approach

### 1. The Scatterplot

Shows all 205 data points across 10 countries and 21 years in a single visualization:
- **X-axis**: Nuclear capacity percentage (0-80%)
- **Y-axis**: Electricity price (€0.08-0.30/kWh)
- **Color**: Country (unique color for each)
- **Transparency**: Time dimension (fainter = older, solid = newer)

This allows viewers to:
- See overall distribution and relationships
- Identify country clusters and patterns
- Notice temporal trends through opacity changes

### 2. The Grid View

Shows individual country trends side-by-side:
- 10 subplots, one per country
- Dual-axis design (nuclear % and price)
- 21 years of data per country
- Easy comparison between countries

This allows viewers to:
- Understand each country's specific trajectory
- Compare growth, decline, and stability patterns
- Identify inflection points and transitions

### 3. Individual Country Charts

Full-sized, detailed charts for focused analysis on specific countries, particularly Germany's unique transition.

## Why This Analysis Could Matter

### For Energy Policy
- Understanding the relationship between generation mix and pricing
- Informing decisions about nuclear phase-out or expansion
- Cost-benefit analysis of energy transitions

### For Climate Action
- Nuclear power's role in decarbonization
- Trade-offs between pricing and emissions
- Alternative paths to zero-carbon grids

### For Citizens
- Understanding electricity costs
- Seeing impact of national energy policies
- Opportunity to evaluate trade-offs


### Observations

1. **No Universal Relationship**: Countries with similar nuclear percentages can have very different prices
2. **Policy Impact**: Germany's phase-out clearly visible (2011-2020)
3. **Price Volatility**: Increased after 2008 financial crisis across all countries
4. **Stability of Nuclear**: Once built, nuclear capacity remains relatively stable

## Methodology Highlights

- **Time Period**: 2000-2020 for data availability and quality
- **Country Selection**: Only countries with complete data across all 21 years (excl. Belgium with missing price data 2003-2007)
- **Price Standardization**: Converted to EUR, excluded taxes, used historical rates from same document

### Important Caveats

- Electricity prices are complex
- Germany's price rise has many causes (not just nuclear phase-out)
- Exchange rates affect price comparisons
- National statistics may hide regional variation

### Potential Expansions

1. Inclusion of more variables for a more encompassing model (amongst which eg. CO2 generation, battery availability)

2. Deeper Dives:
   - Regional analysis (sub-national) (I'm also interested in quality of life in relation to nuclear power plant proximity)
   - Seasonal patterns 

## References & Resources

### Data Sources
- [Ember Global Electricity Review](https://ember-climate.org/)
- [UK Government Energy Price Statistics](https://www.gov.uk/government/statistics)
- [OECD Statistics](https://stats.oecd.org/)

### Energy Policy Resources
- Nuclear Energy Agency (NEA)
- International Energy Agency (IEA)
- European Union - Energy Policy
- National energy agencies and ministries

### Related Research
- Decarbonization pathways literature
- Nuclear economics studies
- European electricity market analyses
- Energy transition case studies

---
