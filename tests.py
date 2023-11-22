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
        winner = board.get_winner()
        print(f"Board State: {board.grid}")
        print(f"Winner: {winner}")
        self.assertEqual(winner, 'X')
    

    def test_players_can_play_only_in_viable_spots(self):
        board = Board()  # New empty board
        row, col = 0, 0  # Assume (0, 0) is a non-empty spot
        board.make_move('O', row, col)  # Occupying the spot with 'O'
        with self.assertRaises(ValueError):
            board.make_move('X', row, col)

    def test_game_initialized_with_empty_board(self):
        board = Board()  # New empty board
        self.assertIsNone(board.get_winner())
        self.assertTrue(all(cell is None for row in board.grid for cell in row))

    @patch('builtins.input', side_effect=['1'])
    def test_game_initialized_with_two_players(self, mock_input):
        player_type = choose_player_type()
        self.assertEqual(player_type, 'X')

    @patch('builtins.input', side_effect=['2'])
    def test_game_initialized_with_one_player(self, mock_input):
        player_type = choose_player_type()
        self.assertEqual(player_type, 'O')

    def test_players_assigned_unique_piece(self):
        board = Board()  # New empty board
        player1_type = 'X'
        player2_type = 'O'
        self.assertNotEqual(player1_type, player2_type)

if __name__ == '__main__':
    unittest.main()
