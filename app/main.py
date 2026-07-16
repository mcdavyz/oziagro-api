from climate.reader import read_climate_data
from climate.processor import process_dataset

def main():
    data = read_climate_data("data/raw/bende_daily_rainfall.xlsx")
    annual = process_dataset(data)
    print(data)
    annual.to_excel("data/processed/annual_rainfall.xlsx", index=False)

    print("\nAnnual Rainfall Generated Successfully.")

    summary = process_dataset(data)
    print(summary)

    
if __name__ == "__main__":
    main()