# 2) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = int(input("Enter number: "))

i = 2 # первое простое число

list01 = []

old = num

while i <= num:

    if num % i == 0:

        list01.append(i)

        num //= i

        i = 2

    else:

        i += 1

print(f"Простые множители числа {old} приведены в списке: {list01}")