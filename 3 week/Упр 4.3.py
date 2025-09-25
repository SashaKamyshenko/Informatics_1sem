def t(size, symb):
    for i in range((size + 1) // 2 + 1):
        print(symb * i)
    for i in range((size + 1) // 2, size + 1):
        print(symb * (size - i))


print(t(int(input()), input()))
