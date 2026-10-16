"""
Polymorphism - Program 11 (Operator Overloading: __eq__ and __gt__):
Create a class Product with product name and price.
Overload the == and > operators to compare two products based on their prices.
"""

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = float(price)

    def __eq__(self, other):
        """Overload '==' operator to compare product prices."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __gt__(self, other):
        """Overload '>' operator to compare product prices."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __str__(self):
        return f"{self.product_name} (Rs. {self.price:,.2f})"


if __name__ == "__main__":
    laptop = Product("Dell Inspiron 15", 55000.0)
    gaming_pc = Product("ASUS ROG Strix", 95000.0)
    workstation = Product("HP Pavilion Plus", 55000.0)

    print("=== Operator Overloading (== and > for Product Price Comparison) ===")
    print(f"Product 1 : {laptop}")
    print(f"Product 2 : {gaming_pc}")
    print(f"Product 3 : {workstation}")
    print("-" * 60)

    # Testing == operator
    if laptop == workstation:
        print(f"EQUALITY CHECK: '{laptop.product_name}' and '{workstation.product_name}' have the SAME price.")
    else:
        print(f"EQUALITY CHECK: Prices are different.")

    # Testing > operator
    if gaming_pc > laptop:
        print(f"GREATER-THAN CHECK: '{gaming_pc.product_name}' is MORE expensive than '{laptop.product_name}'.")
    else:
        print(f"GREATER-THAN CHECK: '{gaming_pc.product_name}' is not more expensive.")
