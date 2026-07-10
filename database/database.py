import sqlite3
import pandas as pd

# Create Database
conn = sqlite3.connect("database/attendance.db")

# Import CSV files
attendance = pd.read_csv("attendance.csv")
report = pd.read_csv("student_report.csv")
feedback = pd.read_csv("student_feedback_sentiment.csv")

# Store into SQLite
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

print("✅ Database Created Successfully!")

conn.close()