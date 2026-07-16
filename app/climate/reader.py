from pathlib import Path
import pandas as pd
def read_climate_data(filepath):
    file_extension = Path(filepath).suffix.lower()
    if file_extension == ".csv":
        return pd.read_csv(filepath)
    elif file_extension in [".xlsx", ".xls"]:
        return pd.read_excel(filepath)
    else: 
        raise ValueError(f"Unsupported file format: {file_extension}")
    
    #Remiving Google Earth Engine columns
    columns_to_drop = ["system.index", ".geo"] 
    data = data.drop(columns=columns_to_drop, errors="ignore")
    return data