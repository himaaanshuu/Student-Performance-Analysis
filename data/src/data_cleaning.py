import pandas as pd


def clean_data(df):
    """Basic cleaning pipeline for the student DataFrame.

    - Drops rows that are completely empty
    - Clips numeric columns to reasonable ranges
    """
    # drop rows where all entries are NA
    df = df.dropna(how="all")

    # Ensure numeric columns exist and clip their values to sensible ranges
    for col in ["maths", "science", "english", "attendance"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
            df[col] = df[col].clip(0, 100)

    return df