# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

a = int(input("Введите значения выручки: "))
b = int(input("Введите значения издержек фирмы: "))
if a > b:
    print(f"Прибыль составила = {a - b}, рентабельность составила {(a - b) / a}")
    c = int(input("Введите кол-во сотрудников: "))
    print(f"Прибыль фирмы на одного сотрудника составила: {(a - b) / c}")
else:
    print("Убыток")
