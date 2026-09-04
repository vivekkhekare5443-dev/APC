def calculate(numbers):
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average

numbers = list(map(int, input("Enter numbers: ").split()))

minimum, maximum, total, average = calculate(numbers)

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", average)