import pandas as pd


def predict_status(df: pd.DataFrame) -> pd.DataFrame:
    """Heuristic prediction for performance status with readable labels.

    Labels:
      - 'Good'
      - 'Needs Improvement'
      - 'At Risk'
    """
    if "average_marks" not in df.columns:
        df["average_marks"] = 0

    if "attendance" not in df.columns:
        df["attendance"] = 0

    def status(row):
        if row["attendance"] < 65 or row["average_marks"] < 50:
            return "At Risk"
        elif row["average_marks"] < 70:
            return "Needs Improvement"
        else:
            return "Good"

    df["performance_status"] = df.apply(status, axis=1)
    return df