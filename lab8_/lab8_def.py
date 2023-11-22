n = int(input("Введите размер квдратной матрицы: "))
a = int(input("Введите как вы хотите повернуть(1 - по часовой, 2 -против часовой): "))
while True:
    if n <= 0:
        print("Размер матрицы не можеть быть отрицательным или меньбше нуля")
        n = int(input("Введите размер квдратной матрицы: "))
    else:
        break
arr = [list(map(int, input(f"Введите {i + 1} строчку: ").split())) for i in range(n)]
print("Исходная матрица: ")
if a == 1:
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
    print("матрица: ")
    for i in range(n):
        print(*arr[i])
if a == 2:
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
    print("матрица: ")
    for i in range(n):
        print(*arr[i])