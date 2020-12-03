# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f_obj = open('Task1_other.txt', 'w')
while True:
    a = input('Write the phrase in english ')
    if a == '':
        break
    f_obj.write(a + '\n')
f_obj.close()
