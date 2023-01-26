# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    _name_type: str

    def __init__(self, name_type: str):
        self._name_type = name_type

    @property
    @abstractmethod
    def calculate(self):
        return float
        pass


class Coat(Clothes):
    _size: float

    def __init__(self, name_type: str, size):
        super().__init__(name_type)
        self._size = size

    @property
    def calculate(self):
        return float('{:.3f}'.format(self._size / 6.5 + 0.5))


class Suit(Clothes):
    _size: float

    def __init__(self, name_type: str, size):
        super().__init__(name_type)
        self._size = size

    @property
    def calculate(self):
        return float('{:.3f}'.format(2 * self._size + 0.3))


coat_1 = Coat("Пальто", 42)
suit_1 = Suit("Пиджак", 42)

print(f"{coat_1.calculate} + {suit_1.calculate} = {coat_1.calculate + suit_1.calculate}")


