# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат. 5. Реализовать класс Stationery (канцелярская принадлежность). определить в
# нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»; создать три
# дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать переопределение метода
# draw. Для каждого класса метод должен выводить уникальное сообщение; создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str
    message = "Запуск отрисовки"

    def draw(self):
        print(self.message)


class Pen(Stationery):
    title = "ручка"
    message = f"в левом кармане у нас - {title}"


class Pencil(Stationery):
    title = "карандаш"
    message = f"в среднем кармане у нас - {title}"


class Handle(Stationery):
    title = "маркер"
    message = f"в нагрудном кармане у нас - {title}"


draw_list = [
    Stationery(),
    Pencil(),
    Handle(),
    Pen()
]

for element in draw_list:
    element.draw()

draw_list[0].message = "Новый год наступил"
draw_list[1].message = "Прогулка, очень хорошее и полезное занятие"
draw_list[2].title = "топор"
draw_list[2].message = f"Если колоть дрова, то лучше взять {draw_list[2].title}"
print()

for element in draw_list:
    element.draw()
