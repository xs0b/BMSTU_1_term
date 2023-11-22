# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая ищет строку с наибольшим количеством нулей (Варинат № 5) 

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
# elif cols == 1 and rows == 1:
#     print("В матрице 1 элемент, считать что-либо бессмысленно")
else:
    # Поиск
    i_max = -1
    count_zero = 0
    max_count_zero = 0
    for i in range(rows):
        count_zero = 0
        for j in range(cols):
            if arr[i][j] == 0:
                count_zero += 1
        if count_zero >= max_count_zero:
            max_count_zero = count_zero
            i_max = i
    # Вывод искомой строки
    if max_count_zero == 0:
        print("Строки с нулями нет")
    else:
        print("Строка с наибольшим количеством нулей:", arr[i_max])