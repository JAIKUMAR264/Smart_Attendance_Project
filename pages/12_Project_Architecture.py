import streamlit as st
from auth import check_access
import streamlit as st
check_access(["Admin"])
from navigation import sidebar

sidebar()


st.set_page_config(
    page_title="Project Architecture",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Smart Attendance Project Architecture")

st.markdown("""
### 📌 System Workflow

This page explains how the Smart Attendance Analytical Platform works from data collection to AI-based recommendations.
""")

st.divider()

st.subheader("🔄 Complete Workflow")

st.markdown("""
```text
Attendance Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Attendance Analytics
        │
        ▼
Decision Tree Model
        │
        ▼
Attendance Prediction
        │
        ▼
LSTM & GRU Forecasting
        │
        ▼
Student Feedback Dataset
        │
        ▼
BERT Sentiment Analysis
        │
        ▼
Student Report Generation
        │
        ▼
Gemini AI Chatbot
        │
        ▼
Admin Analytics Dashboard
            """)
