import numpy as np
import pandas as pd


def calculate_cessation(year_data: pd.DataFrame):
   
    year_data = (
        year_data
        .sort_values("doy")
        .reset_index(drop=True)
    )

    for i in range(len(year_data)):

        if year_data.loc[i, "doy"] < 244:
            continue

        rainfall_20day = (
            year_data
            .loc[i:i + 19, "rain"]
            .sum()
        )

        if rainfall_20day < 20:
            return year_data.loc[i, "doy"]

    return np.nan

def calculate_cessation_all_years(data: pd.DataFrame):
    """
    Calculate rainfall cessation for every year.
    """

    results = []

    for year in sorted(data["year"].unique()):

        yearly_data = data[data["year"] == year]

        cessation = calculate_cessation(yearly_data)

        results.append({
            "year": year,
            "cessation_doy": cessation
        })

    return pd.DataFrame(results)