"""
Inheritance - Program 2:
Create a base class Vehicle with attributes brand and model.
Create a derived class Car with additional attributes fuel_type and price.
Define methods to display vehicle details and calculate the discounted price of the car.
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_details(self):
        super().display_details()
        print(f"Fuel Type      : {self.fuel_type}")
        print(f"Original Price : Rs. {self.price:,.2f}")

    def calculate_discounted_price(self, discount_percent):
        discount_amount = (self.price * discount_percent) / 100
        final_price = self.price - discount_amount
        return final_price, discount_amount


if __name__ == "__main__":
    my_car = Car("Hyundai", "Creta SX", "Petrol", 1450000)
    print("--- Vehicle Details ---")
    my_car.display_details()

    discount_rate = 8.5  # 8.5% festival discount
    final_price, discount_val = my_car.calculate_discounted_price(discount_rate)
    print(f"\nFestival Discount ({discount_rate}%) : Rs. {discount_val:,.2f}")
    print(f"Final Discounted Price           : Rs. {final_price:,.2f}")
