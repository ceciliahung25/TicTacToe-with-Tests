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
        # Check rows
        for row in self.grid:
            if row.count('X') == 3:
                return 'X'
            elif row.count('O') == 3:
                return 'O'
    
        # Check columns
        for col in range(3):
            column = [self.grid[row][col] for row in range(3)]
            if column.count('X') == 3:
                return 'X'
            elif column.count('O') == 3:
                return 'O'
    
        # Check diagonals
        diagonal1 = [self.grid[i][i] for i in range(3)]
        diagonal2 = [self.grid[i][2 - i] for i in range(3)]
    
        if diagonal1.count('X') == 3:
            return 'X'
        elif diagonal1.count('O') == 3:
            return 'O'
        
        if diagonal2.count('X') == 3:
            return 'X'
        elif diagonal2.count('O') == 3:
            return 'O'
    
        # If no winner, return None
        return None

    def get_empty_squares(self):
        empty_squares = []
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] is None:
                    empty_squares.append((row, col))
        return empty_squares


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
