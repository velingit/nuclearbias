---
layout: default
title: Methodology
permalink: /methodology/
---

# Methodology

## Data Sources

### 1. Nuclear Generation Data
**Source**: Ember - Yearly Electricity Generation Dataset

- **File**: `europe_yearly_full_release_long_format.csv`
- **Coverage**: All European countries, 1990-2025
- **Metrics**:
  - Total electricity generation (TWh)
  - Nuclear generation (TWh)
  - Other fuel sources (coal, gas, renewables, etc.)
- **Data Quality**: Complete, regularly updated, high reliability

### 2. Electricity Price Data
**Source**: UK Government - IEA Table 5.5.1 - Domestic Electricity Prices

- **File**: `table_551.xlsx`
- **Coverage**: Major developed countries, 1979-2025
- **Units**: Pence per kWh (GBP base currency)
- **Tax Treatment**: Two variants provided (with/without taxes)
- **This Analysis**: Uses prices excluding taxes

### 3. Exchange Rates
**Source**: OECD Historical Exchange Rates

- **File**: Excel sheet within `table_551.xlsx`
- **Conversion Method**: GBP to EUR using historical annual averages
- **Conversion Formula**: 
  - 1 EUR = 13.7603 Austrian Schillings (ATS)
  - Price (EUR/kWh) = [Price (pence) / 100] × [Austria FX Rate / 13.7603]

## Data Preparation

### Step 1: Filter Time Period
- **Start Year**: 2000 (post-millennium, post-regulatory reforms)
- **End Year**: 2020 (before data quality issues in 2021+)
- **Rationale**: Captures post-deregulation European energy market

### Step 2: Select Countries
- **Criterion**: Must have both complete nuclear generation and electricity price data for entire period
- **Method**: 
  1. Identify all European countries in Ember dataset
  2. Cross-reference with IEA price data
  3. Filter for countries with data from 2000-2020
  4. Exclude aggregates (EU, Europe region, etc.)

**Final Selection**: 10 countries
- Belgium
- Finland
- France
- Germany
- Hungary
- Netherlands
- Slovakia
- Spain
- Switzerland
- United Kingdom

**Excluded Countries** (26 total):
- No nuclear generation: Austria, Denmark, Ireland, Italy, etc.
- Missing price data: Bulgaria, Czechia, Lithuania, Romania, Slovenia, Ukraine
- Incomplete data: Sweden (data starts 2007)

### Step 3: Data Units and Normalization

**Nuclear Capacity Percentage**:
```
Nuclear % = (Nuclear Generation TWh / Total Generation TWh) × 100
```
- Units: Percentage (%)
- Range: 0-100%
- Excludes years with zero nuclear generation

**Electricity Prices**:
```
Price (EUR/kWh) = [Price (pence) / 100] × Exchange Rate (GBP/EUR)
```
- Starting units: British pence per kWh
- Conversion to euros for consistency
- Excludes taxes (cleaner comparison across countries with different tax structures)

### Step 4: Data Validation

**Checks Applied**:
1. No negative values
2. Nuclear % ≤ 100%
3. No missing data points within 2000-2020
4. Exchange rates > 0
5. Electricity prices > 0

**Data Quality Result**: 205 valid data points from 10 countries, 21 years each

## Calculations

### Nuclear Capacity as % of Generation
```
Nuclear_Percent = (Nuclear_Generation_TWh / Total_Generation_TWh) × 100
```
- Only includes years where nuclear generation > 0
- Handles years where country had no nuclear generation

### Price Conversion: GBP to EUR
```
Exchange_Rate_GBP_to_EUR = Austria_FX_Rate / 13.7603

Price_EUR = (Price_GBP_pence / 100) × Exchange_Rate_GBP_to_EUR
```

**Rationale for Conversion Method**:
- Direct GBP/EUR rates unavailable for full time period
- Used ATS (Austrian Schilling) as proxy:
  - Austria maintained stable ATS/EUR rate (13.7603) upon Euro adoption
  - ATS/GBP rates available from 1979 onward
- Provides consistent historical conversion

## Visualization Methods

### Scatterplot: Nuclear % vs Price (All Countries)

**Design**:
- X-axis: Nuclear capacity percentage (0-100%)
- Y-axis: Electricity price (€/kWh)
- Color: Country (one color per country)
- Opacity: Time progression
  - Min opacity (0.3): Year 2000
  - Max opacity (0.95): Year 2020
  - Linear interpolation between

**Purpose**: Show relationship across all data points and countries

**Data Points**: 205 total

### Grid Charts: Individual Country Time Series

**Design**:
- Subplots: One per country (10 total)
- Primary Y-axis (left, blue): Nuclear % of generation
- Secondary Y-axis (right, pink): Electricity price (€/kWh)
- X-axis: Year (2000-2020)

**Purpose**: Visualize temporal trends within each country

**Key Elements**:
- Blue line with dots: Nuclear capacity trend
- Pink line with dots: Price trend
- Filled areas (semi-transparent): Visual emphasis
- Grid lines: Year reference
- Country title: Clear identification

### Individual Country Charts

**Design**: Full-sized version of grid charts for detailed analysis

**Purpose**: Detailed examination of specific country dynamics

## Technical Implementation

### Software Stack
- **Python 3.x**
- **Libraries**:
  - `pandas`: Data manipulation and analysis
  - `matplotlib`: Visualization
  - `openpyxl`: Excel file reading
  - `numpy`: Numerical operations

### Python Scripts

1. **`scatterplot_nuclear_vs_price.py`**
   - Generates scatterplot with all countries
   - Opacity based on year
   - Color-coded by country

2. **`generate_european_charts.py`**
   - Generates individual country charts
   - Generates combined grid view
   - Handles data filtering and validation

### Data Processing Flow

```
Raw Data (CSV, Excel)
        ↓
Filter by:
  - Time period (2000-2020)
  - European countries
  - Complete data availability
        ↓
Convert units:
  - Calculate nuclear %
  - Convert prices to EUR
        ↓
Validate data:
  - Check ranges
  - Handle missing values
        ↓
Generate visualizations:
  - Scatterplot
  - Grid charts
  - Individual charts
```

## Limitations and Caveats

### Data Limitations

1. **Price Data**:
   - Based on IEA statistics, primarily developed countries
   - Excludes taxes (different by country)
   - Historical rates used for GBP/EUR conversion

2. **Generation Data**:
   - Aggregate national statistics (doesn't capture regional variation)
   - Some countries show rounding in original data

3. **Time Period**:
   - 2000-2020 chosen to maximize data availability
   - Excludes recent years (2021-2025)

### Analytical Limitations

1. **Correlation ≠ Causation**:
   - Visual clustering doesn't imply causal relationships
   - Multiple factors affect electricity prices (fuel costs, regulation, grid infrastructure)

2. **Confounding Variables** (not captured):
   - Grid infrastructure age
   - Regulatory framework
   - Market structure
   - Geographic differences
   - Weather patterns (affecting renewables and demand)

3. **Exchange Rate Impact**:
   - GBP/EUR conversion affects absolute prices
   - Relative patterns still valid

### Country-Specific Notes

- **Germany**: Experienced major nuclear phase-out (2011-2020)
- **France**: Stable high nuclear use (baseline comparison)
- **UK**: Increasing nuclear % due to refurbishment
- **Spain**: Declining nuclear (policy choice)

## Reproducibility

### To Regenerate This Analysis

1. **Required Files**:
   - `europe_yearly_full_release_long_format.csv` (Ember)
   - `table_551.xlsx` (IEA prices and exchange rates)

2. **Python Scripts**:
   ```bash
   python scatterplot_nuclear_vs_price.py
   python generate_european_charts.py
   ```

3. **Output**:
   - PNG files in `nuclear_vs_price_scatterplot.png`
   - Individual country charts in `european_charts/` directory

### Version Information

- Python: 3.8+
- pandas: 1.3+
- matplotlib: 3.4+
- openpyxl: 3.5+

## Future Improvements

1. **Statistical Analysis**: Formal regression analysis with confidence intervals
2. **Expanded Period**: Include 2020-2025 data
3. **Additional Metrics**: Carbon emissions, grid stability, storage capacity
4. **Interactive Visualizations**: Plotly/Bokeh for web-based exploration
5. **Regional Analysis**: Sub-national data where available
6. **Renewable Integration**: Detailed renewable generation tracking

---

**Methodology Version**: 1.0

**Last Updated**: March 6, 2026

**Authors**: Energy Analysis Team
