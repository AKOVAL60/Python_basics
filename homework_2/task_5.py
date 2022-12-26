# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
while True:
    inString = input('Введите элемент рейтинга (Press "+" to exit): ')
    if inString == "+":
        break
    rate = int(inString)
    maximum = my_list[0]
    minimum = my_list[0]
    for values in my_list:
        if values > maximum:
            maximum = values
        elif values < minimum:
            minimum = values
    count = my_list.count(rate)
    if count > 0:
        maxIndex = 0
        cnt = 0
        while cnt < count:
            maxIndex = my_list.index(rate, maxIndex)
            cnt += 1
        my_list.insert(maxIndex, rate)
    else:
        idx = 0
        for counter, values in enumerate(my_list):
            if rate > values:
                idx = counter
                break
        if rate > maximum:
            my_list.insert(my_list.index(maximum), rate)
        elif rate < minimum:
            my_list.insert(len(my_list), rate)
        else:
            my_list.insert(idx, rate)
    print(my_list)
