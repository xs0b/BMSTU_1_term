# Джафаров Рустам. Группа ИУ7-16Б
# Программа которая меняет местами минимальный положительный и 
# максимальный положительный.

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

# Поиск максимального и минимального положительного элемента
max_arr_positive = -inf
min_arr_positive = +inf
i_max_arr_positive = 0
i_min_arr_positive = 0
for i in range(length): 
    if max_arr_positive <= arr[i] and arr[i] > 0:
        max_arr_positive = arr[i]
        i_max_arr_positive = i
    if min_arr_positive >= arr[i] and arr[i] > 0:
        min_arr_positive = arr[i]
        i_min_arr_positive = i
if max_arr_positive <= 0 or min_arr_positive <= 0:
    print("В данном списке нет двух положительных чисел")
elif max_arr_positive == min_arr_positive:
    arr[i_max_arr_positive], arr[i_min_arr_positive] = \
    arr[i_min_arr_positive], arr[i_max_arr_positive] # Меняем местами
    print(f"Элемент поменялся сам с собой {max_arr_positive}")
    print("Обновленный список: ", arr)
else:
    arr[i_max_arr_positive], arr[i_min_arr_positive] = \
    arr[i_min_arr_positive], arr[i_max_arr_positive] # Меняем местами
    print("Обновленный список: ", arr)