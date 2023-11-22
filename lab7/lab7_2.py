# Джафаров Рустам. Группа ИУ7-16Б
# Добавляет после четных элементов их удовенное значение  (Варинат № 3)
# import sys

arr = []
length = int(input("Введите длинну списка: "))

# Проверка на корректность ввода
while True: 
    if length < 0:
        print("Длина списка не может быть меньше нуля")
        length = int(input("Введите длинну списка: "))
    else: 
        break

# Заполнение списка
for i in range(length):
    a = int(input(f"Введите элемент списка под номером {i + 1}: "))
    arr.append(a)
print("Введенный вами список: ", arr)

# Добавление элементов
k = 0
for i in range(length):
    if arr[i] % 2 == 0:
        k += 1
j = None
arr.extend([None] * k)
z = 0
for i in range(length - 1, 0, -1):
    if arr[i] % 2 != 0:
        arr[i + k], arr[i] = arr[i], arr[i + k]
    else:
        arr[i + k - 1], arr[i] = arr[i], arr[i + k - 1]
        k -= 1
    # print(arr)
for i in range(len(arr)):
    if arr[i] == None:
        arr[i] = arr[i - 1] * 2
# Вывод списка
print("Обновелнный список: ", arr)
