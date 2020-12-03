# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
f_obj = open('Task2_other.txt')
text = f_obj.readlines()
for i, line in enumerate(text, 1):
    print(f'Количество слов в {i} строке {len(line.split())}')

print(f'Количество строк {len(text)}')
f_obj.close()
