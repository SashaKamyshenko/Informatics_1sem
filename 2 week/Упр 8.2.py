a = input().split()
b = list(map(int, a))
c = (len(b)) // 2
for i in range(len(b)):
    n = 0
    for j in range(len(b)):
        if b[i] > b[j]:
            n += 1
    if n == c:
        print(b[i])
        break
