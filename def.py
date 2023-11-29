# Подключаем модуль(-и)
from math import inf
from itertools import chain
 
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

ev = []
odd = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        ev.append((i, arr[i]))
    else:
        odd.append((i, arr[i]))
min_len = min(len(ev), len(odd))
for i in range(min_len):
    i, j, o, e = odd[i][0], ev[i][0], odd[i][1], ev[i][1]
    arr[j] = o
    arr[i] = e

print(arr)
