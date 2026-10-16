"""
Polymorphism - Program 3:
Create a base class Vehicle with a method start().
Derive Car, Bike, and Bus classes and override start() to display the starting behavior of each vehicle.
"""

class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"{self.name}: Generic vehicle ignition system engaged.")


class Car(Vehicle):
    def start(self):
        print(f"[Car: {self.name}] Push-button start activated. Engine roars to life and dashboard initializes.")


class Bike(Vehicle):
    def start(self):
        print(f"[Bike: {self.name}] Self-starter button pressed / Kick started. Exhaust purrs smoothly.")


class Bus(Vehicle):
    def start(self):
        print(f"[Bus: {self.name}] Air brake pressure checked. Heavy diesel engine ignited with deep rumble.")


if __name__ == "__main__":
    fleet = [
        Car("Honda City"),
        Bike("Royal Enfield Classic 350"),
        Bus("Volvo 9600 Multi-Axle")
    ]

    print("=== Demonstrating start() Polymorphism across Vehicle Fleet ===")
    for v in fleet:
        v.start()
