"""
Inheritance - Program 3 (Multiple Inheritance):
Create two classes Academic and Sports. The Academic class should store marks
obtained by a student, while the Sports class should store sports points.
Create a class Student that inherits from both classes and calculates
the student's overall performance.
"""

class Academic:
    def __init__(self, academic_marks):
        self.academic_marks = academic_marks

    def display_academic(self):
        print(f"Academic Marks (out of 100): {self.academic_marks}")


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

    def display_sports(self):
        print(f"Sports Points (out of 50)  : {self.sports_points}")


class Student(Academic, Sports):
    def __init__(self, roll_no, name, academic_marks, sports_points):
        self.roll_no = roll_no
        self.name = name
        Academic.__init__(self, academic_marks)
        Sports.__init__(self, sports_points)

    def calculate_overall_performance(self):
        # Overall performance out of 150 total points
        total_score = self.academic_marks + self.sports_points
        percentage = (total_score / 150) * 100
        return total_score, percentage

    def display_student_report(self):
        print(f"Roll Number : {self.roll_no}")
        print(f"Name        : {self.name}")
        self.display_academic()
        self.display_sports()
        total, pct = self.calculate_overall_performance()
        print(f"Total Score : {total} / 150")
        print(f"Performance : {pct:.2f}%")


if __name__ == "__main__":
    s = Student("CS2026", "Aarav Sharma", 88, 42)
    print("--- Student Overall Performance Report ---")
    s.display_student_report()
