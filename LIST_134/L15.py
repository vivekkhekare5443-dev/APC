numbers = list(map(int, input("Enter list elements: ").split()))

numbers = list(set(numbers))  # Remove duplicates

numbers.sort()

print("Second Largest Element:", numbers[-2])
