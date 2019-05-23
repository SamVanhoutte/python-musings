from random import shuffle
import numpy as np
import math
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

    def evaluate(self, evaluation_method: str = 'fair'):
        if(evaluation_method=='good'):
            return self.__evaluate_nilsson_sequence()
        elif(evaluation_method=='fair'):
            return self.__evaluate_manhattan()
        elif(evaluation_method=='weak'):
            return self.__evaluate_hamming()
        elif(evaluation_method=='bad'):
            return self.__evaluate_opposites()

    def __evaluate_manhattan(self):
        sum = 0
        for row in range(0, 3):
            for col in range(0, 3):
                tile = self.board[row][col]
                if(tile>0):
                    for m in range(0, 3):
                        for n in range(0, 3):
                            if tile == self.__goal[m][n]:
                                sum += abs(row-m) + abs(col-n)
        return sum

    def __evaluate_nilsson_sequence(self):
        # inspired by the answer here: https://cs.stackexchange.com/questions/1904/nilssons-sequence-score-for-8-puzzle-problem-in-a-algorithm?rq=1
        # if the empty box is not in the middle, start with cost 1
        total_score = 0 if self.board[1][1]==0 else 1 
        # add manhattan distance cost
        distance_cost = self.__evaluate_manhattan()
        # successors
        successor_cost = 0
        goal_pairs = list([[1,2],[2,3],[3,5],[5,8],[8,7],[7,6],[6,4],[4,1]])
        if([self.board[0][0],self.board[0][1]] not in goal_pairs): successor_cost+=1
        if([self.board[0][1],self.board[0][2]] not in goal_pairs): successor_cost+=1
        if([self.board[0][2],self.board[1][2]] not in goal_pairs): successor_cost+=1
        if([self.board[1][2],self.board[2][2]] not in goal_pairs): successor_cost+=1
        if([self.board[2][2],self.board[2][1]] not in goal_pairs): successor_cost+=1
        if([self.board[2][1],self.board[2][0]] not in goal_pairs): successor_cost+=1
        if([self.board[2][0],self.board[1][0]] not in goal_pairs): successor_cost+=1
        return distance_cost + 3 * (total_score + 2*successor_cost)
    
    def __evaluate_hamming(self):
        sum = 0
        for row in range(0, 3):
            for col in range(0, 3):
                tile = self.board[row][col]
                if(tile!=self.__goal[row][col]):
                    sum += 1
        return sum

    def __evaluate_opposites(self):
        sum = 0
        sum += abs(self.board[0][0] - self.board[2][2])
        sum += abs(self.board[0][1] - self.board[2][1])
        sum += abs(self.board[0][2] - self.board[2][0])
        sum += abs(self.board[1][0] - self.board[1][2])
        return abs(16-sum)
