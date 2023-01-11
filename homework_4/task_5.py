# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов
# списка. Подсказка: использовать функцию reduce().
from functools import reduce


def reduce_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el


print(f"Генератор 100-1000: {[el for el in range(100, 1001) if el % 2 == 0]}")
print(f"reduce(reduce_func): {reduce(reduce_func, [el for el in range(100, 1001) if el % 2 == 0])}")
