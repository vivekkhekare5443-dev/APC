numbers = input("Enter list elements: ").split()

for item in numbers:
    print(item, "appears", numbers.count(item), "time(s)")
