def count_occurrences(items, element):
    count = 0

    for item in items:
        if item == element:
            count += 1

    return count

items = input("Enter elements: ").split()
element = input("Enter element to search: ")

print("Occurrences =", count_occurrences(items, element))