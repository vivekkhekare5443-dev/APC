marks = []

for i in range(20):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", average)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Students above average:", above)
print("Students below average:", below)
