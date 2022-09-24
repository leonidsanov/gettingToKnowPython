# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

#num = int (input('insert number'))

#Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

num = int (input("Insert number:"))
if ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and not num % 30 == 0:
    print('True')
else:
    print('False')

# Variant 2
if ((n % 5 == 0 and n % 10 == 0) or (n % 15 == 0)) and not n % 30 == 0:
    print("Да")
else: print("Нет")

