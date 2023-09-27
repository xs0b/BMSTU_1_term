# Джафаров Рустам Расимович. Группа ИУ7-16Б
# Программа для нахождения параметров треугольника и проверки принадлежности введеной точки треугольнику

# Подключаем модули
from math import * 

# Блок функций
def count_side(a1, a2, b1, b2):  # Функция подсчета стороны
    return sqrt(pow(a1-b1,2) + pow(a2-b2,2))

def count_side_with_min_angle(a1, a2, b1, b2, c1, c2):  # Функция подсчета косинуса с минимальным углом и сторон между, которыми он заключен
    side1 = count_side(a1, a2, b1, b2)
    side2 = count_side(b1, b2, c1, c2)
    side3 = count_side(a1, a2, c1, c2)
    cos1 = (pow(side1,2) + pow(side2,2) - pow(side3,2))/(2*side1*side2)  # Нахождение косинуса по теореме косинусов (15-17 строки)
    cos2 = (pow(side2,2) + pow(side3,2) - pow(side1,2))/(2*side3*side2)
    cos3 = (pow(side1,2) + pow(side3,2) - pow(side2,2))/(2*side1*side3)
    m, s1, s2 = cos1, side1, side2  # Нахождение сторон с минимальным углом (18-26 строки)
    if m < cos2: 
        m = cos2
        s1 = side2
        s2 = side3
    if m < cos3: 
        m = cos3
        s1 = side1
        s2 = side3
    return s1, s2

def area(x1, y1, x2, y2, x3, y3, x, y):  # Функция для нахождения площади теругольника
    s_abc = 0.5*abs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))
    s1 = 0.5*abs((x - x2)*(y3 - y2) - (x3 - x2)*(y - y2))
    s2 = 0.5*abs((x1 - x)*(y - y2) - (x - x2)*(y1 - y))
    s3 = 0.5*abs((x1 - x3)*(y - y3) - (x - x3)*(y1 - y3))
    if s1 + s2 + s3 == s_abc: 
        dot_in = "Точка внутри треугольника"
        c = 1
    else: 
        dot_in  = "Точка вне треугольника" 
        c = 2
    return dot_in, c

def equation_line(a1, b1, a2, b2):  # Функция для нахождения уравнения прямой
    A = b2 - b1
    B = (-1)*a2 + a1
    C = a2*b1 - a1*b2
    return A, B, C

# Блок ввода
x1, y1 = map(int, input("Введите координаты точки A(x, y): ").split())
x2, y2 = map(int, input("Введите координаты точки B(x, y): ").split())
x3, y3 = map(int, input("Введите координаты точки C(x, y): ").split())
xm, ym = map(int, input("Введите координаты точки, положение которой вы хотели бы проверить: ").split())

# Блок решения
eps = 1e-25
side1, side2 = count_side_with_min_angle(x1, y1, x2, y2, x3, y3)
side_ab = count_side(x1, y1, x2, y2)
side_bc = count_side(x2, y2, x3, y3)
side_ac = count_side(x1, y1, x3, y3)
# Проверка на существование треугольника (60 строка)
if abs(side_ab + side_bc - side_ac) > eps or \
    abs(side_ab + side_ac - side_bc) > eps or abs(side_bc + side_ac - side_ab) > eps:
    side1, side2 = count_side_with_min_angle(x1, y1, x2, y2, x3, y3)
    if side_ab == side1 and side_bc == side2 or side_bc == side1 and side_ab == side2: 
        side3 = side_ac
    if side_ac == side1 and side_ab == side2 or side_ab == side1 and side_ac == side2: 
        side3 = side_bc
    if side_bc == side1 and side_ac == side2 or side_ac == side1 and side_bc == side2: 
        side3 = side_ab
    bisector = sqrt(side1*side2*(side1 + side2 + side3)*(side1 + side2 - side3))/(side1 + side2)
    if side_ab == side_bc or side_ab == side_ac or side_bc == side_ac:
        isosceles_y_or_n = "Треугольник равнобедренный"
    else:
        isosceles_y_or_n = "Треугольник неравнобедренный"
    print(f"Сторона AB: {side_ab:.7g}",
        f"Сторона ВС: {side_bc:.7g}",
        f"Сторона АС: {side_ac:.7g}",
        f"Биссектриса проведенная из меньшего угла равна: {bisector:.7g}",
        isosceles_y_or_n,
        sep="\n")
    A1, B1, C1 = equation_line(x1, y1, x2, y2)
    A2, B2, C2 = equation_line(x2, y2, x3, y3)
    A3, B3, C3 = equation_line(x3, y3, x1, y1)
    info_dot, k =  area(x1, y1, x2, y2, x3, y3, xm, ym)
    if k == 1:
        print(1)
        print(info_dot)
        distance1 = abs(A1*xm + B1*ym + C1)/sqrt(pow(A1, 2) + pow(B1,2))  # Считаем расстояние (105-107 строки)
        distance2 = abs(A2*xm + B2*ym + C2)/sqrt(pow(A2, 2) + pow(B2,2))
        distance3 = abs(A3*xm + B3*ym + C3)/sqrt(pow(A3, 2) + pow(B3,2))
        distance_min = distance1
        if distance2 < distance_min:
            distance_min = distance2
        if distance3 < distance_min:
            distance_min = distance3
        print(f"Расстояние до меньшей стороны: {distance_min:.7g}")
    if k == 2:
        print(info_dot) 
else:
    print("Треугольника с такими параметрами не существует")
    exit(-1)