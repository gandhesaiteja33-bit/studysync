import sqlite3

DB_NAME = "studysync.db"


def register_user(
    username,
    password,
    role="Student"
):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (username, password, role)
    VALUES (?, ?, ?)
    """, (
        username,
        password,
        role
    ))

    conn.commit()
    conn.close()


def login_user(
    username,
    password
):
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    WHERE username = ?
    AND password = ?
    """, (
        username,
        password
    ))

    user = cursor.fetchone()

    conn.close()

    return user