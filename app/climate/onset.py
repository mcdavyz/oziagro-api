import numpy as np
import pandas as pd


def calculate_onset(year_data: pd.DataFrame):
    
    #Calculate rainfall onset for one year.
    
    year_data = (year_data .sort_values("doy") .reset_index(drop=True))

    false_onsets = 0
    for i in range(len(year_data) - 2):
        # Ignore January and February
        if year_data.loc[i, "doy"] < 60:
            continue

        # Three-day rainfall threshold
        rainfall_3day = (
            year_data
            .loc[i:i + 2, "rain"]
            .sum()
        )

        if rainfall_3day < 20:
            continue

        # Check following 21 days
        window = (
            year_data
            .loc[i:i + 20]
            .reset_index(drop=True)
        )

        dry_spell_found = False

        for j in range(len(window) - 6):

            seven_day_total = (
                window
                .loc[j:j + 6, "rain"]
                .sum()
            )

            if seven_day_total < 1:

                false_onsets += 1
                dry_spell_found = True
                break

        if not dry_spell_found:

            onset_doy = year_data.loc[i, "doy"]

            return onset_doy, false_onsets

    return np.nan, false_onsets

def calculate_onset_all_years(data: pd.DataFrame):
    """
    Calculate rainfall onset for every year.
    """
    results = []

    for year in sorted(data["year"].unique()):

        yearly_data = data[data["year"] == year]

        onset, false_onsets = calculate_onset(yearly_data)

        results.append({
            "year": year,
            "onset_doy": onset,
            "false_onsets": false_onsets
        })

    return pd.DataFrame(results)