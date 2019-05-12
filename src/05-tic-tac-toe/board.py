import numpy as np

class Board:
    computer_char = 'X'
    computer_val = -1
    player_char = 'O'
    player_val = 1

    def __init__(self, size=3):
        self.board = np.zeros(shape=(size, size))
        self.size = size

    def clear(self):
        self.board = np.zeros(shape=(self.size, self.size))

    def render(self):
        print('Computer =', self.computer_char, '- Player =', self.player_char)
        chars = {
            self.computer_val: self.computer_char,
            self.player_val: self.player_char,
            0: ' '
        }
        hor_line = '---------------'

        print('\n' + hor_line)
        for row in self.board:
            for cell in row:
                symbol = chars[cell]
                print(f'| {symbol} |', end='')
            print('\n' + hor_line)

    def board_full(self):
        return False

    def someone_won(self):
        return False

    def player_set(self, field_number):
        row = (field_number - 1) // self.size
        col = (field_number - 1) % self.size
        print('player selected row ', row, 'and column', col)
        self.board[row][col] = self.player_val
        return True