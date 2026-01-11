import pandas as pd
from src.db_connection import get_connection

def fetch_student_report():
    conn = get_connection()
    query = "SELECT * FROM student_report"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
