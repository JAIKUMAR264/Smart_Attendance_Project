import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
import plotly.express as px
check_access(["Admin", "Faculty"])
from navigation import sidebar

sidebar()

st.set_page_config(
    page_title="Attendance Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Load Dataset
# -------------------------------

attendance = pd.read_csv("attendance.csv")
report = pd.read_csv("student_report.csv")

attendance["Attendance_Status"] = (
    attendance["Attendance_Status"]
    .str.strip()
    .str.lower()
)

# -------------------------------
# Statistics
# -------------------------------

total_students = attendance["Student_ID"].nunique()
total_subjects = attendance["Subject"].nunique()
total_records = len(attendance)

present = attendance["Attendance_Status"].isin(
    ["present", "late", "excused"]
).sum()

absent = attendance["Attendance_Status"].isin(
    ["absent", "left_early"]
).sum()

safe = (report["Status"] == "Safe").sum()
shortage = (report["Status"] == "Shortage").sum()

# -------------------------------
# Header
# -------------------------------

st.title("📊 Smart Attendance Dashboard")
st.markdown("Monitor student attendance, risk analysis, and attendance trends.")

st.divider()

# -------------------------------
# KPI Cards
# -------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("👨‍🎓 Students", total_students)
c2.metric("📚 Subjects", total_subjects)
c3.metric("📄 Records", total_records)
c4.metric("🤖 AI Models", "5")

st.divider()

c5, c6, c7, c8 = st.columns(4)

c5.metric("✅ Present", present)
c6.metric("❌ Absent", absent)
c7.metric("🟢 Safe", safe)
c8.metric("🔴 Shortage", shortage)

st.divider()

# -------------------------------
# Attendance Distribution
# -------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("🥧 Attendance Distribution")

    attendance_chart = px.pie(
        values=[present, absent],
        names=["Present", "Absent"],
        hole=0.45
    )

    st.plotly_chart(attendance_chart,
                    use_container_width=True)

with col2:

    st.subheader("📈 Student Status")

    status = report["Status"].value_counts()

    status_chart = px.bar(
        x=status.index,
        y=status.values,
        labels={
            "x":"Status",
            "y":"Students"
        },
        text=status.values
    )

    st.plotly_chart(status_chart,
                    use_container_width=True)

st.divider()

# -------------------------------
# AI Insights
# -------------------------------

st.subheader("🧠 AI Insights")

high_risk = (
    report["Dropout_Risk"] == "High Risk"
).sum()

avg_attendance = report[
    "Attendance_Percentage"
].mean()

st.info(f"""
### 📌 Smart Insights

✅ Total Students : **{total_students}**

📚 Total Subjects : **{total_subjects}**

📊 Average Attendance :
**{avg_attendance:.2f}%**

⚠️ Students with Attendance Shortage :
**{shortage}**

🚨 High Risk Students :
**{high_risk}**

🤖 Recommendation:

• Counsel students with low attendance.

• Encourage participation in classes.

• Monitor attendance weekly.

• Review students with negative sentiment.
""")

st.divider()

# -------------------------------
# Student Table
# -------------------------------

st.subheader("📋 Student Attendance Summary")

st.dataframe(
    report,
    use_container_width=True
)
