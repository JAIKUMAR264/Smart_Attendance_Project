import sqlite3
import pandas as pd
import os


def initialize_database(conn):

    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='attendance'
    """)

    if cursor.fetchone() is None:

        attendance = pd.read_csv("attendance.csv")
        report = pd.read_csv("student_report.csv")
        feedback = pd.read_csv("student_feedback_sentiment.csv")

        attendance.to_sql(
            "attendance",
            conn,
            if_exists="replace",
            index=False
        )

        report.to_sql(
            "student_report",
            conn,
            if_exists="replace",
            index=False
        )

        feedback.to_sql(
            "student_feedback_sentiment",
            conn,
            if_exists="replace",
            index=False
        )


def get_connection():

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(
        "database/attendance.db",
        check_same_thread=False
    )

    initialize_database(conn)

    return conn