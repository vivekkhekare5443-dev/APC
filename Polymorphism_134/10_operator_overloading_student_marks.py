"""
Polymorphism - Program 10 (Operator Overloading: __gt__ and __lt__):
Create a class Student containing the student's name and total marks.
Overload the > and < operators to compare the marks of two students.
"""

class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        """Overload '>' (greater than) operator."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        """Overload '<' (less than) operator."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.total_marks < other.total_marks

    def __eq__(self, other):
        """Overload '==' operator."""
        if not isinstance(other, Student):
            return NotImplemented
        return self.total_marks == other.total_marks

    def __str__(self):
        return f"{self.name} ({self.total_marks} Marks)"


if __name__ == "__main__":
    s1 = Student("Aarav Sharma", 485)
    s2 = Student("Diya Patel", 492)
    s3 = Student("Rohan Verma", 485)

    print("=== Operator Overloading (> and < for Student Marks) ===")
    print(f"Student 1: {s1}")
    print(f"Student 2: {s2}")
    print(f"Student 3: {s3}")
    print("-" * 55)

    # Testing > operator
    if s1 > s2:
        print(f"{s1.name} scored more marks than {s2.name}.")
    else:
        print(f"{s1.name} did not score more marks than {s2.name}.")

    # Testing < operator
    if s1 < s2:
        print(f"{s1.name} scored fewer marks than {s2.name}.")

    # Sorting a list of students using overloaded operators
    class_list = [s1, s2, s3]
    sorted_students = sorted(class_list, reverse=True)
    print("\nStudents ranked in descending order of marks:")
    for rank, st in enumerate(sorted_students, start=1):
        print(f"  Rank {rank}: {st}")
