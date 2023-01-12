# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

filename = "task_5.txt"
numbers = input("Введите числа через пробел: ")
with open(filename, "w", encoding="utf-8") as my_file:
    my_file.write(numbers)


def summary():
    try:
        with open(filename, "r", encoding="utf-8") as f_obj:
            return print(f"Сумма: {sum(map(int, f_obj.readline().split()))}")
    except IOError:
        print(f"Ошибка: {IOError}")
    except ValueError:
        print(f"Чисел не найдено")


summary()
