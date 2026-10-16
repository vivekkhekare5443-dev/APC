"""
Inheritance - Program 8 (Hierarchical Inheritance):
Create a base class Employee containing employee ID, name, and basic salary.
Create derived classes Manager, Developer, and Tester.
Each derived class should calculate salary differently based on its respective allowances.
"""

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display_base(self):
        print(f"ID           : {self.emp_id}")
        print(f"Name         : {self.name}")
        print(f"Basic Salary : Rs. {self.basic_salary:,.2f}")


class Manager(Employee):
    def __init__(self, emp_id, name, basic_salary, leadership_allowance, hra_percent=20):
        super().__init__(emp_id, name, basic_salary)
        self.leadership_allowance = leadership_allowance
        self.hra_percent = hra_percent

    def calculate_total_salary(self):
        hra = (self.basic_salary * self.hra_percent) / 100
        return self.basic_salary + hra + self.leadership_allowance


class Developer(Employee):
    def __init__(self, emp_id, name, basic_salary, project_bonus, tech_allowance):
        super().__init__(emp_id, name, basic_salary)
        self.project_bonus = project_bonus
        self.tech_allowance = tech_allowance

    def calculate_total_salary(self):
        return self.basic_salary + self.project_bonus + self.tech_allowance


class Tester(Employee):
    def __init__(self, emp_id, name, basic_salary, qa_certification_allowance):
        super().__init__(emp_id, name, basic_salary)
        self.qa_certification_allowance = qa_certification_allowance

    def calculate_total_salary(self):
        return self.basic_salary + self.qa_certification_allowance


if __name__ == "__main__":
    staff = [
        Manager("M101", "Vikram Malhotra", 70000, leadership_allowance=25000),
        Developer("D202", "Ananya Sen", 55000, project_bonus=15000, tech_allowance=8000),
        Tester("T303", "Karan Johar", 42000, qa_certification_allowance=6000)
    ]

    print("=== Employee Role-Based Allowances and Total Salaries ===")
    for emp in staff:
        emp.display_base()
        role = type(emp).__name__
        print(f"Role         : {role}")
        print(f"Total Salary : Rs. {emp.calculate_total_salary():,.2f}\n")
