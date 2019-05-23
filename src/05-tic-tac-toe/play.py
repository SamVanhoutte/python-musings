from board import Board,MoveRecommendation
from math import inf as infinity
import random

def __player_turn(board: Board):
    set_field = input('Enter the number of the field you want to play?[1:' + str(board.size**2) + ']')
    print('field id', set_field)
    if(set_field!=''):
        board.player_set(int(set_field))

def negamax(board_state: Board, depth: int, is_human_turn: bool):
    best = MoveRecommendation(None, None, +infinity if is_human_turn else -infinity, False)

    # we have arrived at a simulated state where the game is done, or the last available cell was reached
    # now returning the score of this final move
    game_over, score = board_state.check_game_finished(is_human_turn)
    if depth == 0 or game_over:
        if(game_over): best.score = score
        return best # MoveRecommendation(-1, -1, score, game_over)

    # Loop all available cells, if we are here
    for cell in board_state.get_empty_cells():
        # Try and set all combinations
        row, col = cell[0], cell[1]
        # Simulate the next available move 
        board_state.set_cell(row, col, is_human_turn)
        # recurse the function with the board and the new state set
        negamax_move = negamax(board_state, depth - 1, not(is_human_turn))
        negamax_move.score = -negamax_move.score

        # we get the score of this move and all possible combinations after that
        # Undo the move, to reset the board to the actual state
        board_state.free_cell(row, col)

        if negamax_move.score > best.score:
            best = negamax_move
            best.column = col
            best.row = row

    return best


def minimax(board_state: Board, depth: int, is_human_turn: bool):
    best = MoveRecommendation(None, None, +infinity if is_human_turn else -infinity, False)

    # we have arrived at a simulated state where the game is done, or the last available cell was reached
    # now returning the score of this final move
    game_over, score = board_state.check_game_finished(is_human_turn)
    if depth == 0 or game_over:
        if(game_over): best.score = score
        return best # MoveRecommendation(-1, -1, score, game_over)

    # Loop all available cells, if we are here
    for cell in board_state.get_empty_cells():
        

        row, col = cell[0], cell[1]
        # Try and set all combinations
        # Simulate the next available move 
        board_state.set_cell(row, col, is_human_turn)
        
        # recurse the function with the board and the new state set
        minimax_move = minimax(board_state, depth - 1, not(is_human_turn))

        # Undo the move, to reset the board to the actual state
        board_state.free_cell(row, col)

        if not(is_human_turn):
            # pick the max score/move when computers turn
            if minimax_move.score > best.score:
                best = minimax_move
                best.column = col
                best.row = row
        else:
            # pick the lowest score/move when players turn
            if minimax_move.score < best.score:
                best = minimax_move
                best.column = col
                best.row = row
    return best
    
def __computer_turn(board: Board):
    depth = len(board.get_empty_cells())
    game_over, score = board.check_game_finished(False)
    if depth == 0 or game_over:
        return

    if depth == board.size**2: # when a new board is started (first move), pick random
        row = random.randint(0,board.size-1)
        column = random.randint(0,board.size-1)
    else:
        move = minimax(board, depth, False)
        row, column = move.row, move.column

    print('Computer decided for following move:', row, '-', column)
    board.set_cell(row, column, False)
        
def main():
    board = Board(3)
    # board.set_state([
    #     [1 ,1 ,-1],
    #     [-1 ,1 ,1],
    #     [0 ,0 ,1]
    # ])
    board.render()

    # check who should start
    is_humans_turn = (input('Player to start first? [y/n]: ').upper()=='Y')

    # Main loop of this game

    while not(board.board_full()) and not(board.check_game_finished(is_humans_turn)[0]):  #reversing the is_humans_turn, because we want to check the previous turn
        if is_humans_turn:
            __player_turn(board)
        else:
            __computer_turn(board)
        is_humans_turn = not(is_humans_turn)
        board.render()

    if(board.player_won()):
        print("The player won !!! Congratulations")
    elif(board.computer_won()):
        print("The computer won !!! He's too strong")
    elif(board.board_full()):
        print("It's a draw !")

if __name__ == "__main__": main()