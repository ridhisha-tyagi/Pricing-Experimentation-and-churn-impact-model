import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_data(*path_parts):
    file_path = os.path.join(BASE_DIR, "data", *path_parts)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at {file_path}")

    return pd.read_csv(file_path)