import sqlite3

def get_connection():

    conn = sqlite3.connect(
        "database/attendance.db",
        check_same_thread=False
    )

    return conn