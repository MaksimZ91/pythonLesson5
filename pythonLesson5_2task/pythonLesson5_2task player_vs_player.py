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

def init_game(pathCandies, pathPlayer1, pathPlayer2):
    candies = 2021
    firstPlayerCandies = 0   
    secondPlayerCandies = 0     
    writer(pathCandies, candies)
    writer(pathPlayer1, firstPlayerCandies)
    writer(pathPlayer2, secondPlayerCandies)    



def reader(path):
    with open(path, "r+") as read:
     return int(read.read())

     

def writer(path, value):
    with open(path, "w") as data:          
           data.write(str(value))


currentPlayer = lambda player: "Игрок 1" if player else "Игрок 2" 

def userRequest(candies):
    limit = 28
    if candies < limit:
        limit = candies  
    try:
        requestUserCandies = int(input("Какое количество конфеты вы хотите забрать: "))
        while 1 > requestUserCandies  or requestUserCandies > limit:            
            print(f"Общие количество конфет уменьшилось до {candies}") if requestUserCandies > limit < 28 else "" 
            requestUserCandies = int(input("Какое количество конфеты вы хотите забрать: "))
    except:
        print(f"Значение дожлны быть число от 1 до {limit}.")
        requestUserCandies = int(input("Какое колличество конфеты вы хотите забрать: "))  
    return requestUserCandies



def lottery():  
    player = random.choice([True, False])   
    print(f"В результате жеребьевки первый ход делает Игрок # 1") if  player else print(f"В результате жеребьевки первый ход делает Игрок # 2")
    return player   


def step(candies, pathCandies, pathPlayer, player): 
    playerCandies = reader(pathPlayer)
    requestUserCandies = userRequest(candies)
    playerCandies += requestUserCandies
    candies -= requestUserCandies
    writer(pathCandies,candies)
    writer(pathPlayer, playerCandies )     
    print(f"Количество конфет у {currentPlayer(player)}: {playerCandies}, всего конфет осталось {candies}" )     
    return candies


def game( pathCandies, pathPlayer1, pathPlayer2 ):
    init_game( pathCandies, pathPlayer1, pathPlayer2 )
    candies = reader(pathCandies) 
    player = lottery()    
    while candies > 0:
        if player:
            print("Ход игорка №1")
            step(candies, pathCandies, pathPlayer1, player ) 
            candies = reader(pathCandies)            
            if not candies:                        
                return print (f"Победил игорк {currentPlayer(player)} сделав последний ход")                          
            player = False  
        else: 
            print("Ход игорка №2")
            step(candies,pathCandies, pathPlayer2, player) 
            candies = reader(pathCandies) 
            if not candies:                        
                return print (f"Победил игорк {currentPlayer(player)} сделав последний ход") 
            player = True 
    print(candies) 


game(pathCandies, pathPlayer1, pathPlayer2)