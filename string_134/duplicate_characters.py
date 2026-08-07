s = input("Enter a string: ")
seen = {}
for ch in s:
    seen[ch] = seen.get(ch, 0) + 1
result = ''
for ch in s:
    if seen[ch] > 1 and ch not in result:
        result += ch
print(result if result else "No duplicate characters")