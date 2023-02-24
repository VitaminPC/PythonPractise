# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
N = int(input('Введите натуральное число: '))
Factors = []
Cycles = int(N**(0.5))+1
for i in range(2, Cycles):
    while(N % i == 0):
        Factors.append(i)
        N /= i
if N != 1:
    Factors.append(int(N))
print('Простые множители введенного числа: ', Factors)