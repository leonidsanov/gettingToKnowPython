# Найти максимальное из пяти чисел

max = 0
i = 1
while i <= 5:
    num = int(input())
    if num > max:
        max = num
    i += 1
print(max)