# Упражнение 4. Площадь садового участка
# Создайте программу, запрашивающую у пользователя длину и ширину
# садового участка в метрах. Выведите на экран площадь участка в арах.

length = float(input('Enter the length of the garden plot in meters: '))
width = float(input('Enter the width of the garden plot in meters: '))
area = (length * width) / 100
print(f'The Area of the garden plot {area} ar')