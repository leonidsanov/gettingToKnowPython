# 5) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(x):
    if x in [1, 2]:
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)

def NegaFibonacci(y):
    if y == 1:
        return 1
    elif y == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, y):
            num1, num2 = num2, num1 - num2
        return num2

list01 = [0]

userNumber = int(input('Enter any number: '))

for e in range(1, userNumber + 1):

    list01.append(Fibonacci(e))

    list01.insert(0, NegaFibonacci(e))

print(list01)