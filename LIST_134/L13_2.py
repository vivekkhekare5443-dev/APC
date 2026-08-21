numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort(reverse=True)

print("Descending Order:", numbers)
