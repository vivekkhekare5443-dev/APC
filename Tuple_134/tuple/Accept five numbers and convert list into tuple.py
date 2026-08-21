numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

result = tuple(numbers)

print("Tuple:", result)
