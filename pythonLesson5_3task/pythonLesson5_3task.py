#Создайте программу для игры в ""Крестики-нолики"".
#Реализовать смену игроков / символов
#Реализовать проверка победы
#Доделать валидацию

def printBoard(board):    
    for i in board:                 
        print("-------------")
        print(f"| {i[0]} | {i[1]} | {i[2]} |")
        



def userStep(board, symbol):
    try:
        userCords = list(map(int,input("Введите координаты через пробел в формате строка - стобец: ").split()))
        while (userCords[0] <= 0 or userCords[0] >= 4) or (userCords[1] <= 0 or userCords[1] >= 4):
          userCords = list(map(int,input("Введите координаты через пробел в формате строка - стобец: ").split()))
    except:
        print("Введены не коректные данные")    
    
    while not board[userCords[0]-1][userCords[1]-1] == ("*" or symbol):
        print("Ячейка занята введите другую координату!!!")
        userCords = list(map(int,input("Введите координаты через пробел в формате строка - стобец: ").split()))
    board[userCords[0]-1][userCords[1]-1] = symbol
    return board

def winerChek(board, winerBoard):
    #Выдает True 
    #Три услвия выдачи False 1.Победа Х 2.Победа О 3.Ничья


    return True

winerBoard = [[("X", "X", "X"),(0, 0, 0),(0, 0, 0)],
              [(0, 0, 0),("X", "X", "X"), (0, 0, 0)],
              [(0, 0, 0),(0, 0, 0),("X", "X", "X")],
              [("X", 0, 0),("X", 0, 0),("X", 0, 0)],
              [(0, "X", 0),(0, "X", 0), (0, "X", 0)],
              [(0, 0, "X"),(0, 0, "X"),(0, 0, "X")],
              [("X", 0, 0),(0, "X", 0), (0, 0, "X")],
              [(0, 0, "X"),(0, "X", 0),("X", 0, 0)],
               ]






def game():
    print("Игра началась.")
    board = [["*"]*3 for i in range(3)]
    printBoard(board)
    flag = True
    chek = winerChek(board, winerBoard)
    while chek:
        if flag:
            symbol= "X"
            board = userStep(board, symbol)
            printBoard(board)
            flag = False
        else:
            symbol= "O"
            board = userStep(board, symbol)
            printBoard(board)
            flag = True


game()
