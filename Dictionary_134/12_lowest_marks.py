students = {"Vivek": 90, "Tanvi": 85, "Sanika": 95}
student = min(students, key=students.get)
print("Lowest marks student:", student)
print("Marks:", students[student])
