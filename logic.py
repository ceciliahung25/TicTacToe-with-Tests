import random

class Board:
    def __init__(self):
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def make_move(self, player, row, col):
        if self.grid[row][col] is not None:
            raise ValueError("The selected spot is already occupied.")
        self.grid[row][col] = player

    def get_winner(self):
        # Check rows
        for row in self.grid:
            if self.check_line(row):
                return row[0]

        # Check columns
        for col in range(3):
            if self.check_line([self.grid[row][col] for row in range(3)]):
                return self.grid[0][col]

        # Check diagonals
        if self.check_line([self.grid[i][i] for i in range(3)]):
            return self.grid[0][0]
        elif self.check_line([self.grid[i][2 - i] for i in range(3)]):
            return self.grid[0][2]

        return None

    def check_line(self, line):
        return all(cell == line[0] and cell is not None for cell in line) and line[0] is not None

    def get_empty_squares(self):
        return [(i, j) for i in range(3) for j in range(3) if self.grid[i][j] is None]

class RandomBot:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        available_squares = board.get_empty_squares()
        return random.choice(available_squares) if available_squares else None

def choose_player_type():
    while True:
        choice = input("Choose player type (1 for Human, 2 for RandomBot): ")
        if choice == '1':
            return 'X'
        elif choice == '2':
            return 'O'
        else:
            print("Invalid choice. Please enter 1 or 2.")
