# 3. Реализовать базовый класс Worker (работник). определить атрибуты: name, surname, position (должность),
# income (доход); последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}; создать класс Position (должность) на базе класса Worker; в
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (
# get_total_income); проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


user_1 = Position('Иван', 'Иванов', 'Manager', 25000, 30000)
print(f"{user_1.get_full_name()} | {user_1.position} | income: {user_1.get_total_income()}")

user_2 = Position('Петр', 'Петров', 'Developer', 100000, 50000)
print(f"{user_2.get_full_name()} | {user_2.position} | income: {user_2.get_total_income()}")
