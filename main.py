import os
import sys

# Ensure the top-level `src` package (located at data/src) is importable
ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(ROOT, "data"))

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import calculate_average
from src.visualization import plot_attendance_vs_marks
from src.prediction import predict_status

os.makedirs("outputs/charts", exist_ok=True)

# Always load from CSV to keep the pipeline simple and editable.
df = load_data("data/raw/students_raw.csv")
df = clean_data(df)
df = calculate_average(df)
df = predict_status(df)

out_plot = plot_attendance_vs_marks(df)
print(f"Wrote plot to: {out_plot}")

print(df[["name", "average_marks", "attendance", "performance_status"]])