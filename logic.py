import random

class Board:
    def __init__(self):
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def make_empty_board(self):
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def other_player(self, player):
        return 'O' if player == 'X' else 'X'

    def make_move(self, player, row, col):
        if self.grid[row][col] is not None:
            raise ValueError("Selected spot is already occupied")
        self.grid[row][col] = player

    def get_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            # Check rows
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] is not None:
                print(f"Winner in row {i}")
                return self.grid[i][0]
    
            # Check columns
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] is not None:
                print(f"Winner in column {i}")
                return self.grid[0][i]
    
        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
            print("Winner in top-left to bottom-right diagonal")
            return self.grid[0][0]
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
            print("Winner in top-right to bottom-left diagonal")
            return self.grid[0][2]
    
        print("No winner yet. Current board state:")
        for row in self.grid:
            print(row)
    
        return None


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
