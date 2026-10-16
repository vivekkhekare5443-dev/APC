"""
Inheritance - Program 9 (Hybrid / Diamond Inheritance):
Create a class Person. Derive Student and Faculty from Person.
Create another class TeachingAssistant that inherits from both Student and Faculty.
Display the details and demonstrate the use of multiple and hierarchical inheritance together.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age} years")


class Student(Person):
    def __init__(self, name, age, roll_no, program):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.program = program

    def display_student(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Program : {self.program}")


class Faculty(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_faculty(self):
        print(f"Faculty ID : {self.employee_id}")
        print(f"Department : {self.department}")


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, program, employee_id, department, stipend, assigned_course):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.program = program
        self.employee_id = employee_id
        self.department = department
        self.stipend = stipend
        self.assigned_course = assigned_course

    def display_ta_profile(self):
        print("=== Teaching Assistant (Hybrid Inheritance) ===")
        self.display_person()
        self.display_student()
        self.display_faculty()
        print(f"Assigned Lab/Course : {self.assigned_course}")
        print(f"Monthly Stipend     : Rs. {self.stipend:,.2f}")


if __name__ == "__main__":
    ta = TeachingAssistant(
        name="Meera Nair",
        age=24,
        roll_no="MTECH-AI-12",
        program="M.Tech AI & Robotics",
        employee_id="TA-8041",
        department="Computer Science & Engineering",
        stipend=25000,
        assigned_course="Data Structures Lab"
    )
    ta.display_ta_profile()
    print("\nMethod Resolution Order (MRO):", [cls.__name__ for cls in TeachingAssistant.__mro__])
