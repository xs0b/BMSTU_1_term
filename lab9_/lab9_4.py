# Джафаров Рустам. Группа ИУ7-16Б
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение

cols_d = int(input("Введите количество столбцов матрицы D: "))
rows_d = int(input("Введите количество строк матрицы D: "))
while True: 
    if cols_d <= 0:
        print("Количество столбцов не может быть меньше нуля")
        cols_d = int(input("Введите количество столбцов: "))
    elif rows_d<= 0:
        print("Количество строк не может быть меньше нуля")
        rows_d = int(input("Введите количество строк: "))
    else:
        break
d = [list(map(float, input(f"Введите {i + 1} строчку матрицы D: ").split())) for i in range(rows_d)]
i = [int(_) for _ in input("Введите список I: ").split()]
r = []
for _ in i:
    r.append(max(d[_ - 1]))
print("Матрица D:")
for _ in range(rows_d):
    print(d[_])
print("Список I, R соответственно:", i, r, sep='\n')
print("Среднее арифметичесоке равно: ", sum(r)/len(r))
