# Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
import os
currentDirectory = os.getcwd()
N = int(input('Введите размер списка: '))
a = [randint(1, 100) for i in range(N)]
print('Исходный список: ', *a)
fileWithPositions = open(currentDirectory + '\\2\positionstask4.pos')
result = 1
for line in fileWithPositions:
    position = int(line)
    if position <= len(a):
        result *= a[position - 1]
print(f'Сумма чисел в указанных позициях = {result}')
    