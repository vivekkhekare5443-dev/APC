"""
Polymorphism - Program 4:
Create a base class Animal with a method sound().
Create subclasses Dog, Cat, Cow, and Lion.
Override sound() in each class to display the appropriate sound.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes an unknown sound.")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} (Dog) barks: Woof! Woof!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} (Cat) meows: Meow~ Purr~")


class Cow(Animal):
    def sound(self):
        print(f"{self.name} (Cow) moos: Moooo!")


class Lion(Animal):
    def sound(self):
        print(f"{self.name} (Lion) roars: ROAAR! The jungle trembles.")


if __name__ == "__main__":
    zoo = [
        Dog("Bruno"),
        Cat("Whiskers"),
        Cow("Kamadhenu"),
        Lion("Simba")
    ]

    print("=== Animal Sound Polymorphism ===")
    for animal in zoo:
        animal.sound()
