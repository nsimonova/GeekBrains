# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
f_obj = open('Task3_Other.txt')
text = f_obj.readlines()
sum_salary = 0
print("Сотрудники с зарплатой ниже 20000:")
for line in text:
    surname = line.split()[0]
    salary = int(line.split()[1])
    sum_salary = sum_salary + salary
    if salary < 20000:
        print(f'{surname} {salary}')
average_salary = sum_salary / len(text)
print(f'Средняя зарплата сотрудников {average_salary}')
f_obj.close()
