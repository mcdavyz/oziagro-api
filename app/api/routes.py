from fastapi import APIRouter, UploadFile, File
import shutil
import os


from app.climate.reader import read_climate_data
from app.climate.processor import process_dataset

router = APIRouter()


@router.get("/analyze")
def analyze():

    data = read_climate_data(
        "data/raw/bende_daily_rainfall.xlsx"
    )

    summary = process_dataset(data)

    return summary.to_dict(orient="records")

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    upload_folder = "data/uploads"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully.",
        "filename": file.filename
    }