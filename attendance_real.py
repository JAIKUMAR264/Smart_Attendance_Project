from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv("attendance.csv")

print("\nDATASET INFORMATION")
print(df.info())
# Clean Attendance_Status column
df["Attendance_Status"] = (
    df["Attendance_Status"]
    .str.strip()      # Remove extra spaces
    .str.lower()      # Convert to lowercase
)

# Correct spelling variations
df["Attendance_Status"] = df["Attendance_Status"].replace({
    "present": "present",
    "late": "late",
    "excused": "excused",
    "left early": "left_early",
    "absent": "absent",
    "absnt": "absent"
})

print("\nUNIQUE ATTENDANCE STATUS")
print(df["Attendance_Status"].value_counts())



# Treat only "present and late and excused" as attended
df["Present"] = df["Attendance_Status"].isin(
    ["present", "late", "excused"]
).astype(int)

# Attendance summary for each student
attendance_summary = (
    df.groupby("Student_ID")
      .agg(
          Total_Classes=("Attendance_Status", "count"),
          Attended=("Present", "sum")
      )
)

attendance_summary["Attendance_Percentage"] = (
    attendance_summary["Attended"] /
    attendance_summary["Total_Classes"]
) * 100

print("\nATTENDANCE SUMMARY")
print(attendance_summary.head(10))
print("\nSUBJECT-WISE ATTENDANCE")

subject_summary = (
    df.groupby("Subject")
      .agg(
          Total_Classes=("Attendance_Status", "count"),
          Attended=("Present", "sum")
      )
)

subject_summary["Attendance_Percentage"] = (
    subject_summary["Attended"] /
    subject_summary["Total_Classes"]
) * 100

attendance_summary["Status"] = attendance_summary["Attendance_Percentage"].apply(
    lambda x: "Safe" if x >= 75 else "Shortage"
)
attendance_summary["Target"] = attendance_summary["Status"].map({
    "Shortage": 0,
    "Safe": 1
})
print("\nATTENDANCE SUMMARY WITH STATUS")
print(attendance_summary.head(10))
print("\nSTATUS COUNT")
print(attendance_summary["Status"].value_counts())
# Features and Target
X = attendance_summary[["Attendance_Percentage"]]
y = attendance_summary["Target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL ACCURACY")
print(f"Accuracy: {accuracy*100:.2f}%")

print(subject_summary)
top10 = attendance_summary.sort_values(
    by="Attendance_Percentage",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))
plt.bar(top10.index, top10["Attendance_Percentage"])
plt.title("Top 10 Students by Attendance Percentage")
plt.xlabel("Student ID")
plt.ylabel("Attendance Percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
status_counts = df["Attendance_Status"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    status_counts,
    labels=status_counts.index,
    autopct="%1.1f%%"
)
plt.title("Attendance Status Distribution")
plt.show()
plt.figure(figsize=(8,5))

plt.hist(
    attendance_summary["Attendance_Percentage"],
    bins=10
)

plt.title("Attendance Percentage Distribution")
plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")

plt.show()