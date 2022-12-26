# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# Решение через LIST
myList = list(['Зима', 'Весна', 'Лето', 'Осень'])
monthNumber = int(input('Введите месяц в виде целого числа от 1 до 12: '))

while True:
    if monthNumber < 1 or monthNumber > 12:
        monthNumber = int(input('Неверный диапазон! Введите целое число от 1 до 12: '))
    else:
        break

print(myList[int(monthNumber / 3) - 4])

# Решение через DICT
myDict = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for key in myDict.keys():
    if monthNumber in myDict[key]:
        print(key)
