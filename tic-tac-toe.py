#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def markBoard(position, mark):
    if board[position] == ' ':
        board[position] = mark



def printBoard():
    drawBoard = {
        1: ' ',
        2: ' ',
        3: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        7: ' ',
        8: ' ',
        9: ' '
    }

    for x in drawBoard.keys():
        if board[x] == ' ':
           drawBoard[x] = x 
        else:
            drawBoard[x] = board[x]

    print(
        '\n' +
        str(drawBoard[1]) + ' | '  +  str(drawBoard[2]) + ' | '  +  str(drawBoard[3]) + ' \n '  + 

        '-------- \n' +

        str(drawBoard[4]) + ' | '  +  str(drawBoard[5]) + ' | '  +  str(drawBoard[6]) + ' \n '  + 

        '-------- \n' +

        str(drawBoard[7]) + ' | '  +  str(drawBoard[8]) + ' | '  +  str(drawBoard[9]) + ' \n ' 

    )


def validateMove(position):
    try:
        position = int(position)
        if 1 <= position <= 9 and board[position] == ' ':
            return True
    except ValueError:
        pass
    return False


winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [3, 5, 7],
    [1, 5, 9]

]

def checkWin(player):
    for combination in winCombinations:
        if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player: 
            return True

    return False

def checkFull():
    for x in board:
        if board[x] == ' ':
            return False

    return True

def playGame():
    gameEnded = False
    currentTurnPlayer = 'X'

    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')

    while not gameEnded:
        move = input(currentTurnPlayer + "'s turn, input: ")
        while not validateMove(move):
            print('Input is invalid, please enter a value between 1-9')
            move = input(currentTurnPlayer + "'s turn, input: ")
        markBoard(int(move), currentTurnPlayer)
        printBoard()

        if checkWin(currentTurnPlayer):
            print('Congratulations, winner is {}. Game over!'.format(currentTurnPlayer))
            gameEnded = True

        elif checkFull():
            print('Game is tied.')
            gameEnded = True

        else:
            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            else:
                currentTurnPlayer = 'X'
    return gameEnded

playGame()

quitGame = False
while not quitGame:
    restartGame = input('Start another round of Tic-Tac-Toe? Yes or No? ')
    if restartGame.lower() == 'yes':
        board = {
            1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '
        }
        gameEnded = playGame()
        if gameEnded:
            continue
    else:
        print('Game ends.')
        quitGame = True
