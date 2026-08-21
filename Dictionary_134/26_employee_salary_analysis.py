employees = {"Rahul": 45000, "Priya": 60000, "Amit": 75000, "Sneha": 55000}
print("Highest:", max(employees.values()))
print("Lowest:", min(employees.values()))
print("Average:", sum(employees.values()) / len(employees))
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)
