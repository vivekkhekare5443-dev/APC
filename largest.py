a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))

if a >= b and a >= c :
    print("Largest Number is:",a)
elif b >= a and b >= c:
    print("Largest Number is:",b)
else:
    print("Largest Number is:",c)
