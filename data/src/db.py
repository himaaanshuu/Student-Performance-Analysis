"""Database helpers removed.

This file used to provide SQLite/SQLAlchemy helpers. The project no longer
uses a database; it reads from the CSV directly. Importing this module will
raise to avoid accidental DB usage.
"""

def __getattr__(name):
    raise ImportError("Database support removed. Edit data/raw/students_raw.csv and re-run the script.")
