# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая меняет местами столбцы с минимальной и максимальной суммой
# элементов

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

if cols == 0 or rows == 0:
    print("Матрица пустая, считать что-либо бессмысленно")
elif cols < 1:
    print("Считать что-либо бессмысленно")
else: 
    # Меняем местами
    arr = list(zip(*arr))
    # for i in range(rows):
    #   for j in range(len(arr[0])):
    #       if i != j and i < j:
    #           arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    min_sum = +inf
    i_min = -1
    max_sum = -inf
    i_max = -1
    for i in range(cols):
        sum_now = 0
        for j in range(rows):
            sum_now += arr[i][j]
        if sum_now <= min_sum:
            min_sum = sum_now
            i_min = i
        if sum_now >= max_sum:
            max_sum = sum_now
            i_max = i
        # print(sum_now)
    arr[i_min], arr[i_max] = arr[i_max], arr[i_min]
    arr = list(zip(*arr))
    arr = [list(ele) for ele in arr]
    print("Измененная матрица:")
    for i in range(rows):
        print(arr[i])