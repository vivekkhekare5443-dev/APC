numbers = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(numbers):
    required = target - num
    if required in seen:
        print("Numbers:", required, num)
        break
    seen[num] = i
