def separate_check_float(vvod_float):
    num = '01234565789.-+e'
    flag = True
    k = 0
    for i in vvod_float:
        if i not in num  or vvod_float[0] == 'e' or vvod_float == 'e' or '.e' in vvod_float:
            flag = False
        if i == 'e':
            k += 1
    if k > 1:
        flag = False
    return flag

def separate_check_int(vvod_int):
    num = '01234565789+e'
    flag = True
    k = 0
    for i in vvod_int:
        if i not in num or vvod_int[0] == '0':
            flag = False
    return flag

def check(start, stop, n1, n2):
    output = True
    if separate_check_float(start) == True and separate_check_float(stop) == True:
        print("Начало отрезка введено верно")
        print("Конец отрезка введено верно")
    else:
        print("Введите начало и конец занаво")
        output = False
    if separate_check_int(n1) == True:
        if int(n1) > 0:
            print("N1 введено верно")
    else:
        print("Введите N1 занаво")
        output = False
    if separate_check_int(n2) == True:
        if int(n2) > 0:
            print("N2 введено верно")
    else:
        print("Введите N2 занаво")
        output = False
    return output

def str_to_int_false(start, stop, n1, n2):
    return float(start), float(stop), int(n1), int(n2)