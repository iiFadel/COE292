"""
Tic Tac Toe Player
"""


import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xTurn=0
    oTurn=0
    for row in range(3):
        for col in range(3):
            if board[row][col]== X:
                xTurn+=1
            elif board[row][col]== O:
                oTurn+=1
    if board == initial_state():
        return X
    elif xTurn>oTurn:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions= set()

    for i in range(3):
        for j in range(3):
            if board[i][j]== EMPTY:
                possibleActions.add((i,j))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NameError("The action you have taken is invalid")
    if board[action[0]][action[1]]!= EMPTY:
        raise NameError("The action you have taken is invalid")

    newBoard= copy.deepcopy(board)
    newBoard[action[0]][action[1]]= player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Horizontally
    for i in range(3):
        if (board[i][0]== O) and (board[i][1]== O) and (board[i][2]== O):
            return O
        elif (board[i][0]== X) and (board[i][1]== X) and (board[i][2]== X):
            return X

    #Vertically
    for j in range(3):
        if (board[0][j]== O) and (board[1][j]== O) and (board[2][j]== O):
            return O
        elif (board[0][j]== X) and (board[1][j]== X) and (board[2][j]== X):
            return X

    #Diagonally
    if (board[0][0] == O) and (board[1][1] == O) and (board[2][2] == O):
        return O
    if (board[0][0] == X) and (board[1][1] == X) and (board[2][2] == X):
        return X

    if (board[2][0]== O) and (board[1][1]== O) and (board[0][2]== O):
        return O
    if (board[2][0]== X) and (board[1][1]== X) and (board[0][2]== X):
        return X

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)== X) or (winner(board)== O):
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board)== True:
        return None

    if player(board)== X:
        finalMaxValue= maxValue(board)
        action= finalMaxValue[1]
        return action
    else:
        finalMinValue = minValue(board)
        action = finalMinValue[1]
        return action

def maxValue(board):
    actionTaken=None
    value= float('-inf')

    if terminal(board)== True:
        return list((utility(board), None))

    for action in actions(board):
        minVal= minValue(result(board,action))
        if minVal[0]>value:
            value= minVal[0]
            actionTaken=action
            if value==1:
                return list((value,actionTaken))

    return list((value, actionTaken))

def minValue(board):
    actionTaken= None
    value = float('inf')

    if terminal(board) == True:
        return list((utility(board), None))

    for action in actions(board):
        maxVal = maxValue(result(board, action))
        if maxVal[0] < value:
            value = maxVal[0]
            actionTaken = action
            if value == -1:
                return list((value, actionTaken))

    return list((value, actionTaken))
