# Джафаров Рустам. Группа ИУ7-16Б
# Пооиск элемента с максимальныйм количеством согласных английских букв

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

lst_en_cons = "QWRTPSDFGHJKLZXCVBNMqwrtpasdfghjklzxcvbnm"
i_max = 0
count_max = 0

for i in range(1, len(arr)):
    count = 0
    for j in range(len(arr[i])):
        if arr[i][j] in lst_en_cons:
            count += 1
    if count >= count_max:
        i_max = i

# Вывод элемента
print(arr[i_max])