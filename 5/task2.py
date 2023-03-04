# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint
print('Правила игры:')
print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.')
print('Все конфеты оппонента достаются сделавшему последний ход.')
print()
secondtype = int(input('Выберите тип вторго игрока(2-компьютер, иначе = человек): '))

firstplayer = randint(0, 1)
print('Результат жеребьевки: Первый ход делает игрок номер ', firstplayer + 1) 

currentHoneys = 2021
playersHoneys = [0, 0]

def AIResult(Honeys):
    if Honeys <= 28: #забираем все конфеты
        return Honeys
    if Honeys % 28 == 1: #у противника безпроигрышная позиция. Чтобы запутать делаем случайные ходы
        return randint(1,29)
    else: #Противник прозевал или ходит вторым, тогда перехватываем инициативу и продолжаем безпроигрышную тактику
        step = Honeys % 28
        if step == 0:
            step = 28
        return step - 1 

while currentHoneys > 0:
    print(f'На столе {currentHoneys} конфет')
    maxHoneys = min(28, currentHoneys)
    result = 0
    if firstplayer == 1:
        if secondtype == 2:
            result = AIResult(currentHoneys)
            playersHoneys[1] += result
            print(f'AI got {result}')
        else:
            result = 0
            while result < 1 or result > maxHoneys:
                result = int(input(f'Второй игрок, сколько возьмете конфет?(от 1 до {maxHoneys}): '))
            playersHoneys[1] += result
        currentHoneys -= result
    if firstplayer == 0:
        result = 0
        while result < 1 or result > maxHoneys:
            result = int(input(f'Первый игрок, сколько возьмете конфет?(от 1 до {maxHoneys}): '))
        playersHoneys[0] += result
        currentHoneys -= result
    if currentHoneys > 0:    
        if firstplayer == 1:
            firstplayer = 0
        elif firstplayer == 0:    
            firstplayer = 1
print(f'Победил {firstplayer + 1}-й игрок')
