marks = {"Vivek": 90, "Tanvi": 85, "Sanika": 88}
name = input("Enter student name: ")
if name in marks:
    marks[name] = int(input("Enter new marks: "))
    print(marks)
else:
    print("Student not found")
