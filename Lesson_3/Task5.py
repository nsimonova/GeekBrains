
# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
# добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.
print('Программа сумиирует числа \nДля выхода нажмите"Q"')
number_sum = 0
while True:
    number = input('Введите числа,разделенные пробелами ')
    if number.upper() == 'Q':
        break
    number = sum(map(int, number.split()))
    number_sum = number_sum + number
    print(number_sum)
