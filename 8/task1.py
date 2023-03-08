import os


def menu():
    punkt = '1'
    telefones = list()
    while punkt != '0':
        print('0 - Выход')
        print('1 - Загрузить')
        print('2 - Сохранить')
        print('3 - Добавить')
        print('4 - Удалить')
        print('5 - Найти по подстроке')
        print('6 - Показать')
        punkt = input('Выберите действие:')
        if punkt == '1':
            load(telefones)
        elif punkt == '2':
            save(telefones)
        elif punkt == '3':
            add(telefones)
        elif punkt == '4':
            telefones  = delete(telefones)
        elif punkt == '5':
            find(telefones)
        elif punkt == '6':
            show(telefones)
        elif punkt == '0':
            print('Досвидания!')


def load(telefones):
    currentDirectory = os.getcwd()
    telefones.clear()
    inputFile = open(currentDirectory + '\\8\\list.txt', encoding='utf-8')
    for line in inputFile:
        elems = line.split(';')
        record = dict()
        record['family'] = elems[0].strip()
        record['name'] = elems[1].strip()
        record['fathername'] = elems[2].strip()
        record['phone'] = elems[3].strip()
        record['index'] = elems[0].strip()+elems[1].strip()+elems[2].strip()
        telefones.append(record)
    inputFile.close()


def save(telefones):
    if len(telefones) == 0:
        print('Nothing to write.')
        return
    currentDirectory = os.getcwd()
    OutputFile = open(currentDirectory + '\\8\\list.txt',
                      'w', encoding='utf-8')
    for record in telefones:
        line = record['family'].strip() + ';' + record['name'].strip() + \
            ';' + record['fathername'].strip() + ';' + record['phone'].strip()
        OutputFile.write(line+'\n')
    OutputFile.close()


def add(telefones):
    names = input('Введите фамилие имя и отчество: ').split(' ')
    phone = input('Введите номер телефона: ')

    if len(names) < 3 or len(phone) == 0:
        print('Введите корректные значения.')
        return
    record = dict()
    record['family'] = names[0].strip()
    record['name'] = names[1].strip()
    record['fathername'] = names[2].strip()
    record['phone'] = phone.strip()
    record['index'] = names[0].strip()+names[1].strip()+names[2].strip()
    telefones.append(record)


def findByName(telefones, name):
    indexes = list()
    if len(telefones) == 0:
        return indexes
    indexes = [i for i in range(len(telefones)) if telefones[i]['index'].find(name) > -1]
    return indexes

def delete(telefones):
    names = input(
        'Введите фамилие имя и отчество удаляемой записи: ').split(' ')
    if len(names) < 1:
        print('Введите корректные значения.')
        return
    searchKey = names[0].strip()
    if len(names) > 1:
        searchKey += names[1].strip()
    if len(names) > 2:
        searchKey += names[2].strip()
    indexes = findByName(telefones, searchKey)
    newList = [telefones[i] for i in range(len(telefones)) if not i in indexes]
    return newList

def find(telefones):
    names = input(
        'Введите фамилие имя и отчество или подстроку для поиска: ').split(' ')
    if len(names) < 1:
        print('Введите корректные значения.')
        return
    searchKey = names[0].strip()
    if len(names) > 1:
        searchKey += names[1].strip()
    if len(names) > 2:
        searchKey += names[2].strip()
    indexes = findByName(telefones, searchKey)
    print()
    print('Найденные номера: ')
    print()
    for i in indexes:
        record = telefones[i]
        print(record['family'] + ' ' + record['name'] + ' ' +
              record['fathername'] + ' : ' + record['phone'], sep='\n')
    print()

def show(telefones):
    print()
    print('Справочник телефонов: ')
    print()
    for record in telefones:
        print(record['family'] + ' ' + record['name'] + ' ' +
              record['fathername'] + ' : ' + record['phone'], sep='\n')
    print()


def main():
    menu()


if __name__ == "__main__":
    main()
