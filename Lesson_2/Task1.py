# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.
elements = [2021, 'New Year!', 3.14, True, [1, 2, 3], tuple('Hello'), {'car': 'BMW', 'color': 'red'}, {4, 5, 4}]
for element in elements:
    print(type(element))
