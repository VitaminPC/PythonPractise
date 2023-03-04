#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
N = int(input('Введите размер списка: '))
digits = [randint(1, 20) for i in range(N)]
minimal = int(input('Задайте минимум: '))
maximal = int(input('Задайте максимум: '))
indexes = []
for n in range(0, len(digits)):
    if minimal <= digits[n] <= maximal:
        indexes.append(n)

print('Индексы элементов находящиеся в заданом диапазоне: ')
print(indexes)    