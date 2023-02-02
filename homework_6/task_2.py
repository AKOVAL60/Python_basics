# 2. Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина); значения атрибутов должны
# передаваться при создании экземпляра класса; атрибуты сделать защищёнными; определить метод расчёта массы асфальта,
# необходимого для покрытия всей дороги; использовать формулу: длина*ширина*масса асфальта для покрытия одного кв.
# метра дороги асфальтом, толщиной в 1 см*число см толщины полотна; проверить работу метода. Например: 20 м*5000 м*25
# кг*5 см = 12500 т.

weight = 25
thickness = 5


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        # return self._width * self._length * 25 * 5

        # Если необходимо передавать определённые параметры
        # Объявление идёт в начале программы параметров веса и высоты
        return self._width * self._length * volume(weight, thickness)


def volume(w, t):
    return w * t


roads = [Road(2, 3), Road(4, 6), Road(6, 7), Road(5, 2), Road(3, 2)]
for el in roads:
    print(f"{el.calculate()} т.")