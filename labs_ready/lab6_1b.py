# Джафаров Рустам. Группа ИУ7-16Б
# Программа которая добавляет элемент в заданное место списка (по индексу) 
# алгоритмически

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

# Добавим элемент по индексу алгоритмически
str = input("Вы хотите добавить элемент в конце списка? (Да/Нет): ")
if str == "Да":
    elem = int(input("Введите элемент, который хотите добавить в конец: "))
    arr.append(elem)
else:
    arr_j, j = map(int, input("Введите элемент, который хотите добавить, и индекс,\
куда вы хотите добавить через пробел.\
Учтите, что индексация начинается с нуля: ").split())
    while True:
        if j <= 0 or j > length - 1:
            print("Отрицательный индекс не обрабатываю:")
            j = int(input("Введите индекс куда вы хотитве добавить эелмент: "))
        else:
            break
    arr.append(0) # Начало реализвции алгаритма. Добавляем в конец 0
    i = len(arr) - 1
    temp = None # Дополнительное "ведро", для сдвига
    while i != j: # Сдвигаем все элементы вправо пока не встретим нужный нам индекс
        temp = arr[i]
        arr[i] = arr[i - 1]
        arr[i - 1] = temp
        i -= 1
    arr[j] = arr_j  # Запись добавляемого элемента на искомую свободную позицию

# Вывод списка с добавленным элементом
print("Обновленный список: ", arr)