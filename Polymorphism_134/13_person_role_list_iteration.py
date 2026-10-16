"""
Polymorphism - Program 13:
Create a base class Person with a method display_role().
Derive Student, Faculty, and Administrator.
Override the method to display the respective role.
Store all objects in a list and invoke the same method using a loop.
"""

class Person:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display_role(self):
        print(f"{self.name} is a member of the institution in {self.department}.")


class Student(Person):
    def __init__(self, name, department, roll_number):
        super().__init__(name, department)
        self.roll_number = roll_number

    def display_role(self):
        print(f"[Student] {self.name} (Roll: {self.roll_number}) | Enrolled in {self.department} coursework.")


class Faculty(Person):
    def __init__(self, name, department, designation):
        super().__init__(name, department)
        self.designation = designation

    def display_role(self):
        print(f"[Faculty] {self.name} ({self.designation}) | Teaches and conducts research in {self.department}.")


class Administrator(Person):
    def __init__(self, name, department, admin_responsibility):
        super().__init__(name, department)
        self.admin_responsibility = admin_responsibility

    def display_role(self):
        print(f"[Admin]   {self.name} | Manages {self.admin_responsibility} across {self.department}.")


if __name__ == "__main__":
    # Heterogeneous polymorphic collection
    campus_members = [
        Student("Aarav Sharma", "Computer Science", "CS-2026-042"),
        Faculty("Dr. Neha Deshmukh", "Computer Science", "Associate Professor"),
        Administrator("Sunil Rao", "Academic Affairs", "Admissions and Accreditation"),
        Student("Diya Patel", "Electronics", "EC-2026-118"),
        Faculty("Prof. Amitabh Sen", "Mechanical", "Head of Department")
    ]

    print("=== Invoking display_role() Polymorphically Across Campus Directory ===")
    for member in campus_members:
        member.display_role()
