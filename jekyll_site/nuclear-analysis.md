---
layout: default
title: Nuclear Capacity & Electricity Price Analysis
permalink: /nuclear-analysis/
---

# Nuclear Capacity & Electricity Price Analysis

## Overview

This section presents the relationship between nuclear capacity (as a percentage of total generation) and electricity prices across 10 European countries included in our study. Data spans from 2000 to 2020.
I leave all methodological explanations about price creation to the [Energy prices team from the IEA ](https://www.iea.org/data-and-statistics/data-product/energy-prices)  

**Tip:** Click on any of the countries in the two regressions in order to remove them from the regression! 

## Scatterplot: Nuclear % vs Price (All Countries & FE Model)

<div style="text-align:left;max-width:980px;margin:0 auto 1em auto;">
  {% include scatterplot_household.html %}
  <noscript>
    <img src="{{ '/assets/nuclear_vs_price_scatterplot.png' | relative_url }}" alt="Nuclear vs Price Scatterplot" style="max-width:100%;margin-bottom:0.2em;">
  </noscript>
  <div style="font-size:0.8em;color:#FFFFFF;margin-top:0.1em;">Figure 1: Interactive household-price scatterplot. Hover any point to see the exact country, year, nuclear share, and electricity price. The y-axis is synchronized with Figure 2 for direct comparison.</div>
</div>

<div style="text-align:left;max-width:980px;margin:0 auto 1em auto;">
  {% include scatterplot_industrial.html %}
  <noscript>
    <img src="{{ '/assets/images/nuclear_vs_industrial_price_scatterplot.png' | relative_url }}" alt="Nuclear vs Industrial Price Scatterplot" style="max-width:100%;margin-bottom:0.2em;">
  </noscript>
  <div style="font-size:0.8em;color:#FFFFFF;margin-top:0.1em;">Figure 2: Interactive industrial-price scatterplot with the same y-axis range and hover details, using IEA Table 5.3.1 excluding taxes.</div>
</div>

<div style="text-align:left;max-width:980px;margin:0 auto 1em auto;">
  {% include fe_small_multiples.html %}
  <div style="font-size:0.8em;color:#FFFFFF;margin-top:0.1em;">Figure 3: Country-level OLS regressions of nuclear share (%) on household electricity price (€/kWh, excl. taxes). Solid lines indicate statistical significance (p&lt;0.05); dotted lines are not significant.</div>
</div>

### Key Observations


I have fitted regression lines to both plots out of interest. The industrial price does not show any correlation between nuclear generation and price, all the while a higher percentage of nuclear generation correlates negatively with household electricity prices. The revelation is that this correlation, albeit having a weak explanatory power, is statistically significant. 

Besides that, I have fitted a fixed effects model in order to more closely analyze the correlation on a per-country basis. Some are significant, some are not. Most significant plots besides Finland showcase a drop in price with a higher nuclear % in the production. The reason for adding a fixed effects model is to reduce some of the ommitted variable bias which in this research is plentiful. 

Of course it would be borderline idiotic to fit such a simple model to electricity prices as there are a myriad more variables that affect them (and nuclear generation for that matter). Neither regressions should be read as a strong model of electricity prices or as any form of causal evidence, it was just a fun experiment. 

## Combined Grid View: All Countries Time Series

<div style="text-align:left;margin-bottom:1em;">
  <img src="{{ '/assets/images/All_Countries_Combined.png' | relative_url }}" alt="Combined Grid of All Countries" style="max-width:100%;margin-bottom:0.2em;">
  <div style="font-size:0.8em;color:#FFFFFF;margin-top:0.1em;">Figure 4: Grid layout showing individual nuclear % (left axis, blue) and household electricity prices (right axis, pink) for each country from 2000-2020.</div>
</div>

<div style="text-align:left;margin-bottom:1em;">
  <img src="{{ '/assets/images/All_Countries_Combined_Industrial.png' | relative_url }}" alt="Combined Grid of All Countries Industrial" style="max-width:100%;margin-bottom:0.2em;">
  <div style="font-size:0.8em;color:#FFFFFF;margin-top:0.1em;">Figure 5: Grid layout showing individual nuclear % (left axis, blue) and industrial electricity prices (right axis, pink) for each country from 2000-2020.</div>
</div>

### What to Look For

- **Blue Line/Dots**: Nuclear capacity as percentage of generation
- **Pink Line/Dots**: Household or industrial electricity price in €/kWh (excluding taxes)
- **Trends**: 
  - Stable nuclear percentages in most countries (except Germany)
  - Rising price volatility after 2008 (external factors of course)
  - Country-specific patterns in technology transitions

## Correlation Analysis

While not a formal regression, visual inspection suggests:
- **Weak Direct Correlation**: Higher nuclear % does not always mean lower prices
- **Country-Specific Factors**: Market structure, grid operators, and policy matter significantly (of course)
- **Temporal Factors**: Global energy prices and exchange rates affect all countries similarly


