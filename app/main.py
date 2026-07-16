from climate.reader import read_climate_data
from climate.processor import process_dataset
from recommendation.advisor import generate_all_recommendations
from recommendation.report import print_report

def main():
    data = read_climate_data("data/raw/bende_daily_rainfall.xlsx")
    annual = process_dataset(data)
    #print(data)
    annual.to_excel("data/processed/annual_rainfall.xlsx", index=False)

    summary = process_dataset(data)

    recommendations = generate_all_recommendations(summary)
    print(recommendations)
    print_report(recommendations.iloc[0])

    

    
if __name__ == "__main__":
    main()