#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import os

currentDirectory = os.getcwd()

operation = int(input('Что Вы хотите сделать?(0-упаковать, 1-распаковать):'))

if operation == 0:
    inputFile = open(currentDirectory + '\\5\\origin.txt',encoding='utf-8')
    outputFile = open(currentDirectory + '\\5\\packed.txt',"w",encoding='utf-8')
    for line in inputFile:
        print(line)
        newline = ""
        current = ''
        count = 1
        i = 0
        while i < len(line):
            if line[i] != current:
                if current != '':
                    newline += str(count) + current
            count = 1
            current = line[i]
            i += 1
            while i < len(line) and line[i] == current:
                i += 1
                count += 1
                
        outputFile.write(newline + '\n')
    outputFile.close()
    print(f'Результат записан в файл packed.txt')
elif operation == 1:
    inputFile = open(currentDirectory + '\\5\\packed.txt',encoding='utf-8')
    outputFile = open(currentDirectory + '\\5\\unpacked.txt',"w",encoding='utf-8')
    for line in inputFile:
        print(line)
        newline = ''
        i = 0
        for i in range(0,len(line)-1,2):
            count = int(line[i])
            current = line[i+1]
            newline += current * count
        outputFile.write(newline + '\n')
    outputFile.close()
    print(f'Результат записан в файл unpacked.txt')