def unique_elements(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result

items = input("Enter elements: ").split()

print("Unique elements =", unique_elements(items))