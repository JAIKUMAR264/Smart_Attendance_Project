from turtle import st

import pandas as pd
import google.generativeai as genai

# Configure Gemini
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-2.5-flash")

# Load student report
df = pd.read_csv("student_report.csv")

print("=" * 60)
print(" SMART ATTENDANCE RAG CHATBOT ")
print("=" * 60)

while True:

    question = input("\nAsk your question (type 'exit' to quit): ").strip()

    # Exit the chatbot
    if question.lower() == "exit":
        print("\nThank you for using Smart Attendance AI Chatbot!")
        break

    context = ""

    words = question.upper().split()

    for word in words:
        if word.startswith("S") and len(word) == 6:

            student = df[df["Student_ID"] == word]

            if not student.empty:

                context = student.to_string(index=False)

    # Build prompt
    if context:

        prompt = f"""
You are an AI Attendance Assistant.

Student Information:

{context}

Answer this question:

{question}

Also provide a recommendation if required.
"""

    else:

        prompt = f"""
You are an AI Attendance Assistant.

Answer the following question:

{question}
"""

    response = model.generate_content(prompt)

    print("\nAI Response:\n")
    print(response.text)