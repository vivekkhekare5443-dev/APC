text = input("Enter a string: ")
seen = set()
for char in text:
    if char in seen:
        print("First repeating character:", char)
        break
    seen.add(char)
