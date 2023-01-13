# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.

# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"Автомобиль {self.name} начинает движение")

    def stop(self):
        print(f"Автомобиль {self.name} останавливается")

    def turn(self, direction):
        print(f"Автомобиль {self.name} поворачивает {direction}")

    def show_speed(self):
        print(f"\033[0mАвтомобиль: {self.name} | Цвет: {self.color}\033[0m | Скорость: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('\033[31mСкорость превышена! \033[32mСбавьте скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('\033[31mСкорость превышена! \033[32mСбавьте скорость!')


class PoliceCar(Car):
    def show_speed(self):
        print('\033[34mПолицеская Машина')
        super().show_speed()


car_list = [
    SportCar(200, '\033[31mRED', 'Chevrolet'),
    PoliceCar(160, '\033[34mBLUE', 'Toyota'),
    TownCar(120, '\033[0mWHITE', 'Opel'),
    SportCar(90, '\033[37mSILVER', 'Volkswagen'),
    WorkCar(50, '\033[30mBLACK', 'Nissan'),
    TownCar(100, '\033[33mYELLOW', 'Toyota'),
    PoliceCar(100, '\033[34mBLUE', 'Mercedes'),
]

car_list[0].go()
car_list[0].turn("налево")
car_list[1].turn("направо")
car_list[0].stop()
car_list[2].go()
print()

print(car_list[len(car_list) - 1].speed)

for car in car_list:
    car.show_speed()
    print()
