N = int(input())
while N != 1:
    c = 2
    for i in range(N):
        if N % c == 0:
            N = N / c
            print(c)
        else:
            c += 1
