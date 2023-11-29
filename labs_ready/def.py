my_x = float(input("Введите x: "))

eps = float(input("Введите требуемую точность: "))
while eps <= 0:
    print("Точность не может быть меньше или равна 0.")
    eps = int(input("Введите новое значение точности: "))

max_iterations = int(input("Введите максимальное количество итераций: ")) 
while max_iterations <= 0:
    print("Итерации не могут быть меньше или равна 0.")
    max_iterations = int(input("Введите новое значение максимального количества итераций: "))

print_step = int(input("Введите шаг показа итераций: ")) 
while print_step < 1:
    print("Шаг не может быть меньше 1.")
    print_step = int(input("Введите новое значение шага: "))

s = 1
t = 1 
a = 1 
length = 46
print("-" * length, 
      f"| {'№ итерации':^12} | {'Значение':^12} | {'Сумма':^12} |", 
      "-" * length, 
      sep='\n')
print(f"|{a:^14.5g}| {t:^14.5g}| {s:^14.5g}|")

while abs(t) > eps and a <= max_iterations: 

    number = 2 * a  + 1
    factorial = 1
    while number > 1:
        factorial = factorial * number
        number = number - 1

    t = ((-1)**a) * ((my_x**(2*a)) / factorial) 
    s += t 
    a += 1 
    if (a - 1) % print_step == 0: 
        print(f"|{a:^14.5g}| {t:^14.5g}| {s:^14.7g}|") 
print("-" * length)
if a > max_iterations: 
    print("Требуемая точность не может быть достигнута за указанное количество итераций.")
else: 
    print(f"Сумма бесконечного ряда равна {(s + t):.5g}, вычисленная за {a:.5g} итераций.") # Вывод суммы и количества итераций