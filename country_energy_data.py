from pathlib import Path

import pandas as pd

from iea_electricity_prices import load_country_price_series


BASE_DIR = Path(__file__).resolve().parent
EMBER_CSV = BASE_DIR / 'europe_yearly_full_release_long_format.csv'


def load_country_generation_series(country):
    generation_df = pd.read_csv(EMBER_CSV)
    generation_df = generation_df[
        (generation_df['Area'] == country)
        & (generation_df['Year'] >= 2000)
        & (generation_df['Category'] == 'Electricity generation')
        & (generation_df['Variable'].isin(['Nuclear', 'Renewables']))
        & (generation_df['Unit'] == 'TWh')
    ].copy()

    generation_df['Value'] = generation_df['Value'] * 1000
    generation_df['Period'] = generation_df['Year'].astype(str)

    generation_pivot = generation_df.pivot_table(
        index='Period',
        columns='Variable',
        values='Value',
        aggfunc='sum',
    ).reset_index()
    generation_pivot = generation_pivot.rename(
        columns={
            'Nuclear': 'Nuclear_Generation_GWh',
            'Renewables': 'Renewable_Generation_GWh',
        }
    )

    if 'Nuclear_Generation_GWh' not in generation_pivot.columns:
        generation_pivot['Nuclear_Generation_GWh'] = 0
    if 'Renewable_Generation_GWh' not in generation_pivot.columns:
        generation_pivot['Renewable_Generation_GWh'] = 0

    return generation_pivot[['Period', 'Nuclear_Generation_GWh', 'Renewable_Generation_GWh']]


def build_country_energy_dataframe(country, price_category='household'):
    price_df = load_country_price_series(country, base_dir=BASE_DIR, price_category=price_category)
    price_df = price_df[['Period', 'Price_EUR_per_KWH']]
    generation_df = load_country_generation_series(country)
    return generation_df.merge(price_df, on='Period', how='inner')