# Student Performance Analysis 📊

An end-to-end student performance analysis pipeline built with Python and MySQL.  
This project ingests student marks from CSV files, cleans and processes the data, stores it in a MySQL database, and computes per-student performance summaries (average marks and pass/average/fail status). The project can be run using CSV-based ingestion or by interacting directly with the MySQL database (SQL views are used for convenient aggregated queries and reporting).

---

Badges (optional)
- CI / tests: [add your CI badge]
- License: [add license badge]

Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Quickstart](#quickstart)
- [Configuration](#configuration)
- [Data Input Methods](#data-input-methods)
  - [1) CSV-based ingestion (recommended)](#1-csv-based-ingestion-recommended)
  - [2) Direct MySQL inserts / SQL views](#2-direct-mysql-inserts--sql-views)
- [CSV format (input)](#csv-format-input)
- [How it works](#how-it-works)
- [Sample output](#sample-output)
- [Development & Testing](#development--testing)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- CSV-based ingestion for one or many students and subjects
- Data cleaning and validation using Pandas
- Average marks calculation and performance classification:
  - Pass, Average, Fail (customizable thresholds)
- MySQL persistence for raw and processed records
- Use of SQL views for convenient aggregated queries and reporting
- Modular code: loader → cleaner → analysis → DB writer/reader
- Supports adding data via CSV files or directly into MySQL
- Easily extensible to add visualizations or an API layer

---

## Project Structure

student-performance-analysis/
- data/
  - raw/                # Input CSV files
  - processed/          # (optional) cleaned CSVs / intermediates
- src/                  # Core application logic
  - data_loader.py
  - data_cleaning.py
  - analysis.py
  - prediction.py
  - db_connection.py
  - db_writer.py
  - db_reader.py
- outputs/              # Generated reports (optional)
- main.py               # Entry point of the pipeline
- requirements.txt
- README.md

---

## Tech Stack

- Python 3.8+
- Pandas
- MySQL (mysql-connector-python or pymysql)
- Git / GitHub

---

## Quickstart

1. Clone the repository
```bash
git clone https://github.com/himaaanshuu/Student-Performance-Analysis.git
cd Student-Performance-Analysis
```

2. Create and activate a virtual environment, then install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows (PowerShell)
pip install -r requirements.txt
```

3. Configure MySQL
- Create a MySQL database (e.g., `student_performance`)
- Update database credentials in `src/db_connection.py` (or use environment variables)

4. Provide data (see Data Input Methods below) and run:
```bash
python main.py
```

By default the pipeline will:
- Load CSV(s) from `data/raw/` (unless configured otherwise)
- Clean & validate data
- Insert/update records in the MySQL database
- Fetch processed results and print/display a summary

Tip: you can run only the analysis/reporting step (which uses SQL views) if data is already present in the database.

---

## Configuration

Edit `src/db_connection.py` to set database connection details or provide environment variables. Example (recommended: use environment variables):

```python
# src/db_connection.py (example pattern)
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": int(os.environ.get("DB_PORT", 3306)),
    "user": os.environ.get("DB_USER", "your_user"),
    "password": os.environ.get("DB_PASSWORD", "your_password"),
    "database": os.environ.get("DB_NAME", "student_performance")
}
```

Environment variables:
- DB_HOST
- DB_PORT
- DB_USER
- DB_PASSWORD
- DB_NAME

Using env vars keeps credentials out of source control and is CI / Docker friendly.

---

## Data Input Methods

This project supports two primary ways to add data: CSV-based ingestion and direct MySQL inserts. Choose the method that fits your workflow.

### 1) CSV-based ingestion (recommended)
- Place CSV files in `data/raw/`.
- Run `python main.py` — the pipeline reads CSV(s), cleans, analyses and writes results to the database.
- Pros: simple, auditable, repeatable; good for batch uploads and pipelines.

Example:
```bash
# drop files here:
ls data/raw/

# run pipeline (reads all CSVs in data/raw/)
python main.py
```

If you want to import a single file programmatically, use the loader function from `src/data_loader.py` or `src/db_writer.py` (depending on your implementation). Example pattern (adapt to your code):
```python
from src.data_loader import load_csv
from src.db_writer import write_records_to_db

df = load_csv("data/raw/new_students.csv")
write_records_to_db(df)
```

### 2) Direct MySQL inserts / SQL views
You can add data directly into the database (useful for integrations, UIs, or migration scripts). When adding rows in MySQL, use the same schema expected by the app. The project also defines and uses SQL views for aggregated results (e.g., per-student averages and status) so reporting/consumption can be done directly from the database.

Suggested schema (example):
```sql
-- students table
CREATE TABLE IF NOT EXISTS students (
  student_id VARCHAR(64) PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100)
);

-- marks table (one row per subject mark)
CREATE TABLE IF NOT EXISTS marks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id VARCHAR(64),
  subject VARCHAR(100),
  marks DECIMAL(5,2),
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

Example INSERTs:
```sql
USE student_performance;

INSERT INTO students (student_id, first_name, last_name)
VALUES ('1001', 'Alice', 'Smith');

INSERT INTO marks (student_id, subject, marks)
VALUES ('1001', 'Mathematics', 85.00),
       ('1001', 'Physics', 78.00);
```

You can run the SQL from the command line:
```bash
mysql -u your_user -p student_performance < schema_and_inserts.sql
# or use an interactive session:
mysql -u your_user -p -D student_performance
> INSERT INTO ...
```

Notes:
- If you insert data directly to MySQL, run the pipeline or appropriate reader to re-calculate aggregates if your setup stores derived values separately. The pipeline's analysis step calculates average marks and statuses — either persist them on write or run analysis after inserts.
- Consider using transactions when running batch inserts and perform validation to match CSV loader behavior (e.g., marks numeric range, required fields).
- SQL views can be created to expose aggregates (average marks, status) for dashboards, BI tools or direct querying.

---

## CSV format (input)

Expected CSV columns (example header):

```csv
student_id,first_name,last_name,subject,marks
1001,Alice,Smith,Mathematics,85
1001,Alice,Smith,Physics,78
1002,Bob,Jones,Mathematics,55
```

Notes:
- Multiple rows per student (one per subject) are supported.
- The loader will attempt to parse common variations; missing or malformed rows are logged and skipped.

---

## How it works (high level)

1. data_loader.py
   - Reads CSV(s) from `data/raw/` into DataFrames
   - Basic validation (required columns, types)

2. data_cleaning.py
   - Handles missing or invalid marks
   - Normalizes names and subject labels

3. analysis.py
   - Calculates average marks per student
   - Assigns performance status using configurable thresholds:
     - Example: marks >= 75 => Pass, 50-74 => Average, <50 => Fail

4. db_writer.py / db_reader.py
   - Persist raw and processed data to MySQL
   - Query aggregated results for reporting
   - Optionally create and use SQL views for aggregated queries (per-student averages/status) so reporting consumers can read the view directly without re-running analysis

5. main.py
   - Orchestrates the pipeline and prints a summary to stdout (or writes reports to `outputs/`)

If you add data via MySQL directly, you can run only the analysis step (if implemented) to re-compute aggregates, or run the full pipeline that also validates inputs. If you prefer, use the SQL views for read-only reporting and BI consumption.

---

## Sample output

Example console summary printed by the pipeline:

```
Student Performance Summary
---------------------------
ID    Name            Avg   Status
1001  Alice Smith     81.5  Pass
1002  Bob Jones       55.0  Average
1003  Carol Lee       42.0  Fail
```

You can extend the project to export CSV/JSON reports or generate charts saved to `outputs/`.

---

## Development & Testing

- Add unit tests (pytest recommended) for data cleaning and analysis logic.
- To run tests:
```bash
pip install -r requirements-dev.txt
pytest
```
(If `requirements-dev.txt` doesn't exist yet, add pytest and test utilities to `requirements.txt` or create the file.)

Logging:
- The codebase should use Python's `logging` module for debug/info/warning/error messages. Check logs for rows that are skipped during ingestion.

---

## Future Improvements

- Add data visualizations (Matplotlib / Seaborn) and save images to `outputs/`
- Provide a REST API (FastAPI / Flask) to query student performance and allow inserts over HTTP (this would unify CSV and direct DB approaches)
- Add automated tests and CI (GitHub Actions)
- Add Docker containerization for easier deployment
- Add role-based user access and migrations for DB schema (Alembic)
- Add a command-line flag to `main.py` to choose source (`--source csv|db`) and a dry-run mode for validation-only runs

---

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repo
2. Create a topic branch: `git checkout -b feat/improve-readme`
3. Make changes, add tests where appropriate
4. Open a PR with a clear description of changes

Please follow conventional commits and keep changes scoped.

---

## License

Specify your license here (e.g., MIT). Add a LICENSE file to the repository.

---

## Author

Himanshu Gupta  
Building projects to learn data analysis and backend integration 🚀

If you find this project useful, please ⭐ the repository!

Acknowledgements: inspired by typical ETL/data-pipeline examples using Pandas and relational databases.
