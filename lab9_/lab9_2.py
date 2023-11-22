# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая поворачивает квадратную целочисленную матрицу на 90 
# градусов по часовой стрелке, затем на 90 градусов против часовой стрелки

n = int(input("Введите размер квдратной матрицы: "))
while True:
    if n <= 0:
        print("Размер матрицы не можеть быть отрицательным или меньбше нуля")
        n = int(input("Введите размер квдратной матрицы: "))
    else:
        break
arr = [list(map(int, input(f"Введите {i + 1} строчку: ").split())) for i in range(n)]
print("Исходная матрица: ")
for i in range(n):
    print(*arr[i])
# Поворачиваем по часовой стрелке (обходим против часовой стрелке)
for i in range(n//2):
    for j in range(i, n - 1 - i):
        temp = arr[j][i]
        arr[j][i] = arr[n - 1 - i][j]
        arr[n - 1 - i][j] = arr[n - 1 - j][n - 1 - i]
        arr[n - 1 - j][n - 1 - i] = arr[i][n - 1 - j]
        arr[i][n - 1 - j] = temp
print("Промежуточная матрица: ")
for i in range(n):
    print(*arr[i])
# Поворачиваем против часовой стрелке (обходим по часовой стрелке)
for i in range(n//2):
    for j in range(i, n - i - 1): 
        temp = arr[i][j]
        arr[i][j] = arr[j][n - 1 - i]
        arr[j][n - 1 - i] = arr[n - 1 - i][n - 1 - j]
        arr[n - 1 - i][n - 1 - j] = arr[n - 1 - j][i]
        arr[n - 1 - j][i] = temp
print("Конечная матрица: ")
for i in range(n):
    print(*arr[i])