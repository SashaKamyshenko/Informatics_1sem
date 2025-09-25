s = input()
s0 = ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y", "1", "8"]
s1 = ["E", "J ", "S", "Z"]
s2 = ["3", "L", "2", "5"]

pal = True
mir = True

for i in range((len(s) + 1) // 2):
    if s[i] == s[-i - 1]:
        continue
    else:
        pal = False
        break

for i in range((len(s) + 1) // 2):
    if not mir:
        break
    if s[i] in s0:
        if s[-i - 1] != s0[s0.index(s[i])]:
            mir = False
    elif s[i] in s1:
        if s[-i - 1] != s2[s1.index(s[i])]:
            mir = False
    elif s[i] in s2:
        if s[-i - 1] != s1[s2.index(s[i])]:
            mir = False
    else:
        mir = False


if pal:
    if mir:
        print(f"{s} is a mirrored palindrome.")
    else:
        print(f"{s} is a regular palindrome.")
else:
    if mir:
        print(f"{s} is a mirrored string.")
    else:
        print(f"{s} is not a palindrome.")
