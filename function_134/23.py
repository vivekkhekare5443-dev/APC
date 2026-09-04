def total_marks(marks):
    return sum(marks)


def percentage(marks):
    return sum(marks) / 5


def grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")

    marks = []
    for j in range(5):
        marks.append(float(input("Enter marks: ")))

    total = total_marks(marks)
    percent = percentage(marks)
    gr = grade(percent)

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percent,
        "grade": gr
    })

class_average = sum(s["percentage"] for s in students) / n
highest = max(students, key=lambda s: s["percentage"])
lowest = min(students, key=lambda s: s["percentage"])

print("\n--- Student Records ---")

for s in students:
    print("\nName:", s["name"])
    print("Roll No:", s["roll"])
    print("Total:", s["total"])
    print("Percentage:", s["percentage"])
    print("Grade:", s["grade"])

print("\nClass Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])