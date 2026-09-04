def calculate_grade(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter marks: ")))

percentage, grade = calculate_grade(marks)

print("Percentage =", percentage)
print("Grade =", grade)