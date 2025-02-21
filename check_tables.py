import sqlite3

db_path = "instance/config_dashboard.db"  # Change to "instance/database.db" if needed

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()

    print(f"Tables in {db_path}: {tables}")

except Exception as e:
    print(f"Error: {e}")
