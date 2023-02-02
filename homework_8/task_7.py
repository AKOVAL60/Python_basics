# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
# комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class CNumber():

    def __init__(self, r_part, i_part):
        self.r_part = float(r_part)
        self.i_part = float(i_part)

    def __add__(self, other):
        return CNumber(self.r_part + other.r_part, self.i_part + other.i_part)

    def __mul__(self, other):
        return CNumber(self.r_part * other.r_part - self.i_part * other.i_part, self.r_part * other.i_part
                       + self.i_part * other.r_part)

    def __str__(self):
        return (f'({self.r_part if self.r_part != int(self.r_part) else int(self.r_part)}'
                f'{"" if self.i_part < 0 else "+"}{self.i_part if self.i_part != int(self.i_part) else int(self.i_part)})')

print('Проверка сложения:')
print(CNumber(2, 12) + CNumber(1, 7), end='\n\n')

print(CNumber(3, 6) + CNumber(35, -65), end='\n\n')

print(CNumber(3.14, 6.18) + CNumber(35.24, -64.355), end='\n\n')

print('Проверка умножения:')
print(CNumber(2, 12) * CNumber(1, 7), end='\n\n')

print(CNumber(3, 6) * CNumber(35, -65), end='\n\n')

print(CNumber(3.14, 6.18) * CNumber(35.24, -64.355), end='\n\n')