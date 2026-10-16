"""
Inheritance - Program 17 (Hierarchical Inheritance):
Create a base class Animal with common attributes and methods.
Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.
"""

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating food.")

    def sleep(self):
        print(f"{self.name} is resting peacefully.")

    def make_sound(self):
        print(f"{self.name} makes a generic animal sound.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, species="Dog")
        self.breed = breed

    def make_sound(self):
        print(f"[Sound] {self.name} ({self.breed}) barks: Woof! Woof!")

    def fetch(self, item):
        print(f"[Behavior] {self.name} wags its tail and happily fetches the {item}.")


class Cat(Animal):
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age, species="Cat")
        self.indoor = indoor

    def make_sound(self):
        print(f"[Sound] {self.name} purrs and meows: Meow~")

    def scratch(self):
        print(f"[Behavior] {self.name} is sharpening claws on the scratching post.")


class Cow(Animal):
    def __init__(self, name, age, daily_milk_liters):
        super().__init__(name, age, species="Cow")
        self.daily_milk_liters = daily_milk_liters

    def make_sound(self):
        print(f"[Sound] {self.name} bellows gently: Mooo!")

    def graze(self):
        print(f"[Behavior] {self.name} is happily grazing on green pastures.")


if __name__ == "__main__":
    animals = [
        Dog("Bruno", 4, "Golden Retriever"),
        Cat("Luna", 2, indoor=True),
        Cow("Gauri", 5, daily_milk_liters=14.5)
    ]

    print("=== Animal Sounds and Unique Behaviors ===")
    for a in animals:
        print(f"\nAnimal: {a.name} ({a.species}, {a.age} years old)")
        a.eat()
        a.make_sound()

    print("\n--- Specific Behaviors ---")
    animals[0].fetch("tennis ball")
    animals[1].scratch()
    animals[2].graze()
