"""
Inheritance - Program 5 (Multilevel Inheritance):
Create a class Person containing name and age.
Derive a class Student from Person with roll number and course.
Further derive a class ResearchStudent from Student with research topic and guide name.
Display all details.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age} years")


class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

    def display_student(self):
        self.display_person()
        print(f"Roll Number : {self.roll_number}")
        print(f"Course      : {self.course}")


class ResearchStudent(Student):
    def __init__(self, name, age, roll_number, course, research_topic, guide_name):
        super().__init__(name, age, roll_number, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display_research_student(self):
        print("=== Research Student Complete Record ===")
        self.display_student()
        print(f"Research Topic : {self.research_topic}")
        print(f"Guide Name     : {self.guide_name}")


if __name__ == "__main__":
    scholar = ResearchStudent(
        name="Rohan Verma",
        age=26,
        roll_number="PHD-CS-04",
        course="Ph.D. in Computer Science",
        research_topic="Quantum Natural Language Processing",
        guide_name="Dr. K. S. Ramanujan"
    )
    scholar.display_research_student()
