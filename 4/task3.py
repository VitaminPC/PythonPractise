# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
from random import randint
N = int(input('Введите размер списка: '))
a = [randint(1, 10) for i in range(N)]
print('Исходный список: ', a)
print('Список элементов исходного списка: ', set(a))