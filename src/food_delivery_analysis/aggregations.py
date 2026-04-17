import pandas as pd

from .io_utils import round_numeric


def build_executive_summary(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby(["Order_Date", "City"], dropna=False)
        .agg(
            Orders=("Order ID", "count"),
            Success_Rate=("Order_Success", "mean"),
            Revenue=("Total", "sum"),
            Avg_Order_Value=("Total", "mean"),
            Avg_Rating=("Rating", lambda x: x[x > 0].mean()),
            Complaint_Rate=("Has_Complaint", "mean"),
        )
        .reset_index()
    )
    return round_numeric(out)


def build_restaurant_performance(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby(["Restaurant name", "City", "Subzone"], dropna=False)
        .agg(
            Orders=("Order ID", "count"),
            Success_Rate=("Order_Success", "mean"),
            Avg_Rating=("Rating", lambda x: x[x > 0].mean()),
            Avg_KPT_Min=("KPT duration (minutes)", "mean"),
            Revenue=("Total", "sum"),
            Avg_Order_Value=("Total", "mean"),
            Complaint_Rate=("Has_Complaint", "mean"),
        )
        .reset_index()
    )
    return round_numeric(out)


def build_customer_experience(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby(["Meal_Period", "Distance Category"], dropna=False)
        .agg(
            Orders=("Order ID", "count"),
            Success_Rate=("Order_Success", "mean"),
            Avg_Rating=("Rating", lambda x: x[x > 0].mean()),
            Avg_KPT_Min=("KPT duration (minutes)", "mean"),
            Avg_Rider_Wait_Min=("Rider wait time (minutes)", "mean"),
        )
        .reset_index()
    )
    out = out[out["Orders"] > 0]
    return round_numeric(out)


def build_geographic_intelligence(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.groupby(["City", "Subzone", "Order_Date"], dropna=False)
        .agg(
            Orders=("Order ID", "count"),
            Revenue=("Total", "sum"),
            Success_Rate=("Order_Success", "mean"),
        )
        .reset_index()
    )
    return round_numeric(out)
