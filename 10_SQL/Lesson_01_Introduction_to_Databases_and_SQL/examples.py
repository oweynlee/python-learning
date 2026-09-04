import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create the Customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Country TEXT
)
""")

# Remove old data so the script can be rerun safely
cursor.execute("DELETE FROM Customers")

# Insert customers
customers = [
    (1, "Alice", 22, "Malaysia"),
    (2, "Ben", 30, "Singapore"),
    (3, "Chris", 19, "Malaysia"),
    (4, "David", 28, "Australia"),
    (5, "Emma", 35, "Malaysia")
]

cursor.executemany(
    "INSERT INTO Customers VALUES (?, ?, ?, ?)",
    customers
)

conn.commit()

print("Database setup completed!")

cursor.execute("""
SELECT *
FROM Customers
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()