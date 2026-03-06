import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from pathlib import Path
import numpy as np

# Read the generation data from Ember
ember_df = pd.read_csv('europe_yearly_full_release_long_format.csv')

# Read the price data from Excel (header is at row 8)
price_df = pd.read_excel('table_551.xlsx', sheet_name='5.5.1 (excl. taxes)', skiprows=8)

# Read exchange rates (header at row 4)
exchange_df = pd.read_excel('table_551.xlsx', sheet_name='Exchange rates', skiprows=4)

# Calculate GBP to EUR conversion rates
# Using Austrian Schilling: 1 EUR = 13.7603 ATS
# So: 1 GBP = Austria_rate / 13.7603 EUR
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

print(f"Countries in price data: {price_countries}")

# Filter Ember data for years 2000-2020 and focus on European countries
ember_filtered = ember_df[((ember_df['Year'] >= 2000) & (ember_df['Year'] <= 2020)) & (ember_df['Continent'] == 'Europe')].copy()

# Get unique countries (excluding aggregates like 'EU', 'Europe')
all_countries = sorted([c for c in ember_filtered['Area'].unique() 
                        if c not in ['EU', 'Europe', 'G7', 'G20', 'OECD', 'ASEAN']])

print(f"\nTotal countries in Ember data: {len(all_countries)}")

# Create output directory for charts
output_dir = 'european_charts'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each country and collect data
successful_countries = []
filtered_countries = []
country_data_dict = {}  # Store data for combined chart

for country in all_countries:
    # Get generation data for this country
    country_data = ember_filtered[ember_filtered['Area'] == country].copy()
    
    if len(country_data) == 0:
        filtered_countries.append(f"{country} (no generation data)")
        continue
    
    # Get Total generation and Nuclear generation (in TWh, not %)
    total_gen = country_data[(country_data['Variable'] == 'Total generation') & (country_data['Unit'] == 'TWh')]
    nuclear_gen = country_data[(country_data['Variable'] == 'Nuclear') & (country_data['Unit'] == 'TWh')]
    
    # Create a dictionary for easier access
    total_gen_dict = dict(zip(total_gen['Year'], total_gen['Value']))
    nuclear_gen_dict = dict(zip(nuclear_gen['Year'], nuclear_gen['Value']))
    
    # Get years where we have both total and nuclear data
    years_available = set(total_gen_dict.keys()) & set(nuclear_gen_dict.keys())
    
    if len(years_available) == 0:
        filtered_countries.append(f"{country} (no nuclear data)")
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
        filtered_countries.append(f"{country} (no nuclear generation in period)")
        continue
    
    # Get price data for this country
    if country not in price_countries:
        filtered_countries.append(f"{country} (no price data)")
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
    
    # Check if data covers the full period
    if merged['Year'].min() > 2000 or merged['Year'].max() < 2020:
        filtered_countries.append(f"{country} (data range: {int(merged['Year'].min())}-{int(merged['Year'].max())}))")
        continue
    
    # Store data for combined chart
    country_data_dict[country] = merged
    successful_countries.append(country)

# Create individual charts
for country in successful_countries:
    merged = country_data_dict[country]
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Plot nuclear % on left axis
    color1 = '#2E86AB'
    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Nuclear Capacity as % of Generation', fontsize=11, fontweight='bold', color=color1)
    line1 = ax1.plot(merged['Year'], merged['Nuclear_Percent'], 'o-', linewidth=2.5, markersize=6, 
                     color=color1, label='Nuclear %', zorder=3)
    ax1.fill_between(merged['Year'], merged['Nuclear_Percent'], alpha=0.2, color=color1, zorder=2)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.3, axis='y', zorder=0)
    ax1.set_ylim(bottom=0)
    
    # Plot electricity price on right axis
    ax2 = ax1.twinx()
    color2 = '#A23B72'
    ax2.set_ylabel('Electricity Price (€/kWh) excl. taxes', fontsize=11, fontweight='bold', color=color2)
    line2 = ax2.plot(merged['Year'], merged['Price_EUR'], 's-', linewidth=2.5, markersize=6,
                     color=color2, label='Price (€/kWh)', zorder=3)
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(bottom=0)
    
    # Add title
    plt.title(f'{country}: Nuclear Capacity % and Electricity Prices (2000-2020)', 
              fontsize=13, fontweight='bold', pad=15)
    
    # Combine legends
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=10)
    
    # Set x-axis ticks to show every year or every other year depending on data range
    years = merged['Year'].values
    if len(years) > 20:
        xtick_interval = 2
    else:
        xtick_interval = 1
    
    ax1.set_xticks(range(int(min(years)), int(max(years))+1, xtick_interval))
    ax1.set_xticklabels(range(int(min(years)), int(max(years))+1, xtick_interval), rotation=45)
    
    # Add footnote
    fig.text(0.12, 0.02, 
             'Data sources: Ember (nuclear generation %), UK Government IEA Table 5.5.1 (electricity prices excl. taxes)',
             ha='left', fontsize=8, style='italic', color='gray')
    
    plt.tight_layout(rect=[0, 0.03, 1, 1])
    
    # Save the individual figure
    filename = f'{output_dir}/{country.replace(" ", "_")}_nuclear_price.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[+] Generated chart for: {country}")

# Create combined chart with all countries
n_countries = len(successful_countries)
n_cols = 4
n_rows = (n_countries + n_cols - 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 4*n_rows))
axes = axes.flatten()  # Flatten to 1D array for easier indexing

for idx, country in enumerate(sorted(successful_countries)):
    merged = country_data_dict[country]
    ax1 = axes[idx]
    
    # Plot nuclear % on primary axis
    color1 = '#2E86AB'
    ax1.set_xlabel('Year', fontsize=9, fontweight='bold')
    ax1.set_ylabel('Nuclear %', fontsize=9, fontweight='bold', color=color1)
    ax1.plot(merged['Year'], merged['Nuclear_Percent'], 'o-', linewidth=2, markersize=4,
             color=color1, zorder=3)
    ax1.fill_between(merged['Year'], merged['Nuclear_Percent'], alpha=0.2, color=color1, zorder=2)
    ax1.tick_params(axis='y', labelcolor=color1, labelsize=8)
    ax1.tick_params(axis='x', labelsize=8)
    ax1.grid(True, alpha=0.3, axis='y', zorder=0)
    ax1.set_ylim(bottom=0)
    
    # Create secondary axis for price
    ax2 = ax1.twinx()
    color2 = '#A23B72'
    ax2.set_ylabel('Price (€/kWh)', fontsize=9, fontweight='bold', color=color2)
    ax2.plot(merged['Year'], merged['Price_EUR'], 's-', linewidth=2, markersize=4,
             color=color2, zorder=3)
    ax2.tick_params(axis='y', labelcolor=color2, labelsize=8)
    ax2.set_ylim(bottom=0)
    
    # Set title
    ax1.set_title(country, fontsize=10, fontweight='bold', pad=10)
    
    # Reduce x-axis tick labels
    years = merged['Year'].values
    if len(years) > 15:
        xtick_interval = 5
    elif len(years) > 10:
        xtick_interval = 3
    else:
        xtick_interval = 2
    
    ax1.set_xticks(range(int(min(years)), int(max(years))+1, xtick_interval))
    ax1.set_xticklabels(range(int(min(years)), int(max(years))+1, xtick_interval), rotation=45, fontsize=7)

# Hide empty subplots
for idx in range(n_countries, len(axes)):
    axes[idx].axis('off')

# Overall title and footer
fig.suptitle('European Nuclear Capacity (%) and Electricity Prices (€/kWh) - 2000-2020', 
             fontsize=16, fontweight='bold', y=0.995)

fig.text(0.5, 0.01, 
         'Data sources: Ember (nuclear generation %), UK Government IEA Table 5.5.1 (electricity prices excl. taxes)',
         ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.02, 1, 0.99])

# Save combined figure
combined_filename = f'{output_dir}/All_Countries_Combined.png'
plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
plt.close()
print(f"\n[+] Generated combined chart: {combined_filename}")

print(f"\n[+] Successfully generated {len(successful_countries)} individual charts + 1 combined chart")
print(f"Charts saved to: {output_dir}/")
print(f"\nCountries with charts:")
for country in sorted(successful_countries):
    print(f"  - {country}")

if filtered_countries:
    print(f"\n[-] Filtered out {len(filtered_countries)} countries (no nuclear power generation):")
    for country in sorted(filtered_countries):
        print(f"  - {country}")
