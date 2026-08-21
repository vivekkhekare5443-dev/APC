python_students = {"Vivek", "Rahul", "Tanvi"}
java_students = {"Rahul", "Sneha", "Tanvi"}

both = python_students.intersection(java_students)
only_one = python_students.symmetric_difference(java_students)

print("Students in both:", both)
print("Students in only one:", only_one)
