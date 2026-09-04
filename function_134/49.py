students = [
    ("Rahul", 80),
    ("Amit", 65),
    ("Sneha", 92),
    ("Priya", 78)
]


def average_marks(students):
    return sum(map(lambda s: s[1], students)) / len(students)


above_75 = list(filter(lambda s: s[1] > 75, students))

sorted_students = sorted(students, key=lambda s: s[1])

print("Average Marks =", average_marks(students))

print("\nStudents scoring above 75:")
print(above_75)

print("\nStudents sorted according to marks:")
print(sorted_students)