numbers = input("Enter list elements: ").split()

unique = []

for item in numbers:
    if item not in unique:
        unique.append(item)

print("List after removing duplicates:", unique)
