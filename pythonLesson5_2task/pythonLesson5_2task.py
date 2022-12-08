# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

candies = 2021

player_1_papth = "fisrt_player_canides.txt"
player_2_papth = "second_player_candies_.txt"
candies_player_1 = 0
candies_player_2 = 0

def step(path, candies):
    limit = 28
    if candies < limit:
        limit = candies    
    try:
        candie = int(input("Какое колличество конфеты вы хотите забрать: "))
        while 1 > candie or candie > limit:
            print(f"Общие колличество конфет уменьшилось до {candies}") if candie > limit else "" 
            candie = int(input("Какое колличество конфеты вы хотите забрать: "))
    except:
        print("Значение дожлны быть число от 1 до 28.")
        candie = int(input("Какое колличество конфеты вы хотите забрать: "))  
       
    return candie


def lottery():
    player_1 = True
    player_2 = True
    while (player_1 and player_2):
        player_1  = random.choice([True, False])
        player_2  = random.choice([True, False])
    return {"Игрок 1":player_1,"Игрок 2": player_2}  

 





def game():
    candies = 100    
    player1_candies = 0
    player2_candies = 0
    player_1_path = "./pythonLesson5_2task/fisrt_player_canides.txt"
    player_2_path = "./pythonLesson5_2task/second_player_candies.txt"
    players = lottery()
    while candies > 0:     #вынести функционал под if в отдельну функцию или добавить в step
        if players["Игрок 1"]:
            print("Ход игорка №1")
            st = step(player_1_path, candies)
            candies -= st
            player1_candies += st
            players["Игрок 1"] = False            
            print(f"Количество конфет у игорка № 1: {player1_candies}, всего конфет осталось {candies}" )
        else: 
            print("Ход игорка №2")
            st = step(player_2_path, candies)
            candies -= st
            player2_candies += st
            players["Игрок 1"] = True         
            print(f"Количество конфет у игорка № 2: {player2_candies}, всего конфет осталось {candies}" )  
    print(candies)   



game()
