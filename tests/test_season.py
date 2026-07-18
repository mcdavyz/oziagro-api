import pandas as pd
from app.climate.season import calculate_season_length

def test_calculate_season_length():

    summary = pd.DataFrame({
        "year": [2024],
        "onset_doy": [100],
        "cessation_doy": [280]
    })

    result = calculate_season_length(summary)

    assert result.loc[0, "SeasonLength"] == 180

def test_season_length_column_created():

    summary = pd.DataFrame({
        "year": [2024],
        "onset_doy": [110],
        "cessation_doy": [300]
    })

    result = calculate_season_length(summary)

    assert "SeasonLength" in result.columns