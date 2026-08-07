paragraph = input("Enter paragraph: ")
words = paragraph.split()
frequency = {}
for w in words:
    frequency[w] = frequency.get(w, 0) + 1
for w, count in frequency.items():
    print(f"{w}: {count}")