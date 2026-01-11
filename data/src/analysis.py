import pandas as pd


def calculate_average(df: pd.DataFrame) -> pd.DataFrame:
    """Add an `average_marks` column computed from available subject columns.

    If subject columns are missing, they're treated as zeros.
    """
    subjects = ["maths", "science", "english"]
    for s in subjects:
        if s not in df.columns:
            df[s] = 0

    df["average_marks"] = df[subjects].mean(axis=1)
    return df