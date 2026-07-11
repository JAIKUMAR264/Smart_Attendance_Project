import streamlit as st
from auth import check_access
import streamlit as st
import pandas as pd
import google.generativeai as genai
from navigation import sidebar

sidebar()

# Configure Gemini
import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 AI Attendance Chatbot")

st.write("Ask any question about attendance or a student.")

# Load report
report = pd.read_csv("student_report.csv")

question = st.text_input("Ask your question")

if st.button("Ask AI"):

    context = ""

    # Check if Student ID is mentioned
    words = question.upper().split()

    for word in words:
        if word.startswith("S"):

            student = report[
                report["Student_ID"] == word
            ]

            if not student.empty:
                context = student.to_string(index=False)
                break

    prompt = f"""
You are an AI Attendance Assistant.

Use this student information if available:

{context}

Question:
{question}

Give a clear answer and recommendations.
"""

    response = model.generate_content(prompt)

    st.subheader("🤖 AI Response")

    st.write(response.text)
check_access([
    "Admin",
    "Faculty",
    "Student"
])
