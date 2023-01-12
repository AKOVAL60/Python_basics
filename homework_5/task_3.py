# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее
# 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить
# подсчёт средней величины дохода сотрудников. Пример файла:
#
# Иванов 23543.12
# Петров 13749.32


try:
    with open("task_3.txt", "r", encoding="utf-8") as my_file:
        content = my_file.readlines()
        employee_over = [line.split()[0] for line in content if float(line.split()[1]) < 20000]
        # Подсчёт средней зарплаты сотрудников с окладом менее 20 тысяч
        avg_less = sum([float(line.split()[1]) for line in content if float(line.split()[1]) < 20000]) / len(employee_over)
        # Подсчёт средней зарплаты всех сотрудников
        avg_all = sum([float(line.split()[1]) for line in content]) / len(content)

        print("\n".join(employee_over))
        print(f"\nСредняя величина дохода сотрудников с окладом менее 20 тысяч: {avg_less:.2f}")
        print(f"Средняя величина дохода всех сотрудников: {avg_all:.2f}")
except IOError:
    print(f"Возникла ошибка: {IOError}")

