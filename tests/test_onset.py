import pandas as pd
import numpy as np
from app.climate.onset import calculate_onset, calculate_onset_all_years

def test_calculate_onset():

    data = pd.DataFrame({
        "year": [2024] * 25,
        "doy": list(range(60, 85)),
        "rain": [
            8, 7, 6,      # first 3 days = 21 mm
            2,2,2,2,2,2,2,
            2,2,2,2,2,2,2,
            2,2,2,2,2,2,
            2,2
        ]
    })

    onset, false_onsets = calculate_onset(data)

    assert onset == 60
    assert false_onsets == 0

def test_false_onset():

    data = pd.DataFrame({
        "year": [2024] * 25,
        "doy": list(range(60, 85)),
        "rain": [
            8,7,6,
            0,0,0,0,0,0,0,
            5,5,5,5,5,5,5,
            5,5,5,5,5,5,
            5,5
        ]
    })

    onset, false_onsets = calculate_onset(data)

    assert np.isnan(onset)
    assert false_onsets == 1

def test_calculate_onset_all_years():

    data = pd.DataFrame({
        "year": [2023]*25 + [2024]*25,
        "doy": list(range(60,85))*2,
        "rain": [2]*50
    })

    result = calculate_onset_all_years(data)

    assert len(result) == 2
    assert "onset_doy" in result.columns
    assert "false_onsets" in result.columns