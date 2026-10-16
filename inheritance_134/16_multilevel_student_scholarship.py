"""
Inheritance - Program 16 (Multilevel Inheritance with Fellowship and Publication Tracking):
Create a class Person with name and age.
Derive Student with roll number and course.
Further derive ResearchStudent with research topic and guide name.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age} years")


class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

    def display(self):
        super().display()
        print(f"Roll Number : {self.roll_number}")
        print(f"Course      : {self.course}")


class ResearchStudent(Student):
    def __init__(self, name, age, roll_number, course, research_topic, guide_name, fellowship_amount=35000):
        super().__init__(name, age, roll_number, course)
        self.research_topic = research_topic
        self.guide_name = guide_name
        self.fellowship_amount = fellowship_amount
        self.publications = []

    def add_publication(self, paper_title, journal_name):
        self.publications.append((paper_title, journal_name))

    def display(self):
        print("=== Research Scholar Fellowship & Research Dossier ===")
        super().display()
        print(f"Research Topic     : {self.research_topic}")
        print(f"Research Guide     : {self.guide_name}")
        print(f"Monthly Fellowship : Rs. {self.fellowship_amount:,.2f}")
        print(f"Published Papers   : {len(self.publications)}")
        for idx, (title, journal) in enumerate(self.publications, start=1):
            print(f"   [{idx}] \"{title}\" - {journal}")


if __name__ == "__main__":
    scholar = ResearchStudent(
        name="Vivaan Reddy",
        age=25,
        roll_number="RS-AI-401",
        course="M.S. by Research",
        research_topic="Autonomous Drone Navigation with Deep Reinforcement Learning",
        guide_name="Dr. Radhakrishnan"
    )
    scholar.add_publication("Real-time Obstacle Avoidance for Micro-UAVs", "IEEE Robotics & Automation Letters")
    scholar.add_publication("Visual Odometry in GPS-Denied Environments", "ACM Transactions on Cyber-Physical Systems")
    scholar.display()
