"""
Polymorphism - Program 6:
Create a base class Student with a method calculate_grade().
Derive EngineeringStudent, MedicalStudent, and ManagementStudent.
Override the method according to different grading criteria.
"""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def calculate_grade(self):
        """Default grading scheme."""
        return "Passed" if self.score >= 50 else "Failed"


class EngineeringStudent(Student):
    def calculate_grade(self):
        # Engineering grading: strict technical cutoff
        if self.score >= 85:
            return "Grade S (Distinction in Engineering)"
        elif self.score >= 75:
            return "Grade A (First Class)"
        elif self.score >= 60:
            return "Grade B (Second Class)"
        elif self.score >= 45:
            return "Grade C (Pass)"
        else:
            return "Grade F (Reappear)"


class MedicalStudent(Student):
    def calculate_grade(self):
        # Medical grading: higher pass threshold (50% min) and rigorous clinical band
        if self.score >= 80:
            return "Honours with Distinction"
        elif self.score >= 65:
            return "First Class Division"
        elif self.score >= 50:
            return "Pass (Cleared for Clinical Internship)"
        else:
            return "Unsatisfactory (Supplementary Exam Required)"


class ManagementStudent(Student):
    def calculate_grade(self):
        # Management grading: GPA style scale
        if self.score >= 90:
            return "A+ (Executive Leadership Honour)"
        elif self.score >= 80:
            return "A (Merit)"
        elif self.score >= 70:
            return "B+ (Competent)"
        elif self.score >= 55:
            return "B (Satisfactory)"
        else:
            return "C (Remedial Action Required)"


if __name__ == "__main__":
    candidates = [
        EngineeringStudent("Rohan Verma", 82),
        MedicalStudent("Dr. Diya Patel", 78),
        ManagementStudent("Aarav Sharma", 88)
    ]

    print("=== Degree-Specific Grading Evaluation (Polymorphic Grading) ===")
    for candidate in candidates:
        domain = type(candidate).__name__
        grade = candidate.calculate_grade()
        print(f"[{domain:<18}] {candidate.name:<16} | Score: {candidate.score}% -> {grade}")
