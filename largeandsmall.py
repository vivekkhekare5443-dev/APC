n = int(input("How many numbers? "))
i = 1
num = int(input("Enter number: "))
largest = smallest = num
while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    i += 1
print("Largest =", largest)
print("Smallest =", smallest)