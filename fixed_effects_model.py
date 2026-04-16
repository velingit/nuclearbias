import pandas as pd
import numpy as np
from pathlib import Path
from linearmodels.panel import PanelOLS
from scipy.stats import linregress

from scatterplot_nuclear_vs_price import collect_scatterplot_data

BASE_DIR = Path(__file__).resolve().parent


def build_panel_dataset(price_category='household'):
    data = collect_scatterplot_data(price_category)
    data = data[['Country', 'Year', 'Nuclear_Percent', 'Price_EUR']].copy()
    data = data.set_index(['Country', 'Year'])
    return data


def run_pooled_fixed_effects(panel_data):
    model = PanelOLS(
        dependent=panel_data['Price_EUR'],
        exog=panel_data[['Nuclear_Percent']],
        entity_effects=True,
    )
    result = model.fit(cov_type='clustered', cluster_entity=True)
    return result


def run_country_regressions(data):
    data_flat = data.reset_index()
    countries = sorted(data_flat['Country'].unique())
    results = []

    for country in countries:
        country_data = data_flat[data_flat['Country'] == country].sort_values('Year')
        x = country_data['Nuclear_Percent'].to_numpy(dtype=float)
        y = country_data['Price_EUR'].to_numpy(dtype=float)

        regression = linregress(x, y)
        results.append({
            'Country': country,
            'N': len(x),
            'Nuclear_Pct_Mean': float(np.mean(x)),
            'Nuclear_Pct_Std': float(np.std(x)),
            'Price_Mean': float(np.mean(y)),
            'Price_Std': float(np.std(y)),
            'Slope': float(regression.slope),
            'Intercept': float(regression.intercept),
            'R_squared': float(regression.rvalue ** 2),
            'P_value': float(regression.pvalue),
            'Std_err': float(regression.stderr),
        })

    return pd.DataFrame(results)


def print_section(title):
    width = 80
    print('\n' + '=' * width)
    print(f' {title}')
    print('=' * width)


def format_p_value(p):
    if p < 0.001:
        return 'p < 0.001 ***'
    elif p < 0.01:
        return f'p = {p:.4f} **'
    elif p < 0.05:
        return f'p = {p:.4f} *'
    elif p < 0.10:
        return f'p = {p:.4f} .'
    else:
        return f'p = {p:.4f}'


def main():
    print_section('FIXED-EFFECTS PANEL REGRESSION: Nuclear Share vs Household Electricity Price')
    print('Model: Price_EUR_it = alpha_i + beta * Nuclear_Percent_it + epsilon_it')
    print('Where alpha_i = country-specific fixed effect (intercept)')
    print('Data: 10 European countries, 2000-2020')
    print('Dependent variable: Household electricity price (EUR/kWh, excl. taxes)')
    print('Independent variable: Nuclear generation as % of total generation')

    panel_data = build_panel_dataset('household')
    data_flat = panel_data.reset_index()
    print(f'\nPanel dimensions: {len(data_flat["Country"].unique())} countries, '
          f'{len(data_flat)} observations')

    # ── Part 1: Panel fixed-effects model (all countries pooled) ─────────────
    print_section('PART 1: PANEL FIXED-EFFECTS MODEL (Entity = Country)')

    fe_result = run_pooled_fixed_effects(panel_data)
    print(fe_result.summary)

    # ── Part 2: Country-specific fixed effects (intercepts) ──────────────────
    print_section('PART 2: ESTIMATED COUNTRY FIXED EFFECTS (alpha_i)')
    print('These represent each country\'s baseline price level after controlling')
    print('for the within-country effect of nuclear share.\n')

    estimated_effects = fe_result.estimated_effects
    effects_df = estimated_effects.reset_index()
    effects_df.columns = ['Country', 'Year', 'Fixed_Effect']
    country_effects = effects_df.groupby('Country')['Fixed_Effect'].mean().sort_values()

    overall_mean = data_flat['Price_EUR'].mean()
    print(f'Overall mean price: {overall_mean:.4f} EUR/kWh\n')
    print(f'{"Country":<20} {"Fixed Effect":>14} {"Implied Baseline":>18}')
    print('-' * 54)
    for country, effect in country_effects.items():
        baseline = overall_mean + effect
        print(f'{country:<20} {effect:>+14.4f} {baseline:>14.4f} EUR/kWh')

    # ── Part 3: Individual country OLS regressions ───────────────────────────
    print_section('PART 3: INDIVIDUAL COUNTRY OLS REGRESSIONS')
    print('Within-country time-series regressions (Nuclear % -> Price)\n')

    country_results = run_country_regressions(panel_data)

    print(f'{"Country":<16} {"N":>3} {"Slope":>10} {"Intercept":>10} '
          f'{"R²":>8} {"Std Err":>9} {"Significance":>18}')
    print('-' * 78)
    for _, row in country_results.iterrows():
        sig = format_p_value(row['P_value'])
        print(f'{row["Country"]:<16} {row["N"]:>3} {row["Slope"]:>+10.5f} '
              f'{row["Intercept"]:>10.4f} {row["R_squared"]:>8.3f} '
              f'{row["Std_err"]:>9.5f} {sig:>18}')

    # ── Part 4: Summary statistics per country ───────────────────────────────
    print_section('PART 4: DESCRIPTIVE STATISTICS BY COUNTRY')
    print(f'\n{"Country":<16} {"Nuc% Mean":>10} {"Nuc% Std":>10} '
          f'{"Price Mean":>12} {"Price Std":>10} {"Year Range":>12}')
    print('-' * 74)
    for _, row in country_results.iterrows():
        country_data = data_flat[data_flat['Country'] == row['Country']]
        yr_min, yr_max = int(country_data['Year'].min()), int(country_data['Year'].max())
        print(f'{row["Country"]:<16} {row["Nuclear_Pct_Mean"]:>10.2f} '
              f'{row["Nuclear_Pct_Std"]:>10.2f} {row["Price_Mean"]:>10.4f} '
              f'{row["Price_Std"]:>12.4f} {yr_min:>5}-{yr_max}')

    # ── Part 5: Interpretation ───────────────────────────────────────────────
    print_section('INTERPRETATION')
    beta = fe_result.params['Nuclear_Percent']
    beta_p = fe_result.pvalues['Nuclear_Percent']
    r2_within = fe_result.rsquared_within
    r2_overall = fe_result.rsquared_overall

    print(f'Fixed-effects coefficient (beta): {beta:+.5f} EUR/kWh per 1pp nuclear share')
    print(f'Significance: {format_p_value(beta_p)}')
    print(f'R² (within):  {r2_within:.4f}')
    print(f'R² (overall): {r2_overall:.4f}')
    print(f'\nA 1 percentage-point increase in nuclear share is associated with a')
    print(f'{beta:+.5f} EUR/kWh change in household electricity price (within-country).')

    sig_countries = country_results[country_results['P_value'] < 0.05]
    if len(sig_countries) > 0:
        print(f'\nCountries with individually significant slopes (p < 0.05):')
        for _, row in sig_countries.iterrows():
            print(f'  {row["Country"]}: slope = {row["Slope"]:+.5f}, '
                  f'R² = {row["R_squared"]:.3f}, {format_p_value(row["P_value"])}')
    else:
        print('\nNo individual country has a statistically significant slope at p < 0.05.')


if __name__ == '__main__':
    main()
