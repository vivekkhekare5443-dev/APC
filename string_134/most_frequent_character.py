s = input("Enter a string: ")
frequency = {}
for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1
most = None
for ch, count in frequency.items():
    if most is None or count > frequency[most]:
        most = ch
print("Most frequent character:", most)