import numpy as np
import pandas as pd
from pathlib import Path
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio
from scipy.stats import linregress, t as t_dist

from fixed_effects_model import build_panel_dataset, run_pooled_fixed_effects, run_country_regressions

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / 'jekyll_site' / '_includes'

PLOT_BG = '#11161d'
PAPER_BG = '#11161d'
GRID_COLOR = 'rgba(255, 255, 255, 0.10)'
TEXT_COLOR = '#f3f6fb'
MUTED_COLOR = '#aab6c5'
REGRESSION_COLOR = '#f4a261'
ACCENT_POSITIVE = '#2a9d8f'
ACCENT_NEGATIVE = '#e76f51'
ACCENT_NEUTRAL = '#6c757d'

COUNTRY_COLORS = {
    'Belgium': '#1f77b4',
    'Finland': '#ff7f0e',
    'France': '#2ca02c',
    'Germany': '#d62728',
    'Hungary': '#9467bd',
    'Netherlands': '#8c564b',
    'Slovakia': '#e377c2',
    'Spain': '#7f7f7f',
    'Switzerland': '#bcbd22',
    'United Kingdom': '#17becf',
}


def build_country_regression_details(data_flat):
    countries = sorted(data_flat['Country'].unique())
    results = []
    for country in countries:
        cd = data_flat[data_flat['Country'] == country].sort_values('Year')
        x = cd['Nuclear_Percent'].to_numpy(dtype=float)
        y = cd['Price_EUR'].to_numpy(dtype=float)
        reg = linregress(x, y)
        n = len(x)
        dof = n - 2
        t_crit = t_dist.ppf(0.975, dof)
        ci_low = reg.slope - t_crit * reg.stderr
        ci_high = reg.slope + t_crit * reg.stderr
        results.append({
            'Country': country,
            'N': n,
            'Slope': reg.slope,
            'Intercept': reg.intercept,
            'R_squared': reg.rvalue ** 2,
            'P_value': reg.pvalue,
            'Std_err': reg.stderr,
            'CI_low': ci_low,
            'CI_high': ci_high,
            'x': x,
            'y': y,
            'x_min': x.min(),
            'x_max': x.max(),
        })
    return results


def sig_label(p):
    if p < 0.001:
        return '***'
    elif p < 0.01:
        return '**'
    elif p < 0.05:
        return '*'
    elif p < 0.10:
        return '†'
    return ''


# ── Chart 1: Small multiples ────────────────────────────────────────────────

def render_small_multiples(data_flat, country_details):
    countries = [d['Country'] for d in country_details]
    n_cols = 5
    n_rows = 2

    fig = make_subplots(
        rows=n_rows, cols=n_cols,
        subplot_titles=[
            f"<b>{d['Country']}</b>  R²={d['R_squared']:.3f}{sig_label(d['P_value'])}"
            for d in country_details
        ],
        horizontal_spacing=0.055,
        vertical_spacing=0.13,
    )

    for idx, d in enumerate(country_details):
        row = idx // n_cols + 1
        col = idx % n_cols + 1
        color = COUNTRY_COLORS.get(d['Country'], '#aab6c5')

        min_year = int(data_flat[data_flat['Country'] == d['Country']]['Year'].min())
        max_year = int(data_flat[data_flat['Country'] == d['Country']]['Year'].max())
        year_range = max_year - min_year if max_year > min_year else 1
        cd = data_flat[data_flat['Country'] == d['Country']].sort_values('Year')

        marker_colors = []
        for yr in cd['Year']:
            norm = (yr - min_year) / year_range
            alpha = 0.35 + norm * 0.60
            r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
            marker_colors.append(f'rgba({r},{g},{b},{alpha:.2f})')

        fig.add_trace(
            go.Scatter(
                x=cd['Nuclear_Percent'], y=cd['Price_EUR'],
                mode='markers',
                marker=dict(size=8, color=marker_colors),
                customdata=np.column_stack([cd['Country'], cd['Year']]),
                hovertemplate='<b>%{customdata[0]}</b> %{customdata[1]}<br>'
                              'Nuclear: %{x:.1f}%<br>Price: %{y:.3f} €/kWh<extra></extra>',
                showlegend=False,
            ),
            row=row, col=col,
        )

        reg_x = np.linspace(d['x_min'] - 1, d['x_max'] + 1, 50)
        reg_y = d['Slope'] * reg_x + d['Intercept']
        line_color = ACCENT_NEGATIVE if d['Slope'] < 0 else ACCENT_POSITIVE
        dash = 'solid' if d['P_value'] < 0.05 else 'dot'

        fig.add_trace(
            go.Scatter(
                x=reg_x, y=reg_y,
                mode='lines',
                line=dict(color=line_color, width=2.5, dash=dash),
                hovertemplate=f'slope={d["Slope"]:+.5f}<extra></extra>',
                showlegend=False,
            ),
            row=row, col=col,
        )

    for i in range(1, n_rows * n_cols + 1):
        fig.update_xaxes(
            gridcolor=GRID_COLOR, linecolor='#425268', zeroline=False,
            tickfont=dict(size=9, color=MUTED_COLOR),
            row=(i - 1) // n_cols + 1, col=(i - 1) % n_cols + 1,
        )
        fig.update_yaxes(
            gridcolor=GRID_COLOR, linecolor='#425268', zeroline=False,
            tickformat='.2f',
            tickfont=dict(size=9, color=MUTED_COLOR),
            row=(i - 1) // n_cols + 1, col=(i - 1) % n_cols + 1,
        )

    fig.update_xaxes(title_text='Nuclear %', row=2, col=3, title_font=dict(size=11, color=MUTED_COLOR))
    fig.update_yaxes(title_text='€/kWh', row=1, col=1, title_font=dict(size=11, color=MUTED_COLOR))
    fig.update_yaxes(title_text='€/kWh', row=2, col=1, title_font=dict(size=11, color=MUTED_COLOR))

    fig.update_layout(
        title=dict(
            text='<b>Country-Level Regressions: Nuclear Share vs Household Electricity Price</b>'
                 '<br><sub>Solid line = significant (p&lt;0.05) · Dotted = not significant · '
                 'Red = negative slope · Green = positive slope · Opacity = year (faint→solid = 2000→2020)</sub>',
            x=0.5, font=dict(size=15, color=TEXT_COLOR),
        ),
        height=520,
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(color=TEXT_COLOR, size=11),
        margin=dict(l=60, r=30, t=100, b=60),
    )

    for ann in fig.layout.annotations:
        ann.font = dict(size=11, color=TEXT_COLOR)

    return fig


# ── Chart 2: Forest / coefficient plot ─────────────────────────────────────

def render_forest_plot(country_details, fe_result):
    sorted_details = sorted(country_details, key=lambda d: d['Slope'])

    panel_beta = fe_result.params['Nuclear_Percent']
    panel_se = fe_result.std_errors['Nuclear_Percent']
    panel_p = fe_result.pvalues['Nuclear_Percent']
    panel_ci_low = panel_beta - 1.96 * panel_se
    panel_ci_high = panel_beta + 1.96 * panel_se

    labels = [d['Country'] for d in sorted_details] + ['', 'Panel FE (pooled)']
    slopes = [d['Slope'] for d in sorted_details] + [None, panel_beta]
    ci_lows = [d['CI_low'] for d in sorted_details] + [None, panel_ci_low]
    ci_highs = [d['CI_high'] for d in sorted_details] + [None, panel_ci_high]
    p_values = [d['P_value'] for d in sorted_details] + [None, panel_p]

    fig = go.Figure()

    # Zero reference line
    fig.add_vline(x=0, line=dict(color='rgba(255,255,255,0.3)', width=1, dash='dash'))

    # Country estimates
    for i, d in enumerate(sorted_details):
        color = ACCENT_NEGATIVE if d['Slope'] < 0 else ACCENT_POSITIVE
        if d['P_value'] >= 0.05:
            color = ACCENT_NEUTRAL
        sig = sig_label(d['P_value'])

        fig.add_trace(go.Scatter(
            x=[d['CI_low'], d['CI_high']],
            y=[d['Country'], d['Country']],
            mode='lines',
            line=dict(color=color, width=3),
            showlegend=False,
            hoverinfo='skip',
        ))
        fig.add_trace(go.Scatter(
            x=[d['Slope']],
            y=[d['Country']],
            mode='markers+text',
            marker=dict(size=12, color=color, symbol='diamond'),
            text=[f"  {d['Slope']:+.5f}{sig}"],
            textposition='middle right',
            textfont=dict(size=10, color=color),
            showlegend=False,
            hovertemplate=(
                f"<b>{d['Country']}</b><br>"
                f"Slope: {d['Slope']:+.5f}<br>"
                f"95% CI: [{d['CI_low']:+.5f}, {d['CI_high']:+.5f}]<br>"
                f"R²: {d['R_squared']:.3f}<br>"
                f"p = {d['P_value']:.4f}<extra></extra>"
            ),
        ))

    # Panel FE estimate
    fig.add_trace(go.Scatter(
        x=[panel_ci_low, panel_ci_high],
        y=['Panel FE (pooled)', 'Panel FE (pooled)'],
        mode='lines',
        line=dict(color=REGRESSION_COLOR, width=4),
        showlegend=False,
        hoverinfo='skip',
    ))
    fig.add_trace(go.Scatter(
        x=[panel_beta],
        y=['Panel FE (pooled)'],
        mode='markers+text',
        marker=dict(size=14, color=REGRESSION_COLOR, symbol='diamond'),
        text=[f"  {panel_beta:+.5f}{sig_label(panel_p)}"],
        textposition='middle right',
        textfont=dict(size=11, color=REGRESSION_COLOR),
        showlegend=False,
        hovertemplate=(
            f"<b>Panel Fixed Effects</b><br>"
            f"β: {panel_beta:+.5f}<br>"
            f"95% CI: [{panel_ci_low:+.5f}, {panel_ci_high:+.5f}]<br>"
            f"p = {panel_p:.4f}<extra></extra>"
        ),
    ))

    fig.update_layout(
        title=dict(
            text='<b>Coefficient Comparison: Slope of Nuclear Share on Household Price</b>'
                 '<br><sub>Diamond = point estimate · Horizontal bar = 95% CI · '
                 'Grey = not significant (p≥0.05)</sub>',
            x=0.5, font=dict(size=15, color=TEXT_COLOR),
        ),
        xaxis=dict(
            title='Slope (ΔEUR/kWh per 1pp nuclear share)',
            gridcolor=GRID_COLOR, linecolor='#425268', zeroline=False,
            tickfont=dict(color=MUTED_COLOR),
            title_font=dict(color=MUTED_COLOR),
        ),
        yaxis=dict(
            gridcolor=GRID_COLOR, linecolor='#425268',
            tickfont=dict(color=TEXT_COLOR, size=12),
            categoryorder='array',
            categoryarray=['Panel FE (pooled)', ''] + [d['Country'] for d in sorted_details],
        ),
        height=480,
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(color=TEXT_COLOR, size=11),
        margin=dict(l=140, r=120, t=90, b=60),
    )

    return fig


# ── Chart 3: Country fixed effects (intercepts) ─────────────────────────────

def render_fixed_effects_bar(panel_data, fe_result):
    data_flat = panel_data.reset_index()
    estimated = fe_result.estimated_effects.reset_index()
    estimated.columns = ['Country', 'Year', 'Fixed_Effect']
    country_effects = estimated.groupby('Country')['Fixed_Effect'].mean().sort_values()
    overall_mean = data_flat['Price_EUR'].mean()

    countries = list(country_effects.index)
    effects = list(country_effects.values)
    baselines = [overall_mean + e for e in effects]

    colors = [COUNTRY_COLORS.get(c, '#aab6c5') for c in countries]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=countries,
        y=baselines,
        marker=dict(color=colors, line=dict(color='rgba(255,255,255,0.15)', width=1)),
        text=[f'{b:.4f}' for b in baselines],
        textposition='outside',
        textfont=dict(size=10, color=TEXT_COLOR),
        hovertemplate='<b>%{x}</b><br>Baseline price: %{y:.4f} €/kWh<br>'
                      'Fixed effect: %{customdata:+.4f}<extra></extra>',
        customdata=effects,
        showlegend=False,
    ))

    fig.add_hline(
        y=overall_mean,
        line=dict(color=REGRESSION_COLOR, width=2, dash='dash'),
        annotation_text=f'Overall mean: {overall_mean:.4f}',
        annotation_font=dict(color=REGRESSION_COLOR, size=11),
        annotation_position='top right',
    )

    fig.update_layout(
        title=dict(
            text='<b>Country Fixed Effects: Implied Baseline Household Electricity Price</b>'
                 '<br><sub>Each bar = country mean price level after controlling for nuclear share · '
                 'Dashed line = overall mean</sub>',
            x=0.5, font=dict(size=15, color=TEXT_COLOR),
        ),
        xaxis=dict(
            tickfont=dict(color=TEXT_COLOR, size=11),
            gridcolor=GRID_COLOR, linecolor='#425268',
        ),
        yaxis=dict(
            title='Implied Baseline Price (€/kWh)',
            tickformat='.3f',
            gridcolor=GRID_COLOR, linecolor='#425268', zeroline=False,
            tickfont=dict(color=MUTED_COLOR),
            title_font=dict(color=MUTED_COLOR),
            range=[0, max(baselines) * 1.15],
        ),
        height=440,
        paper_bgcolor=PAPER_BG,
        plot_bgcolor=PLOT_BG,
        font=dict(color=TEXT_COLOR, size=11),
        margin=dict(l=70, r=30, t=100, b=60),
    )

    return fig


def save_html(fig, filename):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    html = pio.to_html(
        fig, full_html=False, include_plotlyjs='cdn',
        config={'responsive': True, 'displaylogo': False},
    )
    path.write_text(html, encoding='utf-8')
    return path


def main():
    panel_data = build_panel_dataset('household')
    data_flat = panel_data.reset_index()
    fe_result = run_pooled_fixed_effects(panel_data)
    country_details = build_country_regression_details(data_flat)

    fig1 = render_small_multiples(data_flat, country_details)
    p1 = save_html(fig1, 'fe_small_multiples.html')
    print(f'[+] Small multiples saved: {p1}')

    fig2 = render_forest_plot(country_details, fe_result)
    p2 = save_html(fig2, 'fe_forest_plot.html')
    print(f'[+] Forest plot saved: {p2}')

    fig3 = render_fixed_effects_bar(panel_data, fe_result)
    p3 = save_html(fig3, 'fe_country_intercepts.html')
    print(f'[+] Fixed-effects bar chart saved: {p3}')

    # Also show in browser
    fig1.show()
    fig2.show()
    fig3.show()


if __name__ == '__main__':
    main()
