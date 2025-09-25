f = open("C:/MyPythonProjects/2 week/input.txt")
s = f.read()
p = s.split()
res = 0
r = ".!?"
for i in range(len(p)):
    if p[i][-1] in r:
        res += 1
print(res)
