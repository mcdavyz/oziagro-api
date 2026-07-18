import pandas as pd

from app.climate.rainfall import calculate_annual_rainfall


def test_calculate_annual_rainfall():

    data = pd.DataFrame({
        "year": [2024, 2024, 2025, 2025],
        "rain": [10.0, 20.0, 30.0, 40.0]
    })

    result = calculate_annual_rainfall(data)

    assert len(result) == 2
    assert result.loc[0, "AnnualRainfall"] == 30.0
    assert result.loc[1, "AnnualRainfall"] == 70.0