"""
Inheritance - Program 10 (Hybrid Inheritance: Hierarchical + Multilevel):
Create a base class Vehicle. Derive Car and Bike from Vehicle.
Create a class SportsCar that inherits from Car and another class ElectricBike that inherits from Bike.
Add suitable attributes and methods to demonstrate a combination of inheritance types.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


# Hierarchical: Car derives from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity

    def display_car(self):
        self.display_vehicle()
        print(f"Seating Capacity : {self.seating_capacity} passengers")


# Hierarchical: Bike derives from Vehicle
class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_bike(self):
        self.display_vehicle()
        print(f"Engine Capacity  : {self.engine_cc} cc")


# Multilevel: SportsCar derives from Car
class SportsCar(Car):
    def __init__(self, brand, model, seating_capacity, top_speed, turbo_boost):
        super().__init__(brand, model, seating_capacity)
        self.top_speed = top_speed
        self.turbo_boost = turbo_boost

    def display_details(self):
        print("--- Sports Car Details ---")
        self.display_car()
        print(f"Top Speed        : {self.top_speed} km/h")
        print(f"Turbo Boost      : {'Yes' if self.turbo_boost else 'No'}")


# Multilevel: ElectricBike derives from Bike
class ElectricBike(Bike):
    def __init__(self, brand, model, battery_capacity_kwh, riding_range_km):
        super().__init__(brand, model, engine_cc=0)  # 0 CC for electric
        self.battery_capacity_kwh = battery_capacity_kwh
        self.riding_range_km = riding_range_km

    def display_details(self):
        print("--- Electric Bike Details ---")
        self.display_vehicle()
        print(f"Battery Capacity : {self.battery_capacity_kwh} kWh")
        print(f"Single Charge Range: {self.riding_range_km} km")


if __name__ == "__main__":
    ferrari = SportsCar("Ferrari", "F8 Tributo", 2, top_speed=340, turbo_boost=True)
    ferrari.display_details()

    print()
    ather = ElectricBike("Ather", "450X Gen 3", battery_capacity_kwh=3.7, riding_range_km=146)
    ather.display_details()
