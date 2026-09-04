employees = [
    ("Rahul", "IT", 55000),
    ("Amit", "HR", 45000),
    ("Sneha", "IT", 70000),
    ("Priya", "Sales", 48000)
]

# a) Employees earning more than 50000
high_salary = list(
    filter(lambda e: e[2] > 50000, employees)
)

# b) Increase salaries by 10%
increased_salary = list(
    map(lambda e: (e[0], e[1], e[2] * 1.10), employees)
)

# c) Sort according to salary
sorted_employees = sorted(
    employees,
    key=lambda e: e[2]
)

print("Employees earning more than ₹50,000:")
print(high_salary)

print("\nSalaries after 10% increase:")
print(increased_salary)

print("\nEmployees sorted according to salary:")
print(sorted_employees)