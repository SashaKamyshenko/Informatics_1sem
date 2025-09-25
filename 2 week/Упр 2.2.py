G, s = input().split()
G = int(G)
n = len(s) // G
res = ""
for i in range(0, len(s), n):
    res += s[i : i + n][::-1]
print(res)
