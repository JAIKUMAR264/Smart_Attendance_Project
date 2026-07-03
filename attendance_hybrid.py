from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Dropout, Input
# Read dataset
df = pd.read_csv("attendance.csv")
df = df.head(50000)

print("FIRST 5 RECORDS")
print(df.head())

print("\nDATASET INFO")
print(df.info())
df["Attendance_Status"] = (
    df["Attendance_Status"]
    .str.strip()
    .str.lower()
)
encoder = LabelEncoder()

df["Attendance_Label"] = encoder.fit_transform(
    df["Attendance_Status"]
)

print("\nENCODED ATTENDANCE")
print(df[["Attendance_Status", "Attendance_Label"]].head(10))
# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Sort data by Student_ID and Date
df = df.sort_values(by=["Student_ID", "Date"])

print("\nSORTED DATA")
print(df.head(10))
print("\nTOTAL STUDENTS")
print(df["Student_ID"].nunique())
sequence_data = []

for student in df["Student_ID"].unique():

    student_data = df[df["Student_ID"] == student]

    sequence = student_data["Attendance_Label"].tolist()

    sequence_data.append(sequence)

print("\nTOTAL SEQUENCES")
print(len(sequence_data))

print("\nFIRST STUDENT SEQUENCE")
print(sequence_data[0])
X = []
y = []

sequence_length = 5

for sequence in sequence_data:

    if len(sequence) > sequence_length:

        for i in range(len(sequence) - sequence_length):

            X.append(sequence[i:i + sequence_length])

            y.append(sequence[i + sequence_length])

X = np.array(X)
y = np.array(y)

print("\nTRAINING DATA SHAPE")
print("X:", X.shape)
print("y:", y.shape)
# Reshape for LSTM
X = X.reshape((X.shape[0], X.shape[1], 1))

print("\nRESHAPED DATA")
print(X.shape)
model = Sequential()

# Input Layer
model.add(Input(shape=(5,1)))

# LSTM Layer
model.add(LSTM(64, return_sequences=True))

# Dropout
model.add(Dropout(0.2))

# GRU Layer
model.add(GRU(32))

# Dropout
model.add(Dropout(0.2))

# Dense Layer
model.add(Dense(32, activation="relu"))

# Output Layer
model.add(Dense(6, activation="softmax"))
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\n HY MODEL SUMMARY")
model.summary()


history = model.fit(
    X,
    y,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)
# Predict next attendance status
predictions = model.predict(X)

predicted_labels = np.argmax(predictions, axis=1)

print("\nFIRST 10 PREDICTIONS")
print(predicted_labels[:10])

print("\nACTUAL VALUES")
print(y[:10])
# Convert prediction probabilities into class labels
predicted_classes = np.argmax(predictions, axis=1)

# Accuracy
accuracy = accuracy_score(y, predicted_classes)

print("\nHYBRID MODEL ACCURACY")
print(f"Accuracy: {accuracy*100:.2f}%")

# Classification Report
print("\nCLASSIFICATION REPORT")
print(classification_report(y, predicted_classes))

# Confusion Matrix
print("\nCONFUSION MATRIX")
print(confusion_matrix(y, predicted_classes))
attendance_percentage = []

for sequence in sequence_data:
    percentage = (sequence.count(5) + sequence.count(2) + sequence.count(3)) / len(sequence) * 100
    attendance_percentage.append(percentage)
    risk = []

for percentage in attendance_percentage:

    if percentage >= 75:
        risk.append("Low Risk")

    elif percentage >= 50:
        risk.append("Medium Risk")

    else:
        risk.append("High Risk")

print("\nFIRST 10 STUDENT RISKS")

for i in range(10):
    print(
        df["Student_ID"].unique()[i],
        "-",
        risk[i]
    )
    