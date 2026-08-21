employees = {101: "Rahul", 102: "Priya", 103: "Amit"}
emp_id = int(input("Enter employee ID: "))
if emp_id in employees:
    print("Employee exists:", employees[emp_id])
else:
    print("Employee does not exist")
