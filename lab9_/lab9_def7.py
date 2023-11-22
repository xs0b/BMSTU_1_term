N = int(input("Введите размер трехмерной матрицы: "))
index = int(input("Введите индекс выбранного среза: "))

if index < 1 or index > N:
    print("Некорректный индекс")
else:
    array = []
    for i in range(N):
        matrix = []
        for j in range(N):
            row = []
            for k in range(N):
                row.append(i * N * N + j * N + k + 1)
            matrix.append(row)
        array.append(matrix)
    print("Исходный массив:")
    for matrix in array:
        print(matrix)
    srez = array[index - 1]
    print("Выбранный срез:")
    for row in srez:
        print(row)
