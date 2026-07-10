import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
check_access(["Admin"])
from navigation import sidebar

sidebar()

st.title("⚠️ Dropout Risk Prediction")

report = pd.read_csv("student_report.csv")

st.subheader("📋 Student Risk Report")

st.dataframe(
    report[
        [
            "Student_ID",
            "Attendance_Percentage",
            "Dropout_Risk"
        ]
    ],
    use_container_width=True
)

risk_count = report["Dropout_Risk"].value_counts()

st.subheader("📊 Risk Distribution")

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    risk_count.index,
    risk_count.values
)

ax.set_xlabel("Risk")
ax.set_ylabel("Students")
ax.set_title("Dropout Risk")

st.pyplot(fig)

st.markdown("---")

high = (report["Dropout_Risk"] == "High Risk").sum()
medium = (report["Dropout_Risk"] == "Medium Risk").sum()
low = (report["Dropout_Risk"] == "Low Risk").sum()

c1, c2, c3 = st.columns(3)

c1.metric("🔴 High", high)
c2.metric("🟡 Medium", medium)
c3.metric("🟢 Low", low)
