# Джафаров Рустам. Группа ИУ7-16Б
# Замена всех строчных 

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
    a = input(f"Введите элемент списка под номером {i + 1}: ")
    arr.append(a)
print("Введенный вами список: ", arr)

for i in range(length):
    tmp = '' # Временная строка          
    for j in range(len(arr[i])):
        if arr[i][j] in "eyuioa":
            tmp += arr[i][j].upper()
        else:
            tmp += arr[i][j]
    arr[i] = tmp

# Вывод измененного списка
print("Вывод списка с измененными буквами", arr)