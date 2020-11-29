# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def exponentiation(x, y):
    answer = x ** y
    return answer


def exponentiation_with_cycle(x, y):
    number = 1
    z = x
    while number < abs(y):
        z = z * x
        number = number + 1
    if y > 0:
        answer = z
    elif y < 0:
        answer = 1 / z
    else:
        answer = 1
    return answer


try:
    a = float(input('Введите действительное положительное число '))
    if a <= 0:
        print('Нельзя отрицательное число и 0!')
    else:
        b = int(input('Введите отрицательное число '))
        if b >= 0:
            print('Нельзя положительное число и 0!')
        else:
            print(exponentiation(a, b))
            print(exponentiation_with_cycle(a, b))
except ValueError:
    print('Введены не корректные данные!')
