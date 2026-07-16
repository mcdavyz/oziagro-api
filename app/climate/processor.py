from .validator import validate_climate_data
from .rainfall import calculate_annual_rainfall
from .onset import calculate_onset_all_years
from .cessation import calculate_cessation_all_years
from .season import calculate_season_length
from .dry_spell import calculate_dry_spell_all_years


def process_dataset(data):
    validate_climate_data(data)
    annual = calculate_annual_rainfall(data)
    onset = calculate_onset_all_years(data)
    cessation = calculate_cessation_all_years(data)
    summary = annual.merge(onset, on="year")
    summary = summary.merge(cessation, on="year")
    summary = calculate_season_length(summary)
    summary = calculate_dry_spell_all_years(data,summary)

    return summary



