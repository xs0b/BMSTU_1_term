def menu():
    """
    Выводит меню
    """
    print("Меню: ")
    print("1. Выровнять текст по левому краю.",
          "2. Выровнять текст по правому краю.",
          "3. Выровнять текст по ширине.",
          "4. Удаление всех вхождений заданного слова.",
          "5. Замена одного слова другим во всём тексте.",
          "6. Вычисление арифметических выражений над целыми числами внутри текста (сложение и вычитание)",
          "7. Найти (вывести на экран) и затем удалить предложение с максимальным количеством слов, начинающихся на заданную букву.",
          "8. Выход.",
          sep='\n')
    print()

# def alignment_left(mas : list) -> list: # Как делают в нормальном редакторе
#     """
#     Сдвигаем влево
#     """
#     print("-" * 210)
#     for i in mas:
#         i = i.lstrip()
#         print(i)
#     print("-" * 210)
#     return mas


# def alignment_left_without_space(mas : list, length : int) -> list:
#     """
#     Сдвигаем влево без пробелов 
#     """
#     print("-" * length)
#     for i in mas:
#         words = i.split()
#         temp = ""
#         for j in range(len(words)):
#             temp += words[j] + " "
#         i = temp
#         # print(i)
#     for i in mas:
#         tmp = ""
#         if len(i) == length:
#             pass
#         else:
#             for j in range(len(i)):
#                 if i[j] == " ":
#                     pass
#                 else:
#                     tmp += i[j]
#             i = tmp
#         print(i)
#     print("-" * length)
#     return mas

def alignment_left_without_space(text : list, length : int) -> list:
    print("-" * length)
    for i in range(len(text)):
        tmp = text[i].split()
        text[i] = ' '.join(tmp)
        print(text[i])
    print("-" * length)
    return text

def alignment_right_without_space(text : list, length : int) -> list:
    print("-" * length)
    for i in range(len(text)):
        tmp = text[i].split()
        text[i] = ' '.join(tmp)
    max_len = 0
    for i in text:
        if len(i) > max_len:
            max_len = len(i)
    for i in range(len(text)):
        l = len(text[i])
        text[i] = ' ' * (max_len - l) + text[i]
        print(text[i])
    print("-" * length)
    return text

# def alignment_left_with_space(mas : list, length : int) -> list:
#     """
#     Сдвигаем влево c пробелами
#     """
#     print("-" * length)
#     for i in mas:
#         words = i.split()
#         temp = ""
#         for j in range(len(words)):
#             temp += words[j] + " "
#         i = temp
#         print(i)
#     for i in mas:
#         quantity_space = length - len(i) # Количество пробелов для текущей строки
#         word_i = i.split()
#         tmp = "" # Типо фиксируем последнее слово
#         if len(i) == length: # Пропускаем самую длинную строку
#             pass
#         else:
#             for j in range(len(word_i)):
#                 tmp += word_i[j] + " " * (quantity_space // len(word_i)) 
#             i = tmp
#         if i[0] == " ":
#             i = i[1:]
#         print(i)
#     print("-" * length)
#     return mas

# def alignment_right(mas : list) -> list: # Как делают в нормальном редакторе
#     """
#     Сдвигаем вправо
#     """
#     print("-" * length)
#     for i in mas:
#         # i.rjust(length, " ")
#         i = " " * (length - len(i)) + i
#         i = i.rstrip()
#         print(i)
#     print("-" * length)
#     return mas

# def alignment_right_without_space(mas : list, length : int) -> list:
#     """
#     Сдвигаем вправо без пробелов 
#     """
#     print("-" * length)
#     for i in mas:
#         words = i.split()
#         temp = ""
#         for j in range(len(words)):
#             temp += words[j] + " "
#         i = temp
#     for i in mas:
#         if len(i) == length: # Пропускаем самую длинную строку
#             pass
#         else:
#             tmp = "" + " " * (length - len(i)) # Временная строка
#             for j in range(len(i)):
#                 tmp += i[j]
#             if i[len(i) - 1] == " ":
#                 tmp = " " + tmp[:-1]
#                 i = tmp
#             else:
#                 i = tmp
#         print(i)
#     print("-" * length)
#     return mas

# def alignment_right_with_space(mas : list, length : int) -> list:
#     """
#     Сдвигаем вправо c пробелами 
#     """
#     print("-" * length)
#     for i in mas:
#         words = i.split()
#         temp = ""
#         for j in range(len(words)):
#             temp += words[j] + " "
#         i = temp
#     for i in mas:
#         if len(i) == length: # Пропускаем самую длинную строку
#             pass
#         else:
#             quantity_space = length - len(i) # Количество пробелов для текущей строки
#             word_i = i.split()
#             tmp = "" # Типо фиксируем первое слово 
#             for j in range(len(word_i)): # Сначала сдвигаем вправо
#                 if j < len(word_i) - 1:
#                     tmp += word_i[j] + " " * (quantity_space // len(word_i)) 
#                 else:
#                     tmp += word_i[j]
#             i = tmp
#             if i[0] == " ":
#                 i = i[1:]
#             i = " " * (length - len(i)) + i
#             i = i.rstrip()
#         print(i)
#     print("-" * length)
#     return mas

# def alignment_width_without_space(mas : list, length : int) -> list:
#     """
#     Выравнивание по ширине без пробелов 
#     """ 
#     for i in mas:
#         words = i.split()
#         temp = ""
#         for j in range(len(words)):
#             temp += words[j] + " "
#         i = temp
#     print("-" * length)
#     for i in mas:
#         i = i.center(length)
#         print(i)
#     print("-" * length)
#     return mas

def alignment_width_with_space(mas : list, length : int) -> list:
    """
    Выравнивание по ширине с пробелами 
    """ 
    print("-" * length)
    for i in mas:
        words = i.split()
        temp = ""
        for j in range(len(words)):
            temp += words[j] + " "
        i = temp
    max_len = length
    for i in range(len(mas)):
        tmp = mas[i].split()
        tmp_len = len(''.join(tmp))
        missing_length = max_len - tmp_len
        space_count = len(tmp) - 1
        space_len = missing_length // space_count
        if missing_length % space_count == 0:
            spaces = ' ' * space_len
            mas[i] = spaces.join(tmp)
        else:
            joined_tmp = ''
            need_add_count = missing_length - (space_count * space_len)
            for j in range(len(tmp)):
                joined_tmp += tmp[j]
                if j == len(tmp) - 1:
                    continue
                elif j >= len(tmp) - 1 - need_add_count:
                    joined_tmp += ' ' * (space_len + 1)
                else:
                    joined_tmp += ' ' * space_len
            mas[i] = joined_tmp
        print(mas[i])
    print("-" * length)
    return mas

def delete_word(mas : list, word : str, length, n : int) -> list:
    """
    Удаление заданного слова
    """
    i = 0
    for i in range(len(mas)):
        tmp = mas[i].split()
        # print(tmp)
        for j in range(len(tmp)):
            if tmp[j] == word:
                tmp[j] = ""
            if tmp[j][:-1] == word and tmp[j][-1] in ".,?!:;":
                tmp[j] = tmp[j][-1]
        mas[i] = " ".join(tmp)
    if n == 0:
        print("-" * length)
        for i in range(len(mas)):
            print(mas[i])
        print("-" * length)
    if n == 1:
        mas = alignment_left_without_space(mas, length)
    if n == 2:
        mas = alignment_right_without_space(mas, length)
    if n == 3:
        mas = alignment_width_with_space(mas, length)
    return mas

def change_word(mas : list, word, change_word : str, length, n : int) -> list:
    """
    Замена заданного слова
    """
    print("-" * length)
    for i in range(len(mas)):
        tmp = mas[i].split()
        for j in range(len(tmp)):
            if tmp[j] == word:
                tmp[j] = change_word
            if tmp[j][:-1] == word and tmp[j][-1] in ".,?!:;":
                tmp[j] = change_word
        mas[i] = " ".join(tmp)
        if n == 0:
            print(mas[i])
    if n == 1:
        mas = alignment_left_without_space(mas, length)
    if n == 2:
        mas = alignment_right_without_space(mas, length)
    if n == 3:
        mas = alignment_width_with_space(mas, length)
    return mas

# def calculate_expression(s):
#     # Инициализируем результат
#     result = ''

#     # Инициализируем переменные для хранения чисел и операций
#     nums = []
#     op = ''

#     # Проходим по каждому символу в строке
#     for char in s:
#         # Если символ является числом, добавляем его к текущему числу
#         if char.isdigit():
#             if not nums or not nums[-1].isdigit():
#                 nums.append(char)
#             else:
#                 nums[-1] += char
#         # Если символ является операцией, сохраняем ее
#         elif char in ['+', '-']:
#             op = char
#         # Если символ является пробелом, вычисляем результат текущего выражения
#         elif char == ' ':
#             if op:
#                 num1 = int(''.join(nums[:-1]))
#                 num2 = int(nums[-1])
#                 if op == '+':
#                     result += str(num1 + num2)
#                 elif op == '-':
#                     result += str(num1 - num2)
#                 nums = [result]
#                 op = ''
#             else:
#                 result += char
#         # Если символ является частью слова, добавляем его к результату
#         else:
#             result += char

#   # Добавляем последнее выражение к результату
#     if op:
#         num1 = int(''.join(nums[:-1]))
#         num2 = int(nums[-1])
#         if op == '+':
#             result += str(num1 + num2)
#         elif op == '-':
#             result += str(num1 - num2)

#     return result

# def calculate_arithmetic(text):
#     operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
#     new_text = []
#     for line in text:
#         words = line.split()
#         for i, word in enumerate(words):
#             if word.isdigit() and i > 0 and words[i-1] in operators:
#                     operator = words[i-1]
#                     operand1 = int(words[i-2])
#                     operand2 = int(word)
#                     result = operators[operator](operand1, operand2)
#                     words[i] = str(result)
#                     words.pop(i-1)
#                     words.pop(i-2)
#         new_text.append(' '.join(words))
#     return new_text

# def calculate_expression_in_text(mas : list) -> list:
#     index_expression = []
#     list_expression = []
#     for i in range(len(mas)):
#         char = mas[i].split()
#         expression = []
#         flag = False
#         for j in range(len(char)):
#             check = separate_check_int(char[j])
#             if check != False:
#                 expression.append(char[j])
#                 index_expression.append(i)
#         list_expression.append(expression)
#     index_expression = list(set(index_expression))
#     print(index_expression)
#     print(expression)
#     for i in range(len(index_expression)):
#         if len(expression[index_expression[i]]) < 3 or int(expression[index_expression[i]][2]) < 0:
#             continue
#         else:
#             pass
#     return mas

# def calculate_expression_in_text(text, length):
#     for i in range(len(text)):
#         cursor_pos = 0
#         while cursor_pos < len(text[i]):
#             if text[i][cursor_pos] in '+-':
#                 left_arg = ''
#                 min_k = cursor_pos
#                 for k in range(cursor_pos - 1, -1, -1):
#                     if text[i][k] == ' ':
#                         break
#                     if text[i][k] == '-':
#                         if not left_arg:
#                             break
#                         else:
#                             left_arg = text[i][k] + left_arg
#                             min_k = k
#                             continue
#                     if text[i][k] in '0123456789' and '-' not in left_arg:
#                         left_arg = text[i][k] + left_arg
#                     else:
#                         break
#                     min_k = k
#                 if not left_arg:
#                     cursor_pos += 1
#                     continue
#                 max_k = cursor_pos
#                 right_arg = ''
#                 for k in range(cursor_pos + 1, len(text[i])):
#                     if text[i][k] == ' ':
#                         break
#                     if text[i][k] == '-':
#                         if right_arg == '':
#                             right_arg = text[i][k] + right_arg
#                             max_k = k
#                             continue
#                     if text[i][k] in '0123456789':
#                         right_arg += text[i][k]
#                     else:
#                         break
#                     max_k += 1
#                 if not right_arg:
#                     cursor_pos += 1
#                     continue
#                 if text[i][cursor_pos] == '+':
#                     result = str(int(left_arg) + int(right_arg))
#                 else:
#                     result = str(int(left_arg) - int(right_arg))
#                 text[i] = text[i][:min_k] + result + text[i][max_k + 1:]
#                 cursor_pos = min_k
#             cursor_pos += 1
#     print('-' * length)
#     for i in text:
#         print(i)
#     print('-' * length)
#     return text

# def separate_check_int(vvod_int : str):
#     num = '01234565789+e-'
#     flag = True
#     for i in vvod_int:
#         if i not in num or vvod_int[0] == '0' or vvod_int[0] == '+':
#             flag = False
#         if vvod_int == '+':
#             flag = '+'
#         if vvod_int == '-':
#             flag = '-'
#     return flag

def calculate(text : list, length, n : int) -> list:
    for i in range(len(text)):
        st = text[i].replace("+", " + ").replace("-", " - ").split()
        dl = len(st)
        c = 1
        while c < dl:
            if st[c] in "+-":
                try:
                    n1, n2 = int(st[c - 1]), int(f"{st[c]}{st[c + 1]}")
                    st[c - 1] = str(n1 + n2)
                    st.pop(c)
                    st.pop(c)
                    dl -= 2
                except:
                    c += 1
            else:
                c += 1
        text[i] = " ".join(st)
        if n == 0:
            print(text[i])
    if n == 1:
        text = alignment_left_without_space(text, length)
    if n == 2:
        text = alignment_right_without_space(text, length)
    if n == 3:
        text = alignment_width_with_space(text, length)
    # for i in range(len(text)):
    #     print(text[i])
    return text

def del_sentence_more_word_start_letter(text, length):
    text = alignment_left(text, length)
    symbol = None
    while symbol is None:
        try:
            symbol = input('Введите символ начала слов: ')
            if not symbol.isalpha() or len(symbol) > 1:
                symbol = None
                raise Exception()
        except Exception:
            print('Символ начала должен быть буквой')
    sentences_pos = p(text)
    removable_sent, need_sent_id = search(sentences_pos, text, symbol)
    if need_sent_id != -1:
        if sentences_pos[need_sent_id][0][0] == sentences_pos[need_sent_id][1][0]:
            text[sentences_pos[need_sent_id][0][0]] = \
                text[sentences_pos[need_sent_id][0][0]
                ][:sentences_pos[need_sent_id][0][1]] + \
                text[sentences_pos[need_sent_id][0][0]
                ][sentences_pos[need_sent_id][1][1] + 1:]

        else:
            text[sentences_pos[need_sent_id][0][0]] = \
                text[sentences_pos[need_sent_id][0]
                [0]][:sentences_pos[need_sent_id][0][1]]

            text[sentences_pos[need_sent_id][1][0]] = \
                text[sentences_pos[need_sent_id][1]
                [0]][sentences_pos[need_sent_id][1][1] + 1:]

            for k in range(sentences_pos[need_sent_id][1][0] - 1,
                           sentences_pos[need_sent_id][0][0], -1):
                text.pop(k)
    try:
        while text.index('') != -1:
            text.pop(text.index(''))
    except Exception:
        pass
    print('-' * length)
    if removable_sent != '':
        print('Удаляемое предложение:')
        print(removable_sent)
    else:
        print('Такое предложение не найдено!')
    print('-' * length)
    text = alignment_left_without_space(text, length)
    return text

def alignment_left(text : list, length : int) -> list:
    for i in range(len(text)):
        tmp = text[i].split()
        text[i] = ' '.join(tmp)
    return text

def p(text:list):
    sentences_pos = []
    for i in range(len(text)):
        start_ind = 0
        while True:
            tmp = text[i].find('.', start_ind)
            if tmp == -1:
                break
            else:
                if len(sentences_pos) == 0:
                    sentences_pos.append([[0, 0], [i, tmp]])
                else:
                    t_str = sentences_pos[-1][1][0]
                    t_pos = sentences_pos[-1][1][1]
                    while True:
                        try:
                            t_pos += 1
                            if len(text[t_str]) == t_pos:
                                t_str += 1
                                t_pos = 0
                            if text[t_str][t_pos] != '.' and text[t_str][t_pos] != ' ':
                                break
                        except:
                            break

                    sentences_pos.append([[t_str, t_pos], [i, tmp]])
                start_ind = tmp + 1
    return sentences_pos

def search(sentences_pos, text, symbol):
    need_sent_id = -1
    max_count = 0
    removable_sent = ''
    for i in range(len(sentences_pos)):
        tmp = ''
        if sentences_pos[i][1][0] == sentences_pos[i][0][0]:
            tmp = text[sentences_pos[i][1][0]][sentences_pos[i][0][1]:sentences_pos[i][1][1]]
        else:
            for j in range(sentences_pos[i][0][0], sentences_pos[i][1][0] + 1):
                if j == sentences_pos[i][1][0]:
                    tmp += ' ' + text[j][:sentences_pos[i][1][1] + 1] + ' '
                elif j == sentences_pos[i][0][0]:
                    tmp += ' ' + text[j][sentences_pos[i][0][1]:] + ' '
                else:
                    tmp += ' ' + text[j] + ' '
        tmp = tmp.split()
        tmp_count = 0
        for word in tmp:
            if word[0].lower() == symbol.lower():
                tmp_count += 1
        if need_sent_id == -1 and tmp_count > 0:
            need_sent_id = i
            max_count = tmp_count
            removable_sent = ' '.join(tmp)
        elif tmp_count > max_count:
            need_sent_id = i
            max_count = tmp_count
            removable_sent = ' '.join(tmp)
    return removable_sent, need_sent_id
