from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

from iea_electricity_prices import build_converted_price_series, load_price_tables


BASE_DIR = Path(__file__).resolve().parent
EMBER_CSV = BASE_DIR / 'europe_yearly_full_release_long_format.csv'
IMAGE_OUTPUT_DIR = BASE_DIR / 'jekyll_site' / 'assets' / 'images'
EXCLUDED_AREAS = ['EU', 'Europe', 'G7', 'G20', 'OECD', 'ASEAN']

PRICE_CONFIGS = {
    'household': {
        'price_axis_label': 'Household electricity price (€/kWh)',
        'series_label': 'Household price (€/kWh)',
        'combined_filename': 'All_Countries_Combined.png',
        'combined_title': 'European Nuclear Capacity (%) and Household Electricity Prices (€/kWh) - 2000-2020',
        'footnote': 'Data sources: Ember (nuclear generation %), UK Government IEA Table 5.5.1 (household electricity prices excl. taxes)',
        'country_filename_suffix': '_nuclear_price.png',
        'country_title_suffix': 'Household Electricity Prices',
        'generate_individual': True,
    },
    'industrial': {
        'price_axis_label': 'Industrial electricity price (€/kWh)',
        'series_label': 'Industrial price (€/kWh)',
        'combined_filename': 'All_Countries_Combined_Industrial.png',
        'combined_title': 'European Nuclear Capacity (%) and Industrial Electricity Prices (€/kWh) - 2000-2020',
        'footnote': 'Data sources: Ember (nuclear generation %), UK Government IEA Table 5.3.1 (industrial electricity prices excl. taxes)',
        'country_filename_suffix': '_nuclear_industrial_price.png',
        'country_title_suffix': 'Industrial Electricity Prices',
        'generate_individual': False,
    },
}


def load_generation_data():
    ember_df = pd.read_csv(EMBER_CSV)
    return ember_df[
        ((ember_df['Year'] >= 2000) & (ember_df['Year'] <= 2020))
        & (ember_df['Continent'] == 'Europe')
    ].copy()


def collect_country_series(price_category):
    ember_filtered = load_generation_data()
    price_df, exchange_df, _ = load_price_tables(price_category=price_category)
    price_countries = [col for col in price_df.columns if col != 'Year']
    all_countries = sorted([
        country for country in ember_filtered['Area'].unique()
        if country not in EXCLUDED_AREAS
    ])

    successful_countries = []
    filtered_countries = []
    country_data_dict = {}

    for country in all_countries:
        country_data = ember_filtered[ember_filtered['Area'] == country].copy()

        if len(country_data) == 0:
            filtered_countries.append(f'{country} (no generation data)')
            continue

        total_gen = country_data[
            (country_data['Variable'] == 'Total generation') & (country_data['Unit'] == 'TWh')
        ]
        nuclear_gen = country_data[
            (country_data['Variable'] == 'Nuclear') & (country_data['Unit'] == 'TWh')
        ]

        total_gen_dict = dict(zip(total_gen['Year'], total_gen['Value']))
        nuclear_gen_dict = dict(zip(nuclear_gen['Year'], nuclear_gen['Value']))
        years_available = set(total_gen_dict.keys()) & set(nuclear_gen_dict.keys())

        if len(years_available) == 0:
            filtered_countries.append(f'{country} (no nuclear data)')
            continue

        gen_data = pd.DataFrame({'Year': sorted(years_available)})
        gen_data['Total_Generation'] = gen_data['Year'].map(total_gen_dict)
        gen_data['Nuclear_Generation'] = gen_data['Year'].map(nuclear_gen_dict)
        gen_data['Nuclear_Percent'] = (
            gen_data['Nuclear_Generation'] / gen_data['Total_Generation'] * 100
        ).fillna(0)
        gen_data = gen_data[gen_data['Nuclear_Percent'] > 0]

        if len(gen_data) == 0:
            filtered_countries.append(f'{country} (no nuclear generation in period)')
            continue

        if country not in price_countries:
            filtered_countries.append(f'{country} (no price data)')
            continue

        country_prices = build_converted_price_series(
            price_df,
            exchange_df,
            country,
            output_column='Price_EUR',
        )

        merged = pd.merge(gen_data, country_prices[['Year', 'Price_EUR']], on='Year', how='inner')
        merged = merged.dropna(subset=['Price_EUR'])
        merged = merged[(merged['Year'] >= 2000) & (merged['Year'] <= 2020)]

        if len(merged) == 0:
            continue

        if merged['Year'].min() > 2000 or merged['Year'].max() < 2020:
            filtered_countries.append(
                f"{country} (data range: {int(merged['Year'].min())}-{int(merged['Year'].max())})"
            )
            continue

        country_data_dict[country] = merged
        successful_countries.append(country)

    return successful_countries, filtered_countries, country_data_dict


def render_individual_chart(country, merged, config):
    fig, ax1 = plt.subplots(figsize=(12, 6))

    color1 = '#2E86AB'
    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Nuclear Capacity as % of Generation', fontsize=11, fontweight='bold', color=color1)
    line1 = ax1.plot(
        merged['Year'],
        merged['Nuclear_Percent'],
        'o-',
        linewidth=2.5,
        markersize=6,
        color=color1,
        label='Nuclear %',
        zorder=3,
    )
    ax1.fill_between(merged['Year'], merged['Nuclear_Percent'], alpha=0.2, color=color1, zorder=2)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.3, axis='y', zorder=0)
    ax1.set_ylim(bottom=0)

    ax2 = ax1.twinx()
    color2 = '#A23B72'
    ax2.set_ylabel(config['price_axis_label'], fontsize=11, fontweight='bold', color=color2)
    line2 = ax2.plot(
        merged['Year'],
        merged['Price_EUR'],
        's-',
        linewidth=2.5,
        markersize=6,
        color=color2,
        label=config['series_label'],
        zorder=3,
    )
    ax2.tick_params(axis='y', labelcolor=color2)
    ax2.set_ylim(bottom=0)

    plt.title(
        f"{country}: Nuclear Capacity % and {config['country_title_suffix']} (2000-2020)",
        fontsize=13,
        fontweight='bold',
        pad=15,
    )

    lines = line1 + line2
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, loc='upper left', fontsize=10)

    years = merged['Year'].values
    xtick_interval = 2 if len(years) > 20 else 1
    ax1.set_xticks(range(int(min(years)), int(max(years)) + 1, xtick_interval))
    ax1.set_xticklabels(range(int(min(years)), int(max(years)) + 1, xtick_interval), rotation=45)

    fig.text(0.12, 0.02, config['footnote'], ha='left', fontsize=8, style='italic', color='gray')
    plt.tight_layout(rect=[0, 0.03, 1, 1])

    filename = IMAGE_OUTPUT_DIR / f"{country.replace(' ', '_')}{config['country_filename_suffix']}"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[+] Generated chart for: {country}")


def render_combined_chart(successful_countries, country_data_dict, config):
    n_countries = len(successful_countries)
    n_cols = 4
    n_rows = (n_countries + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 4 * n_rows))
    axes = axes.flatten()

    for idx, country in enumerate(sorted(successful_countries)):
        merged = country_data_dict[country]
        ax1 = axes[idx]

        color1 = '#2E86AB'
        ax1.set_xlabel('Year', fontsize=9, fontweight='bold')
        ax1.set_ylabel('Nuclear %', fontsize=9, fontweight='bold', color=color1)
        ax1.plot(merged['Year'], merged['Nuclear_Percent'], 'o-', linewidth=2, markersize=4, color=color1, zorder=3)
        ax1.fill_between(merged['Year'], merged['Nuclear_Percent'], alpha=0.2, color=color1, zorder=2)
        ax1.tick_params(axis='y', labelcolor=color1, labelsize=8)
        ax1.tick_params(axis='x', labelsize=8)
        ax1.grid(True, alpha=0.3, axis='y', zorder=0)
        ax1.set_ylim(bottom=0)

        ax2 = ax1.twinx()
        color2 = '#A23B72'
        ax2.set_ylabel(config['series_label'], fontsize=9, fontweight='bold', color=color2)
        ax2.plot(merged['Year'], merged['Price_EUR'], 's-', linewidth=2, markersize=4, color=color2, zorder=3)
        ax2.tick_params(axis='y', labelcolor=color2, labelsize=8)
        ax2.set_ylim(bottom=0)

        ax1.set_title(country, fontsize=10, fontweight='bold', pad=10)

        years = merged['Year'].values
        if len(years) > 15:
            xtick_interval = 5
        elif len(years) > 10:
            xtick_interval = 3
        else:
            xtick_interval = 2

        ax1.set_xticks(range(int(min(years)), int(max(years)) + 1, xtick_interval))
        ax1.set_xticklabels(range(int(min(years)), int(max(years)) + 1, xtick_interval), rotation=45, fontsize=7)

    for idx in range(n_countries, len(axes)):
        axes[idx].axis('off')

    fig.suptitle(config['combined_title'], fontsize=16, fontweight='bold', y=0.995)
    fig.text(0.5, 0.01, config['footnote'], ha='center', fontsize=9, style='italic', color='gray')
    plt.tight_layout(rect=[0, 0.02, 1, 0.99])

    combined_filename = IMAGE_OUTPUT_DIR / config['combined_filename']
    plt.savefig(combined_filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[+] Generated combined chart: {combined_filename}")


def main():
    IMAGE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for price_category, config in PRICE_CONFIGS.items():
        print(f"\nGenerating {price_category} charts")
        successful_countries, filtered_countries, country_data_dict = collect_country_series(price_category)

        if config['generate_individual']:
            for country in successful_countries:
                render_individual_chart(country, country_data_dict[country], config)

        render_combined_chart(successful_countries, country_data_dict, config)

        print(
            f"[+] Successfully generated {len(successful_countries)} country series for {price_category}; combined chart saved to {IMAGE_OUTPUT_DIR}"
        )

        if filtered_countries:
            print(f"[-] Filtered out {len(filtered_countries)} countries for {price_category}:")
            for country in sorted(filtered_countries):
                print(f"  - {country}")


if __name__ == '__main__':
    main()
