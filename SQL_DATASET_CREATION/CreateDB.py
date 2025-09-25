# create_insurance_sql_db.py
import sqlite3
import os

DB_PATH = "insurance.db"

def create_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Customers table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        policy_type TEXT,
        premium_amount REAL
    )
    """)

    # Claims table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS claims (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        policy_type TEXT,
        claim_amount REAL,
        status TEXT,
        date TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )
    """)

    # Policies table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS policies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        coverage_amount REAL,
        exclusions TEXT,
        term INTEGER
    )
    """)

    conn.commit()
    conn.close()
    print("✅ insurance.db created with tables: customers, claims, policies")

if __name__ == "__main__":
    create_db()
