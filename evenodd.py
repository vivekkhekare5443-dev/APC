n = int(input("Enter n: "))

print("Even numbers:")
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

print("Odd numbers:")
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1