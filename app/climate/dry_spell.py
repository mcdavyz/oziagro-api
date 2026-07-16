import pandas as pd


def calculate_dry_spell(year_data: pd.DataFrame,
                         onset_doy,
                         cessation_doy):
    
    season = year_data[
        (year_data["doy"] >= onset_doy) &
        (year_data["doy"] <= cessation_doy)
    ].copy()

    current = 0
    longest = 0
    count = 0

    for rainfall in season["rain"]:

        if rainfall < 1:

            current += 1

        else:

            if current > 0:
                count += 1

            longest = max(longest, current)

            current = 0

    # Handle dry spell ending on final day
    if current > 0:
        count += 1
        longest = max(longest, current)

    return longest, count

def calculate_dry_spell_all_years(
        data,
        summary):
    """
    Calculate dry spell statistics
    for every year.
    """

    longest_list = []
    count_list = []

    for _, row in summary.iterrows():

        year = row["year"]

        yearly = data[
            data["year"] == year
        ]

        longest, count = calculate_dry_spell(
            yearly,
            row["onset_doy"],
            row["cessation_doy"]
        )

        longest_list.append(longest)
        count_list.append(count)

    summary["LongestDrySpell"] = longest_list

    summary["DrySpellCount"] = count_list

    return summary
