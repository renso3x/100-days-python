students = {
    "Romeo": 80,
    "Joy": 90,
    "Ricah": 95
}

student_grades = {}

for student in students:
    score = students[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Excellent"
    elif score > 70:
        student_grades[student] = "Acceptable"
print(student_grades)