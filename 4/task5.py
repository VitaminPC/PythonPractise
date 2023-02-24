from random import randint
from Equation import CreateEquation

def CreateDic(strEquation):
    if str(strEquation)[0:1] == "-x":
        strEquation = '-1'+strEquation[1:]
    if str(strEquation)[0] == "x":
        strEquation = '1'+strEquation
    ForSplit = strEquation.replace(' + ',' +').replace(" - ", " -").replace('+x', '+1x').replace('-x', '-1x')
    Elements = ForSplit.split(' ')
    result = {}
    for Elem in Elements:
        if Elem.find("x**") > -1:
            Para = Elem.split('x**')
            result[int(Para[1])] = int(Para[0].replace('+',''))
        elif Elem.find("x") > -1:
            result[1] = int(Elem.replace('x','').replace('+',''))
        else:
            result[0] = int(Elem.replace('+',''))
    return result

def ElemOfSetsWithoutError(myDict, Key):          
    if Key in myDict:
        return myDict[Key]
    return 0

    
N = int(input('Введите степень первого многочлена: '))
Koefficients = [randint(-10, 10) for i in range(N+1)]
firstEquation = CreateEquation(Koefficients)
print(firstEquation)

N = int(input('Введите степень второго многочлена: '))
Koefficients = [randint(-10, 10) for i in range(N+1)]
secondEquation = CreateEquation(Koefficients)
print(secondEquation)


firstElems = CreateDic(firstEquation)
secondElems = CreateDic(secondEquation)
# print(firstElems)
# print(secondElems)

MaxPower = max(max(firstElems.keys()), max(secondElems.keys()))

newKoefficients = [0] * (MaxPower + 1)
for i in range(MaxPower + 1):
    newKoefficients[i] = ElemOfSetsWithoutError(firstElems, i) + ElemOfSetsWithoutError(secondElems, i)
    
FinalEquation = CreateEquation(newKoefficients)
print()
print('Сумма многочленов = ', FinalEquation)    