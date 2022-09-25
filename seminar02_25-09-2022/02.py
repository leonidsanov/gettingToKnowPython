# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# sec = int(input('Введите время в секундах: '))
# hours = 0
# minutes = 0
# seconds = 0
#
# hours = (sec // 60) // 60
# minutes = sec // 60 - hours * 60
# seconds = sec % 100 - minutes * 60
#
# print(f'{hours} : {minutes} : {seconds}')

# # 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# # Используйте форматирование строк. 3661
# import datetime
# sec = 3661
# minute = sec % 60
# sec1 = minute % 60
# hour = int(sec/3600)  # 1 hour
# timeobj = datetime.time(hour, minute, sec1)
# print(timeobj)
#
# next variant
my_time = int(input('Введите время в секундах: '))

hours = my_time//3600
minutes = (my_time % 3600) // 60
seconds = my_time % 60

print(f'{hours}:{minutes}:{seconds}')
