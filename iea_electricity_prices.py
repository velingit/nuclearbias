from pathlib import Path

import pandas as pd


PRICE_TABLES = {
    'household': {
        'workbook_name': 'table_551.xlsx',
        'sheet_name': '5.5.1 (excl. taxes)',
        'description': 'IEA Table 5.5.1 household electricity prices',
    },
    'industrial': {
        'workbook_name': 'table_531.xlsx',
        'sheet_name': '5.3.1 (excl. taxes)',
        'description': 'IEA Table 5.3.1 industrial electricity prices',
    },
}

EXCHANGE_SHEET_NAME = 'Exchange rates'
PRICE_HEADER_ROW = 8
EXCHANGE_HEADER_ROW = 4
EUR_CONVERSION_COLUMN = 'Austria'


def get_price_table_config(price_category='household'):
    if price_category not in PRICE_TABLES:
        supported = ', '.join(sorted(PRICE_TABLES))
        raise ValueError(f"Unsupported price category '{price_category}'. Expected one of: {supported}.")
    return PRICE_TABLES[price_category]


def resolve_workbook(base_dir=None, price_category='household'):
    config = get_price_table_config(price_category)
    base_path = Path(base_dir) if base_dir is not None else Path(__file__).resolve().parent
    workbook_path = base_path / config['workbook_name']
    if workbook_path.exists():
        return workbook_path

    available_tables = sorted(path.name for path in base_path.glob('table_*.xlsx'))
    details = ''
    if available_tables:
        details = f" Found other workbook(s): {', '.join(available_tables)}."

    raise FileNotFoundError(
        f"Expected {config['workbook_name']} in {base_path}, but it was not found.{details} "
        f"This analysis requires {config['description']}."
    )


def load_price_tables(base_dir=None, price_category='household'):
    config = get_price_table_config(price_category)
    workbook_path = resolve_workbook(base_dir, price_category=price_category)
    prices_df = pd.read_excel(
        workbook_path,
        sheet_name=config['sheet_name'],
        header=PRICE_HEADER_ROW,
    )
    rates_df = pd.read_excel(
        workbook_path,
        sheet_name=EXCHANGE_SHEET_NAME,
        header=EXCHANGE_HEADER_ROW,
    )
    return prices_df, rates_df, workbook_path


def build_converted_price_series(prices_df, rates_df, country, output_column='Price_EUR_per_KWH'):
    if country not in prices_df.columns:
        raise KeyError(f"{country} was not found in the price table.")
    if EUR_CONVERSION_COLUMN not in rates_df.columns:
        raise KeyError(f"{EUR_CONVERSION_COLUMN} was not found in the exchange-rate table.")

    country_prices = prices_df[['Year', country]].dropna().copy()
    eur_rates = rates_df[['Year', EUR_CONVERSION_COLUMN]].dropna().copy()
    merged = country_prices.merge(eur_rates, on='Year', how='inner')
    merged[output_column] = (merged[country] / 100) * merged[EUR_CONVERSION_COLUMN]
    return merged[['Year', output_column]]


def load_country_price_series(country, base_dir=None, price_category='household'):
    config = get_price_table_config(price_category)
    prices_df, rates_df, workbook_path = load_price_tables(base_dir, price_category=price_category)

    if country not in prices_df.columns:
        raise KeyError(f"{country} was not found in {workbook_path.name} sheet {config['sheet_name']}.")
    merged = build_converted_price_series(prices_df, rates_df, country)
    merged['Period'] = merged['Year'].astype(str)
    merged = merged[['Year', 'Period', 'Price_EUR_per_KWH']].sort_values('Year').reset_index(drop=True)
    return merged