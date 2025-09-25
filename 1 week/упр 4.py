with open("C:/MyPythonProjects/1 week/input1.txt", "r") as f:
    lines = f.readlines()
    numbers = list(map(int, lines[0].split()))
    op = lines[1].strip()
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
print(res)
