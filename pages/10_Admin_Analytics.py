import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
import plotly.express as px
check_access(["Admin"])
from navigation import sidebar

sidebar()

st.set_page_config(
    page_title="Admin Analytics",
    page_icon="📈",
    layout="wide"
)

# -------------------------------
# Load Data
# -------------------------------

attendance = pd.read_csv("attendance.csv")
report = pd.read_csv("student_report.csv")
sentiment = pd.read_csv("student_feedback_sentiment.csv")

attendance["Attendance_Status"] = (
    attendance["Attendance_Status"]
    .str.strip()
    .str.lower()
)

# -------------------------------
# Statistics
# -------------------------------

total_students = attendance["Student_ID"].nunique()
subjects = attendance["Subject"].nunique()
records = len(attendance)

safe = (report["Status"] == "Safe").sum()
shortage = (report["Status"] == "Shortage").sum()

positive = (sentiment["Sentiment"] == "POSITIVE").sum()
negative = (sentiment["Sentiment"] == "NEGATIVE").sum()

average_attendance = report["Attendance_Percentage"].mean()
highest_attendance = report["Attendance_Percentage"].max()
lowest_attendance = report["Attendance_Percentage"].min()

# -------------------------------
# Title
# -------------------------------

st.title("📈 Admin Analytics Dashboard")

st.markdown(
    "Overall insights for administrators and faculty."
)

st.divider()

# -------------------------------
# KPI Cards
# -------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("👨‍🎓 Students", total_students)
c2.metric("📚 Subjects", subjects)
c3.metric("📄 Records", records)
c4.metric("🤖 AI Models", "5")

st.divider()

c5, c6, c7 = st.columns(3)

c5.metric(
    "Average Attendance",
    f"{average_attendance:.2f}%"
)

c6.metric(
    "Highest Attendance",
    f"{highest_attendance:.2f}%"
)

c7.metric(
    "Lowest Attendance",
    f"{lowest_attendance:.2f}%"
)

st.divider()

# -------------------------------
# Charts
# -------------------------------

left, right = st.columns(2)

with left:

    st.subheader("Student Status")

    status = report["Status"].value_counts()

    fig = px.pie(
        values=status.values,
        names=status.index,
        hole=0.45
    )

    st.plotly_chart(fig,
                    use_container_width=True)

with right:

    st.subheader("Sentiment Analysis")

    senti = sentiment["Sentiment"].value_counts()

    fig = px.bar(
        x=senti.index,
        y=senti.values,
        text=senti.values
    )

    st.plotly_chart(fig,
                    use_container_width=True)

st.divider()

# -------------------------------
# Top Students
# -------------------------------

st.subheader("🏆 Top 10 Students")

top10 = report.sort_values(
    by="Attendance_Percentage",
    ascending=False
).head(10)

st.dataframe(
    top10,
    use_container_width=True
)

st.divider()

# -------------------------------
# Students Needing Attention
# -------------------------------

st.subheader("⚠️ Students Needing Attention")

attention = report[
    report["Attendance_Percentage"] < 75
]

st.dataframe(
    attention,
    use_container_width=True
)

st.divider()

# -------------------------------
# AI Summary
# -------------------------------

st.subheader("🤖 AI Summary")

high_risk = (
    report["Dropout_Risk"] == "High Risk"
).sum()

st.success(f"""
### AI Insights

👨‍🎓 Total Students : {total_students}

📚 Total Subjects : {subjects}

📊 Average Attendance : {average_attendance:.2f}%

⚠️ Students Below 75% : {len(attention)}

🚨 High Risk Students : {high_risk}

😊 Positive Feedback : {positive}

😟 Negative Feedback : {negative}

### Recommendation

• Monitor students below 75%.

• Conduct counselling sessions.

• Encourage regular attendance.

• Continue collecting student feedback.
""")
st.divider()

st.subheader("🧠 AI Attendance Insights")

average = report["Attendance_Percentage"].mean()

safe = (report["Status"] == "Safe").sum()

shortage = (report["Status"] == "Shortage").sum()

positive = (sentiment["Sentiment"] == "POSITIVE").sum()

negative = (sentiment["Sentiment"] == "NEGATIVE").sum()

highest_subject = attendance["Subject"].mode()[0]

st.success(f"""
### 📊 Attendance Summary

👨‍🎓 Total Students : {len(report)}

📈 Average Attendance : {average:.2f}%

✅ Safe Students : {safe}

⚠️ Shortage Students : {shortage}

😊 Positive Feedback : {positive}

😟 Negative Feedback : {negative}

📚 Most Common Subject : {highest_subject}

---

### 💡 AI Recommendation

• Monitor students below 75%.

• Encourage faculty mentoring.

• Continue collecting feedback.

• Review attendance weekly.

• Identify at-risk students early.
""")
