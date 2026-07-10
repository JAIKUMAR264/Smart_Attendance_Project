import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
from navigation import sidebar

sidebar()

st.set_page_config(
    page_title="Student Reports",
    page_icon="📄",
    layout="wide"
)

report = pd.read_csv("student_report.csv")

st.title("📄 Student Reports")

st.markdown("Search and analyze individual student reports.")

student_id = st.selectbox(
    "🔍 Search Student ID",
    sorted(report["Student_ID"].unique())
)

student = report[
    report["Student_ID"] == student_id
].iloc[0]

st.divider()

# KPI Cards

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Attendance %",
    f"{student['Attendance_Percentage']:.2f}%"
)

c2.metric(
    "Status",
    student["Status"]
)

c3.metric(
    "Dropout Risk",
    student["Dropout_Risk"]
)

c4.metric(
    "Sentiment",
    student["Sentiment"]
)

st.divider()

# Attendance Progress

st.subheader("📈 Attendance Progress")

attendance = float(student["Attendance_Percentage"])

st.progress(attendance/100)

st.write(f"Attendance : **{attendance:.2f}%**")

st.divider()

# Feedback

st.subheader("💬 Student Feedback")

st.info(student["Feedback"])

st.divider()

# AI Recommendation

st.subheader("🤖 AI Recommendation")

if attendance >= 90:

    st.success("""
Excellent attendance.

Keep maintaining consistency.

You are performing very well.
""")

elif attendance >= 75:

    st.info("""
Good attendance.

Try to attend every class.

Maintain your consistency.
""")

else:

    st.error("""
Attendance is below 75%.

Recommendation

• Attend extra classes.

• Meet your faculty advisor.

• Improve attendance immediately.
""")

st.divider()

# Complete Report

st.subheader("📄 Complete Report")

st.dataframe(
    student.to_frame().T,
    use_container_width=True
)

csv = student.to_frame().T.to_csv(index=False)

st.download_button(
    "📥 Download Report",
    csv,
    file_name=f"{student_id}_report.csv",
    mime="text/csv"
)
check_access([
    "Admin",
    "Faculty",
    "Student"
])
