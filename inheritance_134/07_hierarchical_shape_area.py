"""
Inheritance - Program 7 (Hierarchical Inheritance):
Create a base class Shape containing a method to display the name of the shape.
Create three derived classes Circle, Rectangle, and Triangle.
Each class should implement its own method to calculate the area.
"""

import math

class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def display_shape_name(self):
        print(f"Shape: {self.shape_name}")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


if __name__ == "__main__":
    shapes = [
        Circle(radius=7),
        Rectangle(length=12, breadth=8),
        Triangle(base=10, height=6)
    ]

    print("=== Hierarchical Shape Area Calculations ===")
    for s in shapes:
        s.display_shape_name()
        print(f"Calculated Area: {s.calculate_area():.2f} sq units\n")
