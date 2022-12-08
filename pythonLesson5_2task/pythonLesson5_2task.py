# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


pathCandies = "./pythonLesson5_2task/candies.txt"
pathPlayer1 = "./pythonLesson5_2task/fisrt_player_canides.txt"
pathPlayer2 = "./pythonLesson5_2task/second_player_candies.txt"



def step(candies, pathCandies, pathPlayer):
    with open(pathPlayer, "r+") as read:
        player_candis = int(read.read())
    limit = 28
    if candies < limit:
        limit = candies    
    try:
        candie = int(input("Какое колличество конфеты вы хотите забрать: "))
        while 1 > candie or candie > limit:
            print(f"Общие колличество конфет уменьшилось до {candies}") if candie > limit else "" # доработать
            candie = int(input("Какое колличество конфеты вы хотите забрать: "))
    except:
        print(f"Значение дожлны быть число от 1 до {limit}.")
        candie = int(input("Какое колличество конфеты вы хотите забрать: "))     
    with open(pathPlayer, "w") as data:          
        player_candis += candie
        candies -= candie
        data.write(str(player_candis))
    with open(pathCandies, "w") as data:
        data.write(str(candies)) 
    print(f"Количество конфет у игорка № 1: {player_candis}, всего конфет осталось {candies}" )     
    return candie


def lottery():
    player_1 = True
    player_2 = True
    while (player_1 and player_2):
        player_1  = random.choice([True, False])
        player_2  = random.choice([True, False])
    return {"Игрок 1":player_1,"Игрок 2": player_2}  

 





def game( pathCandies, pathPlayer1, pathPlayer2 ):
    init_game( pathCandies, pathPlayer1, pathPlayer2 )
    with open(pathCandies, "r+") as read:
         candies = int(read.read())          

    players = lottery()
    while candies > 0:     #вынести функционал под if в отдельну функцию или добавить в step
        with open(pathCandies, "r+") as read:
            candies = int(read.read())
        if players["Игрок 1"]:
            print("Ход игорка №1")
            st = step(candies, pathCandies, pathPlayer1 )
                     
            players["Игрок 1"] = False            
            
        else: 
            print("Ход игорка №2")
            st = step(candies,pathCandies, pathPlayer2)                    
            players["Игрок 1"] = True 
    print(candies)   





def init_game(pathCandies, pathPlayer1, pathPlayer2):
    candies = 100
    firstPlayerCandies = 0   
    secondPlayerCandies = 0     
    with open(pathCandies, "w") as gameCandies:
        gameCandies.write(str(candies))
    with open(pathPlayer1, "w") as player1Candies:
        player1Candies.write(str(secondPlayerCandies))
    with open(pathPlayer2, "w") as player2Candies:
        player2Candies.write(str(firstPlayerCandies))        



game(pathCandies, pathPlayer1, pathPlayer2)