# модуль поиска по совпадениям
from createFiles import read_data

def data_search_csv():
    strSeach = input('Введите поисковый запрос: ')

    list_data = read_data('nameID.csv')
    list_data += read_data('phone.csv')
    list_data += read_data('post.csv')
    for line in list_data:
        line = line.split(';')
        if strSeach in line:
            return print(line)
    return print('не найдено')