# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
from itertools import cycle
from time import sleep


class TrafficLight:
    def __init__(self):
        self.__colors = ['red', 'yellow', 'green']

    def running(self):
        print('Запуск')
        for color in cycle(self.__colors):
            print(color)
            if color == 'yellow':
                sleep(2)
            else:
                sleep(7)


traffic_light = TrafficLight()
traffic_light.running()
