# Джафаров Рустам. Группа ИУ7-16Б
# Защита лр10

# Подключаем модули
from check_input import *
from math import *
from create_function import *
from table import *

def three_eights(start, end, n): # Метод 3/8
    if n % 3 != 0:
        print(f"Невозможно посчитать интеграл методом трёх восьмых, "
              f"т.к. количество точек разбиения {n} не кратно 3.")
        return "-"
    summa = 0
    delta = (end - start) / n
    x = start
    for i in range(0, n, 3):
        summa += f(x) + 3 * f(x + delta) + \
            3 * f(x + delta * 2) + f(x + delta * 3)
        x += delta * 3
    return (3 * delta / 8) * summa

def parabola(start, end, n): # Метод парабол
    if n % 2 != 0:
        print(f"Невозможно посчитать интеграл методом параболы, "
              f"т.к. количество точек разбиения {n} не кратно 2.")
        return "-"
    summa = 0
    delta = (end - start) / n
    x = start
    for i in range(0, n, 2):
        summa += f(x) + 4 * f(x + delta) + f(x + delta * 2)
        x += delta * 2
    return (delta / 3) * summa

# Ввод данных
start, stop, n1, n2 = map(str, input("Введите начало, конец отрезка, N1, N2: ").split())
mb_error = check(start, stop, n1, n2)

# Заставляем ввести занаво, если данные введены неверно
while True:
    if mb_error == False:
        start, stop, n1, n2 = map(str, input("Введите начало, конец отрезка, N1, N2 снова: ").split())
        mb_error = check(start, stop, n1, n2)
    else:
        break
start, stop, n1, n2 = str_to_int_false(start, stop, n1, n2)
print()
# Начинаем считать 
sigma = F(stop) - F(start) # Эталонное значение 
print(f"Эталонное значение интеграла: {sigma}")
print(parabola(start, stop, n2))