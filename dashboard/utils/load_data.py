import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "processed"

def load_trial():
    return pd.read_csv(DATA_DIR / "trial_experiment_summary.csv")

def load_billing():
    return pd.read_csv(DATA_DIR / "billing_experiment_summary.csv")

def load_plan_seat():
    return pd.read_csv(DATA_DIR / "plan_seat_experiment_summary.csv")

def load_experiment_simulation():
    return pd.read_csv(
        DATA_DIR / "experiment_simulation_results.csv"
    )   
    