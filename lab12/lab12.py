# Джафаров Рустам. Группа ИУ7-16Б
# Текстовый редактор в консоле 

from func_text import *

import math
# Python - это высокоуровневый, интерпретируемый, обобщенный, динамический и 
# объектно-ориентированный язык программирования, который был создан в 1991 году
# Гвидо ван Россумом. Он широко используется для веб-разработки, анализа данных,
# научных вычислений, искусственного интеллекта и машинного обучения. 
# Python обладает простым и понятным синтаксисом, что делает его идеальным для 
# начинающих программистов.
text = ["Python - это высокоуровневый, интерпретируемый,",
        " динамический и объектно-ориентированный язык программирования, обобщенный, который был создан",
        "был создан в 1991 году Гвидо ван Россумом. Он ", 
        "-1+1 a -1-2 a 1--1 a 1---1 a 1 -+ 1",
        "1 +- 1 a 1 - 1 +++ 1 - 1",
        "широко используется для веб-разработки, анализа данных,", 
        "научных вычислений, искусственного интеллекта и машинного ",
        "обучения. Python обладает 1+1 простым и понятным синтаксисом,", 
        "7+      1 что делает его идеальным для начинающих программистов."]

# Поиск длины редактируемой строки
max_len = 0
for i in text:
    if len(i) >= max_len:
        max_len = len(i)

print("-" * max_len)
for i in text:
    print(i)
print("-" * max_len)

menu()
choice = input("Введите номер действия: ")
n = 0
while True:
    if choice == '1':
        text = alignment_left_without_space(text, max_len)
        menu()
        n = 1
        choice = input("Введите номер действия: ")
    elif choice == '2':
        text = alignment_right_without_space(text, max_len)
        menu()
        choice = input("Введите номер действия: ")
        n = 2
    elif choice == '3':
        text = alignment_width_with_space(text, max_len)
        menu()
        n = 3  
        choice = input("Введите номер действия: ")
    elif choice == '4':
        word = None
        while word is None:
            try:
                word = input("Введите слово: ")
                for i in word.split("-"):
                    if not i.isalpha():
                        word = None
                        raise Exception()
            except Exception:
                    print("Параметр 'слово' введен неверно. 'Слово' это набор букв без спецсимволов")
        text = delete_word(text, word, max_len, n)
        menu()  
        choice = input("Введите номер действия: ")
    elif choice == '5':
        word = None
        while word is None:
            try:
                word = input("Введите слово, которое хотитие заменить: ")
                for i in word.split("-"):
                    if not i.isalpha():
                        word = None
                        raise Exception()
            except Exception:
                    print("Параметр 'слово' введен неверно. 'Слово' это набор букв без спецсимволов")
        change_w = None
        while change_w is None:
            try:
                change_w = input("Введите слово на которое хотите заменить: ")
                for i in change_w.split("-"):
                    if not i.isalpha():
                        change_w = None
                        raise Exception()
            except Exception:
                    print("Параметр 'слово' введен неверно. 'Слово' это набор букв без спецсимволов")
        text = change_word(text, word, change_w, max_len, n)
        # for i in text:
        #     print(i)
        menu()
        choice = input("Введите номер действия: ")    
    elif choice == '6':
        text = calculate(text, max_len, n)  
        menu()
        choice = input("Введите номер действия: ")  
    elif choice == '7':
        text = del_sentence_more_word_start_letter(text, max_len)
        menu()
        choice = input("Введите номер действия: ")  
    elif choice == '8':
        print("-" * max_len)
        for i in text:
            print(i)
        print("-" * max_len)
        break
    else:
        print("Выбор неправильный! Введите от 1 до 8. ")
        choice = input("Введите номер действия повторно: ")