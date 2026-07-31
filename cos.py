x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

cos = 1
sign = -1
fact = 1
power = 1

for i in range(2, 2 * n, 2):
    power = power * x * x
    fact = fact * i * (i - 1)
    cos = cos + sign * (power / fact)
    sign = -sign

print("Cos(x) =", cos)
