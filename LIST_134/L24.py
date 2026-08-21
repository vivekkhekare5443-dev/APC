numbers = input("Enter list elements: ").split()

left = numbers[1:] + numbers[:1]

print("Left Rotation:", left)
