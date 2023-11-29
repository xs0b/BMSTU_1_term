# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая счиатет интегралы числеными методами (правых прямоугольников
# и трапеций)

# Подключаем модули
from check_input import *
from math import * # Для пользовательских функций
from create_function import *
from table import *

# Ввод данных
start, stop, n1, n2 = map(str, input("Введите начало, конец отрезка, N1, N2: ").split())
mb_error = check(start, stop, n1, n2)

# Заставляем ввести занаво, если данные введены неверно
while True:
    if mb_error == False:
        print("Введенные параметры неправильные!")
        start, stop, n1, n2 = map(str, input("Введите начало, конец отрезка, N1, N2 снова: ").split())
        mb_error = check(start, stop, n1, n2)

    else:
        break
start, stop, n1, n2 = str_to_int_false(start, stop, n1, n2)
print()
# Начинаем считать 
sigma = F(stop) - F(start) # Эталонное значение 
# if start == stop:
#     print("Интеграл равен 0")
#     exit()
print(f"Эталонное значение интеграла: {sigma}")
print(sigma == 0)
X = [] # Создаем список х
for i in range(4):
    if i == 1 or i == 3:
        n = n1
    else:
        n = n2
    X.append(create_array_X(start, stop, n))
Y = [] # Создаем список значений
for i in range(4):
    Y.append(create_array_Y(X[i]))

# Метод правых пярмоугольников                                                                         
l_1_2 = create_l(X, Y)[:2] # Список итоговых значений интегралов 
# Метод трапеций
l_3_4 = create_l(X, Y)[2:] # Список итоговых значений интегралов 
table_sigma(l_1_2, l_3_4)
table_error(l_1_2, l_3_4, sigma)
num_min, num_max = accuracy(l_1_2, l_3_4, sigma)
eps = input("Введите точность: ")
flag = separate_check_float(eps)
while True:
    if flag == False:
        print("Точность введена неправильно ")
        eps = input("Введите точность: ")
    else:
        break
n = 1
eps = float(eps)
if num_max == 1 or num_max == 2:
    worst_metod = method_1
else:
    worst_metod = method_2
sigma_1 = worst_metod(start, stop, n)
sigma_2 = worst_metod(start, stop, 2*n)
while True:
    if abs(sigma_1 - sigma_2) <= eps:
        print(f'Количество участков разбиения = {n * 64}')
        print(f'Интеграл равен: {sigma + eps}')
        break
    n *= 2
    sigma_1 = sigma_2
    sigma_2 = worst_metod(start, stop, 2*n)