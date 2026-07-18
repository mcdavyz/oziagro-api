import pandas as pd
from app.recommendation.advisor import (generate_recommendation, generate_all_recommendations,)

def test_late_onset_recommendation():

    row = pd.Series({
        "onset_doy": 130,
        "cessation_doy": 300,
        "SeasonLength": 170,
        "LongestDrySpell": 8
    })

    report = generate_recommendation(row)

    assert report["Onset"] == "Late"

    assert (
        "Delay planting until rainfall becomes established."
        in report["Recommendations"]
    )

    assert "Reasons" in report

def test_short_season_recommendation():

    row = pd.Series({
        "onset_doy": 100,
        "cessation_doy": 240,
        "SeasonLength": 120,
        "LongestDrySpell": 5
    })

    report = generate_recommendation(row)

    assert report["SeasonLength"] == "Short"

    assert (
        "Use early-maturing rice varieties."
        in report["Recommendations"]
    )

def test_high_dry_spell_recommendation():

    row = pd.Series({
        "onset_doy": 100,
        "cessation_doy": 300,
        "SeasonLength": 180,
        "LongestDrySpell": 20
    })

    report = generate_recommendation(row)

    assert report["DrySpellRisk"] == "High"

    assert (
        "Prepare supplementary irrigation where possible."
        in report["Recommendations"]
    )

def test_summary_and_risk_created():

    row = pd.Series({
        "onset_doy": 100,
        "cessation_doy": 290,
        "SeasonLength": 180,
        "LongestDrySpell": 5
    })

    report = generate_recommendation(row)

    assert "OverallRisk" in report
    assert "SeasonSummary" in report