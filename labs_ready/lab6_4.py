# Джафаров Рустам. Группа ИУ7-16Б. Варинат № 5.3
# Программа, которая находит последовательность чисел, в которой все, 
# начиная с 3-го, являются суммой двух предыдущих

# Подключаем модуль(-и)
from math import inf

arr = [] # Созадем пустой список
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

# Поиск искомой последовательности
mx = 2
t = 2
indm = 0
lprev = arr[0]
prev = arr[1]
for i in range(2, length):
    if (arr[i] == prev + lprev):
        t += 1
        if t >= mx:
            mx = t
            indm = i
    else:
        t = 2
    prev = arr[i]
    lprev = arr[i - 1]
print("Искомая последовательность: ", arr[(indm - mx + 1):(indm + 1)])