# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Date:
    _day: int
    _month: int
    _year: int

    def __init__(self, date_str: str):
        values = Date.convert(date_str)
        self.validate_values(values)
        self._day, self._month, self._year = values

    def __str__(self):
        return f"День: {self._day}\nМесяц: {self._month}\nГод: {self._year}"

    @classmethod
    def convert(cls, date_str: str):
        return [int(value) for value in date_str.split("-")]

    @staticmethod
    def validate_values(values: list):
        day, month, year = values
        assert 1 <= day <= 31, 'Дни вышли за диапазон, Введите корректное число'
        assert 1 <= month <= 12, 'Месяцы вышли за диапазон, Введите корректный месяц'
        assert 1970 <= year <= 2100, 'Года вышли за диапазон, Введите корректный год'


date1 = Date("22-02-2002")
print(date1)
print()
date2 = Date("32-12-2112")  # AssertionError: Дни вышли за диапазон, Введите корректное число
print(date2)
