message = input("Enter message: ")
shift = int(input("Enter shift: "))
mode = input("Encrypt or decrypt (E/D): ").strip().upper()
result = ''
for ch in message:
    if ch.isalpha():
        base = 'A' if ch.isupper() else 'a'
        offset = ord(ch) - ord(base)
        if mode == 'E':
            offset = (offset + shift) % 26
        else:
            offset = (offset - shift) % 26
        result += chr(ord(base) + offset)
    else:
        result += ch
print(result)