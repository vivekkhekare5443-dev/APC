products = {"Pen": 20, "Book": 5, "Laptop": 10}
while True:
    print("\n1.Add 2.Update 3.Delete 4.Search 5.Low Stock 6.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        products[input("Enter name: ")] = int(input("Enter quantity: "))
    elif choice == 2:
        name = input("Enter name: ")
        if name in products: products[name] = int(input("Enter new quantity: "))
        else: print("Product not found")
    elif choice == 3:
        name = input("Enter name: ")
        if name in products: del products[name]
    elif choice == 4:
        name = input("Enter name: ")
        print(products.get(name, "Product not found"))
    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10: print(name, quantity)
    elif choice == 6:
        break
