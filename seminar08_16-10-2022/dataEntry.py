# модуль ввода данных
import datetime
# функция ввода имени и фамилии с присвоением ID
def entryName():
    id_pers = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    name = input('Имя: ')
    surname = input('Фамилия: ')
    return f'{id_pers};{name};{surname};'

# функция ввода номера телефона
def entryPN():
    phone = input('Номер телефона: ')
    return f'{phone};'

# функция ввода должности
def entryPost():
    pers_post = input('Должность: ')
    return f'{pers_post};'