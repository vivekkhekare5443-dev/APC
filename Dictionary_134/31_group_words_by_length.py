words = ["apple", "cat", "dog", "banana", "bat"]
result = {}
for word in words:
    result.setdefault(len(word), []).append(word)
print(result)
