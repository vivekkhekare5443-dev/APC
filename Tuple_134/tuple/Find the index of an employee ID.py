employee_ids = (101, 102, 103, 104, 105)

emp_id = int(input("Enter employee ID: "))

if emp_id in employee_ids:
    print("Index:", employee_ids.index(emp_id))
else:
    print("Employee ID not found")
