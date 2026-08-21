n = int(input("Enter number of employees: "))

salaries = []

for i in range(n):
    salary = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(salary)

average = sum(salaries) / len(salaries)

print("Highest Salary:", max(salaries))
print("Lowest Salary:", min(salaries))
print("Average Salary:", average)

above50000 = 0
below30000 = 0

for salary in salaries:
    if salary > 50000:
        above50000 += 1
    if salary < 30000:
        below30000 += 1

print("Employees earning above ₹50,000:", above50000)
print("Employees earning below ₹30,000:", below30000)
