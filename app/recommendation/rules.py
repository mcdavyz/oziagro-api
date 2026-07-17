import pandas as pd

def classify_onset(onset_doy):
    """
    Classify rainfall onset.
    """

    if pd.isna(onset_doy):
        return "Unknown"

    elif onset_doy < 90:
        return "Very Early"

    elif onset_doy < 105:
        return "Early"

    elif onset_doy < 120:
        return "Normal"

    elif onset_doy < 135:
        return "Late"

    else:
        return "Very Late"

def classify_cessation(cessation_doy):
    """
    Classify rainfall cessation.
    """

    if pd.isna(cessation_doy):
        return "Unknown"

    elif cessation_doy > 310:
        return "Very Late"

    elif cessation_doy > 295:
        return "Late"

    elif cessation_doy > 280:
        return "Normal"

    elif cessation_doy > 265:
        return "Early"

    else:
        return "Very Early"

def classify_season_length(days):
    """
    Classify growing season length.
    """

    if days >= 180:
        return "Long"

    elif days >= 150:
        return "Moderate"

    else:
        return "Short"

def classify_dry_spell(longest):
    """
    Classify dry spell severity.
    """

    if longest <= 7:
        return "Low"

    elif longest <= 14:
        return "Moderate"

    else:
        return "High"


def classify_risk(onset, season, dry_spell):
    """
    Determine the overall seasonal risk.
    """

    if onset in ["Late", "Very Late"] and dry_spell == "High":
        return "High"

    elif season == "Short":
        return "High"

    elif onset == "Normal" and season == "Long" and dry_spell == "Low":
        return "Low"

    else:
        return "Moderate"