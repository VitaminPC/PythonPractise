def Zadacha2_2():
    # Напишите программу, которая принимает на вход координаты двух точек
    # и находит расстояние между ними в 2D пространстве.
    # Пример:
    # - A (3,6); B (2,1) -> 5,09
    # - A (7,-5); B (1,-1) -> 7,21
    x1 = int(input('Введите x1: '))
    y1 = int(input('Введите y1: '))
    x2 = int(input('Введите x2: '))
    y2 = int(input('Введите y2: '))
    distance = round(((x2 - x1)**2 + (y2 - y1)**2)**(0.5), 2)
    print(f'Растояние между A ({x1},{y1}) и B ({x2},{y2}) равно {distance}')


def Zadacha2_1():
    # Напишите программу, которая по заданному номеру четверти,
    # показывает диапазон возможных координат точек в этой
    # четверти (x и y).
    n = int(input('Номер четверти: '))
    if n < 1 or n > 4:
        print('Введите значение от 1 до 4')
    elif (n == 1):
        print('x > 0 и y > 0')
    elif (n == 2):
        print('x > 0 и y < 0')
    elif (n == 3):
        print('x < 0 и y < 0')
    elif (n == 4):
        print('x < 0 и y > 0')


def Zadacha2():
    # Напишите программу, которая принимает на вход координаты
    # точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
    # плоскости, в которой находится эта точка
    # (или на какой оси она находится).
    # Пример:
    # - x=34; y=-30 -> 4
    # - x=2; y=4-> 1
    # - x=-34; y=-30 -> 3
    x = int(input('Введите значение x: '))
    y = int(input('Введите значение y: '))
    if x == 0 or y == 0:
        print('Нельзя вводить нулевые значения')
    elif (x > 0 and y > 0):
        print(f'x = {x}; y = {y} -> {1}')
    elif (x > 0 and y < 0):
        print(f'x = {x}; y = {y} -> {2}')
    elif (x < 0 and y < 0):
        print(f'x = {x}; y = {y} -> {3}')
    elif (x < 0 and y > 0):
        print(f'x = {x}; y = {y} -> {4}')


def Zadacha1pow():
    # Напишите программу для. проверки истинности утверждения
    # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    result = True
    for x in True, False:
        for y in True, False:
            for z in True, False:
                if not (x or y or z) != (not x and not y and not z):
                    result = False
    if result:
        print('Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно для всех значений предикат')
    else:
        print('Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно не для всех значений предикат')


def Zadacha1():
    # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
    # Пример:
    # - 6 -> да
    # - 7 -> да
    # - 1 -> нет
    day = int(input('Введите номер дня в неделе: '))
    if day == 7 or day == 6:
        print('Это выходной день')
    elif day < 1 or day > 7:
        print('Введите значение от 1 до 7')
    else:
        print('Это не выходной день')


# Zadacha1()
# Zadacha1pow()
# Zadacha2()
# Zadacha2_1()
Zadacha2_2()

# Задача семинара 1
# n = int(input('Введите количество километров в день: '))
# m = int(input('Введите расстояние которе нужно проехать: '))
# print('{}'.format(int(round(m/n + 0.5))))