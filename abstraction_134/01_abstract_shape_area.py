"""
Abstraction - Program 1:
Create an abstract class Shape with an abstract method area().
Derive Circle, Rectangle, and Triangle classes and implement the area() method for each shape.
Create objects of the derived classes and display their areas.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by all concrete shape subclasses."""
        pass

    def display_info(self):
        """Concrete method in abstract base class."""
        print(f"Shape: {self.name} | Area: {self.area():.2f} sq units")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


if __name__ == "__main__":
    print("=== Abstract Class Shape and Concrete Implementations ===")
    shapes = [
        Circle(radius=7),
        Rectangle(length=14, width=6),
        Triangle(base=10, height=8)
    ]

    for s in shapes:
        s.display_info()

    # Demonstrating abstraction enforcement:
    print("\nDemonstrating that abstract class cannot be instantiated directly:")
    try:
        raw_shape = Shape("Generic")
    except TypeError as e:
        print(f"  Caught expected error: {e}")
