---
layout: default
title: Home
permalink: /
---

## Project Overview

This analysis was done because I was looking for a project and since I was born next to a nuclear power plant, I have personally benefitted from nuclear energy. As a result, I have lived my whole life with a nuclear bias. Since I came to Germany, I have met many opposing views. From worries about storage to outright claims that it is not a good energy source. With this research, I aim to clear my nuclear bias and understand its problems. It is an ongoing project and will evolve when I get more ideas.

## Dataset

- **Nuclear Generation Data**: [Ember's yearly electricity generation dataset](https://ember-energy.org/data/yearly-electricity-data/)
- **Electricity Prices**: [UK Government IEA Table 5.5.1](https://www.gov.uk/government/statistical-data-sets/international-industrial-energy-prices) (prices excluding taxes)
- **Exchange Rates**: Historical GBP to EUR conversion rates from the electricity prices table
- **Coverage**: 10 European countries with complete data from 2000-2020. Countries included had complete data in both datasets and have generated nuclear energy in the period.
- **Countries Included**: Belgium, Finland, France, Germany, Hungary, Netherlands, Slovakia, Spain, Switzerland, United Kingdom

## Visualizations

The project currently highlights six core visualizations. Each title links to the page where that visualization is discussed in more detail.

**Tip:** Click on any of the countries in the two regressions in order to remove them from the regression! 

### [Household Regression Scatterplot]({{ '/nuclear-analysis/' | relative_url }})

<div style="text-align:left;max-width:980px;margin:0 auto 2.5em auto;">
	{% include scatterplot_household.html %}
</div>

### [Industrial Regression Scatterplot]({{ '/nuclear-analysis/' | relative_url }})

<div style="text-align:left;max-width:980px;margin:0 auto 2.5em auto;">
	{% include scatterplot_industrial.html %}
</div>

### [Country-Level Fixed-Effects Regressions]({{ '/nuclear-analysis/' | relative_url }})

<div style="text-align:left;max-width:980px;margin:0 auto 1.5em auto;">
	{% include fe_small_multiples.html %}
</div>

### [Interactive Time Series]({{ '/nuclear-analysis/time-series/' | relative_url }})

<div style="text-align:left;max-width:1100px;margin:0 auto 1.5em auto;">
	{% include plotly_timeseries.html %}
</div>

### [Combined Grid: Household Prices]({{ '/nuclear-analysis/' | relative_url }})

<div style="text-align:left;max-width:1100px;margin:0 auto 1.5em auto;">
	<img src="{{ '/assets/images/All_Countries_Combined.png' | relative_url }}" alt="Combined Grid of All Countries Household" style="max-width:100%;margin-bottom:0.2em;">
</div>

### [Combined Grid: Industrial Prices]({{ '/nuclear-analysis/' | relative_url }})

<div style="text-align:left;max-width:1100px;margin:0 auto 1.5em auto;">
	<img src="{{ '/assets/images/All_Countries_Combined_Industrial.png' | relative_url }}" alt="Combined Grid of All Countries Industrial" style="max-width:100%;margin-bottom:0.2em;">
</div>

