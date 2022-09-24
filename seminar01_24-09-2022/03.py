# Вывести на экран числа от -N до N

num = int(input('Insert number:'))
for i in range(-num, num+1):
    print(i, end = '\n')
