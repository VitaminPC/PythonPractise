# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random  
N = int(input('Введите размер списка: '))
a = [round(random.randint(1, 1000) * random.random(), 2) for i in range(N)]
print('Исходный массив: ', *a)
maxDrob = 0
minDrob = 1
for i in range(N):
    drob = a[i]
    if a[i] > 1:
        drob = round(a[i] % int(a[i]), 2) 
    if drob > maxDrob:
        maxDrob = drob
    if drob < minDrob:
        minDrob = drob
print(f'Разница между максимальным и минимальным значением дробной части элементов: {round(maxDrob - minDrob, 2)}')