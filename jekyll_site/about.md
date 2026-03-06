---
layout: default
title: About
permalink: /about/
---

# About This Project

## Project Objective

This project investigates the relationship between nuclear power's role in electricity generation and electricity pricing across European countries during the period 2000-2020. By combining generation statistics with price data, we aim to understand how different countries' nuclear energy strategies correlate with their electricity market outcomes.

## Research Questions

1. **Does nuclear capacity percentage correlate with electricity prices?**
2. **How stable or volatile are these relationships across different countries?**
3. **What can we learn from different national strategies?**
4. **How does the Energiewende (Germany's energy transition) compare internationally?**

## Data

### What We Measure

- **Nuclear Generation**: Percentage of total electricity generation from nuclear sources
- **Electricity Prices**: Retail electricity prices (excluding taxes) in EUR/kWh
- **Time Period**: 2000-2020 (21 years of data)
- **Geographic Coverage**: 10 European countries with complete data

### Data Sources

- **Ember**: International electricity generation database
  - Covers all major energy sources
  - Complete historical data for European countries
  - Regular updates and validation

- **UK Government - IEA Table 5.5.1**: Domestic electricity prices
  - Historical data from 1979 onward
  - Tax and non-tax variants
  - Major developed countries

- **OECD Exchange Rates**: Historical currency conversions
  - GBP to EUR conversion
  - Annual averages for consistency

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

## Why This Analysis Matters

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

### For Investors
- Market dynamics of nuclear vs. other sources
- Price stability and volatility
- Long-term energy market trends

## Key Findings

### High-Level Observations

1. **No Universal Relationship**: Countries with similar nuclear percentages can have very different prices
2. **Policy Impact**: Germany's phase-out clearly visible (2011-2020)
3. **Price Volatility**: Increased after 2008 financial crisis across all countries
4. **Stability of Nuclear**: Once built, nuclear capacity remains relatively stable

### Country Patterns

**France**: Stable high nuclear (~75%), moderate prices

**Germany**: Declining nuclear (dramatic post-2011), rising prices

**Belgium & Slovakia**: Similar nuclear policies, different price evolution

**Spain**: Deliberately declining nuclear, prices rising

**UK**: Flat then increasing nuclear % in later years

## Methodology Highlights

- **Time Period**: 2000-2020 for data availability and quality
- **Country Selection**: Only countries with complete data across all 21 years
- **Price Standardization**: Converted to EUR, excluded taxes, used historical rates
- **Data Validation**: 205 valid data points, no gaps or anomalies

See the [Methodology page](methodology/) for complete technical details.

## Project Team

This analysis was conducted as part of an energy studies initiative to better understand European electricity markets.

**Contributors**: Data analysts and energy policy researchers

**Funding**: Self-funded independent research

## Contact & Feedback

Have questions about the analysis? Want to suggest improvements? Interested in collaborating?

- Open an issue on [GitHub](https://github.com/yourusername/energy-analysis)
- Submit feedback or suggestions
- Fork and contribute improvements

## How to Use These Visualizations

### For Academic Work
Please cite this project:
```
European Nuclear Energy Analysis (2026). Analysis of nuclear capacity 
and electricity prices in Europe, 2000-2020.
Retrieved from https://github.com/yourusername/energy-analysis
```

### For Presentations
Charts are high-resolution PNG files suitable for:
- Academic presentations
- Policy briefings
- Public communication
- Media use
- Educational materials

Attribution appreciated but not required.

### For Further Analysis
All underlying data and Python code is available on GitHub:
- Raw data files
- Processing scripts
- Visualization code
- This website source

## Limitations

### What This Analysis Is NOT

- **Not a causal analysis**: We show correlations, not causal mechanisms
- **Not a cost analysis**: We show prices, not underlying costs or subsidies
- **Not a climate analysis**: We focus on economics, not emissions
- **Not prescriptive**: We don't recommend particular energy policies

### Important Caveats

- Electricity prices are complex (multiple components)
- Germany's price rise has many causes (not just nuclear phase-out)
- Exchange rates affect price comparisons
- National statistics may hide regional variation

## Future Directions

### Potential Expansions

1. **Extended Timeline**: 2020-2025 data as it becomes available
2. **Additional Analysis**:
   - Renewable generation correlation
   - Carbon footprint analysis
   - Grid stability metrics
   - Storage and technology costs

3. **Interactive Versions**:
   - Web-based interactive charts
   - Downloadable data
   - API for further analysis

4. **Deeper Dives**:
   - Regional analysis (sub-national)
   - Seasonal patterns
   - Price component breakdown
   - Investment analysis

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

**Project Started**: 2026

**Data Period**: 2000-2020

**Countries Analyzed**: 10 European nations

**Data Points**: 205 observations

**Visualizations**: 3 main charts + 10 country-specific detailed charts

**Last Updated**: March 6, 2026
