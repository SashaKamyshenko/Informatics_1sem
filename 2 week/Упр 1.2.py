c = int(input())
A = [0] * (c - 1)
for i in range(len(A)):
    A[i] = int(input())

B = 0
for i in range(len(A)):
    B += int(A[i])
D = ((1 + c) / 2) * c

print(D - B)
