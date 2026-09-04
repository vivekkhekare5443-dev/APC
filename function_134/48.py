employees = [
    ("Rahul", 45000),
    ("Amit", 60000),
    ("Sneha", 52000),
    ("Priya", 40000)
]

employees.sort(key=lambda employee: employee[1])

print("Employees sorted by salary:")

for employee in employees:
    print(employee)