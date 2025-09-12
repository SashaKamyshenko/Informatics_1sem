N, b, c = input(), int(input()), int(input())
D = 0
for i in range(len(N)):
    D += int(N[i]) * (b ** (len(N) - 1 - i))
res = ""
while D != 0:
    res.append(D % c)
    D = D // c

print("".join(res[::-1]))
