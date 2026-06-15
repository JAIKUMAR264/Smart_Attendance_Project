from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("attendance_data.csv")

df["Attendance_Percentage"] = (df["Attended"] / df["Total_Classes"]) * 100

df["Status"] = df["Attendance_Percentage"].apply(
    lambda x: "Safe" if x >= 75 else "Shortage"
)
from sklearn.tree import DecisionTreeClassifier

# Convert status to numbers
df["Target"] = df["Status"].map({
    "Safe": 1,
    "Shortage": 0
})

# Features and Target
X = df[["Attendance_Percentage"]]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL ACCURACY")
print(f"Accuracy: {accuracy * 100:.2f}%")

# User Input Prediction
attendance = float(input("\nEnter Attendance Percentage: "))

new_attendance = pd.DataFrame({
    "Attendance_Percentage": [attendance]
})

prediction = model.predict(new_attendance)

print("\nML PREDICTION")
if prediction[0] == 1:
    print("Predicted Status: Safe")
else:
    print("Predicted Status: Shortage")

print("\nATTENDANCE REPORT")
print(df)

print("\nSUMMARY")
print("Total Students:", len(df))
print("Average Attendance:", round(df["Attendance_Percentage"].mean(), 2))

safe_count = len(df[df["Status"] == "Safe"])
shortage_count = len(df[df["Status"] == "Shortage"])

print("Safe Students:", safe_count)
print("Shortage Students:", shortage_count)

highest = df.loc[df["Attendance_Percentage"].idxmax()]
lowest = df.loc[df["Attendance_Percentage"].idxmin()]

print("\nHighest Attendance:")
print(highest["Name"], "-", highest["Attendance_Percentage"], "%")

print("\nLowest Attendance:")
print(lowest["Name"], "-", lowest["Attendance_Percentage"], "%")

# Save report
df.to_csv("attendance_report.csv", index=False)

# Bar Chart
plt.figure(figsize=(10,5))
plt.bar(df["Name"], df["Attendance_Percentage"])
plt.title("Student Attendance Percentage")
plt.xlabel("Students")
plt.ylabel("Attendance %")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,6))
plt.pie(
    [safe_count, shortage_count],
    labels=["Safe", "Shortage"],
    autopct="%1.1f%%"
)
plt.title("Attendance Status Distribution")
plt.show()