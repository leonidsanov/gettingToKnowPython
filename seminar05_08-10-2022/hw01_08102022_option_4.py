# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Вариант 4. Два игрока. Глупый бот против бота наделённого "интеллектом".
import random

candies = 2021  # количество конфет

# Ход бота наделённого "интеллектом"
def botMove():
    if candies % 28 == 0:
        x = random.randint(1, 28)
    elif (candies - 1) % 28 == 0:
        x = (candies - 28 * (candies // 28))
    else:
        x = (candies - 28 * (candies // 28)) - 1
    return x

# жеребьёвка и ход игры
randNum = random.randint(1, 2)
if randNum == 1:
    player01 = random.randint(1, 28)
    print(f'Первым ходит глупый бот: {player01}')
    candies = candies - player01
    print(f'Осталось конфет: {candies}')
    while candies > 28:
        player02 = botMove()
        print(f'Ход бота наделённого "интеллектом": {player02}')
        candies = candies - player02
        print(f'Осталось конфет: {candies}')
        if candies <= 28:
            print('Победил глупый бот! Ему достаются все конфеты')
            break
        player01 = random.randint(1, 28)
        print(f'Ход глупого бота: {player01}')
        candies = candies - player01
        print(f'Осталось конфет: {candies}')
        if candies <= 28:
            print('Победил бот наделённый "интеллектом"! Ему достаются все конфеты')
            break
else:
    randNum == 2
    player02 = botMove()
    print(f'Первым ходит бот наделённый "интеллектом": {player02}')
    candies = candies - player02
    print(f'Осталось конфет: {candies}')
    while candies > 28:
        player01 = random.randint(1, 28)
        print(f'Ход глупого бота: {player01}')
        candies = candies - player01
        print(f'Осталось конфет: {candies}')
        if candies <= 28:
            print('Победил бот наделённый "интеллектом"! Ему достаются все конфеты')
            break
        player02 = botMove()
        print(f'Ход бота наделённого "интеллектом": {player02}')
        candies = candies - player02
        print(f'Осталось конфет: {candies}')
        if candies <= 28:
            print('Победил глупый бот! Ему достаются все конфеты')
            break
