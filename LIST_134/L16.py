students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    marks = float(input("Enter Marks: "))

    students.append([name, roll, marks])

print("\nStudent Details")
for student in students:
    print("Name:", student[0])
    print("Roll No:", student[1])
    print("Marks:", student[2])
    print()
