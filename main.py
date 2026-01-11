import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# Make the package folder `data/src` importable as top-level package `src`.
# Insert at front so it takes precedence during imports.
data_dir = os.path.join(ROOT_DIR, "data")
if data_dir not in sys.path:
	sys.path.insert(0, data_dir)

from src.data_loader import load_data
from src.db_writer import insert_data
from src.db_reader import fetch_student_report

# 1. Load CSV and insert into MySQL
df = load_data("data/raw/students_raw.csv")
insert_data(df)
print("Data inserted into MySQL")

# 2. Fetch final report from SQL VIEW
report_df = fetch_student_report()
print(report_df)