
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import os

currentDirectory = os.getcwd()

inputFile = open(currentDirectory + '\\5\\text1.txt',encoding='utf-8')
newFile = open(currentDirectory + '\\5\\result1.txt',"w",encoding='utf-8')

result = ""
print('text from file:')
for line in inputFile:
    print(line)
    newline = line.replace("абв","")
    newFile.write(newline)
newFile.close()
print(f'Результат записан в файл result1.txt')
