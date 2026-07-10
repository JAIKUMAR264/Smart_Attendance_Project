import streamlit as st

def sidebar():

    st.sidebar.title("🎓 Smart Attendance")

    st.sidebar.write(
        f"👤 {st.session_state.get('username', 'Guest')}"
    )

    st.sidebar.write(
        f"Role: {st.session_state.get('role', '')}"
    )

    st.sidebar.divider()

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()