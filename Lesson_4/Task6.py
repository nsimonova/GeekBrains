# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle

number_start = int(input("Введите стартовое число "))
for x in count(number_start):
    print(x)
    if x >= 10:
        print('The end')
        break
print('=================================================================================')
my_list = ['Каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']
index = 0
for name in cycle(my_list):
    print(name)
    index = index + 1
    if index > 20:
        print('The end')
        break
