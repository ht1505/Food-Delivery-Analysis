from pathlib import Path

import pandas as pd


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def drop_unnamed_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[:, ~df.columns.astype(str).str.startswith("Unnamed")].copy()


def safe_datetime(df: pd.DataFrame, col: str) -> None:
    if col not in df.columns:
        return

    parsed = pd.to_datetime(df[col], format="%I:%M %p, %B %d %Y", errors="coerce")
    needs_fallback = parsed.isna()
    if needs_fallback.any():
        parsed.loc[needs_fallback] = pd.to_datetime(
            df.loc[needs_fallback, col], errors="coerce"
        )
    df[col] = parsed


def safe_numeric(df: pd.DataFrame, cols: list[str]) -> None:
    for col in cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")


def round_numeric(df: pd.DataFrame, decimals: int = 4) -> pd.DataFrame:
    out = df.copy()
    numeric_cols = out.select_dtypes(include="number").columns
    out[numeric_cols] = out[numeric_cols].round(decimals)
    return out
