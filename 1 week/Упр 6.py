with open("input.txt", "r") as f:
    lines = f.readlines()
    numbers = list(map(int, lines[0].split()))
    s = int(lines[2].strip())
    op = lines[1].strip()
    res1 = []
    D = 0
    for j in range (len(numbers)):
        for i in range(len(numbers[i])):
            D += int(numbers[j]) * (s ** (len(numbers[i]) - 1 - j))
        res1.append(D)
    
    if op == "+":
        res = 0
        for i in numbers:
            res += i
    elif op == "*":
        res = 1
        for i in numbers:
            res *= i
    else:
        res = 0
        for i in numbers:
            res -= i
    res2 = []
    for i in range(len(res)):
        while int(res[i]) != 0:
          res2.append(str(D % s))
          int(res[i]) = int(res[i]) // s
          
    print("".join(res2[::-1]))


    