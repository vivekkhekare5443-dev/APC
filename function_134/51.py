products = [
    ("Laptop", 50000, 1),
    ("Mouse", 800, 2),
    ("Keyboard", 1500, 2),
    ("Monitor", 12000, 1)
]


def total_value(product):
    return product[1] * product[2]


# a) Calculate total value
values = list(
    map(lambda p: (p[0], total_value(p)), products)
)

# b) Products costing more than ₹1000
filtered = list(
    filter(lambda p: p[1] > 1000, products)
)

# c) Sort according to total value
sorted_products = sorted(
    products,
    key=lambda p: total_value(p)
)

print("Total value of each product:")
print(values)

print("\nProducts costing more than ₹1,000:")
print(filtered)

print("\nProducts sorted according to total value:")
for p in sorted_products:
    print(p, "Total =", total_value(p))