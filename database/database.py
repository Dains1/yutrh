import sqlite3

def initialize_db():
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE,
        username TEXT,
        first_name TEXT,
        last_name TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, username, first_name, last_name):
    with sqlite3.connect('bot_database.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO users (user_id, username, first_name, last_name)
                VALUES (?, ?, ?, ?)
            ''', (user_id, username, first_name, last_name))
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"User with id {user_id} already exists")

def get_user(user_id):
    with sqlite3.connect('bot_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE user_id = ?
        ''', (user_id,))
        user = cursor.fetchone()
        return user
