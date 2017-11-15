'''
First attempt at tactical engine
For this I will be using the simple game tic-tac-toe. The board will be
represented by a 2D array, with empty spaces stored as 0, x stored as 1
and o stored as 2
Bennet Montgomery
2017-11-12
'''

import random


'''
Novice() function takes the current boardState and returns adjusted boardState with move in place.
Moves are chosen randomly, the most simple tactical AI.
'''
def novice(boardState):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    #if the chosen spot already has an x or o
    if boardState[x][y] != 0:
        return novice(boardState)
    
    boardState[x][y] = 2
    return boardState

'''
Intermediate() function take the current boardState and returns adjusted boardState with move in place.
If the AI notices a potential loss or win in the next turn, it blocks or takes it. Otherwise, it plays
randomly.
'''
def intermediate(boardState):
    #the AI will now prioritize winning over blocking - 2017-11-14
    '''
    Cases where the AI wins this turn:
    '''
    for i in range(len(boardState)):
        if boardState[i] == [0, 2, 2]:
            boardState[i][0] = 2
            return boardState
        if boardState[i] == [2, 0, 2]:
            boardState[i][1] = 2
            return boardState
        if boardState[i] == [2, 2, 0]:
            boardState[i][2] = 2

    for i in range(len(boardState[0])):
        if boardState[0][i] == boardState[1][i] and boardState[2][i] == 0 and boardState[0][i] == 2:
            boardState[2][i] = 2
            return boardState
        if boardState[0][i] == boardState[2][i] and boardState[1][i] == 0 and boardState[0][i] == 2:
            boardState[1][i] = 2
            return boardState
        if boardState[1][i] == boardState[2][i] and boardState[0][i] == 0 and boardState[1][i] == 2:
            boardState[0][i]= 2
            return boardState

    if boardState[0][0] == boardState[1][1] and boardState[2][2] == 0 and boardState[0][0] == 2:
        boardState[2][2] = 2
        return boardState

    if boardState[0][0] == boardState[2][2] and boardState[1][1] == 0 and boardState[0][0] == 2:
        boardState[1][1] = 2
        return boardState

    if boardState[1][1] == boardState[2][2] and boardState[0][0] == 0 and boardState[1][1] == 2:
        boardState[0][0] = 2
        return boardState

    if boardState[0][2] == boardState[1][1] and boardState[2][0] == 0 and boardState[0][2] == 2:
        boardState[2][0] = 2
        return boardState

    if boardState[0][2] == boardState[2][0] and boardState[1][1] == 0 and boardState[0][2] == 2:
        boardState[1][1] = 2
        return boardState

    if boardState[1][1] == boardState[2][0] and boardState[0][2] == 0 and boardState[1][1] == 2:
        boardState[0][2] = 2
        return boardState

    '''
    Cases where the AI loses this turn:
    '''
    for i in range(len(boardState)):
        if  boardState[i] == [0, 1, 1]:
            boardState[i][0] = 2
            return boardState
        if boardState[i] == [1, 0, 1]:
            boardState[i][1] = 2
            return boardState
        if boardState[i] == [1, 1, 0]:
            boardState[i][2] = 2
            return boardState

    for i in range(len(boardState[0])):
        if boardState[0][i] == boardState[1][i] and boardState[2][i] == 0 and boardState[0][i] == 1:
            boardState[2][i] = 2
            return boardState
        if boardState[0][i] == boardState[2][i] and boardState[1][i] == 0 and boardState[0][i] == 1:
            boardState[1][i] = 2
            return boardState
        if boardState[1][i] == boardState[2][i] and boardState[0][i] == 0 and boardState[0][i] == 1:
            boardState[0][i]= 2
            return boardState

    if boardState[0][0] == boardState[1][1] and boardState[2][2] == 0 and boardState[0][0] == 1:
        boardState[2][2] = 2
        return boardState

    if boardState[0][0] == boardState[2][2] and boardState[1][1] == 0 and boardState[0][0] == 1:
        boardState[1][1] = 2
        return boardState

    if boardState[1][1] == boardState[2][2] and boardState[0][0] == 0 and boardState[1][1] == 1:
        boardState[0][0] = 2
        return boardState

    if boardState[0][2] == boardState[1][1] and boardState[2][0] == 0 and boardState[0][2] == 1:
        boardState[2][0] = 2
        return boardState

    if boardState[0][2] == boardState[2][0] and boardState[1][1] == 0 and boardState[0][2] == 1:
        boardState[1][1] = 2
        return boardState

    if boardState[1][1] == boardState[2][0] and boardState[0][2] == 0 and boardState[1][1] == 1:
        boardState[0][2] = 2
        return boardState
            
    return novice(boardState)

'''
Expert() function takes the current boardState and return adjusted boardState with move in place.
Expert AI always makes the ideal opening move. If the player's first move is a corner, the computer
plays the centre, if the player plays the centre, the computer plays the top left corner. If the player
plays an edge, the AI plays the centre.
'''
def expert(boardStatus, opening):
    if boardStatus[1][1] == 1 and opening:
        boardStatus[0][0] = 2
        return boardStatus
    elif opening:
        boardStatus[1][1] = 2
        return boardStatus

    return intermediate(boardStatus)
        

def getAIMove(ai, boardState, opening):
    if ai == 'novice':
        return novice(boardState)
    elif ai == 'intermediate':
        return intermediate(boardState)
    else:
        return expert(boardState, opening)

'''
GameWon() checks if the game has been won by either player
'''
def checkWin(boardState):
    for i in range(len(boardState)):
        if boardState[i] == [1, 1, 1] or boardState[i] == [2, 2, 2]:
            return True

    for i in range(len(boardState[0])):
        if boardState[0][i] == boardState[1][i] and boardState[0][i] == boardState[2][i] and boardState[0][i] != 0:
            return True

    if boardState[0][0] == boardState[1][1] and boardState[0][0] == boardState[2][2] and boardState[0][0] != 0:
        return True

    if boardState[0][2] == boardState[1][1] and boardState[0][2] == boardState[2][0] and boardState[0][2] != 0:
        return True

    #if the board is full:
    full = True
    for i in range(len(boardState)):
        for j in range(len(boardState[i])):
            if boardState[i][j] == 0:
                full = False

    return False or full

'''
PrintBoard() prints the current state of the board, substituting 0, 1, and 2
for -, x, and o respectively
'''
def printBoard(boardState):
    for i in range(len(boardState)):
        lineString = ''
        for j in range(len(boardState[i])):
            if boardState[i][j] == 0:
                lineString += '-'
            elif boardState[i][j] == 1:
                lineString += 'x'
            else:
                lineString += 'o'

        print(lineString)

    print('')
    
'''
GetMove() prompts for input from a human user
'''
def getMove(boardState):
    row = int(input('row: '))
    column = int(input('column: '))
    if row in [0, 1, 2] and column in [0, 1, 2] and boardState[row][column] == 0:
        boardState[row][column] = 1
    else:
        return getMove(boardState)

    return boardState

'''
Game loop
'''
def game(ai):
    gameWon = False
    boardState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    opening = True
    
    while not gameWon:
        boardState = getMove(boardState)
        gameWon = checkWin(boardState)
        printBoard(boardState)
        if gameWon:
            break
        
        boardState = getAIMove(ai, boardState, opening)
        opening = False
        gameWon = checkWin(boardState)
        printBoard(boardState)

'''
main() function prompts user for diffiulty setting and starts the game loop
'''
def main():
    difficulty = input('difficulty: ')
    if difficulty == 'novice':
        game('novice')
    elif difficulty == 'intermediate':
        game('intermediate')
    elif difficulty == 'expert':
        game('expert')
    else:
        main()

if __name__ == '__main__':main()
