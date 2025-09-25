a = input().split()
b = list(map(int, a))
c = 1
for i in range(len(b)):
    if c < b.count(i):
        c = b.count(i)
        d = i

print(d)
