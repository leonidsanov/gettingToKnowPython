# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 67,82 -> 23
# - 0,56 -> 11

# floatNum = input('Введите вещественное число: ')
# sum = 0
#
# for i in range(len(floatNum)):
#     if floatNum[i] != ',' and floatNum[i] != '.' and floatNum[i] != '-':
#         sum += int(floatNum[i])
#
# print(f'Сумма цифр в вещественном числе равна: {sum}')

# Попробуем обернуть в функцию
floatNum = input('Введите вещественное число: ')


def sumFloat(x):
    sum = 0
    for i in range(len(x)):
        if x[i] != ',' and x[i] != '.' and x[i] != '-':
            sum += int(x[i])
    return sum

y = sumFloat(floatNum)

print(f'Сумма цифр в вещественном числе равна: {y}')
