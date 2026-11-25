from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "zomato_rating_model.pkl"

DATA_PATH = BASE_DIR / "data" / "processed" / "zomato_processed.csv"