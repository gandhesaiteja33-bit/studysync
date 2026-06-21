import sqlite3

DB_NAME = "studysync.db"


def register_user(username, password, role="Student"):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            """
        INSERT INTO users (username, password, role)
        VALUES (?, ?, ?)
        """,
            (username, password, role),
        )

        conn.commit()
        conn.close()

        return True, "registered_success"

    except sqlite3.IntegrityError:
        return False, "user_exists"

    except Exception:
        return False, "registration_failed"


def login_user(username, password):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT *
        FROM users
        WHERE username = ?
        AND password = ?
        """,
            (username, password),
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            return True, user
        else:
            return False, "invalid_credentials"

    except Exception:
        return False, "login_error"
