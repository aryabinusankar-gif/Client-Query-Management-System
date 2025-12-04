import sqlite3
import pandas as pd
from .db_utils import get_conn

def import_csv_to_queries(csv_path):
    df = pd.read_csv(csv_path)

    conn = get_conn()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO queries (user_id, subject, description, status)
            VALUES (?, ?, ?, ?)
            """,
            (
                row["user_id"],
                row["subject"],
                row["description"],
                row.get("status", "open")
            )
        )

    conn.commit()
    conn.close()
    print("CSV data imported successfully!")