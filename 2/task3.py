# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# См. task3.md
N = int(input('Введите натуральное число: '))
print(f'Последовательность по формуле (1 + 1/n)**n от 1 до {N}:')
print('[ ',end='')
result = 0
for i in range(1, N+1):
    current = (1 + 1 / i) ** i
    result += current
    print(f' {current}', end='')
    if i < N:
        print(',', end='')
print(' ]')
print(f'Сумма последовательности = {result}')