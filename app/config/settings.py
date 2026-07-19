from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data folders
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
UPLOAD_DIR = DATA_DIR / "uploads"
OUTPUT_DIR = DATA_DIR / "output"

# Default dataset
DEFAULT_DATASET = RAW_DATA_DIR / "bende_daily_rainfall.xlsx"

# API information
API_TITLE = "OziAgro RAINFALL ENGINE API"
API_VERSION = "1.0.0"
API_DESCRIPTION = (
    "Rainfall Analytics API for OziAgro Research Platform"
)