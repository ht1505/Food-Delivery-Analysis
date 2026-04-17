from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

RAW_DATA_FILE = RAW_DIR / "order_history_kaggle_data.csv"

PROCESSED_FILES = {
    "main": PROCESSED_DIR / "tableau_main_data_clean.csv",
    "executive_summary": PROCESSED_DIR / "tableau_executive_summary_clean.csv",
    "restaurant_performance": PROCESSED_DIR / "tableau_restaurant_performance_clean.csv",
    "customer_experience": PROCESSED_DIR / "tableau_customer_experience_clean.csv",
    "geographic_intelligence": PROCESSED_DIR / "tableau_geographic_intelligence_clean.csv",
}
