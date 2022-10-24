# функция добавления данных в файл
def append_data(fileName, data):
    with open(fileName, 'a') as file:
        file.write(f'{data};\n')

# функция чтения данных из файла
def read_data(fileName):
    with open(fileName, 'r') as file:
        info = file.read().split(';')
    return info