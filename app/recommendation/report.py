def print_report(report):
    """
    Display a climate decision support report.
    """

    print("=" * 50)

    print(f"Year: {report['year']}")

    print(f"Onset: {report['Onset']}")

    print(f"Cessation: {report['Cessation']}")

    print(f"Season Length: {report['SeasonLength']}")

    print(f"Dry Spell Risk: {report['DrySpellRisk']}")

    print("\nRecommendations:")

    for recommendation in report["Recommendations"]:
        print(f"- {recommendation}")

    print("=" * 50)