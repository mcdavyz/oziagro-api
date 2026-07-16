def calculate_annual_rainfall(data):
    
    #Calculates total annual rainfall.
    annual_rainfall = ( data.groupby("year")["rain"] .sum().reset_index())

    annual_rainfall.rename(columns={"rain": "AnnualRainfall"},inplace=True)
    
    return annual_rainfall