from src.db_connection import get_connection

def insert_data(df):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students (name, subject, marks)
    VALUES (%s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(query, (
            row["name"],
            row["subject"],
            row["marks"]
        ))

    conn.commit()
    cursor.close()
    conn.close()