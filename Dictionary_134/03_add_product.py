products = {"Laptop": 50000, "Mobile": 20000, "Keyboard": 1500, "Mouse": 800, "Headphones": 2000}
name = input("Enter new product name: ")
price = float(input("Enter price: "))
products[name] = price
print(products)
