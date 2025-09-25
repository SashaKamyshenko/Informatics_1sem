a = input().split()
b = list(map(int, a))
for i in range(len(b) + 1):
    c = b.count(i)
    if c == 1:
        print(i)
