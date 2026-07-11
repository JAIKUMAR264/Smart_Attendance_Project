import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
check_access(["Admin", "Faculty"])
from navigation import sidebar

sidebar()

st.set_page_config(
    page_title="Subjects Dashboard",
    page_icon="📚",
    layout="wide"
)
import pandas as pd

attendance = pd.read_csv("attendance.csv")

attendance["Attendance_Status"] = (
    attendance["Attendance_Status"]
    .str.strip()
    .str.lower()
)





attendance.to_csv(
    "attendance.csv",
    index=False
)

st.title("📚 Subject Management")

st.markdown(
    "Manage subjects and view attendance statistics."
)

st.divider()

st.subheader("➕ Add Subject")
with st.expander("Add New Subject"):

    new_subject = st.text_input(
        "Subject Name"
    )

    if st.button("➕ Add Subject"):

        if new_subject.strip() == "":

            st.warning("Enter subject name.")

        elif new_subject in attendance["Subject"].unique():

            st.warning("Subject already exists.")

        else:

            new_row = attendance.iloc[0].copy()

            new_row["Subject"] = new_subject

            new_row["Student_ID"] = "NEW"

            new_row["Attendance_Status"] = "present"

            attendance = pd.concat(
                [attendance,
                 pd.DataFrame([new_row])],
                ignore_index=True
            )

            attendance.to_csv(
    "attendance.csv",
    index=False
)
            st.success("Subject added successfully!")

            st.rerun()


subjects = sorted(attendance["Subject"].unique())

selected_subject = st.selectbox(
    "Select Subject",
    subjects
)

subject_df = attendance[
    attendance["Subject"] == selected_subject
]

st.divider()

present = subject_df["Attendance_Status"].isin(
    ["present","late","excused"]
).sum()

absent = subject_df["Attendance_Status"].isin(
    ["absent","left early"]
).sum()

students = subject_df["Student_ID"].nunique()

records = len(subject_df)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Students",students)

c2.metric("Records",records)

c3.metric("Present",present)

c4.metric("Absent",absent)

st.divider()

st.subheader("Attendance Status")

status = subject_df["Attendance_Status"].value_counts()

fig,ax = plt.subplots(figsize=(6,6))

ax.pie(
    status.values,
    labels=status.index,
    autopct="%1.1f%%"
)

st.pyplot(fig)

st.divider()

st.subheader("Student List")

st.dataframe(
    subject_df,
    use_container_width=True
)
st.divider()

st.subheader("✏️ Edit Subject Records")

edited_subject = st.data_editor(
    subject_df,
    use_container_width=True
)

if st.button("💾 Save Subject Changes"):

    attendance.loc[
        attendance["Subject"] == selected_subject
    ] = edited_subject.values

    attendance.to_csv(
    "attendance.csv",
    index=False
)

    st.success("Changes saved successfully!")

    st.rerun()
if st.session_state["role"] == "Admin":

    st.divider()

    st.subheader("🗑 Delete Subject")

    delete_subject = st.selectbox(
        "Select Subject",
        sorted(attendance["Subject"].unique()),
        key="delete_subject"
    )

    if st.button("Delete Subject"):

        attendance = attendance[
            attendance["Subject"] != delete_subject
        ]

        attendance.to_csv(
    "attendance.csv",
    index=False
)

        st.success(
            "Subject deleted successfully!"
        )

        st.rerun()
