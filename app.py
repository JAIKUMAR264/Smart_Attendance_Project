import streamlit as st
from login import login
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart Attendance Analytical Platform",
    page_icon="🎓",
    layout="wide"
)
# Login check
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

st.sidebar.success(
    f"Welcome, {st.session_state['username']}"
)

st.sidebar.write(
    f"Role: {st.session_state['role']}"
)

if st.sidebar.button("🚪 Logout"):

    st.session_state.clear()

    st.rerun()

# ===============================
# Load Data
# ===============================

attendance = pd.read_csv("attendance.csv")
report = pd.read_csv("student_report.csv")
sentiment = pd.read_csv("student_feedback_sentiment.csv")

total_students = attendance["Student_ID"].nunique()
total_subjects = attendance["Subject"].nunique()
total_records = len(attendance)

safe = (report["Status"] == "Safe").sum()
shortage = (report["Status"] == "Shortage").sum()

positive = (sentiment["Sentiment"] == "POSITIVE").sum()
negative = (sentiment["Sentiment"] == "NEGATIVE").sum()

# ===============================
# Hero Banner
# ===============================

st.markdown("""
<div style="
padding:35px;
border-radius:18px;
background:linear-gradient(90deg,#2563EB,#06B6D4);
text-align:center;
color:white;
">

<h1>🎓 Smart Attendance Analytical Platform</h1>

<h3>AI Powered Student Attendance Monitoring System</h3>

<p>
Machine Learning • Deep Learning • NLP • Generative AI
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

st.success("Welcome! Choose a module below to begin.")

st.divider()

# ===============================
# Dashboard Overview
# ===============================

st.subheader("📊 Dashboard Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("👨‍🎓 Students", total_students)
c2.metric("📚 Subjects", total_subjects)
c3.metric("📄 Records", total_records)
c4.metric("🤖 AI Models", 5)

c5, c6, c7, c8 = st.columns(4)

c5.metric("✅ Safe", safe)
c6.metric("⚠️ Shortage", shortage)
c7.metric("😊 Positive", positive)
c8.metric("😟 Negative", negative)

st.divider()

# ===============================
# Quick Access
# ===============================

st.subheader("⚡ Quick Access")

q1, q2, q3, q4 = st.columns(4)

with q1:
    st.page_link("pages/1_dashboard.py", label="📊 Dashboard")

with q2:
    st.page_link("pages/7_Students.py", label="👨‍🎓 Students")

with q3:
    st.page_link("pages/8_subjects.py", label="📚 Subjects")

with q4:
    st.page_link("pages/4_chatbot.py", label="🤖 AI Chatbot")

st.write("")

q5, q6, q7, q8 = st.columns(4)

with q5:
    st.page_link("pages/2_Visualization.py", label="📈 Visualization")

with q6:
    st.page_link("pages/3_Reports.py", label="📄 Reports")

with q7:
    st.page_link("pages/5_sentiments.py", label="😊 Sentiment")

with q8:
    st.page_link("pages/6_dropout.py", label="⚠️ Dropout")

st.divider()

# ===============================
# Technology Stack
# ===============================

st.subheader("🛠 Technology Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.success("🐍 Python")
    st.success("📊 Pandas")

with t2:
    st.success("🌳 Decision Tree")
    st.success("🤖 Scikit-Learn")

with t3:
    st.success("🧠 LSTM")
    st.success("🧠 GRU")

with t4:
    st.success("😊 BERT")
    st.success("🤖 Gemini AI")

st.divider()

# ===============================
# Project Features
# ===============================

st.subheader("🚀 Project Features")

left, right = st.columns(2)

with left:
    st.success("📊 Attendance Dashboard")
    st.success("📈 Interactive Visualizations")
    st.success("👨‍🎓 Student Dashboard")
    st.success("📚 Subject Dashboard")

with right:
    st.success("😊 BERT Sentiment Analysis")
    st.success("⚠️ Dropout Prediction")
    st.success("🤖 AI Chatbot")
    st.success("📄 Automated Reports")

st.divider()

# ===============================
# Project Status
# ===============================

st.subheader("📌 Project Status")

st.success("✅ Dataset Loaded")
st.success("✅ AI Models Trained")
st.success("✅ Dashboard Ready")
st.success("✅ Chatbot Connected")
st.success("✅ Ready for Deployment")

st.divider()

st.caption(
    "Developed by JAI KUMAR | Rajalakshmi Engineering College | PENTAS HUB Internship"
)