import pandas as pd
import random

# 70 feedback sentences
positive_feedback = [
    "The classes are very interesting.",
    "Faculty explains concepts clearly.",
    "I enjoy attending practical sessions.",
    "Teaching quality is excellent.",
    "Attendance system is easy to use.",
    "The faculty is supportive.",
    "Learning materials are helpful.",
    "Practical classes improve understanding.",
    "Assignments help me learn.",
    "The course is well organized.",
    "Teachers encourage students.",
    "I like the classroom environment.",
    "The attendance portal works smoothly.",
    "The sessions are interactive.",
    "Faculty answers all doubts.",
    "The course content is useful.",
    "Excellent teaching methods.",
    "I am satisfied with the classes.",
    "The lab sessions are informative.",
    "The project guidance is excellent."
]

neutral_feedback = [
    "The classes are okay.",
    "Attendance system is average.",
    "The course is manageable.",
    "Faculty teaches normally.",
    "Nothing special about the classes.",
    "Assignments are acceptable.",
    "The attendance portal works most of the time.",
    "The classroom facilities are average.",
    "The timetable is manageable.",
    "Teaching is satisfactory."
]

negative_feedback = [
    "Too many assignments are given.",
    "Attendance system is confusing.",
    "The classroom is noisy.",
    "The portal is very slow.",
    "Faculty should explain better.",
    "The classes are boring.",
    "Attendance marking is incorrect.",
    "The schedule is stressful.",
    "More practical sessions are needed.",
    "Teaching pace is too fast."
]

feedback_list = (
    positive_feedback +
    neutral_feedback +
    negative_feedback
)

student_ids = [f"S{str(i).zfill(5)}" for i in range(1, 201)]

feedback = []

for student in student_ids:
    feedback.append({
        "Student_ID": student,
        "Feedback": random.choice(feedback_list)
    })

df = pd.DataFrame(feedback)

df.to_csv("student_feedback.csv", index=False)

print("student_feedback.csv created successfully!")
print(df.head(10))