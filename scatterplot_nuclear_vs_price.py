import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Read the generation data from Ember
ember_df = pd.read_csv('europe_yearly_full_release_long_format.csv')

# Read the price data from Excel (header is at row 8)
price_df = pd.read_excel('table_551.xlsx', sheet_name='5.5.1 (excl. taxes)', skiprows=8)

# Read exchange rates (header at row 4)
exchange_df = pd.read_excel('table_551.xlsx', sheet_name='Exchange rates', skiprows=4)

# Calculate GBP to EUR conversion rates
# Using Austrian Schilling: 1 EUR = 13.7603 ATS
ats_to_eur = 13.7603
gbp_to_eur_rates = {}
for _, row in exchange_df.iterrows():
    year = int(row['Year'])
    ats_rate = float(row['Austria'])
    if pd.notna(ats_rate) and ats_rate > 0:
        gbp_to_eur = ats_rate / ats_to_eur
        gbp_to_eur_rates[year] = gbp_to_eur

# Get list of countries from the price data
price_countries = [col for col in price_df.columns if col != 'Year']

# Filter Ember data for years >= 2000 and focus on European countries
ember_filtered = ember_df[(ember_df['Year'] >= 2000) & (ember_df['Continent'] == 'Europe')].copy()

# Get unique countries (excluding aggregates)
all_countries = sorted([c for c in ember_filtered['Area'].unique() 
                        if c not in ['EU', 'Europe', 'G7', 'G20', 'OECD', 'ASEAN']])

# Collect all data points for scatterplot
all_data_points = []

for country in all_countries:
    # Get generation data for this country
    country_data = ember_filtered[ember_filtered['Area'] == country].copy()
    
    if len(country_data) == 0:
        continue
    
    # Get Total generation and Nuclear generation (in TWh)
    total_gen = country_data[(country_data['Variable'] == 'Total generation') & (country_data['Unit'] == 'TWh')]
    nuclear_gen = country_data[(country_data['Variable'] == 'Nuclear') & (country_data['Unit'] == 'TWh')]
    
    # Create dictionaries for easier access
    total_gen_dict = dict(zip(total_gen['Year'], total_gen['Value']))
    nuclear_gen_dict = dict(zip(nuclear_gen['Year'], nuclear_gen['Value']))
    
    # Get years where we have both total and nuclear data
    years_available = set(total_gen_dict.keys()) & set(nuclear_gen_dict.keys())
    
    if len(years_available) == 0:
        continue
    
    # Create dataframe with generation data
    gen_data = pd.DataFrame({
        'Year': sorted(years_available),
    })
    gen_data['Total_Generation'] = gen_data['Year'].map(total_gen_dict)
    gen_data['Nuclear_Generation'] = gen_data['Year'].map(nuclear_gen_dict)
    
    # Calculate nuclear as % of total
    gen_data['Nuclear_Percent'] = (gen_data['Nuclear_Generation'] / gen_data['Total_Generation'] * 100).fillna(0)
    gen_data = gen_data[gen_data['Nuclear_Percent'] > 0]  # Only keep years with nuclear generation
    
    if len(gen_data) == 0:
        continue
    
    # Get price data for this country
    if country not in price_countries:
        continue
    
    country_prices = price_df[['Year', country]].copy()
    country_prices.columns = ['Year', 'Price_GBP_pence']
    country_prices['Year'] = country_prices['Year'].astype(int)
    country_prices['Price_GBP_pence'] = pd.to_numeric(country_prices['Price_GBP_pence'], errors='coerce')
    
    # Convert prices: pence to pounds first (/100), then to euros
    country_prices['Price_EUR'] = country_prices.apply(
        lambda row: (row['Price_GBP_pence'] / 100) * gbp_to_eur_rates.get(row['Year'], np.nan) if pd.notna(row['Price_GBP_pence']) and row['Year'] in gbp_to_eur_rates else np.nan,
        axis=1
    )
    
    # Merge generation and price data
    merged = pd.merge(gen_data, country_prices[['Year', 'Price_EUR']], on='Year', how='inner')
    merged = merged.dropna(subset=['Price_EUR'])
    merged = merged[(merged['Year'] >= 2000) & (merged['Year'] <= 2020)]
    
    if len(merged) == 0:
        continue
    
    # Check if data covers the period
    if merged['Year'].min() > 2000 or merged['Year'].max() < 2020:
        continue
    
    # Add country name to each row
    merged['Country'] = country
    all_data_points.append(merged)

# Combine all data
scatterplot_data = pd.concat(all_data_points, ignore_index=True)

# Define colors and markers for each country
countries = sorted(scatterplot_data['Country'].unique())
n_countries = len(countries)

# Create color palette (using a variety of colors)
colors = plt.cm.tab20(np.linspace(0, 1, max(n_countries, 3)))
if n_countries > 20:
    colors = plt.cm.hsv(np.linspace(0, 1, n_countries))

# Create the scatterplot
fig, ax = plt.subplots(figsize=(14, 8))

# Get the year range for alpha calculation
min_year = scatterplot_data['Year'].min()
max_year = scatterplot_data['Year'].max()
year_range = max_year - min_year if max_year > min_year else 1

for idx, country in enumerate(countries):
    country_data = scatterplot_data[scatterplot_data['Country'] == country]
    color = colors[idx % len(colors)]
    
    # Plot each point with alpha based on year (earlier years = less solid, later years = more solid)
    for _, row in country_data.iterrows():
        # Calculate alpha: 0.3 (min) to 0.95 (max) based on year
        year_normalized = (row['Year'] - min_year) / year_range if year_range > 0 else 1
        alpha = 0.3 + (year_normalized * 0.65)  # Range from 0.3 to 0.95
        
        ax.scatter(row['Nuclear_Percent'], row['Price_EUR'],
                   marker='o', s=150, color=color, alpha=alpha, 
                   edgecolors='black', linewidth=0.5, zorder=3)
    
    # Add to legend with the most recent year's opacity
    latest_year_data = country_data[country_data['Year'] == country_data['Year'].max()]
    if len(latest_year_data) > 0:
        ax.scatter([], [], label=country, marker='o', s=150, color=color, alpha=0.95, 
                   edgecolors='black', linewidth=0.5)

# Set labels and title
ax.set_xlabel('Nuclear Capacity as % of Generation', fontsize=13, fontweight='bold')
ax.set_ylabel('Electricity Price (€/kWh) excl. taxes', fontsize=13, fontweight='bold')
ax.set_title('European Nuclear Capacity (%) vs Electricity Prices (2000-2020)', 
             fontsize=14, fontweight='bold', pad=20)

# Add grid
ax.grid(True, alpha=0.3, linestyle='--', zorder=1)

# Add legend
ax.legend(loc='best', fontsize=10, framealpha=0.95, title='Country', title_fontsize=11)

# Set limits
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

# Add footnote
fig.text(0.12, 0.04, 
         'Data sources: Ember (nuclear generation %), UK Government IEA Table 5.5.1 (electricity prices excl. taxes)',
         ha='left', fontsize=9, style='italic', color='gray')

fig.text(0.12, 0.01,
         'Note: Color opacity increases from 2000 (fainter) to 2020 (solid) to highlight temporal progression',
         ha='left', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.05, 1, 1])

# Save the figure
filename = 'nuclear_vs_price_scatterplot.png'
plt.savefig(filename, dpi=300, bbox_inches='tight')
plt.close()

print(f"[+] Scatterplot saved as: {filename}")
print(f"\nScatterplot contains {len(scatterplot_data)} data points from {n_countries} countries:")
for country in sorted(countries):
    n_points = len(scatterplot_data[scatterplot_data['Country'] == country])
    print(f"  - {country}: {n_points} data points")
