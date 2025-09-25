with open("input.txt", "r") as f:
    s = f.readlines()
    p = s.split()
    n = 0
    r = ["." "!" "?"]
    for i in range(len(p)):
        if p[i] in r:
            n += 1

print(n)
