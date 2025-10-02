import numpy as np

N = int(input())
M = int(input())

a = []

for i in range(M):
    b = list(map(int, input().split()))
    a.append(b)

a2 = np.delete(a, N, axis=1)

print(a2)
