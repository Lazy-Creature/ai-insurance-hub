# insert_insurance_data.py
import sqlite3

DB_PATH = "insurance.db"

def seed_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # ----------------- Customers (30 rows) -----------------
    customers = [
        (1, 'Deepak Sharma', 35, 'Health', 15000),
        (2, 'Nisha Gupta', 42, 'Auto', 20000),
        (3, 'Rohan Mehta', 29, 'Life', 18000),
        (4, 'Simran Kaur', 50, 'Health', 22000),
        (5, 'Karan Verma', 38, 'Auto', 17000),
        (6, 'Anjali Singh', 31, 'Life', 16000),
        (7, 'Vikram Joshi', 45, 'Health', 25000),
        (8, 'Priya Nair', 27, 'Auto', 14000),
        (9, 'Rahul Patil', 39, 'Life', 21000),
        (10, 'Sneha Reddy', 33, 'Health', 19000),
        (11, 'Amit Bansal', 41, 'Auto', 23000),
        (12, 'Meera Iyer', 36, 'Life', 17000),
        (13, 'Arjun Rao', 44, 'Health', 24000),
        (14, 'Divya Menon', 30, 'Auto', 15000),
        (15, 'Sanjay Kumar', 37, 'Life', 18000),
        (16, 'Rekha Sharma', 48, 'Health', 26000),
        (17, 'Ajay Singh', 32, 'Auto', 16000),
        (18, 'Pooja Patel', 29, 'Life', 14000),
        (19, 'Manish Gupta', 40, 'Health', 22000),
        (20, 'Shalini Reddy', 34, 'Auto', 17500),
        (21, 'Rahul Sharma', 31, 'Life', 16500),
        (22, 'Anita Verma', 43, 'Health', 21000),
        (23, 'Rakesh Kumar', 38, 'Auto', 19000),
        (24, 'Sunita Joshi', 35, 'Life', 15500),
        (25, 'Vivek Nair', 39, 'Health', 23000),
        (26, 'Neha Mehta', 28, 'Auto', 14500),
        (27, 'Kunal Singh', 46, 'Life', 24000),
        (28, 'Swati Reddy', 33, 'Health', 20000),
        (29, 'Tarun Sharma', 37, 'Auto', 18000),
        (30, 'Maya Gupta', 42, 'Life', 21000)
    ]
    cur.executemany("INSERT INTO customers (id, name, age, policy_type, premium_amount) VALUES (?, ?, ?, ?, ?)", customers)

    # ----------------- Claims (30 rows) -----------------
    claims = [
        (1, 1, 'Health', 5000, 'Approved', '2025-01-10'),
        (2, 2, 'Auto', 7000, 'Pending', '2025-02-15'),
        (3, 3, 'Life', 10000, 'Approved', '2025-03-20'),
        (4, 4, 'Health', 12000, 'Rejected', '2025-04-25'),
        (5, 5, 'Auto', 8000, 'Approved', '2025-05-05'),
        (6, 6, 'Life', 6000, 'Pending', '2025-06-12'),
        (7, 7, 'Health', 15000, 'Approved', '2025-07-08'),
        (8, 8, 'Auto', 4000, 'Approved', '2025-01-22'),
        (9, 9, 'Life', 11000, 'Rejected', '2025-02-18'),
        (10, 10, 'Health', 9000, 'Approved', '2025-03-11'),
        (11, 11, 'Auto', 13000, 'Pending', '2025-04-30'),
        (12, 12, 'Life', 7000, 'Approved', '2025-05-21'),
        (13, 13, 'Health', 16000, 'Approved', '2025-06-17'),
        (14, 14, 'Auto', 4500, 'Rejected', '2025-07-05'),
        (15, 15, 'Life', 8000, 'Approved', '2025-01-29'),
        (16, 16, 'Health', 14000, 'Pending', '2025-02-14'),
        (17, 17, 'Auto', 6000, 'Approved', '2025-03-25'),
        (18, 18, 'Life', 5000, 'Rejected', '2025-04-08'),
        (19, 19, 'Health', 13000, 'Approved', '2025-05-13'),
        (20, 20, 'Auto', 7500, 'Approved', '2025-06-19'),
        (21, 21, 'Life', 9000, 'Pending', '2025-07-23'),
        (22, 22, 'Health', 11000, 'Approved', '2025-01-15'),
        (23, 23, 'Auto', 8500, 'Rejected', '2025-02-28'),
        (24, 24, 'Life', 6000, 'Approved', '2025-03-10'),
        (25, 25, 'Health', 12500, 'Approved', '2025-04-22'),
        (26, 26, 'Auto', 4800, 'Pending', '2025-05-18'),
        (27, 27, 'Life', 15000, 'Approved', '2025-06-24'),
        (28, 28, 'Health', 10000, 'Approved', '2025-07-02'),
        (29, 29, 'Auto', 7200, 'Rejected', '2025-01-08'),
        (30, 30, 'Life', 9500, 'Approved', '2025-02-12')
    ]
    cur.executemany("INSERT INTO claims (id, customer_id, policy_type, claim_amount, status, date) VALUES (?, ?, ?, ?, ?, ?)", claims)

    # ----------------- Policies (30 rows) -----------------
    policies = [
        (1, 'Health', 100000, 'Pre-existing conditions', 12),
        (2, 'Auto', 50000, 'Natural disaster', 24),
        (3, 'Life', 200000, 'Suicide within 1 year', 36),
        (4, 'Health', 120000, 'Cosmetic surgery', 12),
        (5, 'Auto', 55000, 'Theft', 24),
        (6, 'Life', 180000, 'War-related damages', 36),
        (7, 'Health', 110000, 'Flood', 12),
        (8, 'Auto', 60000, 'Earthquake', 24),
        (9, 'Life', 210000, 'Pre-existing conditions', 36),
        (10, 'Health', 130000, 'Cosmetic surgery', 12),
        (11, 'Auto', 52000, 'Natural disaster', 24),
        (12, 'Life', 190000, 'Suicide within 1 year', 36),
        (13, 'Health', 140000, 'Flood', 12),
        (14, 'Auto', 58000, 'Theft', 24),
        (15, 'Life', 220000, 'War-related damages', 36),
        (16, 'Health', 150000, 'Pre-existing conditions', 12),
        (17, 'Auto', 61000, 'Natural disaster', 24),
        (18, 'Life', 230000, 'Suicide within 1 year', 36),
        (19, 'Health', 125000, 'Cosmetic surgery', 12),
        (20, 'Auto', 57000, 'Theft', 24),
        (21, 'Life', 205000, 'Flood', 36),
        (22, 'Health', 135000, 'War-related damages', 12),
        (23, 'Auto', 59000, 'Earthquake', 24),
        (24, 'Life', 215000, 'Pre-existing conditions', 36),
        (25, 'Health', 145000, 'Cosmetic surgery', 12),
        (26, 'Auto', 62000, 'Theft', 24),
        (27, 'Life', 225000, 'Suicide within 1 year', 36),
        (28, 'Health', 155000, 'Flood', 12),
        (29, 'Auto', 63000, 'Natural disaster', 24),
        (30, 'Life', 235000, 'War-related damages', 36)
    ]
    cur.executemany("INSERT INTO policies (id, type, coverage_amount, exclusions, term) VALUES (?, ?, ?, ?, ?)", policies)

    conn.commit()
    conn.close()
    print("✅ Inserted 30 rows each into customers, claims, and policies")

if __name__ == "__main__":
    seed_data()
