s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter replacement character: ")
result = ''
for ch in s:
    result += new if ch == old else ch
print(result)