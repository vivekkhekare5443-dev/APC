"""
Abstraction - Program 2:
Create an abstract class Vehicle with abstract methods start() and stop().
Derive Car, Bike, and Bus classes and implement these methods.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    @abstractmethod
    def start(self):
        """Abstract start procedure."""
        pass

    @abstractmethod
    def stop(self):
        """Abstract stop procedure."""
        pass

    def get_status(self):
        return f"{self.brand} {self.model} - Status: {'Running' if self.is_running else 'Stopped'}"


class Car(Vehicle):
    def start(self):
        self.is_running = True
        print(f"[Car: {self.brand} {self.model}] Keyless fob detected. Engine started via push-button.")

    def stop(self):
        self.is_running = False
        print(f"[Car: {self.brand} {self.model}] Engine shut down. Electronic parking brake engaged.")


class Bike(Vehicle):
    def start(self):
        self.is_running = True
        print(f"[Bike: {self.brand} {self.model}] Ignition switch turned ON. Self-starter fired the engine.")

    def stop(self):
        self.is_running = False
        print(f"[Bike: {self.brand} {self.model}] Engine kill-switch turned off. Side stand deployed.")


class Bus(Vehicle):
    def start(self):
        self.is_running = True
        print(f"[Bus: {self.brand} {self.model}] Air compression system checked. Turbo diesel engine initialized.")

    def stop(self):
        self.is_running = False
        print(f"[Bus: {self.brand} {self.model}] Pneumatic brakes locked. Heavy engine turned off.")


if __name__ == "__main__":
    vehicles = [
        Car("Tata", "Harrier"),
        Bike("Yamaha", "R15 V4"),
        Bus("Ashok Leyland", "Viking")
    ]

    print("=== Testing Abstract Interface: Vehicle.start() and stop() ===")
    for v in vehicles:
        print(f"\n--- {v.get_status()} ---")
        v.start()
        print(f"Status after start: {v.get_status()}")
        v.stop()
        print(f"Status after stop:  {v.get_status()}")
