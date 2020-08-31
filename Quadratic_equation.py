from math import *


def get_the_number_of(s):  # возвращает из ax или ax^2 только a
    s = s.replace('x^2', "")
    s = s.replace('x', "")
    return s


def get_two_first_symbols_and_sign(
        s):  # Эта функция достаёт первые три слова, считая знак + или -. Чтобы использовать её в других программах, заведите массив с индексами "position_of_space" и скопируйте функцию "get_the_number_of"
    first_symbol = get_the_number_of(s[:position_of_space[0]])  # Основная суть - с помощью используемой тут функции мы получаем строку без x и x^2, так что остаётся только взять всё от начала строки до первого пробела итп с другими символами
    sign = s[position_of_space[0] + 1:position_of_space[1]]
    second_symbol = get_the_number_of(s[position_of_space[1] + 1:position_of_space[2]])
    return first_symbol, sign, second_symbol


print(
    "Введите квадратное уравнение в виде ax^2 + bx + c = 0 или линейное в виде ax + b = c, где a, b, c - натуральные числа (рекомендую ознакомиться с readme файлом)")
equation = input("Строка ввода: ")
number_of_words = equation.count(' ') + 1  # Количесво слов в строке
position_of_space = []  # Позиции, на которых стоят пробелы
for i in range(len(equation)):
    if equation[i] == ' ':
        position_of_space.append(i)  # Узнаём все индексы пробелов, чтобы уметь доставать все переменные

if number_of_words == 5:  # Если выражение имеет вид ax + b = c, то в нём "5 слов"
    a = int(get_two_first_symbols_and_sign(equation)[0])  # С помощью функции достаём первый (ноликовый) символ итп
    sign = get_two_first_symbols_and_sign(equation)[1]
    b = int(get_two_first_symbols_and_sign(equation)[2])
    if sign == "+":
        b *= -1  # Если выражение имеет вид ax + b = c, то x = (c - b) / a, значит у b знак должен быть обратным

    c = int(equation[
            position_of_space[
                3] + 1:])  # Приведение в комфортный вид всех используемых в математике вычислений

    print("x = " + str((c + b) / a))

else:  # Если выражение всё же квадратное вида ax^2 + bx + c = 0
    a = int(get_two_first_symbols_and_sign(equation)[0])
    b = int(get_two_first_symbols_and_sign(equation)[2])
    first_sign = get_two_first_symbols_and_sign(equation)[1]
    if first_sign == "-":
        b *= -1  # Аналогично 32 строке
    second_sign = equation[position_of_space[2] + 1:position_of_space[3]]
    c = int(equation[position_of_space[3] + 1:position_of_space[4]])
    if second_sign == "-":
        c *= -1

    D = b ** 2 - 4 * a * c  # Дискриминант

    if D > 0:
        x1 = (-1 * b + sqrt(D)) / (2 * a)
        x2 = (-1 * b - sqrt(D)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif D < 0:
        print("D < 0")
    else:
        print("x =", (-1 * b + sqrt(D)) / (2 * a))
