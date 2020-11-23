# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = input("Введите номер месяца!")
try:
    month = int(month)
    if month < 0 or month > 12:
        print('Неверное значение месяца!')
    else:
        season_dict = {'1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна', '5': 'весна', '6': 'лето', '7': 'лето',
                       '8': 'лето',
                       '9': 'осень', '10': 'осень', '11': 'осень', '12': 'зима'}
        print(season_dict.get(str(month)))
        season_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень',
                       'зима']
        print(season_list[int(month) - 1])
except ValueError:
    print('Неверное значение месяца!')