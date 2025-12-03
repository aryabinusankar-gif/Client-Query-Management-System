import sqlite3
from pathlib import Path

DB = Path(__file__).parent / 'cqms.db'

def init_db():
    conn = sqlite3.connect(DB)
    with open(Path(__file__).parent / 'schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database created successfully!")

    users = [
        ("Arya", "arya@gmail.com", "pass123"),
        ("Rahul", "rahul@gmail.com", "pass123"),
        ("Meera", "meera@gmail.com", "pass123"),
        ("Anand", "anand@gmail.com", "pass123"),
        ("Varun", "varun@gmail.com", "pass123"),
        ("Sneha", "sneha@gmail.com", "pass123"),
        ("Riya", "riya@gmail.com", "pass123"),
        ("Dev", "dev@gmail.com", "pass123"),
        ("Binu", "binu@gmail.com", "pass123"),
    ]

    cur.executemany(
        "INSERT INTO users(name, email, password) VALUES (?, ?, ?)",
        users
    )

    # Insert one support agent
    cur.execute(
        "INSERT INTO support_agents(name, email) VALUES (?, ?)",
        ("Support Admin", "support@company.com")
    )

    queries = [
        (1, "Login Issue", "Unable to login", "open"),
        (2, "Payment Error", "Payment failed", "open"),
        (3, "App Crash", "App closes when opening", "open"),
        (4, "Refund Request", "Need refund for last order", "open"),
        (5, "Incorrect Bill", "Amount charged is wrong", "open"),
        (6, "Technical Query", "Error code 503", "open"),
        (7, "Password Reset", "Forgot password", "open"),
        (8, "Feature Request", "Add dark mode", "open"),
        (9, "Account Issue", "Account suspended", "open"),
    ]

    cur.executemany(
        "INSERT INTO queries(user_id, subject, description, status) VALUES (?, ?, ?, ?)",
        queries
    )

conn.commit()