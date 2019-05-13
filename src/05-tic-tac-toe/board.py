import numpy as np

class Board:
    computer_char = 'X'
    computer_val = 1
    player_char = 'O'
    player_val = -1
    board = [[]]

    def __init__(self, size:int =3):
        self.board = np.zeros(shape=(size, size))
        self.size = size

    def set_state(self, board):
        self.board = board

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
        return (len(self.get_empty_cells())==0)

    def game_over(self):
        if(self.board_full()):
            return True, 0  # Draw, so returning 0 as score
        if(self.someone_won(True)):
            return True, self.player_val  # Player wins, so returning -1 as score
        if(self.someone_won(False)):
            return True, self.computer_val  # Computer wins, so returning 1 as score
        return False, 0

    def get_empty_cells(self):
        cells = []
        
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])

        return cells

    def someone_won(self, is_players_turn: bool):
        # Select value, based on whose turn it is
        value = self.player_val if is_players_turn else self.computer_val
        # First check all rows for sequences of the current value
        for state_row in self.board:
            #at least three occurances in this range, so check further
            if(self.check_range_for_sequence(state_row, value)):
                return True
        # Then check all columns for sequences of the current value
        transposed_state = np.array(self.board).transpose()
        for state_col in transposed_state:
            #at least three occurances in this range, so check further
            if(self.check_range_for_sequence(state_col, value)):
                return True
        # Now Loop all diagonals
        for i in range(self.size):
            # First the diagonals from top-left to down-right (starting in first row)
            diag_range = self.get_diagonal_range(row = 0, col = i, down=True)
            if(self.check_range_for_sequence(diag_range, value)):
                return True
            # Then the diagonals from top-left to down-right (starting in first column)
            if(i > 0): # first cell (0,0) already checked above
                diag_range = self.get_diagonal_range(row = i, col = 0, down=True)
                if(self.check_range_for_sequence(diag_range, value)):
                    return True
            # Then the diagonals from down-left to top-right (starting in last row)
            diag_range = self.get_diagonal_range(row = self.size - 1, col = i, down=False)
            if(self.check_range_for_sequence(diag_range, value)):
                return True
            # Then the diagonals from down-left to top-right (starting in first column)
            if(i > 0): # first cell (last,0) already checked above
                diag_range = self.get_diagonal_range(row = self.size - i, col = 0, down=False)
                if(self.check_range_for_sequence(diag_range, value)):
                    return True
            
        return False

    def get_diagonal_range(self, row: int, col: int, down: bool):
        selected_range = []
        # print('get diagonal', row, col, down)
        if(down): # take diagonals
            while(row < self.size and col < self.size):
                selected_range.append(self.board[row][col])
                row += 1; col += 1
        else:
            while(row >= 0 and col < self.size):
                selected_range.append(self.board[row][col])
                row -= 1; col += 1
        return selected_range

    def check_range_for_sequence(self, check_range, value, length=3):
        # print('Checking existence of the following sequence', check_array)
        for i in range(len(check_range)-(length-1)):
            # todo : should update this, to consider the length variable
            if check_range[i]==value and check_range[i+1]==value and check_range[i+2]==value:
                return True

        return False

    def set_field_by_index(self, field_number, value):
        row = (field_number - 1) // self.size
        col = (field_number - 1) % self.size
        self.board[row][col] = value

    def set_cell(self, row: int, col: int, is_human: bool):
        self.board[row][col] = self.player_val if is_human else self.computer_val

    def free_cell(self, row: int, col: int):
        self.board[row][col] = 0

    def player_set(self, field_number):
        self.set_field_by_index(field_number, self.player_val)

    def computer_set(self, field_number):
        self.set_field_by_index(field_number, self.computer_val)