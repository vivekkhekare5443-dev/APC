tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple1 + tuple2

result = tuple(set(merged))

print("Tuple after removing duplicates:", result)
