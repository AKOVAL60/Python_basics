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