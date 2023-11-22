# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая менеят строки c наибольшим и наименьшим кол-вом отрицательных 

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
elif cols < 1 and rows < 1:
    print("Cчитать что-либо бессмысленно")
else:
    # Меняем местами строки
    i_min = 0
    i_max = 0
    count_negative = 0
    max_count_negative = 0
    min_count_negative = len(arr[0])
    for i in range(rows):
        count_negative = 0
        for j in range(cols):
            if arr[i][j] < 0:
                count_negative += 1
        # print(count_negative)
        if (count_negative <= min_count_negative) and count_negative != 0: 
            i_min = i
            min_count_negative = count_negative
            # print(i_min, 'asdas')
        if (count_negative >= max_count_negative) and count_negative != 0:
            i_max = i
            # print(i_max, "+")
            max_count_negative = count_negative
    # Вывод измененной матрицы
    if i_max == i_min:
        pass
    else:
        arr[i_min], arr[i_max] = arr[i_max], arr[i_min]
    print("Обновленная матрица:")
    for i in range(rows):
        print(arr[i])
