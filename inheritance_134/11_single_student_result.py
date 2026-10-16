"""
Inheritance - Program 11:
Create a base class Student with attributes roll_no, name, and course.
Derive a class Result that stores marks in three subjects and calculates total marks,
percentage, and grade.
"""

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def display_student(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Course  : {self.course}")


class Result(Student):
    def __init__(self, roll_no, name, course, sub1_marks, sub2_marks, sub3_marks):
        super().__init__(roll_no, name, course)
        self.sub1_marks = sub1_marks
        self.sub2_marks = sub2_marks
        self.sub3_marks = sub3_marks

    def calculate_total(self):
        return self.sub1_marks + self.sub2_marks + self.sub3_marks

    def calculate_percentage(self):
        return (self.calculate_total() / 300) * 100

    def calculate_grade(self):
        pct = self.calculate_percentage()
        if pct >= 90:
            return "A+ (Outstanding)"
        elif pct >= 80:
            return "A (Excellent)"
        elif pct >= 70:
            return "B (Good)"
        elif pct >= 60:
            return "C (Average)"
        elif pct >= 50:
            return "D (Pass)"
        else:
            return "F (Fail)"

    def display_result(self):
        print("=== Student Examination Marksheet ===")
        self.display_student()
        print(f"Subject 1 Marks : {self.sub1_marks} / 100")
        print(f"Subject 2 Marks : {self.sub2_marks} / 100")
        print(f"Subject 3 Marks : {self.sub3_marks} / 100")
        print(f"Total Marks     : {self.calculate_total()} / 300")
        print(f"Percentage      : {self.calculate_percentage():.2f}%")
        print(f"Final Grade     : {self.calculate_grade()}")


if __name__ == "__main__":
    student_res = Result("CS-101", "Kabir Mehta", "B.Tech Computer Science", 85, 92, 78)
    student_res.display_result()
