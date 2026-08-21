A = []
B = []
C = []

print("Enter elements of Matrix A")
for i in range(3):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements of Matrix B")
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Sum of Matrices:")
for row in C:
    print(row)
