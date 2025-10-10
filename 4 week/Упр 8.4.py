a = input().split()
x = list(map(int, a))
b = input().split()
y = list(map(int, b))

s1 = set(x)
s2 = set(y)

unique1 = list()
unique2 = list()

for i in s1:
    u1 = x.count(i)
    if u1 == 1:
        unique1.append(i)

for i in s2:
    u2 = y.count(i)
    if u2 == 1:
        unique2.append(i)

print(
    "Уникальных элементов в списке 1:",
    unique1,
    " Уникальных элементов в списке 2:",
    unique2,
)

xy = x + y
s3 = set(xy)
unique3 = list()

for i in s3:
    u3 = xy.count(i)
    if u3 == 1:
        unique3.append(i)

print("Уникальных элементов в списке 1 и 2:", unique3)

u4 = s1 & s2
print("Элементов в списке и 1, и 2:", u4)
