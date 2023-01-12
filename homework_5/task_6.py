# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие
# лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий. Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) — Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

my_dict = {}


def int_parse(word):
    num = []
    try:
        for el in word:
            if el.isdigit():
                num.append(el)
        return int("".join(num))
    except ValueError:
        return 0


def summary(line):
    result = 0
    for el in line:
        result += int_parse(el)
    return result


with open('task_6.txt', 'r', encoding="utf-8") as init_f:
    for lines in init_f:
        params = lines.split()
        my_dict[params[0]] = summary(params)
    print(f'Словарь:\n {my_dict}')
