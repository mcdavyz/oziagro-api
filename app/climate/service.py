from app.recommendation.advisor import generate_all_recommendations
from .reader import read_climate_data
from .processor import process_dataset


def analyze_dataset(file_path):

    data = read_climate_data(file_path)
    summary = process_dataset(data)
    
    recommendations = generate_all_recommendations(summary)

    return recommendations