# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

with open("task_2.txt") as my_file:
    print(f"В файле найдено {len(my_file.readlines())} строк")
    my_file.seek(0)
    for i, line in enumerate(my_file):
        print(f"Строка {i + 1}: Слов - {len(line.split())}")
