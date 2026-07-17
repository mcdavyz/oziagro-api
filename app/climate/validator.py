import pandas as pd
from app.exceptions.errors import ClimateDataError


def validate_climate_data(data):

    #Validates the climate dataset before processing.
    required_columns = [
        "date",
        "year",
        "doy",
        "rain"
    ]
    
    # Check required columns
    for column in required_columns:
        if column not in data.columns:
            raise ClimateDataError(
                f"Missing required column: {column}"
            )

    # Check for missing values
    if data[required_columns].isnull().sum().sum() > 0:
        raise ClimateDataError(
            "Rainfall values contain missing value."
        )

    # Check for negative rainfall
    if (data["rain"] < 0).any():
        raise ClimateDataError(
            "Rainfall cannot be negative."
        )

    return True

    
    

