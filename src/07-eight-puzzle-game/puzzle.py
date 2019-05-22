from random import shuffle
import numpy as np

class Puzzle:
    board = [[]]
    depth = 0
    __goal = [[1, 2, 3],[4, 0, 5], [6, 7, 8]]

    def __init__(self, signature:str = None):
        self.board = np.zeros((3, 3), int)
        shuffled_range = [i for i in range(9)]
        shuffle(shuffled_range)
        seq = 0
        for row in range(0, 3):
            for col in range(0, 3):
                value_to_set = shuffled_range[seq]
                if(signature != None):
                    # don't use the shuffle, but take the char from the string
                    c = signature[seq]
                    value_to_set = 0 if c == ' ' else int(c)
                self.board[row][col] = value_to_set
                seq += 1

    def set_state(self, board):
        self.board = board
    
    def __str__(self): 
        hor_line = '---------------\n'
        result = ''
        for row in self.board:
            for cell in row:
                if (cell!=0):
                    result += '| ' + str(cell) + ' |'
                else:
                    result += '|   |'

            result += '\n'
        return result
    
            

    def get_open_cell(self):
        for row in range(0, 3):
            for col in range(0, 3):
                if(self.board[row][col]==0):
                    return row, col

    def get_signature(self):
        # return unique string to check if state has been used already
        result = ''
        for row in self.board:
            for cell in row:
                result += str(cell) if cell != 0 else ' '
        return result + ':' + str(self.depth)

    def get_available_moves(self):
        open_row, open_col = self.get_open_cell()
        available_moves = list()
        # check horizontal moves
        if(open_col-1) >= 0:
            available_moves.append((open_row, open_col - 1))
        if(open_col+1) < 3:
            available_moves.append((open_row, open_col + 1))
        # check vertical moves
        if(open_row-1) >= 0:
            available_moves.append((open_row - 1, open_col))
        if(open_row+1) < 3:
            available_moves.append((open_row + 1, open_col))
        return available_moves

    def completed(self):
        return (np.array(self.board) == np.array(self.__goal)).all()

    def move_cell(self,row:int, col:int):
        # check if move is valid
        open_row, open_col = self.get_open_cell()
        self.board[open_row][open_col] = self.board[row][col]
        self.board[row][col] = 0

    def clone(self):
        cloned_puzzle = Puzzle()
        cloned_puzzle.set_state(np.copy(self.board))
        cloned_puzzle.depth = self.depth
        return cloned_puzzle

    def evaluate_manhattan(self):
        sum = 0
        for row in range(0, 3):
            for col in range(0, 3):
                tile = self.board[row][col]
                for m in range(0, 3):
                    for n in range(0, 3):
                        if tile == self.__goal[m][n]:
                            sum += abs(row-m) + abs(col-n)
        return sum
