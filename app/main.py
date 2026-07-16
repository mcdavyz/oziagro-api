from climate.reader import read_rainfall_data
from climate.processor import process_data

def main():
    data = read_rainfall_data("data/raw/rainfall.csv")
    processed_data = process_data(data)
    processed_data.to_csv("data/processed/rainfall_processed.csv", index=False)

    print(processed_data)
    print("\nClimate dataset processed successfully.")
if __name__ == "__main__":
    main()