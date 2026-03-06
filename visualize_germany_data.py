import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = pd.read_csv('germany_energy_data.csv')
data['Period'] = data['Period'].astype(str)
data = data.sort_values('Period').reset_index(drop=True)
data['x'] = range(len(data))

fig, ax1 = plt.subplots(figsize=(14, 7))

ax2 = ax1.twinx()
width = 0.4
ax2.bar(data['x'] - width/2, data['Nuclear_Generation_GWh'], width=width, alpha=0.6, 
        color='#A23B72', label='Nuclear Generation (GWh)', zorder=1)
ax2.bar(data['x'] + width/2, data['Renewable_Generation_GWh'], width=width, alpha=0.6, 
        color='#4CAF50', label='Renewable Generation (GWh)', zorder=1)
ax2.set_ylabel('Generation (GWh)', fontsize=12, fontweight='bold', color='#A23B72')
ax2.tick_params(axis='y', labelcolor='#A23B72')

ax1.plot(data['x'], data['Price_EUR_per_KWH'], 'o-', 
         linewidth=2.5, markersize=8, color='#2E86AB', label='Electricity Price (€/kWh) excl. taxes', zorder=3)
ax1.fill_between(data['x'], data['Price_EUR_per_KWH'], 
                 alpha=0.2, color='#2E86AB', zorder=2)

ax1.set_xlabel('Period', fontsize=12, fontweight='bold')
ax1.set_ylabel('Electricity Price (€/kWh) excl. taxes', fontsize=12, fontweight='bold', color='#2E86AB')
ax1.tick_params(axis='y', labelcolor='#2E86AB')
ax1.grid(True, alpha=0.3, axis='y', zorder=0)
ax1.set_xlim(-0.5, len(data)-0.5)

plt.title('Germany: Electricity Prices, Nuclear & Renewable Generation (Annual 2007-2025)', 
          fontsize=14, fontweight='bold', pad=20)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=11)

# Set xticks to show every year
xticks = range(0, len(data), 1)
ax1.set_xticks(xticks)
ax1.set_xticklabels([data['Period'].iloc[i] for i in xticks], rotation=45)

fig.text(0.12, 0.02, f'Note: Annual price data (excl. taxes, in EUR/kWh) from Gov.uk Domestic electricity prices in the IEA (QEP 5.5.1); Yearly electricity data Europe (Ember)',
         ha='left', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig('germany_energy_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Plot saved as: germany_energy_analysis.png")
print("\nVisualization shows:")
print(f"  • Nuclear generation annual averages")
print(f"  • Renewable generation annual averages")
print(f"  • Electricity prices annual averages (X_TAX)")
print(f"  • Data from 2007 to 2025")
print(f"  • Data from 2008-S1 to 2025-S1")
