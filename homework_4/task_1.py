# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в
# нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений
# необходимо запускать скрипт с параметрами.


from sys import argv

name, time, salary, bonus = argv

try:
    production = int(time)
    salary = int(salary)
    bonus = int(bonus)
    total = time * salary + bonus
    print(name)
    print(f'заработная плата сотрудника  {total}')
except ValueError:
    print('Не введены числа')
