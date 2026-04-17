import pandas as pd

from .io_utils import safe_datetime


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    safe_datetime(df, "Order Placed At")

    if "Order_Date" not in df.columns:
        df["Order_Date"] = df["Order Placed At"].dt.date
    if "Order_Hour" not in df.columns:
        df["Order_Hour"] = df["Order Placed At"].dt.hour
    if "Order_Day_of_Week" not in df.columns:
        df["Order_Day_of_Week"] = df["Order Placed At"].dt.day_name()
    if "Order_Month" not in df.columns:
        df["Order_Month"] = df["Order Placed At"].dt.month

    if "Meal_Period" not in df.columns:
        df["Meal_Period"] = pd.cut(
            df["Order_Hour"],
            bins=[-1, 4, 11, 16, 21, 24],
            labels=["Late_Night", "Breakfast", "Lunch", "Dinner", "Late_Night"],
            ordered=False,
        )
        df.loc[df["Order_Hour"].isin([22, 23]), "Meal_Period"] = "Late_Night"
        df["Meal_Period"] = df["Meal_Period"].astype("object")

    return df


def add_distance_features(df: pd.DataFrame) -> pd.DataFrame:
    if "Distance" in df.columns:
        extracted = (
            df["Distance"].astype(str).str.extract(r"([0-9]*\.?[0-9]+)", expand=False)
        )
        df["Distance km"] = pd.to_numeric(extracted, errors="coerce")

        if "Distance Category" not in df.columns and "Distance_Category" in df.columns:
            df["Distance Category"] = df["Distance_Category"]
        if "Distance Category" not in df.columns:
            df["Distance Category"] = pd.NA

        df["Distance Category"] = df["Distance Category"].astype("object")
        missing_cat = df["Distance Category"].isna() | (
            df["Distance Category"].astype(str).str.strip() == ""
        )

        rebuilt = pd.cut(
            df.loc[missing_cat, "Distance km"],
            bins=[-float("inf"), 3, 6, float("inf")],
            labels=["Short", "Medium", "Long"],
        )
        df.loc[missing_cat, "Distance Category"] = rebuilt.astype("object")

    return df


def add_business_flags(df: pd.DataFrame) -> pd.DataFrame:
    if "Order_Success" not in df.columns and "Order Status" in df.columns:
        df["Order_Success"] = (df["Order Status"] == "Delivered").astype(int)

    if "Order_Success" in df.columns:
        df["Order_Success"] = (
            df["Order_Success"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map({"true": 1, "false": 0, "1": 1, "0": 0})
            .fillna(0)
            .astype(int)
        )

    if "Has_Complaint" not in df.columns and "Customer complaint tag" in df.columns:
        df["Has_Complaint"] = df["Customer complaint tag"].notna().astype(int)

    if "Has_Complaint" in df.columns:
        df["Has_Complaint"] = (
            df["Has_Complaint"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map({"true": 1, "false": 0, "1": 1, "0": 0})
            .fillna(0)
            .astype(int)
        )

    discount_cols = [
        "Restaurant discount (Promo)",
        "Restaurant discount (Flat offs, Freebies & others)",
        "Gold discount",
        "Brand pack discount",
    ]
    existing_discount_cols = [c for c in discount_cols if c in df.columns]

    if "Total_Discount" not in df.columns:
        df["Total_Discount"] = (
            df[existing_discount_cols].fillna(0).sum(axis=1)
            if existing_discount_cols
            else 0
        )

    if "Net_Revenue" not in df.columns and "Total" in df.columns:
        df["Net_Revenue"] = df["Total"].fillna(0) - df["Total_Discount"].fillna(0)

    return df
