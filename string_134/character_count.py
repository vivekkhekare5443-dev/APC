s = input("Enter a string: ")
vowels = consonants = digits = spaces = special = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)