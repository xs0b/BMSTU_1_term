# Джафаров Рустам. Группа ИУ7-16Б
# Удаляет все отрицательные элементы списка (Варинат № 5)

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

# Удаление
j = None  
for i in range(len(arr)):
    if arr[i] < 0:
        if j == None:
            j = i
    else:
        if j != None:
            arr[j] = arr[i]
            j += 1 
    print(arr)
        
del arr[j:]

# Вывод обновленного списка
print("Обновелнный список: ", arr)