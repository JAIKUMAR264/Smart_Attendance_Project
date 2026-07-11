from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
check_access(["Admin", "Faculty"])
from navigation import sidebar

sidebar()

st.set_page_config(
    page_title="Student Dashboard",
    page_icon="👨‍🎓",
    layout="wide"
)

# Load Data
report = pd.read_csv("student_report.csv")

st.title("👨‍🎓 Student Dashboard")
st.divider()

st.subheader("➕ Add New Student")

with st.expander("Add Student"):

    new_id = st.text_input("Student ID")

    attendance = st.number_input(
        "Attendance %",
        min_value=0.0,
        max_value=100.0,
        value=75.0
    )

    status = st.selectbox(
        "Status",
        ["Safe", "Shortage"]
    )

    risk = st.selectbox(
        "Dropout Risk",
        ["Low Risk", "Medium Risk", "High Risk"]
    )

    sentiment = st.selectbox(
        "Sentiment",
        ["POSITIVE", "NEGATIVE"]
    )

    feedback = st.text_area("Feedback")

    if st.button("➕ Add Student"):

        new_student = pd.DataFrame([{

            "Student_ID": new_id,

            "Attendance_Percentage": attendance,

            "Status": status,

            "Dropout_Risk": risk,

            "Sentiment": sentiment,

            "Feedback": feedback

        }])

        report = pd.concat(
            [report, new_student],
            ignore_index=True
        )

        report.to_csv(
    "student_report.csv",
    index=False
)

        st.success("Student Added Successfully!")

        st.rerun()

st.markdown("Search and analyze student attendance, risk, and feedback.")

st.divider()

# -----------------------------
# Student Selection
# -----------------------------

student_list = sorted(report["Student_ID"].unique())

selected_student = st.selectbox(
    "🔍 Select Student",
    student_list
)

student = report[
    report["Student_ID"] == selected_student
].iloc[0]

st.divider()

# -----------------------------
# Student Overview
# -----------------------------

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
    "Risk",
    student["Dropout_Risk"]
)

c4.metric(
    "Sentiment",
    student["Sentiment"]
)

st.divider()

# -----------------------------
# Feedback
# -----------------------------

st.subheader("💬 Student Feedback")

st.info(student["Feedback"])

st.divider()

# -----------------------------
# Full Report
# -----------------------------

st.subheader("📄 Complete Student Report")

st.dataframe(
    student.to_frame().T,
    use_container_width=True
)

st.divider()
st.divider()

st.subheader("✏️ Edit Student Records")

edited_df = st.data_editor(
    report,
    use_container_width=True,
    num_rows="dynamic"
)

if st.button("💾 Save Changes"):

    edited_df.to_csv(
    "student_report.csv",
    index=False
)
    st.success("Student records updated successfully!")

    st.rerun()
# ===============================
# Delete Student (Admin Only)
# ===============================

if st.session_state["role"] == "Admin":

    st.divider()

    st.subheader("🗑 Delete Student")

    delete_student = st.selectbox(
        "Select Student ID",
        sorted(report["Student_ID"].unique()),
        key="delete_student"
    )

    if st.button("🗑 Delete Student"):

        report = report[
            report["Student_ID"] != delete_student
        ]

        report.to_csv(
    "student_report.csv",
    index=False
)

        st.success(f"{delete_student} deleted successfully!")

        st.rerun()

# -----------------------------
# Download
# -----------------------------

import os

if st.button("📄 Generate PDF Report"):

    pdf_file = f"{selected_student}_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>SMART ATTENDANCE ANALYTICAL PLATFORM</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Student ID :</b> {student['Student_ID']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Attendance :</b> {student['Attendance_Percentage']:.2f}%", styles["Normal"]))

    story.append(Paragraph(f"<b>Status :</b> {student['Status']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Dropout Risk :</b> {student['Dropout_Risk']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Sentiment :</b> {student['Sentiment']}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Student Feedback</b>", styles["Heading2"]))

    story.append(Paragraph(student["Feedback"], styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Recommendation</b>", styles["Heading2"]))

    if student["Attendance_Percentage"] >= 75:

        recommendation = (
            "Attendance is satisfactory. Continue maintaining regular attendance."
        )

    else:

        recommendation = (
            "Attendance is below the required threshold. Attend classes regularly and consult your faculty advisor."
        )

    story.append(Paragraph(recommendation, styles["BodyText"]))

    doc.build(story)

    with open(pdf_file, "rb") as pdf:

        st.download_button(
            label="⬇ Download PDF",
            data=pdf,
            file_name=pdf_file,
            mime="application/pdf"
        )

    os.remove(pdf_file)
