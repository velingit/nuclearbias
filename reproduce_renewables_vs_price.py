from pathlib import Path
import gzip
import xml.etree.ElementTree as ET

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

BASE_DIR = Path(__file__).resolve().parent
MONTHLY_CSV = BASE_DIR / 'europe_monthly_full_release_long_format.csv'
EUROSTAT_PRICE_API = 'https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/nrg_pc_205?precision=1&time=2025&compressed=true'
OUTPUT_IMAGE = BASE_DIR / 'reproduced_renewables_vs_price_2025_better.png'

SHORT_LABELS = {
    'Austria': 'AT',
    'Belgium': 'BE',
    'Denmark': 'DK',
    'Finland': 'FI',
    'France': 'FR',
    'Germany': 'DE',
    'Greece': 'GR',
    'Ireland': 'IE',
    'Italy': 'IT',
    'Luxembourg': 'LU',
    'Netherlands': 'NL',
    'Portugal': 'PT',
    'Spain': 'ES',
    'Sweden': 'SE',
    'Norway': 'NO',
    'Poland': 'PL',
    'Slovakia': 'SK',
    'Switzerland': 'CH',
    'Czechia': 'CZ',
    'Hungary': 'HU',
    'T\u00fcrkiye': 'TR',
    'United Kingdom': 'UK',
}


def load_shares_2025():
    monthly = pd.read_csv(MONTHLY_CSV, parse_dates=['Date'])
    monthly['Year'] = monthly['Date'].dt.year
    monthly['Month'] = monthly['Date'].dt.month

    mask = (
        (monthly['Year'] == 2025)
        & (monthly['Unit'] == '%')
        & (monthly['Variable'].isin(['Renewables', 'Wind and solar']))
    )

    monthly = monthly.loc[mask, ['Area', 'Variable', 'Value', 'Month']].copy()
    annual = (
        monthly.groupby(['Area', 'Variable'])
        .agg(average_share=('Value', 'mean'), months=('Month', 'nunique'))
        .reset_index()
    )
    annual_wide = annual.pivot(index='Area', columns='Variable', values='average_share').reset_index()
    return annual_wide.rename(
        columns={'Renewables': 'Renewables_share', 'Wind and solar': 'WindSolar_share'}
    )


def load_industrial_prices_eurostat():
    response = requests.get(EUROSTAT_PRICE_API, timeout=60)
    response.raise_for_status()
    xml_text = gzip.decompress(response.content)
    root = ET.fromstring(xml_text)

    ns = {'g': 'http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic'}
    price_rows = []

    for series in root.findall('.//g:Series', ns):
        series_key = {v.attrib['id']: v.attrib['value'] for v in series.find('g:SeriesKey', ns).findall('g:Value', ns)}
        if (
            series_key.get('tax') != 'X_TAX'
            or series_key.get('currency') != 'EUR'
            or series_key.get('nrg_cons') != 'MWH500-1999'
            or series_key.get('freq') != 'S'
            or series_key.get('siec') != 'E7000'
            or series_key.get('unit') != 'KWH'
        ):
            continue

        obs_values = {}
        for obs in series.findall('g:Obs', ns):
            dim_node = obs.find('g:ObsDimension', ns)
            value_node = obs.find('g:ObsValue', ns)
            if dim_node is None or value_node is None:
                continue
            year = dim_node.attrib['value']
            try:
                obs_values[year] = float(value_node.attrib['value'])
            except ValueError:
                continue

        if '2025-S1' in obs_values and '2025-S2' in obs_values:
            geo = series_key['geo']
            price_rows.append({
                'geo': geo,
                'Price_EUR_per_kWh': (obs_values['2025-S1'] + obs_values['2025-S2']) / 2,
            })

    return pd.DataFrame(price_rows)


def build_dataset():
    shares = load_shares_2025()
    prices = load_industrial_prices_eurostat()
    rows = []

    geo_to_country = {
        'AT': 'Austria',
        'BE': 'Belgium',
        'DE': 'Germany',
        'DK': 'Denmark',
        'FI': 'Finland',
        'FR': 'France',
        'EL': 'Greece',
        'IE': 'Ireland',
        'IT': 'Italy',
        'LU': 'Luxembourg',
        'NL': 'Netherlands',
        'PT': 'Portugal',
        'ES': 'Spain',
        'SE': 'Sweden',
        'UK': 'United Kingdom',
        'NO': 'Norway',
        'PL': 'Poland',
        'SK': 'Slovakia',
        'CH': 'Switzerland',
        'CZ': 'Czechia',
        'HU': 'Hungary',
    }

    for _, row in prices.iterrows():
        geo = row['geo']
        country = geo_to_country.get(geo)
        if country is None:
            continue
        share_row = shares.loc[shares['Area'] == country]
        if share_row.empty:
            continue
        share_row = share_row.iloc[0]
        rows.append(
            {
                'Area': country,
                'Label': SHORT_LABELS.get(country, country[:2].upper()),
                'Renewables_share': share_row['Renewables_share'],
                'WindSolar_share': share_row['WindSolar_share'],
                'Price_EUR_per_kWh': row['Price_EUR_per_kWh'],
            }
        )

    return pd.DataFrame(rows).dropna().sort_values('Renewables_share')


def plot_dataset(df):
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, axes = plt.subplots(1, 2, figsize=(15, 8))
    fig.subplots_adjust(bottom=0.15)
    panel_info = [
        ('Renewables_share', 'Total renewables share (2025) (%)', 'Panel a'),
        ('WindSolar_share', 'Wind + solar share (2025) (%)', 'Panel b'),
    ]

    for ax, (xcol, xlabel, panel_title) in zip(axes, panel_info):
        x = df[xcol]
        y = df['Price_EUR_per_kWh']
        ax.scatter(x, y, color='#FFB300', edgecolor='black', linewidth=0.6, s=110, zorder=4)

        slope, intercept = np.polyfit(x, y, 1)
        xs = np.linspace(x.min() * 0.95, x.max() * 1.05, 120)
        ax.plot(xs, slope * xs + intercept, color='#4D4D4D', linestyle='--', linewidth=1.8, zorder=3)

        for _, point in df.iterrows():
            ax.text(
                point[xcol],
                point['Price_EUR_per_kWh'],
                point['Label'],
                fontsize=9,
                fontweight='bold',
                ha='center',
                va='center',
                color='#202020',
                bbox=dict(facecolor='white', alpha=0.75, edgecolor='none', pad=0.8),
            )

        ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
        if ax is axes[0]:
            ax.set_ylabel('Industrial price (€/kWh) excl. taxes', fontsize=12, fontweight='bold')
        ax.set_title(panel_title, fontsize=14, fontweight='bold', pad=14)
        ax.set_ylim(bottom=0)
        ax.set_xlim(left=0)
        correlation = np.corrcoef(x, y)[0, 1]
        ax.text(
            0.98,
            0.04,
            f'r = {correlation:.2f}',
            transform=ax.transAxes,
            ha='right',
            va='bottom',
            fontsize=11,
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=0.8),
        )

    fig.suptitle(
        'Industrial price excl. taxes vs 2025 renewables shares',
        fontsize=16,
        fontweight='bold',
        y=0.98,
    )
    fig.text(
        0.5,
        0.04,
        'Note: 2025 shares are averages of monthly values. Industrial prices are Eurostat nrg_pc_205 2025 industrial prices excluding taxes in EUR/kWh.',
        ha='center',
        fontsize=9,
        color='#303030',
        wrap=True,
    )
    fig.savefig(OUTPUT_IMAGE, dpi=300, transparent=False)
    plt.close(fig)
    print(f'Saved improved chart: {OUTPUT_IMAGE}')


if __name__ == '__main__':
    df = build_dataset()
    plot_dataset(df)
