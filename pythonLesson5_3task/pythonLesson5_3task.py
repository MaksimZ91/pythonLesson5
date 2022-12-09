#Создайте программу для игры в ""Крестики-нолики"".
#Реализовать проверка победы


def printBoard(board):    
    for i in board:                 
        print("-------------")
        print(f"| {i[0]} | {i[1]} | {i[2]} |")
        



def userStep(board, symbol):
    try:
        userCords = list(map(int,input("Введите координаты через пробел в формате строка - стобец: ").split()))
    except:
        print("Введены не коректные данные")
        userCords = list(map(int,input("Введите координаты через пробел в формате строка - стобец: ").split()))
    while (userCords[0] <= 0 or userCords[0] >= 4) or (userCords[1] <= 0 or userCords[1] >= 4):
        userCords = list(map(int,input("Введите координаты через пробел в формате строка - стобец: ").split()))
    while not board[userCords[0]-1][userCords[1]-1] == ("*" or symbol):
        print("Ячейка занята введите другую координату!!!")
        userCords = list(map(int,input("Введите координаты через пробел в формате строка - стобец: ").split()))
    board[userCords[0]-1][userCords[1]-1] = symbol
    return board

def winerChek(board, winerBoard):
    stringBoard = []
    for i in board:
        for j in i:
            stringBoard.append(j)
    tmp = ""        
    tmp = tmp.join(stringBoard)     
    for k in winerBoard:       
        print(k, tmp)
      
   
   
 
        

      


    #Выдает True 
    #Три услвия выдачи False 1.Победа Х 2.Победа О 3.Ничья


    return True

winerBoard = ["XXX******", "***XXX***", "******XXX", 
              "X**X**X**", "*X**X**X*", "**X**X**X",
              "X***X***X", "**X*X*X**"]






def game(winerBoard):
    print("Игра началась.")
    board = [["*"]*3 for i in range(3)]
    printBoard(board)
    flag = True
    chek = True
    while chek:
        if flag:
            print("Ходят 'X' ")
            symbol= "X"
            board = userStep(board, symbol)
            chek = winerChek(board, winerBoard)
            printBoard(board)
            flag = False
        else:
            print("Ходят 'O' ")
            symbol= "O"
            board = userStep(board, symbol)
            chek = winerChek(board, winerBoard)
            printBoard(board)
            flag = True


game(winerBoard)
