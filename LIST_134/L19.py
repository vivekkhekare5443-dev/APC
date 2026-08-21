students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

print("Total Students:", len(students))

search = input("Enter student name to search: ")

if search in students:
    print(search, "is present.")
else:
    print(search, "is absent.")

new_student = input("Enter new student name: ")
students.append(new_student)

absent = input("Enter absent student name to remove: ")

if absent in students:
    students.remove(absent)
    print("Student removed.")
else:
    print("Student not found.")

print("Updated Student List:", students)
