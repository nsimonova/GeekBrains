# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Start driving')

    def stop(self):
        print('Stop driving')

    def turn(self, direction):
        print('Turn to ' + direction)

    def show_speed(self):
        print('Current speed ' + str(self.speed))


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Over speed')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Over speed')


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'black', 'Mazda', False)
work_car = WorkCar(45, 'yellow', 'CityCat', False)
sport_car = SportCar(190, 'red', 'Ferrari', False)
police_car = PoliceCar(85, 'white', 'Renault', True)
cars = [town_car, work_car, sport_car, police_car]
for car in cars:
    print(car.speed)
    print(car.color)
    print(car.name)
    print(car.is_police)
    car.go()
    car.stop()
    car.turn('left')
    car.show_speed()
