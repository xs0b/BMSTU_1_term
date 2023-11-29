from random import sample
from sort_m import *
from table import *

# Часть 1
# Ввод данных
list_op = [int(_) for _ in input("Введите список: ").split()]
n = len(list_op)
print(f"Ваш отсортированный список: {bubble_sort_f(list_op, n)[2]}")
list_op.clear()

# Часть 2
# Ввод данных
n1, n2, n3 = map(int, input("Введите кол-во элементо списков n1, n2, n3: ").split())
while True:
    if n1 <= 0:
        print("n1 не может быть меньше нуля или равно нулю")
        n1 = int(input("Введите n1 занаво: "))
    elif n2 <= 0:
        print("n2 не может быть меньше нуля или равно нулю")
        n3 = int(input("Введите n2 занаво: "))
    elif n3 <= 0:
        print("n3 не может быть меньше нуля или равно нулю")
        n3 = int(input("Введите n3 занаво: "))
    else:
        break
arr1 = sample(range(1, 10000000), n1)
arr2 = sample(range(1, 10000000), n2)
arr3 = sample(range(1, 10000000), n3)
time_list = []
counter_list = []
specifications_arr1_1 = bubble_sort_f(arr1, n1)
specifications_arr2_1 = bubble_sort_f(arr2, n2)
specifications_arr3_1 = bubble_sort_f(arr3, n3)
specifications_arr1_2 = bubble_sort_f(arr1, n1)
specifications_arr2_2 = bubble_sort_f(arr2, n2)
specifications_arr3_2 = bubble_sort_f(arr3, n3)
specifications_arr1_3 = bubble_sort_f(arr1[::-1], n1)
specifications_arr2_3 = bubble_sort_f(arr2[::-1], n2)
specifications_arr3_3 = bubble_sort_f(arr3[::-1], n3)
table(specifications_arr1_1, specifications_arr2_1, specifications_arr3_1,\
specifications_arr1_2, specifications_arr2_2, specifications_arr3_2, \
specifications_arr1_3, specifications_arr2_3, specifications_arr3_3, n1, n2, n3)


