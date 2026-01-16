import sqlite3
connection = sqlite3.connect("documents.db", check_same_thread=False)
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    uploaded_at TEXT
)
""")
connection.commit()
