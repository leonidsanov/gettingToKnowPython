# Telephone directory
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
1) Вывод всего справочника
2) Добавление нового номера
3) Поиск по номеру
4) Удаление номера* (необязательно)

Проект состоит из следующих модулей:

`userInterface` модуль взаимодействия с пользователем. Запрашивает имя, фамилию и номер телефона

`createFile` модуль создаия файла, записи данных в файл и вывода данных телефонной книги

`seach` модуль поиска по всему справочнику

При запуске `main` программа запрашивает имя, фамилию и номер телефона, затем записывает данные в файлы txt и csv.
Затем выводит на экран всё содержимое этих файлов. Затем программа просит ввести поисковый запрос. Если найдено совпадение по фамилии, имени или номеру телефона,
то программа выводит на экран всю строку. 