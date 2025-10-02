def factor(n):
    if n <= 1:
        return 1
    return n*factor(n-1)
print(factor(int(input())))