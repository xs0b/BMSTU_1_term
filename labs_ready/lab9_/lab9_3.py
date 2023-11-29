# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая подсчитывает в каждой строке матрицы D количество элементов, 
# превышающих суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G

cols_d = int(input("Введите количество столбцов матрицы D: "))
rows_d = int(input("Введите количество строк матрицы D: "))
cols_z = int(input("Введите количество столбцов матрицы Z: "))
rows_z = int(input("Введите количество строк матрицы Z: "))
while True: 
    if cols_d <= 0:
        print("Количество столбцов не может быть меньше нуля")
        cols_d = int(input("Введите количество столбцов матрицы D: "))
    elif rows_d<= 0:
        print("Количество строк не может быть меньше нуля")
        rows_d = int(input("Введите количество строк матрицы D: "))
    elif cols_z <= 0:
        print("Количество столбцов не может быть меньше нуля")
        cols_z = int(input("Введите количество столбцов матрицы Z: "))
    elif rows_z<= 0:
        print("Количество строк не может быть меньше нуля")
        rows_z = int(input("Введите количество строк матрицы Z: "))
    else:
        break
d = [list(map(float, input(f"Введите {i + 1} строчку матрицы D: ").split())) for i in range(rows_d)]
z = [list(map(float, input(f"Введите {i + 1} строчку матрицы Z: ").split())) for i in range(rows_z)]
g = []
if rows_d == rows_z:
    for i in range(rows_d):
        count = 0
        for j in range(cols_d):
            if d[i][j] > sum(z[i]):
                count += 1
        g.append(count) # Размещаем искомые кол-ва в списке g
    error = "Был полностью пройден список D" 
elif rows_d > rows_z:
    for i in range(rows_z):
        count = 0
        for j in range(cols_z):
            if d[i][j] > sum(z[i]):
                count += 1
        g.append(count) # Размещаем искомые кол-ва в списке g  
        error = "Был не полностью пройден список D" 
else:
    for i in range(rows_z):
        count = 0
        for j in range(cols_z):
            if d[i][j] > sum(z[i]):
                count += 1
        g.append(count) # Размещаем искомые кол-ва в списке g  
        error = "Был не полностью пройден список Z" 
max_g = max(g) # Поиск максимального эелмента в массиве g
print("Матрица Z")
for i in range(rows_z):
    print(*z[i])
print("Матрица D до изменения")
for i in range(rows_z):
    print(*d[i])
for i in range(rows_d): # Умножение матрицы D на число
    for j in range(cols_d):
        d[i][j] *= max_g
print("Матрица D после изменения")
for i in range(rows_z):
    print(*d[i])
print("Список G:", *g)
print(error)

