
#Реализуйте алгоритм перемешивания списка.

from random import randint
N = int(input('Введите размер списка: '))
a = [randint(1, 100) for i in range(N)]
print('Исходный список: ', *a)
for i in range(0, N-1):
    ExchangePosition = randint(i+1,N-1)
    (a[i], a[ExchangePosition]) = (a[ExchangePosition], a[i])
print('Перемешанный список: ', *a)