# Упражнение 8. Сувениры и безделушки
# Интернет-магазин занимается продажей различных сувениров и безделушек.
# Каждый сувенир весит 75 г, а безделушка – 112 г. Напишите программу,
# запрашивающую у пользователя количество тех и других покупок,
# после чего выведите на экран общий вес посылки.

souvenirWeight = 75
trinketWeight = 112
souvenir = int(input('Количество сувениров: '))
trinket = int(input('Количество безделушек: '))
packageWeight = souvenir * souvenirWeight + trinket * trinketWeight
print(f'Общий вес посылки {packageWeight} грамм')