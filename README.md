
# Student Performance Analysis

Small data pipeline to load student data, perform basic cleaning, compute averages,
predict performance status using a heuristic, and produce a chart.

Features
- Load from CSV (default). The pipeline is intentionally simple so the CSV can be edited and re-run quickly.
- Compact, headless-friendly plotting. You can provide a custom output path to the plotting function.

Quickstart
1. Create a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. To run the pipeline (reads CSV and writes a chart):

```bash
python3 main.py
```

Simple usage

```bash
# Edit the CSV
nano data/raw/students_raw.csv

# Re-run the pipeline to see your edits reflected immediately
python3 main.py
```

Plotting API
The plotting function lives in `data/src/visualization.py` and has the signature:

```py
plot_attendance_vs_marks(df, out_path: Optional[str|Path] = None) -> pathlib.Path
```

If `out_path` is not provided, the function writes to `outputs/charts/attendance_vs_marks.png` at the repo root.

Notes & next steps
- Consider adding `__init__.py` to `data/src` and switching to a proper package layout, removing the small `sys.path` hack in `main.py`.
- Add unit tests for data cleaning, analysis, and prediction functions.
- Add a small Makefile or scripts that run the pipeline and tests for easy grading.

Contributions welcome — open a PR with improvements.

