n = int(input("Enter number"))
limit =n*n
term=1
for i in range (limit):
    if term > limit:
        break
    else:
        print(term,end= " ")
        term*=2
