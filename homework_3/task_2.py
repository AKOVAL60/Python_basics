# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('Введите электронную почту: ')
phone = input('Введите номер телефона: ')


def profiles(*args):
    params = []
    for val in args:
        params.append(val)
    return ' '.join(params)


profileInfo = profiles(name, surname, year, city, email, phone)
print(profileInfo)
