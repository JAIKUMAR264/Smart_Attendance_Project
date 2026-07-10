import pandas as pd
from transformers import pipeline

# Load the feedback dataset
df = pd.read_csv("student_feedback.csv", sep="\t")

print("FIRST 5 RECORDS")

print(df.columns)
print(df.head())

# Load pretrained BERT sentiment analysis pipeline
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Predict sentiment
sentiments = []

for feedback in df["Feedback"]:
    result = classifier(feedback)[0]
    sentiments.append(result["label"])

# Add sentiment column
df["Sentiment"] = sentiments

print("\nSENTIMENT RESULTS")
print(df.head(10))

# Save results
df.to_csv("student_feedback_sentiment.csv", index=False)

print("\nSentiment analysis completed successfully!")
print("File saved as: student_feedback_sentiment.csv")