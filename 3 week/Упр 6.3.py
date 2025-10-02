a = input().split()
x = list(map(int, a))
c = input().split()
y = list(map(int, c))

x1 = sum(x) / len(x)
y1 = sum(y) / len(y)

x2 = sum([i**2 for i in x]) / len(x)
a = 0

for i in range(len(x)):
    a = a + x[i] * y[i]

xy = a / len(x)

b = (xy - x1 * y1) / (x2 - x1 * x1)
k = y1 - b * x1

print(k, b)
