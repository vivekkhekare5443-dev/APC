import math

n = int(input("Enter a number: "))
root = int(math.sqrt(n))

if root * root != n:
    print("Square root is not an integer.")
else:
    prime = True
    if root < 2:
        prime = False
    else:
        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

    if prime:
        print(root, "is Prime")
    else:
        print(root, "is Not Prime")
