import pandas as pd
from app.climate.cessation import calculate_cessation, calculate_cessation_all_years

def test_calculate_cessation():

    data = pd.DataFrame({

        "year": [2024] * 40,

        "doy": list(range(250, 290)),

        "rain": (
            [5] * 15 +
            [0] * 25
        )
    })

    cessation = calculate_cessation(data)

    assert cessation is not None

def test_calculate_cessation_all_years():

    data = pd.DataFrame({

        "year": [2024] * 40,

        "doy": list(range(250, 290)),

        "rain": (
            [5] * 15 +
            [0] * 25
        )
    })

    result = calculate_cessation_all_years(data)

    assert len(result) == 1

    assert "cessation_doy" in result.columns