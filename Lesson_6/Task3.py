# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


manager = Position('Иван', 'Котов', 'менеджер', 40000, 10000)
print(manager.name)
print(manager.surname)
print(manager.position)
print(manager._income)
print(manager.get_full_name())
print(manager.get_total_income())

economist = Position('Инна', 'Носова', 'экономист', 30000, 5000)
print(economist.name)
print(economist.surname)
print(economist.position)
print(economist._income)
print(economist.get_full_name())
print(economist.get_total_income())
