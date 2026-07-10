import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
check_access(["Admin", "Faculty"])
from navigation import sidebar

sidebar()

st.title("😊 Student Sentiment Analysis")

# Load data
df = pd.read_csv("student_feedback_sentiment.csv")

st.subheader("📋 Student Feedback")

st.dataframe(df, use_container_width=True)

# Sentiment Summary
st.subheader("📊 Sentiment Distribution")

sentiment_count = df["Sentiment"].value_counts()

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    sentiment_count.index,
    sentiment_count.values
)

ax.set_xlabel("Sentiment")
ax.set_ylabel("Students")
ax.set_title("Sentiment Analysis")

st.pyplot(fig)

st.markdown("---")

positive = (df["Sentiment"] == "POSITIVE").sum()
negative = (df["Sentiment"] == "NEGATIVE").sum()

col1, col2 = st.columns(2)

col1.metric("😊 Positive", positive)
col2.metric("😟 Negative", negative)
