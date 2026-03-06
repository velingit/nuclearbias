---
layout: default
title: Nuclear Capacity & Electricity Price Analysis
permalink: /nuclear-analysis/
---

# Nuclear Capacity & Electricity Price Analysis

## Overview

This section presents the relationship between nuclear capacity (as a percentage of total generation) and electricity prices across all European countries included in our study. Data spans from 2000 to 2020.

## Scatterplot: Nuclear % vs Price (All Countries)

![Nuclear vs Price Scatterplot](/assets/images/nuclear_vs_price_scatterplot.png)

**Figure 1**: All data points from 2000-2020 plotted by country color. Opacity increases from 2000 (fainter) to 2020 (solid) to show temporal progression.

### Key Observations

- **Color Coding**: Each country has a unique color for easy identification
- **Temporal Progression**: Earlier years (2000) appear more transparent, while recent years (2020) are fully opaque
- **Data Points**: 205 total observations across 10 countries
- **Axis Ranges**: 
  - X-axis: Nuclear capacity from 0% to ~80% of generation
  - Y-axis: Electricity prices from €0 to ~0.30/kWh

## Combined Grid View: All Countries Time Series

![Combined Grid of All Countries](/assets/images/All_Countries_Combined.png)

**Figure 2**: Grid layout showing individual nuclear % (left axis, blue) and electricity prices (right axis, pink) for each country from 2000-2020.

### What to Look For

- **Blue Line/Dots**: Nuclear capacity as percentage of generation
- **Pink Line/Dots**: Electricity price in €/kWh (excluding taxes)
- **Trends**: 
  - Stable nuclear percentages in most countries (except Germany)
  - Rising price volatility after 2008
  - Country-specific patterns in technology transitions

## Country-by-Country Analysis

### High Nuclear Capacity Countries
- **France**: ~70-80% nuclear (most stable)
- **Belgium**: ~50-55% nuclear
- **Slovakia**: ~50-55% nuclear
- **Hungary**: ~35-40% nuclear

### Medium Nuclear Capacity Countries
- **Finland**: ~25-30% nuclear
- **Sweden**: 30-40% nuclear (excluded: data starts 2007)
- **Germany**: Declining from 30% to near 0% (Energiewende)

### Lower Nuclear Capacity Countries
- **Spain**: ~15-20% nuclear (declining)
- **Switzerland**: ~35-40% nuclear
- **United Kingdom**: ~15-25% nuclear (increasing)
- **Netherlands**: ~3-5% nuclear

## Price Observations

- **General Range**: €0.10-0.25 per kWh (excluding taxes)
- **Most Volatile**: Germany (significant price increase post-2008)
- **Most Stable**: Switzerland and Hungary
- **Price Spikes**: Most countries show increases around 2007-2008 financial crisis

## Correlation Analysis

While not a formal regression, visual inspection suggests:
- **Weak Direct Correlation**: Higher nuclear % does not always mean lower prices
- **Country-Specific Factors**: Market structure, grid operators, and policy matter significantly
- **Temporal Factors**: Global energy prices and exchange rates affect all countries similarly

## Interactive Observations

1. **France's Stability**: Despite highest nuclear %, shows moderate price volatility
2. **Germany's Transition**: Clear nuclear phase-out visible (declining blue line)
3. **Belgium & Slovakia**: Similar nuclear models but different price patterns
4. **Price Clustering**: Many countries converge to similar prices by 2020

---

**Data Quality**: 
- 205 data points from 10 countries
- 2000-2020 period (21 years)
- Complete for all countries except those noted as excluded

**Excluded Countries**:
- Sweden: Data only available from 2007 onwards
- Other European countries: Either no nuclear generation or missing price data

**Data Sources**:
- Ember: Nuclear generation statistics
- UK Government IEA Table 5.5.1: Electricity prices (excl. taxes)
- Historical exchange rates for GBP to EUR conversion
