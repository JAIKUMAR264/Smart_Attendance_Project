import streamlit as st
from auth import check_access
import streamlit as st

from navigation import sidebar
check_access([
    "Admin"
])

sidebar()


st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Smart Attendance Analytical Platform")

st.markdown("""
### 🎯 Project Objective

The Smart Attendance Analytical Platform is an AI-powered system developed to
analyze student attendance, predict dropout risk, understand student feedback
using NLP, and provide intelligent recommendations through a chatbot.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.subheader("📌 Problem Statement")

    st.info("""
Traditional attendance systems only record attendance.

They do not:

• Predict dropout risk

• Analyze attendance trends

• Understand student feedback

• Provide AI-based recommendations
""")

with col2:

    st.subheader("✅ Proposed Solution")

    st.success("""
Develop an AI-powered attendance platform capable of:

• Attendance Analytics

• Dropout Prediction

• Sentiment Analysis

• AI Chatbot

• Student Reports

• Admin Analytics
""")

st.divider()

st.subheader("📊 Dataset Information")

st.markdown("""
- Attendance Records : **12,156**
- Student Feedback : **20**
- Subjects : **6**
- Student Reports : Generated Automatically
""")

st.divider()

st.subheader("🤖 AI Models Used")

st.markdown("""
### 🌳 Decision Tree
Attendance Classification

### 🧠 LSTM
Attendance Forecasting

### 🧠 GRU
Attendance Forecasting

### 😊 BERT
Student Sentiment Analysis

### 🤖 Gemini + RAG
AI Chatbot & Smart Recommendations
""")

st.divider()

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.success("🐍 Python")
    st.success("📊 Pandas")
    st.success("📈 Plotly")

with tech2:
    st.success("🤖 Scikit-Learn")
    st.success("🧠 TensorFlow")
    st.success("😊 Transformers")

with tech3:
    st.success("🤖 Gemini API")
    st.success("🌐 Streamlit")
    st.success("💻 VS Code")

st.divider()

st.subheader("🔄 Project Workflow")

st.markdown("""
1. Data Collection

⬇️

2. Data Cleaning

⬇️

3. Attendance Analytics

⬇️

4. Machine Learning Prediction

⬇️

5. Sentiment Analysis

⬇️

6. AI Chatbot

⬇️

7. Student Reports

⬇️

8. Admin Analytics
""")

st.divider()

st.subheader("🚀 Future Enhancements")

st.markdown("""
- Face Recognition Attendance

- QR Code Attendance

- Mobile Application

- Parent Notification System

- Cloud Database Integration

- Real-Time Analytics

- Multi-College Support
""")

st.divider()

st.subheader("👨‍💻 Developer")

st.success("""
Name : JAI KUMAR

College : Rajalakshmi Engineering College

Department : Information Technology

Project : Smart Attendance Analytical Platform

Internship : PENTAS HUB
""")

st.divider()

st.caption("© 2026 Smart Attendance Analytical Platform")

