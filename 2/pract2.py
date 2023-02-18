Arbuses = input('Введите данные по арбузам через пробел: ')
Arbuses_data = Arbuses.split(' ')
minArbuse = maxArbuse = int(Arbuses_data[0])
minIndex = 0
maxIndex = 0
for i in range(0, len(Arbuses_data)):
    Arbuse_weight = int(Arbuses_data[i])
    if minArbuse > Arbuse_weight:
        minArbuse = Arbuse_weight
        minIndex = i
    if maxArbuse < Arbuse_weight:
        maxArbuse = Arbuse_weight
        maxIndex = i
print(f'Arbuse for tyosha with weight {minArbuse} is {minIndex + 1}-st')        
print(f'Arbuse for you with weight {maxArbuse} is {maxIndex + 1}-st')        
    

# A = int(input("value A: "))
# result = -1
# if A < 2 and A >=0 :
#     result = A
# else:
#     counter = 3
#     flag = True
#     fib1 = 1
#     fib2 = 1
#     while flag:
#         (fib1,fib2) = (fib2, fib2 + fib1)
#         print(fib2)
#         if fib2 == A:
#             result = counter
#             flag = False
#         elif fib2 > A:
#             flag = False
#         else:
#             counter += 1
# if result == -1:
#     print(f'{A} is not fibonachi')
# else:
#     print(f'{A} is fibonachi number {result}')
        


## factorial(N)
# N = int(input("value N: "))
# result = 1
# for i in range(2, N + 1):
#     result *= i
# print(f'{N}! = {result}')
