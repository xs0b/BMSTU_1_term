# Джафаров Рустам. Группа ИУ7-16Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.

cols, rows = map(int, input("Введите размерность матриц A и B: ").split())
while True: 
    if cols <= 0:
        print("Количество столбцов не может быть меньше нуля")
        cols = int(input("Введите количество столбцов: "))
    elif rows <= 0:
        print("Количество строк не может быть меньше нуля")
        rows = int(input("Введите количество строк: "))
    else:
        break
a = [list(map(float, input(f"Введите {i + 1} строчку матрицы D: ").split())) for i in range(rows)]
b = [list(map(float, input(f"Введите {i + 1} строчку матрицы Z: ").split())) for i in range(rows)]
c = [[0.0] * cols] * rows
for i in range(rows):
    for j in range(cols):
        c[i][j] = a[i][j] * b[i][j]
c = list(zip(*c))
v = []
for i in range(cols):
    v.append(sum(c[i]))
c = list(zip(*c))
c = [list(ele) for ele in c]
print("Матрица A:")
for _ in range(rows):
    print(a[_])
print("Матрица B:")
for _ in range(rows):
    print(b[_])
print("Матрица C:")
for _ in range(rows):
    print(c[_])
print("Список V:", v)
