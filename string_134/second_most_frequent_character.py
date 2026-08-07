s = input("Enter a string: ")
frequency = {}
for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1
pairs = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
if len(pairs) > 1:
    print("Second most frequent character:", pairs[1][0])
else:
    print("No second most frequent character")