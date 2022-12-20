## 1 ##

a = input('Введите число "a": ')
b = input('Введите число "b": ')
c = input('Введите число "c": ')

print(f"a:{a}\r\nb:{b}\r\nc:{c}")

## 2 ##

seconds = int(input('Введите время в секундах: '))

if int(seconds / 60 / 60) <= 9:
    times = '0' + str(int(seconds / 60 / 60))
else:
    times = str(int(seconds / 60 / 60))

if int((seconds / 60) % 60) <= 9:
    times += ':0' + str(int((seconds / 60) % 60))
else:
    times += ':' + str(int((seconds / 60) % 60))

if int(seconds % 60) <= 9:
    times += ':0' + str(int(seconds % 60))
else:
    times += ':' + str(int(seconds % 60))
print(times)

## 3 ##

n = input('Введите число "n": ')
print(f"n + nn + nnn = {int(n) + int(n + n) + int(n + n + n)}")

## 4 ##

number = input('Введите целое положительное число: ')
maximum = int(number[0])
count = 0
while count < len(number):
    if int(number[count]) > maximum:
        maximum = int(number[count])
    count = count + 1
print(maximum)

## 5 , 6 ##

debit = int(input('Введите доходы: '))
credit = int(input('Введите расходы: '))
profit = debit - credit

if profit > 0:
    print('Выручка больше расходов')
    numEmployes = int(input('Введите количество сотрудников в фирме: '))
    print(f"На {numEmployes} сотрудников общая прибыль равна {profit}")
    print(f"На каждого сотрудника приходится 1/{numEmployes} прибыли в размере {profit / numEmployes:.2f}")
elif profit == 0:
    print('Выручка равна расходам')
else:
    print('Выручка меньше доходов')

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

## Send homework_1 to github