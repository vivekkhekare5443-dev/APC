numbers = {10, 20, 30, 40, 50}
num = int(input("Enter number to remove: "))
if num in numbers:
    numbers.remove(num)
    print(numbers)
else:
    print("Number not found")
