# Джафаров Рустам. Группа ИУ7-16Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.

eng = "EYUIOAeyuioa"
cols = int(input("Введите количество столбцов матрицы: "))
rows = int(input("Введите количество строк матрицы: "))
while True: 
    if cols <= 0:
        print("Количество столбцов не может быть меньше нуля")
        cols = int(input("Введите количество столбцов: "))
    elif rows <= 0:
        print("Количество строк не может быть меньше нуля")
        rows = int(input("Введите количество строк: "))
    else:
        break
d = [list(map(str, input(f"Введите {i + 1} строчку матрицы D: ").split())) for i in range(rows)]
print("Матрица D до преобразования:")
for _ in range(rows):
    print(d[_])
for i in range(rows):
    for j in range(cols):
        tmp = ""
        for k in d[i][j]:
            if k in eng:
                tmp += "."
            else:
                tmp += k
        d[i][j] = tmp
print("Матрица D после преобразования:")
for _ in range(rows):
    print(d[_])
            