"""
Polymorphism - Program 1 (Method Overriding & Runtime Polymorphism):
Create a base class Shape with a method area().
Derive Circle, Rectangle, and Triangle classes and override the area() method in each class.
Create objects of each class and demonstrate runtime polymorphism.
"""

import math

class Shape:
    def area(self):
        """Base method to be overridden by derived classes."""
        return 0.0

    def describe(self):
        return f"{self.__class__.__name__} Area: {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


if __name__ == "__main__":
    # Create a polymorphic collection of Shape objects
    shapes = [
        Circle(radius=5),
        Rectangle(length=10, breadth=4),
        Triangle(base=8, height=6)
    ]

    print("=== Demonstrating Runtime Polymorphism through Shape.area() ===")
    for shape in shapes:
        # Dynamic method dispatch determines the appropriate area() implementation at runtime
        print(shape.describe())
