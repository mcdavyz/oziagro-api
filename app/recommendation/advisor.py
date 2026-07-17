from .rules import classify_risk
from .rules import (classify_onset,classify_cessation,classify_season_length,classify_dry_spell, classify_risk)

def generate_recommendation(row):
    """
    Generate recommendations for one season.
    """

    onset = classify_onset(row["onset_doy"])
    cessation = classify_cessation(row["cessation_doy"])
    season = classify_season_length(row["SeasonLength"])
    dry_spell = classify_dry_spell(row["LongestDrySpell"])
    risk = classify_risk(onset, season, dry_spell)
    season_summary = generate_season_summary(onset,season,dry_spell,risk)

    recommendations = []
    reasons = []

    # Onset recommendation
    if onset in ["Late", "Very Late"]:

       recommendations.append("Delay planting until rainfall becomes established.")

       reasons.append(f"Rainfall onset is classified as {onset}.")

    else:
        recommendations.append("Plant at the normal planting window.")

        reasons.append(f"Rainfall onset is {onset}.")

    # Season recommendation
    if season == "Short":
        recommendations.append(
            "Use early-maturing rice varieties."
        )
        reasons.append(f"Early-maturing rice varieties ensures that the crop reaches maturity before the end of the rainy season.")
    elif season == "Moderate":
        recommendations.append(
            "Medium-duration rice varieties are suitable."
        )
        reasons.append(f"This is because medium-duration rice varieties are recommended because their growth cycle matches the moderate length of the rainy season, allowing them to mature before moisture becomes limiting.")
    else:
        recommendations.append(
            "Long-duration rice varieties are suitable."
        )
        reasons.append(f"Long-duration rice varieties can complete their full growth cycle because the rainy season provides sufficient moisture for a longer period.")

    # Dry spell recommendation
    if dry_spell == "High":
        recommendations.append(
            "Prepare supplementary irrigation where possible."
        )
        reasons.append(f"High dry spell frequency increases the risk of moisture stress during critical rice growth stages, so supplementary irrigation helps prevent yield loss.")
    elif dry_spell == "Moderate":
        recommendations.append(
            "Monitor rainfall closely during crop growth."
        )
        reasons.append(f"Moderate dry spells may temporarily reduce soil moisture, so close rainfall monitoring helps detect emerging water stress and guide timely farm management decisions.")
    else:
        recommendations.append(
            "Dry spell risk is low."
        )
        reasons.append(f"Rainfall is expected to be sufficiently regular during the growing season, reducing the likelihood of prolonged moisture stress on the rice crop.")

    return {
        "Onset": onset,
        "Cessation": cessation,
        "SeasonLength": season,
        "DrySpellRisk": dry_spell,
        "OverallRisk": risk,
        "SeasonSummary": season_summary,
        "Recommendations": recommendations,
        "Reasons": reasons,
    }

def generate_season_summary(
    onset,
    season,
    dry_spell,
    risk
):
    """
    Generate a readable seasonal summary.
    """

    return (
        f"Rainfall onset is {onset.lower()}, "
        f"the growing season is {season.lower()}, "
        f"and dry spell risk is {dry_spell.lower()}. "
        f"Overall seasonal risk is {risk.lower()}."
    )

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