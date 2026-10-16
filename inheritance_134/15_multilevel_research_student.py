"""
Inheritance - Program 15 (Multilevel Inheritance with Academic Progress Evaluation):
Create a class Person with name and age.
Derive Student with roll number and course.
Further derive ResearchStudent with research topic and guide name.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, roll_number, course, semester):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course
        self.semester = semester

    def get_info(self):
        return f"{super().get_info()} | Roll: {self.roll_number}, Course: {self.course} (Sem {self.semester})"


class ResearchStudent(Student):
    def __init__(self, name, age, roll_number, course, semester, research_topic, guide_name, thesis_submitted=False):
        super().__init__(name, age, roll_number, course, semester)
        self.research_topic = research_topic
        self.guide_name = guide_name
        self.thesis_submitted = thesis_submitted

    def submit_thesis(self):
        self.thesis_submitted = True
        print(f"[Notice] Thesis on '{self.research_topic}' submitted for evaluation.")

    def display_full_profile(self):
        print("=== Doctoral Research Scholar Record ===")
        print(self.get_info())
        print(f"Research Topic   : {self.research_topic}")
        print(f"Faculty Advisor  : {self.guide_name}")
        print(f"Thesis Status    : {'Submitted' if self.thesis_submitted else 'In Progress'}")


if __name__ == "__main__":
    rs = ResearchStudent(
        name="Ananya Sen",
        age=27,
        roll_number="RS-2023-09",
        course="Ph.D. Computer Engineering",
        semester=6,
        research_topic="Explainable AI for Healthcare Diagnostics",
        guide_name="Prof. M. S. Swaminathan"
    )
    rs.display_full_profile()
    print()
    rs.submit_thesis()
    print()
    rs.display_full_profile()
