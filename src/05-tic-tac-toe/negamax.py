import numpy as np



def moveFind(state):
        """Takes a position as an nparray and determines the legal moves"""
        moveChoices = []

        # Iterate over state, to determine which squares are empty
        it = np.nditer(state, flags=['multi_index'])
        while not it.finished:
            if it[0] == 0:
                    moveChoices.append(it.multi_index)
            it.iternext()
        return moveChoices

def moveSim(state, move, player):
        """Create the state of the player having moved without interfering with the board"""
        simState = state.copy()
        if player == 1:
                simState[move] = 1
        else:
                simState[move] = gamecfg.n + 1
        return simState

def positionScore(state):
        """The game is either won or lost"""
        if winCheck(state) == 'X':
                return 100
        elif winCheck(state) == 'O':
                return -100
        else:
                return 0

def negaMax(state, depth, colour):
        """Recursively find the best move via a negamax search"""
        if depth == 0:
                return positionScore(state) * colour

        highScore = -100

        moveList = moveFind(state)
        for move in moveList:
                score = -negaMax(moveSim(state, move, colour), depth -1, colour * -1)
                highScore = max(score, highScore)

        return highScore


a = np.zeros(9).reshape(3,3)
print(a)
negaMax(a, 6, 1) # Returned zero as it should
negaMax(a, 7, 1) # Returns 100