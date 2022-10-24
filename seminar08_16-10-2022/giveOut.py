# модуль выдачи всей имеющейся информации
from createFiles import read_data

def giveOutInformation():
    list_data = read_data('nameID.csv')
    list_data += read_data('phone.csv')
    list_data += read_data('post.csv')
    for i in list_data:
        print(i)