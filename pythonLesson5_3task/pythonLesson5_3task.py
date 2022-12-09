#Создайте программу для игры в ""Крестики-нолики"".

def printBoard(board):    
    for i in range(3):                
        print("-------------")
        print(f"| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |")

def userStep(board, symbol):
    try:
        userCords = int(input(f"Введите число вместо которго хотит поставить {symbol}: "))
        while (userCords < 1 or userCords > 9):
            userCords = int(input(f"Введите число вместо которго хотит поставить {symbol}: "))
        while board[userCords-1] == ("X" or "O"):
            print("Ячейка занята введите другое число!!!")
            userCords = int(input(f"Введите число вместо которго хотит поставить {symbol}: "))
    except:
        print("Введены не коректные данные")
        userCords = int(input(f"Введите число вместо которго хотит поставить {symbol}: "))      
    board[userCords-1] = symbol
    return board

def winerChek(board):
    winerBoard = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in winerBoard:        
        if board[i[0]] == board[i[1]] == board[i[2]]:
           print(f"Игра окончена победил {board[i[0]]}!!!")
           return False
    return True

def game():
    count = 0
    print("Игра началась.")
    board = [ i for i in range(1,10)]    
    printBoard(board)
    flag = True
    chek = True
    while chek:
        print(count)
        if flag:           
            print("Ходят 'X' ")
            symbol= "X"
            board = userStep(board, symbol)            
            printBoard(board)
            flag = False
            count+=1
        else:
            print("Ходят 'O' ")
            symbol= "O"
            board = userStep(board, symbol)            
            printBoard(board)
            flag = True
            count+=1
        if count > 4:
            chek = winerChek(board)
            if count == 9:
                print("Ничья!")
                chek = False        


                
game()
