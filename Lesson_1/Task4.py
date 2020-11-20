# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции
number = (input('Введите число '))
maximum = 0
i = 0
while i < len(number):
    if int(number[i]) > maximum:
        maximum = int(number[i])
    i = i + 1
print('Максимум: %s' % maximum)
