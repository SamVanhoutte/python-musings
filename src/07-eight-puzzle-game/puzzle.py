from random import shuffle
import numpy as np

class puzzle:
    board = [[]]
    depth = 0

    def __init__(self):
        shuffled_range = [i for i in range(9)]
        shuffle(shuffled_range)
        seq = 0
        self.board = np.zeros((3, 3), int)
        for row in range(0, 3):
            for col in range(0, 3):
                self.board[row][col] = shuffled_range[seq]
                seq += 1

    def set_state(self, board):
        self.board = board
    
    def __str__(self): 
        result = ''
        hor_line = '---------------'
        result = '\n' + hor_line
        for row in self.board:
            for cell in row:
                if (cell!=0):
                    result += '| ' + str(cell) + ' |'
                else:
                    result += '|   |'

            result += '\n' + hor_line
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
                result += str(cell) + '-'
        return result

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
        return (np.array(self.board) == np.array([[1, 2, 3],[4, 0, 5], [6, 7, 8]])).all()

    def move_cell(self,row:int, col:int):
        # check if move is valid
        open_row, open_col = self.get_open_cell()
        self.board[open_row][open_col] = self.board[row][col]
        self.board[row][col] = 0

    def clone(self):
        cloned_puzzle = puzzle()
        cloned_puzzle.set_state(np.copy(self.board))
        cloned_puzzle.depth = self.depth
        return cloned_puzzle

def main():
    puzz = puzzle()
    # puzz.set_state([[1, 2, 3],
    #                 [4, 7, 5],
    #                 [6, 0, 8]])
    print(puzz)

if __name__ == "__main__": main()