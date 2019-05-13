import board as brd

def player_turn(board):
    set_field = input('Enter the number of the field you want to play?[1:' + str(board.size**2) + ']')
    print('field id', set_field)
    if(set_field!=''):
        board.player_set(int(set_field))

def computer_turn(board):
    print('computer turn')
    
def main():
    board = brd.Board(3)
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
    if(board.someone_won(False)):
        print("The computer won !!! He's too strong")
    if(board.board_full()):
        print("It's a draw !")
        
if __name__ == "__main__": main()