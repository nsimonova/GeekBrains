# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

with open('Task7_other.txt', encoding='utf-8') as f_obj:
    all_profit = 0
    count_firms = 0
    all_firms = dict()
    for line in f_obj:
        elements = line.split()
        profit = int(elements[2]) - int(elements[3])
        all_firms[elements[0]] = profit
        if profit > 0:
            all_profit = all_profit + profit
            count_firms = count_firms + 1
    average_profit = {'average_profit': all_profit / count_firms}
    result = [all_firms, average_profit]
    with open('Task7_my_file.json', 'w') as json_file:
        json.dump(result, json_file)
