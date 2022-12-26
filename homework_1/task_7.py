## 7 ##

a = int(input('Введите результат первого дня (км): '))
b = int(input('Введите желаемое расстояние (км): '))
count = 1

while True:
    print(f"{count}-й день: {a:.2f}")
    if a >= b:
        break
    a = a * 1.1
    count = count + 1

print(f"на {count}-й день спортсмен достиг результата — не менее {b} км.")