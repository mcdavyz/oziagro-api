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
    
    return {
        "Onset": onset,
        "Cessation": cessation,
        "SeasonLength": season,
        "DrySpellRisk": dry_spell,
        "OverallRisk": risk,
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