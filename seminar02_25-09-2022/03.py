# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = input('Введите целое число: ')
number2 = number * 2
number3 = number * 3

print(f'{number} + {number2} + {number3} = {int(number) + int(number2) + int(number3)}')