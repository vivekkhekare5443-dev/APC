paragraph = input("Enter a paragraph: ")
result = {}
for word in paragraph.split():
    length = len(word)
    result[length] = result.get(length, 0) + 1
print(result)
