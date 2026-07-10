import streamlit as st


def check_access(allowed_roles):

    if "logged_in" not in st.session_state:
        st.error("Please login first.")
        st.stop()

    role = st.session_state.get("role")

    if role not in allowed_roles:

        st.error("⛔ Access Denied!")

        st.warning(
            f"This page is available only for: {', '.join(allowed_roles)}"
        )

        st.stop()