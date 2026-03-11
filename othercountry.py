from pathlib import Path

from country_energy_data import build_country_energy_dataframe


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / 'france_energy_data.csv'


def main():
    combined = build_country_energy_dataframe('France')
    print(combined.to_string(index=False))
    combined.to_csv(OUTPUT_FILE, index=False)


if __name__ == '__main__':
    main()




