# a = [0] * 5
# print(a)

my_text = input('Введите текст: ')
my_text = my_text.replace(',',' ')
my_text = my_text.replace('.',' ')
my_text = my_text.replace('-',' ')
my_text = my_text.replace(')',' ')
my_text = my_text.replace('(',' ')
test_words = my_text.split(' ')
print(len(test_words))
print(len(set(test_words)))