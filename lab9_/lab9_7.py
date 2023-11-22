# Джафаров Рустам. Группа ИУ7-16Б
# Программа, которая выводит срез трехмерной матрицы

x, y, z = map(int, input().split())
number_y = int(input("Введите номер среза: "))
arr = []
for i in range(x):
    arr_i = []
    for j in range(y):
        arr_j = []
        for k in range(z):
            vvod = int(input(f"Введите элемент [{i}][{j}][{k}] трехмерной матрицы: "))
            arr_j.append(vvod)
        arr_i.append(arr_j)
    arr.append(arr_i)
print(arr)
j = number_y - 1
a = []
b = []
c = []
print("Искомые срезы")
for i in range(x):
    for k in range(z):
        a.append(arr[i][j][k])
for i in range(x):
    for k in range(z):
        b.append(arr[j][k][i])
for i in range(x):
    for k in range(z):
        c.append(arr[i][k][j])
print(a)
print(b)
print(c)