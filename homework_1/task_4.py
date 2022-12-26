## 4 ##

number = input('Введите целое положительное число: ')
maximum = int(number[0])
count = 0
while count < len(number):
    if int(number[count]) > maximum:
        maximum = int(number[count])
    count = count + 1
print(maximum)