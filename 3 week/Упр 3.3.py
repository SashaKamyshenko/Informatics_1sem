def e(a, b):

    x, y, z, f = 1, 0, 0, 1
    while b != 0:
        c = a // b
        a, b = b, a % b
        x, y = y, x - y * c
        z, f = f, z - f * c
    return (a, x, z)


print(e(int(input()), int(input())))
