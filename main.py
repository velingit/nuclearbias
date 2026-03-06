import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# ELECTRICITY PRICES FROM EXCEL (EXCLUDING TAXES, CONVERTED TO EUROS)
# ============================================================================

try:
    # Read prices in pence per kWh (excluding taxes)
    prices_df = pd.read_excel('table_551.xlsx', sheet_name='5.5.1 (excl. taxes)', header=8)
    # Read exchange rates (pound to EUR)
    rates_df = pd.read_excel('table_551.xlsx', sheet_name='Exchange rates', header=4)
    
    # Extract Germany data
    germany_prices = prices_df[['Year', 'Germany']].copy()
    germany_prices = germany_prices.dropna()
    
    # Merge with exchange rates
    germany_prices = germany_prices.merge(rates_df[['Year', 'Germany']], on='Year', suffixes=('_price', '_rate'))
    
    # Convert pence to pounds, then to euros using exchange rate
    # Price in pence / 100 * exchange rate = price in euros
    germany_prices['Price_EUR_per_KWH'] = (germany_prices['Germany_price'] / 100) * germany_prices['Germany_rate']
    
    germany_prices = germany_prices[['Year', 'Price_EUR_per_KWH']]
    germany_prices['Period'] = germany_prices['Year'].astype(str)
    germany_prices = germany_prices[['Period', 'Price_EUR_per_KWH']]
    germany_prices = germany_prices.sort_values('Period').reset_index(drop=True)
    
except Exception as e:
    raise ValueError(f"Failed to fetch price data from Excel: {str(e)}")

# ============================================================================
# ELECTRICITY GENERATION DATA (FROM YEARLY CSV)
# ============================================================================

try:
    generation_df = pd.read_csv('europe_yearly_full_release_long_format.csv')
    generation_df = generation_df[generation_df['Area'] == 'Germany']
    generation_df = generation_df[generation_df['Year'] >= 2000]
    generation_df = generation_df[(generation_df['Category'] == 'Electricity generation') & 
                                  (generation_df['Variable'].isin(['Nuclear', 'Renewables'])) & 
                                  (generation_df['Unit'] == 'TWh')]
    
    # Convert TWh to GWh
    generation_df['Value'] = generation_df['Value'] * 1000
    
    # Create period from Year
    generation_df['Period'] = generation_df['Year'].astype(str)
    
    # Pivot to have Nuclear and Renewables as columns
    generation_pivot = generation_df.pivot_table(index='Period', columns='Variable', values='Value', aggfunc='sum').reset_index()
    generation_pivot = generation_pivot.rename(columns={'Nuclear': 'Nuclear_Generation_GWh', 'Renewables': 'Renewable_Generation_GWh'})
    
    # Ensure columns exist
    if 'Nuclear_Generation_GWh' not in generation_pivot.columns:
        generation_pivot['Nuclear_Generation_GWh'] = 0
    if 'Renewable_Generation_GWh' not in generation_pivot.columns:
        generation_pivot['Renewable_Generation_GWh'] = 0
    
    germany_generation = generation_pivot
    
except Exception as e:
    raise ValueError("Failed to process generation data from CSV")

# ============================================================================
# MERGE AND SAVE
# ============================================================================

combined = pd.merge(germany_generation, germany_prices, on='Period', how='inner')

print(combined.to_string(index=False))

combined.to_csv('germany_energy_data.csv', index=False)




