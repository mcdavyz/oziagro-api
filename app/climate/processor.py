from .season import calculate_calculate_length
from .risk import classify_risk

def process_data(data):
    data = calculate_calculate_length(data)
    data["Risk"] = data["Rainfall"].apply(classify_risk)
    return data



