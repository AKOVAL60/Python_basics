# Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа
# x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной
# функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):  # VARIANT 1 #
    return x ** y


print(my_func(5, -3))


def my_func_cycle(x, y):  # VARIANT 2 #
    result = x
    for i in range(1, abs(y)):
        result *= x
    return 1 / result


print(my_func_cycle(5, -3))
