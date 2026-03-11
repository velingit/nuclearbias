import json
from pathlib import Path

import pandas as pd

from iea_electricity_prices import build_converted_price_series, load_price_tables


BASE_DIR = Path(__file__).resolve().parent
EMBER_CSV = BASE_DIR / 'europe_yearly_full_release_long_format.csv'
OUTPUT_JS = BASE_DIR / 'jekyll_site' / 'assets' / 'energy_data.js'

SUPPORTED_COUNTRIES = [
    'Belgium',
    'Finland',
    'France',
    'Germany',
    'Hungary',
    'Netherlands',
    'Slovakia',
    'Spain',
    'Switzerland',
    'United Kingdom',
]


def load_generation_series(gen_df, country):
    generation_df = gen_df[
        (gen_df['Area'] == country)
        & (gen_df['Category'] == 'Electricity generation')
        & (gen_df['Variable'] == 'Nuclear')
        & (gen_df['Unit'] == 'TWh')
    ][['Year', 'Value']].copy()
    generation_df['Period'] = generation_df['Year'].astype(str)
    generation_df['Nuclear_Generation_GWh'] = generation_df['Value'] * 1000
    return generation_df[['Period', 'Nuclear_Generation_GWh']]


def load_price_series(prices_df, rates_df, country, output_column):
    price_df = build_converted_price_series(
        prices_df,
        rates_df,
        country,
        output_column=output_column,
    )
    price_df['Period'] = price_df['Year'].astype(str)
    return price_df[['Period', output_column]]


def build_energy_data():
    gen_df = pd.read_csv(EMBER_CSV)
    household_prices_df, household_rates_df, _ = load_price_tables(price_category='household')
    industrial_prices_df, industrial_rates_df, _ = load_price_tables(price_category='industrial')

    energy_data = []

    for country in SUPPORTED_COUNTRIES:
        generation_df = load_generation_series(gen_df, country)
        household_price_df = load_price_series(
            household_prices_df,
            household_rates_df,
            country,
            output_column='Household_Price_EUR_per_KWH',
        )
        industrial_price_df = load_price_series(
            industrial_prices_df,
            industrial_rates_df,
            country,
            output_column='Industrial_Price_EUR_per_KWH',
        )

        merged = generation_df.merge(household_price_df, on='Period', how='inner')
        merged = merged.merge(industrial_price_df, on='Period', how='inner')
        merged['Period'] = pd.to_numeric(merged['Period'], errors='coerce').astype('Int64')
        merged = merged.dropna(subset=['Period']).sort_values('Period')
        merged['Period'] = merged['Period'].astype(int)
        energy_data.append({'country': country, 'data': merged.to_dict(orient='records')})

    return energy_data


def write_energy_data_js(energy_data):
    OUTPUT_JS.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JS.open('w', encoding='utf-8') as output_file:
        output_file.write('// This file contains time series data for all analyzed countries\n')
        output_file.write('// Format: { country: \'CountryName\', data: [{Period, Nuclear_Generation_GWh, Household_Price_EUR_per_KWH, Industrial_Price_EUR_per_KWH}, ...] }\n')
        output_file.write('const energyData = ')
        json.dump(energy_data, output_file, ensure_ascii=False, indent=2)
        output_file.write(';\n')


def main():
    energy_data = build_energy_data()
    write_energy_data_js(energy_data)
    print(f'Done. Saved to {OUTPUT_JS}')


if __name__ == '__main__':
    main()
