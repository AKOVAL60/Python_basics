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