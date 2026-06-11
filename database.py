import sqlite3
from datetime import datetime

DB_NAME = "studysync.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # USERS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # ASSIGNMENTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        subject TEXT,
        due_date TEXT,
        priority TEXT,
        status TEXT
    )
    """)

    # ATTENDANCE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        conducted INTEGER,
        attended INTEGER
    )
    """)

    # GPA
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        credits INTEGER,
        grade TEXT
    )
    """)

    # EXAMS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        exam_date TEXT
    )
    """)

    # STUDY TASKS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        status TEXT
    )
    """)

    # NOTES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT,
        file_name TEXT,
        uploaded_at TEXT
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# ASSIGNMENTS
# ==========================

def add_assignment(title, subject, due_date, priority):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO assignments
    (title, subject, due_date, priority, status)
    VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        subject,
        due_date,
        priority,
        "Pending"
    ))

    conn.commit()
    conn.close()


def get_assignments():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM assignments"
    ).fetchall()

    conn.close()

    return rows

def delete_assignment(assignment_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM assignments WHERE id=?",
        (assignment_id,)
    )

    conn.commit()
    conn.close()


def mark_assignment_complete(assignment_id):
    conn = get_connection()

    conn.execute(
        """
        UPDATE assignments
        SET status='Completed'
        WHERE id=?
        """,
        (assignment_id,)
    )

    conn.commit()
    conn.close()


# ==========================
# ATTENDANCE
# ==========================

def add_attendance(subject, conducted, attended):
    conn = get_connection()

    conn.execute("""
    INSERT INTO attendance
    (subject, conducted, attended)
    VALUES (?, ?, ?)
    """, (
        subject,
        conducted,
        attended
    ))

    conn.commit()
    conn.close()


def get_attendance():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM attendance"
    ).fetchall()

    conn.close()

    return rows


# ==========================
# GPA
# ==========================

def add_grade(subject, credits, grade):
    conn = get_connection()

    conn.execute("""
    INSERT INTO grades
    (subject, credits, grade)
    VALUES (?, ?, ?)
    """, (
        subject,
        credits,
        grade
    ))

    conn.commit()
    conn.close()


def get_grades():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM grades"
    ).fetchall()

    conn.close()

    return rows


# ==========================
# EXAMS
# ==========================

def add_exam(subject, exam_date):
    conn = get_connection()

    conn.execute("""
    INSERT INTO exams
    (subject, exam_date)
    VALUES (?, ?)
    """, (
        subject,
        exam_date
    ))

    conn.commit()
    conn.close()


def get_exams():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM exams"
    ).fetchall()

    conn.close()

    return rows


# ==========================
# STUDY TASKS
# ==========================

def add_task(task):
    conn = get_connection()

    conn.execute("""
    INSERT INTO study_tasks
    (task, status)
    VALUES (?, ?)
    """, (
        task,
        "Pending"
    ))

    conn.commit()
    conn.close()


def get_tasks():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM study_tasks"
    ).fetchall()

    conn.close()

    return rows


# ==========================
# NOTES
# ==========================

def add_note(subject, file_name):
    conn = get_connection()

    conn.execute("""
    INSERT INTO notes
    (subject, file_name, uploaded_at)
    VALUES (?, ?, ?)
    """, (
        subject,
        file_name,
        datetime.now().strftime("%Y-%m-%d %H:%M")
    ))

    conn.commit()
    conn.close()


def get_notes():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM notes"
    ).fetchall()

    conn.close()

    return rows

def add_attendance(subject, conducted, attended):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO attendance
        (subject, conducted, attended)
        VALUES (?, ?, ?)
        """,
        (subject, conducted, attended)
    )

    conn.commit()
    conn.close()


def get_attendance():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM attendance"
    ).fetchall()

    conn.close()

    return rows


def delete_attendance(record_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM attendance WHERE id=?",
        (record_id,)
    )

    conn.commit()
    conn.close()