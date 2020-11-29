# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def sum_max(x, y, z):
    return x + y + z - min(x, y, z)


first_number = int(input('Введите первое число '))
second_number = int(input('Введите второе число '))
third_number = int(input('Введите третье число '))

print(sum_max(first_number, second_number, third_number))
