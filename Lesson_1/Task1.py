# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
userName = input("Привет! Как тебя зовут? ")
print('Добро пожаловать, ' + userName)
print('Эта программа решает уравнение линейного типа ax+b=0')
a = int(input('Введите значение a '))
b = int(input('Введите значение b '))
x = (-b / a)
print('Решение уравнения: x=%s' % x)
