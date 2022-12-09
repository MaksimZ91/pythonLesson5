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
    while not board[userCords[0]-1][userCords[1]-1] == ("Z" or symbol):
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
        if tmp[0] == k[0] and tmp[1] == k[1] and tmp[2] == k[2]:
            return False
        elif tmp[3] == k[3] and tmp[4] == k[4] and tmp[5] == k[5]:
            return False
        elif tmp[6] == k[6] and tmp[7] == k[7] and tmp[8] == k[8]:
            return False  
        elif tmp[0] == k[0] and tmp[3] == k[3] and tmp[5] == k[5]:
            return False
        elif tmp[1] == k[1] and tmp[4] == k[4] and tmp[7] == k[7]:
            return False
        elif tmp[2] == k[2] and tmp[5] == k[5] and tmp[8] == k[8]:
            return False  
        elif tmp[0] == k[0] and tmp[4] == k[4] and tmp[8] == k[8]:
            return False  
        elif tmp[2] == k[2] and tmp[4] == k[4] and tmp[6] == k[6]:
            return False                   

      
   
   
 
        

      


    #Выдает True 
    #Три услвия выдачи False 1.Победа Х 2.Победа О 3.Ничья


    return True

winerBoard = ["XXX******", "***XXX***", "******XXX", 
              "X**X**X**", "*X**X**X*", "**X**X**X",
              "X***X***X", "**X*X*X**"]






def game(winerBoard):
    print("Игра началась.")
    board = [["Z"]*3 for i in range(3)]
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
