# Джафаров Рустам Расимович. Группа ИУ7-16Б. Вариант № 28
# Программа для построения вывода таблицы графиков: t1 = x - 0.5 ** x, 
# t2 = x ** 3 - 4.49*x ** 2 - 24.5*x + 19.5. А также постороени графика t1 на 
# на некотором заданном пользователем отрезке, используя только цикл for.

# Подключаем модули
from math import isclose, inf

# Блок ввода
x0 = float(input("Введите начальное значение x0: "))
xn = float(input("Введите конечное значение xn: "))
h = float(input("Введите шаг h: "))
print("Если вы ввели очень маленький диапозон х, то график будет просто \
константой")

# Проверка на корректоность ввода данных
for op in range(99):
    if x0 >= xn:
        print("Начало или конец аргумента введены неправильно")
        x0 = float(input("Введите начальное значение x0: "))
        xn = float(input("Введите конечное значение xn: "))
    elif h <= 0:
        print("Шаг не может быть отрицательным или 0")
        h = float(input("Введите шаг h: "))
    elif xn - x0 < h:
        print("Шаг не может быть больше разницы xn - x0")
        h = float(input("Введите шаг h: "))
    else:
        break

# Счиатем значения функций и выводим их в таблицу # ИСПРАВИТЬ ТАБЛИЧКУ 
x = x0
t1_max = -inf
t1_min = +inf
t2_min = +inf
t2_max = -inf
counter = int((xn - x0)/h) + 1
print("-" * 46)
print(f"| {'x':^12} | {'t1':^12} | {'t2':^12} |")
print("-" * 46)
for i in range(counter):
    t1 = x - 0.5 ** x 
    t2 = x ** 3 - 4.49*x ** 2 - 24.5*x + 19.5
    if isclose(t1, t1_min) or t1 < t1_min:
        t1_min = t1 
    if isclose(t1, t1_max) or t1 > t1_max:
        t1_max = t1 
    if isclose(t2, t2_min) or t2 < t2_min:
        t2_min = t2 
    if isclose(t2, t2_max) or t2 > t2_max:
        t2_max = t2
    if abs(x) < 1e-9:
        x == 0.0
    print(f"| {x:^12.5g} | {t1:^12.5g} | {t2:^12.5g} |")    
    x += h
print("-" * 46)
print()

# Построение графика
serif = int(input("Введите количество засечек (от 4 до 8): "))
# Проверка на правильность введеного количества засечек
for i in range(99):
    if serif < 4 or serif > 8:
        print("Количество засчек строго от 4 до 8")
        serif = int(input("Введите количество засечек (от 4 до 8): "))
    else:
        break

t = t2_min
# Паметры осей и графика в целом 
length = 200                                       # Длинна оси ОY
dist_serif = round((length - 8*serif)/(serif - 1)) # Расстояние между засчеками
delta = (t2_max - t2_min)/(serif - 1)              # Разница между двумя засечками
OY_read = " " * 9

for i in range(serif):
    if i == serif - 1:
        OY_read += f"{t: >8.5g}"
    elif i == serif - 2:
        OY_read += f"{t: <8.5g}" + " " * dist_serif
    else:
        OY_read += f"{t: <8.5g}" + " " * dist_serif
    t += delta
print(OY_read)
scale_graph = abs(t2_max - t2_min)/(length)

# Постороение графика t2
x = x0
#c = 0
for i in range(counter):
    if abs(x) < 1e-14:
        print(f"{0:^8.5g}|", end="")
    else:
        print(f"{x:^8.5g}|", end="")
    string = ""
    t2 = -(x ** 3 - 4.49*x ** 2 - 24.5*x + 19.5)
    # if float(f"{x:.5g}") == int(float(f"{x:.5g}")) or abs(x) < 1e-14:
    #     string = "~"*length
    #     x += h
    #     print(string)
    #     continue
    # else:
    for j in range(length+1):
        if scale_graph*j <= t2 - t2_min < scale_graph*(j + 1):
            string += "*"
        elif j == int(abs(t2_min)/scale_graph) and t2_min < 0: 
            string += "|"
        else:
            string += " "
    print(string)
    x += h

# Блок вывода
print("Минимальное зачнеие графика t1: ", f"{t1_min:.5g}",
"Минимальное зачнеие графика t2: ", f"{t2_min:.5g}",
sep='\n')