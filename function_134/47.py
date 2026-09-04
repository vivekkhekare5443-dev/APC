students = [
    ("Rahul", 75),
    ("Amit", 90),
    ("Sneha", 82),
    ("Priya", 68)
]

students.sort(key=lambda student: student[1])

print("Students sorted by marks:")

for student in students:
    print(student)