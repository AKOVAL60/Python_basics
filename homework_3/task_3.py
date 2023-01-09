# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(*args):
    arr = sorted(args)
    arr.reverse()
    if len(arr) >= 2:
        return arr[0] + arr[1]
    else:
        return 'Недостаточно аргументов, необходимо не менее двух'


print(my_func(6, 3, 23, 7, 4, 2))
