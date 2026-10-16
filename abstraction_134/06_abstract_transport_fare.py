"""
Abstraction - Program 6:
Create an abstract class Transport with an abstract method calculate_fare(distance).
Implement subclasses:
a) Bus
b) Train
c) Taxi
d) Flight
Calculate the fare according to the transportation type.
"""

from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, service_provider):
        self.service_provider = service_provider

    @abstractmethod
    def calculate_fare(self, distance_km):
        """Calculates travel fare for given distance in kilometers."""
        pass


class Bus(Transport):
    def calculate_fare(self, distance_km):
        # Rs. 2.5 per km, minimum fare Rs. 15
        fare = distance_km * 2.5
        return max(15.0, fare)


class Train(Transport):
    def calculate_fare(self, distance_km):
        # Base fare Rs. 50 + Rs. 1.25 per km for Sleeper/Express class
        base_fare = 50.0
        return base_fare + (distance_km * 1.25)


class Taxi(Transport):
    def calculate_fare(self, distance_km):
        # Base pickup fare Rs. 100 + Rs. 18 per km
        base_fare = 100.0
        return base_fare + (distance_km * 18.0)


class Flight(Transport):
    def calculate_fare(self, distance_km):
        # Base aviation fee Rs. 2500 + Rs. 5.5 per km + Rs. 650 airport tax
        base_fare = 2500.0
        airport_tax = 650.0
        return base_fare + airport_tax + (distance_km * 5.5)


if __name__ == "__main__":
    journey_distance = 350.0  # 350 km intercity journey

    modes = [
        Bus("KSRTC Express"),
        Train("Vande Bharat Express"),
        Taxi("Ola Outstation Prime"),
        Flight("IndiGo Airlines")
    ]

    print(f"=== Multi-Modal Fare Comparison for {journey_distance:.0f} km Journey ===")
    for mode in modes:
        mode_name = type(mode).__name__
        fare = mode.calculate_fare(journey_distance)
        print(f"[{mode_name:<6}] {mode.service_provider:<25} -> Estimated Fare: Rs. {fare:,.2f}")
