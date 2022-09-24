# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

quarterNumber = int(input('Введите номер четверти: '))
if quarterNumber == 1:
    print('x > 0 and y > 0')
elif quarterNumber == 2:
    print('x > 0 and y < 0')
elif quarterNumber == 3:
    print('x < 0 and y < 0')
elif quarterNumber == 4:
    print('x < 0 and y > 0')
else:
    print('Введите целое число от 1 до 4')