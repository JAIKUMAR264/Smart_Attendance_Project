import pandas as pd

# Load report
df = pd.read_csv("student_report.csv")

print("=" * 60)
print("     SMART ATTENDANCE ANALYTICAL PLATFORM")
print("         Attendance Q&A System")
print("=" * 60)

while True:

    print("\nChoose an option")
    print("-" * 40)
    print("1. Show Highest Attendance Student")
    print("2. Show Lowest Attendance Student")
    print("3. Total Safe Students")
    print("4. Total Shortage Students")
    print("5. Search Student by ID")
    print("6. Students with Negative Feedback")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":

        student = df.loc[df["Attendance_Percentage"].idxmax()]

        print("\n========== HIGHEST ATTENDANCE ==========")
        print(student)

    elif choice == "2":

        student = df.loc[df["Attendance_Percentage"].idxmin()]

        print("\n========== LOWEST ATTENDANCE ==========")
        print(student)

    elif choice == "3":

        safe = (df["Status"] == "Safe").sum()

        print("\nTotal Safe Students :", safe)

    elif choice == "4":

        shortage = (df["Status"] == "Shortage").sum()

        print("\nTotal Shortage Students :", shortage)

    elif choice == "5":

        sid = input("\nEnter Student ID (Example: S00001): ").strip().upper()

        result = df[df["Student_ID"] == sid]

        if not result.empty:

            print("\n========== STUDENT REPORT ==========")
            print(result.to_string(index=False))

        else:

            print("\nStudent ID not found.")

    elif choice == "6":

        negative = df[df["Sentiment"] == "NEGATIVE"]

        print("\n========== NEGATIVE FEEDBACK ==========")
        print(negative[["Student_ID", "Feedback", "Sentiment"]].to_string(index=False))

    elif choice == "7":

        print("\nThank you for using Smart Attendance Analytical Platform.")
        break

    else:

        print("\nInvalid choice! Please enter a number between 1 and 7.")

    again = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()

    if again != "yes":

        print("\nThank you for using Smart Attendance Analytical Platform.")
        break