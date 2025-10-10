import string

with open("C:/MyPythonProjects/4 week/license.txt", "r") as f:
    t = f.read()
t2 = t.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
w = t2.lower().split()

d = {}
for a in w:
    if a not in d.keys():
        d[a] = 1
    else:
        d[a] = d[a] + 1

# for k in d.keys:

f = 0
while f < 10:
    for k in d.keys():
        if d[k] == max(d.values()):
            print(k, d[k])
            d[k] = 0
            f += 1
        if f == 10:
            break
