# создание файлов csv и txt и запись в них данных

from userInterface import dataRequest as dR

info = dR()

def create_fileCSV():
    with open('phone_directory.csv', 'a') as phoneDirectoryCSV:
        phoneDirectoryCSV.write(f'{info[0]};{info[1]};{info[2]}\n')

def create_fileTXT():
    with open('phone_directory.txt', 'a') as phoneDirectoryTXT:
        phoneDirectoryTXT.write(f'{info[0]};{info[1]};{info[2]}\n')

def data_output_csv():
    phoneDirectoryCSV = open('phone_directory.csv', 'r')
    for line in phoneDirectoryCSV:
        print(line)
    phoneDirectoryCSV.close()

def data_output_txt():
    phoneDirectoryTXT = open('phone_directory.txt', 'r')
    for line in phoneDirectoryTXT:
        print(line)
    phoneDirectoryTXT.close()
