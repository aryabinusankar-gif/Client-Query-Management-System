import sqlite3
from pathlib import Path

DB = Path(__file__).parent.parent / 'db' / 'cqms.db'

def get_conn():
    return sqlite3.connect(DB, check_same_thread=False)

def register_user(username, password_hash, role):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                    (username, password_hash, role))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

def get_user_by_username(username):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, username, password_hash, role FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    conn.close()
    return row