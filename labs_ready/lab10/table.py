from create_function import *

def table_sigma(l_1_2, l_3_4): # Создаем таблицу
    print("Таблица значений")
    print("-" * 44)
    print(f'|{" " * 10}| N1 {" " * 11}| N2 {" " * 11}|') 
    print("-" * 44)
    print(f"| Метод №1 |{l_1_2[0]:^15.7g}|{l_1_2[1]:^15.7g}|")
    print("-" * 44)
    print(f"| Метод №2 |{l_3_4[0]:^15.7g}|{l_3_4[1]:^15.7g}|")    
    print("-" * 44)
    print()

def table_error(l_1_2, l_3_4, sigma): # Создаем таблицу
    print("Таблица погрешностей")
    print("-" * 71)
    print(f'|{" " * 10}| N1 {" " * 25}| N2 {" " * 24}|') 
    print("-", " " * 9, "-" * 59)
    print(f'|{" " * 10}| abs_err{" " * 6}| rel_err{" " * 6}| abs_err{" " * 5} | rel_err{" " * 5}|')
    print("-" * 71) 
    a1, r1 = abs_rel_error(sigma, l_1_2[0])
    a2, r2 = abs_rel_error(sigma, l_1_2[1])
    a3, r3 = abs_rel_error(sigma, l_3_4[0])
    a4, r4 = abs_rel_error(sigma, l_3_4[1])
    print(f"| Метод №1 | {a1:^12.7g} | {r1:^12.7g} | {a2:^12.7g} | {r2:^11.7g} |")
    print("-" * 71)
    print(f"| Метод №2 | {a3:^12.7g} | {r3:^12.7g} | {a4:^12.7g} | {r4:^11.7g} |")    
    print("-" * 71)
    print()

def accuracy(l_1_2, l_3_4, sigma):
    a1, r1 = abs_rel_error(sigma, l_1_2[0])
    a2, r2 = abs_rel_error(sigma, l_1_2[1])
    a3, r3 = abs_rel_error(sigma, l_3_4[0])
    a4, r4 = abs_rel_error(sigma, l_3_4[1])
    min1 =  min(r1, r2)
    min2 =  min(r3, r4)
    min_0 = min(min1, min2)
    if min_0 == r1:
        print("Самый точный метод №1 при N1 разбиений")
        num = 1
    if min_0 == r2:
        print("Самый точный метод №1 при N2 разбиений")
        num = 2
    if min_0 == r3:
        print("Самый точный метод №2 при N1 разбиений")
        num = 3
    if min_0 == r4:
        print("Самый точный метод №2 при N2 разбиений")
        num = 4
    if num == 1 or num == 2:
        num1 = 3
    if num ==3 or num == 4:
        num1 = 1
    return num, num1