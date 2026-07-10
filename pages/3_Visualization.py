import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
check_access(["Admin", "Faculty"])
from navigation import sidebar

sidebar()

st.title("📈 Attendance Data Visualization")

# Load dataset
df = pd.read_csv("attendance.csv")

# Clean Attendance Status
df["Attendance_Status"] = (
    df["Attendance_Status"]
    .str.strip()
    .str.lower()
)

# Present Column
df["Present"] = df["Attendance_Status"].isin(
    ["present", "late", "excused"]
).astype(int)

# Attendance Summary
attendance_summary = (
    df.groupby("Student_ID")
    .agg(
        Total_Classes=("Attendance_Status", "count"),
        Attended=("Present", "sum")
    )
)

attendance_summary["Attendance_Percentage"] = (
    attendance_summary["Attended"]
    / attendance_summary["Total_Classes"]
) * 100

# ----------------------------
# Sidebar Filter
# ----------------------------

st.sidebar.header("Filters")

selected_subject = st.sidebar.selectbox(
    "Select Subject",
    ["All"] + sorted(df["Subject"].unique().tolist())
)

if selected_subject != "All":
    filtered_df = df[df["Subject"] == selected_subject]
else:
    filtered_df = df

# ----------------------------
# Pie Chart
# ----------------------------

st.subheader("🥧 Attendance Status Distribution")

status_counts = filtered_df["Attendance_Status"].value_counts()

fig, ax = plt.subplots(figsize=(6,6))

ax.pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%"
)

ax.set_title("Attendance Status")

st.pyplot(fig)

# ----------------------------
# Histogram
# ----------------------------

st.subheader("📊 Attendance Percentage Distribution")

fig, ax = plt.subplots(figsize=(8,5))

ax.hist(
    attendance_summary["Attendance_Percentage"],
    bins=10
)

ax.set_xlabel("Attendance Percentage")
ax.set_ylabel("Students")
ax.set_title("Attendance Histogram")

st.pyplot(fig)

# ----------------------------
# Top Students
# ----------------------------

st.subheader("🏆 Top 10 Students")

top10 = attendance_summary.sort_values(
    by="Attendance_Percentage",
    ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    top10.index,
    top10["Attendance_Percentage"]
)

plt.xticks(rotation=45)

ax.set_ylabel("Attendance %")

st.pyplot(fig)

# ----------------------------
# Bottom Students
# ----------------------------

st.subheader("⚠ Bottom 10 Students")

bottom10 = attendance_summary.sort_values(
    by="Attendance_Percentage"
).head(10)

fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    bottom10.index,
    bottom10["Attendance_Percentage"]
)

plt.xticks(rotation=45)

ax.set_ylabel("Attendance %")

st.pyplot(fig)
