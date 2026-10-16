"""
Abstraction - Program 4:
Create an abstract class FoodOrder with abstract methods calculate_bill() and delivery_charge().
Derive RestaurantOrder and HomeDeliveryOrder and implement the methods appropriately.
"""

from abc import ABC, abstractmethod

class FoodOrder(ABC):
    def __init__(self, order_id, customer_name, items_cost):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items_cost = float(items_cost)

    @abstractmethod
    def calculate_bill(self):
        """Abstract method to calculate total bill."""
        pass

    @abstractmethod
    def delivery_charge(self):
        """Abstract method to calculate delivery charges."""
        pass

    def display_invoice(self):
        print(f"Order ID       : {self.order_id}")
        print(f"Customer       : {self.customer_name}")
        print(f"Items Cost     : Rs. {self.items_cost:,.2f}")
        print(f"Delivery Charge: Rs. {self.delivery_charge():,.2f}")
        print(f"Total Bill     : Rs. {self.calculate_bill():,.2f}")


class RestaurantOrder(FoodOrder):
    def __init__(self, order_id, customer_name, items_cost, table_no, service_charge_rate=5.0):
        super().__init__(order_id, customer_name, items_cost)
        self.table_no = table_no
        self.service_charge_rate = service_charge_rate

    def delivery_charge(self):
        # Dine-in orders have zero delivery charge
        return 0.0

    def calculate_bill(self):
        # Dine-in has 5% GST and optional service charge
        gst = 0.05 * self.items_cost
        service_charge = (self.service_charge_rate / 100) * self.items_cost
        return self.items_cost + gst + service_charge


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, order_id, customer_name, items_cost, distance_km):
        super().__init__(order_id, customer_name, items_cost)
        self.distance_km = distance_km

    def delivery_charge(self):
        # Rs. 30 base charge + Rs. 10 per km beyond 2 km
        if self.distance_km <= 2:
            return 30.0
        else:
            return 30.0 + ((self.distance_km - 2) * 10.0)

    def calculate_bill(self):
        gst = 0.05 * self.items_cost
        packaging_fee = 25.0
        return self.items_cost + gst + packaging_fee + self.delivery_charge()


if __name__ == "__main__":
    dine_in = RestaurantOrder("ORD-DINE-101", "Vikram Malhotra", items_cost=1800.0, table_no=7)
    takeaway = HomeDeliveryOrder("ORD-DELIV-202", "Pooja Hegde", items_cost=850.0, distance_km=5.5)

    print("=== Dine-In Restaurant Bill ===")
    dine_in.display_invoice()
    print(f"Table Number   : {dine_in.table_no}")

    print("\n=== Doorstep Home Delivery Bill ===")
    takeaway.display_invoice()
    print(f"Delivery Range : {takeaway.distance_km} km")
