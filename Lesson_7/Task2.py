# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
# существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self, x):
        pass


class Coat(Clothes):
    def fabric_consumption(self, x):
        result = x / 6.5 + 0.5
        return result


class Costume(Clothes):
    def fabric_consumption(self, x):
        result = 2 * x + 0.3
        return result

    @property
    def color(self):
        return 'red'


coat = Coat('Пальто')
print(coat.name)
print(coat.fabric_consumption(5))

costume = Costume('Костюм')
print(costume.name)
print(costume.fabric_consumption(3))
print(costume.color)
