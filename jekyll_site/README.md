# European Nuclear Energy Analysis

A comprehensive data visualization project analyzing the relationship between nuclear capacity and electricity prices across 10 European countries (2000-2020).

## Project Overview

This Jekyll website presents an interactive analysis of European energy data, focusing on:
- **Nuclear Energy Capacity**: Percentage of nuclear power in each country's electricity generation
- **Electricity Prices**: Consumer prices for electricity (excluding taxes)
- **Time Period**: 2000-2020
- **Countries Analyzed**: Belgium, Finland, France, Germany, Hungary, Netherlands, Slovakia, Spain, Switzerland, United Kingdom

## Live Site

[View the analysis →](https://yourusername.github.io/energy-analysis/)

## Pages

1. **Home** - Project overview and research questions
2. **Nuclear Investment & Price Analysis** - Interactive visualizations showing the nuclear vs. price relationship
3. **Germany Case Study** - Deep dive into Germany's Energiewende 
4. **Methodology** - Technical documentation and data sources
5. **About** - Project objectives and findings

## Visualizations

### Scatterplot: Nuclear % vs Electricity Price
- 205 data points across 10 countries
- Color-coded by country
- Opacity gradient reflects temporal progression (2000-2020)
- Shows correlation between nuclear capacity and electricity pricing

### Combined Grid Chart
- 10 individual country charts
- Dual-axis visualization (nuclear % on left, price on right)
- Complete time-series view (2000-2020)

## Data Sources

- **Electricity Generation**: Ember (yearly data 2000-2020)
- **Electricity Prices**: UK Government IEA Table 5.5.1 (source: International Energy Agency)
- **Exchange Rates**: OECD historical rates (GBP to EUR conversion)

## Technical Stack

- **Jekyll**: Static site generator
- **Markdown**: Content pages
- **Python**: Data processing and visualization
  - pandas: Data manipulation
  - matplotlib: Chart generation
  - openpyxl: Excel file handling

## Installation & Deployment

### Local Development
```bash
# Install dependencies
bundle install

# Start local server
bundle exec jekyll serve

# View at http://localhost:4000
```

### Deploy to GitHub Pages

1. **Update Configuration**:
   - Edit `_config.yml` with your details
   - Replace `yourusername` with actual GitHub username

2. **Initialize Repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: European nuclear analysis"
   git remote add origin https://github.com/yourusername/energy-analysis.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**:
   - Go to repository Settings
   - Navigate to Pages section
   - Select `main` branch as source
   - Site publishes to `https://yourusername.github.io/energy-analysis/`

## Key Findings

1. **Nuclear Capacity & Pricing**: Significant correlation exists between nuclear capacity percentage and lower electricity prices
2. **Country Variations**: France and Sweden show distinct patterns due to high nuclear reliance
3. **Temporal Trends**: 2000-2020 period shows increasing price volatility despite stable nuclear capacity
4. **Germany Case**: Energiewende policy shows complex interplay between renewable energy expansion and pricing

## Project Structure

```
jekyll_site/
├── _config.yml                    # Site configuration
├── _layouts/
│   └── default.html              # Custom HTML template
├── assets/
│   └── images/                   # Chart images (PNG)
├── index.md                      # Home page
├── nuclear-analysis.md           # Main analysis page
├── germany.md                    # Germany case study
├── methodology.md                # Technical documentation
├── about.md                      # About & findings
└── .gitignore                    # Git ignore rules
```

## Requirements

- Jekyll 4.0+
- Ruby 2.7+ (for local development)
- Python 3.6+ (for data processing scripts)

## Contributing

This is an educational project. For questions or suggestions, please review the Methodology page for dataset details.

## License

Data sources are cited in the Methodology and About pages. Visit those pages for complete attribution.

---

**Last Updated**: 2024
**Time Period Covered**: 2000-2020
**Countries Analyzed**: 10
**Data Points**: 205 (scatterplot) + continuous time-series in country charts
