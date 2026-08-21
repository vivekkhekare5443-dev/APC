scores = []

for i in range(10):
    score = int(input(f"Enter score in match {i+1}: "))
    scores.append(score)

total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
