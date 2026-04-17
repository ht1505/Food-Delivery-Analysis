import pandas as pd

from .aggregations import (
    build_customer_experience,
    build_executive_summary,
    build_geographic_intelligence,
    build_restaurant_performance,
)
from .config import PROCESSED_DIR, PROCESSED_FILES, RAW_DATA_FILE
from .features import add_business_flags, add_distance_features, add_time_features
from .io_utils import drop_unnamed_columns, ensure_directory, safe_numeric


def load_raw_data() -> pd.DataFrame:
    df = pd.read_csv(RAW_DATA_FILE)
    df = drop_unnamed_columns(df)

    safe_numeric(
        df,
        [
            "Total",
            "Rating",
            "KPT duration (minutes)",
            "Rider wait time (minutes)",
            "Restaurant discount (Promo)",
            "Restaurant discount (Flat offs, Freebies & others)",
            "Gold discount",
            "Brand pack discount",
        ],
    )

    df = add_time_features(df)
    df = add_distance_features(df)
    df = add_business_flags(df)
    return df


def build_processed_tables() -> dict[str, pd.DataFrame]:
    main_df = load_raw_data()

    return {
        "main": main_df,
        "executive_summary": build_executive_summary(main_df),
        "restaurant_performance": build_restaurant_performance(main_df),
        "customer_experience": build_customer_experience(main_df),
        "geographic_intelligence": build_geographic_intelligence(main_df),
    }


def save_processed_tables(tables: dict[str, pd.DataFrame]) -> None:
    ensure_directory(PROCESSED_DIR)
    for name, df in tables.items():
        df.to_csv(PROCESSED_FILES[name], index=False)


def run_pipeline() -> None:
    tables = build_processed_tables()
    save_processed_tables(tables)
    print("Processed files created in data/processed")
    for name, path in PROCESSED_FILES.items():
        print(f"- {name}: {path.name}")
