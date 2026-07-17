
from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.config.settings import (UPLOAD_DIR,DEFAULT_DATASET,)
from app .logging.logger import logger
from app.exceptions.errors import ClimateDataError

from app.climate.service import analyze_dataset

router = APIRouter()


@router.get("/analyze/sample")
def analyze():

    summary = analyze_dataset(DEFAULT_DATASET)
    return summary.to_dict(orient="records")

@router.post("/analyze")
async def analyze_uploaded_file(file: UploadFile = File(...)):
    logger.info(f"Received file:{file.filename}")
    logger.info("Starting climate analysis")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_DIR / file.filename
    allowed_extensions = [".xlsx", ".xls"]
    filename = file.filename.lower()

    if not any(filename.endswith(ext) for ext in allowed_extensions):
        return { "error": "Only Excel (.xlsx or .xls) files are supported."
        }
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:

        summary = analyze_dataset(file_path)

        logger.info("Analysis completed successfully")

        return {"status": "success","records": len(summary),"results": summary.to_dict(orient="records")}

    except ClimateDataError as e:

        logger.error(str(e))

        return {"status": "error","message": "Dataset validation failed.","details": str(e)}

    except Exception as e:

        logger.exception("Unexpected error")

        return {"status": "error", "message": "Internal server error." }
    