import pandas as pd
from app.climate.dry_spell import (calculate_dry_spell, calculate_dry_spell_all_years,)

def test_calculate_dry_spell():

    data = pd.DataFrame({

        "doy": list(range(100, 111)),

        "rain": [
            5,
            0,
            0,
            0,
            4,
            0,
            0,
            6,
            5,
            4,
            2
        ]
    })

    longest, count = calculate_dry_spell(
        data,
        onset_doy=100,
        cessation_doy=110
    )

    assert longest == 3
    assert count == 2

def test_no_dry_spell():

    data = pd.DataFrame({

        "doy": list(range(100, 106)),

        "rain": [5,4,6,3,8,2]
    })

    longest, count = calculate_dry_spell(
        data,
        100,
        105
    )

    assert longest == 0
    assert count == 0

def test_calculate_dry_spell_all_years():

    data = pd.DataFrame({

        "year": [2024]*6,

        "doy": [100,101,102,103,104,105],

        "rain": [5,0,0,4,5,6]
    })

    summary = pd.DataFrame({

        "year": [2024],

        "onset_doy": [100],

        "cessation_doy": [105]
    })

    result = calculate_dry_spell_all_years(
        data,
        summary
    )

    assert "LongestDrySpell" in result.columns

    assert "DrySpellCount" in result.columns

    assert result.loc[0, "LongestDrySpell"] == 2

    assert result.loc[0, "DrySpellCount"] == 1