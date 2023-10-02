# Джафаров Рустам Расимович. Группа ИУ7-16Б
# Нахождения параметров треугольника
# Проверка принадлежности точки треугольнику

# Подключаем модули
from math import * 

# Подсчет стороны
def count_side(a1, a2, b1, b2):  
    return sqrt(pow(a1-b1,2) + pow(a2-b2,2))

# Подсчет косинуса с минимальным углом и сторон, между которыми он заключен
def count_side_with_min_angle(a1, a2, b1, b2, c1, c2): 
    side1 = count_side(a1, a2, b1, b2)
    side2 = count_side(b1, b2, c1, c2)
    side3 = count_side(a1, a2, c1, c2)
    # Используя теорему косинусов находит косинус соответствующего угла
    cos1 = (pow(side1,2) + pow(side2,2) - pow(side3,2))/(2*side1*side2) 
    cos2 = (pow(side2,2) + pow(side3,2) - pow(side1,2))/(2*side3*side2)
    cos3 = (pow(side1,2) + pow(side3,2) - pow(side2,2))/(2*side1*side3)
    m, s1, s2 = cos1, side1, side2  \
    # Нахождение сторон с минимальным углом
    if isclose(m, cos2) or m < cos2: 
        m = cos2
        s1 = side2
        s2 = side3
    if isclose(m, cos3) or m < cos3: 
        m = cos3
        s1 = side1
        s2 = side3
    return s1, s2

# Функция для нахождения площади теругольника
def area(x1, y1, x2, y2, x3, y3, x, y): 
    # Используем формулу расчета площади по координатам трех вершин
    s_abc = 0.5*abs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))
    s1 = 0.5*abs((x - x2)*(y3 - y2) - (x3 - x2)*(y - y2))
    s2 = 0.5*abs((x1 - x)*(y - y2) - (x - x2)*(y1 - y))
    s3 = 0.5*abs((x1 - x3)*(y - y3) - (x - x3)*(y1 - y3))
    # Проверка точки
    if isclose(s1 + s2 + s3, s_abc): 
        dot_in = "Точка внутри треугольника"
        c = 1
    else: 
        dot_in  = "Точка вне треугольника" 
        c = 2
    return dot_in, c

# Функция для нахождения уравнения прямой
def equation_line(a1, b1, a2, b2): 
    # Находим коэффиценты прямой заданой двумя точками
    A = b2 - b1
    B = (-1)*a2 + a1
    C = a2*b1 - a1*b2
    return A, B, C

# Ввода координат вершин треугольника и точки
x1, y1 = map(int, input("Введите координаты точки A(x, y): ").split())
x2, y2 = map(int, input("Введите координаты точки B(x, y): ").split())
x3, y3 = map(int, input("Введите координаты точки C(x, y): ").split())
xm, ym = map(int, input("Введите координаты точки, \
положение которой вы хотели бы проверить: ").split())

# Блок решения
side_ab = count_side(x1, y1, x2, y2)
side_bc = count_side(x2, y2, x3, y3)
side_ac = count_side(x1, y1, x3, y3)
# Проверква на существование треугольника
if x1 == x2 == x3 or y1 == y2 == y3 or x1 - y1 == x2 - y2 == x3 - y3: 
    print("Треугольника с такими параметрами не существует")
    exit()
side1, side2 = count_side_with_min_angle(x1, y1, x2, y2, x3, y3)
if isclose(side_ab, side1) and isclose(side_bc, side2) or \
isclose(side_bc, side1) and isclose(side_ab, side2): 
    side3 = side_ac
if isclose(side_ac, side1) and isclose(side_ab, side2) or \
isclose(side_ab, side1) and isclose(side_ac, side2): 
    side3 = side_bc
if isclose(side_bc, side1) and isclose(side_ac, side2) or \
isclose(side_ac, side1) and isclose(side_bc, side2): 
    side3 = side_ab
bisector = sqrt(side1*side2*(side1 + side2 + side3)*\
                (side1 + side2 - side3))/(side1 + side2)
if isclose(side_ab, side_bc) or isclose(side_ab, side_ac) or\
isclose(side_ac, side_bc):
    isosceles_y_or_n = "Треугольник равнобедренный"
else:
    isosceles_y_or_n = "Треугольник неравнобедренный"
A1, B1, C1 = equation_line(x1, y1, x2, y2)
A2, B2, C2 = equation_line(x2, y2, x3, y3)
A3, B3, C3 = equation_line(x3, y3, x1, y1)
info_dot, k =  area(x1, y1, x2, y2, x3, y3, xm, ym)
if k == 1:
    # Поиск расстояния от точки до всех сторон по координатам
    distance1 = abs(A1*xm + B1*ym + C1)/sqrt(pow(A1, 2) + pow(B1,2))
    distance2 = abs(A2*xm + B2*ym + C2)/sqrt(pow(A2, 2) + pow(B2,2))
    distance3 = abs(A3*xm + B3*ym + C3)/sqrt(pow(A3, 2) + pow(B3,2))
    # Поиск минимального расстояния
    distance_min = distance1
    if isclose(distance2, distance_min) or distance2 < distance_min:
        distance_min = distance2
    if isclose(distance3, distance_min) or distance3 < distance_min:
        distance_min = distance3

# Блок вывода
print(f"Сторона AB: {side_ab:.5g}",
    f"Сторона ВС: {side_bc:.5g}",
    f"Сторона АС: {side_ac:.5g}",
    f"Биссектриса проведенная из меньшего угла равна: {bisector:.5g}",
    isosceles_y_or_n,
    info_dot,
    f"Расстояние до меньшей стороны: {distance_min:.5g}",
    sep="\n")
