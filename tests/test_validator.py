import pandas as pd
import pytest

from app.climate.validator import validate_climate_data
from app.exceptions.errors import ClimateDataError


def test_validate_good_dataset():
    data = pd.DataFrame({
        "date": ["2024-01-01"],
        "year": [2024],
        "doy": [1],
        "rain": [10.5]
    })

    assert validate_climate_data(data) is True


def test_negative_rainfall():
    data = pd.DataFrame({
        "data": ["2024-01-01"],
        "year": [2024],
        "doy": [1],
        "rain": [-5]
    })

    with pytest.raises(ClimateDataError):
        validate_climate_data(data)