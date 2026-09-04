def fibonacci(n):
    a, b = 0, 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter n: "))

print("Fibonacci =", fibonacci(n))