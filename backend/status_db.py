import sqlite3

conn = sqlite3.connect("email_status.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS email_logs (
    email TEXT,
    status TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def log_status(email, status):
    cursor.execute("INSERT INTO email_logs (email, status) VALUES (?, ?)", (email, status))
    conn.commit()

def get_status_summary():
    cursor.execute("SELECT status, COUNT(*) FROM email_logs GROUP BY status")
    data = cursor.fetchall()
    return {"data": data}
