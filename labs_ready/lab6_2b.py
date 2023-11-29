# Джафаров Рустам. Группа ИУ7-16Б
# Программа которая удаляет элемент по индексу алгоритмически

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

# Удаление элемента
j = int(input("Учтите, что индексация начинается с нуля. \
Введите индекс, для удаления элемента на данном месте: "))
temp = None # Начало реализвции алгаритма. Дополнительное "ведро", для сдвига
while True:
    if j <= 0 or j > length - 1:
        print("Отрицательный индекс не обрабатываю:")
        j = int(input("Введите индекс куда вы хотитве добавить эелмент: "))
    else:
        break
# Сдвигаем все элементы вправо пока не встретим нужный нам индекс
for i in range(j, len(arr) - 1): 
    temp = arr[i]
    arr[i] = arr[i + 1]
    arr[i + 1] = temp
print(arr)
arr.pop()

# Вывод списка с удаленным элементом
print("Обновленный список: ", arr)