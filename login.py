import streamlit as st

# ----------------------------
# Dummy Users
# ----------------------------

users = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },
    "faculty": {
        "password": "faculty123",
        "role": "Faculty"
    },
    "student": {
        "password": "student123",
        "role": "Student"
    }
}

# ----------------------------
# Login Function
# ----------------------------

def login():

    st.title("🎓 Smart Attendance Platform")

    st.subheader("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username in users:

            if users[username]["password"] == password:

                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = users[username]["role"]

                st.success("Login Successful")

                st.rerun()

            else:

                st.error("Incorrect Password")

        else:

            st.error("User not found")