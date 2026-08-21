students = {"Vivek": 90, "Tanvi": 85, "Sanika": 95}
topper = max(students, key=students.get)
print("Highest marks student:", topper)
print("Marks:", students[topper])
