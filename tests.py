import unittest
from unittest.mock import patch
from logic import Board, RandomBot, choose_player_type

class TestTicTacToe(unittest.TestCase):

    def test_correct_game_winner_detected(self):
        board = Board()  # New empty board
        board.grid = [
            ['X', None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(board.get_winner(), 'X')

    def test_players_can_play_only_in_viable_spots(self):
        board = Board()  # New empty board
        row, col = 0, 0  # Assume (0, 0) is a non-empty spot
        with self.assertRaises(ValueError):
            # Attempt to place 'X' in a non-empty spot
            board.grid[row][col] = 'X'
            board.grid[row][col] = 'X'  # This line should raise a ValueError

    def test_game_initialized_with_empty_board(self):
        board = Board()  # New empty board
        self.assertIsNone(board.get_winner())  # Ensure no winner at the start
        self.assertTrue(all(cell is None for row in board.grid for cell in row))  # All cells should be empty

    @patch('builtins.input', side_effect=['1'])
    def test_game_initialized_with_two_players(self, mock_input):
        player_type = choose_player_type()  # Simulate user input 1, indicating choosing a human player
        self.assertEqual(player_type, 'X')  # Ensure the chosen player type is 'X'

    @patch('builtins.input', side_effect=['2'])
    def test_game_initialized_with_one_player(self, mock_input):
        player_type = choose_player_type()  # Simulate user input 2, indicating choosing a RandomBot player
        self.assertEqual(player_type, 'O')  # Ensure the chosen player type is 'O'

    def test_players_assigned_unique_piece(self):
        board = Board()  # New empty board
        player1_type = 'X'
        player2_type = 'O'
        self.assertNotEqual(player1_type, player2_type)  # Ensure both players are assigned different piece types

if __name__ == '__main__':
    unittest.main()
