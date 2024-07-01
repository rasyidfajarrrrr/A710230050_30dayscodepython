# database.py
import sqlite3

def create_connection():
    connection = sqlite3.connect("users.db")
    return connection

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_user(name, age):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
    ''', (name, age))
    conn.commit()
    conn.close()

def get_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return rows
