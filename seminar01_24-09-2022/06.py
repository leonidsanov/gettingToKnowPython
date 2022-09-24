# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

num = int(input('Ведите число от 1 до 7 '))

if 1 <= num <= 5:
    print('Рабочий день')
elif 6 <= num <= 7:
    print('Выходной день')
else:
    print('Введите целое число от 1 до 7')


# Variant 2
count=0
num=input("enter number: ")
list=["понедельник","вторник","среда","четверг","пятница","суббота","воскресение"]
while count==0:            
    if num.isdigit()==True and int(num)<7 and not int(num)<1:
        if int(num)<6:
            #print("working day")
            print(f' День недели "{list[int(num)-1]}" является рабочим днем')
        else:
            print("weekend")  
        count=1
    
    else: 
        print("you entered not number or wrong number")
        num=input("enter number again: ")
