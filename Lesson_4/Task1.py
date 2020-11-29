# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами
from sys import argv

print('Program for calculating the salary of an employee')
work_time, salary_rate, bonus = argv[1:]
salary = (int(work_time) * int(salary_rate) + int(bonus))
print(f'The salary {salary}')
