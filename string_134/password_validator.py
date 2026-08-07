password = input("Enter a password: ")
length = uppercase = lowercase = digit = special = 0
for ch in password:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
length = len(password)
if length >= 8 and uppercase and lowercase and digit and special:
    print("Valid password")
else:
    print("Invalid password")