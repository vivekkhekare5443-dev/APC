"""
Inheritance - Program 4 (Multiple Inheritance):
Create classes PersonalDetails and ProfessionalDetails. Store personal information
such as name and age in the first class and employee ID, designation, and salary
in the second class. Create an Employee class that inherits from both classes
and displays complete employee information.
"""

class PersonalDetails:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_personal(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age} years")
        print(f"Gender : {self.gender}")


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

    def display_professional(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Designation : {self.designation}")
        print(f"Salary      : Rs. {self.salary:,.2f}")


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, gender, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age, gender)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display_employee_info(self):
        print("=== Complete Employee Profile ===")
        self.display_personal()
        self.display_professional()


if __name__ == "__main__":
    emp = Employee("Diya Patel", 28, "Female", "EMP-9021", "Senior Software Engineer", 88000)
    emp.display_employee_info()
