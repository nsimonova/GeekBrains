# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
f_obj = open('Task4_other.txt')
numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
file_new = open('Task4_NEW.txt', 'w')
while True:
    text = f_obj.readline().split()
    if not text:
        break
    key = text[0]
    text[0] = numbers.get(key)
    file_new.write(' '.join(text) + '\n')
f_obj.close()
file_new.close()
