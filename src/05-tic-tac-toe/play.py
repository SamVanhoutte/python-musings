import board as brd
from math import inf as infinity
import random

def __player_turn(board: brd.Board):
    set_field = input('Enter the number of the field you want to play?[1:' + str(board.size**2) + ']')
    print('field id', set_field)
    if(set_field!=''):
        board.player_set(int(set_field))

# def negamax(board_state: brd.Board, depth: int, is_human_turn: bool, loop_count = 0):
#     if not(is_human_turn): #computers turn
#         best = [-1, -1, -infinity, loop_count]
#     else:
#         best = [-1, -1, +infinity, loop_count]

#     if depth == 0:
#         #move_evaluation = board_state.evaluate_move(x, y, is_human_turn)
#         game_over, score = board_state.check_game_finished(is_human_turn)
#         return [-1, -1, (score if not(is_human_turn) else -score), loop_count]

#     highScore = -100

#     for cell in board_state.get_empty_cells():
#         # Try and set all combinations
#         x, y = cell[0], cell[1]
#         # Simulate the next available move 
#         board_state.set_cell(x, y, is_human_turn)
#         #move_evaluation = board_state.evaluate_move(x, y, is_human_turn)
#         # recurse the function with the board and the new state set
#         loop_count+=1
#         # we get the score of this move and all possible combinations after that
#         megamax_move = negamax(board_state, depth - 1, not(is_human_turn))
#         megamax_move[2] = -megamax_move[2]  #change sign (nega!)
#         # Undo the move, to reset the board to the actual state
#         board_state.free_cell(x, y)
#         megamax_move[0], megamax_move[1] = x, y

#         #highScore = max(megamax_move[2], highScore)
#         if(megamax_move[2] > highScore):
#             best = megamax_move

#     return best

def negamax(board_state: brd.Board, depth: int, is_human_turn: bool):
    # if not(is_human_turn): #computers turn
    #     best = [-1, -1, -infinity]
    # else:
    #     best = [-1, -1, +infinity]

    best = [None, None, -infinity]
    # we have arrived at a simulated state where the game is done, or the last available cell was reached
    # now returning the score of this final move
    # game_over, score = board_state.check_game_finished(is_human_turn)
    if (depth==0 or board_state.board_full()):
        #if depth == 0 or game_over:
        _, score = board_state.check_game_finished(is_human_turn)
        return [None, None, score]
        #return [-1, -1, score]

    # Loop all available cells, if we are here
    for cell in board_state.get_empty_cells():
        # Try and set all combinations
        x, y = cell[0], cell[1]
        # Simulate the next available move 
        board_state.set_cell(x, y, is_human_turn)
        # recurse the function with the board and the new state set
        negamax_move = negamax(board_state, depth - 1, not(is_human_turn))
        # we get the score of this move and all possible combinations after that

        # Undo the move, to reset the board to the actual state
        board_state.free_cell(x, y)
        # We will return a list with the row, col and score, so we're setting row & col here
        negamax_move[0], negamax_move[1], negamax_move[2] = x, y, -negamax_move[2]

        if(negamax_move[2] > best[2]):
            best = negamax_move

        # if not(is_human_turn):
        #     # pick the max score/move when computers turn
        #     if minimax_move[2] > best[2]:
        #         best = minimax_move  # max value
        # else:
        #     # pick the lowest score/move when players turn
        #     if minimax_move[2] < best[2]:
        #         best = minimax_move  # min value
    # print ('Nega max depth', depth, ' - ishuman: ', is_human_turn , '- score: ', best)
    return best


def minimax(board_state: brd.Board, depth: int, is_human_turn: bool, loop_count = 0):
    if not(is_human_turn): #computers turn
        best = [-1, -1, -infinity, loop_count]
    else:
        best = [-1, -1, +infinity, loop_count]

    # we have arrived at a simulated state where the game is done, or the last available cell was reached
    # now returning the score of this final move
    game_over, score = board_state.check_game_finished(is_human_turn)
    if depth == 0 or game_over:
        return [-1, -1, score, loop_count]

    # Loop all available cells, if we are here
    for cell in board_state.get_empty_cells():
        # Try and set all combinations
        x, y = cell[0], cell[1]
        # Simulate the next available move 
        board_state.set_cell(x, y, is_human_turn)
        # recurse the function with the board and the new state set
        loop_count+=1
        minimax_move = minimax(board_state, depth - 1, not(is_human_turn), loop_count)
        loop_count = minimax_move[3]
        # we get the score of this move and all possible combinations after that

        # Undo the move, to reset the board to the actual state
        board_state.free_cell(x, y)
        # We will return a list with the row, col and score, so we're setting row & col here
        minimax_move[0], minimax_move[1] = x, y

        if not(is_human_turn):
            # pick the max score/move when computers turn
            if minimax_move[2] > best[2]:
                best = minimax_move  # max value
        else:
            # pick the lowest score/move when players turn
            if minimax_move[2] < best[2]:
                best = minimax_move  # min value
    return best
    
def __computer_turn(board: brd.Board):
    depth = len(board.get_empty_cells())
    game_over, score = board.check_game_finished(False)
    if depth == 0 or game_over:
        return

    if depth == board.size**2: # when a new board is started (first move), pick random
        x = random.randint(0,board.size-1)
        y = random.randint(0,board.size-1)
    else:
        move = negamax(board, depth, False)
        x, y = move[0], move[1]

    print('Computer decided for following move:', x, '-', y)
    board.set_cell(x, y, False)
        
def main():
    board = brd.Board(3)
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