def calculate_season_length(summary):
    summary["SeasonLength"] = (
        summary["cessation_doy"] - summary["onset_doy"]
    )
    return summary