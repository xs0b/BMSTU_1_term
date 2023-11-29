# Джафаров Рустам. Группа ИУ7-16Б
# Программа, кторая из 2-х массивов формирует матрицу по формуле и определяет 
# среденее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического

from math import sin, isclose
d = []
f = []
d = [float(_) for _ in input("Введите список D через пробел: ").split()]
f = [float(_) for _ in input("Введите список F через пробел: ").split()]
while True: 
    if d == []:
        print("Список не может быть пустым")
        d = [float(_) for _ in input("Введите список D через пробел: ").split()]
    elif f == []:
        print("Список не может быть пустым")
        f = [float(_) for _ in input("Введите список F через пробел: ").split()]
    else:
        break
eps = 1e-7
rows = len(d)
cols = len(f)
a = [[0.0] * cols] * rows
for i in range(rows): # Заполнение матрицы
    for j in range(cols):
        a[i][j] = sin(d[i] + f[j])
av = [0] * rows
l = [0] * rows
for i in range(rows): # Поиск среднего арифмитического
    summ = 0
    for j in range(cols):
        if a[i][j] > 0:
            summ += a[i][j]
    if summ == 0:
        av[i] = None
    else:
        av[i] = summ/cols
for i in range(rows): # Поиск количества эл-ов, меньших среднего 
    count = 0         # арифмитическокого для данной строки
    for j in range(cols):
        if av[i] == None:
            l[i] = "Тут был None"
            continue
        if isclose(av[i], a[i][j]) or a[i][j] - av[i] > 0 :
            count += 1
        l[i] = count
for i in range(rows):
    print(*a[i], '\t', av[i], '\t', l[i])
