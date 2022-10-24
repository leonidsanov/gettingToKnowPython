# Модуль взаимодействия с пользователем
# Импорт модулей
from dataEntry import *
from createFiles import *
from giveOut import giveOutInformation
from employeeSearch import data_search_csv


# функция выбора действия
def request():
    while True:
        print(f'Выберите запрос:\nЕсли Вы хотите ввести новую информацию нажмите 1\nЕсли вы хотите вывести всю информацию нажмите 2\nЕсли вы хотите найти конкретные данные нажмите 3\nЗакрыть БД 4')
        user_request = input('Введите цифру: ')
        if user_request == '1':
            data_pers = entryName()
            append_data('nameID.csv', data_pers)

            data_pers = entryPN()
            append_data('phone.csv', data_pers)

            data_pers = entryPost()
            append_data('post.csv', data_pers)
        elif user_request == '2':
            giveOutInformation()
        elif user_request == '3':
            data_search_csv()
        elif user_request == '4':
            print('База данных закрыта')
            exit()
