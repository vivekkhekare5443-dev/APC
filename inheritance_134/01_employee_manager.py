"""
Inheritance - Program 1:
Create a class Employee with attributes emp_id, name, and salary.
Create a derived class Manager that inherits from Employee and contains an additional
attribute department. Display all employee and manager details and calculate
the manager's annual salary.
"""

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee ID   : {self.emp_id}")
        print(f"Name          : {self.name}")
        print(f"Monthly Salary: Rs. {self.salary:,.2f}")

    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department    : {self.department}")
        print(f"Annual Salary : Rs. {self.calculate_annual_salary():,.2f}")


if __name__ == "__main__":
    print("--- General Employee ---")
    emp = Employee("E101", "Rajesh Kumar", 45000)
    emp.display_details()
    print(f"Annual Salary : Rs. {emp.calculate_annual_salary():,.2f}")

    print("\n--- Manager (Derived Class) ---")
    mgr = Manager("M201", "Priya Sharma", 85000, "Information Technology")
    mgr.display_details()
