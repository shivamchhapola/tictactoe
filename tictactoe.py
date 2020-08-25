import random
turn = 1 # 1 means turn of player X and 0 means turn of player O
board = ["   "]*10 # list of empty spaces in board the number 0 is not used so the total number of cell is 9
players = [" O ", " X "] #List of players
ai = True #is the game played against AI
player = 1 #if player is 0 the Player goes first and if the player is 1 the Ai goes first

def drawBoard(): # this function prints an ugly board in terminal
    print(board[1]+"|"+board[2]+"|"+board[3]) # board[int] displays whatever there is in the cell, it might be empty, it might have "X" or it might have "O"
    print("-----------")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-----------")
    print(board[7]+"|"+board[8]+"|"+board[9])

def getInput(): # to get a valid player input
    inputKey = input("Enter a valid move(1 to 9): ")
    while not (inputKey.isdigit() and int(inputKey) <= 9 and int(inputKey) != 0 and board[int(inputKey)] == "   "):
        inputKey = input("Enter a valid move(1 to 9): ")    #this loop eliminates only when player input is a number between 1 to 9 and only if the cell is empty, so, let's say if player enters "12" or any alphabet the loop will again ask for input again as they are not in-between 1 to 9 and if the player inputs a number between 1 to 9 the loop terminates. Mind well the loop does not start if the player inputs a number between 1 to 9 in the first trial, this helps to optimize the code.
    inputKey = int(inputKey) #it converts the input string to integer
    return inputKey

def isWinner(player): #checks if any player has won the game or not
    if (board[1] == player and board[2] == player and board[3] == player) or (board[4] == player and board[5] == player and board[6] == player) or (board[7] == player and board[8] == player and board[9] == player): # checks horizontally wins
        return True
        #if there are Xs or Os in a horizontal line, it'll return true
        #example
        #  X | X | X
        #  ---------
        #  O |   | O
        #  ---------
        #    |   |  
    elif (board[1] == player and board[5] == player and board[9] == player) or (board[7] == player and board[5] == player and board[3] == player): # checks diagonals wins
        return True
        #if there are Xs or Os in a Diagonal line, it'll return true
        #example
        #  X |   |  
        #  ---------
        #  O | X | O
        #  ---------
        #    |   | X
    elif (board[1] == player and board[4] == player and board[7] == player) or (board[2] == player and board[5] == player and board[8] == player) or (board[9] == player and board[6] == player and board[3] == player): # checks vertical wins
        return True
         #example
        #    | X |  
        #  ---------
        #  O | X | O
        #  ---------
        #    | X |  
    else:
        return False

def makeMove(inputKey, board): # this function replaces an empty cell with a valid player move
    if turn == 1: #replaces the player input integer with "X"
        board[inputKey] = players[turn]
    elif turn == 0 and not ai: #replaces the player input integer with "O" when game is in 2 Player Mode
        board[inputKey] = players[turn]
    elif turn == 0 and ai:
        board[aiMove(board)] = players[turn]

def aiMove(board):
    dupeboard = board.copy()
    for i in range(1,10):
        if dupeboard[i] == "   ":
            makeMove(i, dupeboard)
            if isWinner(" O "):
                return i
    for i in range(1,10):
        if dupeboard[i] == "   ":
            makeMove(i, dupeboard)
            if isWinner(" X "):
                return i
    for i in [1,3,5,7,9]:
        if dupeboard[i] == "   ":
            return i
    for i in [2,4,6,8]:
        if dupeboard[i] == "   ":
            return i   # Why I created multiple loops is a little hard to explain in text so, call me, I'll explain you on call.


while True: # main gameloop
    if turn == 1:
        drawBoard()
        inputKey = 0 
        inputKey = getInput()
        makeMove(inputKey,board)
        turn = 0
    elif turn == 0:
        inputKey = 0
        makeMove(inputKey,board)
        drawBoard()
        input("Press Enter to Continue")
        turn = 1
    if isWinner(" X "): #if "X wins the game it'll display a message and will break the main game loop so, the game closes"
        drawBoard()
        print("X won")
        input("Press Enter to End Game") #it'll diaplay a message "X won" and will wait till the player enters any key to stop the game
        break
    elif isWinner(" O "):
        drawBoard()
        print("O won")
        input("Press Enter to End Game")
        break