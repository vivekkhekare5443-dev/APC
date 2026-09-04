def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")