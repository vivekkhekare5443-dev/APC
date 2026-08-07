s = input("Enter main string: ")
sub = input("Enter substring: ")
found = False
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        found = True
        break
print("Substring exists" if found else "Substring does not exist")