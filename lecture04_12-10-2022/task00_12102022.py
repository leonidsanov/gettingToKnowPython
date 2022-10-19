# Задача 0. Сложить 2 числа

sum = lambda a, b: a + b

x = int(input('x = '))
y = int(input('y = '))

print(f'{x} + {y} = {sum(x, y)}')