# поиск данных

def data_search_csv():
    strSeach = input('Введите поисковый запрос: ')
    phoneDirectoryCSV = open('phone_directory.csv', 'r')
    for line in phoneDirectoryCSV:
        line = line.split(';')
        if strSeach in line:
            return print(line)
    return print('не найдено')

# def data_search_txt():
#     strSeach = input('Введите поисковый запрос: ')
#     phoneDirectoryTXT = open('phone_directory.txt', 'r')
#     for line in phoneDirectoryTXT:
#         line = line.split(';')
#         if strSeach in line:
#             return print(line)
#     return print('не найдено')