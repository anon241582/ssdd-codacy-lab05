import secrets
import sqlite3
import os

# Fix 1: Use environment variable instead of hardcoded password
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Fix 2: Parameterized query prevents SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def generate_token():
    # Fix 3: secrets module is cryptographically secure
    return str(secrets.randbelow(900000) + 100000)

# Fix 4: Removed unused_count variable

print(get_user('admin'))
print(generate_token())
