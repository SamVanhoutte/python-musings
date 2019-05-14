import board as brd
from math import inf as infinity
import random

def player_turn(board: brd.Board):
    set_field = input('Enter the number of the field you want to play?[1:' + str(board.size**2) + ']')
    print('field id', set_field)
    if(set_field!=''):
        board.player_set(int(set_field))

def minimax(board_state: brd.Board, depth: int, is_human_turn: bool):
    if not(is_human_turn): #computers turn
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    game_over, score = board_state.check_game_finished(is_human_turn)
    if depth == 0 or game_over:
        return [-1, -1, score]

    # Loop all available cells
    for cell in board_state.get_empty_cells():
        # Try and set all combinations
        x, y = cell[0], cell[1]
        board_state.set_cell(x, y, is_human_turn)
        score = minimax(board_state, depth - 1, not(is_human_turn))
        # Undo the move
        board_state.free_cell(x, y)
        score[0], score[1] = x, y

        if not(is_human_turn):
            # pick the max score/move when computers turn
            if score[2] > best[2]:
                best = score  # max value
        else:
            # pick the lowest score/move when players turn
            if score[2] < best[2]:
                best = score  # min value
    #print('minimax - depth', depth, 'is-human:', is_human_turn, 'result:', best[0], best[1])
    return best

def computer_turn(board: brd.Board):
    depth = len(board.get_empty_cells())
    game_over, score = board.check_game_finished(False)
    if depth == 0 or game_over:
        return

    if depth == board.size**2: # when a new board is started (first move), pick random
        x = random.randint(0,board.size-1)
        y = random.randint(0,board.size-1)
    else:
        move = minimax(board, depth, False)
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
    while not(board.board_full()) and not(board.someone_won(not(is_humans_turn))):  #reversing the is_humans_turn, because we want to check the previous turn
        if is_humans_turn:
            player_turn(board)
        else:
            computer_turn(board)
        is_humans_turn = not(is_humans_turn)
        board.render()

    if(board.someone_won(True)):
        print("The player won !!! Congratulations")
    elif(board.someone_won(False)):
        print("The computer won !!! He's too strong")
    elif(board.board_full()):
        print("It's a draw !")

if __name__ == "__main__": main()