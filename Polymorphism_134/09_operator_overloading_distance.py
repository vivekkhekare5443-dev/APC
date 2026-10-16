"""
Polymorphism - Program 9 (Operator Overloading: __add__):
Create a class Distance with feet and inches.
Overload the + operator to add two distance objects and display the result in normalized form.
(Note: 12 inches = 1 foot)
"""

class Distance:
    def __init__(self, feet=0, inches=0):
        self.feet = feet
        self.inches = inches
        self.normalize()

    def normalize(self):
        """Converts excess inches (>= 12) into feet."""
        if self.inches >= 12:
            self.feet += int(self.inches // 12)
            self.inches = self.inches % 12

    def __add__(self, other):
        """Overloads the + operator to add two Distance objects."""
        if not isinstance(other, Distance):
            return NotImplemented
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        return Distance(total_feet, total_inches)

    def __str__(self):
        return f"{self.feet} ft {self.inches} in"

    def __repr__(self):
        return f"Distance({self.feet}, {self.inches})"


if __name__ == "__main__":
    d1 = Distance(5, 9)
    d2 = Distance(3, 8)

    print("=== Operator Overloading (+ Operator for Distance) ===")
    print(f"Distance 1 : {d1}")
    print(f"Distance 2 : {d2}")

    # Using the overloaded '+' operator
    d3 = d1 + d2

    print("-" * 45)
    print(f"Result (d1 + d2) in normalized form: {d3}")
    print(f"Explanation: (5 ft + 3 ft) = 8 ft; (9 in + 8 in) = 17 in = 1 ft 5 in; Total = 9 ft 5 in.")
