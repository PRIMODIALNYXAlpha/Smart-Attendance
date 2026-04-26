import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    name TEXT,
    email TEXT,
    date TEXT,
    time TEXT
)
""")

conn.commit()
conn.close()

print("✅ Database Ready!")