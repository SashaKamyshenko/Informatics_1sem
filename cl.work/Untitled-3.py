n, m = map(int, input("Введите количество строк и столбцов: ").split())
matrix = []

print("Введите матрицу построчно:")
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Полученная матрица:")
print(matrix)
