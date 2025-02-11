import sqlite3

conn = sqlite3.connect('banall.db')
cursor = conn.cursor()

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS banned_users (
            user_id INTEGER PRIMARY KEY,
            reason TEXT
        );
    ''')
    conn.commit()
