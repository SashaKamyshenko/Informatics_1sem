a = input().split()
b = list(map(int, a))
c = len(b)
f = int(c)
d = 1
for i in range(c):
    d *= b[i]

print(d ** (1 / f))
