from .rules import (
    classify_onset,
    classify_cessation,
    classify_season_length,
    classify_dry_spell,
)

def generate_recommendation(row):
    """
    Generate recommendations for one season.
    """

    onset = classify_onset(row["onset_doy"])
    cessation = classify_cessation(row["cessation_doy"])
    season = classify_season_length(row["SeasonLength"])
    dry_spell = classify_dry_spell(row["LongestDrySpell"])

    recommendations = []

    # Onset recommendation
    if onset in ["Late", "Very Late"]:
        recommendations.append(
            "Delay planting until rainfall becomes established."
        )
    else:
        recommendations.append(
            "Plant at the normal planting window."
        )

    # Season recommendation
    if season == "Short":
        recommendations.append(
            "Use early-maturing rice varieties."
        )
    elif season == "Moderate":
        recommendations.append(
            "Medium-duration rice varieties are suitable."
        )
    else:
        recommendations.append(
            "Long-duration rice varieties are suitable."
        )

    # Dry spell recommendation
    if dry_spell == "High":
        recommendations.append(
            "Prepare supplementary irrigation where possible."
        )
    elif dry_spell == "Moderate":
        recommendations.append(
            "Monitor rainfall closely during crop growth."
        )
    else:
        recommendations.append(
            "Dry spell risk is low."
        )

    return {
        "Onset": onset,
        "Cessation": cessation,
        "SeasonLength": season,
        "DrySpellRisk": dry_spell,
        "Recommendations": recommendations,
    }

import pandas as pd


def generate_all_recommendations(summary):
    """
    Generate recommendations for every year.
    """

    reports = []

    for _, row in summary.iterrows():

        report = generate_recommendation(row)

        report["year"] = row["year"]

        reports.append(report)

    return pd.DataFrame(reports)