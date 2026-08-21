# Accept 10 numbers from the user
numbers = []

for i in range(10):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)

# Calculate sum
total = 0
for num in numbers:
    total += num

# Calculate average
average = total / len(numbers)

# Display results
print("\nNumbers entered:", numbers)
print("Sum =", total)
print("Average =", average)
