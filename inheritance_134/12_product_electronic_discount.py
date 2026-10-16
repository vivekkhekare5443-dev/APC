"""
Inheritance - Program 12:
Create a class Product with product ID, name, and price.
Derive ElectronicProduct with additional attributes such as brand and warranty.
Calculate the final price after applying a discount.
"""

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Base Price : Rs. {self.price:,.2f}")


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty_years = warranty_years

    def calculate_final_price(self, discount_percent):
        discount = (self.price * discount_percent) / 100
        return self.price - discount

    def display_details(self, discount_percent=10):
        print("=== Electronic Product Details ===")
        self.display_product()
        print(f"Brand      : {self.brand}")
        print(f"Warranty   : {self.warranty_years} year(s)")
        final_price = self.calculate_final_price(discount_percent)
        print(f"Discount   : {discount_percent}%")
        print(f"Final Price: Rs. {final_price:,.2f}")


if __name__ == "__main__":
    laptop = ElectronicProduct("EP-402", "UltraBook 15", 75000.0, "Dell", warranty_years=2)
    laptop.display_details(discount_percent=12)
