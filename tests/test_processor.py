import pandas as pd
from app.climate.processor import process_dataset

def test_process_dataset():

    data = pd.DataFrame({

        "date": pd.date_range(
            "2024-01-01",
            periods=365
        ),

        "year": [2024] * 365,

        "doy": list(range(1, 366)),

        "rain": [5.0] * 365
    })

    result = process_dataset(data)

    expected_columns = [

        "year",

        "AnnualRainfall",

        "onset_doy",

        "false_onsets",

        "cessation_doy",

        "SeasonLength",

        "LongestDrySpell",

        "DrySpellCount",
    ]

    for column in expected_columns:

        assert column in result.columns

def test_process_dataset_one_year():

    data = pd.DataFrame({

        "date": pd.date_range(
            "2024-01-01",
            periods=365
        ),

        "year": [2024] * 365,

        "doy": list(range(1, 366)),

        "rain": [5.0] * 365
    })

    result = process_dataset(data)

    assert len(result) == 1