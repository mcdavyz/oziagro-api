import pandas as pd

from .rules import (
    classify_onset,
    classify_cessation,
    classify_season_length,
    classify_dry_spell,
    classify_risk,
)


def generate_recommendation(row):
    """
    Generate rainfall analysis for one year.

    Returns:
    - Scientific rainfall metrics
    - Standardized classifications
    """

    onset_category = classify_onset(row["onset_doy"])
    cessation_category = classify_cessation(row["cessation_doy"])
    season_category = classify_season_length(row["SeasonLength"])
    dry_spell_category = classify_dry_spell(row["LongestDrySpell"])

    overall_risk = classify_risk(
        onset_category,
        season_category,
        dry_spell_category,
    )

    return {

        # ===============================
        # Year
        # ===============================
        "year": int(row["year"]),

        # ===============================
        # Scientific Rainfall Metrics
        # ===============================
        "AnnualRainfallMM": round(float(row["AnnualRainfall"]), 1),

        "OnsetDayOfYear": int(row["onset_doy"]),
        "CessationDayOfYear": int(row["cessation_doy"]),

        "SeasonLengthDays": int(row["SeasonLength"]),

        "LongestDrySpellDays": int(row["LongestDrySpell"]),

        # ===============================
        # Climate Classifications
        # ===============================
        "OnsetCategory": onset_category,

        "CessationCategory": cessation_category,

        "SeasonLengthCategory": season_category,

        "DrySpellRisk": dry_spell_category,

        "OverallRisk": overall_risk,
    }


def generate_all_recommendations(summary):
    """
    Generate rainfall analysis for all years.
    """

    reports = []

    for _, row in summary.iterrows():

        reports.append(generate_recommendation(row))

    return pd.DataFrame(reports)