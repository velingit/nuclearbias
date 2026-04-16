import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
from pathlib import Path
import plotly.graph_objects as go
import plotly.io as pio
from scipy.stats import linregress

from iea_electricity_prices import build_converted_price_series, load_price_tables

BASE_DIR = Path(__file__).resolve().parent
EMBER_CSV = BASE_DIR / 'europe_yearly_full_release_long_format.csv'
IMAGE_OUTPUT_DIR = BASE_DIR / 'jekyll_site' / 'assets' / 'images'
INCLUDE_OUTPUT_DIR = BASE_DIR / 'jekyll_site' / '_includes'
CHART_WIDTH = 11.5
CHART_HEIGHT = 6.4
PLOT_BACKGROUND = '#11161d'
PAPER_BACKGROUND = '#11161d'
GRID_COLOR = 'rgba(255, 255, 255, 0.10)'
MATPLOTLIB_GRID_COLOR = (1.0, 1.0, 1.0, 0.10)
TEXT_COLOR = '#f3f6fb'
MUTED_TEXT_COLOR = '#aab6c5'
LEGEND_BACKGROUND = '#18212b'
LEGEND_TEXT_COLOR = '#f3f6fb'
REGRESSION_LINE_COLOR = '#f4a261'


def format_sidebar_text(text, max_words_per_line=7):
    words = text.split()
    lines = []

    for index in range(0, len(words), max_words_per_line):
        lines.append(' '.join(words[index:index + max_words_per_line]))

    return '\n'.join(lines)


def calculate_regression_stats(scatterplot_data):
    x_values = scatterplot_data['Nuclear_Percent'].to_numpy(dtype=float)
    y_values = scatterplot_data['Price_EUR'].to_numpy(dtype=float)

    regression = linregress(x_values, y_values)

    return {
        'slope': float(regression.slope),
        'intercept': float(regression.intercept),
        'r_squared': float(regression.rvalue ** 2),
        'p_value': float(regression.pvalue),
        'std_err': float(regression.stderr),
        'n': int(len(x_values)),
    }


def build_regression_label(regression_stats):
    slope = regression_stats['slope']
    intercept = regression_stats['intercept']
    r_squared = regression_stats['r_squared']
    p_value = regression_stats['p_value']
    intercept_sign = '+' if intercept >= 0 else '-'
    significance_label = 'significant' if p_value < 0.05 else 'not significant'
    p_value_text = 'p < 0.001' if p_value < 0.001 else f'p = {p_value:.3f}'

    return (
        'Linear regression\\n'
        f'y = {slope:.4f}x {intercept_sign} {abs(intercept):.4f}\\n'
        f'R² = {r_squared:.3f}\n'
        f'{p_value_text} ({significance_label})'
    )


def build_sidebar_html(footnote_text, note_text, regression_label):
    footnote_html = footnote_text.replace('\n', '<br>')
    note_html = note_text.replace('\n', '<br>')
    regression_html = regression_label.replace('\\n', '<br>')
    return (
        f'{footnote_html}'
        '<br><br>'
        f'{note_html}'
        '<br><br>'
        f'{regression_html}'
    )


def collect_scatterplot_data(price_category):
    ember_df = pd.read_csv(EMBER_CSV)
    price_df, exchange_df, _ = load_price_tables(price_category=price_category)

    price_countries = [col for col in price_df.columns if col != 'Year']
    ember_filtered = ember_df[(ember_df['Year'] >= 2000) & (ember_df['Continent'] == 'Europe')].copy()
    all_countries = sorted([
        country for country in ember_filtered['Area'].unique()
        if country not in ['EU', 'Europe', 'G7', 'G20', 'OECD', 'ASEAN']
    ])

    all_data_points = []

    for country in all_countries:
        country_data = ember_filtered[ember_filtered['Area'] == country].copy()
        if len(country_data) == 0:
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
            continue

        gen_data = pd.DataFrame({'Year': sorted(years_available)})
        gen_data['Total_Generation'] = gen_data['Year'].map(total_gen_dict)
        gen_data['Nuclear_Generation'] = gen_data['Year'].map(nuclear_gen_dict)
        gen_data['Nuclear_Percent'] = (
            gen_data['Nuclear_Generation'] / gen_data['Total_Generation'] * 100
        ).fillna(0)
        gen_data = gen_data[gen_data['Nuclear_Percent'] > 0]

        if len(gen_data) == 0 or country not in price_countries:
            continue

        country_prices = build_converted_price_series(price_df, exchange_df, country, output_column='Price_EUR')

        merged = pd.merge(gen_data, country_prices[['Year', 'Price_EUR']], on='Year', how='inner')
        merged = merged.dropna(subset=['Price_EUR'])
        merged = merged[(merged['Year'] >= 2000) & (merged['Year'] <= 2020)]

        if len(merged) == 0:
            continue

        if merged['Year'].min() > 2000 or merged['Year'].max() < 2020:
            continue

        merged['Country'] = country
        all_data_points.append(merged)

    return pd.concat(all_data_points, ignore_index=True)


def build_shared_axis_limits(scatterplot_datasets):
    max_nuclear = max(dataset['Nuclear_Percent'].max() for dataset in scatterplot_datasets)
    max_price = max(dataset['Price_EUR'].max() for dataset in scatterplot_datasets)

    x_upper = max(5, math.ceil((max_nuclear * 1.05) / 5) * 5)
    y_upper = max(0.02, math.ceil((max_price * 1.08) / 0.02) * 0.02)

    return {
        'x': (0, x_upper),
        'y': (0, y_upper),
    }


def get_country_palette(n_countries):
    colors = plt.cm.tab20(np.linspace(0, 1, max(n_countries, 3)))
    if n_countries > 20:
        colors = plt.cm.hsv(np.linspace(0, 1, n_countries))
    return colors


def format_rgb(color):
    red, green, blue = (int(channel * 255) for channel in color[:3])
    return red, green, blue


def render_scatterplot(scatterplot_data, filename, title, ylabel, footnote, axis_limits):
    countries = sorted(scatterplot_data['Country'].unique())
    n_countries = len(countries)
    colors = get_country_palette(n_countries)

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(CHART_WIDTH, CHART_HEIGHT))
    fig.patch.set_facecolor(PAPER_BACKGROUND)
    ax.set_facecolor(PLOT_BACKGROUND)
    min_year = scatterplot_data['Year'].min()
    max_year = scatterplot_data['Year'].max()
    year_range = max_year - min_year if max_year > min_year else 1
    regression_stats = calculate_regression_stats(scatterplot_data)
    footnote_text = format_sidebar_text(footnote, max_words_per_line=6)
    note_text = format_sidebar_text(
        'Note: Marker opacity increases from 2000 to 2020 to highlight temporal progression.',
        max_words_per_line=6,
    )
    regression_text = build_regression_label(regression_stats)
    sidebar_text = (
        f'{footnote_text}\n\n'
        f'{note_text}\n\n'
        f'{regression_text.replace("\\n", "\n")}'
    )

    for idx, country in enumerate(countries):
        country_data = scatterplot_data[scatterplot_data['Country'] == country]
        color = colors[idx % len(colors)]

        for _, row in country_data.iterrows():
            year_normalized = (row['Year'] - min_year) / year_range if year_range > 0 else 1
            alpha = 0.3 + (year_normalized * 0.65)
            ax.scatter(
                row['Nuclear_Percent'],
                row['Price_EUR'],
                marker='o',
                s=115,
                color=color,
                alpha=alpha,
                edgecolors='none',
                linewidth=0,
                zorder=3,
            )

        if len(country_data[country_data['Year'] == country_data['Year'].max()]) > 0:
            ax.scatter([], [], label=country, marker='o', s=115, color=color, alpha=0.95,
                       edgecolors='#e8eef7', linewidth=0.5)

    ax.set_xlabel('Nuclear Capacity as % of Generation', fontsize=12, fontweight='bold', color=TEXT_COLOR)
    ax.set_ylabel(ylabel, fontsize=12, fontweight='bold', color=TEXT_COLOR)
    ax.set_title(title, fontsize=13, fontweight='bold', pad=16, color=TEXT_COLOR)
    ax.grid(True, alpha=0.6, linestyle='--', color=MATPLOTLIB_GRID_COLOR, zorder=1)
    legend = ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=8.8, framealpha=0.98, title='Country', title_fontsize=10)
    legend.get_frame().set_facecolor(LEGEND_BACKGROUND)
    legend.get_frame().set_edgecolor('#425268')
    plt.setp(legend.get_texts(), color=LEGEND_TEXT_COLOR)
    plt.setp(legend.get_title(), color=LEGEND_TEXT_COLOR)
    ax.set_xlim(*axis_limits['x'])
    ax.set_ylim(*axis_limits['y'])
    ax.tick_params(colors=TEXT_COLOR)

    for spine in ax.spines.values():
        spine.set_color('#425268')

    fig.text(
        0.80,
        0.29,
        sidebar_text,
        ha='left',
        va='top',
        fontsize=7.9,
        color=TEXT_COLOR,
    )

    plt.tight_layout(rect=[0, 0.06, 0.84, 1])
    IMAGE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = IMAGE_OUTPUT_DIR / filename
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    return output_path, countries


def render_interactive_scatterplot(
    scatterplot_data,
    include_filename,
    title,
    ylabel,
    footnote,
    axis_limits,
    regression_dash='solid',
):
    countries = sorted(scatterplot_data['Country'].unique())
    colors = get_country_palette(len(countries))
    min_year = scatterplot_data['Year'].min()
    max_year = scatterplot_data['Year'].max()
    year_range = max_year - min_year if max_year > min_year else 1
    regression_stats = calculate_regression_stats(scatterplot_data)
    footnote_text = format_sidebar_text(footnote, max_words_per_line=6)
    note_text = format_sidebar_text(
        'Note: Marker opacity increases from 2000 (fainter) to 2020 (solid) to highlight temporal progression.',
        max_words_per_line=6,
    )
    regression_label = build_regression_label(regression_stats)
    sidebar_annotation_text = build_sidebar_html(footnote_text, note_text, regression_label)

    fig = go.Figure()

    for idx, country in enumerate(countries):
        country_data = scatterplot_data[scatterplot_data['Country'] == country].sort_values('Year')
        red, green, blue = format_rgb(colors[idx % len(colors)])
        marker_colors = []

        for year in country_data['Year']:
            year_normalized = (year - min_year) / year_range if year_range > 0 else 1
            alpha = 0.3 + (year_normalized * 0.65)
            marker_colors.append(f'rgba({red}, {green}, {blue}, {alpha:.3f})')

        fig.add_trace(
            go.Scatter(
                x=country_data['Nuclear_Percent'],
                y=country_data['Price_EUR'],
                mode='markers',
                name=country,
                marker={
                    'size': 13,
                    'color': marker_colors,
                    'line': {'color': 'rgba(0, 0, 0, 0)', 'width': 0},
                },
                customdata=country_data[['Country', 'Year']],
                hovertemplate=(
                    '<b>%{customdata[0]}</b><br>'
                    'Year: %{customdata[1]}<br>'
                    'Nuclear share: %{x:.1f}%<br>'
                    'Price: %{y:.3f} €/kWh<extra></extra>'
                ),
            )
        )

    regression_x = np.array(axis_limits['x'], dtype=float)
    regression_y = regression_stats['slope'] * regression_x + regression_stats['intercept']

    fig.add_trace(
        go.Scatter(
            x=regression_x,
            y=regression_y,
            mode='lines',
            name='Linear regression',
            visible=True,
            showlegend=False,
            line={'color': REGRESSION_LINE_COLOR, 'width': 3, 'dash': regression_dash},
            hovertemplate=(
                '<b>Linear regression</b><br>'
                'Predicted price: %{y:.3f} €/kWh<br>'
                'Nuclear share: %{x:.1f}%<extra></extra>'
            ),
        )
    )

    country_trace_count = len(countries)
    regression_hidden = [True] * country_trace_count + [False]
    regression_visible = [True] * country_trace_count + [True]

    fig.update_layout(
        title={'text': title, 'x': 0.46, 'y': 0.97},
        template='plotly_dark',
        hovermode='closest',
        height=560,
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PLOT_BACKGROUND,
        font={'color': TEXT_COLOR, 'size': 13},
        margin={'l': 72, 'r': 330, 't': 92, 'b': 72},
        legend={
            'title': {'text': 'Country'},
            'orientation': 'v',
            'bgcolor': LEGEND_BACKGROUND,
            'font': {'color': LEGEND_TEXT_COLOR, 'size': 12},
            'title_font': {'color': LEGEND_TEXT_COLOR, 'size': 14},
            'bordercolor': '#425268',
            'borderwidth': 1,
            'yanchor': 'top',
            'y': 0.93,
            'xanchor': 'left',
            'x': 1.02,
        },
        updatemenus=[
            {
                'type': 'buttons',
                'direction': 'left',
                'x': 1.02,
                'y': 1.01,
                'xanchor': 'left',
                'yanchor': 'top',
                'showactive': False,
                'bgcolor': '#223041',
                'bordercolor': '#425268',
                'font': {'color': TEXT_COLOR, 'size': 11},
                'pad': {'r': 6, 't': 0, 'b': 0},
                'buttons': [
                    {
                        'label': 'Regression off',
                        'method': 'update',
                        'args': [{'visible': regression_hidden}],
                    },
                    {
                        'label': 'Regression on',
                        'method': 'update',
                        'args': [{'visible': regression_visible}],
                    },
                ],
            }
        ],
        xaxis={
            'title': 'Nuclear Capacity as % of Generation',
            'range': list(axis_limits['x']),
            'ticksuffix': '%',
            'gridcolor': GRID_COLOR,
            'linecolor': '#425268',
            'zeroline': False,
        },
        yaxis={
            'title': ylabel,
            'range': list(axis_limits['y']),
            'tickformat': '.2f',
            'gridcolor': GRID_COLOR,
            'linecolor': '#425268',
            'zeroline': False,
        },
        annotations=[
            {
                'xref': 'paper',
                'yref': 'paper',
                'x': 1.02,
                'y': 0.34,
                'showarrow': False,
                'align': 'left',
                'xanchor': 'left',
                'yanchor': 'top',
                'text': sidebar_annotation_text,
                'font': {'size': 10, 'color': TEXT_COLOR},
            },
        ],
    )

    html = pio.to_html(
        fig,
        full_html=False,
        include_plotlyjs='cdn',
        config={
            'responsive': True,
            'displaylogo': False,
            'toImageButtonOptions': {'format': 'png', 'filename': include_filename.replace('.html', '')},
        },
    )

    INCLUDE_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = INCLUDE_OUTPUT_DIR / include_filename
    output_path.write_text(html, encoding='utf-8')
    return output_path


def main():
    chart_configs = [
        {
            'price_category': 'household',
            'filename': 'nuclear_vs_price_scatterplot.png',
            'include_filename': 'scatterplot_household.html',
            'title': 'European Nuclear Capacity (%) vs Household Electricity Prices (2000-2020)',
            'ylabel': 'Household Electricity Price (€/kWh) excl. taxes',
            'footnote': 'Data sources: Ember (nuclear generation %), UK Government IEA Table 5.5.1 (household electricity prices excl. taxes)',
            'label': 'household',
            'regression_dash': 'solid',
        },
        {
            'price_category': 'industrial',
            'filename': 'nuclear_vs_industrial_price_scatterplot.png',
            'include_filename': 'scatterplot_industrial.html',
            'title': 'European Nuclear Capacity (%) vs Industrial Electricity Prices (2000-2020)',
            'ylabel': 'Industrial Electricity Price (€/kWh) excl. taxes',
            'footnote': 'Data sources: Ember (nuclear generation %), UK Government IEA Table 5.3.1 (industrial electricity prices excl. taxes)',
            'label': 'industrial',
            'regression_dash': 'dash',
        },
    ]

    scatterplot_datasets = {
        config['price_category']: collect_scatterplot_data(config['price_category'])
        for config in chart_configs
    }
    axis_limits = build_shared_axis_limits(scatterplot_datasets.values())

    for config in chart_configs:
        scatterplot_data = scatterplot_datasets[config['price_category']]
        output_path, countries = render_scatterplot(
            scatterplot_data,
            config['filename'],
            config['title'],
            config['ylabel'],
            config['footnote'],
            axis_limits,
        )
        include_path = render_interactive_scatterplot(
            scatterplot_data,
            config['include_filename'],
            config['title'],
            config['ylabel'],
            config['footnote'],
            axis_limits,
            regression_dash=config.get('regression_dash', 'solid'),
        )
        print(f"[+] {config['label'].capitalize()} scatterplot saved as: {output_path}")
        print(f"[+] {config['label'].capitalize()} interactive scatterplot saved as: {include_path}")
        print(
            f"\n{config['label'].capitalize()} scatterplot contains {len(scatterplot_data)} data points from {len(countries)} countries:"
        )
        for country in countries:
            n_points = len(scatterplot_data[scatterplot_data['Country'] == country])
            print(f"  - {country}: {n_points} data points")

    print(
        f"\nShared axis limits applied to both scatterplots: x={axis_limits['x'][0]}-{axis_limits['x'][1]}%, y={axis_limits['y'][0]:.2f}-{axis_limits['y'][1]:.2f} €/kWh"
    )


if __name__ == '__main__':
    main()
