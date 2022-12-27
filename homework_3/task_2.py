# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

# firstname = input('Введите имя: ')
# lastname = input('Введите фамилию: ')
# year = input('Введите год рождения: ')
# city = input('Введите город: ')
# email = input('Введите электронную почту: ')
# phone = input('Введите номер телефона: ')


def my_func(firstname, lastname, year, city, email, phone):
    return ' '.join([firstname, lastname, year, city, email, phone])


print(my_func(firstname='Александр', lastname='Коваль', year='1962',
              city='Калининград', email='koval@mdx39.ru', phone='89998887766'))
