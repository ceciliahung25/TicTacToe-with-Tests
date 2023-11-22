import unittest
from unittest.mock import patch
from logic import Board, RandomBot, choose_player_type

class TestTicTacToe(unittest.TestCase):

    def test_correct_game_winner_detected(self):
        board = Board()
        # Set up a winning scenario
        board.grid = [
            ['X', 'O', 'X'],
            [None, 'O', None],
            ['O', None, 'X'],
        ]
        print(board.get_winner())  # Add this line to debug
        self.assertEqual(board.get_winner(), 'X')

    @patch('builtins.input', side_effect=['1'])
    def test_players_can_play_only_in_viable_spots(self, mock_input):
        board = Board()
        player = choose_player_type()
        row, col = 0, 0
        board.grid[row][col] = 'X'
        print(board.grid)  # Add this line to debug
        # Ensure the following line raises a ValueError
        with self.assertRaises(ValueError):
            board.grid[row][col] = player

if __name__ == '__main__':
    unittest.main()
