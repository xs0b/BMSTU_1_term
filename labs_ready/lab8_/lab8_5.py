# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая ищет максимальный элемент в квадратной матрице над
# главной диагональю и минимальное под побочной

from math import inf
cols = int(input("Введите количество столбцов: "))
rows = int(input("Введите количество строк: "))
variant = int(input("Как вы хотите вводить матрицу (1 - построчно, 2 - поэлементно)? "))
# Проверка на корректность ввода
while True: 
    if cols < 0:
        print("Количество столбцов не может быть меньше нуля")
        cols = int(input("Введите количество столбцов: "))
    elif rows < 0:
        print("Количество строк не может быть меньше нуля")
        rows = int(input("Введите количество строк: "))
    elif variant != 1 and variant != 2:
        print("Способ ввода может быть только 1 или 2")
        variant = int(input("Как вы хотите вводить матрицу (1 - построчно, 2 - поэлементно)? "))
    else:
        break

# Инициализирую матрицу
arr = [[0 for _ in range(cols)] for _ in range(rows)]
# Заполнение списка
z = 1 
if variant == 1:
    arr = [list(map(int, input(f"Введите {i + 1} строчку: ").split())) for i in range(rows)]
if variant == 2:
    for i in range(cols):
        for j in range(rows):
            a = int(input(f"Введите элементы {i + 1} строки под номером в матрице {z}: "))
            arr[i][j] = a
            z += 1
print("Введенная вами матрица: ")
for i in range(rows):
    print(arr[i])
# Считаем
if cols == 0 or rows == 0:
    print("Матрица пустая, считать что-либо бессмысленно")
elif cols == 1 and rows == 1:
    print("В матрице 1 элемент, считать что-либо бессмысленно")
else:
    max_arr = -inf
    min_arr = +inf
    for i in range(rows):
        for j in range(cols):
            if i < j and arr[i][j] >= max_arr:
                max_arr = arr[i][j]
            if i + j > rows - 1 and arr[i][j] <= min_arr:
                min_arr = arr[i][j]
print(f"Максимальный элемент над главной равен: {max_arr}",
      f"Минимальный элемент под побочной равен: {min_arr}",
      sep='\n')