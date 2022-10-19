# запрос у пользователя номера телефона, имени и фамилии абонента

def dataRequest():
    subscriberData = []
    name = input('Введите имя абонента: ')
    subscriberData.append(name)
    surname = input('Введите фамилию абонента: ')
    subscriberData.append(surname)
    phoneNumber = input('Введите номер телефона абонента: ')
    subscriberData.append(phoneNumber)
    return subscriberData

#print(dataRequest()[0])
