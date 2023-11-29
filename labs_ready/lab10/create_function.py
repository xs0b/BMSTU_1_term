from numpy import linspace

def f(x): # Функция f(x)
    z = pow(x, 1)
    return z

def F(x): # Первообразная функции f(x) F(x)
    return pow(x, 2)/2

def create_array_X(start, stop, n): 
    X = linspace(start, stop, num=n + 1, endpoint=True)
    return X

def create_array_Y(X):
    Y = []
    for i in range(len(X)):
        Y.append(f(X[i]))
    return Y

def create_l(X, Y): 
    l = []  
    for i in range(len(X)):
        summ = 0
        if i <= 1: # Метод правых пярмоугольников
            for j in range(len(X[i])):
                summ += Y[i][j]
            l.append(summ * (X[i][1] - X[i][0]))
            # print(summ * (X[i][1] - X[i][0]))
        else: # Метод трапеций
            s = 0
            for j in range(len(X[i]) - 1): # Метод трапеций
                s = (Y[i][j] +  Y[i][j + 1])
                summ += (s * (X[i][1] - X[i][0]))/2
            l.append(summ)
    return l

def abs_rel_error(sigma, l): # Погрешности
    a = sigma - l
    if l == 0:
        l = 0.0001
    r = abs(a/l)
    return a, r

# Метод правых прямоугольников
def method_1(a, b, count_sec):
    h = (b - a) / count_sec
    return h * sum([f(a + i * h) for i in range(1, count_sec + 1)])

# Метод трапеций
def method_2(a, b, count_sec):
    h = (b - a) / count_sec
    return h * sum([(f(a + i * h) + f(a + (i + 1) * h)) / 2 for i in range(count_sec)])

# def worst_metod(start, stop, n, number):
#     summm = 0
#     if number == 1 or number == 2:
#         X = []
#         Y = []
#         X.append(create_array_X(start, stop, n))
#         for i in range(len(X)):
#             Y.append(f(X[i]))
#         for j in range(len(X)):
#             summm += Y[0][j] * (X[0][1] - X[0][0])
#     else:
#         X = []
#         Y = []
#         X.append(create_array_X(start, stop, n))
#         for i in range(len(X)):
#             Y.append(f(X[i]))
#         for j in range(len(X) - 1): # Метод трапеций
#             s = (Y[0][j] +  Y[0][j + 1])
#             summm += (s * (X[0][1] - X[0][0]))/2
#     return summm