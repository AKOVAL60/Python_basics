# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных будет свидетельствовать пустая строка.

# Вариант решения через методы открытия\записи\чтения\закрытия файла
my_file = open("task_1.txt", "w", encoding="utf-8")
while True:
    line = input("Введите текст: ")
    if not line:
        print("\nПустой ввод. Производится выход из программы")
        break
    my_file.write(f"{line}\n")
my_file.close()
my_file = open("task_1.txt", "r", encoding="utf-8")
content = my_file.read()
print(f"{content}")
my_file.close()

# Вариант решения через методы контекста

with open("task_1_ctx_mgr.txt", "w+", encoding="utf-8") as my_f:
    while True:
        line = input("Введите текст: ")
        if not line:
            print("\nПустой ввод. Производится выход из программы")
            break
        my_f.write(line + "\n")
    my_f.seek(0)
    print(my_f.read())
