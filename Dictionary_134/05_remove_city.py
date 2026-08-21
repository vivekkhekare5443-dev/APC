cities = {"Pune": 7000000, "Mumbai": 12000000, "Kolhapur": 600000}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found")
