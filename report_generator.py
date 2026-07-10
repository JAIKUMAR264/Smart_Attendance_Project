import pandas as pd

# Read attendance dataset
attendance = pd.read_csv("attendance.csv")

# Read sentiment dataset
feedback = pd.read_csv("student_feedback_sentiment.csv", sep=",")

# Clean attendance status
attendance["Attendance_Status"] = (
    attendance["Attendance_Status"]
    .str.strip()
    .str.lower()
)

# Treat present, late and excused as attended
attendance["Present"] = attendance["Attendance_Status"].isin(
    ["present", "late", "excused"]
).astype(int)

# Attendance summary
attendance_summary = (
    attendance.groupby("Student_ID")
    .agg(
        Total_Classes=("Attendance_Status", "count"),
        Attended=("Present", "sum")
    )
    .reset_index()
)

attendance_summary["Attendance_Percentage"] = (
    attendance_summary["Attended"] /
    attendance_summary["Total_Classes"]
) * 100

# Status
attendance_summary["Status"] = attendance_summary[
    "Attendance_Percentage"
].apply(lambda x: "Safe" if x >= 75 else "Shortage")

# Dropout Risk
def risk(attendance):
    if attendance >= 75:
        return "Low Risk"
    elif attendance >= 50:
        return "Medium Risk"
    else:
        return "High Risk"

attendance_summary["Dropout_Risk"] = attendance_summary[
    "Attendance_Percentage"
].apply(risk)

# Merge attendance with feedback
report = pd.merge(
    attendance_summary,
    feedback,
    on="Student_ID",
    how="left"
)

print("\nSTUDENT REPORT")
print(report.head(10))

# Save report
report.to_csv("student_report.csv", index=False)

print("\nReport generated successfully!")
print("Saved as: student_report.csv")