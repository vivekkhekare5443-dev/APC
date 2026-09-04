def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(float, input("Enter numbers: ").split()))

print("Average =", average(numbers))