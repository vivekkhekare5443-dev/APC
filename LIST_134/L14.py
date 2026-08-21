numbers = [10, 20, 30, 20, 40, 10, 50, 30]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Unique Elements:", unique)
