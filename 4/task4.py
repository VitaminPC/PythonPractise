# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from Equation import CreateEquation
from random import randint

N = int(input('Введите степень многочлена: '))
Koefficients = [randint(-10, 10) for i in range(N+1)]

print(CreateEquation(Koefficients))
