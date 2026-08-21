temperatures = []

for i in range(10):
    temp = float(input(f"Enter temperature of day {i+1}: "))
    temperatures.append(temp)

average = sum(temperatures) / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest Day Temperature:", max(temperatures))
print("Coldest Day Temperature:", min(temperatures))
print("Average Temperature:", average)
print("Days above average:", above)
print("Days below average:", below)
