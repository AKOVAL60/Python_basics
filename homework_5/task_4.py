# 4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Напишите
# программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_dict = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}

with open("task_4.txt", "r", encoding="utf-8") as my_file:
    content = [item for item in my_file]
    with open("task_4_res.txt", "w", encoding="utf-8") as f_obj:
        print("".join(line.replace(line.split()[0], my_dict[int(line.split()[2])]) for line in content), file=f_obj)
